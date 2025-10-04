---
toc: true
title: AutoDistill

tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:34 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# AutoDistill
- [AutoDistill: an End-to-End Framework to Explore and Distill Hardware-Efficient Language Models](https://arxiv.org/abs/2201.08539)
- (NLP) tasks but they are expensive to serve due to long serving latency and large memory usage
- compress these models, [Knowledge Distillation](Knowledge%20Distillation.md)
- handling fast evolving models, considering serving performance, and optimizing for multiple objectives.
- end-to-end model distillation framework integrating model architecture exploration and multi-objective optimization for building hardware-efficient NLP pre-trained models
- [Bayesian](Bayesian.md) Optimization to conduct multi-objective Neural Architecture Search for selecting student model architectures
- proposed search comprehensively considers both prediction accuracy and serving latency on target hardware
- TPUv4i
- MobileBERT
- [GLUE](GLUE.md)
- higher than BERT_BASE, DistillBERT, [TinyBERT](TinyBERT.md), NAS-BERT, and MobileBERT



