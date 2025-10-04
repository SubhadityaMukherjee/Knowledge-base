---
tags: ['temp']
toc: true
title: Detailed Balance
date modified: Monday, October 10th 2022, 2:02:30 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Detailed Balance
- To find a transition kernel T(x|y) for a homogenous, [Ergodic](Ergodic.md) [Markov Chain](Markov%20Chain.md)
- If we pick some state x with the [Probability](Probability.md) given by g and multiply its prob g(x) with the transition [Probability](Probability.md) [Density](Density.md) T(x|y) (weighted by [Probability](Probability.md) [Density](Density.md) of x) then its the same as the reverse weighted transiting [Probability](Probability.md) [Density](Density.md) from y to x
- $$\forall x,y \in \mathbb{R}^{k}: T(y|x)g(x) = T(x|y)g(y)$$
- If T(x|y) has detailed balance wrt g, then it is an [Invariant Distribution](Invariant%20Distribution.md)
- $$\int_{\mathbb{R}^{k}}T(x|y)g(y)dy = \int_{\mathbb{R}^{k}}T(y|x)g(x)dy = g(x)\int_{\mathbb{R}^{k}}P(y|x)dy = g(x)$$



