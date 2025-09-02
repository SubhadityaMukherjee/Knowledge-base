---
title: Change of variable theorem
toc: true
tags:
  - algebra
date modified: Tuesday 19th November 2024, Tue
date created: Tuesday 19th November 2024, Tue
---

# Change of Variable Theorem
```toc
```
- this is from [here](https://lilianweng.github.io/posts/2018-10-13-flow-models/)
- Given a random variable $z$ and its known probability density function $z \sim \pi(z)$, we would like to construct a new random variable using a 1-1 mapping function $x = f(z)$. The function $f$ is invertible, so $z=f^{-1}(x)$. 
- Now the question is <em>how to infer the unknown probability density function of the new variable</em>, $p(x)$
  
## Example
- [[6bf14b0bc57f4e48294e30954defc432_MD5.webp|Open: Pasted image 20241119160831.png]]
![[6bf14b0bc57f4e48294e30954defc432_MD5.webp]]
- define how space will be transformed locally
	- $det(J) = 2\cdot2 -0\cdot0 = 4$ (area increases by a factor of 4)
- $$p(x) = p(z) |det(\frac{\partial z}{\partial x})| = p(z) |1/ det(\frac{\partial x}{\partial z})|$$
	- each point in the X region should have 1/4th of the area of it's inverse
	- orientation does not matter

## Derivation
$$
\begin{aligned}
& \int p(x)dx = \int \pi(z)dz = 1 \scriptstyle{\text{   ; Definition of probability distribution.}}\\
& p(x) = \pi(z) \left\vert\frac{dz}{dx}\right\vert = \pi(f^{-1}(x)) \left\vert\frac{d f^{-1}}{dx}\right\vert = \pi(f^{-1}(x)) \vert (f^{-1})'(x) \vert
\end{aligned}
$$

- By definition, the integral $\int \pi(z)dz$ is the sum of an infinite number of rectangles of infinitesimal width $\Delta z$. 
- The height of such a rectangle at position $z$ is the value of the density function $\pi(z)$. When we substitute the variable, $z = f^{-1}(x)$ yields $\frac{\Delta z}{\Delta x} = (f^{-1}(x))'$ and $\Delta z =  (f^{-1}(x))' \Delta x$. 
- Here $\vert(f^{-1}(x))';\vert$ indicates the ratio between the area of rectangles defined in two different coordinate of variables $z$ and $x$ respectively.
- The multivariable version has a similar format

$$
\begin{aligned}
\mathbf{z} &\sim \pi(\mathbf{z}), \mathbf{x} = f(\mathbf{z}), \mathbf{z} = f^{-1}(\mathbf{x}) \\
p(\mathbf{x}) 
&= \pi(\mathbf{z}) \left\vert \det \dfrac{d \mathbf{z}}{d \mathbf{x}} \right\vert  
= \pi(f^{-1}(\mathbf{x})) \left\vert \det \dfrac{d f^{-1}}{d \mathbf{x}} \right\vert
\end{aligned}
$$

where $\det \frac{\partial f}{\partial\mathbf{z}}$ is the [[Jacobian Matrix#Jacobian Matrix|Jacobian]] determinant of the function $f$. 
