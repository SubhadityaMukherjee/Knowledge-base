---
toc: true
title: Gated Recurrent Unit (GRU)
tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:27 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Gated [Recurrent](Recurrent.md) Unit (GRU)
- ![](../images/Pasted%20image%2020220621124840.png)
- Simplified [LSTM)](Long Short Term Memory (LSTM|Long Short Term Memory (LSTM|[LSTM)](LSTM)](LSTM)](Long Short Term Memory (LSTM|Long Short Term Memory (LSTM|[LSTM)](LSTM).md).md)
- It has an input and forget gate, no output gate
- Faster than LSTM in training, but does not perform well in many tasks
- Tries to forget what is not important

## The Math
- Two gates, [Sigmoid](Sigmoid.md)
	- Reset : $$g_r = \sigma(W_{hr}h_{t-1} + W_{xr}x_t + b_r)$$
	- Update : $$g_u = \sigma(W_{hu}h_{t-1} + W_{xu}x_t + b_u)$$
- Hidden state proposal
	- $$\hat h_t = tanh(W_{xh}x_t + W_{hh}g_r\cdot h_{t-1} + b_h)$$
- Final hidden state
	- Linear [Interpolation](Interpolation.md) between last hidden state and proposal
	- $$h_t = (1-g_u)\cdot h_{t-1} + g_u \cdot \hat h_t$$



