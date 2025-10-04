---
toc: true
title: Filter Wise Normalization

tags: ['explainability']
date modified: Monday 27th March 2023, Mon
date created: Monday 27th March 2023, Mon
---

# Filter Wise Normalization


- Following up from [Random Directions](Random Directions.md) 
$$
d_{i,j} \leftarrow \frac{d_{i,j}}{||d_{i,j}||}||\theta_{i,j}||
$$
	- d is a random Gaussian Direction vector
	- $d_{i,j}$ is $j_{th}$ filter of the $i_{th}$ layer of the direction vector d
	- $||\cdot||$ is the [Frobenius norm](Frobenius norm.md)
- ![](../images/Pasted%20image%2020230327130027.png)
- ![](../images/Pasted%20image%2020230327130311.png)



