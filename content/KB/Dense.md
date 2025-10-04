---
tags: ['temp']
toc: true
title: Dense
tag: architecture
date modified: Monday, October 10th 2022, 2:02:30 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Dense
- Weighted [LinearRegression](LinearRegression.md)
- Forward
	- $$z = W\cdot x + b$$ , $$y=g(z)$$
- Backward
	- $$\delta = g'(z)\circ \nabla_y E$$
	- $$\nabla_WE = \delta \cdot x^T$$ , $$\nabla_bE = \delta$$
	- $$\nabla_xE = W^T\cdot \delta$$



