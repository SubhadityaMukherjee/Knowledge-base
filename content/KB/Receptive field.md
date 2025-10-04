---
toc: true
title: Receptive field
tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:18 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Receptive Field
- Not for Dense, only local connected [Layers](Layers.md) like [Conv](Conv.md), [Pooling](Pooling.md)
- A neuron's receptive field is the patch of the total field of view that a single neuron has access to
- Almost a logarithmic relationship between classification accuracy and receptive field size
	- Large fields are almost necessary for high level recognition tasks, but with diminishing rewards
- $$r(i-1) = s_{i}\times r_{i} + (k_{i}-s_{i})$$
- ![](https://theaisummer.com/static/f0e95de5fb54ce75ebdf93c0bd576ebe/77a9e/receptive-field-1d-conv-visualization.png)
- Recursive
	- $$r_{0} = \Sigma^{L}_{i=1}((k_{i}-1)\Pi_{j=1}^{l-1}s_{j})+1$$
- How to increase receptive field
	- Add more [Conv](Conv.md)
	- Add [Pooling](Pooling.md) or higher stride
	- [Causal Dilated Conv](Causal%20Dilated%20Conv.md)
	- [Depthwise Separable](Depthwise%20Separable.md)



