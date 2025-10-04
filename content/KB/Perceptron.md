---
tags: ['temp']
toc: true
title: Perceptron
tag: architecture
date modified: Monday, October 10th 2022, 2:02:20 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Perceptron
- $$f(x)=sign(\Sigma _i w_ix_i +b) = sign(\mathbf{w^Tx}+b)$$
	- $$sign(x) = \begin{cases} 1 & x\geq0 \\ 0 & otherwise\end{cases}$$
![](../images/Pasted%20image%2020220304121008.png)
- computational graph![](../images/Pasted%20image%2020220304121221.png)
- Multi layer
	- Stack multiple perceptrons
	- $$\begin{align} \\& h_0 = x h1= sign(\mathbf{w_1^T}+b_1) \\ &…\\& h1= sign(\mathbf{w_{L-1}^T}+b_L) \end{align}$$



