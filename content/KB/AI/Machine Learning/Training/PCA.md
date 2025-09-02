---
tags: ['temp']
toc: true
title: PCA
date modified: Monday, October 10th 2022, 2:02:20 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# PCA
- m dim affine hyperplace spanned by first m eigenvectors. Only manifolds and no codebook vectors
- Be able to reconstruct x from f(x) : decoding function $$x \approx d \circ f(x)$$
- ![](Pasted%20image%2020220312115438.webp)

## Steps

1. Center data (A)
	- Subtract their mean from each pattern.
	- $$\mu = \frac{1}{N}\Sigma_{i}x_{i}$$ and getting patterns $$\hat x_{i}=x_{i}-\mu$$
	- [Point Cloud](Point%20Cloud.md) with center of [Gravity](Gravity.md) : origin
		- Extend more in some "directions" characterized by unit norm direction vectors $u \in \mathbb{R}^n$ .
		- Distance of a point from the origin in the direction of u : projection of $\bar x_i$ on u aka inner product $u'\bar x_i$
		- Extension of cloud in direction u : Mean square dist to origin.
		- Largest extension : $$u_{1}= argmax_{u_{1}, ||u|| = 1} \frac{1}{N}\Sigma_{i}(u
		'\bar x_i)^2$$
		- Since centered: mean is 0 and $\frac{1}{N}\Sigma_{i}(u'\bar x_i)^2$ is the variance
		- $u_1$ is the longest direction : First PC : **PC1**
2. Project points (B)
	- Find orthogonal (90deg) subspace . (n-1) dim linear
	- Map all points $\bar x$ to $$\bar x ^{\ast}=\bar x- (u' \bar x_i^\ast)^2$$- Second PC : **PC2**
3. Rinse and repeat (C)
4. New PCs plotted in original cloud (D)
5. For featurres $f_{k}: \mathbb{R}^{n}\rightarrow \mathbb{R}$ , $x \rightarrow u'_{k}\bar x$
6. Reconstruction : $$x= \mu + \Sigma_{k= 1, …,n}f_{k}(x)u_{k}$$
	- First few PCs till index m
		- $(f_{1}(x), …, f_{m}(x))'$
		- Decoding function $$d: (f_{1}(x), …, f_{m}(x))' \rightarrow \mu + \Sigma_{k= 1}f_{k}(x)u_{k}$$
- How good is the reconstruction
	- $$\Sigma_{k=m+1}^{n} (\frac{1}{N}\Sigma_if_{k}(x_i)^2)$$
	- Relative amount of dissimilarity to mean empirical variance of patterns - 1
		- $$\frac{\Sigma_{k=m+1}^{n} (\frac{1}{N}\Sigma_if_{k}(x_i)^2)}{\Sigma_{k=1}^{n} (\frac{1}{N}\Sigma_if_{k}(x_i)^2)}$$
		- Ratio very small as index k grows. Very little info lost by reducing dims. Aka good for very high dim stuff.
7. Compute SVD
	- $u_{1,}…u_{n}$ form orthonormal, real eigenvectors
	- variances $\sigma_{1}^{2,}…, \sigma_{n}^2$ are eigenvalues
	- $C = U\Sigma U'$ to get PC vectors $u_k$ lined up in U and variances $\sigma_k^2$ as eigenvalues in $\Sigma$
	- If we want to preserve 98% variance : Rhs of (1) st. ratio is (1-0.98)



