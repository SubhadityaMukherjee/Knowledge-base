---
toc: true
title: Longformer

tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:23 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Longformer
- [Longformer: the Long-Document Transformer](https://arxiv.org/abs/2004.05150)
- [Transformer](Transformer.md)
- [Sliding Window Attention](Sliding%20Window%20Attention.md)
- [Dilated Sliding Window Attention](Dilated%20Sliding%20Window%20Attention.md)
- [Global and Sliding Window Attention](Global%20and%20Sliding%20Window%20Attention.md)
- [Attention](Attention.md) mechanism that scales linearly with sequence length
- drop-in replacement for the standard self-[Attention](Attention.md)
- local windowed [Attention](Attention.md) with a task motivated global [Attention](Attention.md)
- text8
- enwik8
- consistently outperforms [RoBERTa](RoBERTa.md) on long document tasks and sets new state-of-the-art results on WikiHop and TriviaQA
- Longformer-Encoder-Decoder (LED), a Longformer variant for supporting long document generative sequence-to-sequence tasks, and demonstrate its effectiveness on the arXiv summarization dataset



