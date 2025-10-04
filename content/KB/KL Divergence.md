---
toc: true
title: KL Divergence
tags: ['loss']
date modified: Monday, October 10th 2022, 2:02:24 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# KL Divergence
- Classification
- [Entropy](Entropy.md) + [Cross Entropy](Cross%20Entropy.md)
- Distribution Based metric
- Measures difference between two [PDF](PDF.md)
- We first define xlogx for a weird edge case $$x \cdot \log\left( x \right)$$

Then [Entropy](Entropy.md) $$\mathrm{sum}\left( \mathrm{xlogx}\left( y \right) \right) \cdot \mathrm{//}\left( 1, \mathrm{size}\left( y, 2 \right) \right)$$

Then cce as defined before $$ - \mathrm{sum}\left( y \cdot \log\left( ŷ \right) \right)$$

Finally KLD $$entropy + crossentropyloss$$

 - $$KL(p,q) = \Sigma_x p(x) log\frac{p(x)}{q(x)}$$



