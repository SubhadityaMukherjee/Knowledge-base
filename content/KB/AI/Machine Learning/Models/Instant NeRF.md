---
toc: true
title: Instant NeRF

tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:25 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Instant NeRF
- [Instant Neural Graphics Primitives with a Multiresolution Hash Encoding](https://arxiv.org/abs/2201.05989)
- [Neural Radiance Field](Neural%20Radiance%20Field.md)
- Neural graphics primitives, parameterized by fully connected neural networks, can be costly to train and evaluate
- rely on task specific [Data Structures](Data%20Structures.md)
- new input encoding that permits the use of a smaller network without sacrificing quality
- educing the number of floating point and memory access operations
- near-instant training of neural graphics primitives on a single GPU for multiple tasks
- small neural network is augmented by a multiresolution hash table of trainable feature vectors whose values are optimized through [Gradient Descent](Gradient%20Descent.md)
- automatically focuses on relevant detail, independent of task at hand
- low overhead
- In a gigapixel image, they represent an image by a neural network. SDF learns a signed distance function in 3D space whose zero level-set represents a 2D surface
- 2D images and their camera poses to reconstruct a volumetric radiance-and-[Density](Density.md) field that is visualized using ray marching.
- neural volume learns a denoised radiance and [Density](Density.md) field directly from a volumetric path tracer.
- only vary the hash table size which trades off quality and performance
- disambiguate hash collisions, making for a simple architecture that is trivial to parallelize on modern GPUs
- parallelism
- fully-fused [Operator Fusion](Operator%20Fusion.md) CUDA kernels with a focus on minimizing wasted bandwidth and compute operations



