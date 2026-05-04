#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EnvGeo-Earthquake のホームページ（日本語版）。

このページは EnvGeo-Seawater の Streamlit ホームページをもとに、
研究・教育向けの簡易的な地震可視化アプリ用に書き換えたものです。
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
            "EnvGeo-Earthquake: EnvGeo-Seawater をもとにした、"
            "研究・教育向けの簡易地震可視化アプリです。"
        ),
    },
)


def render_markdown_streamlit(md_text: str, base_dir: Path | None = None) -> None:
    """
    ローカル画像を表示できるようにしながら Markdown を Streamlit で描画
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
    """ページ名を文字列として表示。st.page_link() は使用しない"""
    st.markdown(f"- `{page_path}` — {label}")


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
    st.subheader("研究・教育向けの簡易地震震源可視化アプリ")
    st.write(
        "EnvGeo-Earthquake は、地震の震源を時刻・位置・マグニチュード・深さに基づいて"
        "探索するための Webアプリです。EnvGeo-Seawater(https://envgeo.h.kyoto-u.ac.jp/sw_jpn/) の 3D/4D 可視化ワークフローを、"
        "地震カタログデータに応用して構築しました。"
    )
    st.write(f"バージョン: {APP_VERSION}")
    st.caption("データソース: USGS Earthquake Catalog API（GeoJSON, eventtype=earthquake）。")
    st.warning(
        "このアプリは研究・教育・探索的可視化を目的としたものです。"
        "公式の地震速報、津波警報、ハザード評価、防災対応ツールではありません。"
    )

    tab_main, tab_about, tab_sources, tab_manual, tab_limits, tab_readme = st.tabs(
        ["MAIN", "ABOUT", "DATA SOURCES", "MANUAL", "LIMITATIONS", "README"]
    )

    with tab_main:
        st.header("Start")
        st.write("サイドバーから地震可視化ページを開いてください。")

        col_basic, col_advanced = st.columns(2)

        with col_basic:
            st.subheader("4D Visualizer Earthquake")
            st.write(
                "地震データ専用のシンプルな可視化ページです。USGS地震データを取得し、"
                "日付、マグニチュード、深さ、地域でフィルタしたうえで、"
                "基本的な 2D マップおよび 3D/4D 震源マップとして表示します。"
            )

        with col_advanced:
            st.subheader("4D Visualizer Earthquake Advanced")
            st.write(
                "地震データを詳細に探索するための発展版可視化ページです。"
                "2D マップ、3D/4D 震源プロット、プレート境界表示、"
                "断面図、深度プロファイル、時系列ヒストグラム、"
                "JMA/NIED カタログ比較機能を含みます。"
            )

        st.info("3D 表示は PC での利用を推奨します。スマートフォンやタブレットでは 2D マップの利用を推奨します。")

        st.subheader("教育的な活用例")
        st.markdown(
            """
- 最近の地震は、日本周辺または全球のどこに集中しているか？
- 沈み込み帯に沿って震源深さはどのように変化するか？
- 大きなマグニチュードの地震は、特定の深さ範囲に集中しているか？
- 選択した期間内で、地震活動は時間的にどのように変化するか？
- 日本周辺において、USGS の震源位置とアップロードしたユーザーデータ（JMA/NIEDのデータなど） との比較はどうか？（Advancedページ内）
            """
        )

    with tab_about:
        st.header("About")
        st.write(
            "EnvGeo-Earthquake は、EnvGeo-Seawater(https://envgeo.h.kyoto-u.ac.jp/sw_jpn/) のコードベースから作成したコンパクトな"
            "地震可視化アプリです。EnvGeo-Seawater はもともと、海洋学・地球化学データの"
            "インタラクティブな 3D/4D 可視化を目的としていました。本アプリでは、その空間可視化の"
            "考え方を震源データに応用しています。"
        )
        st.write(
            "目的は、公式の地震情報サービスを置き換えることではありません。"
            "カタログのフィルタリング、2D/3D マッピング、断面解析、出典を意識したデータ処理を、"
            "教育や探索的研究の場で利用しやすくすることを目的としています。"
        )
        st.markdown(
            """
基本コンセプト:

