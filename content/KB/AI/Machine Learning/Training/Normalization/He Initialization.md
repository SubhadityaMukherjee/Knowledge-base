---
toc: true
title: He Initialization

tags: ['regularization']
date modified: Monday, October 10th 2022, 2:02:26 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# He Initialization
- bring the variance of those outputs to approximately one
- However, Kumar indeed proves mathematically that for the [Relu](Relu.md) activation function, the best weight [Initialization](Initialization.md) strategy is to initialize the weights randomly but with this variance:
	- $$\begin{equation} v^{2} = 2/N \end{equation}$$
- For [Sigmoid](Sigmoid.md) based activation functions



