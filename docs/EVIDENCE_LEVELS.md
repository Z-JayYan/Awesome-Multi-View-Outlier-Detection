# Cross-Cutting Evidence Levels

Evidence level is useful as a second, cross-cutting taxonomy, but it is not a replacement for mechanism tags.

- **Instance-level:** direct aligned-instance likelihood, reconstruction, mapping, or correspondence evidence.
- **Local-level:** neighborhood sets, local graphs, manifolds, or sampled local regions.
- **Global-level:** cluster consensus, global subspace, low-rank decomposition, or dataset-level latent structure.

Many methods span levels—for example, a global representation can produce an instance score, or a global graph can be filtered to expose local disagreement. The registry therefore allows multiple values. Tags describe the mathematical source of evidence, not the granularity of the final AUROC label.
