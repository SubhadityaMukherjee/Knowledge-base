---
toc: true
title: Uniform Sampling
tags: ['distributions']
date modified: Monday, October 10th 2022, 2:02:14 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Uniform [[Sampling]]
- Random [[Sampler.md]]
- [[Uniform Distribution.md]]
- If need to sample from another distribution with a [[PDF.md]] f(x). Can use a uniform [[Sampler.md]] on the distribution [0,1] to indirectly sample from it
	- Coordinate transform
	- [[CDF.md]]
	- Get a [[Sampler.md]] for by $$X_{i} = \varphi^{-1}\circ U_{i}$$
	- ![[../images/Pasted image 20220324113838.png]]



