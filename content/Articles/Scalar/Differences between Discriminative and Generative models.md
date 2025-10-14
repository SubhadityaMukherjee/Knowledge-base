
---
toc: true
title: Differences between Discriminative and Generative models

tags: ["article"]
date modified: 
date created: 
---
# Differences between Discriminative and Generative models

:::section{.abstract}

## Overview
Machine learning models can be broadly classified into discriminative and generative. Discriminative models, such as logistic regression, support vector machines, and decision [Trees](../../KB/Trees.md), while discriminative models are more commonly used for classification and regression.
:::
:::section{.scope}

## Scope
- The article introduces the concept of discriminative and generative models in the context of machine learning.
- The article explains the differences between these two models and how they approach tasks differently.
- The article provides examples of commonly used machine learning models in the discriminative or generative category.
- The article discusses the applications of discriminative and generative models in various tasks, such as classification, regression, and unsupervised learning.
- The article also compares the advantages and disadvantages of discriminative and generative models.

:::
:::section{.main}

## Introduction
Various Machine Learning models have been proposed over the years, each for different tasks. A broad categorization of these models is to classify them into Generative and Discriminative models. Discriminative models estimate the conditional probability, while Generative models estimate the joint probability distribution. This article will examine the difference between Generative and Discriminative models. We will also introduce several commonly used ML models and categorize them into these two groups.

## Discriminative Model
Discriminative Models are a family of models that do not generate new data points but learn to model boundaries around classes in a dataset instead. These models aim to maximize the separation between the classes in the dataset to perform classification or Regression. Discriminative models estimate the conditional probability $P(Y|X =x)$ on a data X and a target Y. 
Note that sometimes classifiers that do not use a probability model are called Discriminative Models.

### Logistic Regression
Logistic Regression is a classification algorithm that uses the **Sigmoid** function instead of a linear function to model data.

The Sigmoid curve is shown in the figure below.