- 4D 可視化: 経度、緯度、深さに加え、色またはサイズでマグニチュードや深さを表現します。
- 再現可能なクエリ: 各データ取得に用いた USGS API URL を表示します。
- 出典表示: 地震データ、プレート境界、比較データセットの出典をアプリ内で示します。
- 利用: 速報的なカタログデータや概略的なプレート境界は、教育・研究用の可視化補助として扱います。
            """
        )

    with tab_sources:
        st.header("データソースと参考情報")
        st.subheader("地震データ")
        st.write(
            "震源データは、FDSN Event Web Service を実装した USGS Earthquake Catalog API から取得します。"
            "本アプリでは `eventtype=earthquake` の GeoJSON を取得し、UTC時刻、マグニチュード、"
            "深さ、緯度経度範囲、並び順、イベント数上限でフィルタできます。"
        )
        st.write(
            "推奨引用: U.S. Geological Survey (2017), "
            "Advanced National Seismic System (ANSS) Comprehensive Catalog, "
            "U.S. Geological Survey, https://doi.org/10.5066/F7MS3QZH."
        )
        st.write(
            "USGS が作成した情報は一般に米国パブリックドメインとされていますが、USGS は適切な"
            "クレジット表示を求めています。地震カタログには複数の観測網・機関からの情報が含まれる"
            "場合があるため、出版や再配布の際には各提供元のガイダンスにも従ってください。"
        )

        st.subheader("プレート境界")
        st.write(
            "プレート境界は、利用可能な場合に USGS Tectonic Plate Boundaries ArcGIS REST service "
            "から読み込みます。本アプリでは Plates および任意で Microplates レイヤーを使用します。"
            "このサービスでは、USGS Seismicity of the Earth Map Series、Bird (2003)、"
            "DeMets et al. (2010) が出典として示されています。"
        )
        st.write(
            "境界位置は概略であり、教育・研究用の可視化を目的としたものです。"
            "公式なハザード評価や防災判断には使用しないでください。"
        )

        st.subheader("JMA / NIED 比較")
        st.write(
            "Advancedページには、手動でアップロードした JMA/NIED 表データとの比較機能があります。"
            "JMA や NIED のサービスを自動的にスクレイピングするものではありません。"
            "これらのカタログをダウンロードまたは再配布する際は、各提供元の利用条件や謝辞要件を確認してください。"
        )

        st.subheader("地図と表示レイヤー")
        st.markdown(
            f"""
- 標準地図: Plotly/CARTO ベースマップスタイル。OpenStreetMap の attribution は地図レイヤー側で扱われます。
- 衛星画像: [USGS National Map imagery tile service]({URLS['usgs_imagery']})。
- 海底地形図: [Esri World Ocean Base tiles]({URLS['esri_ocean']})。出版や静的出力では Esri の attribution guidance に従ってください。
- 等高線・地形図: [国土地理院（GSI）標準タイル]({URLS['gsi_tiles']})。
- 海岸線オーバーレイ: EnvGeo の地図ユーティリティから継承したローカル海岸線座標ファイルを、表示上の参照レイヤーとして使用します。
            """
        )



        st.subheader("Source links")
        render_source_links()

    with tab_manual:
        st.header("Manual")
        st.markdown(
            """
1. `4D Visualizer Earthquake Advanced` を開きます。
2. メインページで `Japan and surrounding area` または `Global` を選択します。
3. サイドバーで、日付・時刻、マグニチュード、震源深さ、緯度経度、並び順、最大イベント数を設定します。
4. カラーバー変数として、マグニチュードまたは震源深さを選択します。
5. 概観やスマートフォン・タブレットでは 2D マップを使用します。
6. 深さ構造や沈み込み帯の形状を確認する場合は、PC で 3D/4D マップを使用します。
7. `Cross-section / depth` で A-B 断面を定義し、深さ分布と地図上の断面線を確認します。
8. `Time histogram` で時間的な集中や変化を確認します。
9. `4D Visualizer Earthquake Advanced` 内の JMA/NIED 比較機能で、対応するカタログ表をアップロードし、現在の USGS クエリ結果と比較します。
            """
        )

    with tab_limits:
        st.header("利用上の注意")
        st.markdown(
            """
- USGS の地震データは速報的な情報を含み、公開後に修正される場合があります。
- USGS API のクエリ結果は 20,000 イベントに制限されています。結果が上限に達する可能性がある場合、アプリは警告を表示します。
- このアプリは地震早期警報、津波警報、公式な災害対応ツールではありません。
- プレート境界オーバーレイは、概略的な地域・全球コンテキスト線です。
- JMA/NIED データ比較には、利用者がアップロードしたファイルが必要です。提供元の利用条件は利用者が確認してください。
- 3D Plotly の操作は小さな画面では重くなります。3D 表示は PC を推奨し、スマートフォンやタブレットでは 2D 表示を推奨します。
- 大規模な全球クエリでは、多数のインタラクティブ点をブラウザで描画するため、動作が遅くなる場合があります。
            """
        )
        st.write(
            "日本国内の緊急情報については、気象庁や自治体などの公式防災情報を確認してください。"
            "全球の地震情報については、対象地域の公式な地震観測機関の情報を確認してください。"
        )

    with tab_readme:
        st.header("README")
        readme_file = BASE_DIR / "../README_Japanese.md"
        if readme_file.exists():
            with st.expander("README を表示", expanded=True):
                render_markdown_streamlit(read_text_file(readme_file), base_dir=BASE_DIR)
        else:
            st.info("README_Japanese.md が見つかりません。")

    st.write("_____")
    render_external_link("EnvGeo / Lab", URLS["lab"])


if __name__ == "__main__":
    main()
