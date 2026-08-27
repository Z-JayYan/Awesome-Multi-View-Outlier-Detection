# Awesome-MVOD v0.2 Build Report

Build date: 2026-08-27
Release theme: **Coverage + Comparability**

## Repository audit

| Metric | v0.1 | v0.2 |
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

## Publication decisions still required

- **License:** no legal license has been selected. Candidate discussion remains owner-controlled.
- **Citation author:** repository URL, title, version, and release date are filled in `CITATION.cff.template`; a verified personal or organizational author identity is still required before renaming it to `CITATION.cff`.

## Remaining uncertainty

Bibliographic status is verified for all 42 records, but many protocol fields and artifact claims remain explicitly unknown. The generated, paper-by-paper list is in `docs/REMAINING_UNCERTAINTY.md`. RNAMOD in particular still lacks verified dataset names, detailed benchmark protocol, final PMLR/DOI metadata, and an official-code conclusion beyond `unknown`.
