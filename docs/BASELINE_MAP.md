# Baseline Map

A baseline suite should cover distinct evidence mechanisms, not merely maximize the number of old methods.

| Role | Representative family | Why include | Code caution | Scalability concern |
|---|---|---|---|---|
| Historical | cluster/affinity disagreement | Establishes the early class-anomaly formulation | Implementations are often unavailable or non-canonical | Pairwise views and clustering sensitivity |
| Classical structured | DMOD / CRMOD / MLRA / LDSR | Covers coefficients, low rank, and consensus representations | Verify exact version and preprocessing | Matrix factorization; some formulations scale poorly with samples/views |
| Probabilistic | robust PLVM / hierarchical Bayesian / shared latent | Tests whether one latent cause explains all views | Hyperparameters and inference details matter | Iterative inference and dense latent projections |
| Deep representation | MODDIS / fast encoder / CGAEs | Covers nonlinear intact-space and reconstruction evidence | “Code available” must point to an official repository | Training cost; pairwise cross-reconstruction can grow with views |
| Local structure | neighborhood MVAD / NCMOD / SRLSP | Avoids a strict global cluster assumption | Neighbor construction and `k` selection affect results | Exact KNN and dense similarities can dominate memory |
| Graph | graph denoising / optimal graph filtering | Represents relational denoising and filtering | Graph construction must match the paper | Dense \(N\times N\) graphs are a common risk |
| Contrastive / information | dPoE / RCPMOD / information-aware | Tests alignment and disentangled fusion | Partial-view masks and augmentations must be preserved | Batch negatives, memory, and view count |
| Partial-view | collective learning / RCPMOD / incomplete-view models | Required when views are missing | Complete-view results do not substitute | Imputation/fusion plus anomaly scoring |
| Recent frontier | SCoNE, tensor/high-order, verified 2025–2026 entries | Probes efficiency and newer evidence models | Treat preprints separately from proceedings | Check reported vs. derived complexity |

## Minimal defensible suite

For classical complete-view MVOD, select at least one structured representation method, one local/graph method, one deep or probabilistic model, and one recent information/contrastive method. For partial MVOD add at least one method designed for missing views. Match the protocol before interpreting wins.
