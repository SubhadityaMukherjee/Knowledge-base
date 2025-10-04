---
toc: true
title: S2ST

tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:18 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# S2ST
- [Direct Speech-to-speech Translation with Discrete Units](https://arxiv.org/abs/2107.05604)
- direct speech-to-speech translation (S2ST) model that translates speech from one language to speech in another language without relying on intermediate text generation
- self-supervised discrete speech encoder on the target speech
- training a sequence-to-sequence speech-to-unit translation
- model to predict the discrete representations of the target speech
- When target text transcripts are available, they design a joint speech and text training framework that enables the model to generate dual [Modality](Modality.md) output (speech and text) simultaneously in the same inference pass
- [Fisher Spanish-English](Fisher%20Spanish-English.md)



