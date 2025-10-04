---
toc: true
title: VL-BEIT

tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:14 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# VL-BEIT
- [VL-BEIT: Generative Vision-Language Pretraining](https://arxiv.org/abs/2206.01127)
- vision-language foundation model
- simple and effective approach to pretraining a bidirectional multimodal Transformer encoder for both vision-language and vision tasks learned by generative pretraining
- conducts masked prediction on both monomodal and multimodal data with a shared Transformer
- solely employs generative pretraining tasks, including [masked language modeling](masked language modeling.md) on texts, masked image modeling on images, and masked vision-language modeling on image-text pairs
- learned from scratch with one unified pretraining task, one shared backbone, and one-stage training which renders it conceptually simple and empirically effective
- transferable visual [Features](Features.md)



