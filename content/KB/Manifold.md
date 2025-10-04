---
tags: ['explainability']
toc: true
title: Manifold
date modified: Tuesday, November 15th 2022, 12:47:32 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Manifold
- Data manifolds are an abstraction
- Only geometric insights are important
- Locally around some point c where the [PDF](PDF.md) is large -> It will stay large only for a small fraction of directions
	- Those directions span a low dimensional hyperplane around c
	- "low dimensional sheets"
	- curved path
- In an n dimensional real vector space $\mathbb{R}^{n}$ . [Embedding](Embedding.md) space
	- $m \leq n$ is a positive integer
	- An m dim manifold $\mathcal{M}$ is a subset of the vector space where one can smoothly map a neighborhood of that point to a neighborhood of the origin in m dim Euclidean space
		- Locally represents Euclidean space
- Only surface and not interior
- No sharp edges or spikes
- Can be exploited by [Adversarial Learning](Adversarial%20Learning.md)
- Examples
	- 1 dim -> Lines in some high dim figure : B
	- 2 dim -> Surfaces : A
	- ![](../images/Pasted%20image%2020220316181643.png)
	- ![](../images/Pasted%20image%2020220316181947.png)
	- ![](../images/Pasted%20image%2020220316182354.png)
	- ![](../images/Pasted%20image%2020220316182449.png)

## Refs
- [tds](https://towardsdatascience.com/manifolds-in-data-science-a-brief-overview-2e9dde9437e5)
- [way more stuff : bjlkeng](https://bjlkeng.github.io/posts/manifolds/) #todo



