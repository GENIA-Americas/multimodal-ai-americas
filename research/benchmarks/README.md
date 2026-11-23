# Benchmarks

Specs for benchmarks aimed at regional language and applied AI tasks in the Americas.

**Early stage.** The only benchmark with any data in this repo is AmeriNLI, as a 5-example seed sample. There are no published baseline results and no evaluation scripts yet. Everything below describes design targets, and each section says what exists today.

## Index

| Benchmark | Task | Languages / coverage | Status |
|-----------|------|----------------------|--------|
| [AmeriNLI](../../datasets/amerinli/) | Natural language inference | es-LA first, pt-BR planned | Seed sample |
| RegioNER | Named entity recognition | es-LA, pt-BR | Proposed |
| CorridorQA | Question answering | es-LA, pt-BR, en | Proposed |
| IndigenousNLP | Text classification | qu, gn, nah | Proposed |
| FinInclusionBench | Credit scoring fairness | Latin America and the Caribbean | Proposed |
| RemittanceFlow | Time series forecasting | Mexico, Central America | Proposed |
| HarvestYield-LAC | Yield prediction | Brazil, Argentina, Mexico | Proposed |
| CropDiseaseAmericas | Image classification | Tropical crops | Proposed |
| CivicServiceNLP | Intent classification | es-LA | Proposed |
| DocumentProcessing | Information extraction | es-LA, pt-BR | Proposed |

Why regional benchmarks at all: general benchmarks such as GLUE were not built to test regional language variation, and we want to measure that instead of assuming it.

## AmeriNLI

Given a premise and a hypothesis, classify the relationship as entailment, contradiction, or neutral.

**Exists today:** a seed sample, a JSON schema, a validator (`tools/validate_amerinli.py`), and an open submission folder.

**Design targets:**
- Sources: premises and hypotheses written by contributors in their own regional Spanish, across news, legal, agriculture, health, education, commerce, culture, and environment domains
- Size: on the order of 12,000 pairs in a train/validation/test split
- Annotation: multiple annotators per pair, with agreement reported
- Metrics: accuracy (primary), macro-F1, per-domain and per-region breakdowns

**Baselines:** none published. They will be run with committed scripts and logs before any number appears here.

## RegioNER

Named entity recognition with entity types that general benchmarks cover poorly: regional place names, Indigenous community names, local organizations, economic entities, legislative references.

**Exists today:** nothing beyond this spec.

**Design targets:** entity types PER, ORG, LOC, ECON, LEGIS in IOB2 format, sentences drawn from regional news, government documents, and court records, with entity-level F1 as the primary metric. The target size is a few thousand annotated sentences.

## Other proposed benchmarks

These are sketches and open for anyone to take on. Open an issue before starting.

- **FinInclusionBench:** binary credit approval with fairness metrics across gender, urban/rural, and income groups (demographic parity difference, equal opportunity difference, disparate impact ratio) alongside AUC-ROC. Data would be synthetic.
- **HarvestYield-LAC:** crop yield regression (RMSE, MAPE, R2) using public agricultural and climate sources listed in the [dataset catalog](../../datasets/README.md).
- **CorridorQA, IndigenousNLP, RemittanceFlow, CropDiseaseAmericas, CivicServiceNLP, DocumentProcessing:** names and tasks only.

## Contributing a benchmark

1. Open an issue with the task, data sources, metrics, and why the region matters.
2. Provide runnable evaluation code.
3. Document data licensing and restrictions.
4. Report at least one baseline with logs.

A benchmark without runnable code and reproducible baselines is not accepted. Reproducibility is the point.

Contact: admin@genia.ai
