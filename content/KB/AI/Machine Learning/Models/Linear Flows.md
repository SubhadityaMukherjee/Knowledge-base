---
title: Linear Flows
toc: true
tags:
  - architecture
date modified: Tuesday 19th November 2024, Tue
date created: Tuesday 19th November 2024, Tue
---

# Linear Flows
```toc
```

$$f[h] = \beta+ \Omega h$$

- the determinant of the jacobian is the determinant of $\Omega$
- One way to make a linear flow that is general, eﬀicient to invert, and for which the Jacobian can be computed eﬀiciently is to parameterize it directly in terms of the LU decomposition
	- $$\Omega= PL(U + D)$$
	- where P is a predetermined permutation matrix, L is a lower triangular matrix, U is an upper triangular matrix with zeros on the diagonal, and D is a diagonal matrix that supplies those missing diagonal elements