---
toc: true
title: DeepFM

tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:30 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# DeepFM
- [DeepFM: a Factorization-Machine Based Neural Network for CTR Prediction](https://arxiv.org/abs/1703.04247)
- Learning sophisticated feature interactions behind user behaviors is critical in maximizing CTR for recommender systems
- existing methods seem to have a strong bias towards low- or high-order interactions, or require expertise feature engineering
- an end-to-end learning model that emphasizes both low- and high-order feature interactions
- DeepFM is a Factorization-Machine (FM) based Neural Network for CTR prediction, to overcome the shortcomings of the state-of-the-art models and to achieve better performance.
- DeepFM trains a deep component and an FM component jointly and models low-order feature interactions through FM and models high-order feature interactions through the DNN
- DeepFM can be trained end-to-end with a shared input to its “wide” and “deep” parts, with no need of feature engineering besides raw [Features](Features.md).
- 1) it does not need any pre-training; 2) it learns both high- and low-order feature interactions; 3) it introduces a sharing strategy of feature [Embedding](Embedding.md) to avoid feature engineering
- combines the power of factorization machines for recommendation and deep learning for [Feature Learning](Feature%20Learning.md) in a new neural network architecture
- Criteo



