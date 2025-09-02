---
toc: true
title: Perplexity

tags: ['loss']
date modified: Monday, October 10th 2022, 2:02:20 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Perplexity
- Perplexity is defined as the exponentiated average negative log-likelihood of a sequence.
- If we have a tokenized sequence $X = (x_0, x_1, \dots, x_t)$, then the perplexity of $X$ is, $$\text{PPL}(X) = \exp \left\{ {-\frac{1}{t}\sum_i^t \log p_\theta (x_i|x_{<i}) } \right\}$$where $\log p_\theta (x_i|x_{<i})$ is the log-likelihood of the ith token conditioned on the preceding tokens $x_{<i}$ according to our model.
- Intuitively, it can be thought of as an evaluation of the model's ability to predict uniformly among the set of specified tokens in a corpus.
- Importantly, this means that the tokenization procedure has a direct impact on a model's perplexity which should always be taken into consideration when comparing different models.
- This is also equivalent to the exponentiation of the [Cross Entropy](Cross%20Entropy.md) between the data and model predictions



