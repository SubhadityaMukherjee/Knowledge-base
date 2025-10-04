---
toc: true
title: Vanishing Gradient

tags: ['architecture']
date modified: Tuesday 7th February 2023, Tue
date created: Tuesday 7th February 2023, Tue
---

# Vanishing Gradient


- Deltas become smaller initially. using [Sigmoid] -> [ill conditioning](Sigmoid] -> [ill conditioning.md) 
- $$g(x) = (1+e^{-x})^{-1}$$
- $$\nabla_{x}[g] = g(1-g) \in [0,1]$$
- Saturation and prevent [Backprop](Backprop.md) 
- $$g(x) \approx 1 \rightarrow \nabla_{x}[g] \approx 0 $$
- Weight matrices are usually initialized with random values $|w_{ji}| << 1$ 
	- gradient magnitueds decay exponentially -> max eigenvalue



