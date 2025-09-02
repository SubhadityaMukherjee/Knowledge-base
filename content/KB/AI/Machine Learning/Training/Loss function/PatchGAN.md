---
toc: true
title: PatchGAN

tags: ['loss']
date modified: Sunday, December 11th 2022, 1:22:46 pm
date created: Sunday, December 11th 2022, 1:16:53 pm
---

# PatchGAN

- Type of discriminator
- only penalizes structure at the scale of local image patches
- tries to classify if each $N \times N$ patch in an image is real or fake
- discriminator is run convolutionally across the image, averaging all responses to provide the ultimate output of $D$
- effectively models the image as a Markov random field
- assuming independence between pixels separated by more than a patch diameter
- type of texture/style loss
- rather the regular GAN maps from a 256×256 image to a single scalar output, which signifies “real” or “fake”, whereas the PatchGAN maps from 256×256 to an NxN (here 70×70) array of outputs X, where each $X_{ij}$ signifies whether the patch _ij_ in the image is real or fake.
- ![](../images/Pasted%20image%2020221211131813.png)



