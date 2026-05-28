# Datasets

GENIA Americas Corporation / RaceFor.AI
Open Research Repository

---

## Purpose

This directory catalogs datasets relevant to AI development in the
Americas — those contributed directly, those curated from public
sources, and those proposed for collection.

The goal is to address the core data gap that causes imported AI
systems to underperform in regional contexts: training and evaluation
data that reflects the actual demographic, linguistic, economic, and
environmental conditions of the hemisphere.

---

## Catalog

### Agriculture and Food Systems

| Dataset | Coverage | Format | Status | Access | Notes |
|---------|----------|--------|--------|--------|-------|
| CONAB Crop Production Statistics | Brazil | CSV | Public | https://www.conab.gov.br | Annual harvest data by state and crop |
| SIAP Agricultural Statistics | Mexico | CSV | Public | https://www.gob.mx/siap | Crop production, livestock, fisheries |
| INDEC Agricultural Census | Argentina | CSV | Public | https://www.indec.gob.ar | National agricultural census data |
| FAO FAOSTAT Americas subset | Regional | CSV/JSON | Public | https://www.fao.org/faostat | Curated regional subset — see pipelines/faostat-americas.yml |

Priority gaps:
- Soil composition data with geospatial resolution below departamento level
- Smallholder farm yield data across Andean nations
- Indigenous crop variety registries

---

### Climate and Environment

| Dataset | Coverage | Format | Status | Access | Notes |
|---------|----------|--------|--------|--------|-------|
| INMET Climate Data | Brazil | CSV/NetCDF | Public | https://bdmep.inmet.gov.br | Historical weather station data |
| IDEAM Climate Records | Colombia | CSV | Public | https://www.ideam.gov.co | Hydrology, meteorology, environmental |
| Amazon deforestation (PRODES) | Amazon basin | GeoTIFF | Public | https://terrabrasilis.dpi.inpe.br | Annual deforestation mapping |
| GBIF Biodiversity Americas | Regional | Darwin Core | Public | https://www.gbif.org | Species occurrence data |

Priority gaps:
- High-resolution precipitation data for Central America
- Mangrove and coastal ecosystem monitoring datasets
- Andean glacier retreat time series

---

### Economic and Financial

| Dataset | Coverage | Format | Status | Access | Notes |
|---------|----------|--------|--------|--------|-------|
| CEPAL/ECLAC Economic Statistics | Regional | CSV | Public | https://statistics.cepal.org | Macroeconomic indicators, 35 nations |
| World Bank Open Data Americas | Regional | CSV/API | Public | https://data.worldbank.org | Development indicators, API available |
| CNBV Financial Inclusion Data | Mexico | CSV | Public | https://www.cnbv.gob.mx | Banking access, credit, remittances |
| BCB Financial System Data | Brazil | CSV | Public | https://www.bcb.gov.br | Financial system statistics |

Priority gaps:
- Informal economy activity estimates with methodology documentation
- Remittance flow data at subnational level
- SME credit access data across Central America

---

### Language and NLP

| Dataset | Coverage | Format | Status | Access | Notes |
|---------|----------|--------|--------|--------|-------|
| OPUS Regional Spanish Corpus | Americas Spanish variants | Text | Public | https://opus.nlpl.eu | Multilingual parallel corpus |
| Leipzig Corpora Collection | Multiple languages | Text | Public | https://wortschatz.uni-leipzig.de | Includes regional Spanish and Portuguese |
| Americas NLI (proposed) | Regional | Text | Proposed | — | NLI benchmark for regional language variants |
| Indigenous Languages of the Americas | Multiple | Text | Partial | See notes | Aggregated from SIL, ELDP, AILLA — licensing varies |

Priority gaps:
- Named entity recognition datasets for Latin American named entities
- Sentiment analysis corpora for regional Spanish variants
- Low-resource corpora for Quechua, Nahuatl, Guarani, Maya languages
- ASR training data for regional accents

---

### Public Health

| Dataset | Coverage | Format | Status | Access | Notes |
|---------|----------|--------|--------|--------|-------|
| PAHO Health Data | Regional | CSV | Public | https://www.paho.org/data | Pan American Health Organization statistics |
| MS DataSUS | Brazil | CSV | Public | https://datasus.saude.gov.br | National health system data |
| SINAVE Epidemiological Surveillance | Mexico | CSV | Public | https://www.gob.mx/salud | Disease surveillance data |

Priority gaps:
- Hospital capacity and utilization data at facility level
- Community health worker activity data
- Mental health epidemiological data

---

### Infrastructure and Logistics

| Dataset | Coverage | Format | Status | Access | Notes |
|---------|----------|--------|--------|--------|-------|
| OpenStreetMap Americas Extract | Regional | PBF/GeoJSON | Public | https://download.geofabrik.de/south-america.html | Road, rail, infrastructure |
| CEPAL Trade Data | Regional | CSV | Public | https://statistics.cepal.org | International trade flows |
| Panama Canal Authority Statistics | Panama | CSV | Public | https://www.pancanal.com | Canal traffic, vessel statistics |

---

## Contributed Datasets

Datasets contributed directly by GENIA Americas or network partners
are stored in subdirectories of this directory with individual README
files covering:

- Source and collection methodology
- Licensing terms
- Known limitations and biases
- Intended use cases
- Prohibited uses

No dataset is stored here without explicit licensing documentation.

---

## Data Schemas

Schemas for regional data standards are in datasets/schemas/.
These define canonical formats for cross-border data integration
through the Glapagos platform.

Current schemas:
- schemas/agriculture-production.json
- schemas/climate-station.json
- schemas/financial-inclusion.json
- schemas/health-facility.json

---

## Data Pipelines

Pipeline configurations for ingesting and normalizing public datasets
are in datasets/pipelines/. These are YAML configuration files
compatible with the Glapagos data orchestration layer.

---

## Proposing a Dataset

To propose a dataset for inclusion:

1. Open an issue using the Dataset Proposal template
2. Include: source, licensing, format, coverage, intended use,
   known limitations
3. Maintainers will review and assign a contributor to integration

Datasets with unclear provenance, missing licensing documentation,
or containing PII without explicit research consent will not be
accepted.

---

## Licensing Note

Datasets in this repository carry their original licenses. Use of
any dataset is subject to its license terms. GENIA Americas makes
no warranty regarding the fitness of any dataset for a particular
purpose. Users are responsible for verifying that their use complies
with applicable data protection law in their jurisdiction.

Contact: admin@genia.ai
