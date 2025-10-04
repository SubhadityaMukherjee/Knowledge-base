---
toc: true
title: Cosine Similarity
tags: ['loss']
date modified: Wednesday, December 7th 2022, 10:55:21 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Cosine Similarity
- [Lp Regularization](Lp%20Regularization.md) l2norm aka p = 2
- $$S_{c}(A,B) := cos(\theta) = \frac{A\cdot B}{||A|| ||B||} = \frac{\Sigma_{i=1}^{n}A_{i}B_{i}}{\sqrt{\Sigma_{i=1}^{n}A^{2}_{i}} \sqrt{\Sigma_{i=1}^{n}B_{i}^{2}}}$$
- ranges from -1 : exactly opposite, 1 : exactly same, 0: orthogonal/not correlated, intermediate
- [Cosine Distance](Cosine Distance.md)
- Cosine similarity is $$ - \mathrm{sum}\left( \mathrm{l2norm}\left( y \right) \cdot \mathrm{l2norm}\left( ŷ \right) \right)$$
- ![](../images/Pasted%20image%2020220506155815.png)
- magnitude of vectors is not taken into account, merely their direction
- In practice, this means that the differences in values are not fully taken into account
- If you take a [Recommender System](Recommender%20System.md), for example, then the cosine similarity does not take into account the difference in rating scale between different users
- high-dimensional data and when the magnitude of the vectors is not of importance



