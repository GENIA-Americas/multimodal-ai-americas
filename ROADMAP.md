# Roadmap

Status: AmeriXLM is not trained, and AmeriNLI and RegioNER are not fully released. This file tracks what has to happen, in order. Boxes get checked when the artifact is public.

## 1. Make the docs match reality
- [x] Hub model card states "not trained yet"
- [x] Repo docs mark unverified numbers and missing code

## 2. AmeriNLI v0.1 (real data, small)
- [x] Validator, stats script, and CI in `tools/` and `.github/workflows/`
- [ ] First batch of contributed examples under `datasets/amerinli/submissions/`
- [x] Writing guidelines (`datasets/amerinli/GUIDELINES.md`)
- [ ] Agreement numbers published
- [ ] Dataset card and release on the Hugging Face Hub

## 3. Baselines anyone can reproduce
- [ ] Evaluation script committed under `research/benchmarks/nlp/ameri-nli/`
- [ ] mBERT and XLM-R baselines rerun with logs and result files committed

## 4. RegioNER
- [ ] Data, annotation guide, and evaluation script published

## 5. AmeriXLM
- [ ] Corpus sources and licenses documented
- [ ] Tokenizer decision
- [ ] First training run (approach depends on available compute)
- [ ] Weights, config, and tokenizer on the Hub
- [ ] Results on AmeriNLI and RegioNER with code to reproduce them

## How to help
Contribute examples to AmeriNLI (see `datasets/amerinli/README.md`), review annotation guidelines, or open an issue.
