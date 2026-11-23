# multimodal-ai-americas

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20437260.svg)](https://doi.org/10.5281/zenodo.20437260)
[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)

Open datasets, benchmarks, and research notes for AI that works in Latin American Spanish, Brazilian Portuguese, and the Indigenous languages of the Americas.

The project is early. The first concrete piece is **AmeriNLI**, a natural language inference dataset written by speakers of these varieties. It needs contributors more than anything else, and adding your first examples takes about ten minutes.

## Status

| Piece | State |
|-------|-------|
| [AmeriNLI](datasets/amerinli/) | 5-example seed sample, JSON schema, validator. Open for contributions. |
| RegioNER (NER benchmark) | Planned. No data or code yet. |
| Benchmark evaluation scripts | Planned. See [research/benchmarks](research/benchmarks/). |
| [AmeriXLM](models/) | Not trained. No weights. The [Hugging Face repo](https://huggingface.co/genia-americas/ameri-xlm) is a placeholder. |
| Glapagos platform and SDK | Specs and drafts only, see [platform/](platform/) and [tools/glapp/](tools/glapp/). No platform code in this repo, and the SDK packages are not published. |
| Policy, strategy, and background docs | Written and in this repo. See the table below. |

Order of work: [ROADMAP.md](ROADMAP.md).

## Contribute an AmeriNLI example

Each example is a premise, a hypothesis, and a label (`entailment`, `neutral`, or `contradiction`), written in the Spanish of your own country or region. Latin American Spanish is the current scope. Brazilian Portuguese is planned.

```bash
git clone https://github.com/GENIA-Americas/multimodal-ai-americas.git
cd multimodal-ai-americas
git checkout -b dataset/<github-username>-<region>

# add your examples, one JSON object per line, to:
#   datasets/amerinli/submissions/<github-username>_<region>.jsonl

python3 tools/validate_amerinli.py datasets/amerinli/submissions/<github-username>_<region>.jsonl
```

Then open a pull request. Field rules are in [datasets/amerinli/README.md](datasets/amerinli/README.md) and the workflow is in [CONTRIBUTING.md](CONTRIBUTING.md).

## Other ways to help

- Read the AmeriNLI rules and tell us where they are unclear.
- Write the AmeriNLI evaluation script. Baselines get published with their logs.
- Add or correct entries in the [dataset catalog](datasets/README.md) for the regions and languages you know.
- Help design RegioNER: entity types, annotation guide, source texts.
- Check the [literature list](research/literature/README.md) for errors and gaps.

Not sure where to start? Open an issue.

## Why this exists

The working hypothesis: multilingual models trained mostly on text from other regions handle Latin American varieties and Indigenous languages worse than they should, and standard benchmarks do not show it well. This repo is where the data to test that gets built, in the open. It has not been measured yet.

## What is in the repository

| Path | Contents |
|------|----------|
| `datasets/` | AmeriNLI and a catalog of public regional datasets |
| `research/` | Benchmark specs, a literature list, one working paper, one illustrative case study |
| `models/` | Model registry. Every entry is currently a plan. |
| `tools/` | AmeriNLI validator and a draft of the GLAPP SDK interface |
| `platform/` | Draft specs for the Glapagos platform and API |
| `policy/` | Ethics charter, regional regulatory notes, a note on H.Res.649 |
| `strategy/` | Regional AI strategy document |
| `docs/` | Manifesto, white paper, architecture notes, glossary, coverage map |
| `community/` | Governance, partners, summits, working groups |
| `media/` | Press log |

## About

Maintained by GENIA Americas Corporation with the RaceFor.AI network. Sites: [racefor.ai](https://www.racefor.ai), [glapagos.com](https://www.glapagos.com), [LinkedIn](https://www.linkedin.com/company/genia-americas/).

## Cite

Use GitHub's "Cite this repository" button ([CITATION.cff](CITATION.cff)) or the DOI above. AmeriXLM is not a released model and should not be cited as one.

## Contact

Research and partnerships: admin@genia.ai. Press: prensa@genia.ai.

## License

Apache-2.0, see [LICENSE](LICENSE). Individual papers and policy documents carry their own attribution in file headers.
