---
toc: true
title: Guided GradCAM

tags: ['explainability']
date modified: Saturday, January 14th 2023, 5:04:24 pm
date created: Friday, November 18th 2022, 1:09:31 pm
---

# Guided [Grad-CAM](Grad-CAM.md)

- @selvarajuGradCAMWhyDid2017
- Pointwise multiply betwen [Grad-CAM] and [Guided BackProp](Grad-CAM] and [Guided BackProp.md)
- Class Discriminative
- High resolution
- Similar to [Occlusion Map](Occlusion Map.md) but faster
- Guided [Grad-CAM] is a variation of [Grad-CAM](Grad-CAM] is a variation of [Grad-CAM.md) that combines the gradients of the class scores with respect to the feature maps with the gradients of a guided backpropagation algorithm. Guided backpropagation is a method for visualizing the internal representations of a neural network by backpropagating the output of the network to the input image, while only propagating the positive gradients.
- The main difference between [Grad-CAM] and Guided [Grad-CAM] is that while [Grad-CAM] focuses on finding the regions of an image that are most important for a given classification, Guided [Grad-CAM] also takes into account the positive gradients of the guided backpropagation algorithm, in order to provide a more fine-grained [visualization] of the internal representations of the network. This can make Guided [Grad-CAM](Grad-CAM] and Guided [Grad-CAM] is that while [Grad-CAM] focuses on finding the regions of an image that are most important for a given classification, Guided [Grad-CAM] also takes into account the positive gradients of the guided backpropagation algorithm, in order to provide a more fine-grained [visualization] of the internal representations of the network. This can make Guided [Grad-CAM.md) more effective for understanding how the model is making its decisions, and for identifying the specific features of an image that the model is using for a given classification.
- ![](../images/1!cPUwFxeQBgkMoMmC1LoZkA.png)


