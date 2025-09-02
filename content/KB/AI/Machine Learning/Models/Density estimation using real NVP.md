---
title: Density estimation using real NVP
toc: true
tags:
  - distributions
  - architecture
date modified: Tuesday 19th November 2024, Tue
date created: Tuesday 19th November 2024, Tue
---

# Density Estimation Using Real NVP
```toc
```
- ![[dcc9909e54da929309a50a552074048b_MD5.webp|Open: Pasted image 20241119171117.png]]
- follow up to [[NICE - non linear independant components estimation]]
- different sets of latent variables for different resolutions $$z = (z^{(1)}, …, z^{(L)})$$
	- latents corresponding to finer details can be left out during inference

## Also for [[VAE]]
- Eg: Parameterize the approximate posterior in a [[VAE]] using a flow for better inference $p_\theta(x|z)p_\theta(z)$
	- [[268644ad8a5d0ae0a9b1f6c93465616e_MD5.webp|Open: Pasted image 20241119171440.png]]
![[268644ad8a5d0ae0a9b1f6c93465616e_MD5.webp]]
- transform into something more flexible[[71485bd3414e589c2d9e74c3f27fe674_MD5.webp|Open: Pasted image 20241119171554.png]]
![[71485bd3414e589c2d9e74c3f27fe674_MD5.webp]]

