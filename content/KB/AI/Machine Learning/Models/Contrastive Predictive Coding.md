---
toc: true
title: Contrastive Predictive Coding

tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:31 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Contrastive Predictive Coding
- [Representation Learning with Contrastive Predictive Coding](https://arxiv.org/abs/1807.03748)
- Contrastive Predictive Coding
- framework for extracting compact latent representations to encode predictions over future observations
- learn such representations by predicting the future in latent space by using powerful [Autoregressive](Autoregressive.md) models
- probabilistic [Contrastive Loss](Contrastive%20Loss.md) based on NCE, which both the encoder and [Autoregressive](Autoregressive.md) model are trained to jointly optimize, which they call InfoNCE
- InfoNCE induces the latent space to capture information that is maximally useful to predict future samples
- combines [Autoregressive](Autoregressive.md) modeling and noise-contrastive estimation with intuitions from predictive coding to learn abstract representations in an unsupervised fashion
- negative sampling



