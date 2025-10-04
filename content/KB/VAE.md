---
toc: true
title: Variational Autoencoder
tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:14 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Variational Autoencoder
- Some control over distribution of learned [Features](Features.md)
- Eg: Decoder as a generative model
- Constraint [loss](../Tag%20Pages/loss.md) function and a given [Probability](Probability.md) $\mathcal{D}$
	- Eg: By [loss](../Tag%20Pages/loss.md) func [KL Divergence](KL%20Divergence.md) and prob distribution $$L(X) = n^{-1}\Sigma_i||x_i - D(E(\tilde x))||^2 + \lambda \cdot KL(f_i, d)$
	- Use 2D unit distribution. 0 mean, unit variance
	- Latent vector : $$f=\mu + \epsilon e^{2log\sigma}$$
- $$L(X) = n^{-1}\Sigma_i||x_i - D(E(\tilde x))||^2 + \frac{1}{2n}\Sigma_i(e^{log\sigma(x_i)} + \mu(x_i)^2 -1 -log(\sigma (x_i))$
- Encoder predicts mean and std $$E(x_i) = (\mu(x_i) , log \sigma(x_i))$$



