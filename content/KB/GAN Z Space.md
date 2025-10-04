---
toc: true
title: GAN Z Space

tags: ['architecture']
date modified: Sunday 18th December 2022, Sun
date created: Sunday 18th December 2022, Sun
---

# GAN Z Space

## Vector Algebra in Z-Space
- Controllable generation is somewhat similar to interpolation.
- With interpolation, you get intermediate examples between two generated observations.
- These intermediate examples between to two targets by manipulating the inputs from Z-space, which is the same idea behind controllable generation.
- In order to get intermediate values between two images, for example, you can make an interpolation between their two input vectors v1 and v2 in the Z-space.
- Controllable generation also uses changes in Z-space and makes use of how adjustments to the noise vector are reflected in the output from the generator.
-  Differences in the features generated, for example different hair colors, occur due to changes in the direction that you have to move in Z-space to modify the features of the image.
- If image output of $g(v_{1})$ , new controlled output with $g(v_{1}+d)$



