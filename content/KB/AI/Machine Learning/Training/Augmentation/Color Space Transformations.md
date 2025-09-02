---
toc: true
title: Color Space Transformations
tags: ['augmentation']
date created: Monday, October 10th 2022, 1:58:12 pm
date modified: Tuesday, January 17th 2023, 12:18:33 pm
---

# Color Space Transformations
- Image data is encoded into 3 stacked matrices, each of size height×width. These matrices represent pixel values for an individual RGB color value
- Lighting biases are amongst the most frequently occurring challenges to image recognition problems
- A quick fix to overly bright or dark images is to loop through the images and decrease or increase the pixel values by a constant value.
- Another quick color space manipulation is to splice out individual RGB color matrices.
- Another transformation consists of restricting pixel values to a certain min or max value.
- Similar to [[Geometric Transformations]], a disadvantage of color space transformations is increased memory, transformation costs, and training time.
- Additionally, color transformations may discard important color information and thus are not always a label-preserving transformation.
- For example, when decreasing the pixel values of an image to simulate a darker environment, it may become impossible to see the objects in the image.
- Digital image data is usually encoded as a tensor of the dimension (height × width × color channels)
- Performing augmentations in the color channels space is another strategy that is very practical to implement.
- Very simple color augmentations include isolating a single color channel such as R, G, or B.
- An image can be quickly converted into its representation in one color channel by isolating that matrix and adding 2 zero matrices from the other color channels. Additionally, the RGB values can be easily manipulated with simple matrix operations to increase or decrease the brightness of the image.
- More advanced color augmentations come from deriving a color histogram describing the image



