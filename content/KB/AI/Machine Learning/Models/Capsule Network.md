---
toc: true
title: Capsule Network

tags: ['architecture']
date modified: Sunday 12th February 2023, Sun
date created: Sunday 12th February 2023, Sun
---

# Capsule Network


- replace traditional convolutional and pooling layers with a more biologically inspired architecture that better captures the **spatial relationships between objects in an image**
- idea that the human visual system is composed of a **hierarchy of “capsules”** that process visual information at different levels of abstraction. 
- Each capsule comprises a **group of neurons** sensitive to **specific features** of an image, such as the presence of an edge or a particular shape. 
- These features are then combined and passed up the hierarchy to **higher-level capsules**, which extract more abstract concepts such as the identity of an object or the presence of a face.
- Capsule Networks overcome the problem of [[Translational Invariance]] caused by CNNs.
- Capsule Networks are able to capture better spatial relationship. 
- Capsule Networks uses better [[Downsampling]] methods which do not cause loss of information seen in CNNs.
- Capsule Network perform much better than CNNs but are more computationally epensive.

## Drawbacks of pooling layers
- **pooling layers**, which **down-sample** the input image and can lead to the **loss of important information** about the spatial relationships between objects in the image. 
- Capsule networks aim to overcome this limitation by using a different down-sampling mechanism that preserves more spatial information.
- [[Capsule Layer]]
- [[Primary Capsule]]
- [[Higher Layer Capsule]]

## Loss
- [[Max Margin Loss]] 
- [[Reconstruction loss]]

## Pros
-   Capsule networks are more robust to image distortions and translations than traditional CNNs
-   They can maintain the spatial relationships between objects in an image
-   They can handle partially obscured objects better
-   They can be used for a variety of tasks, including object recognition and segmentation

## Cons
- Capsule networks are more complex and computationally expensive than traditional CNNs
- They are a relatively new architecture, and there is still ongoing research to improve their performance and computational efficiency.



