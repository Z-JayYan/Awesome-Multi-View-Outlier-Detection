# Protocol Comparability

Two papers using the same dataset name are **not automatically comparable**. In particular, “BBCSport” may refer to different feature partitions, preprocessing, anomaly construction, contamination ratios, repetitions, or sample selections.

The machine-readable rules are in [`data/comparability.yaml`](../data/comparability.yaml), and each paper's known protocol evidence is stored under `protocol` in [`data/papers.yaml`](../data/papers.yaml).

## Conservative statuses

| Status | Meaning |
|---|---|
| `DIRECTLY_COMPARABLE` | All relevant captured fields are verified and match. |
| `CONDITIONALLY_COMPARABLE` | The task boundary is compatible, but one or more known protocol choices differs and must be controlled or explained. |
| `NOT_DIRECTLY_COMPARABLE` | Task setting, view completeness, endpoint, feature level, or another hard boundary is incompatible. |
| `UNKNOWN` | Essential evidence is missing for at least one paper. Unknown never means “probably comparable.” |

## Track-level matrix

| A \ B | CORE complete-view | Partial / incomplete | Industrial / natural |
|---|---|---|---|
| **CORE complete-view** | Conditional pending fingerprint match | Not direct | Not direct |
| **Partial / incomplete** | Not direct | Conditional pending missingness/protocol match | Not direct |
| **Industrial / natural** | Not direct | Not direct | Conditional pending camera, backbone, split, and endpoint match |

## Decision order

1. Reject a direct comparison when view setting or evaluation endpoint is incompatible.
2. Require the same exact dataset variant—not only the same display name.
3. Compare anomaly generation, affected views, contamination, preprocessing, feature source/backbone, train/test setting, metric, endpoint, repetitions, and seeds.
4. Return `UNKNOWN` whenever an essential field has not been verified.
5. Use `DIRECTLY_COMPARABLE` only when the relevant complete fingerprint is verified and equal.

Use `python scripts/compare_protocols.py PAPER_ID_A PAPER_ID_B` for a conservative registry-level check. The tool intentionally refuses to turn missing evidence into a score.

## Result reporting policy

This repository does not publish a cross-protocol leaderboard. Results that do not meet the direct-comparability rule may be documented only as **Reported Result Context — not directly comparable**.
