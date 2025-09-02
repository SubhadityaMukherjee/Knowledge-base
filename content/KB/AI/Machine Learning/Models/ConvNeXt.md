---
tags: ['architecture']
date modified: Sunday, October 23rd 2022, 4:19:51 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# ConvNeXt
- @liuConvNet2020s2022
- modifying a standard [Res Net](Res%20Net.md) , following design choices closely inspired by [Vision Transformer](Vision%20Transformer.md)
- A vanilla ViT, on the other hand, faces difficulties when applied to general computer vision tasks such as object detection and semantic segmentation
- hierarchical Transformers (e.g., [Swin Transformer](Swin%20Transformer.md) ) that reintroduced several [Conv](Conv.md) priors, making Transformers practically viable as a generic vision backbone
- effectiveness of such hybrid approaches is still largely credited to the intrinsic superiority of Transformers, rather than the inherent inductive biases of convolutions
- extending the number of epochs, using [AdamW](AdamW.md) optimizer, Stochastic Depth, [Label Smoothing](Label%20Smoothing.md)
- number of blocks in each stage (stage compute ratio), which was adjusted from (4, 4, 6, 3) to (3, 3, 9, 3)
- The second is the stem cell configuration, which in the original ResNet consisted of 7×7 convolutions with stride 2 followed by a max-[Pooling](Pooling.md) layer. This was substituted by a more [Transformer](Transformer.md)-like “patchify” layer which utilizes 4×4 non-overlapping convolutions with stride 4
- [Depthwise Separable](Depthwise%20Separable.md) , which are interestingly similar to self-[Attention](Attention.md) as they work on a per-channel basis
- higher number of channels (from 64 to 96)
- Inverted Bottleneck: An essential configuration of Transformers is the expansion-compression rate in the MLP block (the hidden dimension is 4 times higher than the input and output dimension)
- input is expanded using 1 \times 1 convolutions and then shrunk through depthwise convolution and 1 \times 1 convolutions
- move the depthwise convolution before the convolution
- 7 \times 7 window (higher values did not bring any alterations in the results
- [GELU](GELU.md) instead of [Relu](Relu.md) , a single activation for each block (the original [Transformer](Transformer.md) module has just one activation after the MLP), fewer normalization [Layers](Layers.md), [Batch Normalization](Batch%20Normalization.md) substituted by [Layer Normalization](Layer%20Normalization.md) , and separate [Downsampling](Downsampling.md) layer
- [ImageNet](ImageNet.md)
- [COCO](COCO.md)
- [ADE20K](ADE20K.md)
- A case in point is multi-modal learning, in which a cross-[Attention](Attention.md) module may be preferable for modeling feature interactions across many modalities
- Transformers may be more flexible when used for tasks requiring discretized, sparse, or structured outputs



