# Awesome Multi-View Outlier Detection

[English](README.md) | **简体中文**

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Registry validation](https://github.com/Z-JayYan/Awesome-Multi-View-Outlier-Detection/actions/workflows/validate.yml/badge.svg)](https://github.com/Z-JayYan/Awesome-Multi-View-Outlier-Detection/actions/workflows/validate.yml)
[![Papers](https://img.shields.io/badge/papers-42-4c1)](data/papers.yaml)
[![Version](https://img.shields.io/badge/version-0.3.0-blue)](CHANGELOG.md)

多视图离群检测（MVOD）的论文、代码、数据集和实验协议索引。所有表格都由结构化数据生成，便于检查和维护。

## 什么是 MVOD？

一个对象可以有多种描述，例如不同特征、语言、传感器或拍摄角度。MVOD 的目标，是找出在单个视图内或多个视图之间表现异常的对象。

仓库主要解决三件事：快速了解领域、选择基线方法、核对论文结果能否直接比较。

## 仓库范围

这里按问题设定分组，而不是按“传统方法/深度方法”分组。

| 轨道 | 问题设定 | 为什么分开 |
|---|---|---|
| **CORE / 完整视图 MVOD** | 每个对象都有全部对齐视图。 | 这是特征级 MVOD 的主要设定。 |
| **PARTIAL / 不完整视图 MVOD** | 部分对象缺少一个或多个视图。 | 缺失观测改变了任务和实验协议。 |
| **INDUSTRIAL / 自然异常检测** | 图像或传感器从多个角度记录真实缺陷。 | 数据、监督方式及图像/像素评估均不同。 |

深度、图、张量和对比学习方法都可能属于 CORE。

## 从这里开始

- **初次了解 MVOD：** [研究脉络](docs/RESEARCH_LANDSCAPE.zh-CN.md)
- **选择方法：** [方法分类](docs/METHOD_TAXONOMY.md) · [基线方法图](docs/BASELINE_MAP.md)
- **核对实验：** [数据集变体](docs/DATASET_VARIANTS.zh-CN.md) · [可比性规则](docs/COMPARABILITY.zh-CN.md)
- **查找资料：** [论文数据库](docs/PAPERS.md) · [异常类型](docs/ANOMALY_TAXONOMY.md)

命令行比较两个已重建协议：

```bash
python scripts/compare_protocols.py PAPER_ID_A PAPER_ID_B
```

## 如何理解“已核实”

论文题目、作者和出处已核实，不代表实验可以复现。官方代码、配置、数据处理、预训练权重和实验协议是分别记录的；查不到的内容保留为 `unknown`。

## 比较规则

数据集名称和评价指标相同，结果仍可能不能直接比较。还需要核对样本子集、视图、特征、异常构造、异常比例、预处理、训练/测试划分和重复实验方式。详见[可比性规则](docs/COMPARABILITY.zh-CN.md)。本仓库不制作跨协议排行榜。

## 论文表与最新研究

完整的 42 篇论文表和最新研究列表位于英文首页及[论文数据库](docs/PAPERS.md)。论文标题、作者和期刊/会议信息保留原文，避免翻译造成歧义。

异常缩写：**A = 属性异常**、**C = 类别异常**、**M = 混合异常**、**G = 未细分异常**、**N = 自然缺陷**。

## 贡献与引用

提交修正前请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。引用信息见 [CITATION.cff](CITATION.cff)。
