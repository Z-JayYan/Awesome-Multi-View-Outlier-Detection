# MVOD Research Landscape

[English] | [简体中文](RESEARCH_LANDSCAPE.zh-CN.md)

This document explains changes in scientific questions and inductive biases across the registry. It is not a chronology of superiority, and papers in the same section are not necessarily benchmark-compatible.

## Problem Setting

MVOD scores aligned objects using evidence from multiple views. The repository separates complete-view CORE, partial/incomplete-view, and industrial/natural multimodal settings because their observation assumptions and endpoints differ. Attribute, class, mixed, generic, and natural anomaly labels do not by themselves specify an identical anomaly operator.

## Early Structural Modeling

Early methods asked how disagreement or incomplete consensus across views could expose unusual objects. HOAD used clustering and graph structure; DMOD, MLRA, and LDSR developed shared representation, low-rank, and subspace formulations. Self-representation remains a useful counterfactual to learned deep models because it isolates explicit structural constraints.

## Shared Representation and Deep Modeling

PLVM, MODDIS, CGAEs, and dPoE increasingly learned spaces in which cross-view consistency could be modeled through latent variables, reconstruction, prediction, or shared/private evidence. These are different assumptions and should not be collapsed into one “deep” family for comparison.

## Local Structure and Relation Modeling

NCMOD, SRLSP, MODGD, and RNAMOD focus on neighborhood consensus, local similarity, graph denoising, and reliability. Graph construction, neighborhood definition, and feature scaling become protocol-critical rather than incidental preprocessing.

## Contrastive, Information, and Robust Representation

IAMOD, RCPMOD, and reliability-aware methods introduce information constraints, contrastive objectives, robust graphs, or view reliability. They do not simply replace reconstruction or subspace approaches; they encode different assumptions about meaningful agreement.

## Efficiency and Structural Simplification

SRLSP, SCoNE, and MOD-TDID represent fast structural, low-training/learning-free neighborhood, and high-order tensor alternatives. They reopen the question of whether complex deep representation is necessary for every MVOD regime. Runtime claims still require matched hardware, implementation, data, and stopping conditions.

## Partial / Incomplete MVOD

Missing views change the observation model: a method must distinguish absent evidence from anomalous evidence. RCPMOD belongs here. Its mechanisms may be relevant to CORE, but its results cannot be pooled with complete-view benchmarks.

## Industrial / Natural Multi-View Anomaly Detection

Industrial MVAD often uses images, RGB-D, point clouds, natural defects, normal-only training, and image/pixel endpoints. It shares alignment and reconstruction mechanisms with CORE but remains a parallel adjacent track, not CORE's next generation.

## Open Research Questions

Evidence in the registry supports restrained questions about protocol inconsistency, benchmark fragmentation, anomaly-definition ambiguity, incomplete reporting, scalability, reliability, natural versus synthetic anomalies, training contamination, global versus local consistency, and reproducibility. It does not support claims that these areas are wholly unstudied.
