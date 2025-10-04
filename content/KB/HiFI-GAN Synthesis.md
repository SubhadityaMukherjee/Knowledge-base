---
toc: true
title: HiFI-GAN Synthesis

tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:26 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# HiFI-GAN Synthesis
- [HiFi-GAN: Generative Adversarial Networks for Efficient and High Fidelity Speech Synthesis](https://arxiv.org/abs/2010.05646)
- synthesis
- As speech audio consists of sinusoidal signals with various periods, they demonstrate that modeling periodic patterns of an audio is crucial for enhancing sample quality
- shows a significant improvement in terms of synthesis speed.
- MOS
- characteristic of speech audio that consists of patterns with various periods and applied it to neural networks, and verified that the existence of the proposed discriminator greatly influences the quality of speech synthesis through the ablation study
- generalize to the mel-[Spectrogram](Spectrogram.md) inversion of unseen speakers and synthesize speech audio comparable to human quality from noisy inputs in an end-to-end setting
- progress towards on-device natural speech synthesis, which requires low latency and memory footprint
- generators of various configurations can be trained with the same discriminators and learning mechanism
- possibility of flexibly selecting a generator configuration according to the target specifications without the need for a time-consuming hyper-parameter search for the discriminators



