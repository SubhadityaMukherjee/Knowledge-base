---
toc: true
title: Convolutional RNN
tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:31 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Convolutional RNN
- $$h_t = \sigma_h(W_{hh}\star h_{t-1} + W_{xh}\star x_t + b_h)$$
- $$y_t = \sigma_y(W_{hy}\star h_t + b_y)$$
- $$\star$$ is spatial [Conv](Conv.md)
- 5D shapes -> [samples, timesteps, width, height, channels]
- Very memory intensive
- $$x^{2}+x$$



