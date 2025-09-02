---
toc: true
title: wave2vec

tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:09 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# wave2vec
- [wav2vec: Unsupervised Pre-training for Speech Recognition](https://arxiv.org/abs/1904.05862)
- Reducing the need for manually annotated data is important for developing systems that understand non-English languages, particularly those with limited existing training sets of transcribed speech
- first application of unsupervised pre-training to [speech recognition](speech recognition.md) using a fully convolutional model that learns representations of raw, unlabeled audio
- trained on large amounts of unlabeled audio data and the resulting representations are then used to improve acoustic model training
- pre-train a simple multi-layer convolutional neural network optimized via a noise contrastive binary classification task
- learn the difference between original speech examples and modified versions, often repeating this task hundreds of times for each second of audio, and predicting the correct audio milliseconds into the future
- beats traditional ASR systems that rely solely on transcribed audio
- experiments on WSJ reduce WER of a strong character-based log-mel filterbank baseline
- more data for pre-training improves performance and that this approach not only improves resource-poor setups, but also settings where all WSJ training data is used



