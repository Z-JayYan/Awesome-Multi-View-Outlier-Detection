# Related Areas

**Related does not mean benchmark-compatible.** These areas share mechanisms with complete-view MVOD while changing the observation model, labels, or metrics.

- **Multimodal industrial anomaly detection:** combines RGB, depth, point clouds, or sensors to detect and localize physical defects.
- **3D anomaly detection:** models point clouds or meshes; view alignment and geometry replace tabular aligned-feature assumptions.
- **RGB-D anomaly detection:** uses registered appearance and depth, often with image/pixel AUROC or overlap metrics.
- **Multi-view visual anomaly detection:** aggregates multiple camera views of the same object; object-level labels and view coverage matter.
- **Partial multi-view learning:** provides missing-view representation and imputation techniques, but ordinary clustering/classification papers are not automatically MVOD papers.
- **Multimodal OOD detection:** detects distribution or semantic novelty, often with supervised labels and train/test shifts unlike unsupervised MVOD corruption protocols.
- **Multi-view graph anomaly detection:** may use multiple relation graphs over nodes; include in core only when aligned node instances and cross-view anomaly scoring are central.
- **Multi-view time-series anomaly detection:** adds temporal dependence and detection-delay/event metrics.

Use [Awesome Industrial Anomaly Detection](https://github.com/Z-JayYan/awesome-industrial-anomaly-detection) for broader industrial image coverage.
