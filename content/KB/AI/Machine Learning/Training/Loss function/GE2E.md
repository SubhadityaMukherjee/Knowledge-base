---
toc: true
title: GE2E

tags: ['loss']
date modified: Monday, October 10th 2022, 2:02:27 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# GE2E
- [Generalized End-to-end Loss for Speaker Verification](https://arxiv.org/abs/1710.10467)
- new loss function
- training of [Speaker Verification](Speaker%20Verification.md) models more efficient
- Unlike TE2E, the GE2E loss function updates the network in a way that emphasizes examples that are difficult to verify at each step of the training process
- pushes the [Embedding](Embedding.md) towards the [centroid] of the true speaker, and away from the [centroid](centroid] of the true speaker, and away from the [centroid.md) of the most similar different speaker
- does not require an initial stage of example selection
- [MultiReader technique](MultiReader%20technique.md)



