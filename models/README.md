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

### NLP Models

| Model | Task | Languages | Parameters | Status | Directory |
|-------|------|-----------|------------|--------|-----------|
| AmeriXLM | Multilingual LM | es-LA, pt-BR, en | 270M | Active | regional-nlp/ameri-xlm/ |
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

### Overview

AmeriXLM is a multilingual language model pre-trained on a corpus
weighted toward Latin American Spanish and Brazilian Portuguese text.
It is the base model for most NLP work in the Corridor.

The motivation for a regionally-trained base model is straightforward:
XLM-R and mBERT allocate training compute in proportion to the volume
of text available per language. Latin American Spanish and Brazilian
Portuguese receive less compute than Castilian Spanish and European
Portuguese, which in turn receive far less than English. Regional
linguistic variation is underrepresented even within Spanish and
Portuguese allocations.

AmeriXLM corrects this by training on a corpus that explicitly
weights Latin American regional text.

### Architecture

- Base: RoBERTa architecture
- Parameters: 270M
- Vocabulary: 64,000 tokens, trained on regional corpus
- Pre-training: masked language modeling, 1M steps
- Context length: 512 tokens

### Training Data

- Brazilian Portuguese: 45B tokens (news, government, legal, web)
- Latin American Spanish: 38B tokens (news, government, legal, web)
- English (Americas): 12B tokens (news, government)
- Indigenous languages: 800M tokens (Quechua, Guarani, Nahuatl)

Data sources documented in datasets/README.md.

### Benchmark Results

| Benchmark | Score | Baseline (XLM-R large) | Delta |
|-----------|-------|----------------------|-------|
| AmeriNLI es-LA | 83.7 | 79.4 | +4.3 |
| AmeriNLI pt-BR | 82.9 | 78.2 | +4.7 |
| RegioNER es-LA F1 | 88.2 | 86.7 | +1.5 |
| RegioNER pt-BR F1 | 87.6 | 85.3 | +2.3 |

### Usage

```python
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("genia-americas/ameri-xlm")
model = AutoModel.from_pretrained("genia-americas/ameri-xlm")

inputs = tokenizer("Texto en español latinoamericano", return_tensors="pt")
outputs = model(**inputs)
```

Model weights: Hugging Face Hub — genia-americas/ameri-xlm
Model card: regional-nlp/ameri-xlm/MODEL_CARD.md

### Citation

```
@techreport{genia2025amerixlm,
  title={AmeriXLM: A Multilingual Language Model for the Americas},
  author={GENIA Americas Corporation},
  institution={GENIA Americas / RaceFor.AI},
  year={2025},
  url={https://github.com/GENIA-Americas/multimodal-ai-americas}
}
```

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
