---
toc: true
title: Long Short Term Memory (LSTM)
tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:23 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Long Short Term Memory (LSTM)
- ![](../images/Pasted%20image%2020220621124622.png)
- Smaller chance of exploding or vanishing #architecture
- Better ability to model long term dependencies
- Gated connections
- Gates that learn to forget some aspects, and remember others better
- Splitting state into parts -> output pred and [Feature Learning](Feature%20Learning.md)
- At the end of the day, these could not handle too long sequences. Therefore -> [Transformer](Transformer.md)

## The Math
- Gates
	- Forget $$g_f = \sigma(W_{hf}h_{t-1} + W_{xf}x_t + b_f)$$
		- How much of the previous cell state is used
	- Input $$g_i = \sigma(W_{hi}h_{t-1} + W_{xi}x_t + b_i)$$
		- How proposal is added to the state
	- Output $$g_o = \sigma(W_{ho}h_{t-1} + W_{xo}x_t + b_o)$$
		- Component wise products
- Hidden state
	- $$C_t$$ to model cross timestep dependencies
		- Cell state proposal : $$\hat C = tanh(W_{hc}h_{t-1} + W_{xc}x_t + b_c)$$
		- Final cell state : $$C_t = g_f \cdot C_{t-1} + g_i\cdot \hat C$$
	- $$h_t$$ to predict output
		- $$h_t = g_o \cdot \sigma_y(C_t)$$



