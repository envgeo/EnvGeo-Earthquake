# EnvGeo-Earthquake

EnvGeo-Earthquake is a simple Streamlit application for visualizing earthquake
hypocenters for research and education.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/python-3.10--3.12-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

This application was created by adapting the spatial 3D/4D visualization workflow
of **EnvGeo-Seawater** to earthquake catalog data. The original EnvGeo-Seawater
project focused on interactive visualization of oceanographic and marine
geochemical data. EnvGeo-Earthquake keeps the educational, exploratory, and
source-aware philosophy of that project, but removes the ocean chemistry
workflow from the earthquake pages.

The app is intended for **simple research, teaching, and exploratory
visualization**. It is not an official earthquake alert, tsunami warning,
hazard assessment, or disaster-response system.

---

## Overview

EnvGeo-Earthquake fetches earthquake hypocenter data from the USGS Earthquake
Catalog API and visualizes the result as:

- 2D maps with marker size scaled by magnitude
- 3D/4D hypocenter plots with depth, magnitude, and colorbar controls
- arbitrary A-B cross-sections with a section-location map
- depth-frequency profiles
- time-series histograms
- Japan-focused comparison with uploaded JMA/NIED catalog tables
- plate-boundary overlays from USGS where available

The current earthquake pages do not use seawater isotope or ocean chemistry
datasets.

---

## Main Pages

- `pages/54_4D_Visualizer_Earthquake.py`  
  Basic earthquake-only USGS hypocenter visualizer.

- `pages/55_4D_Visualizer_Earthquake_Advanced.py`  
  Advanced earthquake visualizer with plate boundaries, 2D/3D maps,
  cross-section, depth profile, time histogram, and JMA/NIED comparison tab.

- `pages/56_Earthquake_JMA_NIED_Comparison.py`  
  Japan-focused page for comparing the current USGS query with a user-uploaded
  JMA, NIED Hi-net, JMA unified catalog, or related local catalog table.

---

## Key Features

- USGS Earthquake Catalog API access using GeoJSON
- filters for UTC date/time, magnitude, hypocenter depth, latitude, longitude,
  order, and maximum event count
- main-screen region selection for Japan and surrounding area or global view
- magnitude-scaled marker size on 2D maps
- colorbar variable selection between magnitude and hypocenter depth
- EnvGeo-style 3D/4D view using local kilometer coordinates so horizontal
  scale is more physically meaningful than raw degree axes
- depth-axis scaling up to 1,000 km
- plate-boundary overlays from the USGS Tectonic Plate Boundaries service
- arbitrary cross-section and depth-profile tools
- map showing the selected A-B cross-section line and section width
- time-series histogram of earthquake occurrence
- CSV export of the selected USGS catalog records
- warning when the selected query reaches the 20,000-event API limit
- concise source and data-use notes in the app
- PC recommendation for 3D display and 2D recommendation for smartphones/tablets

---

## Data Sources and Attribution

### USGS Earthquake Catalog API

Primary earthquake hypocenter data are accessed from:

- USGS Earthquake Catalog API / FDSN Event Web Service  
  https://earthquake.usgs.gov/fdsnws/event/1/

The app uses the `query` method with:

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

The USGS API documentation states that the service implements the FDSN Event
Web Service and supports query parameters for time, geographic bounds,
magnitude, depth, order, and a result limit. The service limit is 20,000 events;
the app therefore warns the user when a query reaches the selected limit.

Recommended catalog citation:

> U.S. Geological Survey. (2017). Advanced National Seismic System (ANSS)
> Comprehensive Catalog. U.S. Geological Survey.
> https://doi.org/10.5066/F7MS3QZH

Additional USGS links:

- ANSS / USGS FDSN data-center record  
  https://www.fdsn.org/datacenters/detail/USGS/
- USGS Earthquake Hazards Program  
  https://www.usgs.gov/programs/earthquake-hazards
- USGS Search Earthquake Catalog  
  https://earthquake.usgs.gov/earthquakes/search/
- USGS Latest Earthquakes  
  https://www.usgs.gov/tools/latest-earthquakes

### USGS data credit and preliminary-data note

USGS-authored or USGS-produced data and information are generally considered to
be in the U.S. public domain, and USGS requests proper credit when its products,
publications, or websites are used. However, earthquake catalog systems can
include information contributed by multiple networks or agencies, and some
non-USGS materials on USGS websites may have separate copyright restrictions.
For publication or redistribution, cite the USGS/ANSS catalog and also follow
any contributor-specific acknowledgement required by the specific catalog or
table being used.

- USGS Copyrights and Credits  
  https://www.usgs.gov/information-policies-and-instructions/copyrights-and-credits

Earthquake information can be preliminary and may be revised. This app therefore
states that earthquake data may be updated and that official agencies should be
used for emergency response and public-safety decisions.

