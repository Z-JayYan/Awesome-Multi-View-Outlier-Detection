# Awesome-MVOD v0.2.1 Public Release Cleanup Report

Build date: 2026-08-28
Release theme: **Public Release Cleanup**

The v0.2 **Coverage + Comparability** research structure remains intact. v0.2.1 adds release-facing consistency, tests, licensing, citation, and naming cleanup without expanding the literature registry.

## Repository audit

| Metric | v0.1 | v0.2 / v0.2.1 |
|---|---:|---:|
| Total papers | 40 | 42 |
| CORE complete-view | 30 | 31 |
| Partial / incomplete | 2 | 2 |
| Industrial / natural | 7 | 8 |
| Uncertain-scope | 1 | 1 |
| Dataset cards | 12 | 13 |
| Verified records | 37 | 42 |
| Partially verified records | 3 | 0 |
| Official-code entries | 18 | 20 |

### Added

- Reliable Neighborhood-Aware Multi-View Outlier Detection (RNAMOD), ICML 2026, CORE.
- Visual Anomaly Detection under Complex View-Illumination Interplay / Multi-View Multi-Illumination Anomaly Detection (M2AD), industrial/natural benchmark.
- M2AD dataset card with synchronized view/illumination structure and named protocols.

### Corrected

- Multi-Flow: complete authors, Real-IAD dataset, official author/institute/code evidence, and reproducibility metadata.
- Bilateral Graph Filtering Framework: complete author list and official ICASSP schedule evidence.
- Multi-View Group Anomaly Detection: complete authors and DBLP evidence; scope remains explicitly uncertain.

No valid paper was removed or downgraded.

## Critical fixes

- Track definitions now identify task settings rather than model age or deep/shallow categories.
- README recent research is generated in Track → Year → Venue order.
- `docs/BASELINE_MAP.md` is generated as method-level evidence cards answering why a comparison is useful and when it is invalid.
- Every paper has a flexible machine-readable protocol fingerprint with explicit unknown values.
- `data/comparability.yaml`, `docs/COMPARABILITY.md`, and `scripts/compare_protocols.py` implement conservative comparison statuses without a leaderboard.
- Dataset cards include canonical v0.2 fields plus v0.1 compatibility aliases.
- Record-level verification debt is reduced from three partial records to zero.

## Engineering checks

- JSON Schema validation for paper and dataset entries.
- Duplicate ID/title-year/DOI detection.
- Required-field, vocabulary, dataset-reference, reverse-usage, protocol-coherence, URL, and internal Markdown-link checks.
- Generated-file freshness check in CI.
- Unit tests for conservative comparability decisions.
- Monthly, non-blocking external-link audit separated from per-commit CI to reduce publisher anti-bot false failures.
- Formal tests cover registry validation, duplicate identities, dataset references, taxonomy values, generated-file freshness, and documented internal paths.
- `data/comparability.yaml` is validated against `schemas/comparability.schema.yaml`.

## v0.2.1 release cleanup

- Published the synthetic-protocol guide as `docs/COMMON_SYNTHETIC_PROTOCOLS.md`; D1–D6 remain explicitly source-local configuration identifiers.
- Replaced the citation template with a public `CITATION.cff` using the verified GitHub maintainer identity.
- Added scoped MIT and CC BY 4.0 license files.
- Added `CHANGELOG.md` and normalized current version markers to v0.2.1.

## Publication status

- **License:** code is MIT; original documentation and curated metadata are CC BY 4.0.
- **Citation:** `CITATION.cff` identifies the maintainer as `Z-JayYan`, the identity supported by repository ownership and Git metadata. No unverified real name is asserted.

## v0.2.1 validation result

Executed on 2026-08-28:

```text
PASS: 42 papers, 13 datasets, 5 resources, 33 unique DOIs
PASS: paper, dataset, resource, taxonomy, and comparability schemas
PASS: generated tables are fresh under both generator entry points
PASS: 13 unit tests
PASS: Citation File Format 1.2.0 schema validation
PASS: Python compilation and git diff --check
```

## Remaining uncertainty

Bibliographic status is verified for all 42 records, but many protocol fields and artifact claims remain explicitly unknown. The generated, paper-by-paper list is in `docs/REMAINING_UNCERTAINTY.md`. RNAMOD in particular still lacks verified dataset names, detailed benchmark protocol, final PMLR/DOI metadata, and an official-code conclusion beyond `unknown`.
