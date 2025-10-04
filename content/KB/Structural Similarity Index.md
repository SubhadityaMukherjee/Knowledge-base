---
toc: true
title: Structural Similarity Index

tags: ['explainability']
date modified: Monday, October 10th 2022, 2:02:08 pm
date created: Wednesday, October 5th 2022, 2:56:23 pm
---

# Structural Similarity Index
- method for predicting the perceived quality of digital television and cinematic pictures, as well as other kinds of digital images and videos. SSIM is used for measuring the similarity between two images
- $$\hbox{SSIM}(x,y) = \frac{(2\mu_x\mu_y + c_1)(2\sigma_{xy} + c_2)}{(\mu_x^2 + \mu_y^2 + c_1)(\sigma_x^2 + \sigma_y^2 + c_2)}$$
- $\mu_x$ the pixel sample mean of $x$;
- $\mu_y$ the pixel sample mean of $y$;
- $\sigma_x^2$ the variance of $x$;
- $\sigma_y^2$ the variance of $y$;
- $\sigma_{xy}$ the [Covariance](Covariance.md) of $x$ and $y$;
- $c_1 = (k_1L)^2$, $c_2 = (k_2L)^2$ two variables to stabilize the division with weak denominator;
- $L$ the dynamic range of the pixel-values (typically this is $2^{\#bits\ per\ pixel}-1$);
- $k_1 = 0.01$ and $k_2 = 0.03$ by default.



