---
toc: true
title: Fixed Factorization Attention

tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:27 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Fixed Factorization [Attention](Attention.md)
- [paper](https://arxiv.org/abs/1904.10509v1)
- Specific cells summarize previous locations and propagate to all future cells.
- Part of [Sparse Transformer](Sparse%20Transformer.md)
- Fixed [Attention](Attention.md) pattern with c = 1 limits expressivity
- many representations in the network are only used for one block whereas a small number of locations are used by all blocks.
- Choosing $c \in [Strided Attention](Strided%20Attention.md)
- when using multiple heads, having them attend to distinct subblocks of length $c$ within the block of size $l$ was preferable to having them attend to the same subblock
- ![](../images/Pasted%20image%2020220621181149.png)



