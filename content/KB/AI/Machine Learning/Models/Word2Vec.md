---
toc: true
title: Word2Vec

tags: ['architecture']
date modified: Thursday, December 8th 2022, 12:15:44 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Word2Vec
- [Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/abs/1301.3781)
- Duality of vector representations of words derived by various models on a collection of syntactic and semantic language tasks involving word similarity
- possible to train high quality [Word Vectors](Word%20Vectors.md) using very simple model architectures
- [Skip Gram] or [CBOW](Skip Gram] or [CBOW.md)

## Training
- Ask it to predict a vector with probabilities
- Find error vector
- Update params
- to generate high-quality embeddings using a high-performance model, we can switch the model’s task from predicting a neighboring word And switch it to a model that takes the input and output word, and outputs a score indicating if they’re neighbors or not (0 for “not neighbors”, 1 for “neighbors”).
- This simple switch changes the model we need from a neural network, to a logistic regression model – thus it becomes much simpler and much faster to calculate. + [Negative Sampling](Negative Sampling.md)
- Embedding and Context matrices randomly initialized
- ![](../images/Pasted%20image%2020221208001319.png)
- ![](../images/Pasted%20image%2020221208001413.png)

## Hyperparams

### Window Size
- smaller window sizes (2-15) lead to embeddings where high similarity scores between two embeddings indicates that the words are _interchangeable_ (notice that antonyms are often interchangable if we’re only looking at their surrounding words – e.g. _good_ and _bad_ often appear in similar contexts).
- Larger window sizes (15-50, or even more) lead to embeddings where similarity is more indicative of _relatedness_ of the words
- default is 5 (two words - word - two words)

### No of Negative Samples
- The original paper prescribes 5-20 as being a good number of negative samples. It also states that 2-5 seems to be enough when you have a large enough dataset. The Gensim default is 5 negative samples.



