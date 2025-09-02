---
toc: true
title: Transformer
tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:15 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Transformer
- Encoder Decoder
- Auto regressive : decoder outputs fed back as inputs to decoder
- Decoder can access not only the hidden step of the last time step from the encoder, but all the hidden states from the encoder
- During decoding, consider pairwise relationshop between decoder state and all the returned states from the encoder
	- Some words relevant, others are not
- Transform all hidden states from the encoder into context vectors, that shows how the decoding step is relevant to the input sequences
- [Attention](Attention.md)
- [Basic Transformer](Basic%20Transformer.md)

## Nice Little Blogs
- [lillog](https://lilianweng.github.io/posts/2018-06-24-attention/)



