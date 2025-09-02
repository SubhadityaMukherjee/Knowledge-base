---
toc: true
title: SaliencyMix
tags: ['augmentation']
date created: Sunday, October 9th 2022, 12:21:26 pm
date modified: Monday, October 10th 2022, 2:02:07 pm
---

# SaliencyMix
- @uddinSaliencyMixSaliencyGuided2021
- extracts salient regions and pastes them on the corresponding location in the target image
- The salient region is extracted around the maximum intensity pixel location in the saliency map
- Regional dropout is one of the popular solutions that guides the model to focus on less discriminative parts by randomly removing image regions, resulting in improved regularization
- however, such information removal is undesirable.
- On the other hand, recent strategies suggest to randomly cut and mix patches and their labels among training images, to enjoy the advantages of regional dropout without having any pointless pixel in the augmented images.
- selects a representative image patch with the help of a saliency map and mixes this indicative patch with the target image
- Furthermore, models that are trained with SaliencyMix help to improve the object detection performance
- we cut a source patch and mix it to the target image and also mix their labels proportionally to the size of the mixed patches
- But in order to prevent the model from learning any irrelevant feature representation, the proposed method enforces to select a source patch in a way so that it must contains information about the source object
- It first extracts a saliency map of the source image to highlight the objects of interest and then selects a patch surrounding the peak salient region to mix with the target image.

## Algorithm
- If $I_{s} \in \mathbb{R}^{W \times H \times C}$ is randomly selected training source with label $y_{s}$. Saliency map is $I_{vs}= f(I_{s})$ where $I_{vs}$ is the visual saliency. $f(\cdot)$ is a saliency model. 
- Search for a pixel $I_{vs}^{i,j}$ with maximum intensity
- 
$$

i,j = argmax(I_{vs})
$$
- Patch selected by centering on the $I_{vs}^{i,j}$ pixel or with this pixel in the patch
- Patch determined on a ration $\lambda$ chosen from [Uniform Distribution](Uniform Distribution.md) 

## Mixing Patches and Labels
- Another image $I_{s} \in \mathbb{R}^{W \times H \times C}$
- $I_{a} = M \odot I_{s} + M' \odot I_{t}$
	- $M \in \{0,1\}^{W, H}$
- labels $y_{a} = \lambda y_{t}+ (1-\lambda)y_{s}$

## DIFFERENT WAYS OF SELECTING AND MIXING THE SOURCE PATCH
- schemes: (i) Salient to Corresponding, that selects the source patch from the most salient region and mix it to the corresponding location of the target image; (ii) Salient to Salient, that selects the source patch from the most salient region and mix it to the salient region of the target image; (iii) Salient to Non-Salient, that selects the source patch from the most salient region but mix it to the non-salient region of the target image; (iv) Non-Salient to Salient, that selects the source patch from the non-salient region of the source image but mix it to the salient region of the target image; and (v) Non-Salient to NonSalient, that selects the source patch from the non-salient region of the source image and also mix it to the non-salient region of the target image.
- To find out the non-salient region, we use the least important pixel of an image.

## Images
- ![images/Pasted%20image%2020230508113658.png](images/Pasted%20image%2020230508113658.png)
- ![images/Pasted%20image%2020230508113709.png](images/Pasted%20image%2020230508113709.png)
- ![images/Pasted%20image%2020230508113721.png](images/Pasted%20image%2020230508113721.png)
- ![images/Pasted%20image%2020230508113734.png](images/Pasted%20image%2020230508113734.png)
- ![images/Pasted%20image%2020230508113752.png](images/Pasted%20image%2020230508113752.png)



