---
toc: true
title: Trajectory Plotting with PCA

tags: ['explainability']
date modified: Monday 27th March 2023, Mon
date created: Monday 27th March 2023, Mon
---

# Trajectory Plotting with PCA


- The problem: the path lies in a low-dimensional space.
- The solution: [PCA](PCA.md)
- Construct a matrix $$
M = [\theta_{0}- \theta_{n};...;\theta_{n-1}-\theta_{n}]
$$
- where,
- $\theta_{i}$ is the model params during epoch i
- n is number of epochs
- apply PCA to M and use 2 most explanatory directions
- ![](../images/Pasted%20image%2020230327130326.png)