- USGS Earthquake Notification Service disclaimer, included here as a related
  USGS note about preliminary earthquake information  
  https://earthquake.usgs.gov/ens/help_disclaimer

### Plate-boundary data

Plate-boundary overlays are loaded from:

- USGS Tectonic Plate Boundaries ArcGIS REST service  
  https://earthquake.usgs.gov/arcgis/rest/services/eq/map_plateboundaries/MapServer

The app uses:

- `Plates (1)`
- optional `Microplates (0)`

The USGS plate-boundary service metadata lists the following sources:

- USGS Seismicity of the Earth Map Series, as cited in the USGS service metadata  
  https://earthquake.usgs.gov/earthquakes/byregion/
- Bird, P. (2003). An updated digital model of plate boundaries.
  *Geochemistry, Geophysics, Geosystems*, 4(3), 52 pp.  
  https://doi.org/10.1029/2001GC000252
- DeMets, C., Gordon, R. G., & Argus, D. F. (2010). Geologically current
  plate motions. *Geophysical Journal International*, 181, 1-80.  
  https://doi.org/10.1111/j.1365-246X.2009.04491.x

Plate-boundary locations are approximate and are used as educational/research
context lines. They should not be used as official fault traces, hazard-zone
boundaries, or disaster-response information.

If the USGS plate-boundary service cannot be reached, the app can show a small
Japan-area fallback set of approximate schematic lines for trenches and troughs.
Those fallback lines are visual guides only and are not a formal dataset.

### JMA and NIED comparison data

The app does **not** automatically scrape JMA or NIED services. Instead, it
provides a comparison interface where the user can upload a catalog table
obtained and checked by the user.

Relevant official references:

- JMA Earthquake Information issued by Japan Meteorological Agency  
  https://www.data.jma.go.jp/eqev/data/en/guide/earthinfo.html
- JMA Seismological Bulletin of Japan  
  https://www.data.jma.go.jp/eqev/data/bulletin/index_e.html
- JMA Hypocenter file format  
  https://www.data.jma.go.jp/eqev/data/bulletin/data/format/fmthyp_e.html
- NIED Hi-net data guidance  
  https://www.hinet.bosai.go.jp/about_data/?LANG=en

NIED Hi-net guidance describes the automatic hypocenter catalog as a quick
report and advises users to refer to official JMA earthquake information. It
also notes that the JMA unified catalog is available through the Hi-net website
for registered users and recommends using the final JMA Seismological Bulletin
where appropriate.

Users are responsible for checking provider-specific terms, registration
requirements, acknowledgement requirements, and redistribution rules for any
JMA/NIED data they upload.

### Base maps and display layers

The app uses several map background styles through Plotly Mapbox layers:

- Standard map: Plotly/CARTO basemap style, based on CARTO basemaps and
  OpenStreetMap data attribution handled by the interactive map layer  
  https://carto.com/basemaps  
  https://www.openstreetmap.org/copyright
- Satellite map: USGS National Map imagery tiles  
  https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer
- Bathymetry map: Esri World Ocean Base tiles  
  https://services.arcgisonline.com/arcgis/rest/services/Ocean/World_Ocean_Base/MapServer
  Esri's Ocean Basemap attribution guidance should be followed for publication
  or static map exports.  
  https://support.esri.com/en-us/knowledge-base/what-is-the-correct-way-to-cite-an-arcgis-online-basema-000012040
- Contour/topographic map: Geospatial Information Authority of Japan (GSI) tiles  
  https://maps.gsi.go.jp/development/ichiran.html
  https://maps.gsi.go.jp/help/termsofuse.html



### Source certainty audit

The following status was checked against official or provider pages on
2026-05-04.

- High confidence: USGS FDSN Event Web Service/API parameters, GeoJSON output,
  `eventtype=earthquake`, depth/magnitude/location/time filters, and the
  20,000-event service limit are documented by USGS.
- High confidence: the ANSS Comprehensive Catalog citation and DOI
  `10.5066/F7MS3QZH` are listed by the FDSN USGS data-center record.
- High confidence: the plate-boundary overlay is an official USGS ArcGIS REST
  service with `Plates (1)` and `Microplates (0)` layers. Its own metadata cites
  Bird (2003), DeMets et al. (2010), and the USGS Seismicity of the Earth Map
  Series.
- High confidence: JMA and NIED links are official provider pages. The app does
  not scrape them; it only accepts user-uploaded comparison tables.
- Medium confidence: standard, satellite, bathymetry, and GSI background tiles
  are appropriate as interactive reference layers when their visible/provider
  attribution is retained. For papers, figures, printed handouts, or static
  exports, re-check each tile provider's current terms and required attribution.
- Coastline data used for plotting were derived from Natural Earth public domain vector data.

---

## Installation

This project is designed for Python 3.10 to 3.12.

```bash
pip install -r requirements.txt
```

For macOS Apple Silicon, geospatial packages such as Cartopy may be easier to
install through conda-forge before installing the remaining Python packages:

