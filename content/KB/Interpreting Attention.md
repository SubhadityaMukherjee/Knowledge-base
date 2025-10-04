---
toc: true
title: Interpreting Attention

tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:24 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Interpreting [Attention](Attention.md)
- [Attention Interpretability Across NLP Tasks](https://arxiv.org/abs/1909.11218)
- empirically prove the hypothesis that [Attention](Attention.md) weights are interpretable and are correlated with feature importance measures
- n both single and pair sequence tasks, the [Attention](Attention.md) weights in samples with original weights do make sense in general
- However, in the former case, the [Attention](Attention.md) mechanism learns to give higher weights to tokens relevant to both kinds of sentiment.
- They show that [Attention](Attention.md) weights in single sequence tasks do not provide a reason for the prediction, which in the case of pairwise tasks, [Attention](Attention.md) do reflect the reasoning behind model output
- [BertViz](https://github.com/jessevig/bertviz) repo



