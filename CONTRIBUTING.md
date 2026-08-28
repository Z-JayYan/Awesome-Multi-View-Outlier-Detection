# Contributing to Awesome Multi-View Outlier Detection

Accuracy, task boundaries, and traceable evidence matter more than paper count. Do not edit generated tables in `README.md`, `docs/PAPERS.md`, `docs/DATASETS.md`, or `docs/BASELINE_MAP.md` directly; update the registries and run the generator.

## Add or correct a paper

A submission must include:

- official full title and complete author list;
- venue, publication year, and venue status;
- an official paper source (publisher, proceedings, author project, or arXiv);
- task Track and view setting;
- minimal method/evidence tags from `data/taxonomy.yaml`;
- official-code status and the evidence establishing repository ownership;
- dataset references only when verified;
- protocol notes/fingerprint fields, using `unknown` for unreported values;
- `verified_from` sources listing the specific facts each source supports;
- baseline relevance only when the card neutrally explains why a researcher should compare.

Do not assign a Track from the title alone. `CORE` is a complete-view task setting, not a synonym for shallow or non-deep. A missing-view industrial-camera method is not automatically partial MVOD.

## Evidence hierarchy

Prefer official proceedings/publisher pages, then author/project pages and official GitHub repositories, followed by arXiv and DBLP. Search results, Papers With Code-style aggregators, and unrelated GitHub repositories do not establish official code status.

If a field cannot be established from public evidence, use `unknown`, explain it in `notes`, and do not infer a likely value.

## Protocol fingerprint

Every paper requires a `protocol` block covering:

- complete, partial/incomplete, industrial, or unknown view setting;
- anomaly types and generation details;
- contamination and training contamination;
- normalization, dimension reduction, feature source, and backbone;
- metrics, repetitions, seeds, and evaluation endpoint;
- dataset variants, train/test splits, and normal-only training;
- verification sources and confidence.

For synthetic anomaly suites, also read [`docs/COMMON_SYNTHETIC_PROTOCOLS.md`](docs/COMMON_SYNTHETIC_PROTOCOLS.md). Labels such as D1–D6 must be documented as source-local configuration identifiers, never as field-wide standard benchmark names.

Unknown protocol evidence is valid. A fabricated complete fingerprint is not.

## Dataset submissions

Add the official source, aliases, task Track, sample/view counts, dimensions, modality/feature type, labels, known variants, common preprocessing, protocol notes, and industrial camera/annotation details when applicable. Counts that vary by derived benchmark must remain `unknown` or variant-specific.

## Comparability and results

Do not add a leaderboard row merely because two papers use the same dataset name or metric. A comparable-results table requires a verified match on the factors in `data/comparability.yaml`. Otherwise label values **Reported Result Context — not directly comparable**.

## Required checks

```bash
python scripts/validate_registry.py
python scripts/generate_tables.py
python scripts/validate_registry.py
python -m unittest discover -s tests -v
git diff --exit-code
git diff --check
```

`git diff --exit-code` is the generated-file freshness check after generation. CI also validates JSON Schemas, duplicate paper identities, duplicate DOIs, dataset references, and internal Markdown links.

## Research neutrality

Apply the same schema and evidentiary standard to every method. Do not star an affiliated method, disparage competitors, infer ineffectiveness from unavailable code, or cherry-pick baselines. Neutral statements such as `official code unknown`, `not reproduced`, or `protocol mismatch` are welcome when supported.
