---
toc: true
title: Inductive Bias
tags:
  - graph
date modified: Monday, October 10th 2022, 2:02:25 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Inductive Bias
- Set of assumptions that the learner uses to predict outputs of given inputs that it has not yet encountered
- In [Bayesian](Bayesian.md)
	- [Bayesian Prior](Bayesian%20Prior.md) can shape the [Bayesian Posterior](Bayesian%20Posterior.md) in the way that it can be a similar distribution to the former
- In [KNN](KNN)
	- we assume that similar data points are clustered near each other away from the dissimilar ones
- in [LinearRegression](LinearRegression.md)
	- we assume that the variable Y is linearly dependent on the explanatory variables X.
	- Therefore, the resulting model linearly fits the training data. However, this assumption can limit the model’s capacity to learn non-linear functions.
- in [Logistic Regression](Logistic%20Regression)
	- assume that there’s a hyperplane that separates the two classes from each other. This simplifies the problem, but one can imagine that if the assumption is not valid, we won’t have a good model.
- [Non Relational Inductive Bias](Non%20Relational%20Inductive%20Bias.md)
- [Relational Inductive Bias](Relational%20Inductive%20Bias.md)



