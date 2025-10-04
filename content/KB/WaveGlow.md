---
toc: true
title: WaveGlow

tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:13 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# WaveGlow
- [WaveGlow: a Flow-based Generative Network for Speech Synthesis](https://arxiv.org/abs/1811.00002)
- flow-based network capable of generating high quality speech from mel-spectrograms
- combines insights from [GLOW](GLOW.md) and WaveNet in order to provide fast, efficient and high-quality audio synthesis, without the need for auto-regression
- mplemented using only a single network, trained using only a single cost function: maximizing the likelihood of the training data, which makes the training procedure simple and stable
- more than 500 kHz on an NVIDIA V100 GPU
- Mean Opinion Scores



