---
toc: true
title: Ensemble Distillation
tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:28 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Ensemble Distillation
- [Distilling the Knowledge in a Neural Network](https://arxiv.org/abs/1503.02531)
- training many different models on the same data and then to average their predictions
- making predictions using a whole ensemble of models is cumbersome and may be too computationally expensive to allow deployment to a large number of users, especially if the individual models are large neural nets
- compress the knowledge in an ensemble into a single model
- [MNIST](MNIST.md)
- ensemble composed of one or more full models and many specialist models which learn to distinguish fine-grained classes that the full models confuse
- specialist models can be trained rapidly and in parallel
- distillation works remarkably well even when the transfer set that is used to train the distilled model lacks any examples of one or more of the classes
- performance of a single really big net that has been trained for a very long time can be significantly improved by learning a large number of specialist nets, each of which learns to discriminate between the classes in a highly confusable cluster.



