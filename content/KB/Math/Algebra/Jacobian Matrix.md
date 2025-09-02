---
title: Jacobian Matrix
toc: true
tags:
  - algebra
date modified: Monday 18th November 2024, Mon
date created: Monday 18th November 2024, Mon
---

# Jacobian Matrix
```toc
```
- Given a function of mapping a n-dim input vector x to a m-dim output vector $\mathbf{f}: \mathbb{R}^n \mapsto \mathbb{R}^m$, the matrix of all first order partial derivates of this function is the Jacobian matrix J
- $\mathbf{J}_{ij} = \frac{\partial f_i}{\partial x_j}$
- jacobian matrix $$\mathbf{J} = \begin{bmatrix}
\frac{\partial f_1}{\partial x_1} & \dots & \frac{\partial f_1}{\partial x_n} \\[6pt]
\vdots & \ddots & \vdots \\[6pt]
\frac{\partial f_m}{\partial x_1} & \dots & \frac{\partial f_m}{\partial x_n} \\[6pt]
\end{bmatrix}$$

## Determinant

- The absolute value of the determinant can be thought of as a measure of _"how much multiplication by the matrix expands or contracts space"._
- Only exists for square matrices
- if det(M) = 0, then M is not invertible
- The determinant of a 2 × 2 matrix is ${\displaystyle {\begin{vmatrix}a&b\\c&d\end{vmatrix}}=ad-bc}$
- determinant of a 3 × 3 matrix is $\begin{vmatrix} a & b & c \\ d & e & f \\ g & h & i \end{vmatrix}= aei + bfg + cdh - ceg - bdi - afh$
- nxn matrix M is $$\det M = \det \begin{bmatrix}
a_{11} & a_{12} & \dots & a_{1n} \\
a_{21} & a_{22} & \dots & a_{2n} \\
\vdots & \vdots & & \vdots \\
a_{n1} & a_{n2} & \dots & a_{nn} \\
\end{bmatrix} = \sum_{j_1 j_2 \dots j_n} (-1)^{\tau(j_1 j_2 \dots j_n)} a_{1j_1} a_{2j_2} \dots a_{nj_n}$$
- where the subscript under the summation j1⁢j2…jn are all permutations of the set {1, 2, …, n}, so there are n! items in total; τ⁡(.) indicates the signature of a permutation.
- $det(AB) = det(A)det(B)$