---
toc: true
title: ConvBERT

tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:31 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# ConvBERT
- Convolutional BERT (ConvBERT) improves the original [BERT](BERT.md) by replacing some [Multi Head Attention](Multi%20Head%20Attention.md) [Self Attention](Self%20Attention.md) segments with cheaper and naturally local operations, so-called [span-based dynamic convolutions](span-based%20dynamic%20convolutions). These are integrated into the self-[Attention](Attention.md) mechanism to form a mixed [Attention](Attention.md) mechanism, allowing Multi-headed Self-[Attention](Attention.md) to capture global patterns; the Convolutions focus more on the local patterns, which are otherwise captured anyway. In other words, they reduce the computational intensity of training BERT.



