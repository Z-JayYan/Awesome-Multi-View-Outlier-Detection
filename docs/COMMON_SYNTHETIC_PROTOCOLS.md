# Common Synthetic MVOD Protocols

This document describes recurring synthetic anomaly-construction conventions in Multi-View Outlier Detection (MVOD). It does not define a universal benchmark.

## What can be stated safely

- Attribute, class, and combined/mixed corruptions recur across the literature.
- Papers commonly vary the relative proportions of those corruption types.
- Labels such as `D1` through `D6` are local configuration identifiers. They are not field-wide standardized benchmark names, and the same label can refer to different experiment-specific configurations.

## Required registry for a locally named D1–D6 suite

| Field | Example description, not a prescribed value |
|---|---|
| `attribute_ratio` | Fraction of instances receiving within-view corruption |
| `class_ratio` | Fraction receiving cross-class re-pairing |
| `combined_ratio` | Fraction receiving both operators, if applicable |
| `affected_views` | Fixed, random, or all views |
| `operator` | Swap, replacement, additive noise, or paper-specific code |
| `preprocessing_order` | Before or after corruption |
| `source` | Exact paper section and code path/commit |

No numeric D1–D6 table is included because the reviewed public evidence does not justify treating one mapping as field-wide. A contribution may document a paper-specific mapping only when it cites the exact paper or code and identifies the labels as local to that source.
