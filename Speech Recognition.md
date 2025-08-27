---
toc: true
title: Speech Recognition
tags:
  - architecture
date modified: Monday, October 10th 2022, 2:02:16 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Speech Recognition
- [Recurrent Neural Network Based Language Model](https://www.fit.vutbr.cz/research/groups/speech/publi/2010/mikolov_interspeech2010_IS100722.pdf)
	- 50% reduction of [Perplexity](./Perplexity.md#)
	- mixture of several [Basic RNN Architectures](./Basic%2520RNN%2520Architectures.md#)
	- [Wall Street Journal task](./Wall%2520Street%2520Journal%2520task.md#)
	- connectionist language models are superior to standard [n gram](n%20gram) techniques, except their high computational (training) complexity
	- break the myth that language modeling is just about counting n-grams, and that the only reasonable way how to improve results is by acquiring new training dat
- [Towards End-To-End Speech Recognition with Recurrent Neural Networks](http://proceedings.mlr.press/v32/graves14.pdf)
	- character-level speech recognition system that directly transcribes audio data with text using a recurrent neural network
	- combination of the deep bidirectional LSTM recurrent neural network architecture and a modified Connectionist Temporal Classification ([CTC](./CTC.md#)) objective function
	- word error rate
	- [Wall Street Journal task](./Wall%2520Street%2520Journal%2520task.md#)