[IMAGE {1} { Sigmoid Curve } START SAMPLE]
![Sigmoid Curve](https://hackmd.io/_uploads/Sk3E2bDKj.png)
[IMAGE {1} FINISH SAMPLE]

We can also use Logistic Regression for multi-class tasks by modelling each class separately. Therefore, the Regression's outcome must be a discrete or categorical value. (e.g., Yes/No, True/False) The model's output is a probabilistic value in the range [0,1]. The modelled curve that the logistic function uses indicates the likelihood of the binary decision. 
The following equation can mathematically represent Logistic Regression.
$$log[\frac{y}{1-y}] = b_0 + b_1 x_1 + b_2 x_2 + … + b_n x_n$$

Considering the difference between Generative and Discriminative models is important in understanding why these models are Discriminative.

### Support Vector Machine

A Support Vector Machine (SVM) is a supervised classification and regression algorithm that uses the concept of **hyperplanes**. These hyperplanes can be understood as **multi-dimensional linear [Decision Boundaries](../../KB/Decision%20Boundaries.md)** that separate groups of unequal data points. 
An example of a hyperplane is shown below.

[IMAGE {2 } { SVM } START SAMPLE]
![SVM](https://hackmd.io/_uploads/rkOvSQPFs.png)
[IMAGE { 2} FINISH SAMPLE]

An optimal fit of the SVM occurs when a hyperplane is furthest from the training data points of any of the classes—the larger this distance margin, the lower the error of the classifier. 
To better understand how the SVM works, consider a group of data points like the one shown in the diagram. It is a good fit if the hyperplane separates the points in the space so they are clustered according to their labels. If not, further iterations of the algorithm are performed. 

### Decision Tree

Decision [Trees](../../KB/Trees.md) are tree-based decision models that use an internal structure of a **root node** followed by successive child **leaf nodes**. The leaf nodes are a placeholder for the classification label, and the branches show the outcomes of the decision. The paths from the tree's root to the leaves represent the classifier rules. Each tree and sub-tree models a single decision and enumerates all the possible decisions to choose the best one.
A Decision tree can be optimal if it represents most of the data with the least number of levels. Decision [Trees](../../KB/Trees.md) are computationally efficient, and many tree-based optimizations have been created over the years to make them perform even faster.
An example of such a tree is shown below. 
[IMAGE {3 } { Decision Tree } START SAMPLE]
![Decision Tree](https://hackmd.io/_uploads/SJxhur7PYi.png)
[IMAGE { 3} FINISH SAMPLE]


### Random Forest

[IMAGE {4 } { Random Forest } START SAMPLE]
![Random Forest](https://hackmd.io/_uploads/S1wFBmPYo.png)
[IMAGE { 4} FINISH SAMPLE]

Random Forest models use a forest of Decision [Trees](../../KB/Trees.md) for a task is the best after the aggregation. This technique of aggregating multiple results from similar processes is called **Ensembling**. 
The second component of the Random Forest pertains to another technique called **Bagging**. Bagging differs from Ensembling because, in Bagging, the data is different for every model, while in Ensembling, the different models are run on the same data. In Bagging, a random sample with replacement is chosen multiple times to create a data sample. These data samples are then used to train the model independently. After training all these models, the majority vote is taken to find a better estimate of the data.
Random forests combine the concepts of Bagging and Ensembling to decide the best feature splits and select subsets of the same. This algorithm is better than using a single Decision Tree as it reduces bias and the net variance, generating better predictions.

Bagging and Ensembling might seem like they help model the joint probability distribution, but that is not the case. Understanding the difference between Generative and Discriminative models can clear this confusion.

## Generative Models
Generative Models are a family of models that create new data points. They are generally used for unsupervised tasks. Generative Models use the joint probability distribution $P(X, Y)$ on a variable X and a target variable Y to model the data and perform inference by estimating the probability of the new data point belonging to any given class.

### Latent Dirichlet Allocation ([LDA](../../KB/LDA.md))
[LDA](../../KB/LDA.md) maximizes the class separation and not the variance of the data.
This principle is illustrated in the figure below.

[IMAGE {5 } { LDA } START SAMPLE]
![LDA](https://hackmd.io/_uploads/rk4oHXPFi.png)
[IMAGE { 5} FINISH SAMPLE]


### Bayesian Network
A Bayesian Network is a graph-based probabilistic model that uses a special graph structure known as a DAG - Directed Acyclic Graph to model conditional dependencies between the given variables. These networks are useful in finding the possible cause of an event, given several contributing factors.
A classic example of what a Bayesian Network looks like is shown below.

[IMAGE {6 } { Bayesian Network } START SAMPLE]
![Bayesian Network](https://hackmd.io/_uploads/HJ4hrXPFj.png)
[IMAGE { 6} FINISH SAMPLE]

The Bayesian Network uses this graph to model the joint probability distribution. Each of the edges in the graph represents a dependency, while each node represents a unique variable. The model can then use this learnt distribution for inference.
We can use Bayesian Networks to infer unobserved variables, learn parameters from the data and learn the structure of a manually created data distribution.

Note that each represents Boolean variables if there are $m$ parent nodes. A minimum of $2^m$ entries are required to model the possible events.


### Hidden Markov Model
A Markov process is a sequential process where the previous item only influences the next item in the sequence. A Markov Chain, therefore, is a graph that uses probabilities to denote how likely it is to move to the next state in the chain. (If it is not clear how this is a Generative model, refer to the section on the difference between Generative and Discriminative models)
An example Markov Chain is shown below.
[IMAGE {7 } { Markov Chain } START SAMPLE]
![Markov Chain](https://hackmd.io/_uploads/SJaVS7wFs.png)
[IMAGE { 7} FINISH SAMPLE]

A Hidden Markov Model is a graph where the chain is unobservable. The inputs the model receives are combined with the probabilities of the previous step. This combination is used to calculate the next step in the graph. 
A constraint in an HMM is that at a certain time $t= t_{0}$, the target Y must be influenced only by the state of X at $t= t_{0}$. The states of Y at $t= t_{0}$ should not be affected by the states of X and Y at $t < t_{0}$.

An example of a Markov Model is shown here for reference.
[IMAGE {8 } { HMM } START SAMPLE]
![HMM](https://hackmd.io/_uploads/rkINBXDKj.png)
[IMAGE { 8} FINISH SAMPLE]


### Autoregressive model
An Autoregressive model is used in time series forecasting. This model uses the past values in the time series to predict values that might occur in the future.
An Autoregressive model gets its name as it is a regression of itself. These models are generally represented as stochastic difference equations that use linear combinations of past values to model the data. A mathematical representation is as follows.

$y_{t} + c + \phi_{1} y_{t-1} + \phi_{2} y_{t-2} + … + \phi_{p} y_{t-p} + \epsilon_{t}$
where  $\epsilon_{t}$ is white noise. 
Note that changing the patterns for $\phi$ changes the time series. Varying the error term does not change the pattern but modifies the scale of the data instead.

An example of an Autoregressive model is shown below.
[IMAGE {9 } { Autoregressive Model } START SAMPLE]
![Autoregressive Model](https://hackmd.io/_uploads/H1sQBQPYs.png)
[IMAGE { 9} FINISH SAMPLE]


### Generative Adversarial Network
Generative Adversarial Networks are models that take large image datasets as input and generate new images. A GAN models the data distribution by exploiting the latent space of the dataset given to it. A GAN comprises two parts - A Generator and a Discriminator. These parts play a MinMax Game, where the Generator creates novel images from random noise while the Discriminator classifies the outputs into real or fake. When the Discriminator can no longer distinguish between real and fake images created by the Generator, the GAN training is said to be complete.

An example of a GAN that converts images to a different style is shown in the following image.
[IMAGE {10 } { GAN } START SAMPLE]
![GAN](https://hackmd.io/_uploads/SJXQrQPKj.png)
[IMAGE { 10} FINISH SAMPLE]

### Discriminative vs Generative Models

The difference between Generative and Discriminative models is summarised in the following table.


| Generative Models                       | Discriminative Models                   |
| --------------------------------------- | --------------------------------------- |
| Aim to understand the data distribution | Aim to model the data decision boundary |
| Uses the joint probability               | Uses the conditional probability         |
| Relatively computationally expensive    | Relatively cheaper computationally      |
| Unsupervised Tasks                      | Supervised Tasks                        |
| Harmed by outliers                      | More robust to the presence of outliers |
| Models how data is placed in space      | Generates boundaries around similar classes of data in space                                        |

:::
:::section{.summary}

## Conclusion
- In summary, discriminative and generative models are two categories of machine learning models that approach tasks differently.
- Discriminative models aim to maximize the separation between classes in a dataset to perform classification or regression. 
- In contrast, generative models create new data points by estimating the joint probability distribution of the data and the target variable. 
- Both models have their own set of advantages and disadvantages and can be applied to various tasks. 

:::



