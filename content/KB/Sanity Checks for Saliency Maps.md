---
toc: true
title: Sanity Checks for Saliency Maps

tags: ['explainability']
date modified: Wednesday 22nd February 2023, Wed
date created: Wednesday 22nd February 2023, Wed
---

# Sanity Checks for Saliency Maps


- @adebayoSanityChecksSaliency2020
- whether saliency methods are insensitive to model and data
- Insensitivity is highly undesirable, because it would mean that the "explanation" isunrelated to model and data
- Methods that are insensitive to model and training data are similar to edge detectors
- Edge detectors simply highlight strong pixel color changes in images and areunrelated to a prediction model or abstract features of the image, and require no training
- The methods tested were Vanilla Gradient, Gradient x Input, Integrated Gradients,Guided Backpropagation, Guided Grad-CAM and SmoothGrad (with VanillaGradient).
- Vanilla Gradient and Grad-CAM passed the insensitivity check, while GuidedBackpropagation and Guided Grad-CAM failed
- However, the sanity checks paper itself has found some criticism from Tomsett et al.(2020) 89 with a paper called "Sanity checks for caliency metrics" (of course
- They found that there is a lack of consistency for evaluation metrics
- So we are back to where we started ... It remains difficult to evaluate the visual explanations. This makes it very difficult for a practitioner.



