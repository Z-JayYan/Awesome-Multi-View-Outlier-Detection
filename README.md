# Awesome Multi-View Outlier Detection

**English** | [简体中文](README.zh-CN.md)

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Registry validation](https://github.com/Z-JayYan/Awesome-Multi-View-Outlier-Detection/actions/workflows/validate.yml/badge.svg)](https://github.com/Z-JayYan/Awesome-Multi-View-Outlier-Detection/actions/workflows/validate.yml)
[![Papers](https://img.shields.io/badge/papers-42-4c1)](data/papers.yaml)
[![Version](https://img.shields.io/badge/version-0.3.0-blue)](CHANGELOG.md)

Papers, code, datasets, and experimental protocols for **Multi-View Outlier Detection (MVOD)**. The collection is maintained as structured data so that every table can be regenerated and checked.

## What is MVOD?

MVOD studies objects described by several views, such as different feature sets, languages, sensors, or camera angles. The aim is to find objects whose behavior is unusual within or across those views.

This repository is organized around three practical needs: learning the field, choosing baselines, and checking whether reported results can actually be compared.

## Repository Scope

The papers are separated by problem setting, not by whether the method is classical or deep.

| Track | Setting | Kept separate because |
|---|---|---|
| **CORE / Complete-view MVOD** | Every object has all aligned feature views. | This is the main feature-level MVOD setting. |
| **PARTIAL / Incomplete MVOD** | Some objects are missing one or more views. | Missing observations change both the task and the protocol. |
| **INDUSTRIAL / Natural MVAD** | Images or sensors capture real defects across views. | Data, supervision, and image/pixel evaluation differ from feature-level MVOD. |

Deep, graph, tensor, and contrastive methods may all belong to CORE. Ordinary multi-view clustering and single-view anomaly detection are outside the collection.

## Start Here

- **New to MVOD:** [Research Landscape](docs/RESEARCH_LANDSCAPE.md) · [中文](docs/RESEARCH_LANDSCAPE.zh-CN.md)
- **Choosing methods:** [Method Taxonomy](docs/METHOD_TAXONOMY.md) · [Baseline Map](docs/BASELINE_MAP.md)
- **Checking experiments:** [Dataset Variants](docs/DATASET_VARIANTS.md) · [Comparability Rules](docs/COMPARABILITY.md)
- **Browsing records:** [Paper Database](docs/PAPERS.md) · [Anomaly Taxonomy](docs/ANOMALY_TAXONOMY.md)

To compare reconstructed protocols, run `python scripts/compare_protocols.py PAPER_ID_A PAPER_ID_B`.

## Recent research

Recent work is grouped by track, then by year and venue. This is a reading list, not a ranking.

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

## How papers are tagged

Methods are tagged along several independent axes: problem setting, mechanism, training regime, anomaly type, and evidence level. See the [Method Taxonomy](docs/METHOD_TAXONOMY.md), [Anomaly Taxonomy](docs/ANOMALY_TAXONOMY.md), and [Paper Tree](docs/PAPER_TREE.md).

## Datasets

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

The same dataset name may refer to different samples, features, views, preprocessing, or injected anomalies. Use the [variant registry](docs/DATASET_VARIANTS.md) before comparing results.

## Choosing baselines

The [Baseline Map](docs/BASELINE_MAP.md) groups representative methods by the question they help test: shared representation, local structure, graph denoising, contrastive learning, efficiency, and other choices. It explains why a method is relevant without turning reported numbers into a leaderboard.

## Comparing results

Same dataset and metric are not enough. Views, features, anomaly construction, contamination, preprocessing, train/test setup, and repetition policy may still differ. The [comparison guide](docs/COMPARABILITY.md) records four outcomes, from directly comparable to insufficient information. The repository does not publish a cross-protocol leaderboard.

## Selected papers

This generated table highlights representative records. It is not a ranking.

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

## Code and reproducibility

Code is marked `official` only when a paper, author page, or project page establishes ownership. Configs, data instructions, weights, environments, and licenses are tracked separately in [Reproducibility](docs/REPRODUCIBILITY.md). `unknown` simply means that the checked sources were not enough to decide.

## Contributing

Corrections and verified additions are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md), edit the data files, regenerate the tables, and run the tests before opening a pull request.

## Citation

Use the machine-readable [`CITATION.cff`](CITATION.cff) when citing this release. The author identity is limited to the repository owner's verified GitHub identity; no real-world name has been inferred.

## License

Code, schemas, tests, and workflows are licensed under the [MIT License](LICENSE-CODE). Original documentation, taxonomy, and curated metadata are licensed under [Creative Commons Attribution 4.0 International](LICENSE-CONTENT). Bibliographic facts and linked third-party works are not claimed as original repository content. See the [changelog](CHANGELOG.md) for release history.
