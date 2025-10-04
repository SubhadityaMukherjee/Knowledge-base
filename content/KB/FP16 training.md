---
tags: ['temp']
toc: true
title: FP16 training
date modified: Monday, October 10th 2022, 2:02:28 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# FP16 Training
- @micikeviciusMixedPrecisionTraining2018
- Reduced precision has a narrower range that might make the results more out of range and worsen the training progress
- Can store all parameters and activations in FP16 and then use that for gradients.
- Also copy to FP32 for parameter updates
- Multiply scalar to loss to align range of FP16



