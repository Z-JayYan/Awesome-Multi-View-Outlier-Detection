# Contributing to Awesome-MVOD

Thank you for helping improve the registry. Accuracy and traceability are more important than list length.

## Add a paper

1. Confirm that anomaly/outlier detection is a primary task and that the method explicitly uses relations between at least two aligned views.
2. Add one entry to `data/papers.yaml`; use normalized title plus publication year to check duplicates.
3. Use only tags from `data/taxonomy.yaml`. Multiple mechanism tags are allowed, but keep the set minimal.
4. Cite a publisher/conference page, official arXiv manuscript, or DBLP record for title/year/venue.
5. Add a code URL only when the paper, author, or official project page establishes ownership. Otherwise use `code: null` and `code_status: not_found` or `unknown`.
6. Add one neutral sentence answering: “What cross-view signal is used to detect anomalies?” Do not copy the abstract.
7. Record dataset names only when the paper or official code verifies them.
8. Run:

   ```bash
   python scripts/validate_registry.py
   python scripts/generate_tables.py
   python scripts/validate_registry.py
   ```

## Entry template

```yaml
- id: method-2026
  title: Full verified title
  acronym: METHOD
  authors: [First Author, Second Author]
  year: 2026
  online_year: null
  venue: arXiv
  venue_type: preprint
  venue_status: preprint
  track: uncertain
  status: partially_verified
  featured: false
  tasks: [multi_view_outlier_detection]
  mechanisms: [local_structure]
  anomaly_types: [generic]
  evidence_levels: [local]
  representation: {learned: true}
  partial_view: false
  datasets: []
  summary: Detects anomalies through disagreement of local neighborhood relations across views.
  links:
    paper: https://arxiv.org/abs/...
    arxiv: https://arxiv.org/abs/...
    code: null
    project: null
    dblp: null
  code_status: unknown
  link_status: verified
  verified_from:
    - kind: arxiv
      url: https://arxiv.org/abs/...
      facts: [title, authors, year, method]
  complexity: {reported: null, provenance: unknown, notes: null}
  reproducibility:
    official_code: unknown
    official_config: unknown
    dataset_instructions: unknown
    pretrained_weights: unknown
    environment: unknown
    license: unknown
  notes: Explain uncertainty instead of guessing.
```

## Scope and venue quality

Ordinary multi-view clustering/classification and single-view anomaly detection are out of scope. A paper without a confirmed formal venue can be included as a preprint when a stable public manuscript exists. Do not invent a proceedings status. Unverifiable, deceptive, or predatory publications should not be added.

## Corrections

Corrections should cite a stronger source than the current entry. Acronyms are not identifiers; never merge records solely because two papers use the same acronym.
