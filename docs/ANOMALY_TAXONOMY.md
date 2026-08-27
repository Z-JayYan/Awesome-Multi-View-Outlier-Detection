# Anomaly Taxonomy

## Attribute anomaly

An instance is unusual because its observed features deviate within one or more views. Synthetic protocols may replace a feature vector, perturb features with noise, or inject an outlying sample. Those procedures are not equivalent.

## Class anomaly

Each view can look individually plausible, but the aligned views are semantically incompatible. A common synthetic construction swaps or re-pairs one view between instances from different classes. The number of modified views and class-selection rule matter.

## Class-attribute / mixed anomaly

Both within-view deviation and cross-view incompatibility are present. Some papers use “class-attribute” for an explicitly combined sample; others use “mixed” for a dataset containing separate attribute and class anomalies. Registry notes should preserve that distinction whenever the paper makes it clear.

## Generic multi-view outlier

Some work defines an outlier through low likelihood, cluster disagreement, or relational inconsistency without adopting the attribute/class taxonomy. Such work is tagged `generic`, not retrofitted to a later corruption scheme.

## Natural anomaly

The related multimodal track uses real defects or abnormal events. Its image-level, object-level, or pixel-level ground truth is not comparable to a synthetic tabular class anomaly.

## Missing-view setting

Missingness is a data-availability condition, not automatically an anomaly label. Partial MVOD may combine ordinary anomaly types with MCAR/MAR-like missing-view masks; both mechanisms must be reported.

> Different MVOD papers use related terminology but may implement different anomaly-generation protocols.

Minimum reporting: exact modification operator, anomaly ratio, selected views, replacement/noise distribution, label-based sampling rule, random seed policy, and whether train data are contaminated.
