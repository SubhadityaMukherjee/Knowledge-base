---
toc: true
title: Instance-based Learning
tags: ['robotics']
---

# Instance-based Learning
- an object category is represented by a set of known instances a nearest neighbor classifier is used
- IBL considers category learning as a process of learning about the instances of the category:
- The training phase is very fast
- IBL can recognize objects using a very small number of experiences IBL is a baseline approach to evaluate object representations Simple and easy to implement
- Memory usage in instance-based systems is continuously growing. Computational complexity grows with the number of training instances
- The computational complexity of classifying a single new instance is O(n), where n is number of instances stored in perceptual memory.
- Salience and forgetting mechanisms can be used to bound the memory usage which are also useful for reducing the risk of overfitting to noise in the training set.
- Overfitting
- Sensitive to noise
- ![](../images/Pasted%20image%2020221103123756.png)



