---
toc: true
title: Diffusion LM

tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:29 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Diffusion LM
- [Diffusion-LM Improves Controllable Text Generation](https://arxiv.org/abs/2205.14217)
- Controlling the behavior of language models (LMs) without re-training is a major open problem in natural language generation
- non-[Autoregressive](Autoregressive.md) language model based on continuous diffusions
- substantial departure from the current paradigm of discrete [Autoregressive](Autoregressive.md) generation
- iteratively denoises a sequence of Gaussian vectors into word vectors, yielding a sequence of intermediate latent variables
- continuous, hierarchical nature of these intermediate variables enables a simple gradient-based algorithm to perform complex, controllable generation tasks
- successful control of Diffusion-LM for six challenging fine-grained control tasks



