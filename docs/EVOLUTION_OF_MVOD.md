# Evolution of MVOD

The public literature supports a cautious evolution narrative, but not a clean replacement chain.

1. **Cross-view inconsistency through clusters and affinities.** Early work identifies instances whose view-wise memberships or relations disagree.
2. **Structured global representations.** Low-rank, subspace, and consensus models separate shared structure from sample-specific residuals and make attribute/class distinctions explicit.
3. **Local evidence and nonlinear representation.** Neighborhood consistency and deep reconstruction reduce dependence on globally separable clusters.
4. **Disentanglement, probabilistic fusion, and self-supervision.** Later models ask what should be shared, what should stay view-specific, and how aligned views can supervise one another.
5. **Graphs, high-order relations, efficiency, and missing views.** Recent work revisits relational evidence using filtering/tensors/ensembles while making scalability and incomplete observations first-class concerns.

The steps overlap: probabilistic latent models appear early, graph-based reasoning recurs, and recent studies still depend on older synthetic anomaly generators. The narrative should therefore guide reading, not imply a monotonic SOTA lineage.
