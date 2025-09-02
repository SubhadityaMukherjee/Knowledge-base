---
toc: true
title: Factorized Embedding Parameters

tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:28 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Factorized [Embedding](Embedding.md) Parameters
- Factorization of these parameters is achieved by taking the matrix representing the weights of the word embeddings $E$ and decomposing it into two different matrices. Instead of projecting the one-hot encoded vectors directly onto the hidden space, they are first projected on some-kind of lower-dimensional [Embedding](Embedding.md) space, which is then projected to the hidden space (Lan et al, 2019). Normally, this should not produce a different result, but let's wait.
- Another thing that actually ensures that this change reduces the number of parameters is that the authors suggest to reduce the size of the [Embedding](Embedding.md) matrix.
- In [BERT](BERT.md), the shape of the vocabulary/[Embedding](Embedding.md) matrix E equals that of the matrix for the hidden state H.
- First of all, theoretically, the matrix E captures context-independent information
- whereas the hidden representation H captures context-dependent information
- [ALBERT](ALBERT.md) solves this issue by decomposing the [Embedding](Embedding.md) parameters into two smaller matrices, allowing a two-step mapping between the original [Word Vectors](Word%20Vectors.md) and the space of the hidden state. In terms of computational cost, this no longer means $\text{O(VxH)}$ but rather $\text{O(VxE + ExH)}$, which brings a significant reduction when $\text{H >> E}$.



