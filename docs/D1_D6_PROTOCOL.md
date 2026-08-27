# Common Synthetic MVOD Protocols

The title intentionally avoids calling D1–D6 a universal standard. Public papers and code use several ratio grids and naming conventions; the labels are not safe to interpret without a source.

## What can be stated safely

- Attribute, class, and combined/mixed corruptions recur across the literature.
- Papers commonly vary the relative proportions of those corruption types.
- Identical labels such as `D1` can refer to experiment-specific configurations rather than a globally standardized recipe.

## Required registry for a D1–D6 suite

| Field | Example description, not a prescribed value |
|---|---|
| `attribute_ratio` | Fraction of instances receiving within-view corruption |
| `class_ratio` | Fraction receiving cross-class re-pairing |
| `combined_ratio` | Fraction receiving both operators, if applicable |
| `affected_views` | Fixed, random, or all views |
| `operator` | Swap, replacement, additive noise, or paper-specific code |
| `preprocessing_order` | Before or after corruption |
| `source` | Exact paper section and code path/commit |

No numeric D1–D6 table is included in the first release because the public evidence reviewed did not justify treating one mapping as field-wide. Contributions are welcome when they cite the exact paper/code and label the mapping as paper-specific.
