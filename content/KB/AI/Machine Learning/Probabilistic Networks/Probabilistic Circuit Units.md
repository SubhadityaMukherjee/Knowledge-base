---
title: Probabilistic Circuit Units
toc: true
tags: 
date modified: Thursday 20th February 2025, Thu
date created: Thursday 20th February 2025, Thu
---

# Probabilistic Circuit Units
```toc
```

diff computational graph

- encode a fn over X
## Units in Computational Graph
### Types
- input unit (any fn) : distribution
- product unit : factorization
- sum unit : mixture
- integral unit
	- continuous heirarchial mixture models
	- stack K gaussian components
	- output is a function after solving an analytical integration
- can be stacked 
- outputs a number
- evaluated bottom up - joint probability
- non linearities at input and product
- probabilistic
	- when it encodes a non negative fn 
	- input units encode distributions (like [[Normal Distribution]]), sum weights are positive
- for tractability
	- sum/products must be smooth/decomposable
	- can compute marginal probability (exact)