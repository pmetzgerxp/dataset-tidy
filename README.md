# dataset-tidy

Fine-tune data hygiene: dedup, length filter, train/valid split

Built for my own use; public in case it helps someone.

## How to use

```bash
python prep.py raw.jsonl --out-dir data/ --valid-ratio 0.1
```

## What it does

- Dedup by normalized instruction text
- Length filters keep the sweet spot
- Prints a stats summary you can eyeball
- Deterministic split with a seed

## Getting started

```bash
# stdlib only
```

## Project structure

```text
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   └── bug_report.md
│   └── pull_request_template.md
├── docs/
│   ├── configuration.md
│   ├── development.md
│   ├── faq.md
│   └── usage.md
├── tests/
│   └── test_smoke.py
├── .gitattributes
├── .gitignore
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── SECURITY.md
└── prep.py
```

## Development

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m pytest -q
```

## Known issues

- none reported yet (surprisingly)

## License

MIT licensed, see LICENSE.
