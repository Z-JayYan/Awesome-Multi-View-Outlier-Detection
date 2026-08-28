# 实验协议可比性

[English](COMPARABILITY.md) | **简体中文**

> 相同数据集名称和相同指标不代表结果可以直接比较。

比较至少需要核对 source dataset、benchmark variant、feature representation、views、sample subset、anomaly generation、anomaly ratio、training contamination、preprocessing、metric、evaluation endpoint、seed/repetition 以及 transductive/inductive 假设。

四种保守状态：

| 状态 | 含义 |
|---|---|
| `DIRECTLY_COMPARABLE` | 已核实的关键 fingerprint 一致。 |
| `PARTIALLY_COMPARABLE` | 任务边界兼容，但已知协议选择不同，需要控制或解释。 |
| `NOT_DIRECTLY_COMPARABLE` | 任务设定、视图完整性或端点存在阻断差异。 |
| `INSUFFICIENT_INFORMATION` | 至少一个关键字段缺乏证据；不能假设“可能可比”。 |

仓库不建立跨协议 leaderboard；不匹配的数字只能作为 reported-result context。
