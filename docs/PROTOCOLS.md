# Protocol Map

There is no field-wide, unique MVOD protocol. Results should be compared only after the following axes are matched.

## Attribute anomaly generation

Published studies variously perturb all views, replace one or more view vectors with random values, sample outlying points, or corrupt a subset of features. Important differences include noise distribution and scale, whether every view is changed, clipping, and whether corruption happens before or after normalization.

## Class anomaly generation

A common family of protocols selects instances from different semantic classes and swaps or re-pairs one view while retaining other views. Variants differ in the number of affected views, whether pairs are disjoint, whether class balance is preserved, and whether replacement is uniform across classes.

## Mixed / class-attribute generation

“Mixed” can mean one sample receives both operators, or a test set contains separate attribute and class anomalies. A paper must be read before translating the label into a registry tag.

## Partial / incomplete views

Report the missing rate, missingness distribution, minimum observed views, whether test missingness matches training, and whether missing views are imputed before anomaly scoring. Missingness should not be silently counted as anomaly evidence unless the task explicitly defines it that way.

## Preprocessing

The following choices can change distances and neighborhoods materially:

- feature-wise min–max scaling vs. one range per view;
- z-score standardization vs. L2 normalization;
- PCA or other dimension reduction fitted on all data vs. training only;
- zero-variance feature handling;
- sparse text normalization and TF–IDF construction;
- class/subset filtering before vs. after normalization.

## Evaluation

At minimum report AUROC computation unit, positive label, macro/micro aggregation, number of repetitions, seed policy, anomaly ratio, and confidence interval or dispersion. A single split/seed should not be presented as a stable benchmark rank.

## Comparability checklist

Two result rows are not directly comparable unless dataset variant, corruption code, view selection, preprocessing, contamination, metric, and repetition policy all match.

> Same anomaly name does not necessarily mean identical corruption protocol.
