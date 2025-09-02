---
toc: true
title: Leaky Relu
tags: ['regularization']
date modified: Tuesday, January 24th 2023, 8:31:13 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Leaky Relu
- Andrew L. Maas, Awni Y. Hannun, Andrew Y. Ng (2014). Rectifier Nonlinearities Improve Neural Network Acoustic Models.
- has a small slope for negative values instead of a flat slope. The slope coefficient is determined before training, i.e. it is not learnt during training. This type of activation function is popular in tasks where we we may suffer from sparse gradients, for example training generative adversarial networks.
- The reasons can be numerous, but in order to fight the situation when suddenly lot’s of neurons in the network simply do nothing
- $$max(0.01x,x)$$
- ![](../images/Pasted%20image%2020220626151659.png)



