---
toc: true
title: Generative Spoken Language Modeling

tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:26 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Generative Spoken Language Modeling
- [Generative Spoken Language Modeling from Raw Audio](https://arxiv.org/abs/2102.01192)
- learns speech representations from CPC, Wav2Vec2.0, and HuBERT for synthesizing speech
- task of learning the acoustic and linguistic characteristics of a language from raw audio
- et of metrics to automatically evaluate the learned representations at acoustic and linguistic levels for both encoding and generation
- set up baseline systems consisting of a discrete speech encoder (returning pseudo-text units)
- generative language model (trained on pseudo-text)
- speech decoder (generating a waveform from pseudo-text)
- trained without supervision
- number of discrete units (50, 100, or 200) matters in a task-dependent and encoder-dependent way, and that some combinations approach text-based systems



