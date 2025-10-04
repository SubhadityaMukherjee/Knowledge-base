---
toc: true
title: Generative RNN

tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:26 pm
date created: Thursday, July 28th 2022, 5:59:06 pm
---

# Generative RNN
- initial sequence is used as seed and output is sampled 
    - random or argmax to sample
    - normally not taking argmax but sample with respective [Softmax](Softmax.md) probabilities -> allows to generate something different than input
- new output is used as seed to generate next 
- repeat until termination criterion



