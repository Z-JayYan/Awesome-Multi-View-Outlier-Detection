# v0.2 Coverage and Verification Audit

Audit date: 2026-08-27. Scope: requested historical anchors plus 2024–2026 frontier methods. Publisher, proceedings, author/project, official GitHub, and arXiv sources were preferred. A method name containing “anomaly detection” was not sufficient for inclusion or Track assignment.

## Audit result

| Method / resource | v0.1 state | v0.2 decision | Track | Artifact conclusion |
|---|---|---|---|---|
| Reliable Neighborhood-Aware Multi-View Outlier Detection (RNAMOD) | Missing | Added; ICML 2026 metadata and abstract verified | CORE | Official code unknown |
| Information-aware Multi-view Outlier Detection (IAMOD) | Present | Metadata and Track retained | CORE | Official code verified |
| Multi-view Outlier Detection via Graphs Denoising (MODGD) | Present | Metadata and Track retained | CORE | Author-hosted official code verified |
| Low-rank Tucker Decomposition for Multi-view Outlier Detection based on Meta-learning (LRTDM) | Present | Metadata and Track retained | CORE | Official code unknown |
| Unsupervised Multi-View Outlier Detection via Optimal Graph Filtering (OGF) | Present | Metadata and Track retained | CORE | Official code unknown |
| Multi-granularity Fusion of Fuzzy Rough Granules (MGFMOD) | Present | Metadata and Track retained | CORE | Official code verified |
| Tensor Decomposition and Information Decoupling (MOD-TDID) | Present | Metadata and Track retained | CORE | Official code verified |
| Spherical Consistent Neighborhoods Ensemble (SCoNE) | Present | AAAI 2026 placement retained | CORE | Official code unknown |
| Regularized Contrastive Partial Multi-view Outlier Detection (RCPMOD) | Present | Partial Track retained; baseline relevance made explicit | PARTIAL | Official code unknown |
| Partial Multi-View Outlier Detection Based on Collective Learning | Present | Historical partial-view anchor retained | PARTIAL | No verified official code |
| Cross-aligned and Gumbel-refactored Autoencoders (CGAEs) | Present | Historical anchor retained | CORE | No verified official code |
| Neighborhood Consensus Networks (NCMOD) | Present | Historical anchor retained | CORE | Official code verified |
| Disentangled Product-of-Experts Modeling (dPoE) | Present | Online/deep anchor retained | CORE | Official code verified |
| Self-Representation with Local Similarity Preserving (SRLSP) | Present | Historical/scalability anchor retained | CORE | Official code verified |
| Fast Multi-View Outlier Detection via Deep Encoder (FMOD) | Present | Speed-oriented anchor retained | CORE | No verified official code |
| LDSR / DMOD / MODDIS | Present | Historical baseline cards added | CORE | LDSR and MODDIS official code verified; DMOD not found |
| Efficient Adaptive Selection (MVAS) | Present | Industrial/natural boundary retained | INDUSTRIAL / NATURAL | Official code unknown |
| Intra-view Decoupling and Inter-view Fusion (IDIF) | Present | Industrial baseline card added | INDUSTRIAL / NATURAL | Official code verified |
| Multi-Flow | Partially verified | Authors, Real-IAD, proceedings, environment, and official code verified | INDUSTRIAL / NATURAL | Official code verified |
| Flow Matching for Multi-View Anomaly Detection (MATCH) | Present | Preprint status retained | INDUSTRIAL / NATURAL | Official code unknown |
| SGANet | Present | Preprint status retained | INDUSTRIAL / NATURAL | Official code unknown |
| IMMoE | Present | Industrial incomplete-view method retained; not reclassified as classical partial MVOD | INDUSTRIAL / NATURAL | Official code verified |
| Multi-View Multi-Illumination Anomaly Detection (M2AD) | Missing | Benchmark paper and dataset added | INDUSTRIAL / NATURAL | Official benchmark code verified |

## Critical primary evidence added in v0.2

- RNAMOD: [ICML 2026 official poster page](https://icml.cc/virtual/2026/poster/61856), [ICML downloads index](https://icml.cc/Downloads/2026), and [OpenReview record](https://openreview.net/forum?id=mL4B6DdgPU).
- Multi-Flow: [CVPR Open Access](https://openaccess.thecvf.com/content/CVPR2025W/VAND/html/Kruse_Multi-Flow_Multi-View-Enriched_Normalizing_Flows_for_Industrial_Anomaly_Detection_CVPRW_2025_paper.html), [authors' institute page](https://www.tnt.uni-hannover.de/de/project/anomaly/?publ=2), and [official implementation](https://github.com/m-kruse98/Multi-Flow).
- M2AD: [official project page](https://hustcyq.github.io/M2AD/), [arXiv manuscript](https://arxiv.org/abs/2505.10996), and [official benchmark repository](https://github.com/hustCYQ/M2AD).
- Bilateral graph filtering: [official ICASSP 2026 schedule](https://www.cmsworkshops.com/ICASSP2026/view_paper.php?PaperNum=15636).
- Multi-View Group Anomaly Detection: [DBLP proceedings record](https://dblp.org/rec/conf/cikm/WangSZWL18) plus the publisher DOI already in the registry.

## Verification debt: before and after

| State | v0.1 | v0.2 |
|---|---:|---:|
| Verified records | 37 | 42 |
| Partially verified records | 3 | 0 |
| Uncertain verification status | 0 | 0 |

Record-level bibliographic debt is cleared for this release. This does **not** mean every protocol field is known: most historical papers still have explicit `unknown` values for anomaly-generation ratios, seeds, dataset variants, preprocessing, or metrics. Scope uncertainty also remains separate from verification status for the group-anomaly paper.

## Coverage boundary decisions

- RNAMOD is CORE because the official description studies aligned multi-view samples and reliable cross-view neighborhoods, not missing views or natural-image defects.
- RCPMOD remains PARTIAL even though it is a strong conceptual contrastive baseline for complete-view work.
- IMMoE handles missing industrial camera views but remains INDUSTRIAL / NATURAL because its inputs, training, endpoints, and benchmark are not classical feature-level partial MVOD.
- M2AD is a benchmark paper/resource; it is included in the industrial Track and is not presented as a CORE detection algorithm.
- Multi-View Group Anomaly Detection remains `track: uncertain` because its group-level endpoint differs from aligned-instance outlier scoring, despite verified bibliography.
