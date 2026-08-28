# Experiment-Level Protocol Reconstructions

Generated from `data/protocols.yaml`. Completeness is a maintenance signal, not a paper-quality score. Unknown primary-source facts remain unknown.

## DMOD — Dual-Regularized Multi-View Outlier Detection

- **Record / track:** `dmod-main-uci` / `core_mvod`
- **Dataset variants:** `uci-feature-split-dmod`
- **View / training:** `complete` / `unsupervised`
- **Anomaly operators:** attribute — replace selected sample features in every view with random values; class — select objects from different classes and swap one view while leaving the other unchanged; mixed — none in the reported main protocol
- **Ratios:** [[0.08, 0.02, 0], [0.05, 0.05, 0], [0.02, 0.08, 0]] (total samples; tuple order is attribute/class/mixed)
- **Evaluation:** AUROC; 50 repetitions; mean and standard deviation
- **Code match:** `unknown` — no official code verified
- **Completeness:** **84%** (dataset 100%, preprocessing 100%, anomaly 100%, evaluation 83%, code 12%)
- **Remaining blockers:** random-value distribution, view split boundary, overlap policy, random seeds

## LDSR — Latent Discriminant Subspace Representations for Multi-View Outlier Detection

- **Record / track:** `ldsr-main` / `core_mvod`
- **Dataset variants:** `uci-feature-split-ldsr`
- **View / training:** `complete` / `unsupervised`
- **Anomaly operators:** attribute — replace a selected sample's features in every view with random values; class — cross-class pair swap in ceil(V/2) views; mixed — cross-class pair swap in ceil(V/2) views and random replacement in remaining views
- **Ratios:** [[0.05, 0.05, 0.05], [0.1, 0.1, 0]] (total samples; tuple order is attribute/class/mixed)
- **Evaluation:** AUROC; 50 repetitions; mean and standard deviation
- **Code match:** `partial` — official demo selects the best mean AUC across parameter combinations; paper only states tuning and best results, and random seeds are unset
- **Completeness:** **94%** (dataset 100%, preprocessing 75%, anomaly 100%, evaluation 83%, code 100%)
- **Remaining blockers:** random-value distribution, exact feature split boundaries, seeds, normalization

## MODDIS — Multi-view Outlier Detection in Deep Intact Space

- **Record / track:** `moddis-official-code` / `core_mvod`
- **Dataset variants:** `unresolved-moddis`
- **View / training:** `complete` / `unsupervised`
- **Anomaly operators:** attribute — generate random Uniform(0,1) feature vectors; class — swap feature blocks between randomly selected pairs; mixed — combines swap and random-value blocks
- **Ratios:** [[0.05, 0.05, 0.05]] (base data_num in official code)
- **Evaluation:** AUROC; 10 repetitions; mean and standard deviation printed by code
- **Code match:** `unknown` — public data directory is empty, preventing dataset and paper/code result reproduction
- **Completeness:** **94%** (dataset 100%, preprocessing 100%, anomaly 87%, evaluation 83%, code 88%)
- **Remaining blockers:** dataset identities and variants, paper/code match, exact class and mixed affected-view rule, seeds

## NCMOD — Neighborhood Consensus Networks for Unsupervised Multi-view Outlier Detection

- **Record / track:** `ncmod-main` / `core_mvod`
- **Dataset variants:** `ncmod-mnist-1000`, `ncmod-reuters-1000`, `ncmod-ttc-1000`
- **View / training:** `complete` / `unsupervised`
- **Anomaly operators:** attribute — replace all-view features with an object sampled from outlier classes; class — randomly pair samples and swap feature vectors in floor(V/2) views; mixed — swap in floor(V/2) views and use outlier-class object features in remaining views
- **Ratios:** [[0.02, 0.05, 0.08], [0.02, 0.08, 0.05], [0.05, 0.02, 0.08], [0.05, 0.08, 0.02], [0.08, 0.02, 0.05], [0.08, 0.05, 0.02]] (total N=1000; tuple order attribute/class/mixed)
- **Evaluation:** AUROC, F1; unknown repetitions; scalar AUC/F1; paper tables do not report deviation
- **Code match:** `partial` — paper says source including dataset generation is supplied, but audited repository expects pre-generated CSVs and contains no generator
- **Completeness:** **91%** (dataset 100%, preprocessing 75%, anomaly 100%, evaluation 71%, code 88%)
- **Remaining blockers:** repetitions and seeds, normalization, inlier class choices, missing official generation script

## SRLSP — A Self-Representation Method with Local Similarity Preserving for Fast Multi-View Outlier Detection

- **Record / track:** `srlsp-public-artifact` / `core_mvod`
- **Dataset variants:** `unresolved-srlsp`
- **View / training:** `complete` / `unsupervised`
- **Anomaly operators:** attribute — unknown; class — unknown; mixed — unknown
- **Ratios:** unknown (unknown)
- **Evaluation:** AUROC; unknown repetitions; AUROC returned by perfcurve
- **Code match:** `unknown` — official repository exposes only the core algorithm and cannot reconstruct paper experiments
- **Completeness:** **51%** (dataset 100%, preprocessing 0%, anomaly 20%, evaluation 67%, code 88%)
- **Remaining blockers:** paper datasets, feature variants, all anomaly operators and ratios, preprocessing, repetitions and seeds

## IAMOD — Information-aware Multi-view Outlier Detection

