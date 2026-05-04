# EnvGeo-Earthquake

EnvGeo-Earthquake は、研究・教育向けに地震の震源を可視化するための
シンプルな Streamlit アプリケーションです。

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/python-3.10--3.12-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

このアプリケーションは、**EnvGeo-Seawater**
(https://envgeo.h.kyoto-u.ac.jp/sw_jpn/) の空間 3D/4D 可視化ワークフローを、
地震カタログデータに応用して作成しました。もとの EnvGeo-Seawater プロジェクトは、
海洋学・海洋地球化学データのインタラクティブな可視化を目的としていますが
EnvGeo-Earthquake は、その教育的・探索的・出典を重視する方針を引き継いでいます。

本アプリは、**簡易的な研究、授業、探索的可視化**を目的としています。
公式の地震速報、津波警報、ハザード評価、防災対応システムではありません。

---

## 概要

EnvGeo-Earthquake は、USGS Earthquake Catalog API から震源データを取得し、
以下の形式で可視化します。

- マグニチュードに応じてマーカーサイズを変えた 2D マップ
- 深さ、マグニチュード、カラーバー制御を備えた 3D/4D 震源プロット
- 任意の A-B 断面図と断面位置マップ
- 深度頻度プロファイル
- 時系列ヒストグラム
- アップロードした JMA/NIED カタログ表との日本周辺向け比較
- 利用可能な場合の USGS プレート境界オーバーレイ


---

## Main Pages

このアプリでは以下の Streamlit ページファイルを使用します。

- `pages/54_4D_Visualizer_Earthquake.py`  
  地震専用の基本的な USGS 震源可視化ページです。

- `pages/55_4D_Visualizer_Earthquake_Advanced.py`  
  プレート境界、2D/3D マップ、断面図、深度プロファイル、時系列ヒストグラム、
  JMA/NIED 比較タブを含む発展版の地震可視化ページです。

- `pages/56_Earthquake_JMA_NIED_Comparison.py`  
  現在の USGS クエリ結果を、利用者がアップロードした JMA、NIED Hi-net、
  JMA 一元化カタログ、または関連する地域カタログ表と比較する日本周辺向けページです。

---

## 主な機能

- GeoJSON を用いた USGS Earthquake Catalog API へのアクセス
- UTC 日時、マグニチュード、震源深さ、緯度、経度、並び順、最大イベント数によるフィルタ
- メイン画面での「日本周辺」または「全球」表示の選択
- 2D マップにおけるマグニチュード連動のマーカーサイズ
- カラーバー変数として、マグニチュードまたは震源深さを選択可能
- 経緯度の生値ではなくローカルな km 座標を用いた EnvGeo 形式の 3D/4D 表示
- 最大 1,000 km までの深度軸スケーリング
- USGS Tectonic Plate Boundaries service からのプレート境界オーバーレイ
- 任意断面図と深度プロファイル機能
- 選択した A-B 断面線と断面幅を表示するマップ
- 地震発生数の時系列ヒストグラム
- 選択した USGS カタログ記録の CSV 出力
- 選択クエリが 20,000 イベントの API 上限に達した場合の警告
- アプリ内での簡潔な出典・利用上の注意表示
- 3D 表示は PC 推奨、スマートフォン・タブレットでは 2D 表示推奨

---

## データソースと出典表示

### USGS Earthquake Catalog API

主要な震源データは以下から取得します。

- USGS Earthquake Catalog API / FDSN Event Web Service  
  https://earthquake.usgs.gov/fdsnws/event/1/

本アプリでは `query` メソッドを用い、主に以下のパラメータを使用します。

- `format=geojson`
- `eventtype=earthquake`
- `starttime`
- `endtime`
- `minmagnitude`, `maxmagnitude`
- `mindepth`, `maxdepth`
- `minlatitude`, `maxlatitude`
- `minlongitude`, `maxlongitude`
- `orderby`
- `limit`

USGS API ドキュメントでは、このサービスが FDSN Event Web Service を実装しており、
時刻、地理範囲、マグニチュード、深さ、並び順、結果数上限などのクエリパラメータを
サポートしていることが説明されています。サービスの上限は 20,000 イベントであるため、
本アプリではクエリが選択上限に達した場合に警告を表示します。

推奨カタログ引用:

> U.S. Geological Survey. (2017). Advanced National Seismic System (ANSS)
> Comprehensive Catalog. U.S. Geological Survey.
> https://doi.org/10.5066/F7MS3QZH

追加の USGS 関連リンク:

- ANSS / USGS FDSN data-center record  
  https://www.fdsn.org/datacenters/detail/USGS/
- USGS Earthquake Hazards Program  
  https://www.usgs.gov/programs/earthquake-hazards
- USGS Search Earthquake Catalog  
  https://earthquake.usgs.gov/earthquakes/search/
- USGS Latest Earthquakes  
  https://www.usgs.gov/tools/latest-earthquakes

### USGS データのクレジットと速報値に関する注意

USGS が作成したデータや情報は、一般に米国のパブリックドメインとみなされます。
一方で、USGS はそのプロダクト、出版物、Web サイトを利用する際に適切なクレジットを
表示することを求めています。また、地震カタログには複数の観測網や機関から提供された
情報が含まれる場合があり、USGS Web サイト上の非 USGS 資料には別の著作権制限が
適用されることがあります。出版や再配布の際には、USGS/ANSS カタログを引用するとともに、
利用するカタログや表に対して各提供元が求める謝辞・利用条件にも従ってください。

- USGS Copyrights and Credits  
  https://www.usgs.gov/information-policies-and-instructions/copyrights-and-credits

地震情報は速報的であり、後から修正される場合があります。そのため本アプリでは、
地震データが更新・修正される可能性があること、緊急対応や公共安全上の判断には
公式機関の情報を利用すべきであることを明示しています。

- USGS Earthquake Notification Service disclaimer  
  https://earthquake.usgs.gov/ens/help_disclaimer

### プレート境界データ

プレート境界オーバーレイは以下から読み込みます。

- USGS Tectonic Plate Boundaries ArcGIS REST service  
  https://earthquake.usgs.gov/arcgis/rest/services/eq/map_plateboundaries/MapServer

本アプリでは以下を使用します。

- `Plates (1)`
- 任意で `Microplates (0)`

USGS のプレート境界サービスのメタデータには、以下の出典が示されています。

- USGS Seismicity of the Earth Map Series  
  https://earthquake.usgs.gov/earthquakes/byregion/
- Bird, P. (2003). An updated digital model of plate boundaries.
  *Geochemistry, Geophysics, Geosystems*, 4(3), 52 pp.  
  https://doi.org/10.1029/2001GC000252
- DeMets, C., Gordon, R. G., & Argus, D. F. (2010). Geologically current
  plate motions. *Geophysical Journal International*, 181, 1-80.  
  https://doi.org/10.1111/j.1365-246X.2009.04491.x

プレート境界の位置は概略であり、教育・研究用の文脈表示として使用します。
公式な断層線、ハザードゾーン境界、防災対応情報として使用しないでください。

USGS プレート境界サービスに接続できない場合、本アプリは日本周辺の海溝・トラフを示す
小規模な概略フォールバック線を表示できます。これらは視覚的なガイドであり、
正式なデータセットではありません。

### JMA および NIED 比較データ

本アプリは JMA や NIED のサービスを自動的にスクレイピングしません。
代わりに、利用者が取得・確認したカタログ表をアップロードして比較できる
インターフェースを提供します。

関連する公式情報:

- JMA Earthquake Information issued by Japan Meteorological Agency  
  https://www.data.jma.go.jp/eqev/data/en/guide/earthinfo.html
- JMA Seismological Bulletin of Japan  
  https://www.data.jma.go.jp/eqev/data/bulletin/index_e.html
- JMA Hypocenter file format  
  https://www.data.jma.go.jp/eqev/data/bulletin/data/format/fmthyp_e.html
- NIED Hi-net data guidance  
  https://www.hinet.bosai.go.jp/about_data/?LANG=en

NIED Hi-net のガイダンスでは、自動震源カタログは速報的な報告であり、
公式な地震情報については気象庁情報を参照するよう案内されています。
また、JMA 一元化カタログは登録ユーザー向けに Hi-net Web サイトから利用可能であり、
必要に応じて最終版の JMA Seismological Bulletin を使用することが推奨されています。

JMA/NIED データをアップロードする利用者は、提供元ごとの利用条件、登録要件、謝辞要件、
再配布ルールを確認する責任があります。

### ベースマップと表示レイヤー

本アプリでは、Plotly Mapbox レイヤーを通じて複数の地図背景を使用します。

- 標準地図: CARTO ベースマップおよび OpenStreetMap データに基づく
  Plotly/CARTO ベースマップスタイル。インタラクティブ地図レイヤー側で
  attribution が扱われます。  
  https://carto.com/basemaps  
  https://www.openstreetmap.org/copyright
- 衛星画像: USGS National Map imagery tiles  
  https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer
- 海底地形図: Esri World Ocean Base tiles  
  https://services.arcgisonline.com/arcgis/rest/services/Ocean/World_Ocean_Base/MapServer  
  出版や静的地図出力では、Esri の Ocean Basemap attribution guidance に従ってください。  
  https://support.esri.com/en-us/knowledge-base/what-is-the-correct-way-to-cite-an-arcgis-online-basema-000012040
- 等高線・地形図: 国土地理院（GSI）タイル  
  https://maps.gsi.go.jp/development/ichiran.html  
  https://maps.gsi.go.jp/help/termsofuse.html

### 出典確認状況

以下の状態は、2026-05-04 に公式または提供元ページに基づいて確認したものです。

- USGS FDSN Event Web Service/API パラメータ、GeoJSON 出力、
  `eventtype=earthquake`、深さ・マグニチュード・位置・時刻フィルタ、
  20,000 イベントのサービス上限は USGS により文書化されています。
- ANSS Comprehensive Catalog の引用情報と DOI `10.5066/F7MS3QZH` は
  FDSN の USGS data-center record に記載されています。
- プレート境界オーバーレイは、`Plates (1)` および `Microplates (0)` レイヤーを持つ
  USGS の公式 ArcGIS REST service です。メタデータでは Bird (2003)、DeMets et al. (2010)、
  USGS Seismicity of the Earth Map Series が引用されています。
- JMA と NIED のリンクは公式提供元ページです。本アプリはこれらをスクレイピングせず、
  利用者がアップロードした比較表のみを受け付けます。
- 論文、図、印刷教材、静的出力で使う場合は、
  各タイル提供元の最新の利用条件と必要な attribution を再確認してください。
- プロットに使用する海岸線データは Natural Earth のパブリックドメインベクターデータに由来します。

---

## インストール

このプロジェクトは Python 3.10 から 3.12 を想定しています。

```bash
pip install -r requirements.txt
```



---

## Quick Start

```bash
streamlit run home.py
```

その後、ターミナルに表示されるローカル URL を開きます。通常は以下です。

```text
http://localhost:8501
```

推奨ワークフロー:

1. `4D Visualizer Earthquake Advanced` を開きます。
2. `Japan and surrounding area` または `Global` を選択します。
3. サイドバーで、時刻、マグニチュード、深さ、地理範囲のフィルタを設定します。
4. USGS クエリを取得または更新します。
5. まず 2D マップで概観を確認します。
6. 深さ構造を確認する場合は、PC で 3D/4D マップを使用します。
7. 沈み込み帯や地域地震活動を解析する場合は、断面図と深度プロファイルを使用します。
8. 時系列ヒストグラムで時系列の地震発生頻度を確認します。
9. 日本周辺カタログを比較する場合は、手動で取得したカタログデータを JMA/NIED 比較ページにアップロードします。

---

## API 使用例

USGS データローダーは `envgeo_utils.py` に実装されています。

```python
from datetime import datetime, timezone

import envgeo_utils

df = envgeo_utils.load_usgs_earthquake_data(
    starttime=datetime(2026, 1, 1, tzinfo=timezone.utc),
    endtime=datetime(2026, 1, 31, tzinfo=timezone.utc),
    minmagnitude=4.5,
    mindepth=0,
    maxdepth=700,
    minlatitude=20,
    maxlatitude=50,
    minlongitude=120,
    maxlongitude=155,
    limit=2000,
    orderby="time",
)
```

返される主な列:

- `EventID`
- `DateTime_UTC`
- `Time_UTC`
- `Longitude_degE`
- `Latitude_degN`
- `Depth_km`
- `Magnitude`
- `MagnitudeType`
- `Place`
- `URL`

生成された USGS クエリ URL は以下に保存されます。

```python
df.attrs["query_url"]
```

---

## ディレクトリ構成

- `home.py`  
  EnvGeo-Earthquake の Streamlit メインエントリーポイントです。

- `envgeo_utils.py`  
  USGS API 読み込み、GeoJSON 正規化、地図スタイル、海岸線読み込み、
  キャッシュ削除などを含む低レベル共通ユーティリティです。

- `envgeo_earthquake_utils.py`  
  地震専用の Streamlit コントロール、プレート境界オーバーレイ、2D/3D マップ、
  断面図、深度プロファイル、時系列ヒストグラム、JMA/NIED 比較補助関数を含みます。

- `pages/54_4D_Visualizer_Earthquake.py`  
  基本的な地震可視化ページです。

- `pages/55_4D_Visualizer_Earthquake_Advanced.py`  
  発展版の地震可視化ページです。

- `pages/56_Earthquake_JMA_NIED_Comparison.py`  
  日本周辺向けのカタログ比較ページです。

- `coastline/`  
  3D 参照オーバーレイ用のローカル海岸線座標ファイルです。

- `test/`  
  プロジェクトから継承された基本的なテストです。

このプロジェクトは EnvGeo-Seawater から派生したため、レガシーな海水関連ディレクトリや
ファイルがリポジトリに残っている場合があります。地震専用ページでは海洋化学データセットを
必要としません。

---

## 再現性とキャッシュ

USGS 地震クエリは明示的な URL パラメータを通じて実行され、クエリ URL はアプリ内に表示されます。
取得結果は CSV としてエクスポートできます。

Streamlit のキャッシュを用いて、API への重複アクセスを減らしています。
USGS 地震クエリのキャッシュは 1 時間、プレート境界クエリのキャッシュは 24 時間です。
サイドバーにはキャッシュ削除・再読み込みボタンがあります。

地震カタログは修正される場合があるため、USGS がイベントパラメータを更新した場合や、
後日クエリを再実行した場合には、完全に同じ結果が再現されないことがあります。

---

## 制約

- このアプリは公式の警報・防災対応プロダクトではありません。
- USGS イベントデータは速報的であり、後から修正される場合があります。
- USGS FDSN event service には 20,000 イベントのクエリ上限があります。
- 大規模な全球クエリは、多数の点をブラウザがインタラクティブに描画するため遅くなる場合があります。
- Plotly 3D の操作は PC に適しています。スマートフォンやタブレットでは 2D マップを推奨します。
- プレート境界は概略的なコンテキスト線です。
- JMA/NIED 比較は、利用者がアップロードしたデータと、利用者側での提供元条件遵守に依存します。
- ローカル海岸線参照ファイルは、可視化コンテキストとしてのみ使用します。

---

## 関連する公式ツール

- USGS Latest Earthquakes  
  https://www.usgs.gov/tools/latest-earthquakes
- USGS Search Earthquake Catalog  
  https://earthquake.usgs.gov/earthquakes/search/
- JMA earthquake information  
  https://www.data.jma.go.jp/eqev/data/en/guide/earthinfo.html
- JMA Seismological Bulletin of Japan  
  https://www.data.jma.go.jp/eqev/data/bulletin/index_e.html
- NIED Hi-net  
  https://www.hinet.bosai.go.jp/?LANG=en

---

## 開発参考資料

USGS 地震 API の実装は、公式 USGS ドキュメントと以下の入門記事を参考にしています。

- ssfuno, "PyGMTとUSGSのAPIを使って地震の分布を描いてみる"  
  https://zenn.dev/ssfuno/articles/56e2577ee794f3

データアクセス、利用条件、引用については、上記の公式 USGS ドキュメントおよび提供元ページを
一次的な参照先として使用してください。

---

## Citation

授業資料、発表、研究ワークフローで本アプリを使用する場合は、アプリ本体と元データ提供者の
両方を引用してください。

推奨アプリ引用:

> Ishimura, T. (2026). EnvGeo-Earthquake: A simple research and education
> earthquake visualization app based on EnvGeo-Seawater. Kyoto University.

必須または推奨されるデータ引用には、以下を含めてください。

> U.S. Geological Survey. (2017). Advanced National Seismic System (ANSS)
> Comprehensive Catalog. U.S. Geological Survey.
> https://doi.org/10.5066/F7MS3QZH

プレート境界を表示する場合は、以下も引用してください。

> Bird, P. (2003). An updated digital model of plate boundaries.
> *Geochemistry, Geophysics, Geosystems*, 4(3), 52 pp.
> https://doi.org/10.1029/2001GC000252

> DeMets, C., Gordon, R. G., & Argus, D. F. (2010). Geologically current
> plate motions. *Geophysical Journal International*, 181, 1-80.
> https://doi.org/10.1111/j.1365-246X.2009.04491.x

日本周辺カタログ比較を行う場合は、使用した具体的なデータセットに応じて、
JMA/NIED の提供元ガイダンスに従い、引用・謝辞を記載してください。

---

## License

アプリケーションコードは MIT License のもとで公開されています。
外部サービスから取得するデータは、それぞれの元提供者の利用条件、ポリシー、
attribution guidance に従います。
