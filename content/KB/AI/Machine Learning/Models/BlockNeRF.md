---
toc: true
title: BlockNeRF

tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:32 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# BlockNeRF
- [Block-NeRF: Scalable Large Scene Neural View Synthesis](https://arxiv.org/abs/2202.05263)
- variant of [[Neural Radiance Field]]
- reconstruct large-scale environments
- scaling NeRF to render city-scale scenes spanning multiple blocks, it is vital to decompose the scene into individually trained NeRFs that can be optimized independently.
- this decomposition decouples rendering time from scene size
- allows per-block updates of the environment
- data collected will necessarily have transient objects and variations in appearance
- modifying the underlying NeRF architecture to make NeRF robust to data captured over months under different environmental conditions
- appearance [[Embedding]], learned pose refinement, and controllable exposure to each individual NeRF
- procedure for aligning appearance between adjacent NeRFs so that they can be seamlessly combined
- building an entire neighborhood in San Francisco from 2.8M images using a grid of Block-NeRFs, forming the largest neural scene representation to date



