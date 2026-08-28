# v0.2.1 Quality Audit

Audit date: 2026-08-28.

## Public release cleanup

- The synthetic-protocol guide is published as `COMMON_SYNTHETIC_PROTOCOLS.md`; D1–D6 are explicitly local configuration identifiers rather than universal benchmark names.
- Every documented internal Markdown path is checked for existence.
- Paper, dataset, resource, taxonomy, and comparability registries are covered by validation and formal tests.
- Generated README and registry tables must remain deterministic and committed.
- Public citation and scoped license files are present without inferring a real-world maintainer name.

## Verification status

Before v0.2: 37 verified, 3 partially verified, 0 uncertain-status records.
After v0.2: 42 verified, 0 partially verified, 0 uncertain-status records.

The three v0.1 partial records were resolved as follows:

1. `multi-flow-2025`: promoted using CVPR Open Access, the authors' institute page, and the official implementation.
2. `bilateral-graph-filter-2026`: promoted using the official ICASSP 2026 schedule with the full author list.
3. `multiview-group-anomaly-2018`: bibliography promoted using DBLP and the publisher DOI; Track remains `uncertain` because group-level detection differs from aligned-instance MVOD.

RNAMOD and M2AD were added from official conference/author/arXiv/code evidence. Verification status describes bibliographic and classification confidence, not protocol completeness. Unknown protocol details remain visible in `docs/REMAINING_UNCERTAINTY.md`.

## Neutrality checks

- No method receives an affiliation-based marker or promotional badge.
- Baseline roles are counterfactual/evidence descriptions, not performance judgments.
- Missing code is recorded as `unknown` or `not_found`, never as ineffective.
- Cross-Track methods may be methodologically relevant without being numerically comparable.
- No reported AUROC leaderboard was created.

## Structural checks

- Track and view setting agree for every paper.
- Protocol anomaly types mirror the controlled registry classification.
- Dataset reverse-usage maps agree with paper references.
- Official code claims require a code URL and ownership evidence.
- Duplicate IDs, normalized title-year pairs, and DOIs are rejected.
- Internal Markdown links and generated-file freshness are checked in CI.
