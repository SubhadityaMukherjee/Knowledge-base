---
tags: ['temp']
toc: true
title: Markov for Continuous Distributions
date modified: Monday, October 10th 2022, 2:02:22 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Markov for Continuous Distributions
- Family of [PDF](PDF.md)
- If a [Markov Chain](Markov%20Chain.md) with state set S, matrix M is executed m times . The transition probabilities transmit between states and then, $$P(X_{n+m}=s_{j}|X_{n}= s_{i}) = M^{m}(i, j)$$
- where $M^{m}= M \cdot M \cdot M … \cdot M$ (m times)
- To get the [PDF](PDF.md) $$g^{n+1}(x) = \int_{\mathbb{R}^{k}}T(x|y)g^{n}(y)dy$$
- [Invariant Distribution](Invariant%20Distribution.md)



