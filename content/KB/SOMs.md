---
tags: ['temp']
toc: true
title: Self Organizing Maps
date modified: Monday, October 10th 2022, 2:02:17 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Self Organizing Maps
- Kohonen maps
- Crumbled up grid of SOM neurons
- #neuromorphic
- Essentially : need to map a high dim space to a grid of neurons while trying to preserve the neighborhood relations from the high dim space. This is technically impossible so compromise.
- First initialized with small random values
- For each new pattern, identify [Best Maching Unit](Best%20Maching%20Unit.md) based on current vectors. Reduce the value of r. And pull the point to the part of the grid with similar weight vectors.
	- Update weights $$w(v_{kl}) \leftarrow w(v_{kl}) + \lambda f_r(d(v_{kl}, v_{BMU}))(x-w(v_{kl}))$$
	- $\lambda$ is learning rate
	- d is [Euclidean Distance](Euclidean%20Distance.md) between two neurons in grid.
	- $f_{r}(0)=1$. Tends to 0 as argument grows. r is radius. Greater values, will spread it out.
	- Regulated by $f_r(d(v_{kl}, v_{BMU}))$
- Eventually this will lead to an organization. Covered evenly after a while. Eventually neighbors of $v_0$ would have weights towards $w(v_0)$ . And $w(v_{0)} \approx mean(all patterns x)$
- Repeat until response stops. Each members BMU rate is too low to expand.
- Start with large r and then slow down.



