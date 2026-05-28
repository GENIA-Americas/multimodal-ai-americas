# Regional AI Benchmarks

GENIA Americas Corporation / RaceFor.AI
Open Research Repository

---

## Purpose

This directory contains benchmark suites for evaluating AI system
performance in the specific linguistic, economic, and environmental
contexts of the Americas.

Global benchmarks — GLUE, SuperGLUE, ImageNet, and their derivatives —
are insufficient for regional deployment evaluation. They were built
on data distributions that underrepresent the hemisphere and do not
test for the failure modes that matter in production here.

These benchmarks are designed to be runnable, citable, and extensible.
They are not aspirational — they reflect real deployment conditions.

---

## Benchmark Suite Index

### NLP Benchmarks

| Benchmark | Task | Languages | Status | Directory |
|-----------|------|-----------|--------|-----------|
| AmeriNLI | Natural language inference | es-LA, pt-BR | Active | nlp/ameri-nli/ |
| RegioNER | Named entity recognition | es-LA, pt-BR | Active | nlp/regio-ner/ |
| CorridorQA | Question answering | es-LA, pt-BR, en | Proposed | nlp/corridor-qa/ |
| IndigenousNLP | Text classification | qu, gn, nah | In development | nlp/indigenous/ |

### Economic and Financial AI Benchmarks

| Benchmark | Task | Coverage | Status | Directory |
|-----------|------|----------|--------|-----------|
| FinInclusionBench | Credit scoring fairness | LAC region | Active | economic/fin-inclusion/ |
| RemittanceFlow | Time series forecasting | Mexico, Central America | Active | economic/remittance/ |

### Agricultural AI Benchmarks

| Benchmark | Task | Coverage | Status | Directory |
|-----------|------|----------|--------|-----------|
| HarvestYield-LAC | Yield prediction | Brazil, Argentina, Mexico | Active | agri/harvest-yield/ |
| CropDiseaseAmericas | Image classification | Tropical crops | In development | agri/crop-disease/ |

### Public Sector AI Benchmarks

| Benchmark | Task | Coverage | Status | Directory |
|-----------|------|----------|--------|-----------|
| CivicServiceNLP | Intent classification | es-LA | Active | public-sector/civic-service/ |
| DocumentProcessing | Information extraction | es-LA, pt-BR | Proposed | public-sector/doc-processing/ |

---

## AmeriNLI

### Overview

AmeriNLI is a natural language inference benchmark designed to evaluate
model performance on Latin American Spanish and Brazilian Portuguese.
It covers four domains: legal texts, news, government documents, and
conversational language.

Standard NLI benchmarks use data sources that systematically
underrepresent Latin American linguistic variation. AmeriNLI corrects
this by sourcing premises and hypotheses from regionally produced text.

### Task

Given a premise and a hypothesis, classify the relationship as:
entailment, contradiction, or neutral.

### Data

- 12,000 premise-hypothesis pairs
- Languages: Latin American Spanish (es-LA), Brazilian Portuguese (pt-BR)
- Domains: legal, news, government, conversational
- Split: 70% train, 15% validation, 15% test
- Annotation: triple-annotated with inter-annotator agreement reported

### Metrics

Primary: accuracy on test set
Secondary: per-domain accuracy, per-language accuracy, macro-F1

### Baseline Results

| Model | es-LA Accuracy | pt-BR Accuracy | Notes |
|-------|---------------|----------------|-------|
| mBERT | 71.3 | 69.8 | Multilingual BERT baseline |
| XLM-R (base) | 76.1 | 74.9 | Strong multilingual baseline |
| XLM-R (large) | 79.4 | 78.2 | Upper bound for transformer baselines |
| GPT-4 (zero-shot) | 82.1 | 81.7 | Zero-shot, API-based evaluation |

### Running the Benchmark

```bash
cd research/benchmarks/nlp/ameri-nli
pip install -r requirements.txt
python evaluate.py --model xlm-roberta-base --language es-LA
python evaluate.py --model xlm-roberta-base --language pt-BR
```

