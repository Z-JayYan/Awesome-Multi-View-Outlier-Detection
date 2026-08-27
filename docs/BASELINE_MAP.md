# Method-Level Baseline Evidence Map

Generated from the `baseline` blocks in `data/papers.yaml`. A card explains why a method is a defensible comparison; it does not create a leaderboard.

## CORE / complete-view baselines

### MOD-TDID — Multi-view outlier detection via tensor decomposition and information decoupling

- **Year / venue:** 2026 / Applied Intelligence
- **Track / view setting:** `core_mvod` / `complete`
- **Core mechanism:** tensor, graph, shared private, local structure
- **Artifact status:** [official code](https://github.com/YF-W/MOD-TDID); registry status `verified`
- **Main datasets / metrics:** unknown / unknown
- **Baseline roles:** tensor information decoupling, standard mvod
- **Closest counterfactual:** Does the new mechanism improve on tensor-regularized shared/view-specific graph decoupling?
- **Why compare:** MOD-TDID is a recent high-order information-decoupling baseline with official code and dataset instructions.
- **Why not automatically directly comparable:** Dataset variants and corruption recipes must still be matched exactly.
- **Scalability candidate:** no
- **Evidence:** [source 1](https://doi.org/10.1007/s10489-026-07375-y), [source 2](https://github.com/YF-W/MOD-TDID)

### RNAMOD — Reliable Neighborhood-Aware Multi-View Outlier Detection

- **Year / venue:** 2026 / ICML
- **Track / view setting:** `core_mvod` / `complete`
- **Core mechanism:** local structure, graph, correspondence
- **Artifact status:** unknown; registry status `verified`
- **Main datasets / metrics:** unknown / unknown
- **Baseline roles:** strong frontier, neighborhood reliability representative, standard mvod, scalability candidate
- **Closest counterfactual:** Can a new method outperform reliable-neighborhood and scale-invariant directional consensus under the same complete-view protocol?
- **Why compare:** RNAMOD is a 2026 complete-view frontier method explicitly designed to prevent outlier propagation through unreliable neighborhoods.
- **Why not automatically directly comparable:** Direct comparison still requires matched datasets, corruption generation, preprocessing, contamination, metrics, and repetitions.
- **Scalability candidate:** yes
- **Evidence:** [source 1](https://openreview.net/forum?id=mL4B6DdgPU)

### SCoNE — SCoNE: Spherical Consistent Neighborhoods Ensemble for Effective and Efficient Multi-View Anomaly Detection

- **Year / venue:** 2026 / AAAI
- **Track / view setting:** `core_mvod` / `complete`
- **Core mechanism:** local structure, ensemble, probabilistic neighborhood
- **Artifact status:** unknown; registry status `verified`
- **Main datasets / metrics:** unknown / unknown
- **Baseline roles:** efficient neighborhood ensemble, standard mvod, scalability candidate
- **Closest counterfactual:** Can the proposed model beat a nonparametric spherical consistent-neighborhood ensemble at comparable cost?
- **Why compare:** SCoNE is an efficiency-oriented 2026 neighborhood ensemble and a useful counterpoint to learned deep models.
- **Why not automatically directly comparable:** Its exact implementation and full protocol remain insufficiently captured for direct table-level comparison.
- **Scalability candidate:** yes
- **Evidence:** [source 1](https://doi.org/10.1609/AAAI.V40I19.38643)

### LRTDM — Low-rank Tucker decomposition for multi-view outlier detection based on meta-learning

- **Year / venue:** 2025 / Information Fusion
- **Track / view setting:** `core_mvod` / `complete`
- **Core mechanism:** tensor, low rank, self representation, shared latent
- **Artifact status:** unknown; registry status `verified`
- **Main datasets / metrics:** unknown / unknown
- **Baseline roles:** tensor low rank representative, standard mvod, scalability candidate
- **Closest counterfactual:** Does the method improve on high-order low-rank self-expression and meta-learned view fusion?
- **Why compare:** LRTDM is a recent tensor baseline and exposes the cost/benefit of quadratic sample interactions.
- **Why not automatically directly comparable:** Compare only under matching tensor construction, preprocessing, anomaly ratios, and evaluation protocol.
- **Scalability candidate:** yes
- **Evidence:** [source 1](https://doi.org/10.1016/j.inffus.2025.103313)

### MGFMOD — Multi-view outlier detection based on multi-granularity fusion of fuzzy rough granules

- **Year / venue:** 2025 / International Journal of Approximate Reasoning
- **Track / view setting:** `core_mvod` / `complete`
- **Core mechanism:** local structure, probabilistic neighborhood, ensemble
- **Artifact status:** [official code](https://github.com/YF-W/MGFMOD); registry status `verified`
- **Main datasets / metrics:** unknown / unknown
- **Baseline roles:** multi granularity neighborhood, standard mvod
- **Closest counterfactual:** Does the method remain stronger than fuzzy-rough evidence fused across neighborhood granularities?
- **Why compare:** MGFMOD tests whether gains persist against a non-neural, multi-granularity local baseline with official code.
- **Why not automatically directly comparable:** Granularity selection and anomaly generation must be aligned before comparing metrics.
- **Scalability candidate:** no
- **Evidence:** [source 1](https://doi.org/10.1016/j.ijar.2025.109402), [source 2](https://github.com/YF-W/MGFMOD)

### MODGF — Unsupervised Multi-View Outlier Detection via Optimal Graph Filtering

- **Year / venue:** 2025 / ICASSP
- **Track / view setting:** `core_mvod` / `complete`
- **Core mechanism:** graph, local structure
- **Artifact status:** unknown; registry status `verified`
- **Main datasets / metrics:** unknown / unknown
- **Baseline roles:** graph filtering representative, standard mvod, scalability candidate
- **Closest counterfactual:** Does the method improve on graph-frequency filtering of multi-view outlier evidence?
- **Why compare:** Optimal Graph Filtering is a recent signal-processing baseline for relational structure.
- **Why not automatically directly comparable:** Graph variants and protocol fields are not yet complete enough for direct reported-result comparison.
- **Scalability candidate:** yes
- **Evidence:** [source 1](https://doi.org/10.1109/ICASSP49660.2025.10889803)

### IAMOD — Information-aware Multi-view Outlier Detection

- **Year / venue:** 2024 / ACM TKDD
- **Track / view setting:** `core_mvod` / `complete`
- **Core mechanism:** information theoretic, shared latent, local structure
- **Artifact status:** [official code](https://github.com/GTML-LAB/IAMOD); registry status `verified`
- **Main datasets / metrics:** unknown / unknown
- **Baseline roles:** information theoretic representative, standard mvod
- **Closest counterfactual:** Does the new evidence model add value beyond compact, non-redundant information-aware representations?
- **Why compare:** IAMOD represents information-structure reasoning without relying only on a shallow cluster or subspace assumption.
- **Why not automatically directly comparable:** Reported numbers require the same anomaly construction and feature preprocessing before direct comparison.
- **Scalability candidate:** no
- **Evidence:** [source 1](https://doi.org/10.1145/3638354), [source 2](https://github.com/GTML-LAB/IAMOD)

### MODGD — Multi-view Outlier Detection via Graphs Denoising

- **Year / venue:** 2024 / Information Fusion
- **Track / view setting:** `core_mvod` / `complete`
- **Core mechanism:** graph, local structure
- **Artifact status:** [official code](http://Doctor-Nobody.github.io/codes/MODGD.zip); registry status `verified`
- **Main datasets / metrics:** unknown / unknown
- **Baseline roles:** graph denoising representative, standard mvod
- **Closest counterfactual:** Can the new method improve on explicit view-graph denoising and consensus-graph residual evidence?
- **Why compare:** MODGD is a modern graph baseline that separates attribute evidence from structured cross-view graph disagreement.
- **Why not automatically directly comparable:** Graph construction and dataset preprocessing must match; the dataset name alone is insufficient.
- **Scalability candidate:** no
- **Evidence:** [source 1](https://doi.org/10.1016/j.inffus.2023.102012), [source 2](http://Doctor-Nobody.github.io/codes/MODGD.zip)

### SRLSP — A Self-Representation Method with Local Similarity Preserving for Fast Multi-View Outlier Detection

- **Year / venue:** 2023 / ACM TKDD
- **Track / view setting:** `core_mvod` / `complete`
- **Core mechanism:** self representation, local structure, graph
- **Artifact status:** [official code](https://github.com/wy54224/SRLSP); registry status `verified`
- **Main datasets / metrics:** unknown / unknown
- **Baseline roles:** self representation representative, local similarity representative, scalability candidate
- **Closest counterfactual:** Does the new model add evidence beyond fast self-representation with local similarity preservation?
- **Why compare:** SRLSP is a reproducible bridge between self-representation and local-neighborhood evidence.
- **Why not automatically directly comparable:** Runtime and detection numbers depend on neighbor construction, feature scaling, and corruption details.
- **Scalability candidate:** yes
- **Evidence:** [source 1](https://doi.org/10.1145/3532191), [source 2](https://github.com/wy54224/SRLSP)

### dPoE — Debunking Free Fusion Myth: Online Multi-view Anomaly Detection with Disentangled Product-of-Experts Modeling

- **Year / venue:** 2023 / ACM MM
- **Track / view setting:** `core_mvod` / `complete`
- **Core mechanism:** generative, shared private, information theoretic
- **Artifact status:** [official code](https://github.com/cshaowang/dPoE); registry status `verified`
- **Main datasets / metrics:** MNIST, Fashion-MNIST, COIL-20 / unknown
- **Baseline roles:** online deep generative anchor, shared private representative
- **Closest counterfactual:** Does the method improve on disentangled product-of-experts fusion for post-deployment scoring?
- **Why compare:** dPoE is an official-code deep generative anchor that challenges naïve free fusion.
- **Why not automatically directly comparable:** Its online scoring semantics and learned-feature protocol must not be conflated with batch shallow methods.
- **Scalability candidate:** no
- **Evidence:** [source 1](https://doi.org/10.1145/3581783.3612487), [source 2](https://github.com/cshaowang/dPoE)

### FMOD — Fast Multi-View Outlier Detection via Deep Encoder

- **Year / venue:** 2022 / IEEE Transactions on Big Data
- **Track / view setting:** `core_mvod` / `complete`
- **Core mechanism:** subspace, low rank, shared private
- **Artifact status:** not_found; registry status `verified`
- **Main datasets / metrics:** unknown / unknown
- **Baseline roles:** fast encoder anchor, scalability candidate, standard mvod
- **Closest counterfactual:** Does the new scalable method improve on sampled training followed by encoder-based scoring?
- **Why compare:** FMOD is an explicit speed-oriented deep encoder baseline.
- **Why not automatically directly comparable:** Runtime comparisons require matched hardware, sample sizes, feature dimensions, and training subsets.
- **Scalability candidate:** yes
- **Evidence:** [source 1](https://doi.org/10.1109/TBDATA.2020.3004057)

### NCMOD — Neighborhood Consensus Networks for Unsupervised Multi-view Outlier Detection

- **Year / venue:** 2021 / AAAI
- **Track / view setting:** `core_mvod` / `complete`
- **Core mechanism:** reconstruction, local structure, graph
- **Artifact status:** [official code](https://github.com/auguscl/NCMOD); registry status `verified`
- **Main datasets / metrics:** MNIST, Reuters / unknown
- **Baseline roles:** deep neighborhood consensus anchor, standard mvod
- **Closest counterfactual:** Is the new cross-view relation mechanism stronger than learned neighborhood consensus plus reconstruction?
- **Why compare:** NCMOD is a historical deep local-structure anchor with an official implementation.
- **Why not automatically directly comparable:** Latent-neighbor settings and generated anomaly types must match for a direct numerical comparison.
- **Scalability candidate:** no
- **Evidence:** [source 1](https://doi.org/10.1609/AAAI.V35I8.16873), [source 2](https://github.com/auguscl/NCMOD)

### MODDIS — Multi-view Outlier Detection in Deep Intact Space

- **Year / venue:** 2019 / ICDM
- **Track / view setting:** `core_mvod` / `complete`
- **Core mechanism:** shared latent, reconstruction, shared private
- **Artifact status:** [official code](https://github.com/sigerma/ICDM-2019-MODDIS); registry status `verified`
- **Main datasets / metrics:** unknown / unknown
- **Baseline roles:** deep intact space anchor, standard mvod
- **Closest counterfactual:** Does the representation improve on nonlinear intact-space modeling of shared and inconsistent factors?
- **Why compare:** MODDIS is an official-code historical deep baseline for complete-view MVOD.
- **Why not automatically directly comparable:** Architecture, contamination, and synthetic anomaly generation must match for direct comparison.
- **Scalability candidate:** no
- **Evidence:** [source 1](https://doi.org/10.1109/ICDM.2019.00136), [source 2](https://github.com/sigerma/ICDM-2019-MODDIS)

### LDSR — Latent Discriminant Subspace Representations for Multi-View Outlier Detection

- **Year / venue:** 2018 / AAAI
- **Track / view setting:** `core_mvod` / `complete`
- **Core mechanism:** subspace, low rank, shared private
- **Artifact status:** [official code](https://github.com/kailigo/mvod); registry status `verified`
- **Main datasets / metrics:** unknown / unknown
- **Baseline roles:** low rank subspace anchor, standard mvod
- **Closest counterfactual:** Does the method add value beyond view-consistent and view-specific discriminant subspaces?
- **Why compare:** LDSR is a widely reused official-code low-rank baseline covering attribute, class, and mixed anomalies.
- **Why not automatically directly comparable:** Its dataset variants and preprocessing cannot be inferred from dataset names alone.
- **Scalability candidate:** no
- **Evidence:** [source 1](https://doi.org/10.1609/AAAI.V32I1.11826), [source 2](https://github.com/kailigo/mvod)

### DMOD — Dual-Regularized Multi-View Outlier Detection

- **Year / venue:** 2015 / IJCAI
- **Track / view setting:** `core_mvod` / `complete`
- **Core mechanism:** shared latent, self representation, low rank
- **Artifact status:** not_found; registry status `verified`
- **Main datasets / metrics:** unknown / unknown
- **Baseline roles:** historical structured anchor, standard mvod
- **Closest counterfactual:** Does the method improve beyond dual-regularized shared coefficients and sample-specific errors?
- **Why compare:** DMOD is a foundational complete-view reference for jointly modeling cross-view inconsistency and abnormality.
- **Why not automatically directly comparable:** Historical preprocessing and anomaly construction must be recovered before numerical reuse.
- **Scalability candidate:** no
- **Evidence:** [source 1](https://www.ijcai.org/Abstract/15/572)

## Partial / incomplete methodological baselines

### RCPMOD — Regularized Contrastive Partial Multi-view Outlier Detection

- **Year / venue:** 2024 / ACM MM
- **Track / view setting:** `partial_mvod` / `partial`
- **Core mechanism:** partial view, contrastive, local structure, shared latent
- **Artifact status:** unknown; registry status `verified`
- **Main datasets / metrics:** Fashion-MNIST / unknown
- **Baseline roles:** closest contrastive methodological, partial view representative
- **Closest counterfactual:** Does the proposed cross-view representation improve on outlier-aware contrastive learning and neighbor relation transfer?
- **Why compare:** RCPMOD is a strong conceptual baseline for contrastive cross-view relation modeling and explicitly handles missing views.
- **Why not automatically directly comparable:** Its partial-view task setting is not directly interchangeable with a complete-view CORE experiment.
- **Scalability candidate:** no
- **Evidence:** [source 1](https://doi.org/10.1145/3664647.3681125)

## Industrial / natural multi-view baselines

### Multi-Flow — Multi-Flow: Multi-View-Enriched Normalizing Flows for Industrial Anomaly Detection

- **Year / venue:** 2025 / CVPR Workshops
- **Track / view setting:** `related_natural_multimodal` / `industrial`
- **Core mechanism:** generative, shared latent
- **Artifact status:** [official code](https://github.com/m-kruse98/Multi-Flow); registry status `verified`
- **Main datasets / metrics:** Real-IAD / unknown
- **Baseline roles:** industrial normalizing flow, industrial multiview representative
- **Closest counterfactual:** Does the industrial method improve on cross-view message passing inside an exact-likelihood flow?
- **Why compare:** Multi-Flow is a reproducible Real-IAD baseline for sample-, image-, and pixel-level industrial endpoints.
- **Why not automatically directly comparable:** It is not directly comparable to classical feature-level MVOD or to a different backbone/endpoint protocol.
- **Scalability candidate:** no
- **Evidence:** [source 1](https://doi.org/10.1109/CVPRW67362.2025.00378), [source 2](https://github.com/m-kruse98/Multi-Flow)

### IDIF — Unveiling Multi-View Anomaly Detection: Intra-view Decoupling and Inter-view Fusion

- **Year / venue:** 2025 / AAAI
- **Track / view setting:** `related_natural_multimodal` / `industrial`
- **Core mechanism:** shared private, information theoretic, reconstruction, partial view
- **Artifact status:** [official code](https://github.com/Kerio99/IDIF); registry status `verified`
- **Main datasets / metrics:** Real-IAD / unknown
- **Baseline roles:** industrial intra inter view fusion, industrial multiview representative
- **Closest counterfactual:** Does the method improve on decoupled intra-view modeling followed by inter-view fusion?
- **Why compare:** IDIF is an official-code industrial multi-view anomaly-detection baseline on Real-IAD.
- **Why not automatically directly comparable:** Natural-defect, normal-only, backbone-dependent endpoints are not a CORE MVOD leaderboard.
- **Scalability candidate:** no
- **Evidence:** [source 1](https://doi.org/10.1609/AAAI.V39I12.33349), [source 2](https://github.com/Kerio99/IDIF)
