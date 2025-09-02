---
toc: true
title: Effects of Regularization

tags: ['regularization']
date modified: Monday, October 10th 2022, 2:02:29 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Effects of [Regularization](Regularization.md)
- [The Effects of Regularization and Data Augmentation are Class Dependent](https://arxiv.org/abs/2204.03632)
- Current Deep Networks heavily rely on regularizers such as data [Augmentation](Augmentation.md) (DA) or [Weight Decay](Weight%20Decay), and employ structural risk minimization, i.e., [Cross Validation](Cross%20Validation.md), to select the optimal [Regularization](Regularization.md) hyper-parameters
- weight decay increases the average test performances at the cost of significant performance drops on some specific classes
- unfair across classes
- By focusing on maximizing aggregate performance statistics we have produced learning mechanisms that can be potentially harmful, especially in [Transfer Learning](Transfer%20Learning.md) tasks
- optimal amount of DA or weight decay found from cross-validation leads to disastrous model performances on some classes
- only by introducing random crop DA during training
- such performance drop also appears when introducing uninformative [Regularization](Regularization.md) techniques such as weight decay
- ur search for ever increasing generalization performance – averaged over all classes and samples – has left us with models and regularizers that silently sacrifice performances on some classes.
- varying the amount of [Regularization](Regularization.md) employed during pre-training of a specific dataset impacts the per-class performances of that pre-trained model on different downstream tasks e.g. an [ImageNet](ImageNet.md) pre-trained ResNet50 deployed on INaturalist sees its performances fall from 70% to 30% on a particular classwhen introducing random crop DA during the [ImageNet](ImageNet.md) pre-training phase
- designing novel regularizers without class-dependent bias remains an open research question
- Categories largely identifiable by color or texture (for e.g., yellow bird, textured mushroom) are unaffected by aggressive [cropping], while categories identifiable by shape (for e.g., corkscrew) see a performance degradation with aggressive [cropping](cropping], while categories identifiable by shape (for e.g., corkscrew) see a performance degradation with aggressive [cropping.md) that only contains part of the object
- Conversely, color jitter does not affect shape or texture-based categories (for e.g., zebra), but affects color-based categories (for e.g., basket ball)



