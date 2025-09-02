---
toc: true
title: Swish
tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:15 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Swish
- $$x\cdot sigmoid(x)$$
- While Swish reportedly improves model performance (Ramachandran et al., 2017), it still does not allow you to avoid [Vanishingexploding gradients](Vanishingexploding%20gradients.md)
- Even though the vanishing gradients problem is much less severe in case of Swish, only inputs of $x >= 2$ result in gradients of 1 and (sometimes) higher. In any other case, the gradient will still cause the chain to get smaller with increasing [Layers](Layers.md).
- Move to [Lisht](Lisht.md)
- non monotonic
- First, it is bounded below. Swish therefore benefits from [Sparsity](Sparsity.md) similar to [Relu](Relu.md). Very negative weights are simply zeroed out.
- Second, it is unbounded above. This means that for very large values, the outputs do not saturate to the maximum value (i.e., to 1 for all the neurons). According to the authors of the Swish paper, this is what set [Relu](Relu.md) apart from the more traditional activation functions.
- Third, separating Swish from [Relu](Relu.md), the fact that it is a smooth curve means that its output landscape will be smooth. This provides benefits when optimizing the model in terms of convergence towards the minimum [loss](../Tag%20Pages/loss.md).
- Fourth, small negative values are zeroed out in [Relu](Relu.md) (since f(x) = 0 for x < 0). However, those negative values may still be relevant for capturing patterns underlying the data, whereas large negative values may be zeroed out (for reasons of [Sparsity](Sparsity.md), as we saw above). The [Smoothness](Smoothness.md) property and the values of f(x) < 0 for x ≈ 0 yield this benefit. This is a clear win over [Relu](Relu.md).
- ![](../images/Pasted%20image%2020220626151728.png)



