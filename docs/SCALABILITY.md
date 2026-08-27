# Scalability Registry Guide

Scalability claims are recorded only when the paper or official code supports them. Registry field `complexity.provenance` distinguishes `author_claim`, `derived`, and `unknown`.

## Operations to audit

- **Dense pairwise matrices:** memory can become quadratic in instance count.
- **Exact KNN:** graph construction may dominate even when the learning objective is linear in stored edges.
- **Pairwise view processing:** cost can grow quadratically with the number of views.
- **Matrix/tensor decomposition:** report dimensions, rank, iteration count, and convergence criterion.
- **Deep reconstruction:** distinguish training cost from online per-instance scoring.
- **Contrastive batches or memory banks:** disclose batch/memory size and negative sampling.
- **Sampling / ensembles:** include number of samples/models and parallelization assumptions.
- **ANN support:** name the index, approximation settings, recall, and preprocessing.

Do not convert an asymptotic expression into an author claim. A repository-derived observation belongs in `notes` with `provenance: derived`.
