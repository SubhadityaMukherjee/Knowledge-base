---
toc: true
title: Wide Deep Recommender

tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:13 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Wide Deep Recommender
- [Wide & Deep Learning for Recommender Systems](https://arxiv.org/abs/1606.07792)
- Generalized linear models with nonlinear feature transformations are widely used for large-scale regression and classification problems with sparse inputs.
- Memorization of feature interactions through a wide set of cross-product feature transformations are effective and interpretable, while generalization requires more feature engineering effort
- However, memorization and generalization are both important for recommender systems.
- With less feature engineering, deep neural networks can generalize better to unseen feature combinations through low-dimensional dense embeddings learned for the sparse [Features](Features.md)
- However, deep neural networks with embeddings can over-generalize and recommend less relevant items when the user-item interactions are sparse and high-rank.
- jointly trained wide linear models and deep neural networks – to combine the benefits of memorization and generalization for recommender systems
- Wide linear models can effectively memorize sparse feature interactions using cross-product feature transformations, while deep neural networks can generalize to previously unseen feature interactions through low dimensional embeddings
- In other words, the fusion of wide and deep models combines the strengths of memorization and generalization, and provides us with better recommendation systems
- The two models are trained jointly with the same [loss](../Tag%20Pages/loss.md) function.
- Google Play Store



