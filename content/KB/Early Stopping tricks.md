---
tags: ['deeplearning']
toc: true
title: Early Stopping
date modified: Thursday, January 5th 2023, 8:17:54 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Early Stopping
- No of epochs is a hyper parameter : to prevent overfitting
- Early Stopping is a [Regularization](Regularization.md) technique that improves image classification accuracy by intentionally stopping the training when validation loss increases. Training is stopped as training a model for too many epochs sometimes causes Overfitting.
- In Early Stopping, the number of epochs becomes a tunable hyperparameter. We continuously store the best parameters during training, and when these parameters no longer change for several epochs, we stop training.



