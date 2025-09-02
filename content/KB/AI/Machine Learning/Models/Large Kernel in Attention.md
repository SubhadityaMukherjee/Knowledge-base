---
toc: true
title: Large Kernel in Attention

tags: ['architecture']
date modified: Sunday, October 23rd 2022, 5:00:07 pm
date created: Sunday, October 23rd 2022, 5:00:06 pm
---

# Large Kernel in Attention


- self-attention can be viewed as a global depth-wise kernel that enables each layer to have a global receptive field.
- Swin Transformer (Liu et al., 2021e) is a ViTs variant that adopts local attention with a shifted window manner
- greatly improve the memory and computation efficiency with appealing performance
- Since the size of attention windows is at least 7, it can be seen as an alternative class of large kernel
- recent work (Guo et al., 2022b) proposes a novel large kernel attention module that
- uses stacked depthwise, small convolution, dilated convolution as well as pointwise convolution to capture both local and global structure



