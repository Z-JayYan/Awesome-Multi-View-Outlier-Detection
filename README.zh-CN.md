# Awesome Multi-View Outlier Detection

[English](README.md) | **简体中文**

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Registry validation](https://github.com/Z-JayYan/Awesome-Multi-View-Outlier-Detection/actions/workflows/validate.yml/badge.svg)](https://github.com/Z-JayYan/Awesome-Multi-View-Outlier-Detection/actions/workflows/validate.yml)
[![Papers](https://img.shields.io/badge/papers-42-4c1)](data/papers.yaml)
[![Version](https://img.shields.io/badge/version-0.3.0-blue)](CHANGELOG.md)

> 面向多视图离群检测（MVOD）研究者的、可审计且机器可读的科研知识库，并严格区分相邻的多视图异常检测任务。

**v0.3.0 — 科研可用性与研究脉络。** 本版本将结构化论文 registry 与方法演化、baseline 选择、benchmark variant 和协议可比性连接起来。

> **同名数据集不代表相同 benchmark protocol。** 无法从论文、supplementary material、官方代码或作者页面核实的字段保留为 `unknown`。

`论文 → Benchmark Variant → Protocol Fingerprint → 可比性`

## 什么是 MVOD？

多视图离群检测利用同一对象的多个特征视图计算异常证据。不同论文中的异常可能指属性异常、类别异常、混合异常、未细分的通用异常或真实自然缺陷；这些定义相关，但不能直接互换。

本仓库帮助研究者理解方法如何演化、选择科学上合理的 baseline，并判断两个结果是否具有足够一致的实验协议。机器可读 registry 是 single source of truth，网页表格只是导航视图。

## 仓库范围

| 轨道 | 定义 | 常见端点 | 直接比较边界 |
|---|---|---|---|
| **Track 1 — CORE：完整视图 MVOD** | 每个对象拥有全部对齐特征视图，视图间样本对应明确。 | 对象/样本异常分数 | 完整视图 MVOD 主比较空间 |
| **Track 2 — PARTIAL / INCOMPLETE MVOD** | 对齐对象可能缺失一个或多个视图，方法同时处理缺失观测与异常。 | 缺失视图协议下的对象/样本分数 | 与完整视图结果分开 |
| **Track 3 — INDUSTRIAL / NATURAL MVAD** | 多相机、RGB/depth、点云或传感器观察带真实缺陷的对象或场景。 | 样本、图像、对象或像素端点 | 不与特征级完整视图 MVOD 合并 |

CORE 是任务设定，不等于 classical、shallow 或 non-deep。深度、对比学习、图和张量方法都可以属于 CORE。

## 从这里开始

- [研究脉络](docs/RESEARCH_LANDSCAPE.zh-CN.md) · [English](docs/RESEARCH_LANDSCAPE.md)
- [方法分类](docs/METHOD_TAXONOMY.md)
- [异常类型分类](docs/ANOMALY_TAXONOMY.md)
- [数据集与 Benchmark Variant](docs/DATASET_VARIANTS.zh-CN.md) · [English](docs/DATASET_VARIANTS.md)
- [Baseline Map](docs/BASELINE_MAP.md)
- [协议可比性规则](docs/COMPARABILITY.zh-CN.md) · [English](docs/COMPARABILITY.md)
- [完整论文数据库](docs/PAPERS.md)
- [v0.3 中文审计报告](V0.3_REVIEW_REPORT.zh-CN.md)

命令行比较两个已重建协议：

```bash
python scripts/compare_protocols.py PAPER_ID_A PAPER_ID_B
```

## 验证维度

Bibliography、artifact 和 protocol verification 相互独立。论文书目信息已核实，不代表实验协议可以复现；发现官方代码，也不表示配置、数据预处理和 checkpoint 均已发布。

| 审计维度 | 状态 |
|---|---:|
| 书目信息已核实 | 42 / 42 |
| 官方 artifact 已核实 | 以英文 README 的自动生成统计为准 |
| 协议充分/部分核实 | 以英文 README 和 BUILD_REPORT 的自动生成统计为准 |

## 比较规则

保守状态为 `DIRECTLY_COMPARABLE`、`PARTIALLY_COMPARABLE`、`NOT_DIRECTLY_COMPARABLE` 和 `INSUFFICIENT_INFORMATION`。

> **相同数据集 + 相同指标，不代表结果可以直接比较。**

必须检查 source dataset、benchmark variant、feature representation、views、sample subset、anomaly generation、ratio、training contamination、preprocessing、metric、endpoint、seed/repetition 以及 transductive/inductive 假设。

本仓库不建立跨协议 leaderboard。

## 论文表与最新研究

完整的 42 篇论文表和按 Track → Year → Venue 生成的最新研究列表位于英文首页及 [论文数据库](docs/PAPERS.md)。论文标题、作者、venue 和链接保留原文，避免翻译造成身份歧义。

异常缩写：**A = Attribute（属性）**、**C = Class（类别）**、**M = Mixed / Class-Attribute（混合）**、**G = Generic（通用/未细分）**、**N = Natural（自然缺陷）**。

## 贡献与引用

提交修正前请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)，修改 registry 后重新生成派生文件并运行全部校验。引用信息见 [CITATION.cff](CITATION.cff)。
