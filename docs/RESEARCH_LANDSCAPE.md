# MVOD Research Landscape

[English] | [简体中文](RESEARCH_LANDSCAPE.zh-CN.md)

This is a short guide to how the field's questions changed over time. Papers grouped together here may still use different datasets and protocols.

## Problem Setting

MVOD looks for unusual objects described by several views. Most early benchmarks assume that every object has every view; partial-view work relaxes that assumption. Industrial work usually deals with real defects in images or sensor data. These settings share ideas, but they do not test the same task.

## Early Structural Modeling

Early work treated an outlier as an object that did not fit the structure shared across views. HOAD used clustering and graphs. DMOD, MLRA, and LDSR used shared coefficients, low-rank structure, or discriminative subspaces. These methods remain useful baselines because their assumptions are explicit and relatively easy to isolate.

## Shared Representation and Deep Modeling

Later methods learned the shared structure instead of specifying it only through linear constraints. PLVM introduced a probabilistic latent model; MODDIS learned a deep intact space; CGAEs used cross-view reconstruction; dPoE separated shared and private evidence. Reconstruction, prediction, and probabilistic fusion answer related but distinct questions.

## Local Structure and Relation Modeling

A single global representation can miss small, local inconsistencies. NCMOD moved toward neighborhood consensus, SRLSP preserved local similarity, MODGD denoised view graphs, and RNAMOD modeled whether a neighborhood is trustworthy. In this line of work, graph construction and feature scaling directly affect what the method sees as anomalous.

## Contrastive, Information, and Robust Representation

IAMOD asks which cross-view information is useful. RCPMOD uses contrastive learning when views may be missing. Reliability-aware methods try to stop noisy views or neighborhoods from dominating the score. These methods add new ways to control agreement rather than making older structural models obsolete.

## Efficiency and Structural Simplification

Recent work also revisits cost and complexity. SRLSP emphasizes fast self-representation; SCoNE builds an efficient neighborhood ensemble; MOD-TDID uses tensor structure to separate shared and view-specific information. The practical question is simple: when does a more complex learned representation justify its cost?

## Partial / Incomplete MVOD

When views are missing, a method must distinguish absent evidence from anomalous evidence. RCPMOD is included as an important methodological reference, but its reported results should not be mixed with complete-view benchmarks.

## Industrial / Natural Multi-View Anomaly Detection

Industrial MVAD often uses images, RGB-D, point clouds, normal-only training, and image- or pixel-level evaluation. It shares alignment and reconstruction ideas with feature-level MVOD, but studies different data and anomaly semantics.

## Open Research Questions

The clearest unresolved issue is not a lack of methods, but uneven experimental practice. Dataset names often hide different features or anomaly generators; seeds and preprocessing are frequently missing; synthetic and natural anomalies are easy to conflate. Better reporting would make progress easier to measure.
