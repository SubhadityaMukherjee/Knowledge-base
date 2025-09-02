---
toc: true
title: DLRM

tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:30 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# DLRM
- [Deep Learning Recommendation Model for Personalization and Recommendation Systems](https://arxiv.org/abs/1906.00091)
- DLRM
- The DLRM model handles continuous (dense) and categorical (sparse) [Features](Features.md) that describe users and products
- wide range of hardware and system components, such as memory capacity and bandwidth, as well as communication and compute resources
- design a specialized [Parallelization](Parallelization.md) scheme utilizing model parallelism on the [Embedding](Embedding.md) tables to mitigate memory constraints while exploiting data parallelism to scale-out compute from the fully-connected [Layers](Layers.md)
- it computes the feature interactions explicitly while limiting the order of interaction to pairwise interactions.
- treats each embedded feature vector (corresponding to categorical [Features](Features.md)) as a single unit, whereas other methods (such as Deep and Cross) treat each element in the feature vector as a new unit that should yield different cross terms
- These design choices help reduce computational/memory cost while maintaining competitive accuracy



