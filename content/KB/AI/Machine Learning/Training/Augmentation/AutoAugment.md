---
toc: true
title: AutoAugment
tags: ['augmentation']
date created: Monday, October 10th 2022, 1:58:12 pm
date modified: Monday, October 10th 2022, 2:02:06 pm
---

# AutoAugment
- developed by Cubuk et al.
- much different approach to meta-learning than [[Neural Augmentation]]
- AutoAugment is a Reinforcement Learning algorithm that searches for an optimal augmentation policy amongst a constrained set of [[Geometric Transformations]] with miscellaneous levels of distortions. For example, ‘translateX 20 pixels’ could be one of the transformations in the search space
- In Reinforcement Learning algorithms, a policy is analogous to the strategy of the learning algorithm. This policy determines what actions to take at given states to achieve some goal. The AutoAugment approach learns a policy which consists of many subpolicies, each sub-policy consisting of an image transformation and a magnitude of transformation
- Reinforcement Learning is thus used as a discrete search algorithm of augmentations.



