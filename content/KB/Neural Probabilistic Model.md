---
toc: true
title: Neural Probabilistic Model

tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:21 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Neural Probabilistic Model
- [A Neural Probabilistic Language Model](https://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf)
- more compact and smoother representations based on distributed representations that can accommodate far more conditioning variables
- learning the joint [Probability](Probability.md) function of sequences of words in a language was intrinsically difficult because of the [Curse Of Dimensionality](Curse%20Of%20Dimensionality.md)
- learning a distributed representation for words which allows each training sentence to inform the model about an exponential/combinatorial number of semantically neighboring sentences
- The model learns simultaneously (i) a distributed representation for each word along with (ii) the [Probability](Probability.md) function for word sequences, expressed in terms of these representations
- Generalization is obtained because a sequence of words that has never been seen before gets high [Probability](Probability.md) if it is made of words that are similar
- significantly improves on state-of-the-art [n gram](n%20gram) models



