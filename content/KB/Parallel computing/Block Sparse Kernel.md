---
toc: true
title: Block Sparse Kernel
tags: ['parallelcomputing']
date modified: Monday, October 10th 2022, 2:02:32 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Block Sparse Kernel
- For networks with block sparse weights
- Can choose amount of [[Sparsity]]
- Can replace normal [[Dense]] [[Layers]] with sparse and wide or sparse and deep
- ![[Pasted image 20220425233755.webp]]
- Enables wider and deeper networks
- Only compute on non zero blocks
- ![[Pasted image 20220425233903.webp]]
- Connectivity is unaffected in the spatial dimensions
- Compute cost is only prop to number of non zero weights
- [[Small World graphs]]
- Also useful for compression

## Refs
- [openai](https://openai.com/blog/block-sparse-gpu-kernels/)



