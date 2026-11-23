# AmeriNLI writing guidelines

How to write good examples. Read this before your first submission. Field and file rules are in [README.md](README.md).

## What an example is

A **premise** (a sentence or two), a **hypothesis** (one sentence), and a **label** saying how the hypothesis relates to the premise. Treat both as describing the same situation.

| Label | Meaning | Test |
|-------|---------|------|
| `entailment` | The hypothesis is almost certainly true if the premise is true | Would nearly any reader accept it? |
| `contradiction` | The hypothesis is almost certainly false if the premise is true | Could both be true at once? If yes, it is not a contradiction. |
| `neutral` | The hypothesis might be true, but the premise does not settle it | Is it plausible but unconfirmed? |

Label by what a typical speaker would infer, not by strict logic. If two reasonable speakers would disagree on the label, rewrite the pair.

## Write in your own variety

The point of AmeriNLI is regional language. Use the vocabulary, idioms, and register people in your country or region actually use. Set `region` to the two-letter country code (ISO 3166-1 alpha-2) of the variety you are writing, such as `MX`, `CO`, `AR`, `PE`, `CL`.

## Do

- Write original sentences, or short paraphrases of events in your own words.
- Cover a mix of the eight domains: `news`, `legal`, `agriculture`, `health`, `education`, `commerce`, `culture`, `environment`.
- Aim for roughly equal numbers of the three labels in a file.
- Vary hypothesis length and structure.
- Read each pair out loud once. If it sounds unnatural, fix it.

## Avoid

- **Negation as the only contradiction.** If every contradiction contains "no" or "nunca", a model can learn that shortcut and the benchmark stops measuring understanding. Write contradictions that change a fact, a number, a place, or a time.
- **Hypotheses that copy the premise** with one word changed.
- **Neutral examples that are really entailments**, or the reverse. Check each one.
- Text copied from articles, books, or websites. Your own words only.
- Personal data, private individuals, or real people in a negative light.
- Hateful, sexual, or violent content.
- Anything you do not have the right to contribute.

## Examples

These are illustrations of the three labels, not part of the dataset.

| Premise | Hypothesis | Label |
|---------|------------|-------|
| La alcaldía cerró la avenida principal por obras hasta el viernes. | El tránsito por la avenida principal estará restringido esta semana. | `entailment` |
| La cooperativa vendió toda su producción de cacao a un comprador de Ecuador. | La cooperativa exportó su cacao a Perú. | `contradiction` |
| El centro de salud abrió una nueva sala de vacunación. | Hubo largas filas el primer día. | `neutral` |

## Before you open a pull request

```bash
python3 tools/validate_amerinli.py datasets/amerinli/submissions/<github-username>_<region>.jsonl
python3 tools/amerinli_stats.py datasets/amerinli/submissions/<github-username>_<region>.jsonl
```

The validator checks format. The stats script shows your label, domain, and region balance and how often negation words appear per label. Both also run automatically on pull requests.

Starting small is fine. 20 to 50 careful examples is a useful first submission.

## What reviewers check

- The label is the one most readers would choose
- No copied text, personal data, or offensive content
- The region and domain fields are accurate
- No negation shortcut or near-duplicate pairs

## No GitHub account? Use a spreadsheet

Copy [submission_template.csv](submission_template.csv), fill in one example per row, and send it to the maintainers. Spanish column headers (`premisa`, `hipótesis`, `etiqueta`, `región`, `dominio`) and Spanish labels (`implicación`, `neutral`, `contradicción`) are accepted. A maintainer converts the file, credits you in the `contributor` field, and opens the pull request:

```bash
python3 tools/csv_to_jsonl.py examples.csv --contributor "Your Name" \
    --out datasets/amerinli/submissions/<name>_<region>.jsonl
```

Nothing is written if any row has a problem, and the error says which row.
