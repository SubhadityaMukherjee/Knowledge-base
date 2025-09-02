---
toc: true
title: SGD

tags: ['gradients']
date modified: Monday, October 10th 2022, 2:02:18 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# SGD
- instead of taking the whole dataset for each iteration, we randomly select the batches of data
- The procedure is first to select the initial parameters w and learning rate n. Then randomly shuffle the data at each iteration to reach an approximate minimum.
- full of noise
- Due to an increase in the number of iterations, the overall computation time increases.
- $$\theta = \theta - \eta \cdot \nabla_{\theta} J(\theta ; x^{i}; y^{i} )$$
	- For each example $x^{i}$ and label $y^{i}$
## Implicit Regularization
- ![](../images/Pasted%20image%2020240918105821.png)