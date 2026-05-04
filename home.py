#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Home page for EnvGeo-Earthquake.

This page is adapted from the EnvGeo-Seawater Streamlit home page and rewritten
for a simple research/education earthquake visualization app.
"""

import re
from pathlib import Path

import streamlit as st


BASE_DIR = Path(__file__).resolve().parent
APP_VERSION = "0.2.0-earthquake-20260504"

URLS = {
    "lab": "https://envgeo.h.kyoto-u.ac.jp/sw_jpn/",
    "contact": "https://www.h.kyoto-u.ac.jp/en_f/faculty_f/ishimura_toyoho_4dea/#mailform",
    "usgs_api": "https://earthquake.usgs.gov/fdsnws/event/1/",
    "usgs_comcat": "https://www.fdsn.org/datacenters/detail/USGS/",
    "usgs_credit": "https://www.usgs.gov/information-policies-and-instructions/copyrights-and-credits",
    "usgs_plate": "https://earthquake.usgs.gov/arcgis/rest/services/eq/map_plateboundaries/MapServer",
    "jma_info": "https://www.data.jma.go.jp/eqev/data/en/guide/earthinfo.html",
    "jma_bulletin": "https://www.data.jma.go.jp/eqev/data/bulletin/index_e.html",
    "nied_hinet": "https://www.hinet.bosai.go.jp/about_data/?LANG=en",
    "carto_basemaps": "https://carto.com/basemaps",
    "osm_copyright": "https://www.openstreetmap.org/copyright",
    "usgs_imagery": "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer",
    "esri_ocean": "https://services.arcgisonline.com/arcgis/rest/services/Ocean/World_Ocean_Base/MapServer",
    "esri_basemap_attribution": "https://support.esri.com/en-us/knowledge-base/what-is-the-correct-way-to-cite-an-arcgis-online-basema-000012040",
    "gsi_tiles": "https://maps.gsi.go.jp/development/ichiran.html",
    "gsi_terms": "https://maps.gsi.go.jp/help/termsofuse.html",
}


st.set_page_config(
    page_title="EnvGeo-Earthquake",
    initial_sidebar_state="auto",
    menu_items={
        "Get Help": URLS["usgs_api"],
        "Report a bug": URLS["contact"],
        "About": (
            "EnvGeo-Earthquake: a simple research/education earthquake "
            "visualization app based on EnvGeo-Seawater."
        ),
    },
)


def render_markdown_streamlit(md_text: str, base_dir: Path | None = None) -> None:
    """
    Render markdown while keeping local images visible in Streamlit.
    """
    image_pattern = re.compile(r"!\[(.*?)\]\((.*?)\)")
    buffer = []

    for line in md_text.splitlines():
        match = image_pattern.fullmatch(line.strip())
        if match:
            if buffer:
                st.markdown("\n".join(buffer), unsafe_allow_html=True)
                buffer = []

            caption, image_path = match.groups()
            if base_dir and not image_path.startswith(("http://", "https://", "data:")):
                image_path = str((base_dir / image_path).resolve())
            st.image(image_path, caption=caption if caption else None)
        else:
            buffer.append(line)

    if buffer:
        st.markdown("\n".join(buffer), unsafe_allow_html=True)


def read_text_file(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def render_external_link(label: str, url: str) -> None:
    if hasattr(st, "link_button"):
        st.link_button(label, url)
    else:
        st.markdown(f"[{label}]({url})")


def render_page_link(page_path: str, label: str) -> None:
    if hasattr(st, "page_link"):
        st.page_link(page_path, label=label)
    else:
        st.markdown(f"`{page_path}`: {label}")


def render_source_links() -> None:
    st.markdown(f"- [USGS Earthquake Catalog API]({URLS['usgs_api']})")
    st.markdown(f"- [ANSS Comprehensive Catalog citation]({URLS['usgs_comcat']})")
    st.markdown(f"- [USGS Copyrights and Credits]({URLS['usgs_credit']})")
    st.markdown(f"- [USGS Tectonic Plate Boundaries]({URLS['usgs_plate']})")
    st.markdown(f"- [JMA Earthquake Information]({URLS['jma_info']})")
    st.markdown(f"- [JMA Seismological Bulletin of Japan]({URLS['jma_bulletin']})")
    st.markdown(f"- [NIED Hi-net data guidance]({URLS['nied_hinet']})")
    st.markdown(f"- [CARTO Basemaps]({URLS['carto_basemaps']})")
    st.markdown(f"- [OpenStreetMap copyright and license]({URLS['osm_copyright']})")
    st.markdown(f"- [USGS National Map imagery tiles]({URLS['usgs_imagery']})")
    st.markdown(f"- [Esri Ocean Basemap attribution guidance]({URLS['esri_basemap_attribution']})")
    st.markdown(f"- [GSI tile list]({URLS['gsi_tiles']})")
    st.markdown(f"- [GSI terms of use]({URLS['gsi_terms']})")


def main():
    st.title("EnvGeo-Earthquake")
    st.subheader("Simple earthquake hypocenter visualization for research and education")
    st.write(
        "EnvGeo-Earthquake is a Streamlit app for exploring earthquake hypocenters "
        "by time, location, magnitude, and depth. It was built by adapting the "
        "EnvGeo-Seawater 3D/4D visualization workflow to earthquake catalog data."
    )
    st.write(f"Version: {APP_VERSION}")
    st.caption("Data source: USGS Earthquake Catalog API (GeoJSON, eventtype=earthquake).")
    st.warning(
        "This app is for research, education, and exploratory visualization. "
        "It is not an official earthquake alert, tsunami warning, hazard assessment, "
        "or disaster-response tool."
    )

    tab_main, tab_about, tab_sources, tab_manual, tab_limits, tab_readme = st.tabs(
        ["MAIN", "ABOUT", "DATA SOURCES", "MANUAL", "LIMITATIONS", "README"]
    )

    with tab_main:
        st.header("Start")
        st.write("Open one of the earthquake pages from the sidebar or the links below.")

        col_left, col_right = st.columns(2)
        with col_left:
            st.subheader("4D Visualizer")
            st.write(
                "Fetch USGS earthquake data, filter by date, magnitude, depth, and area, "
                "then visualize the results as 2D maps, 3D/4D hypocenter plots, "
                "cross-sections, depth profiles, and time histograms."
            )
            render_page_link(
                "pages/55_4D_Visualizer_Earthquake_Advanced.py",
                "Open 4D Visualizer Earthquake Advanced",
            )

        with col_right:
            st.subheader("JMA / NIED Comparison")
            st.write(
                "Compare the current USGS query with a user-uploaded JMA, NIED Hi-net, "
                "or JMA unified catalog table. This page does not scrape JMA/NIED data."
            )
            render_page_link(
                "pages/56_Earthquake_JMA_NIED_Comparison.py",
                "Open JMA / NIED Comparison",
            )

        st.info("3D views are recommended for PC. On smartphones and tablets, the 2D map is recommended.")

        st.subheader("Typical questions")
        st.markdown(
            """
