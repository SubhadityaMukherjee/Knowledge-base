---
toc: true
title: AugMix
tags: ['augmentation']
date created: Sunday, October 9th 2022, 12:21:26 pm
date modified: Monday, October 10th 2022, 2:02:07 pm
---

# AugMix
- @hendrycksAugMixSimpleData2020
- using the input image itself
- t transforms (translate, shear, rotate and etc) the input image and mixes it with the original image
- Image transformation involves series of randomly selected augmentation operations applied with three parallel augmentation chains.
- Each chain has a composition of operations that could involve applying, for example, translation on input image followed by shear and so on
- The output of these three chains is three images mixed to form a new image.
- This new image is later mixed with the original image to generate the final augmented output image,
- while we considered mixing by alpha compositing, we chose to use elementwise convex combinations for simplicity. The k-dimensional vector of convex coefficients is randomly sampled from a Dirichlet(α, . . . , α) distribution. 
- Once these images are mixed, we use a “skip connection” to combine the result of the augmentation chain and the original image through a second random convex combination sampled from a Beta(α, α) distribution. The final image incorporates several sources of randomness from the choice of operations, the severity of these operations, the lengths of the augmentation chains, and the mixing weights
- [Jensen Shannon Divergence Consistency Loss](Jensen%20Shannon%20Divergence%20Consistency%20Loss.md)



