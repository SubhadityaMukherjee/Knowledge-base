---
tags: ['temp']
toc: true
title: Recurrent
tag: todo architecture
date modified: Monday, October 10th 2022, 2:02:18 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Recurrent
- Sequences as inputs/outputs
- Sequential processing
- Turing complete
- memory through state persisted between timesteps
	- operation invariant to the sequence
	- reduces no of params needed
- Output comes back as input
	- ![](../images/Pasted%20image%2020220314132442.png)
- variable sized inputs and outputs : encoder decoder
- Three weight matrices and two bias vectors.
- $$h_t = \sigma_h(W_{hh}h_{t-1} + W_{xh}x_t + b_h)$$
- $$y_t = \sigma_y(W_{hy}h_t + b_y)$$
- Stateful : hidden state kept across batches of inputs
- Activation usually [Sigmoid](Sigmoid.md) or [Tanh](Tanh.md)
- BPTT
	- ![](../images/Pasted%20image%2020220306185944.png)![](../images/Pasted%20image%2020220306190603.png)
	- #architecture
		- If eigen decomposition $$W = Q\wedge^tQ$$, then $$h_t = Q^T\wedge^tQ$$
		- If less than 0 then will converge to 0 or if bigger then will explore to infinity -> long sequences
		- Element wise clipping #deeplearning
			- [CLIP](CLIP.md) if bigger than value
		- Norm clipping
			- [CLIP](CLIP.md) if $$||g|| >v$ set $g = \frac{gv}{||g||}$
			- v can be decided by trial and error
- Training stuff
	- [Softmax](Softmax.md) but on every output vector simultaneously
		- If [Softmax](Softmax.md#T%20is%20the%20Temperature) is lower (eg between 0 and 0.5). It becomes more confident and hence more conservative
		- Near 0 is very diverse and less confident
	- Feed a char into the RNN -> distribution over characters that comes next -> Sample from it -> Feed it back
- Some basic patterns [from here](http://karpathy.github.io/2015/05/21/rnn-effectiveness/)
	- The model first discovers the general word-space structure and then rapidly starts to learn the words.
	- First starting with the short words and then eventually the longer ones.
	- Topics and themes that span multiple words (and in general longer-term dependencies) start to emerge only much later.