- Where are recent earthquakes concentrated around Japan or globally?
- How does hypocenter depth change across a subduction zone?
- Are larger-magnitude events concentrated in a particular depth range?
- How does seismicity vary through time within a selected window?
- How do USGS locations compare with uploaded JMA/NIED catalog tables around Japan?
            """
        )

    with tab_about:
        st.header("About")
        st.write(
            "EnvGeo-Earthquake is a compact earthquake visualization app created from "
            "the EnvGeo-Seawater code base. EnvGeo-Seawater originally focused on "
            "interactive 3D/4D visualization of oceanographic and geochemical datasets; "
            "this earthquake version reuses that spatial visualization idea for "
            "hypocenter data."
        )
        st.write(
            "The goal is not to replace official earthquake services. The goal is to "
            "make catalog filtering, 2D/3D mapping, cross-section analysis, and "
            "source-aware data handling accessible in a teaching or exploratory "
            "research setting."
        )
        st.markdown(
            """
Core concepts:

- 4D visualization: longitude, latitude, depth, and color/size as magnitude or depth.
- Reproducible query: the USGS API URL is shown for each data request.
- Transparent source notes: earthquake data, plate boundaries, and comparison datasets are identified in the app.
- Conservative use: preliminary catalog data and approximate plate boundaries are treated as educational/research visual aids.
            """
        )

    with tab_sources:
        st.header("Data Sources and References")
        st.subheader("Earthquake catalog")
        st.write(
            "Earthquake hypocenters are retrieved from the USGS Earthquake Catalog API, "
            "which implements the FDSN Event Web Service. The app requests GeoJSON "
            "with `eventtype=earthquake` and supports filters for UTC time, magnitude, "
            "depth, latitude/longitude bounds, order, and event limit."
        )
        st.write(
            "Recommended catalog citation: U.S. Geological Survey (2017), "
            "Advanced National Seismic System (ANSS) Comprehensive Catalog, "
            "U.S. Geological Survey, https://doi.org/10.5066/F7MS3QZH."
        )
        st.write(
            "USGS-authored or USGS-produced information is generally public domain, "
            "but USGS requests credit. Because earthquake catalogs can include "
            "contributions from multiple networks or agencies, publication or "
            "redistribution should also follow any contributor-specific guidance."
        )

        st.subheader("Plate boundaries")
        st.write(
            "Plate boundaries are loaded from the USGS Tectonic Plate Boundaries "
            "ArcGIS REST service when available. The app uses the Plates and optional "
            "Microplates layers. USGS cites the Seismicity of the Earth Map Series, "
            "Bird (2003), and DeMets et al. (2010) for this service."
        )
        st.write(
            "Boundary locations are approximate and are intended for educational/research "
            "visualization, not for official hazard assessment or disaster-response decisions."
        )

        st.subheader("JMA / NIED comparison")
        st.write(
            "The comparison page is designed for manually uploaded JMA/NIED tables. "
            "It intentionally does not automatically scrape JMA or NIED services. "
            "Use provider guidance and acknowledgement requirements when downloading "
            "or redistributing these catalogs."
        )

        st.subheader("Map and display layers")
        st.markdown(
            f"""
