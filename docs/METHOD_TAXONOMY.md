# Method Taxonomy

MVOD methods often combine several mechanisms. This taxonomy is therefore multi-label: it describes where anomaly evidence comes from, not whether a model is classical or deep. Task scope, code availability, and protocol completeness are recorded separately.

## 1. Cluster and consensus disagreement

These methods compare cluster assignments or cluster structure across views. An object is suspicious when it cannot join a stable cross-view consensus.

**Representative papers:** [HOAD](https://ieeexplore.ieee.org/document/6137313), [Consensus Clustering](https://doi.org/10.1109/SPW.2012.18)

**Registry tags:** `clustering`, `correspondence`, `graph`

## 2. Subspace, low-rank, and self-representation

Normal objects are expected to share a compact linear structure or explain one another with consistent coefficients. Sparse residuals and inconsistent representations provide anomaly evidence.

**Representative papers:** [DMOD](https://www.ijcai.org/Abstract/15/572), [MLRA](https://doi.org/10.1137/1.9781611974010.84), [LDSR](https://doi.org/10.1609/AAAI.V32I1.11826), [SRLSP](https://doi.org/10.1145/3532191)

**Registry tags:** `subspace`, `low_rank`, `self_representation`, `shared_latent`

## 3. Shared latent and shared-private modeling

A latent representation explains what views have in common, while shared-private models also retain view-specific information. Anomalies appear when one representation cannot explain the views consistently.

**Representative papers:** [PLVM](https://proceedings.neurips.cc/paper/2016/hash/0f96613235062963ccde717b18f97592-Abstract.html), [MODDIS](https://doi.org/10.1109/ICDM.2019.00136), [dPoE](https://doi.org/10.1145/3581783.3612487), [SeeM](https://doi.org/10.1007/978-981-97-2242-6_7)

**Registry tags:** `shared_latent`, `shared_private`, `generative`

## 4. Reconstruction and cross-view mapping

One view predicts another, or all views reconstruct through a common code. Within-view error may reveal attribute anomalies, while failed cross-view prediction may reveal inconsistent pairings. The exact interpretation depends on the paper's protocol.

**Representative papers:** [CGAEs](https://doi.org/10.1109/ICTAI52525.2021.00218), [NCMOD](https://doi.org/10.1609/AAAI.V35I8.16873), [MODDIS](https://doi.org/10.1109/ICDM.2019.00136)

**Registry tags:** `reconstruction`, `cross_view_mapping`, `shared_latent`

## 5. Local structure and neighborhood consistency

These methods compare nearest neighbors, local similarity, or an object's role in each view. They are useful when a global shared representation is too coarse to expose local inconsistency.

**Representative papers:** [SRLSP](https://doi.org/10.1145/3532191), [MODGD](https://doi.org/10.1016/j.inffus.2023.102012), [RNAMOD](https://openreview.net/forum?id=mL4B6DdgPU), [SCoNE](https://doi.org/10.1609/AAAI.V40I19.38643)

**Registry tags:** `local_structure`, `graph`, `probabilistic_neighborhood`, `ensemble`

## 6. Graph, tensor, and high-order relations

Graphs encode sample relations within a view; tensor models retain interactions across samples and views. Filtering, denoising, fusion, or sparse high-order components expose disagreement.

**Representative papers:** [MODGD](https://doi.org/10.1016/j.inffus.2023.102012), [LRTDM](https://doi.org/10.1016/j.inffus.2025.103313), [MOD-TDID](https://doi.org/10.1007/s10489-026-07375-y)

**Registry tags:** `graph`, `tensor`, `low_rank`, `local_structure`

## 7. Contrastive alignment

Contrastive objectives pull compatible views or neighborhoods together and separate incompatible evidence. A failed alignment can contribute to the anomaly score, but missing-view and complete-view protocols remain distinct.

**Representative papers:** [ECMOD](https://github.com/scu-kdde/OAM-ECMOD-2023), [RCPMOD](https://doi.org/10.1145/3664647.3681125)

**Registry tags:** `contrastive`, `correspondence`, `partial_view`

## 8. Probabilistic and information-theoretic modeling

Probabilistic models use likelihood or uncertainty; information-theoretic methods control what is shared and what remains view-specific. These signals may be combined with reconstruction or neighborhood evidence.

**Representative papers:** [PLVM](https://proceedings.neurips.cc/paper/2016/hash/0f96613235062963ccde717b18f97592-Abstract.html), [IAMOD](https://doi.org/10.1145/3638354), [SCoNE](https://doi.org/10.1609/AAAI.V40I19.38643)

**Registry tags:** `generative`, `information_theoretic`, `probabilistic_neighborhood`

## Task-setting overlays

- **Partial / incomplete MVOD:** missing views are part of the task. Methods may use relation transfer, imputation, masking, or contrastive learning.
- **Industrial / natural MVAD:** images, RGB-D, point clouds, or sensors introduce natural-defect and localization protocols that remain separate from CORE benchmarks.

## Evidence and tagging rules

Representative papers above are drawn from verified records in [`data/papers.yaml`](../data/papers.yaml). A paper may appear in several families. Tags describe the scoring mechanism, not every architectural component, and they do not imply that reported results are directly comparable.
