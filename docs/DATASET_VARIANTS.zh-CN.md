# 数据集与 Benchmark Variant

[English](DATASET_VARIANTS.md) | **简体中文**

> 同一 Source Dataset 不代表同一 MVOD Benchmark Variant。

源数据集只表示底层语料或图像集合；论文变体还由样本子集、视图数、特征来源、特征维度、预处理、异常生成、异常比例和评估协议共同确定。

- MODGD 的 Caltech101 记录为 9,144 个样本，SCoNE 的 Caltech 记录为 1,474 个样本，IAMOD 代码还命名了未随仓库发布的 `caltech7.mat`。它们不能合并。
- NCMOD 的 Reuters 变体使用 1,000 个样本以及 2/3 视图的 2,000 维特征切分，不能自动等同于其他 Reuters 实验。
- NCMOD 的 1,000 样本 MNIST 变体也不等于 70,000 样本的源数据集。

详细逐项记录见英文生成页。`unknown` 表示当前 primary evidence 不足，不代表事实不存在。
