# Models

GENIA Americas Corporation / RaceFor.AI
Open Research Repository

---

## Purpose

This directory is the model registry for the AI Corridor of the
Americas. It catalogs models produced by or in collaboration with
GENIA Americas, the RaceFor.AI network, and affiliated researchers.

Models listed here are evaluated against regional benchmarks defined
in research/benchmarks/. A model that has not been evaluated against
at least one regional benchmark is not listed as production-ready
regardless of its global benchmark performance.

---

## Registry

> Note: the directories in these tables are not in this repo yet (`models/` only holds this file). Statuses describe intent, not released artifacts. Check each model's own repo or Hub page for what is actually downloadable. AmeriXLM is planned and has no weights.

### NLP Models

| Model | Task | Languages | Parameters | Status | Directory |
|-------|------|-----------|------------|--------|-----------|
| AmeriXLM | Multilingual LM | es-LA, pt-BR, en | TBD | Planned (not trained) | n/a |
| CorridorNER | Named entity recognition | es-LA, pt-BR | 110M | Active | regional-nlp/corridor-ner/ |
| IndigenousLM | Language modeling | qu, gn, nah | 125M | In development | regional-nlp/indigenous-lm/ |

### Agricultural Models

| Model | Task | Coverage | Status | Directory |
|-------|------|----------|--------|-----------|
| HarvestNet | Yield prediction | Brazil, Argentina, Mexico | Active | agribusiness/harvest-net/ |
| CropHealthViT | Disease detection | Tropical crops | In development | agribusiness/crop-health-vit/ |

### Supply Chain Models

| Model | Task | Coverage | Status | Directory |
|-------|------|----------|--------|-----------|
| CorridorRoute | Logistics optimization | Americas | Proposed | supply-chain/corridor-route/ |
| TradeFlowLSTM | Trade volume forecasting | LAC region | Active | supply-chain/trade-flow-lstm/ |

### Public Sector Models

| Model | Task | Coverage | Status | Directory |
|-------|------|----------|--------|-----------|
| CivicIntent | Intent classification | es-LA | Active | public-sector/civic-intent/ |

---

## AmeriXLM

**Status: planned, not trained.** There are no weights yet. The Hugging Face repo (`genia-americas/ameri-xlm`) is a placeholder and says the same thing.

### Motivation

XLM-R and mBERT split their training compute roughly by how much text exists per language. That likely leaves Latin American Spanish and Brazilian Portuguese underweighted. AmeriXLM is meant to be an encoder trained on a corpus that weights regional text on purpose. Whether it beats existing models is something we still have to measure.

### Planned design

Targets only. Any of this can change.

- RoBERTa-style encoder, masked language modeling, 512 token context
- Languages: es-LA, pt-BR, English, plus Quechua, Guarani, and Nahuatl
- Regional tokenizer
- Size, vocabulary, and training budget: not decided

### Evaluation plan

AmeriXLM will be evaluated on AmeriNLI and RegioNER (see `research/benchmarks/`). There are no AmeriXLM scores yet. They get added here when the model exists and the eval code is public.

### Citation

Not citable as a released model. A citation entry will be added with the weights and a report.

---

## HarvestNet

### Overview

HarvestNet is a crop yield prediction model trained on agricultural
data from Brazil, Argentina, and Mexico. It is the reference model
for the HarvestYield-LAC benchmark.

### Architecture

- Gradient boosted trees (XGBoost base) with neural feature extraction
- Inputs: climate variables, soil type, crop variety, management
  practices, satellite-derived vegetation indices
- Output: yield prediction in tonnes/hectare with confidence interval

### Performance

| Crop | Region | RMSE | MAPE | R2 |
|------|--------|------|------|----|
| Soy | Brazil | 0.31 | 4.2% | 0.87 |
| Soy | Argentina | 0.28 | 3.9% | 0.89 |
| Corn | Brazil | 0.44 | 5.1% | 0.83 |
| Corn | Mexico | 0.51 | 6.3% | 0.79 |
| Wheat | Argentina | 0.38 | 4.7% | 0.85 |

### Usage

```python
from genia.agri import HarvestNet

model = HarvestNet.from_pretrained("genia-americas/harvest-net-v1")
prediction = model.predict(
    crop="soy",
    region="mato_grosso_br",
    climate=climate_data,
    soil=soil_data
)
print(prediction.yield_estimate, prediction.confidence_interval)
```

---

## Model Card Requirements

Every model in this registry must have a MODEL_CARD.md in its
directory covering:

- Model description and intended use
- Training data (sources, size, known limitations)
- Evaluation results on regional benchmarks
- Known failure modes and out-of-distribution behavior
- Prohibited uses
- Licensing terms
- Contact for questions

Models without a complete model card are listed as In Development
regardless of their technical readiness.

---

## Contributing a Model

1. Open an issue using the Model Contribution template
2. Provide evaluation results on at least one benchmark from
   research/benchmarks/ before submitting
3. Complete the MODEL_CARD.md template
4. Large model files use Git LFS — see .gitattributes
5. Add an entry to the registry table above

Models submitted without regional benchmark evaluation will not be
accepted into the Active registry.

---

Contact: admin@genia.ai
https://www.racefor.ai
