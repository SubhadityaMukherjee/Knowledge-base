---
toc: true
title: DeepNet

tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:30 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# DeepNet
- [DeepNet: Scaling Transformers to 1,000 Layers](https://arxiv.org/abs/2203.00555)
- allows train extremely deep transformers with 1000L+ [Layers](Layers.md)
- fundamental, effective and simple
- can be used in any Transformer architecture (encoder, decoder, encoder-decoder) which covers almost all different tasks across AI areas (language, vision, speech, multimodal, and beyond)
- newly proposed normalization function
- [DeepNorm](DeepNorm.md)
- It works alongside a dedicated [Initialization](Initialization.md) scheme based on [Xavier Initialization](Xavier%20Initialization.md).
- These two tricks lead to greater stability during the training which allows the authors to scale their modified Transformer architecture (DeepNet) up to 1000 [Layers](Layers.md)



