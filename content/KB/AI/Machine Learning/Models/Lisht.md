---
toc: true
title: Lisht

tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:23 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Lisht
- ![](../images/Pasted%20image%2020220625234951.png)
- Derivatives
	- ![](../images/Pasted%20image%2020220625234959.png)
- [blog](https://github.com/christianversloot/machine-learning-articles/blob/main/beyond-swish-the-lisht-activation-function.md) #[Roam-Highlights](Roam-Highlights)
    - Linearly Scaled Hyperbolic Tangent
    - his activation function simply uses the [Tanh](Tanh.md) function and scales it linearly, as follows
    - $$LiSHT(x) = x \times tanh(x)$$
    - Essentially, LiSHT looks very much like [Swish](Swish.md) in terms of the first-order derivative. However, the range is expanded into the negative as well, which means that the vanishing gradient problem is reduced even further - at least in theory.
    - In their work, Roy et al. (2019) report based on empirical testing that indeed, the vanishing gradient problems is reduced compared to [Swish](Swish.md) and traditional [Relu](Relu.md). Additional correlations between network learning and the shape of e.g. the LiSHT loss landscape were identified.



