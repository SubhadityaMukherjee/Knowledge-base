---
toc: true
title: Rmsprop
tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:18 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Rmsprop
- RL
- More stable than [Adagrad](Adagrad.md)
- Moving exponential avg : older grads given less weight
- $$\begin{align}\\

& E[g^{2}]_{t}= 0.9E[g^{2}]_{t-1}+ 0.1g^{2}_{t}\\

& \theta_{t+1}= \theta_{t}- \frac{\eta}{\sqrt{E[g^{2}])_{t}+\epsilon}}g_{t}

\end{align}

$$
- Suggested $\gamma=0.9$ and $\eta= 0.001$



