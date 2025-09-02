---
toc: true
title: Rejection Sampling
tags: ['distributions']
date modified: Monday, October 10th 2022, 2:02:18 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Rejection [[Sampling]]
- Also called Best-of-n [[sampling]]
- No [[CDF.md]] with a simple inverse
- Importance [[sampling]]
- Use a simpler distribution which is somewhat related to the target [[PDF.md]]
	- Sample by transformation
- Now if we can take a [[Proto PDF.md]] $g_{0} \geq f$ where we can sample from the [[PDF.md]] g
- Take a point from g with [[Probability.md]] $f(\tilde x)/g_{0}(\tilde x)$
	- Either accept or reject if satisfies [[Probability.md]]
	- If accepted then return the sample
- Drop a point from $g_{0}(x)$ with that [[Probability.md]]
- Depends on how close g is to f of course
- ![[../images/Pasted image 20220324114746.png]]
	- If the ratio $\frac{f}{g_{0}}$ is small. (aka f is bigger), then there are many rejections and the algo will be slow. Impossible to not do in high dim spaces



