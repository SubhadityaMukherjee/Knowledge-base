---
toc: true
title: Collaborative Topic Regression

tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:31 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Collaborative Topic Regression
- [Collaborative Deep Learning for Recommender Systems](https://arxiv.org/abs/1409.2944)
- Collaborative [Filtering](Filtering.md) (CF) is a successful approach commonly used by many recommender systems
- Conventional CF-based methods use the ratings given to items by users as the sole source of information for learning to make recommendation
- However, the ratings are often very sparse in many applications, causing CF-based methods to degrade significantly in their recommendation performance
- To address this [Sparsity](Sparsity.md) problem, auxiliary information such as item content information may be utilized
- Collaborative topic regression (CTR) is an appealing recent method taking this approach which tightly couples the two components that learn from two different sources of information
- Nevertheless, the latent representation learned by CTR may not be very effective when the auxiliary information is very sparse.
- generalizing recent advances in deep learning from i.i.d input to non-i.i.d (CF-based) input and propose a hierarchical [Bayesian](Bayesian.md) model called collaborative deep learning (CDL), which jointly performs deep representation learning for the content information and collaborative [Filtering](Filtering.md) for the ratings (feedback) matrix.



