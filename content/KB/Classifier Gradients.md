---
toc: true
title: Classifier Gradients

tags: ['architecture']
date modified: Sunday 18th December 2022, Sun
date created: Sunday 18th December 2022, Sun
---

# Classifier Gradients


- For example, if we want to add sunglasses to an image of a face, we can used a trained classifier that identifies if a personal has that feature.
- To do this, we can take a batch of noise vector Z that goes through the generator.
- We then pass this image through a classifier, in this case a sunglasses classifier, which will tell us if the output has that feature.
- We the use this information to modify the Z vectors, without modifying the weights of the generator at all.
- To do so, we modify the Z vectors by moving in the direction of the gradient with the costs that will penalize the model for images classified as not having sunglasses. 
- We then repeat this process until the images are classified with the desired feature.
- The downside with this method is that we need a pre-trained classifier that can detect the desired feature, which may not always be readily available.



