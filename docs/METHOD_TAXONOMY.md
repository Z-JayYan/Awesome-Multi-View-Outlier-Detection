# Method Taxonomy: Where Does the Anomaly Evidence Come From?

This is a multi-label mechanism taxonomy. It deliberately avoids a single “deep vs. non-deep” split: depth describes an implementation family, while the tags below describe the evidence used to score an instance.

Task Track is orthogonal to this taxonomy. A deep or contrastive method may belong to CORE complete-view MVOD; a partial-view method is not a lesser method category; and industrial multi-view anomaly detection is a related protocol space rather than a chronological replacement for CORE.

## 1. Cluster and consensus disagreement

Early methods compare cluster memberships or cross-view cluster structures. They are historically important but may rely on visible cluster structure and, in some formulations, pairwise-view processing.

Controlled tags: `clustering`, sometimes `correspondence` or `graph`.

## 2. Subspace, low-rank, and self-representation

These methods explain normal instances using common or view-specific low-dimensional structure. Sparse residuals, inconsistent coefficients, or deviations from a shared representation become anomaly evidence.

Controlled tags: `subspace`, `low_rank`, `self_representation`, `shared_latent`.

## 3. Shared latent and generative modeling

A latent variable or representation is expected to explain all views of a normal instance. Low joint likelihood, multiple inferred latent explanations, or disagreement between shared/private factors indicates an anomaly.

Controlled tags: `shared_latent`, `shared_private`, `generative`, `information_theoretic`.

## 4. Reconstruction and cross-view mapping

Normal cross-view relations allow one view to reconstruct or predict another, or allow all views to reconstruct through a common code. Within-view error is often sensitive to attribute anomalies; cross-view error is often sensitive to incompatible pairings. That mapping is paper-specific, not universal.

Controlled tags: `reconstruction`, `cross_view_mapping`, optionally `shared_latent`.

## 5. Local structure and neighborhood consistency

Rather than require global clusters, these methods compare nearest-neighbor sets, local similarity graphs, or neighborhood relations across views. An instance is suspicious when its local role changes between views or fails to join a cross-view consensus neighborhood.

Controlled tags: `local_structure`, `graph`, `probabilistic_neighborhood`, `ensemble`.

## 6. Graph, tensor, and high-order relations

Graphs encode sample relations within each view; filtering, denoising, fusion, or sparse outlier components expose disagreement. Tensor methods retain high-order view/sample interactions rather than flattening them into pairwise comparisons.

Controlled tags: `graph`, `tensor`, `low_rank`, `local_structure`.

## 7. Contrastive and information-theoretic representation

Contrastive objectives treat aligned views of the same instance or compatible neighborhoods as positives, while information objectives control what is shared and what remains view-specific. Anomalies are detected through alignment failure, information imbalance, or downstream reconstruction/neighborhood scores.

Controlled tags: `contrastive`, `information_theoretic`, `shared_private`, `local_structure`.

## 8. Partial / incomplete multi-view modeling

Missing views are part of the problem, not merely a preprocessing nuisance. Methods transfer relations from observed views, impute missing views, learn partial-view consensus, or mask unavailable experts before scoring anomalies.

Controlled tags: `partial_view` plus the actual scoring mechanism.

## 9. Related natural multimodal and multi-view AD

RGB–depth, point-cloud, multi-camera, and multi-sensor systems may use spatial registration, geometric correspondence, cross-modal reconstruction, or feature fusion. They share mechanisms with classical MVOD but use natural defects, localization metrics, and object/image-level protocols; they remain a separate track.

## Categories considered but not promoted

`retrieval_rank` remains in the vocabulary for publicly verified future work, but current evidence does not justify making retrieval/rank a top-level historical branch. The taxonomy does not include any unpublished method as support for a category.

## Tagging rule

Assign the smallest set of tags that explains the scoring signal. Do not tag every architectural component. Bibliographic verification, scope confidence, code availability, and protocol completeness are separate fields: a verified paper may still have `unknown` protocol details.
