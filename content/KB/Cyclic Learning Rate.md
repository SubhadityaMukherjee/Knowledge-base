---
toc: true
title: Cyclic Learning Rate

tags: ['optimizer']
date modified: Monday, October 10th 2022, 2:02:30 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Cyclic Learning Rate
- With respect to local minima and [Saddle Points](Saddle%20Points.md), one could argue that you could simply walk "past" them if you set steps that are large enough. Having a learning rate that is too small will thus ensure that you get stuck.
- Now, Cyclical Learning Rates - which were introduced by Smith (2017) - help you fix this issue. These learning rates are indeed cyclical, and ensure that the learning rate moves back and forth between a _minimum value_ and a _maximum value_ all the time.
- ![](../images/Pasted%20image%2020220626150653.png)
- ![](../images/Pasted%20image%2020220626150655.png)
- ![](../images/Pasted%20image%2020220626150701.png)



