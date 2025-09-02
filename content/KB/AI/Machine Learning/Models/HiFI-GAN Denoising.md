---
toc: true
title: HiFI-GAN_Denoising

tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:26 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# HiFI-GAN_Denoising
- [HiFi-GAN: High-Fidelity Denoising and Dereverberation Based on Speech Deep [Features](Features.md) in Adversarial Networks](<https://arxiv.org/abs/2006.05694)>
- Real-world audio recordings are often degraded by factors such as noise, reverberation, and equalization distortion
- transform recorded speech to sound as though it had been recorded in a studio
- end-to-end feed-forward WaveNet architecture, trained with multi-scale adversarial discriminators in both the time domain and the time-frequency domain
- relies on the deep feature matching losses of the discriminators to improve the perceptual quality of enhanced speech



