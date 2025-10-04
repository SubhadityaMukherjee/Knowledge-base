---
toc: true
title: SpecAugment

tags: ['augmentation']
date modified: Monday, October 10th 2022, 2:02:16 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# SpecAugment
- [SpecAugment: a Simple Data Augmentation Method for Automatic Speech Recognition](https://arxiv.org/abs/1904.08779)
- simple data [augmentation](Augmentation.md) method for [speech recognition](speech recognition.md)
- applied directly to the feature inputs of a neural network
- warping the [Features](Features.md), masking blocks of frequency channels, and masking blocks of time steps
- apply SpecAugment on Listen, Attend and Spell (LAS) networks for end-to-end [speech recognition](speech recognition.md) tasks
- [LibriSpeech](LibriSpeech.md)
- [Swichboard](Swichboard.md)
- end-to-end LAS networks by augmenting the training set using simple handcrafted policies
- converts ASR from an over-[Fitting](Fitting.md) to an under-[Fitting](Fitting.md) problem, and they are able to gain performance by using bigger networks and training longer



