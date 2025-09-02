---
toc: true
title: Focal Loss
tags: ['loss']
date modified: Monday, October 10th 2022, 2:02:27 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Focal Loss
- two-stage approach popularized by R-CNN, where a classifier is applied to a sparse set of candidate object locations.
- In contrast, one-stage detectors that are applied over a regular, [Dense](Dense.md) [sampling](Sampling.md) of possible object locations have the potential to be faster and simpler, but have trailed the accuracy of two-stage detectors thus far.
- Extreme foreground-background class imbalance encountered during training of [Dense](Dense.md) detectors is the central cause
- modulating term to [Cross Entropy](Cross%20Entropy.md) in order to focus learning on hard misclassified examples
- scaling factor decays to zero as confidence in the correct class increases
- training on a sparse set of hard examples and prevents the vast number of easy negatives from overwhelming the detector during training
- [RetinaNet](RetinaNet.md)



