---
toc: true
title: Dot Product Attention

tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:29 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Dot Product [Attention](Attention.md)
- [Luong et al., 2015](https://arxiv.org/pdf/1508.04025.pdf)
- $$f_{att}(h_{i}, s_{j}) = h_{i}^{T}s_{j}$$
- Equivalent to [Multiplicative Attention](Multiplicative%20Attention.md) with no trainable weight matrix. Performs better at larger dimensions
- Identity matrix
- $h$ is hidden state for encoder and $s$ is hidden state for decoder
- A type of [Attention Alignment](Attention%20Alignment.md)
- Final scores after [Softmax](Softmax.md)
- ![](../images/Pasted%20image%2020220621174933.png)



