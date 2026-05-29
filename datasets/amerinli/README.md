# AmeriNLI — Natural Language Inference for Latin American Spanish

AmeriNLI is a benchmark dataset for Natural Language Inference (NLI) grounded in
Latin American Spanish across diverse regions, registers, and domains.

## Task Definition

Given a premise and a hypothesis, determine the logical relationship:

- entailment — the hypothesis follows necessarily from the premise
- neutral — the hypothesis is consistent with but not entailed by the premise
- contradiction — the hypothesis cannot be true if the premise is true

## Schema

Each record is a JSON object on a single line (JSONL format).

Required fields: premise, hypothesis, label, region (ISO 3166-1 alpha-2), domain
Optional fields: contributor (GitHub username), notes

Allowed label values: entailment, neutral, contradiction
Allowed domain values: news, legal, agriculture, health, education, commerce, culture, environment

## Submission Naming Convention

datasets/amerinli/submissions/<github-username>_<region>.jsonl

Example: jsmith_MX.jsonl

## Contact

admin@genia.ai
