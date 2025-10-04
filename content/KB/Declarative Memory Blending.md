---
toc: true
title: Declarative Memory Blending

tags: ['cognitivemodel']
date modified: Monday, November 28th 2022, 1:17:50 pm
date created: Monday, November 28th 2022, 1:07:49 pm
---

# Declarative Memory Blending

- Like "weighted avg"
- store no of pulses
- activation decays in time
	- $$A(t) = log(t-t_{creation})^{-d}+\text{mismatchpenalty}$$
	- Retrieval probability
		- [Softmax](Softmax.md)
		- $$P_{i}= \frac{e^{\frac{A_{t}}{t}}}{\Sigma_{i}e^{\frac{A_{t}}{t}}}$$
	- Adds up to 1
	- $$Result = \Sigma_{j}P_{j}V_{j}$$
	- t controls noise
		- if t is high : 1/no of competitors , more prob of retrieval
	- Looking for long interval (partial matching)
	- Penalty for short intervals
	- Apply $P_{i}$
	- Weighted avg $Result$
- Too short is positive. else negative, correct is 0
- no of pulses to wait : duration + feedback from memory

## Fit
- Exp done on generated data as well
- Compares if same as when run on original
- Does well with unmodified mode	
- ![](../images/Pasted%20image%2020221128131719.png)



