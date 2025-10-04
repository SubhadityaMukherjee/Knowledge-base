---
toc: true
title: FGSM

tags: ['explainability']
date modified: Monday, October 10th 2022, 2:02:08 pm
date created: Wednesday, October 5th 2022, 2:53:25 pm
---

# FGSM
- FGSM is a method of generating noise in the direction of the cost function gradient concerning the data
- Given original input image x, label y, model parameter θ, and loss J.  
- $$adv_{x}= x+ \epsilon \ast sign(\nabla_{x}(J(\theta, x, y)))$$
- this gives us the perturbations



