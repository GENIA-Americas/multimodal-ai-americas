# Datasets

Catalog of datasets relevant to AI in the Americas: ones built in this project, public sources worth knowing about, and gaps we would like to fill.

**Status describes the source, not a copy.** Nothing in this catalog is mirrored in this repository except AmeriNLI. Source links have not been bulk-verified. If one is dead or wrong, open an issue.

## Built in this project

| Dataset | Coverage | Format | Status | Location |
|---------|----------|--------|--------|----------|
| [AmeriNLI](amerinli/) | Latin American Spanish, natural language inference | JSONL | Seed sample, open for contributions | `datasets/amerinli/` |

## Public sources

### Agriculture and food systems

| Dataset | Coverage | Format | Access | Notes |
|---------|----------|--------|--------|-------|
| CONAB crop production statistics | Brazil | CSV | https://www.conab.gov.br | Harvest data by state and crop |
| SIAP agricultural statistics | Mexico | CSV | https://www.gob.mx/siap | Crop production, livestock, fisheries |
| INDEC agricultural census | Argentina | CSV | https://www.indec.gob.ar | National agricultural census |
| FAOSTAT | Global, filter to the Americas | CSV/JSON | https://www.fao.org/faostat | Production and trade statistics |

Gaps:
- Soil composition data at geospatial resolution finer than departamento level
- Smallholder yield data across the Andean countries
- Indigenous crop variety registries

### Climate and environment

| Dataset | Coverage | Format | Access | Notes |
|---------|----------|--------|--------|-------|
| INMET climate data | Brazil | CSV/NetCDF | https://bdmep.inmet.gov.br | Historical weather station data |
| IDEAM climate records | Colombia | CSV | https://www.ideam.gov.co | Hydrology, meteorology, environment |
| PRODES deforestation | Amazon basin | GeoTIFF | https://terrabrasilis.dpi.inpe.br | Annual deforestation mapping |
| GBIF occurrence data | Global, filter to the Americas | Darwin Core | https://www.gbif.org | Species occurrences |

Gaps:
- High-resolution precipitation data for Central America
- Mangrove and coastal ecosystem monitoring
- Andean glacier retreat time series

### Economic and financial

| Dataset | Coverage | Format | Access | Notes |
|---------|----------|--------|--------|-------|
| CEPAL/ECLAC statistics | Latin America and the Caribbean | CSV | https://statistics.cepal.org | Macroeconomic and social indicators |
| World Bank Open Data | Global, filter to the Americas | CSV/API | https://data.worldbank.org | Development indicators, API available |
| CNBV financial inclusion data | Mexico | CSV | https://www.cnbv.gob.mx | Banking access, credit, remittances |
| BCB financial system data | Brazil | CSV | https://www.bcb.gov.br | Financial system statistics |

Gaps:
- Informal economy estimates with documented methodology
- Subnational remittance flows
- SME credit access across Central America

### Language and NLP

| Dataset | Coverage | Format | Access | Notes |
|---------|----------|--------|--------|-------|
| OPUS | Multilingual, includes Spanish and Portuguese | Text | https://opus.nlpl.eu | Parallel corpora collection. Regional variety labels are not guaranteed. |
| Leipzig Corpora Collection | Multiple languages | Text | https://wortschatz.uni-leipzig.de | Check per-corpus licensing and provenance |
| Indigenous language archives | Multiple | Text, audio | SIL, ELDP, AILLA directly | Pointers only, nothing mirrored here. Licensing varies by archive. |

Gaps:
- Named entity recognition data for Latin American entities
- Sentiment corpora for regional Spanish varieties
- Corpora for Quechua, Nahuatl, Guarani, and Maya languages, with clear licensing
- Speech recognition data for regional accents

### Public health

| Dataset | Coverage | Format | Access | Notes |
|---------|----------|--------|--------|-------|
| PAHO health data | Regional | CSV | https://www.paho.org/data | Pan American Health Organization statistics |
| DATASUS | Brazil | CSV | https://datasus.saude.gov.br | National health system data |
| SINAVE | Mexico | CSV | https://www.gob.mx/salud | Epidemiological surveillance |

Gaps:
- Facility-level hospital capacity and utilization
- Community health worker activity
- Mental health epidemiology

### Infrastructure and logistics

| Dataset | Coverage | Format | Access | Notes |
|---------|----------|--------|--------|-------|
| OpenStreetMap extracts | South America | PBF/GeoJSON | https://download.geofabrik.de/south-america.html | Roads, rail, infrastructure |
| CEPAL trade data | Latin America and the Caribbean | CSV | https://statistics.cepal.org | International trade flows |
| Panama Canal Authority statistics | Panama | CSV | https://www.pancanal.com | Canal traffic and vessels |

## Datasets built here

A dataset stored in this repository gets its own directory and README covering:

- Source and collection method
- License
- Known limitations and biases
- Intended use
- Prohibited uses

No dataset goes in without license documentation. Schemas and ingestion pipelines for the other catalog entries are planned and not in this repo. The AmeriNLI schema is [amerinli/schema.json](amerinli/schema.json).

## Proposing a dataset

1. Open an issue with the "Dataset proposal" template.
2. Include source, license, format, coverage, intended use, and known limitations.
3. A maintainer reviews it and, if accepted, finds someone to integrate it.

Datasets with unclear provenance, missing license documentation, or personal data without explicit research consent are not accepted.

## Licensing

Datasets keep their original licenses, and use is subject to those terms. GENIA Americas makes no warranty about fitness for any purpose. You are responsible for checking that your use complies with the data protection law that applies to you.

Contact: admin@genia.ai
