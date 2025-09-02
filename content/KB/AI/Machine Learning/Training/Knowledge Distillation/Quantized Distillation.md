---
toc: true
title: Quantized Distillation

tags: ['knowledgedistillation']
date modified: Monday, October 10th 2022, 2:02:09 pm
date created: Tuesday, October 4th 2022, 11:52:35 am
---

# Quantized Distillation
- Network quantization reduces the computation com- plexity of neural networks by converting high-precision networks (e.g., 32-bit floating point) into low-precision networks (e.g., 2-bit and 8-bit). Meanwhile, knowledge distillation aims to train a small model to yield a performance comparable to that of a complex model.
- Specifically, Polino et al. (2018) proposed a quan- tized distillation method to transfer the knowledge to a weight-quantized student network. In (Mishra and Marr, 2018), the proposed quantized KD is called the “ap- prentice”. A high precision teacher network transfers knowledge to a small low-precision student network. To ensure that a small student network accurately mim- ics a large teacher network, the full-precision teacher network is first quantized on the feature maps, and then the knowledge is transferred from the quantized teacher to a quantized student network (Wei et al., 2018).