- Standard map: Plotly/CARTO basemap style with OpenStreetMap attribution handled by the map layer.
- Satellite map: [USGS National Map imagery tile service]({URLS['usgs_imagery']}).
- Bathymetry map: [Esri World Ocean Base tiles]({URLS['esri_ocean']}); follow Esri attribution guidance for publication or static exports.
- Contour/topographic map: [Geospatial Information Authority of Japan (GSI) standard tiles]({URLS['gsi_tiles']}).
- Coastline overlay: local coastline coordinate files inherited from the EnvGeo mapping utilities; used only as a visual reference layer.
            """
        )

        st.subheader("Source certainty / 出典確認状況")
        st.markdown(
            """
- High confidence: USGS API parameters, GeoJSON output, earthquake filtering, the 20,000-event limit, ANSS/ComCat DOI, USGS plate-boundary service, JMA official pages, and NIED Hi-net guidance are supported by official/provider pages.
- Medium confidence: basemap tiles are suitable as interactive reference layers when provider attribution is retained; for papers, handouts, and static exports, re-check each provider's current terms.
- Unresolved: the local coastline Excel files do not contain source or license metadata in this repository. They should be treated only as visual reference overlays unless their provenance is recovered.
- Secondary reference: the Zenn article is useful implementation background, not a primary data source or licensing authority.
            """
        )
        st.caption(
            "ローカル海岸線ファイルの上流データは、このリポジトリ内では確認できませんでした。"
            "論文・教材で海岸線データ自体を引用する場合は、出典が明確なデータへ置き換えてください。"
        )

        st.subheader("Source links")
        render_source_links()

    with tab_manual:
        st.header("Manual")
        st.markdown(
            """
1. Open `4D Visualizer Earthquake Advanced`.
2. Choose `Japan and surrounding area` or `Global` on the main page.
3. Set API filters in the sidebar: date/time, magnitude, hypocenter depth, latitude/longitude, order, and maximum events.
4. Select the colorbar variable: magnitude or hypocenter depth.
5. Use the 2D map for overview and mobile/tablet viewing.
6. Use the 3D/4D map on a PC for depth structure and subduction-zone geometry.
7. Use `Cross-section / depth` to define an A-B section, inspect the depth distribution, and see the section line on the map.
8. Use `Time histogram` to inspect temporal clustering.
9. Use `JMA/NIED comparison` to upload a compatible catalog table and compare it with the current USGS query.
            """
        )

    with tab_limits:
        st.header("Limitations and Use Notes")
        st.markdown(
            """
- USGS earthquake data may be preliminary and can be revised after publication.
- The USGS API limits query results to 20,000 events; the app warns when a result may be truncated.
- This app is not an earthquake early-warning, tsunami-warning, or official disaster-response tool.
- Plate-boundary overlays are approximate regional/global context lines.
- JMA/NIED data comparison requires user-uploaded files; provider terms should be checked by the user.
- Local coastline files are reference overlays only; their upstream provenance is not documented in this repository.
- 3D Plotly interaction is heavy on small screens; PC use is recommended for 3D and 2D is recommended for smartphones/tablets.
- Very large global queries may be slow because the browser renders many interactive points.
            """
        )
        st.write(
            "For emergency information in Japan, use official sources such as the Japan "
            "Meteorological Agency and local government disaster information. For global "
            "earthquake information, check the relevant official seismic agency."
        )

    with tab_readme:
        st.header("README")
        readme_file = BASE_DIR / "README.md"
        if readme_file.exists():
            with st.expander("Show README", expanded=True):
                render_markdown_streamlit(read_text_file(readme_file), base_dir=BASE_DIR)
        else:
            st.info("README.md was not found.")

    st.write("_____")
    render_external_link("EnvGeo / Lab", URLS["lab"])


if __name__ == "__main__":
    main()
