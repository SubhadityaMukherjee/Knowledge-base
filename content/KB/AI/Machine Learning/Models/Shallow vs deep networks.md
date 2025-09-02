---
title: Shallow vs deep networks
toc: true
tags:
  - deeplearning
date modified: Tuesday 27th August 2024, Tue
date created: Tuesday 27th August 2024, Tue
---

# Shallow vs deep networks
```toc
```

| **Shallow Networks**                                                                        | **Deep Networks**                                                                                                                                                                                                                                                                              |
| :------------------------------------------------------------------------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| single hidden layer                                                                         | multiple hidden layers                                                                                                                                                                                                                                                                         |
| can model continuous functions, but needs more hidden layers to do so                       | composition of shallow networks, so few can represent more complex functions                                                                                                                                                                                                                   |
| With one input, one output and $D > 2$ hidden units -> $D+1$ linear regions , $3D+1$ params | One input, one output, K layers of $D>2$ hidden units -> $(D+1)^{K}$ linear regions and $3D + 1 + (K-1)D(D+1)$ params                                                                                                                                                                          |
| Flexibility of functions is limited by number of parameters                                 | Complex dependencies and symmetries                                                                                                                                                                                                                                                            |
| More hidden units to achieve approximation                                                  | Less hidden units to achieve approximation -> Depth efficiency                                                                                                                                                                                                                                 |
| Processing data like images is almost infeasible                                            | Pretty easy to do so. Process local image regions in parallel and then gradually integrate information from increasingly large regions                                                                                                                                                         |
| Hard to fit data                                                                            | Overparameterized deep models have a large family of roughly equivalent solutions that are easy to find                                                                                                                                                                                        |
| Does not generalize well to new data                                                        | Generalizes better than shallow networks                                                                                                                                                                                                                                                       |
| NA                                                                                          | If the number of hidden units D in each of the K layers is the same, and D is an integer multiple of the input dimensionality $D_i$, then the maximum number of linear regions $N_r$ - $N_{r}= (\frac{D}{D_{i}}+1)^{D_{i}(K-1)} \cdot \Sigma_{j=0}^{D_{i}} \begin{pmatrix}C \\ J\end{pmatrix}$ |

