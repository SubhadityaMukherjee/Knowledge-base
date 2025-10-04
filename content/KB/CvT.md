---
tags: ['temp']
date modified: Monday, October 10th 2022, 2:02:30 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

---

toc: true
title: CvT

tags: ['temp']

---

# CvT
- [CvT: Introducing Convolutions to Vision Transformers](https://arxiv.org/abs/2103.15808)
	- improves [Vision Transformer](Vision%20Transformer.md)
	- introducing [Conv](Conv.md)
	- a hierarchy of Transformers containing a new convolutional token [Embedding](Embedding.md)
	- convolutional [Transformer](Transformer.md) block leveraging a convolutional projection
	- shift, scale, and distortion invariance
	- dynamic [Attention](Attention.md) , global context, and better generalization
	- [ImageNet](ImageNet.md)
	- [Position Encoding](Position%20Encoding.md) , a crucial component in existing Vision Transformers, can be safely removed in our model
	- potential advantage for adaption
	- built-in local context structure introduced by convolutions, CvT no longer requires a position [Embedding](Embedding.md)



