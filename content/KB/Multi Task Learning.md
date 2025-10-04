---
toc: true
title: Multi Task Learning

tags: ['multitask']
date modified: Tuesday 7th February 2023, Tue
date created: Tuesday 7th February 2023, Tue
---

# Multi Task Learning


- multiple outputs (as desired), and typically a shared trunk of weights can indirectly encode common or shared knowledge
- Can linearly combine loss for each task $L_{i}$
- $$L(x,y, \theta) = \Sigma_{i}w_{i}L_{i}(f_{i}(x), y, \theta_{i})$$
	- $f_{i}(x)$ is output head with weights $\theta_{i}$
- The exact scale of the weights does not matter as multiplying the loss by a positive scalar does not change the optimum.
- [Hard Parameter Sharing](Hard Parameter Sharing.md)
- [Soft Parameter Sharing](Soft Parameter Sharing.md)
- [augment](augment.md) 
- [Attribute Selection](Attribute Selection.md)
- [Eavesdropping](Eavesdropping.md)
- [Representation Bias](Representation Bias.md)



