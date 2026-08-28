# Awesome Multi-View Outlier Detection (MVOD)

**English** | [简体中文](README.zh-CN.md)

**Papers · Code · Datasets · Taxonomy · Baselines · Reproducibility**

A curated research hub for Multi-View Outlier Detection. Machine-readable metadata and evidence-backed protocol checks support reproducible research without turning incomplete information into assumptions.

<!-- AUTO-GENERATED: STATS START -->
[![Papers](https://img.shields.io/badge/papers-42-4c1)](docs/PAPERS.md) [![Verified records](https://img.shields.io/badge/verified-42-2f855a)](docs/QUALITY_AUDIT.md) [![Official code](https://img.shields.io/badge/official_code-20-2563eb)](docs/REPRODUCIBILITY.md) [![Datasets](https://img.shields.io/badge/datasets-13-7c3aed)](docs/DATASETS.md) [![License: CC BY 4.0](https://img.shields.io/badge/license-CC_BY_4.0-lightgrey)](LICENSE-CONTENT)
<!-- AUTO-GENERATED: STATS END -->

## 🔥 Latest Updates

<!-- AUTO-GENERATED: UPDATES START -->
- **2026 coverage:** 10 records across CORE and related multi-view anomaly settings.
- **Research map:** method taxonomy and representative research routes reorganized for field navigation.
- **Datasets:** 13 source datasets linked to paper-specific benchmark variants.
- **v0.3:** research-portal layout, bilingual entry points, and protocol-aware baseline guidance.

[See the full changelog →](CHANGELOG.md)
<!-- AUTO-GENERATED: UPDATES END -->

## What is MVOD?

MVOD studies objects described by several aligned views, such as different feature sets, languages, sensors, or camera angles. It looks for objects that are unusual within a view, across views, or in both ways.

- **Attribute anomaly:** an object is unusual within one or more individual views.
- **Class anomaly:** individual views may look locally normal, but their semantic or instance correspondence is inconsistent across views.
- **Mixed anomaly:** attribute-level and cross-view/class-level abnormality occur together.

These are anomaly definitions, not fixed synthetic corruption recipes. Different methods use different evidence to detect them.

## Scope

### Core Research Scope

**CORE — Complete-View Multi-View Outlier Detection** assumes that every object has all aligned feature views. This is the repository's main benchmark space. CORE includes classical and deep methods, as well as graph, tensor, generative, and contrastive models.

### Extended MVOD Settings

**Partial / Incomplete MVOD** studies objects with missing views. It is methodologically close to CORE, but missing observations create a distinct protocol and comparison boundary.

### Related Multi-View Anomaly Detection

**Industrial / Natural MVAD** covers multi-camera images, RGB-D, point clouds, and natural defects. These studies share cross-view ideas with CORE but use different data, supervision, and evaluation.

## Quick Navigation

- 📚 [Full Paper Registry](docs/PAPERS.md)
- 🧠 [Method Taxonomy](docs/METHOD_TAXONOMY.md)
- 🌳 [MVOD Research Map](docs/PAPER_TREE.md)
- 🧪 [Datasets and Benchmark Variants](docs/DATASETS.md)
- ⚔️ [Baseline Selection Guide](docs/BASELINE_MAP.md)
- 🔬 [Protocol Comparability](docs/COMPARABILITY.md)
- ♻️ [Reproducibility](docs/REPRODUCIBILITY.md)
- 🤝 [Contributing](CONTRIBUTING.md)

## Recent Papers

Only selected recent papers are shown here. The list is generated from verified, featured records in [`data/papers.yaml`](data/papers.yaml).

<!-- AUTO-GENERATED: RECENT START -->
### 2026

- **MVAS** — Learning Multi-View Anomaly Detection With Efficient Adaptive Selection — *IEEE Transactions on Multimedia 2026* · `RELATED` · [Paper](https://doi.org/10.1109/TMM.2026.3660076)
- **MOD-TDID** — Multi-view outlier detection via tensor decomposition and information decoupling — *Applied Intelligence 2026* · `CORE` · [Paper](https://doi.org/10.1007/s10489-026-07375-y) · [Code](https://github.com/YF-W/MOD-TDID)
- **RNAMOD** — Reliable Neighborhood-Aware Multi-View Outlier Detection — *ICML 2026* · `CORE` · [Paper](https://openreview.net/forum?id=mL4B6DdgPU)
- **SCoNE** — SCoNE: Spherical Consistent Neighborhoods Ensemble for Effective and Efficient Multi-View Anomaly Detection — *AAAI 2026* · `CORE` · [Paper](https://doi.org/10.1609/AAAI.V40I19.38643)

### 2025

- **LRTDM** — Low-rank Tucker decomposition for multi-view outlier detection based on meta-learning — *Information Fusion 2025* · `CORE` · [Paper](https://doi.org/10.1016/j.inffus.2025.103313)
- **MGFMOD** — Multi-view outlier detection based on multi-granularity fusion of fuzzy rough granules — *International Journal of Approximate Reasoning 2025* · `CORE` · [Paper](https://doi.org/10.1016/j.ijar.2025.109402) · [Code](https://github.com/YF-W/MGFMOD)
- **MODGF** — Unsupervised Multi-View Outlier Detection via Optimal Graph Filtering — *ICASSP 2025* · `CORE` · [Paper](https://doi.org/10.1109/ICASSP49660.2025.10889803)
- **IDIF** — Unveiling Multi-View Anomaly Detection: Intra-view Decoupling and Inter-view Fusion — *AAAI 2025* · `RELATED` · [Paper](https://doi.org/10.1609/AAAI.V39I12.33349) · [Code](https://github.com/Kerio99/IDIF)

### 2024

- **IAMOD** — Information-aware Multi-view Outlier Detection — *ACM TKDD 2024* · `CORE` · [Paper](https://doi.org/10.1145/3638354) · [Code](https://github.com/GTML-LAB/IAMOD)
- Learning Diffusion Models for Multi-view Anomaly Detection — *ECCV 2024* · `RELATED` · [Paper](https://doi.org/10.1007/978-3-031-73414-4_19) · [Code](https://github.com/jayliu0313/Diffusion_Multi-View_AD)
- **MODGD** — Multi-view Outlier Detection via Graphs Denoising — *Information Fusion 2024* · `CORE` · [Paper](https://doi.org/10.1016/j.inffus.2023.102012) · [Code](http://Doctor-Nobody.github.io/codes/MODGD.zip)
- **RCPMOD** — Regularized Contrastive Partial Multi-view Outlier Detection — *ACM MM 2024* · `PARTIAL` · [Paper](https://doi.org/10.1145/3664647.3681125)
- **SeeM** — SeeM: A Shared Latent Variable Model for Unsupervised Multi-view Anomaly Detection — *PAKDD 2024* · `CORE` · [Paper](https://doi.org/10.1007/978-981-97-2242-6_7) · [Code](https://github.com/thanhphuong163/SeeM)

[Browse the complete paper registry →](docs/PAPERS.md)
<!-- AUTO-GENERATED: RECENT END -->

## Dataset Overview

> **Dataset name ≠ protocol identity.** Papers may use different samples, views, features, preprocessing, and anomaly construction under the same dataset name.

The homepage shows stable source-level information. Exact dimensions, ratios, and paper-specific variants remain in the [dataset cards](docs/DATASETS.md) and [variant registry](docs/DATASET_VARIANTS.md).

<!-- AUTO-GENERATED: DATASETS START -->
| Dataset | Domain | Scope | Notes |
|---|---|---|---|
| [100Leaves](https://archive.ics.uci.edu/dataset/241/one-hundred-plant-species-leaves-data-set) | plant leaf shape, margin, and texture | CORE | Many MVOD studies subsample or corrupt the complete UCI feature set. |
| [3Sources](http://erdos.ucd.ie/datasets/3sources.html) | multilingual/news text | CORE | Article alignment and feature construction vary across redistributed benchmark files. |
| [BBCSport](http://mlg.ucd.ie/datasets/segment.html) | news text | CORE | Multi-view versions use different vocabulary partitions or feature preprocessing. |
| [Caltech101](https://data.caltech.edu/records/mzrjq-6wc02) | object images represented by multiple handcrafted or learned features | CORE | MVOD papers usually use a derived multi-feature subset; class count, sample count, and views are paper-specific. |
| [CiteSeer](https://linqs-data.soe.ucsc.edu/public/lbc/citeseer.tgz) | scientific documents/citation network | CORE | Text, citation, and label variants differ; record the exact preprocessing when reporting a result. |
| [COIL-20](https://www.cs.columbia.edu/CAVE/software/softlib/coil-20.php) | multi-angle object images | CORE | The base dataset has 72 poses per object; feature-view construction is paper-specific. |
| [Fashion-MNIST](https://github.com/zalandoresearch/fashion-mnist) | clothing images represented by constructed feature views | CORE | Not inherently multi-view; views and anomaly corruption are constructed by each study. |
| [M2AD](https://hustcyq.github.io/M2AD/) | industrial multi-view and multi-illumination images | RELATED | 999 specimens are captured with 12 synchronized views and 10 illumination settings; M2AD-Synergy and M2AD-Invariant are distinct protocols. |
| [MNIST](http://yann.lecun.com/exdb/mnist/) | handwritten digits represented by constructed feature views | CORE | Not inherently multi-view; view construction and sampling vary across papers. |
| [MVTec 3D-AD](https://www.mvtec.com/company/research/datasets/mvtec-3d-ad) | multimodal industrial inspection | RELATED | Related RGB+3D track; modalities are spatially registered but use natural-defect protocols. |
| [NUSWIDEOBJ](https://lms.comp.nus.edu.sg/wp-content/uploads/2019/research/nuswide/NUS-WIDE.html) | web images with visual features and tags | CORE | MVOD subsets differ in concepts, retained samples, visual descriptors, and tag features. |
| [Real-IAD](https://realiad4ad.github.io/Real-IAD/) | industrial multi-view images | RELATED | Related natural multi-view track; protocol and metrics are not comparable to tabular complete-view MVOD. |
| [Reuters](https://archive.ics.uci.edu/dataset/137/reuters+21578+text+categorization+collection) | multilingual/news text | CORE | “Reuters” denotes several incompatible multi-view constructions; never assume one canonical shape. |
<!-- AUTO-GENERATED: DATASETS END -->

## How to Choose Baselines

Choose baselines by the scientific question they represent, then check protocol compatibility before comparing numbers.

<!-- AUTO-GENERATED: BASELINES START -->
| Research question / mechanism | Representative anchors |
|---|---|
| Historical foundations | [DMOD](https://www.ijcai.org/Abstract/15/572), [LDSR](https://doi.org/10.1609/AAAI.V32I1.11826) |
| Local / neighborhood | [SRLSP](https://doi.org/10.1145/3532191), [RNAMOD](https://openreview.net/forum?id=mL4B6DdgPU), [SCoNE](https://doi.org/10.1609/AAAI.V40I19.38643) |
| Shared latent / generative | [dPoE](https://doi.org/10.1145/3581783.3612487) |
| Information-theoretic | [IAMOD](https://doi.org/10.1145/3638354) |
| Graph-based | [MODGD](https://doi.org/10.1016/j.inffus.2023.102012), [RNAMOD](https://openreview.net/forum?id=mL4B6DdgPU) |
| Tensor / low-rank | [LRTDM](https://doi.org/10.1016/j.inffus.2025.103313), [MOD-TDID](https://doi.org/10.1007/s10489-026-07375-y) |
| Partial-view contrastive | [RCPMOD](https://doi.org/10.1145/3664647.3681125) |
<!-- AUTO-GENERATED: BASELINES END -->

[Detailed Baseline Evidence Map →](docs/BASELINE_MAP.md)

## Comparing Results

The protocol comparator checks dataset variants, feature construction, anomaly generation, contamination, preprocessing, evaluation, and repetition policy. It returns one of four conservative states:

- `DIRECTLY_COMPARABLE`
- `CONDITIONALLY_COMPARABLE`
- `NOT_DIRECTLY_COMPARABLE`
- `UNKNOWN`

The repository does not publish a cross-protocol leaderboard. See the [comparison guide](docs/COMPARABILITY.md) or run:

```bash
python scripts/compare_protocols.py PAPER_ID_A PAPER_ID_B
```

## Data and Maintenance

[`data/papers.yaml`](data/papers.yaml) is the source of truth for paper records. Generated pages are rebuilt by [`scripts/generate_tables.py`](scripts/generate_tables.py) and checked by schema validation, reference checks, duplicate detection, link checks, and unit tests.

For release details, see the [changelog](CHANGELOG.md) and [v0.3 release report](docs/releases/v0.3.md).

## Citation and License

Citation metadata is available in [`CITATION.cff`](CITATION.cff). Code is licensed under [MIT](LICENSE-CODE); original documentation and curated metadata are licensed under [CC BY 4.0](LICENSE-CONTENT).
