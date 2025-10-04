---
toc: true
title: Pre Integrated Volume Rendering

tags: ['visualization']
date modified: Monday, October 10th 2022, 2:02:19 pm
date created: Thursday, July 28th 2022, 5:59:06 pm
---

# Pre Integrated Volume Rendering
- Assume
	- Linear interpolations of scalar values in a ray segment
	- Constant length of ray segment L
- Pre computation from a slab
- $$s_{L}(t) = s_{b}+ \frac{t}{L}(s_{f}-s_{b})$$
- becomes
- $$c_{i}= \int_{0}^{L}g(t)e^{-\int_{t}^{L}{\kappa(t')d_{t}}}dt' $$
- $$o_{i}= e^{\int_{0}^{L}\kappa(t)}d_{t} $$
- ![](../images/Screenshot%202022-09-14%20at%2012.18.54%20PM.png)



