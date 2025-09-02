---
tags: ['temp']
date modified: Monday, October 10th 2022, 2:02:21 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# NCE
- [Conditional Negative Sampling for Contrastive Learning of Visual Representations](https://arxiv.org/abs/2010.02037)
- [[Contrastive Learning]]
- noise-contrastive estimation
- bound on mutual information between two views of an image
- randomly sampled negative examples to normalize the objective
- choosing difficult negatives, or those more similar to the current instance, can yield stronger representation
- Conditional Noise Contrastive Estimator
- sample negatives conditionally
- in a "ring" around each positive, by approximating the partition function using samples from a class of conditional [[Distributions.md|Distributions]]
- hese estimators lower-bound mutual information
- higher bias but lower variance than NCE [[Bias Vs Variance]]
- Applying these estimators as objectives in contrastive representation learning
- transferring [[Features.md]] to a variety of new image [[Distributions.md|Distributions]] from the meta-dataset collection
- [[Contrastive Loss.md]]

