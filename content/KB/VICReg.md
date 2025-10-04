---
toc: true
title: VICReg

tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:14 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---
- [VICReg: Variance-Invariance-Covariance Regularization for Self-Supervised Learning](https://arxiv.org/abs/2105.04906)
- [Self Supervised](Self%20Supervised.md)
- based on maximizing the agreement between [Embedding](Embedding.md) vectors from different views of the same image
- rivial solution is obtained when the encoder outputs constant vectors
- [Mode Collapse](Mode%20Collapse.md) is often avoided through implicit biases
- explicitly avoids the collapse problem with a simple [Regularization](Regularization.md) term on the variance of the embeddings along each dimension individually
- triple objective: learning invariance to different views with a invariance term, avoiding collapse of the representations with a variance preservation term, and maximizing the information content of the representation with a [Covariance](Covariance.md) [Regularization](Regularization.md) term
- [Bias Vs Variance](Bias%20Vs%20Variance)
- combines the variance term with a decorrelation mechanism based on redundancy reduction and [Covariance](Covariance.md) [Regularization](Regularization.md)
- does not require the [Embedding](Embedding.md) branches to be identical or even similar



