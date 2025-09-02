---
toc: true
title: DeepPERF

tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:30 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# DeepPERF
- [DeepPERF: a Deep Learning-Based Approach for Improving Software Performance](https://arxiv.org/abs/2206.13619)
- Performance bugs may not cause system failure and may depend on user input, so detecting them can be challenging
- harder to fix than non-performance bugs
- performance bug detection approaches have emerged to help developers identify performance [Issues](Issues.md)
- Building rule-based analyzers is a non-trivial task, as it requires achieving the right balance between precision and [Recall](Recall.md)
- Once developed, maintaining these rules can also be costly
- large [Transformer](Transformer.md) model to suggest changes at application source code level to improve its performance
- first pretrain the model using masked language modelling (MLM) tasks on English text and source code taken from open source repositories on GitHub, followed by finetuning on millions of performance commits made by .NET developers
- recommend patches to provide a wide-range of performance optimizations in C`#` applications
- Most suggested changes involve modifications to high-level constructs like API/Data Structure usages or other algorithmic changes, often spanning multiple methods, which cannot be optimized away automatically by the C`#` compiler and could, therefore, lead to slow-downs on the user’s side



