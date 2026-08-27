# Quality Audit

Audit date: 2026-08-27. Sampling seed: `20260827`.

## Method

The registry was shuffled with a fixed seed and the first 15 entries were checked again for title, publication year, venue/status, primary paper URL, code claim, and mechanism tags. Link checks used one low-frequency `HEAD` request per sampled paper. A 403 was recorded as publisher anti-bot behavior, not as a broken link.

## Sampled entries

1. `mlra-2015`
2. `bilateral-graph-filter-2026`
3. `hbm-2020`
4. `seem-2024`
5. `multiview-group-anomaly-2018`
6. `dpoe-2023`
7. `granular-ball-2026`
8. `mod-tdid-2026`
9. `plvm-2016`
10. `multi-flow-2025`
11. `scone-2026`
12. `sganet-2026`
13. `moddis-2019`
14. `lrtdm-2025`
15. `srlsp-2023`

## Findings and corrections

- All 15 primary URLs returned an HTTP response. Eleven resolved with 2xx statuses; four DOI targets returned 403 to an automated `HEAD` request and were retained because DOI metadata and independent indexing support them.
- Online-first vs. issue/proceedings years were kept separate for SRLSP and other affected records.
- `Multi-View Group Anomaly Detection` remains `track: uncertain` because its group-level target differs from the core aligned-instance setting.
- `Multi-Flow` and the bilateral graph-filter paper remain `partially_verified`; author/dataset/method metadata should be checked from stable proceedings full text before promotion.
- SCoNE is recorded as AAAI 2026 proceedings, with its 2025 arXiv year stored separately.
- No sampled missing-code entry was given a fabricated repository.

## Remaining uncertainty

Three of 40 records are `partially_verified`: `IMMoE` is no longer among them after arXiv/official-code verification; remaining partial records are `multi-flow-2025`, `bilateral-graph-filter-2026`, and `multiview-group-anomaly-2018`. A later audit should also expand dataset variants and exact complexity expressions, which are deliberately sparse in release 0.1.
