---
toc: true
title: Scaled Dot Product Attention
tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:17 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Scaled [Dot Product Attention](Dot%20Product%20Attention.md)
- [Vaswani et al., 2017](https://arxiv.org/abs/1706.03762)
- Q is query, K is key V is value. Same dims
- $q_{i}= W_{q}x_i$ , $k_{i}= W_{k}x_{i}$ , $v_{i}= W_{v}x_{i}$
	- $w_{ij}' = q_{i}^{T}k_{j}$
	- $y_{i}= \Sigma_{j}w_{ij}v_{j}$
- [Softmax](Softmax.md) is sensitive to large values. Which sucks for the #architecture
- The avg value of the dot product grows with [Embedding](Embedding.md) dimension k. So scale back.
	- $\sqrt{k}$ . Vector in $\mathbb{R}^{k}$ with all values as c
	- Euclidean length is $\sqrt{kc}$
- $$Attention(Q, K,V) = softmax(\frac{QK^T}{\sqrt{d_{k}}})V$$
- Generalization of [Soft Attention](Soft%20Attention.md)
- ![](../images/Pasted%20image%2020220526133045.png)
- [Attention Alignment](Attention%20Alignment.md) score $$\alpha_{t,i} = \frac{s_{t}^{T}h_{i}}{\sqrt{n}}$$



