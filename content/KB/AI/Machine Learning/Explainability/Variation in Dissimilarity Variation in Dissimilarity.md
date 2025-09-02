---
toc: true
title: Variation in Dissimilarity Variation in Dissimilarity

tags: ['explainability']
date modified: Monday, October 10th 2022, 2:02:08 pm
date created: Wednesday, October 5th 2022, 3:02:27 pm
---

# Variation in Dissimilarity Variation in Dissimilarity
- is the variance of the NISSIM metric over the adversarial set over different levels of attack eps for a model, this shows the distribution of the attack on the model when different levels of attack are performed
- Ideally, we would want the distribution to be stable for different levels of attack
- $$m_{h}= \frac{1}{eps}\Sigma(NISSIM_{eps})$$
- $$VID = \sqrt{\frac{\Sigma(NISSIM_{eps}-m_{h})^{2}}{eps}}$$



