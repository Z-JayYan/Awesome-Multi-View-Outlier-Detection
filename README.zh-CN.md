# Awesome Multi-View Outlier Detection (MVOD)

[English](README.md) | **简体中文**

**论文 · 代码 · 数据集 · 方法分类 · 基线 · 可复现性**

一个面向多视图离群检测（MVOD）的研究门户，汇集论文、代码、数据集、方法谱系、基线和可复现资源。仓库以机器可读元数据和证据支持的协议审计为研究提供支撑，不对缺失信息作推测。

<!-- AUTO-GENERATED: STATS START -->
[![Papers](https://img.shields.io/badge/papers-42-4c1)](docs/PAPERS.md) [![Verified records](https://img.shields.io/badge/verified-42-2f855a)](docs/QUALITY_AUDIT.md) [![Official code](https://img.shields.io/badge/official_code-20-2563eb)](docs/REPRODUCIBILITY.md) [![Datasets](https://img.shields.io/badge/datasets-13-7c3aed)](docs/DATASETS.md) [![License: CC BY 4.0](https://img.shields.io/badge/license-CC_BY_4.0-lightgrey)](LICENSE-CONTENT)
<!-- AUTO-GENERATED: STATS END -->

## 🔥 最新更新

<!-- AUTO-GENERATED: UPDATES START -->
- **2026 覆盖：**CORE 及相关多视图异常设定共收录 10 条记录。
- **研究地图：**重新组织方法分类与代表性研究路线。
- **数据集：**13 个源数据集已关联到论文级 benchmark 变体。
- **v0.3：**重构研究门户、中英文入口和协议感知的基线指南。

[查看完整变更记录 →](CHANGELOG.md)
<!-- AUTO-GENERATED: UPDATES END -->

## 什么是 MVOD？

MVOD 研究由多个对齐视图描述的对象，例如不同特征集、语言、传感器或相机角度。它要找出在单个视图内、多个视图之间，或两者中同时异常的对象。

- **属性异常：**对象在一个或多个单独视图内异常。
- **类别异常：**各视图在局部看起来可能正常，但跨视图的语义或实例对应关系不一致。
- **混合异常：**属性级异常与跨视图/类别级异常同时存在。

这些是异常的概念定义，不是固定的合成扰动配方。不同 MVOD 方法利用不同证据识别这些异常。

## 研究范围

### 核心研究范围

**CORE — 完整视图多视图离群检测**假设每个对象都具备全部对齐特征视图，是本仓库的主要 benchmark 空间。CORE 是任务设定；浅层、深度、图、张量、生成式与对比学习方法都可能属于 CORE。

### 扩展 MVOD 设定

**Partial / Incomplete MVOD** 研究存在视图缺失的对象。它在方法上与 CORE 相关，但缺失观测形成了不同的协议和比较边界。

### 相关多视图异常检测

**Industrial / Natural MVAD** 包括多相机图像、RGB-D、点云和自然缺陷。这些研究与 CORE 共享跨视图思想，但数据、监督和评估方式不同。

## 快速导航

- 📚 [完整论文数据库](docs/PAPERS.md)
- 🧠 [方法分类](docs/METHOD_TAXONOMY.md)
- 🌳 [MVOD 研究地图](docs/PAPER_TREE.md)
- 🧪 [数据集与 benchmark 变体](docs/DATASETS.md)
- ⚔️ [基线选择指南](docs/BASELINE_MAP.md)
- 🔬 [协议可比性](docs/COMPARABILITY.zh-CN.md)
- ♻️ [可复现性](docs/REPRODUCIBILITY.md)
- 🤝 [贡献指南](CONTRIBUTING.md)

## 近期论文

此处只展示近年精选论文，由 [`data/papers.yaml`](data/papers.yaml) 中已核实且标记为 featured 的记录自动生成。论文题目保留原文，避免翻译造成歧义。

<!-- AUTO-GENERATED: RECENT START -->
### 2026

- **MVAS** — Learning Multi-View Anomaly Detection With Efficient Adaptive Selection — *IEEE Transactions on Multimedia 2026* · `RELATED` · [论文](https://doi.org/10.1109/TMM.2026.3660076)
- **MOD-TDID** — Multi-view outlier detection via tensor decomposition and information decoupling — *Applied Intelligence 2026* · `CORE` · [论文](https://doi.org/10.1007/s10489-026-07375-y) · [代码](https://github.com/YF-W/MOD-TDID)
- **RNAMOD** — Reliable Neighborhood-Aware Multi-View Outlier Detection — *ICML 2026* · `CORE` · [论文](https://openreview.net/forum?id=mL4B6DdgPU)
- **SCoNE** — SCoNE: Spherical Consistent Neighborhoods Ensemble for Effective and Efficient Multi-View Anomaly Detection — *AAAI 2026* · `CORE` · [论文](https://doi.org/10.1609/AAAI.V40I19.38643)

### 2025

- **LRTDM** — Low-rank Tucker decomposition for multi-view outlier detection based on meta-learning — *Information Fusion 2025* · `CORE` · [论文](https://doi.org/10.1016/j.inffus.2025.103313)
- **MGFMOD** — Multi-view outlier detection based on multi-granularity fusion of fuzzy rough granules — *International Journal of Approximate Reasoning 2025* · `CORE` · [论文](https://doi.org/10.1016/j.ijar.2025.109402) · [代码](https://github.com/YF-W/MGFMOD)
- **MODGF** — Unsupervised Multi-View Outlier Detection via Optimal Graph Filtering — *ICASSP 2025* · `CORE` · [论文](https://doi.org/10.1109/ICASSP49660.2025.10889803)
- **IDIF** — Unveiling Multi-View Anomaly Detection: Intra-view Decoupling and Inter-view Fusion — *AAAI 2025* · `RELATED` · [论文](https://doi.org/10.1609/AAAI.V39I12.33349) · [代码](https://github.com/Kerio99/IDIF)

### 2024

- **IAMOD** — Information-aware Multi-view Outlier Detection — *ACM TKDD 2024* · `CORE` · [论文](https://doi.org/10.1145/3638354) · [代码](https://github.com/GTML-LAB/IAMOD)
- Learning Diffusion Models for Multi-view Anomaly Detection — *ECCV 2024* · `RELATED` · [论文](https://doi.org/10.1007/978-3-031-73414-4_19) · [代码](https://github.com/jayliu0313/Diffusion_Multi-View_AD)
- **MODGD** — Multi-view Outlier Detection via Graphs Denoising — *Information Fusion 2024* · `CORE` · [论文](https://doi.org/10.1016/j.inffus.2023.102012) · [代码](http://Doctor-Nobody.github.io/codes/MODGD.zip)
- **RCPMOD** — Regularized Contrastive Partial Multi-view Outlier Detection — *ACM MM 2024* · `PARTIAL` · [论文](https://doi.org/10.1145/3664647.3681125)
- **SeeM** — SeeM: A Shared Latent Variable Model for Unsupervised Multi-view Anomaly Detection — *PAKDD 2024* · `CORE` · [论文](https://doi.org/10.1007/978-981-97-2242-6_7) · [代码](https://github.com/thanhphuong163/SeeM)

[浏览完整论文数据库 →](docs/PAPERS.md)
<!-- AUTO-GENERATED: RECENT END -->

## 数据集概览

> **数据集名称 ≠ 实验协议身份。**不同论文在同名数据集上可能使用不同样本、视图、特征、预处理和异常构造。

首页只展示稳定的数据源级信息。精确维度、比例和论文特定变体保留在[数据集卡片](docs/DATASETS.md)与[变体数据库](docs/DATASET_VARIANTS.zh-CN.md)中。

<!-- AUTO-GENERATED: DATASETS START -->
| 数据集 | 领域 | 范围 | 备注 |
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

## 如何选择基线

先根据基线代表的科学问题进行选择，再核对实验协议是否兼容。

<!-- AUTO-GENERATED: BASELINES START -->
| 研究问题 / 机制 | 代表性锚点 |
|---|---|
| 历史基础 | [DMOD](https://www.ijcai.org/Abstract/15/572), [LDSR](https://doi.org/10.1609/AAAI.V32I1.11826) |
| 局部 / 邻域 | [SRLSP](https://doi.org/10.1145/3532191), [RNAMOD](https://openreview.net/forum?id=mL4B6DdgPU), [SCoNE](https://doi.org/10.1609/AAAI.V40I19.38643) |
| 共享潜变量 / 生成式 | [dPoE](https://doi.org/10.1145/3581783.3612487) |
| 信息论 | [IAMOD](https://doi.org/10.1145/3638354) |
| 图方法 | [MODGD](https://doi.org/10.1016/j.inffus.2023.102012), [RNAMOD](https://openreview.net/forum?id=mL4B6DdgPU) |
| 张量 / 低秩 | [LRTDM](https://doi.org/10.1016/j.inffus.2025.103313), [MOD-TDID](https://doi.org/10.1007/s10489-026-07375-y) |
| 部分视图对比学习 | [RCPMOD](https://doi.org/10.1145/3664647.3681125) |
<!-- AUTO-GENERATED: BASELINES END -->

[查看详细基线证据图 →](docs/BASELINE_MAP.md)

## 如何比较结果

协议比较器会检查数据集变体、特征构造、异常生成、污染、预处理、评估与重复实验策略，并返回四种保守状态之一：

- `DIRECTLY_COMPARABLE`
- `CONDITIONALLY_COMPARABLE`
- `NOT_DIRECTLY_COMPARABLE`
- `UNKNOWN`

本仓库不发布跨协议排行榜。详见[可比性指南](docs/COMPARABILITY.zh-CN.md)，或运行：

```bash
python scripts/compare_protocols.py PAPER_ID_A PAPER_ID_B
```

## 数据与维护

[`data/papers.yaml`](data/papers.yaml) 是论文记录的唯一真实来源。生成页面由 [`scripts/generate_tables.py`](scripts/generate_tables.py) 重建，并经过 schema 验证、引用检查、重复检测、链接检查和单元测试。

发布详情见[变更记录](CHANGELOG.md)和 [v0.3 发布报告](docs/releases/v0.3.zh-CN.md)。

## 引用与许可

引用元数据见 [`CITATION.cff`](CITATION.cff)。代码按 [MIT](LICENSE-CODE) 许可；原创文档与整理的元数据按 [CC BY 4.0](LICENSE-CONTENT) 许可。
