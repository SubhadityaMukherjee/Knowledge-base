---
toc: true
title: Self Attention
tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:17 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Self [Attention](Attention.md)
- [paper](https://arxiv.org/abs/1706.03762v5)
- hypernetworks
- Basically [Scaled Dot Product Attention](Scaled%20Dot%20Product%20Attention.md)
- Q,K,V all from same module but prev layer
- Weighted average over all input vectors $$y_{i}= \Sigma_{j}w_{ij}x_{j}$$
	- j is over the sequence
	- weights sum to 1 over j
	- $w_{ij}$ is derived $w^{'}_{ij}=x_{i}^{T}x_{j}$
		- Any value between -inf to +inf so [Softmax](Softmax.md) is applied
	- $x_i$ is the input vector at the same pos as the current output vector $y_i$
- Propagates info between vectors
- ![](../images/Pasted%20image%2020220525183444.png)
- The process
	- Assign every word t in the vocabular an [Embedding](Embedding.md)
	- Feeding this into a self [Attention](Attention.md) layer we get another seq of vectors $y_{the}$ , $y_{cat}$ etc
	- each of the $y_{something}$ is a weighted sum over all the [Embedding](Embedding.md) vectors in the first seq weighted by their normalized dot product with $v_{something}$
	- the dot product shows how related the vectors are in the sequence
		- weights determined by them
		- Self-[Attention](Attention.md) layer may give more weights to those input vectors that are more similar to each other when generating the output vectors
- Properties
	- Inputs are a set (not sequence)
	- If input seq is permuted, the output is too
	- Ignores the sequential nature of input by itself
- Code

```python
def attention(K, V, Q):
    _, n_channels, _ = K.shape
    A = torch.einsum('bct,bcl->btl', [K, Q])
    A = F.softmax(A * n_channels ** (-0.5), 1)
    R = torch.einsum('bct,btl->bcl', [V, A])
    return torch.cat((R, Q), dim=1)
```

## Ref
- [perterbloem](https://peterbloem.nl/blog/transformers)