```bash
conda create -n envgeo-earthquake python=3.12
conda activate envgeo-earthquake
conda install -c conda-forge proj pyproj cartopy -y
pip install -r requirements.txt
```

Optional future interactive cross-section drawing with Leaflet/Folium would use:

```bash
pip install folium streamlit-folium
```

These optional packages are not required for the current Plotly-based
cross-section controls.

---

## Quick Start

```bash
streamlit run home.py
```

Then open the local URL shown in the terminal, usually:

```text
http://localhost:8501
```

Recommended workflow:

1. Open `4D Visualizer Earthquake Advanced`.
2. Select `Japan and surrounding area` or `Global`.
3. Set the sidebar filters for time, magnitude, depth, and geographic bounds.
4. Fetch/update the USGS query.
5. Review the 2D map first.
6. Use the 3D/4D map on a PC for depth structure.
7. Use cross-section and depth-profile tools for subduction-zone or regional
   seismicity analysis.
8. Use the time histogram to examine temporal clustering.
9. Use the JMA/NIED comparison page with manually uploaded catalog data when
   comparing Japan-area catalogs.

---

## API Usage

The USGS data loader is implemented in `envgeo_utils.py`.

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

Returned columns include:

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

The generated USGS query URL is stored in:

```python
df.attrs["query_url"]
```

---

## Directory Structure

- `home.py`  
  Main Streamlit entry point for EnvGeo-Earthquake.

- `envgeo_utils.py`  
  Shared utilities, including USGS API loading, GeoJSON normalization,
  mapping styles, coastline loading, and cache clearing.

- `pages/54_4D_Visualizer_Earthquake.py`  
  Basic earthquake visualizer.

- `pages/55_4D_Visualizer_Earthquake_Advanced.py`  
  Advanced earthquake visualizer.

- `pages/56_Earthquake_JMA_NIED_Comparison.py`  
  Japan-focused catalog comparison page.

- `coastline/`  
  Local coastline coordinate files for 3D reference overlays.

- `test/`  
  Basic tests inherited from the project.

Legacy seawater-related directories and files may remain in the repository
because this project was adapted from EnvGeo-Seawater. The earthquake-specific
pages do not require ocean chemistry datasets.

---

## Reproducibility and Caching

USGS earthquake queries are made through explicit URL parameters and the query
URL is displayed in the app. Downloaded results can be exported as CSV.

Streamlit caching is used to reduce repeated API access. Cached USGS earthquake
queries use a time-to-live of 1 hour, and plate-boundary queries use a
time-to-live of 24 hours. The sidebar includes a cache-clear/reload button.

Because earthquake catalogs can be revised, exact reproduced results may change
when USGS updates event parameters or when a query is rerun at a later date.

---

## Limitations

- This app is not an official alert or disaster-response product.
- USGS event data may be preliminary and may be revised.
- The USGS FDSN event service has a 20,000-event query limit.
- Large global queries can be slow in the browser because many points are drawn
  interactively.
- Plotly 3D interaction is best on a PC; 2D maps are recommended for
  smartphones and tablets.
- Plate boundaries are approximate context lines.
- JMA/NIED comparison depends on user-uploaded data and user-side compliance
  with provider terms.
- Local coastline reference files are used only for visualization context.

---

## Related Official Tools

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

## Development Reference

The USGS earthquake API implementation was informed by the official USGS
documentation and by the following introductory article:

- ssfuno, "PyGMTとUSGSのAPIを使って地震の分布を描いてみる"  
  https://zenn.dev/ssfuno/articles/56e2577ee794f3

The official USGS documentation and provider pages listed above should be used
as the primary references for data access, terms, and citations.

---

## Citation

If you use this application in teaching material, presentations, or research
workflows, please cite both the app and the original data providers.

Suggested app citation:

> Ishimura, T. (2026). EnvGeo-Earthquake: A simple research and education
> earthquake visualization app based on EnvGeo-Seawater. Kyoto University.

Required or recommended data citations should include:

> U.S. Geological Survey. (2017). Advanced National Seismic System (ANSS)
> Comprehensive Catalog. U.S. Geological Survey.
> https://doi.org/10.5066/F7MS3QZH

When plate boundaries are shown, also cite:

> Bird, P. (2003). An updated digital model of plate boundaries.
> *Geochemistry, Geophysics, Geosystems*, 4(3), 52 pp.
> https://doi.org/10.1029/2001GC000252

> DeMets, C., Gordon, R. G., & Argus, D. F. (2010). Geologically current
> plate motions. *Geophysical Journal International*, 181, 1-80.
> https://doi.org/10.1111/j.1365-246X.2009.04491.x

For Japan-area catalog comparison, cite and acknowledge JMA/NIED according to
the provider guidance for the specific dataset used.

---

## License

The application code is released under the MIT License. Data accessed from
external services remain subject to the terms, policies, and attribution
guidance of their original providers.
