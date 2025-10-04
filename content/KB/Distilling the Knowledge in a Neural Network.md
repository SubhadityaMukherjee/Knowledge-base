---
toc: true
title: Distilling the Knowledge in a Neural Network

tags: ['knowledgedistillation']
date modified: Tuesday, January 24th 2023, 8:23:46 pm
date created: Tuesday, October 4th 2022, 12:50:52 pm
---

# Distilling the Knowledge in a Neural Network
- Geoffrey Hinton, Oriol Vinyals, Jeff Dean

## Intro
- compress the knowledge in an ensemble into a single model which is much easier to deploy
- new type of ensemble composed of one or more full models and many specialist models which learn to distinguish fine-grained classes that the full models confuse
- Unlike a mixture of experts, these specialist models can be trained rapidly and in parallel
- Many insects have a larval form that is optimized for extracting energy and nutrients from the environment and a completely different adult form that is optimized for the very different requirements of traveling and reproduction
- training must extract structure from very large, highly redundant datasets but it does not need to operate in real time and it can use a huge amount of computation. Deployment to a large number of users, however, has much more stringent requirements on latency and computational resources.
- The cumbersome model could be an ensemble of separately trained models or a single very large model trained with a very strong regularizer such as [Dropout](Dropout.md)
- we tend to identify the knowledge in a trained model with the learned parameter values and this makes it hard to see how we can change the form of the model but keep the same knowledge.
- learned
- where T is a temperature that is normally set to 1

## Observations
- This net achieved 67 test errors whereas a smaller net with two hidden layers of 800 rectified linear hidden units and no [Regularization](Regularization.md) achieved 146 errors
- soft targets can transfer a great deal of knowledge to the distilled model, including the knowledge about how to generalize that is learned from translated training data even though the transfer set does not contain any translations.
- When the distilled net had 300 or more units in each of its two hidden layers, all temperatures above 8 gave fairly similar results
- But when this was radically reduced to 30 units per layer, temperatures in the range 2.5 to 4 worked significantly better than higher or lower temperatures.

## Automatic [Speech Recognition](Speech Recognition.md)
- State-of-the-art ASR systems currently use DNNs to map a (short) temporal context of features derived from the waveform to a probability distribution over the discrete states of a Hidden Markov Model (HMM)
- DNN produces a probability distribution over clusters of tri-phone states at each time and a decoder then finds a path through the HMM states that is the best compromise between using high probability states and producing a transcription that is probable under the language model.
- There is, however, another important objection to ensembles: If the individual models are large neural networks and the dataset is very large, the amount of computation required at training time is excessive, even though it is easy to parallelize.

## JFT
- JFT is an internal Google dataset that has 100 million labeled images with 15,000 labels. When we did this work, Google’s baseline model for JFT was a deep convolutional neural network that had been trained for about six months using asynchronous stochastic gradient descent on a large number of cores.
- When the number of classes is very large, it makes sense for the cumbersome model to be an ensemble that contains one generalist model trained on all the data and many 'specialist' models, each of which is trained on data that is highly enriched in examples from a very confusable subset of the classes (like different types of mushroom)
- The softmax of this type of specialist can be made much smaller by combining all of the classes it does not care about into a single dustbin class.
- To reduce overfitting and share the work of learning lower level feature detectors, each specialist model is initialized with the weights of the generalist model
- These weights are then slightly modified by training the specialist with half its examples coming from its special subset and half sampled at random from the remainder of the training set. After training, we can correct for the biased training set by incrementing the logit of the dustbin class by the log of the proportion by which the specialist class is oversampled.
- In order to derive groupings of object categories for the specialists, we decided to focus on categories that our full network often confuses.
- Even though we could have computed the confusion matrix and used it as a way to find such clusters, we opted for a simpler approach that does not require the true labels to construct the clusters. In particular, we apply a [clustering] algorithm to the [covariance](clustering] algorithm to the [covariance.md) matrix of the predictions of our generalist model, so that a set of classes Sm that are often predicted together will be used as targets for one of our specialist models, m.
- on-line version of the K-means algorithm to the columns of the [Covariance](Covariance.md) matrix, and obtained reasonable clusters
- One of our main claims about using soft targets instead of hard targets is that a lot of helpful information can be carried in soft targets that could not possibly be encoded with a single hard target.
- It is even more remarkable to note that we did not have to do early stopping: the system with soft targets simply 'converged' to 57%. This shows that soft targets are a very effective way of communicating the regularities discovered by a model trained on all of the data to another model.
- The specialists that we used in our experiments on the JFT dataset collapsed all of their non-specialist classes into a single dustbin class. If we allow specialists to have a full softmax over all classes, there may be a much better way to prevent them overfitting than using early stopping. A specialist is trained on data that is highly enriched in its special classes.
- This means that the effective size of its training set is much smaller and it has a strong tendency to overfit on its special classes.
- The use of specialists that are trained on subsets of the data has some resemblance to mixtures of experts which use a gating network to compute the probability of assigning each example to each expert
- At the same time as the experts are learning to deal with the examples assigned to them, the gating network is learning to choose which experts to assign each example to based on the relative discriminative performance of the experts for that example.
- Using the discriminative performance of the experts to determine the learned assignments is much better than simply [Clustering](Clustering.md) the input vectors and assigning an expert to each cluster, but it makes the training hard to parallelize: First, the weighted training set for each expert keeps changing in a way that depends on all the other experts and second, the gating network needs to compare the performance of different experts on the same example to know how to revise its assignment probabilities.

## Conclusions
- These difficulties have meant that mixtures of experts are rarely used in the regime where they might be most beneficial: tasks with huge datasets that contain distinctly different subsets.
- It is much easier to parallelize the training of multiple specialists
- e first train a generalist model and then use the confusion matrix to define the subsets that the specialists are trained on
- We have shown that distilling works very well for transferring knowledge from an ensemble or from a large highly regularized model into a smaller, distilled model.
- For really big neural networks, it can be infeasible even to train a full ensemble, but we have shown that the performance of a single really big net that has been trained for a very long time can be significantly improved by learning a large number of specialist nets, each of which learns to discriminate between the classes in a highly confusable cluster. We have not yet shown that we can distill the knowledge in the specialists back into the single large net.



