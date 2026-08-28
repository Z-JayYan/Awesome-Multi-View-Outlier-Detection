# Awesome Multi-View Outlier Detection

**English** | [简体中文](README.zh-CN.md)

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Registry validation](https://github.com/Z-JayYan/Awesome-Multi-View-Outlier-Detection/actions/workflows/validate.yml/badge.svg)](https://github.com/Z-JayYan/Awesome-Multi-View-Outlier-Detection/actions/workflows/validate.yml)
[![Papers](https://img.shields.io/badge/papers-42-4c1)](data/papers.yaml)
[![Version](https://img.shields.io/badge/version-0.3.0-blue)](CHANGELOG.md)

> A curated, auditable, and machine-readable knowledge base for **Multi-View Outlier Detection (MVOD)** and carefully separated adjacent multi-view anomaly-detection settings.

**v0.3.0 — Scientific Usability & Research Landscape.** This release connects the auditable registry to method evolution, baseline selection, and dataset-variant-aware protocol comparison.

> **Same dataset name does not imply the same benchmark protocol.** Protocol reconstruction follows primary evidence and may remain incomplete when papers, supplements, or official code do not disclose a field.

`Paper → Dataset Variant → Protocol Fingerprint → Comparability`

## What is MVOD?

Multi-View Outlier Detection (MVOD) assigns anomaly evidence to aligned objects observed through multiple feature views. Depending on the paper, an anomaly may be an unusual attribute pattern, an unexpected class, a mixed class-attribute inconsistency, a generic deviation, or a natural defect. These definitions are related but not interchangeable.

This repository helps researchers understand how methods evolved, choose scientifically relevant baselines, and determine whether two experimental results share enough protocol to compare. The machine-readable registries are the source of truth; generated tables are navigation views.

## Repository Scope

**Multi-View Outlier Detection (MVOD)** is overloaded. Track is a task setting—not a synonym for model age, “classical algorithm,” or “non-deep method.” A CORE method may be deep, contrastive, graph-based, or tensor-based.

| Track | Definition | Typical endpoint | Direct benchmark boundary |
|---|---|---|---|
| **Track 1 — CORE: Complete-View Multi-View Outlier Detection** | Each object has all aligned feature views and an explicit sample correspondence across views. | Object/sample outlier score | Main complete-view MVOD comparison space |
| **Track 2 — PARTIAL / INCOMPLETE Multi-View Outlier Detection** | An aligned object may be missing one or more views; the method must handle incomplete observations as well as anomalies. | Object/sample score under a missing-view protocol | Separate from complete-view results; still methodologically relevant |
| **Track 3 — INDUSTRIAL / NATURAL Multi-View Anomaly Detection** | Multiple cameras, RGB/depth, point clouds, or other sensors observe a physical object or scene with natural defects. | Sample, image, object, or pixel endpoint | Not pooled with feature-level complete-view MVOD |

The industrial/natural track frequently uses normal-only training, frozen visual backbones, raw images, and image/pixel metrics. These choices differ fundamentally from complete-view feature-level MVOD. A paper title containing “multi-view anomaly detection” does not determine its track; the data model and evaluation protocol do.

Ordinary multi-view clustering/classification, single-view anomaly detection, and systems that merely ensemble unrelated backbones are out of scope. Borderline records remain explicitly marked rather than being silently forced into CORE.

## Start Here

- [Research Landscape](docs/RESEARCH_LANDSCAPE.md) · [中文](docs/RESEARCH_LANDSCAPE.zh-CN.md)
- [Method Taxonomy](docs/METHOD_TAXONOMY.md)
- [Anomaly Taxonomy](docs/ANOMALY_TAXONOMY.md)
- [Dataset and Benchmark Variants](docs/DATASET_VARIANTS.md) · [中文](docs/DATASET_VARIANTS.zh-CN.md)
- [Baseline Map](docs/BASELINE_MAP.md)
- [Comparability Rules](docs/COMPARABILITY.md) · [中文](docs/COMPARABILITY.zh-CN.md)
- [Paper Database](docs/PAPERS.md)

To compare reconstructed protocols, run `python scripts/compare_protocols.py PAPER_ID_A PAPER_ID_B`.

## Recent research

Recent work is ordered **Track → Year → Venue**. Placement in the same year is not a claim of benchmark compatibility.

<!-- AUTO-GENERATED: RECENT START -->
### Recent Complete-View MVOD

#### 2026

**AAAI**
- **SCoNE: Spherical Consistent Neighborhoods Ensemble for Effective and Efficient Multi-View Anomaly Detection** [[paper]](https://doi.org/10.1609/AAAI.V40I19.38643)

**Applied Intelligence**
- **Multi-view outlier detection via tensor decomposition and information decoupling** [[paper]](https://doi.org/10.1007/s10489-026-07375-y) [[code]](https://github.com/YF-W/MOD-TDID)

**ICASSP**
- **Bilateral Graph Filtering Framework with Alternating Optimization for Robust Multi-View Outlier Detection** [[paper]](https://doi.org/10.1109/ICASSP55912.2026.11460482)
- **Granular-Ball Based Multi-View Outlier Detection** [[paper]](https://doi.org/10.1109/ICASSP55912.2026.11462415)

**ICML**
- **Reliable Neighborhood-Aware Multi-View Outlier Detection** [[paper]](https://openreview.net/forum?id=mL4B6DdgPU)

#### 2025

**ICASSP**
- **Unsupervised Multi-View Outlier Detection via Optimal Graph Filtering** [[paper]](https://doi.org/10.1109/ICASSP49660.2025.10889803)

**Information Fusion**
- **Low-rank Tucker decomposition for multi-view outlier detection based on meta-learning** [[paper]](https://doi.org/10.1016/j.inffus.2025.103313)

**International Journal of Approximate Reasoning**
- **Multi-view outlier detection based on multi-granularity fusion of fuzzy rough granules** [[paper]](https://doi.org/10.1016/j.ijar.2025.109402) [[code]](https://github.com/YF-W/MGFMOD)

#### 2024

**ACM TKDD**
- **Information-aware Multi-view Outlier Detection** [[paper]](https://doi.org/10.1145/3638354) [[code]](https://github.com/GTML-LAB/IAMOD)

**Information Fusion**
- **Multi-view Outlier Detection via Graphs Denoising** [[paper]](https://doi.org/10.1016/j.inffus.2023.102012) [[code]](http://Doctor-Nobody.github.io/codes/MODGD.zip)

**Multimedia Systems**
- **Multi-view anomaly detection via hybrid instance-neighborhood aligning and cross-view reasoning** [[paper]](https://doi.org/10.1007/s00530-024-01526-2) [[code]](https://github.com/tl-git320/INA-CR)

**PAKDD**
- **SeeM: A Shared Latent Variable Model for Unsupervised Multi-view Anomaly Detection** [[paper]](https://doi.org/10.1007/978-981-97-2242-6_7) [[code]](https://github.com/thanhphuong163/SeeM)

### Recent Partial / Incomplete Multi-View Outlier Detection

#### 2024

**ACM MM**
- **Regularized Contrastive Partial Multi-view Outlier Detection** [[paper]](https://doi.org/10.1145/3664647.3681125)

### Recent Industrial / Natural Multi-View Anomaly Detection

#### 2026

**ECCV**
- **IMMoE: Incomplete Multi-View Anomaly Detection via Mixture of View Experts Fusion** (accepted; publisher record/DOI may still be pending) [[paper]](https://arxiv.org/abs/2607.19032) [[code]](https://github.com/HULEI7/IMMoE)

**IEEE Transactions on Multimedia**
- **Learning Multi-View Anomaly Detection With Efficient Adaptive Selection** [[paper]](https://doi.org/10.1109/TMM.2026.3660076)

**Pattern Recognition**
- **Visual Anomaly Detection under Complex View-Illumination Interplay: A Large-Scale Benchmark** (accepted; publisher record/DOI may still be pending) [[paper]](https://arxiv.org/abs/2505.10996) [[code]](https://github.com/hustCYQ/M2AD)

**arXiv**
- **MATCH: Flow Matching for Multi-View Anomaly Detection** (preprint) [[paper]](https://arxiv.org/abs/2606.24375)
- **SGANet: Semantic and Geometric Alignment for Multimodal Multi-view Anomaly Detection** (preprint) [[paper]](https://arxiv.org/abs/2604.05632)

#### 2025

**AAAI**
- **Unveiling Multi-View Anomaly Detection: Intra-view Decoupling and Inter-view Fusion** [[paper]](https://doi.org/10.1609/AAAI.V39I12.33349) [[code]](https://github.com/Kerio99/IDIF)

**CVPR Workshops**
- **Multi-Flow: Multi-View-Enriched Normalizing Flows for Industrial Anomaly Detection** [[paper]](https://doi.org/10.1109/CVPRW67362.2025.00378) [[code]](https://github.com/m-kruse98/Multi-Flow)

#### 2024

**ECCV**
- **Learning Diffusion Models for Multi-view Anomaly Detection** [[paper]](https://doi.org/10.1007/978-3-031-73414-4_19) [[code]](https://github.com/jayliu0313/Diffusion_Multi-View_AD)
<!-- AUTO-GENERATED: RECENT END -->

## Taxonomy overview

The registry uses orthogonal fields rather than one mutually exclusive category:

- `track` and `view_setting` describe the task boundary;
- `mechanisms` describe representation and evidence families such as graph, tensor, neighborhood, reconstruction, contrastive, or information-theoretic modeling;
- `training_paradigm` records the learning regime when verified;
- `anomaly_types` and `evidence_levels` describe what is scored and where evidence is gathered;
- `protocol` records the known benchmark fingerprint without filling unreported fields by inference.

See [Method Taxonomy](docs/METHOD_TAXONOMY.md), [Anomaly Taxonomy](docs/ANOMALY_TAXONOMY.md), [Evidence Levels](docs/EVIDENCE_LEVELS.md), and the [Paper Tree](docs/PAPER_TREE.md).

## Benchmark and dataset overview

<!-- AUTO-GENERATED: DATASETS START -->
| Dataset | Track | Samples | Views | Feature / modality | Variants |
|---|---|---:|---:|---|---|
| [100Leaves](https://archive.ics.uci.edu/dataset/241/one-hundred-plant-species-leaves-data-set) | CORE | 1600 | 3 | 64/64/64 in the UCI feature files | unknown |
| [3Sources](http://erdos.ucd.ie/datasets/3sources.html) | CORE | 416 | 3 | variant-dependent | unknown |
| [BBCSport](http://mlg.ucd.ie/datasets/segment.html) | CORE | 544 | 2 | variant-dependent | unknown |
| [Caltech101](https://data.caltech.edu/records/mzrjq-6wc02) | CORE | unknown | unknown | variant-dependent | unknown |
| [CiteSeer](https://linqs-data.soe.ucsc.edu/public/lbc/citeseer.tgz) | CORE | unknown | unknown | variant-dependent | unknown |
| [COIL-20](https://www.cs.columbia.edu/CAVE/software/softlib/coil-20.php) | CORE | 1440 | unknown | variant-dependent | unknown |
| [Fashion-MNIST](https://github.com/zalandoresearch/fashion-mnist) | CORE | 70000 | unknown | variant-dependent | unknown |
| [M2AD](https://hustcyq.github.io/M2AD/) | industrial / natural | 119880 | 12 | RGB images; 1024x1024 and 256x256 public variants | M2AD-1024, M2AD-256, M2AD-Synergy, M2AD-Invariant |
| [MNIST](http://yann.lecun.com/exdb/mnist/) | CORE | 70000 | unknown | variant-dependent | unknown |
| [MVTec 3D-AD](https://www.mvtec.com/company/research/datasets/mvtec-3d-ad) | industrial / natural | 4147 | 2 | RGB image and organized 3D point cloud | unknown |
| [NUSWIDEOBJ](https://lms.comp.nus.edu.sg/wp-content/uploads/2019/research/nuswide/NUS-WIDE.html) | CORE | unknown | unknown | variant-dependent | unknown |
| [Real-IAD](https://realiad4ad.github.io/Real-IAD/) | industrial / natural | 150000 | 5 | image pixels | unknown |
| [Reuters](https://archive.ics.uci.edu/dataset/137/reuters+21578+text+categorization+collection) | CORE | unknown | unknown | variant-dependent | unknown |
<!-- AUTO-GENERATED: DATASETS END -->

Dataset names are labels, not protocol identifiers. BBCSport, Reuters, Caltech101, and other reused sources may have different feature partitions, subsets, preprocessing, or anomaly generation in different papers.

## Baseline selection guide

The [Baseline Evidence Map](docs/BASELINE_MAP.md) provides method-level cards for Reliable Neighborhood-Aware Multi-View Outlier Detection (RNAMOD), Regularized Contrastive Partial Multi-view Outlier Detection (RCPMOD), Information-aware Multi-view Outlier Detection (IAMOD), Multi-view Outlier Detection via Graphs Denoising (MODGD), Low-rank Tucker Decomposition for Multi-view Outlier Detection based on Meta-learning (LRTDM), Self-Representation Learning with Local Similarity Preserving for Multi-View Outlier Detection (SRLSP), and other historical/frontier anchors.

Each card answers **why compare**, identifies the closest counterfactual, records artifact status, and states why the reported numbers may still not be directly comparable. Track mismatch does not erase methodological relevance: for example, RCPMOD is a strong contrastive baseline even when a new method uses complete views.

## Protocol comparability warning

> **Same dataset name ≠ directly comparable results.**

The conservative statuses are `DIRECTLY_COMPARABLE`, `PARTIALLY_COMPARABLE`, `NOT_DIRECTLY_COMPARABLE`, and `INSUFFICIENT_INFORMATION`. Direct comparison requires matching dataset variant, anomaly generation, view completeness, preprocessing, contamination, metric, endpoint, feature/backbone level, train/test setting, and relevant repetition/seed details.

This repository intentionally has no traditional cross-protocol leaderboard. Where evidence is incomplete, the correct label is **Reported Result Context — not directly comparable**. See [comparability rules](data/comparability.yaml) and the full [decision guide](docs/COMPARABILITY.md).

## Representative registry snapshot

This generated table is navigation, not a ranking. The Track column is part of every comparison decision.

Anomaly abbreviations: **A = Attribute**, **C = Class**, **M = Mixed / Class-Attribute**, **G = Generic**, **N = Natural**.

<!-- AUTO-GENERATED: PAPERS START -->
| Year | Method | Track | Venue | Mechanism | Anomaly | Code |
|---:|---|---|---|---|---|---|
| 2026 | [MVAS](https://doi.org/10.1109/TMM.2026.3660076) | INDUSTRIAL / NATURAL | IEEE Transactions on Multimedia | local structure, shared latent | N | — |
| 2026 | [MOD-TDID](https://doi.org/10.1007/s10489-026-07375-y) | CORE | Applied Intelligence | tensor, graph | A/C/M | [official](https://github.com/YF-W/MOD-TDID) |
| 2026 | [RNAMOD](https://openreview.net/forum?id=mL4B6DdgPU) | CORE | ICML | local structure, graph | G | — |
| 2026 | [SCoNE](https://doi.org/10.1609/AAAI.V40I19.38643) | CORE | AAAI | local structure, ensemble | G/C | — |
| 2025 | [LRTDM](https://doi.org/10.1016/j.inffus.2025.103313) | CORE | Information Fusion | tensor, low rank | A/C/M | — |
| 2025 | [MGFMOD](https://doi.org/10.1016/j.ijar.2025.109402) | CORE | International Journal of Approximate Reasoning | local structure, probabilistic neighborhood | A/C | [official](https://github.com/YF-W/MGFMOD) |
| 2025 | [MODGF](https://doi.org/10.1109/ICASSP49660.2025.10889803) | CORE | ICASSP | graph, local structure | G/C | — |
| 2025 | [IDIF](https://doi.org/10.1609/AAAI.V39I12.33349) | INDUSTRIAL / NATURAL | AAAI | shared private, information theoretic | N | [official](https://github.com/Kerio99/IDIF) |
| 2024 | [IAMOD](https://doi.org/10.1145/3638354) | CORE | ACM TKDD | information theoretic, shared latent | A/C/M | [official](https://github.com/GTML-LAB/IAMOD) |
| 2024 | [Learning Diffusion Models for Multi-view Anomaly Detection](https://doi.org/10.1007/978-3-031-73414-4_19) | INDUSTRIAL / NATURAL | ECCV | diffusion, shared latent | N | [official](https://github.com/jayliu0313/Diffusion_Multi-View_AD) |
| 2024 | [MODGD](https://doi.org/10.1016/j.inffus.2023.102012) | CORE | Information Fusion | graph, local structure | A/C/M | [official](http://Doctor-Nobody.github.io/codes/MODGD.zip) |
| 2024 | [RCPMOD](https://doi.org/10.1145/3664647.3681125) | PARTIAL | ACM MM | partial view, contrastive | A/C/M | — |
| 2024 | [SeeM](https://doi.org/10.1007/978-981-97-2242-6_7) | CORE | PAKDD | generative, shared latent | G/C | [official](https://github.com/thanhphuong163/SeeM) |
| 2023 | [SRLSP](https://doi.org/10.1145/3532191) | CORE | ACM TKDD | self representation, local structure | A/C/M | [official](https://github.com/wy54224/SRLSP) |
| 2023 | [dPoE](https://doi.org/10.1145/3581783.3612487) | CORE | ACM MM | generative, shared private | A/C/M | [official](https://github.com/cshaowang/dPoE) |
| 2022 | [FMOD](https://doi.org/10.1109/TBDATA.2020.3004057) | CORE | IEEE Transactions on Big Data | subspace, low rank | A/C/M | — |
| 2021 | [CGAEs](https://doi.org/10.1109/ICTAI52525.2021.00218) | CORE | ICTAI | reconstruction, cross view mapping | A/C | — |
| 2021 | [NCMOD](https://doi.org/10.1609/AAAI.V35I8.16873) | CORE | AAAI | reconstruction, local structure | A/C/M | [official](https://github.com/auguscl/NCMOD) |
| 2019 | [MUVAD](https://doi.org/10.1609/AAAI.V33I01.33014894) | CORE | AAAI | local structure | A/C | — |
| 2019 | [MODDIS](https://doi.org/10.1109/ICDM.2019.00136) | CORE | ICDM | shared latent, reconstruction | A/C/M | [official](https://github.com/sigerma/ICDM-2019-MODDIS) |
| 2018 | [LDSR](https://doi.org/10.1609/AAAI.V32I1.11826) | CORE | AAAI | subspace, low rank | A/C/M | [official](https://github.com/kailigo/mvod) |
| 2018 | [Partial Multi-View Outlier Detection Based on Collective Learning](https://doi.org/10.1609/AAAI.V32I1.11278) | PARTIAL | AAAI | partial view, self representation | C | — |
| 2016 | [PLVM](https://proceedings.neurips.cc/paper/2016/hash/0f96613235062963ccde717b18f97592-Abstract.html) | CORE | NeurIPS | generative, shared latent | G/C | — |
| 2015 | [DMOD](https://www.ijcai.org/Abstract/15/572) | CORE | IJCAI | shared latent, self representation | A/C | — |
| 2015 | [MLRA](https://doi.org/10.1137/1.9781611974010.84) | CORE | SDM | low rank, subspace | A/C | [official](https://sheng-li.org/Codes/SDM15_MLRA_Code.zip) |
| 2011 | [HOAD](https://ieeexplore.ieee.org/document/6137313) | CORE | ICDM | clustering, graph | C | — |
<!-- AUTO-GENERATED: PAPERS END -->

## Reproducibility overview

Artifact claims are evidence-backed. `official` code requires a paper, author page, or official project source establishing ownership; a GitHub search hit alone is insufficient. `unknown` means the audit did not find enough official evidence, not that an artifact cannot exist.

The registry separately records official code, configs, dataset instructions, pretrained weights, environment details, and repository license. See [Reproducibility](docs/REPRODUCIBILITY.md) and the historical [v0.2 coverage audit](docs/COVERAGE_AUDIT_V02.md).

## Contributing

Corrections and carefully verified additions are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md), edit the registry, regenerate derived files, and run the validator and tests before opening a pull request.

## Citation

Use the machine-readable [`CITATION.cff`](CITATION.cff) when citing this release. The author identity is limited to the repository owner's verified GitHub identity; no real-world name has been inferred.

## License

Code, schemas, tests, and workflows are licensed under the [MIT License](LICENSE-CODE). Original documentation, taxonomy, and curated metadata are licensed under [Creative Commons Attribution 4.0 International](LICENSE-CONTENT). Bibliographic facts and linked third-party works are not claimed as original repository content. See the [changelog](CHANGELOG.md) for release history.
