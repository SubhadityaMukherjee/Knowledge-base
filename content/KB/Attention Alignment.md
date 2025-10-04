---
toc: true
title: Attention Alignment

tags: ['loss']
date modified: Monday, October 10th 2022, 2:02:34 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# [Attention](Attention.md) Alignment
- If there are sequences $x, y$
	- Encoder is any [Recurrent](Recurrent.md) with a forward state $$\overrightarrow h^{T}$$ and $$\overleftarrow h^{T}$$ for backward
	- Concat them represents the preceding and following word annotations
		- $$h_{i}= [\overrightarrow h_{i}^{T}; \overleftarrow h_{i}^{T}]$$, $i = 1, …, n$
		- Decoder has hidden state $s_{t}= f(s_{t-1}, y_{t-1}, c_{t})$ for the output word at position t for $t = 1, …, m$
			- Context vector $c_{t}$ is a sum of hidden states of the input seq, weighted by alignment scores
			- $$c_{t}= \Sigma_{i=1}^{n}\alpha_{t,i}h_{i}$$
			- How well the two words are aligned is given by
			- $$\alpha_{t,i} = align(y_{t}, x_{i})$$
			- Taking [Softmax](Softmax.md)
				- $$\frac{exp(score(s_{t-1}, h_{i}))}{\Sigma_{i'-1}^{n}exp(score(s_{t-1}, h_{i}'))}$$
- $$f_{att}(h_{i}, s_{j}) = v_{a}^{T}tanh(W_{a}[h_{i};s_{j}])$$
- $v_{a}$ and $W_{a}$ are the learned [Attention](Attention.md) params
- $h$ is the hidden state for the encoder
- $s$ is the hidden state for the decoder
- Matrix of alignment
	- ![[Pasted image 20220621170423.png]]
	- Final scores calculated with a [Softmax](Softmax.md)



