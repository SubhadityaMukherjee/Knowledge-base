---
title: Chapter 16 - Normalizing Flows
toc: true
tags:
  - architecture
  - distributions
date modified: Monday 18th November 2024, Mon
date created: Monday 18th November 2024, Mon
---

# Chapter 16 - Normalizing Flows
```toc
```

- Warning : If I explain every equation **fully**, we won't get lunch. So I will share this document later.
- ![[acdbeae2c39f724956669541acd4e3f2_MD5.webp]]
## Intro
- [[Articles/Scalar/CycleGAN #scalar#GAN|GANs]] -> samples should be as close to real data as possible -> hard to identify distribution
- Normalizing flow -> take an input distribution -> convert it to a more complicated one using a NN -> learn a probability model
- ![[e43129be5da18e472c80f272a621bd7f_MD5.webp]]
## Algebra
- [[Jacobian Matrix]]
- [[bijective function]], [[surjection]]

## What is a Normalizing Flow

- Density estimation is hard
	- we need to run backprop in deep learning models, the posterior $p(z|x$) should be easy to calculate the derivative of. So, we use a gaussian distribution when we can. (Of course this is not really nice always)
- NF models offer better and more powerful distribution approximation
- Transforms a simple distribution into a complex one by applying a sequence of invertible transformation functions
	- Flowing through a chain of transformations, we repeatedly substitute the variable for the new one according to the change of variables theorem and eventually obtain a probability distribution of the final target variable.
	- ![[0de75c83dd213adddd7e30d75e464f8e_MD5.webp]]
- only works with integer data
## Uses of Normalizing Flows
- ![[58d549db79bf271c31b4ed36d53613f4_MD5.webp]]
- Approximating density models
## Steps for a Normalizing Flow
- Consider a continuous random variable $z \sim p_{\theta(z)}= \mathcal{N}(z;0,I)$ (simple distribution like Spherical gaussian)
- Transform this distribution using a composition of functions to a more complicated one. $x = f_{\theta}(z)$
- each $f_{i}$ is invertible ([[bijective function]]), so all of the transformations are also invertible $x = f_{\theta}(z) = f_{k} \circ … \circ f_{2} \circ f_{1}(z)$
	- ![[b88922b248204fa1441df4638d7083cc_MD5.webp]]
- So what is the [[PDF]] of x? 
	- Maybe, $p_{\theta(x)}= p_\theta(f^{-1}_{\theta}(x))$
	- but this is not really always true, and depends on the behavior of the function f
	- why?
		- ![[59f52d7d23d99e0027e69eb14f1d4923_MD5.webp|Open: Pasted image 20241119181152.png]]
		- z = f(x) is where the point in x moves to z
		- the det is the mass that gets pushed in the neighborhood
	- forward and backward mapping
		- ![[198b30b1fb5901d77b40c7803e2170d7_MD5.webp]]
- From the [[Change of variable theorem]] and [[Jacobian Matrix]], we get $p_{\theta}(x)= p_{\theta}(f^{-1}(\mathbf{x})) \left\vert \det (\dfrac{\partial f^{-1}(x)}{\partial \mathbf{x}}) \right\vert$
	- Assume $f^{-1}(x) =z$
	- $p_{\theta}(x)= p_{\theta}(z) \left\vert \det (\dfrac{\partial z}{\partial \mathbf{x}}) \right\vert$
	- A valid pdf must always integrate to 1
- So what is a normalizing flow?
	- A sequence of bijective transformations is a normalizing flow. After z is initially sampled, it flows through these steps.
		- Density function is re-normalized at each step to ensure it remains valid.
- forward mapping for deep neural networks
			- ![[76ff523a24286f0a8a8035b8107e4fd7_MD5.webp]]
			- ![[f375adad1fcac49c628730e327bd387d_MD5.webp]]
- [[Capsule Network#Loss|Loss]] function
	- Let us parameterize the likelihood function as a flow
		- We have, $p_{\theta(x)}= p_{\theta}(z)\left\vert \det (\dfrac{\partial f^{-1}}{\partial \mathbf{x}}) \right\vert$
		- Applying log on both sides, $\log p_{\theta(x)}= \log p_{\theta}(z) + \log \left\vert \det (\dfrac{\partial f^{-1}}{\partial \mathbf{x}}) \right\vert$
	- Overall transformation f is a composition of a sequence of functions
		- replace the log determinant with the sum of the log determinants of the intermediate jacobians
		- $\log p_{\theta(x)}= \log p_{\theta}(z) + \Sigma_{i=1}^{K} \log \left\vert \det (\dfrac{\partial f^{-1}}{\partial \mathbf{x}}) \right\vert$
		- Using this, we can now use [[Maximum Likelihood]] to train our model since we can calculate the log marginal likelihood exactly
		- Exact posterior inference (unique z for a given x using ($z = f^{-1}(x$))
	- This determinant is now very expensive to compute (of course it is :P), so we ensure that the [[Jacobian Matrix#Jacobian Matrix|Jacobian]] is triangular.
		- determinant of a triangular matrix = product of it's diagonal
		- to ensure triangular : the paper [[NICE - non linear independant components estimation]] uses [[coupling flows]]
	- Using [[coupling flows]], we now get $$\log p_{\theta(x)}= \Sigma_{i=1}^D [\log (p_\theta(f^{-1}(x)_{i}))- log(\vert S_{ii} \vert)]$$
- Now it is annoying to only have latent space = dimensionality of the data (need this for a bijection)
	- [[Density estimation using real NVP]]

## Other Detailed Information (if time permits)
-  [[Properties Required by Network Layers for Normalizing Flows]]
- How do we handle different types of data - [[Types of Normalizing flows]]

## Vs Others
- vs. [[VAE]] 
	- can only get the lower bound on log-likelihood ([[ELBO loss]])
	- approximate posterior $q_\theta(z|x)$
- [[GAN]]
	- no log likelihood, only min-max evaluation
	- no latent variable inference

## References + Resources for the Math
- [Ari seff](https://www.youtube.com/watch?v=i7LjDvsLWCg)
- [lilian weng](https://lilianweng.github.io/posts/2018-10-13-flow-models/)
- [hans van gorp](https://www.youtube.com/watch?v=yxVcnuRrKqQ)
- [4 hour cvpr tutorial](https://www.youtube.com/watch?v=8XufsgG066A)