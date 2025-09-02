---
toc: true
title: ELECTRA

tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:29 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# ELECTRA
- [ELECTRA: Pre-training Text Encoders As Discriminators Rather Than Generators](https://arxiv.org/abs/2003.10555)
- Pre-training methods such as BERT corrupt the input by replacing some tokens with [MASK] and then train a model to reconstruct the original tokens.
- sample-efficient pre-training alternative task called replaced token detection
- self-supervised task for language representation learning
- Instead of masking the input, their approach corrupts it by replacing some tokens with plausible alternatives sampled from a small generator network
- Then, instead of training a model that predicts the original identities of the corrupted tokens, the key idea is training a discriminative text encoder model to distinguish input tokens from high-quality negative samples produced by an small generator network
- more compute-efficient and results in better performance on downstream tasks
- particularly strong for small models
- [GLUE](GLUE.md)
- performs comparably to [RoBERTa](RoBERTa.md) and [XLNet](XLNet.md) while using less than 1/4 of their compute and outperforms them when using the same amount of compute.



