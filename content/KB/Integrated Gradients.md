---
toc: true
title: Integrated Gradients
tags: ['explainability']
date modified: Tuesday, December 6th 2022, 12:46:40 pm
date created: Tuesday, December 6th 2022, 12:46:39 pm
---

# Integrated Gradients
- @sundararajanAxiomaticAttributionDeep2017

## Terms
- [Gradient Sensitivity](Gradient Sensitivity.md)
- [Implementation Invariance](Implementation Invariance.md)

## Calculation

- a function F representing our model
- input $x \in \mathbb{R}^{n}$ because this is a general definition of IG and not CNN specific),
- baseline $x' \in \mathbb{R}^{n}$
- We assume a straight line path between x and x' and compute gradients along that path
- The integrated gradient along $i^{th}$ dimension is defined as:
- $$IntegratedGrads_i​(x)::=(x_i​-x_i'​)\times \int_{\alpha=0}^{1}\frac{\partial F(x' + \alpha \times (x-x'))}{\partial x_{i}}d \alpha$$
- The original definition of Integrated Gradients is incalculable (because of the integral).
- Therefore, the implementation of the method uses approximated value by replacing the integral with the summation:
- $$IntegratedGrads_i​^{approx}(x)::=(x_i​-x_i'​)\times \Sigma_{k=1}^{m}\frac{\partial F(x' + \frac{k}{m} \times (x-x'))}{\partial x_{i}} \times \frac{1}{m}$$
- In the approximated calculation (Eq. 2), m defines a number of interpolation steps.

## Explanation (chatgpt)
- In IntegratedGrads, the goal is to understand the contribution of each pixel in the input image towards the model's prediction. Specifically, for a given pixel $i$, IntegratedGrads computes the partial derivative of the model output with respect to that pixel and integrates it along a path from a baseline image to the input image, weighting each step of the path by the partial derivative.
- The equation you provided is an approximation of IntegratedGrads, which involves dividing the path into $m$ equally spaced steps and approximating the integral using a Riemann sum. Let's break down the equation using an example of an image of a bird:
- $IntegratedGrads_i^{approx}(x)$ represents the attribution of pixel $i$ towards the model's prediction, using the IntegratedGrads approximation.
- $(x_i-x_i')$ is the difference between the input image pixel $i$ and the baseline pixel $i'$.
- $\Sigma_{k=1}^{m}$ is a sum over the $m$ steps of the path from the baseline image to the input image.
- $\frac{\partial F(x' + \frac{k}{m} \times (x-x'))}{\partial x_i}$ is the partial derivative of the model output $F$ with respect to pixel $i$ at the $k$-th step of the path, where $x' + \frac{k}{m} \times (x-x')$ is the image at that step.
- $\frac{1}{m}$ is a weighting factor that ensures that each step of the path is given equal importance in the approximation.
- For example, let's say we have an image of a bird and we want to understand the contribution of the pixel at position $(10, 20)$ towards the model's prediction that the image is a bird. We set the baseline pixel value to be zero and divide the path into 10 steps. We compute the partial derivative of the model output with respect to pixel $(10, 20)$ at each step of the path and weight each step by $\frac{1}{10}$ to obtain the approximation of IntegratedGrads for pixel $(10, 20)$. The resulting attribution value will give us an indication of how important that pixel is in the model's prediction.

## Baselines

- replacing the constant color baseline with an alternative
- [Gaussian Baseline](Gaussian Baseline.md)
- [Blur Baseline](Blur Baseline.md)
- [Visualizing the Impact of Feature Attribution Baselines](Visualizing the Impact of Feature Attribution Baselines.md)




