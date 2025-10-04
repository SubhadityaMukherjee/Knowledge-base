---
tags: ['temp']
date modified: Monday, October 10th 2022, 2:02:33 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

---

toc: true
title: BYOL

tags: ['temp']

---

# BYOL
- [Bootstrap Your Own Latent: a New Approach to Self-supervised Learning](https://arxiv.org/abs/2006.07733)
	- [Self Supervised](Self%20Supervised.md) image representation learning
	- predicting previous versions of its outputs, without using negative pairs
	- two neural networks, referred to as online and target networks
	- that interact and learn from each other
	- From an augmented view of an image, they train the [[Online Learning]] network to predict the target network representation of the same image under a different augmented view
	- update the target network with a slow-moving average of the online network
	- [ImageNet](ImageNet.md)
	- [Res Net](Res%20Net.md)
	- dependent on existing sets of [[Augmentation.md|Augmentation]] that are specific to vision applications
	- [BYOL Loss](BYOL%20Loss.md)



