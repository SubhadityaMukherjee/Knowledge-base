---
toc: true
title: Cross Entropy
tags: ['loss']
date modified: Friday, January 20th 2023, 1:50:35 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Cross [Entropy](Entropy.md)
- [Entropy](Entropy.md)
- Cross-[Entropy](Entropy.md) is a measure from the field of information theory, building upon [Entropy](Entropy.md) and generally calculating the difference between two [Probability](Probability.md) [Distributions](Distributions.md).
- It is closely related to but is different from [KL Divergence](KL%20Divergence.md) that calculates the relative [Entropy](Entropy.md) between two [Probability](Probability.md) [Distributions](Distributions.md), whereas cross-[Entropy](Entropy.md) can be thought to calculate the total [Entropy](Entropy.md) between the [Distributions](Distributions.md).
- implicit distribution $$
p(Y|x;\theta)
$$ -> use CE
- $$
\mathscr{L}(\theta) = -\mathbb{E}_{(x,y) \sim P(X,Y)} log (p_{model}(Y|x))
$$
	- Categorical CE
		- ![Pasted image 20240828102117](Pasted%20image%2020240828102117.png)
		- Classification
		- Labels should be [One hot](One hot.md) 
		- $$
\mathscr{L}(\theta) = -\mathbb{E}_{(x,y) \sim P(X,Y)} \Sigma_{i=1}^C 1(y=i)log (p_{model}f_i(x|\theta))
$$
		- C is no of classes
		- $$
L(y, \hat y) = - \Sigma_{i}\Sigma_{c}y_{i}^{c} log(\hat y_{i}^{c})
$$
	- [MSE](MSE.md)
		- Regression
		- $$
\mathscr{L}(\theta) = \frac{1}{2}\mathbb{E}_{(x,y) \sim P(X,Y)}||y-f(x;\theta)||^2
$$
- [Binary Cross Entropy](Binary%20Cross%20Entropy.md)

- The Cross Entropy Loss function is a popular loss function that is used in multi-class image classification tasks. Derived from the field of information theory, it uses the concept of entropy to quantifies the discrepancy between two given probability distributions. The formula for computing the loss is given by $$
\mathscr{l}(x,y) = L = \{l_{1}, ..., l_{N}\}^{T}
$$ where $$
l_{n} = -w_{y_{n}}log \frac{exp(x_{n, y_{n}})}{\Sigma_{c=1}^{C}exp(x_{n,c})}
$$, $x$ is the input, $y$ is the target, $C$ is the number of classes

- ![](../images/Pasted%20image%2020240828102220.png)
- ![](../images/Pasted%20image%2020240828102230.png)
- Also [Negative Log Likelihood](Negative%20Log%20Likelihood.md)

