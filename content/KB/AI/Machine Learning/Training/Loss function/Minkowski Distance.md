---
toc: true
title: Minkowski Distance

tags: ['loss']
date modified: Monday, October 10th 2022, 2:02:22 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Minkowski Distance
- ![](../images/Pasted%20image%2020220623160934.png)
- $$D(x,y) = (\Sigma_{i=1}^{n}|x_{i}-y_{i}|^{p})^{\frac{1}{p}}$$
- It is a metric used in Normed vector space (n-dimensional real space), which means that it can be used in a space where distances can be represented as a vector that has a length.
	- Zero Vector — The zero vector has a length of zero whereas every other vector has a positive length. For example, if we travel from one place to another, then that distance is always positive. However, if we travel from one place to itself, then that distance is zero.
	- Scalar Factor — When you multiple the vector with a positive number its length is changed whilst keeping its direction. For example, if we go a certain distance in one direction and add the same distance, the direction does not change.
	- Triangle Inequality — The shortest distance between two points is a straight line.
- Most interestingly about this distance measure is the use of parameter p. We can use this parameter to manipulate the distance metrics to closely resemble others.
- Common values of p are:
	- p=1 — [Manhattan Distance](Manhattan%20Distance.md)
	- p=2 — [Euclidean Distance](Euclidean%20Distance.md)
	- p=$\infty$ — [Chebyshev Distance](Chebyshev%20Distance.md)
- The upside to p is the possibility to iterate over it and find the distance measure that works best for your use case.