Results are written to results/ameri-nli-{model}-{timestamp}.json

### Citation

If you use AmeriNLI in your research, cite:

```
@techreport{genia2025amerinli,
  title={AmeriNLI: Natural Language Inference for Latin American Spanish
         and Brazilian Portuguese},
  author={GENIA Americas Corporation},
  institution={GENIA Americas / RaceFor.AI},
  year={2025},
  url={https://github.com/GENIA-Americas/multimodal-ai-americas}
}
```

---

## RegioNER

### Overview

RegioNER is a named entity recognition benchmark for Latin American
Spanish and Brazilian Portuguese. It focuses on entity types that
are poorly covered by existing NER benchmarks: regional place names,
indigenous community names, local organizations, and regional
economic entities.

### Entity Types

- PER: Person names (regional naming conventions)
- ORG: Organizations (government agencies, NGOs, companies)
- LOC: Locations (cities, regions, indigenous territories, natural features)
- ECON: Economic entities (currencies, commodities, financial institutions)
- LEGIS: Legislative and regulatory references

### Data

- 8,500 annotated sentences
- Sources: regional news, government documents, court records
- Languages: Latin American Spanish, Brazilian Portuguese
- IOB2 tagging format

### Metrics

Primary: entity-level F1
Secondary: per-entity-type F1, per-country F1

### Baseline Results

| Model | es-LA F1 | pt-BR F1 |
|-------|----------|----------|
| mBERT | 78.2 | 76.9 |
| XLM-R (base) | 83.1 | 82.4 |
| XLM-R (large) | 86.7 | 85.3 |

---

## FinInclusionBench

### Overview

FinInclusionBench evaluates credit scoring models for fairness across
demographic groups in Latin American markets. It tests whether models
trained on historical credit data reproduce or amplify existing
inequalities in access to financial services.

### Task

Binary classification: credit approval / denial. Fairness evaluation
across gender, geographic region (urban/rural), and income quintile.

### Data

Synthetic dataset generated from documented distributions of credit
outcomes across the LAC region. Real PII-free.

### Metrics

- AUC-ROC: predictive performance
- Demographic parity difference: approval rate gap across groups
- Equal opportunity difference: true positive rate gap across groups
- Disparate impact ratio: ratio of approval rates across groups

### Significance

A model that achieves high AUC-ROC but fails fairness metrics is not
deployable in a system committed to financial inclusion. This benchmark
makes that tradeoff explicit and measurable.

---

## HarvestYield-LAC

### Overview

HarvestYield-LAC evaluates crop yield prediction models across the
primary agricultural regions of Brazil, Argentina, and Mexico.

Models trained on U.S. Midwest data systematically underperform on
Southern Hemisphere growing conditions, soil types, and crop varieties.
This benchmark quantifies that gap and provides a target for
regionally-trained models.

### Task

Regression: predict crop yield (tonnes/hectare) given climate,
soil, and management inputs.

### Crops Covered

- Soy (Brazil, Argentina)
- Corn (Brazil, Mexico, Argentina)
- Sugarcane (Brazil)
- Wheat (Argentina)
- Coffee (Brazil, Colombia)

### Data Sources

CONAB, SIAP, INTA, combined with INMET and IDEAM climate data.
See datasets/README.md for access details.

### Metrics

- RMSE: primary performance metric
- MAPE: mean absolute percentage error
- R2: coefficient of determination
- Per-crop and per-region breakdowns required for valid submission

---

## Contributing a Benchmark

To contribute a new benchmark:

1. Open an issue using the Benchmark Proposal template
2. Define: task, data sources, metrics, baseline, regional relevance
3. Provide runnable evaluation code
4. Document data licensing and any restrictions
5. Report at least one baseline result before submitting

Benchmarks without runnable code and documented baselines will not
be accepted. The value of a benchmark is its reproducibility.

---

Contact: admin@genia.ai
https://www.racefor.ai
