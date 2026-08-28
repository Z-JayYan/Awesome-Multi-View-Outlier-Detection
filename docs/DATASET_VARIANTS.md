# Dataset Variant Registry

**English** | [简体中文](DATASET_VARIANTS.zh-CN.md)

Generated from `data/dataset_variants.yaml`. A common dataset label is not evidence of a common N × V × feature × preprocessing protocol.

## 100Leaves

### `audit-100leaves-unresolved`

- **Used by:** none (audit-only record)
- **N / views / dimensions:** unknown / unknown / unknown
- **Features:** IAMOD code references a generic leaf path but does not establish this canonical dataset identity
- **Preprocessing:** unknown
- **Resolution:** `unresolved`

## BBCSport

### `audit-bbcsport-unresolved`

- **Used by:** none (audit-only record)
- **N / views / dimensions:** unknown / unknown / unknown
- **Features:** unknown
- **Preprocessing:** no Priority Paper primary source in this audit established an attributable BBCSport variant
- **Resolution:** `unresolved`

## BDGP / Scene15 / LandUse21 / Fashion-MNIST

### `rcpmod-four-benchmarks`

- **Used by:** `rcpmod-2024`
- **N / views / dimensions:** [2500, 4568, 2100, 10000] / [2, 3, 3, 3] / unknown
- **Features:** four complete multi-view benchmarks transformed into partial-view data
- **Preprocessing:** randomly remove one view from selected instances at missing rates 0, 0.15, 0.30, 0.45
- **Resolution:** `partially_resolved`

## Caltech101

### `modgd-caltech101-six-view`

- **Used by:** `modgd-2024`
- **N / views / dimensions:** 9144 / 6 / [48, 40, 254, 1984, 512, 680, 32]
- **Features:** published six-view feature benchmark; paper table prints seven dimension values, an unresolved inconsistency
- **Preprocessing:** KNN graphs normalized in the method; raw feature scaling not reported
- **Resolution:** `partially_resolved`

### `scone-caltech-six-view`

- **Used by:** `scone-2026`
- **N / views / dimensions:** 1474 / 6 / total dimension 3766; per-view dimensions unknown
- **Features:** original six-view Caltech variant used by IAMOD lineage
- **Preprocessing:** unknown
- **Resolution:** `partially_resolved`

### `iamod-caltech7-code`

- **Used by:** `iamod-2024`
- **N / views / dimensions:** unknown / unknown / unknown
- **Features:** caltech7.mat, absent from the public repository
- **Preprocessing:** row normalization applied independently to every loaded view
- **Resolution:** `unresolved`

## CiteSeer

### `audit-citeseer-unresolved`

- **Used by:** none (audit-only record)
- **N / views / dimensions:** unknown / unknown / unknown
- **Features:** unknown
- **Preprocessing:** a bibliography citation is not evidence of an experiment variant
- **Resolution:** `unresolved`

## MNIST

### `ncmod-mnist-1000`

- **Used by:** `ncmod-2021`
- **N / views / dimensions:** 1000 / [2, 3] / original 784 dimensions split into contiguous subsets
- **Features:** class-labelled benchmark features
- **Preprocessing:** select inlier classes, sample N=1000, then split the original feature vector by view
- **Resolution:** `resolved`

## NUSWIDEOBJ

### `audit-nuswideobj-unresolved`

- **Used by:** none (audit-only record)
- **N / views / dimensions:** unknown / unknown / unknown
- **Features:** unknown
- **Preprocessing:** no Priority Paper primary source in this audit resolved the feature/view construction
- **Resolution:** `unresolved`

## Reuters

### `ncmod-reuters-1000`

- **Used by:** `ncmod-2021`
- **N / views / dimensions:** 1000 / [2, 3] / original 2000 dimensions split into contiguous subsets
- **Features:** class-labelled Reuters benchmark features; exact corpus preprocessing upstream is unknown
- **Preprocessing:** select inlier classes, sample N=1000, then split the feature vector by view
- **Resolution:** `partially_resolved`

## TTC

### `ncmod-ttc-1000`

- **Used by:** `ncmod-2021`
- **N / views / dimensions:** 1000 / [2, 3] / original 7507 dimensions split into contiguous subsets
- **Features:** class-labelled TTC benchmark features
- **Preprocessing:** select inlier classes, sample N=1000, then split the feature vector by view
- **Resolution:** `partially_resolved`

## UCI tabular benchmarks

### `uci-feature-split-dmod`

- **Used by:** `dmod-2015`
- **N / views / dimensions:** [150, 569, 351, 20000] / 2 / feature vector split into two subsets; exact boundary unknown
- **Features:** iris, breast, ionosphere, and letter from UCI
- **Preprocessing:** per-sample L2 normalization after view construction
- **Resolution:** `partially_resolved`

### `uci-feature-split-ldsr`

- **Used by:** `ldsr-2018`
- **N / views / dimensions:** [101, 1300, 178, 569, 768] / [2, 3] / contiguous feature subsets; exact boundaries unknown
- **Features:** zoo, letter subset, wine, wdbc, and pima from UCI
- **Preprocessing:** letter subsampled to 50 examples per class; features split into V subsets
- **Resolution:** `partially_resolved`

## unresolved

### `unresolved-srlsp`

- **Used by:** `srlsp-2023`
- **N / views / dimensions:** unknown / unknown / unknown
- **Features:** unknown
- **Preprocessing:** official repository contains only the algorithm, not experiment data or runner
- **Resolution:** `unresolved`

### `unresolved-lrtdm`

- **Used by:** `lrtdm-2025`
- **N / views / dimensions:** unknown / unknown / unknown
- **Features:** unknown
- **Preprocessing:** unknown
- **Resolution:** `unresolved`

### `unresolved-rnamod`

- **Used by:** `rnamod-2026`
- **N / views / dimensions:** unknown / unknown / unknown
- **Features:** unknown
- **Preprocessing:** unknown
- **Resolution:** `unresolved`

### `unresolved-moddis`

- **Used by:** `moddis-2019`
- **N / views / dimensions:** unknown / unknown / unknown
- **Features:** official repository data directory is empty in the audited commit
- **Preprocessing:** min-max scaling per feature is implemented in Methods.py
- **Resolution:** `unresolved`

## Zoo / Parkinson / Wdbc / MNIST

### `scone-uci-three-view`

- **Used by:** `scone-2026`
- **N / views / dimensions:** [101, 197, 569, 70000] / 3 / original features split into three subsets
- **Features:** UCI benchmark features
- **Preprocessing:** feature splitting; exact split boundaries and scaling unknown
- **Resolution:** `partially_resolved`
