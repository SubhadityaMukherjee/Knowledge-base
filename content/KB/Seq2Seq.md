---
toc: true
title: Seq2Seq
tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:17 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Seq2Seq
- [Basic RNN Architectures](Basic%20RNN%20Architectures.md)
- Long term dependency [Issues](Issues.md)
- Even if hidden state vector has a high dimensionality, cannot hold all info
- [Sequence to Sequence Learning with Neural Networks](https://proceedings.neurips.cc/paper/2014/file/a14ac55a4f27472c5d894ec1c3c743d2-Paper.pdf)
- encoder-decoder learning to map sequences to sequences
- multilayered Long Short-Term Memory [LSTM)](Long Short Term Memory (LSTM|Long Short Term Memory (LSTM|[LSTM)](LSTM)](LSTM)](Long Short Term Memory (LSTM|Long Short Term Memory (LSTM|[LSTM)](LSTM).md).md)
- large deep LSTM with a limited vocabulary can outperform a standard statistical machine translation (SMT)-based system whose vocabulary is unlimited on a large-scale MT task
- [WMT14](WMT14.md)
- [BLEU](BLEU.md) score
- reversing the order of the words in all source sentences (but not target sentences) improved the LSTM’s performance markedly, because doing so introduced many short term dependencies between the source and the target sentence which made the optimization problem easier



