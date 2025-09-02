---
toc: true
title: Ridge Regression
tags: ['temp']
date modified: Monday, October 10th 2022, 2:02:18 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Ridge Regression
- [LinearRegression](LinearRegression.md)
- $$(XX')$$ suffers from numerical instability when almost singular (real world data. sparse I think)
- Add a tiny term
	- $$w'_{opt} = (XX' + \alpha ^2 I_{nxn})^{-1}XY$$
	- Solution to overfitting



