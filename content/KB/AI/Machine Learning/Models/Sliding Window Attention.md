---
toc: true
title: Sliding Window Attention

tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:16 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Sliding Window [Attention](Attention.md)
- Given the importance of local context, the sliding window [Attention](Attention.md) pattern employs a fixed-size window [Attention](Attention.md) surrounding each token
    - multiple stacked [Layers](Layers.md) of such windowed [Attention](Attention.md) results in a large [Receptive field](Receptive%20field.md), where top [Layers](Layers.md) have access to all input locations and have the capacity to build representations that incorporate information across the entire input
    - But a model with typical multiple stacked transformers will have a large [Receptive field](Receptive%20field.md). This is analogous to CNNs where stacking [Layers](Layers.md) of small kernels leads to high level [Features](Features.md) that are built from a large portion of the input ([Receptive field](Receptive%20field.md))
    - Depending on the application, it might be helpful to use different values of $w$ for each layer to balance between efficiency and model representation capacity.
- Given a fixed window size $w$, each token attends to $\frac{1}{2}w$ tokens on each size
- Complexity is $O(n \times w)$
	- $w$ should be small compared to $n$
- With $l$ layers, [Receptive field](Receptive%20field.md) size is $l \times w$
- ![](../images/Pasted%20image%2020220621181138.png)