- **Record / track:** `iamod-public-artifact` / `core_mvod`
- **Dataset variants:** `iamod-caltech7-code`
- **View / training:** `complete` / `unsupervised`
- **Anomaly operators:** attribute — pre-generated files referenced; class — pre-generated files referenced; mixed — pre-generated files referenced
- **Ratios:** unknown (unknown)
- **Evaluation:** AUROC; 10 repetitions; mean and standard deviation
- **Code match:** `unknown` — public runner selects the best test AUROC across epochs and uses absolute author-local data paths; dataset files are not distributed
- **Completeness:** **67%** (dataset 100%, preprocessing 75%, anomaly 40%, evaluation 83%, code 88%)
- **Remaining blockers:** paper experiment tables, dataset dimensions, anomaly operators and ratios, epoch selection correspondence to paper, seeds

## MODGD — Multi-view Outlier Detection via Graphs Denoising

- **Record / track:** `modgd-main` / `core_mvod`
- **Dataset variants:** `modgd-caltech101-six-view`
- **View / training:** `complete` / `unsupervised`
- **Anomaly operators:** attribute — random feature alteration; class — swap paired sample features in a partial set of views; mixed — combine partial-view swapping with random replacement in remaining views
- **Ratios:** [[0.02, 0.05, 0.08], [0.02, 0.08, 0.05], [0.05, 0.02, 0.08], [0.05, 0.08, 0.02], [0.08, 0.02, 0.05], [0.08, 0.05, 0.02]] (total instances; tuple order attribute/class/mixed)
- **Evaluation:** AUROC; 5 repetitions; mean and standard deviation
- **Code match:** `unknown` — unversioned ZIP prevents commit-level provenance; paper Table 2 labels six views but prints seven Caltech dimension values
- **Completeness:** **85%** (dataset 100%, preprocessing 75%, anomaly 100%, evaluation 83%, code 38%)
- **Remaining blockers:** Caltech dimension inconsistency, exact random replacement distribution, exact swapped-view count, seeds, ZIP commit identity

## RCPMOD — Regularized Contrastive Partial Multi-view Outlier Detection

- **Record / track:** `rcpmod-main` / `partial_mvod`
- **Dataset variants:** `rcpmod-four-benchmarks`
- **View / training:** `partial` / `unsupervised`
- **Anomaly operators:** attribute — replace selected instance features in all views with random values; class — swap paired samples in floor(V/2) views; mixed — swap in floor(V/2) views and replace remaining views with random values
- **Ratios:** [[0.02, 0.05, 0.08], [0.02, 0.08, 0.05], [0.05, 0.02, 0.08], [0.05, 0.08, 0.02], [0.08, 0.02, 0.05], [0.08, 0.05, 0.02]] (total samples; tuple order attribute/class/mixed)
- **Evaluation:** AUROC; unknown repetitions; mean and standard deviation in tables
- **Code match:** `unknown` — no author-verified official repository established
- **Completeness:** **78%** (dataset 100%, preprocessing 75%, anomaly 100%, evaluation 67%, code 12%)
- **Remaining blockers:** random-value distribution, anomaly/view-removal ordering, repetitions, seeds, official code

## LRTDM — Low-rank Tucker decomposition for multi-view outlier detection based on meta-learning

- **Record / track:** `lrtdm-accessible-evidence` / `core_mvod`
- **Dataset variants:** `unresolved-lrtdm`
- **View / training:** `complete` / `unsupervised`
- **Anomaly operators:** attribute — unknown; class — unknown; mixed — unknown
- **Ratios:** unknown (unknown)
- **Evaluation:** unknown; unknown repetitions; unknown
- **Code match:** `unknown` — no official code verified
- **Completeness:** **21%** (dataset 100%, preprocessing 0%, anomaly 20%, evaluation 0%, code 12%)
- **Remaining blockers:** all dataset variants, anomaly generation and ratios, preprocessing, training endpoint, evaluation, code

## SCoNE — SCoNE: Spherical Consistent Neighborhoods Ensemble for Effective and Efficient Multi-View Anomaly Detection

- **Record / track:** `scone-main` / `core_mvod`
- **Dataset variants:** `scone-uci-three-view`, `scone-caltech-six-view`
- **View / training:** `complete` / `unsupervised`
- **Anomaly operators:** attribute — randomly alter features of selected samples; class — exchange features between selected sample pairs in a partial set of views; mixed — partial-view pair swap followed by random data in remaining views
- **Ratios:** [[0.02, 0.08, 0.05], [0.05, 0.05, 0.05], [0.08, 0.02, 0.05]] (total samples; tuple order attribute/class/mixed normalized by registry)
- **Evaluation:** AUROC; 20 repetitions; mean plus/minus 2 standard errors
- **Code match:** `unknown` — no official code linked by primary sources
- **Completeness:** **80%** (dataset 100%, preprocessing 75%, anomaly 100%, evaluation 83%, code 12%)
- **Remaining blockers:** normalization, exact corruption operators, overlap policy, seeds, official code

## RNAMOD — Reliable Neighborhood-Aware Multi-View Outlier Detection

- **Record / track:** `rnamod-public-record` / `core_mvod`
- **Dataset variants:** `unresolved-rnamod`
- **View / training:** `complete` / `unsupervised`
- **Anomaly operators:** attribute — unknown; class — unknown; mixed — unknown
- **Ratios:** unknown (unknown)
- **Evaluation:** unknown; unknown repetitions; unknown
- **Code match:** `unknown` — author page exposes placeholder paper/code links and no verified artifact
- **Completeness:** **24%** (dataset 100%, preprocessing 0%, anomaly 20%, evaluation 17%, code 12%)
- **Remaining blockers:** dataset names and variants, all corruption operators and ratios, preprocessing, training/evaluation protocol, official code
