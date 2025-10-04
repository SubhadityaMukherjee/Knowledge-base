---
toc: true
title: FTSwish

tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:28 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# FTSwish
- ![](../images/Pasted%20image%2020220626150952.png)
- [Relu](Relu.md) + [Sigmoid](Sigmoid.md)
- $$\begin{equation} FTSwish: f(x) = \begin{cases} T, & \text{if}\ x < 0 \\ \frac{x}{1 + e^{-x}} + T, & \text{otherwise} \\ \end{cases} \end{equation}$$
- As we can see, the [Sparsity](Sparsity.md) principle is still true - the neurons that produce negative values are taken out.
- What we also see is that the derivative of FTSwish is smooth, which is what made [Swish](Swish.md) theoretically better than [Relu](Relu.md) in terms of the loss landscape
- However, what I must note is that this function does not protect us from the dying [Relu](Relu.md) problem: the gradients for $x < 0$ are zero, as with [Relu](Relu.md).



