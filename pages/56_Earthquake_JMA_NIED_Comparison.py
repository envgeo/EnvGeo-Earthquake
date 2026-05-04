#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Japan-focused USGS vs JMA/NIED earthquake catalog comparison page.
"""


import pandas as pd
import streamlit as st

import envgeo_utils
import envgeo_earthquake_utils as eq


version = "0.1.0"


def main():
    st.header("EnvGeo-Earthquake")
    st.header(f"JMA / NIED Comparison ({version})")
    st.caption("USGS query results can be compared with uploaded JMA/NIED catalog tables.")
    st.caption("JMA/NIEDデータは自動取得せず、利用者が取得・確認した表データをアップロードして比較します。")

    with st.expander("Data use note / データ利用上の注意", expanded=False):
        st.write("Data source: USGS Earthquake Catalog API (GeoJSON, eventtype=earthquake).")
        eq.render_plate_boundary_note()
        st.write(
            "JMA/NIED catalogs may have provider-specific terms, update timing, registration, "
            "and acknowledgement requirements. Confirm the original provider guidance before use."
        )
        st.markdown(f"- [JMA earthquake information]({eq.JMA_EARTHQUAKE_INFO_URL})")
        st.markdown(f"- [JMA Seismological Bulletin of Japan]({eq.JMA_BULLETIN_URL})")
        st.markdown(f"- [NIED Hi-net data guidance]({eq.NIED_HINET_DATA_URL})")

    st.subheader("Region")
    st.write("Japan and surrounding area")

    query = eq.sidebar_controls(eq.JAPAN_REGION_LABEL)
    df_eq = eq.fetch_earthquake_dataframe(query)
    query_url = df_eq.attrs.get("query_url", "")
    st.write(f"{len(df_eq)} USGS earthquake events found")
    if query_url:
        st.markdown(f"[USGS API query]({query_url})")
    if len(df_eq) >= query["limit"]:
        if query["limit"] >= 20000:
            st.warning("20000件上限に達したため一部のみ表示している可能性があります。条件を絞るか、Order by を変更してください。")
        else:
            st.warning(
                f"{query['limit']}件の取得上限に達しました。条件に一致する全件ではなく一部のみ表示している可能性があります。"
            )

    if df_eq.empty:
        st.warning("No USGS earthquake data available for the selected conditions.")
        return

    df_plot = eq.prepare_plot_dataframe(df_eq)
    if df_plot.empty:
        st.warning("No plottable USGS hypocenter data were returned.")
        return

    show_plate_boundaries = st.sidebar.checkbox(
        "Overlay plate boundaries",
        value=True,
        key="eq_compare_show_plate_boundaries",
    )
    include_microplates = st.sidebar.checkbox(
        "Include microplates",
        value=True,
        disabled=not show_plate_boundaries,
        key="eq_compare_include_microplates",
    )

    plate_boundary_df = pd.DataFrame()
    if show_plate_boundaries:
        with st.spinner("Loading plate boundaries..."):
            plate_boundary_df, plate_source, plate_errors = eq.load_plate_boundary_dataframe(
                query,
                include_microplates,
            )
        if plate_errors and plate_boundary_df.empty:
            st.warning("Plate boundary data could not be loaded from USGS.")
        elif plate_errors:
            st.warning("USGS plate boundary service could not be reached; fallback Japan lines are shown.")
        if not plate_boundary_df.empty:
            st.caption(
                f"Plate boundaries: {plate_source}. Boundary locations are approximate; "
                "for educational/research visualization only."
            )
            st.caption("プレート境界位置は概略です。教育・研究用の可視化として利用してください。")

    eq.render_jma_nied_comparison_page(df_plot, query, plate_boundary_df)

    if st.sidebar.button("Reload / clear API cache"):
        envgeo_utils.clear_app_cache()
        st.rerun()


if __name__ == "__main__":
    main()
