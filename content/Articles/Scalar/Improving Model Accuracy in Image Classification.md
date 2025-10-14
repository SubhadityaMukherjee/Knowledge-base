
---
toc: true
title: Improving Model Accuracy in Image Classification

tags: ["article"]
date modified: 
date created: 
---
# Improving Model Accuracy in Image Classification

:::section{.abstract}

## Overview
Improving image classification accuracy is one of the biggest hurdles in deep learning. Apart from using a deeper network and better data, many techniques have been developed to optimize network performance. Some techniques, such as **[Dropout](../../KB/Dropout.md)**, are more focused on improving the overall pipeline. 
:::
:::section{.scope}

## Scope
- This article explains the concepts of **Overfitting** and **Underfitting**.
- **Dropout** and other **[Regularization](../../KB/Regularization.md)** techniques like **Data Augmentation** are explained.
- The article also explains **Early Stopping** and other pipeline tweaks such as **Hyperparameter Tuning** and **Transfer Learning**.

:::
:::section{.main}

## Introduction
It is often impossible to always have better data or larger models. In such cases, using techniques like [Regularization](../../KB/Regularization.md) and Early Stopping tackle the challenges of Overfitting. 
This article provides an introduction to many such algorithms and pipeline tweaks that help in the process of improving model accuracy in image classification.

## Improving Model Accuracy
The two biggest hurdles in training neural networks are **Overfitting** and **Underfitting**. In the first case, the network memories the data, and in the second, the network does not learn enough. The following techniques can be divided into categories based on these two concepts.
[Dropout](../../KB/Dropout.md), Early Stopping, tackle **Overfitting**.  Transfer Learning and Hyperparameter Tuning tackle **Underfitting**.
If there is a lack of data, we can use Transfer learning and Data Augmentation. The other algorithms can be experimented with if the model does not perform well.
The below sections explain all of these algorithms.

### Overfitting and Underfitting
Training a neural network is a balancing act that requires understanding many metrics. 
Training accuracy is defined as the model's accuracy during training time on the train/test split of the data. 
Validation accuracy is defined as the model's performance when tested on real-world data that the model has never seen.
If, in improving image classification accuracy, the training accuracy is far higher than the validation accuracy for many epochs, this is called Overfitting. In Overfitting, the model focuses too heavily on the training data and essentially fails to predict any sample it has yet to see before. 

If the training accuracy is very low and the validation accuracy seems to fluctuate or is much higher than the training accuracy, this is called Underfitting. In Underfitting, the model must be more powerful to fit the data. 
Both Overfitting and Underfitting can be countered in many ways, but it is to be noted that they have a delicate balance. Learning to understand which of these the network is going through is essential in being able to improve image classification accuracy.

[IMAGE {1} Overfitting_Underfitting START SAMPLE]
![Overfitting_Underfitting](https://hackmd.io/_uploads/SJisbIE5j.png)
[IMAGE {1} FINISH SAMPLE]


### [Dropout](../../KB/Dropout.md) layers

When the single unit in a network computes gradients wrt the error, it also considers the other units and tries to fix their mistakes. This dependency is known as Co Adaptation and leads to the formation of complex relations that encourages Overfitting. [Dropout](../../KB/Dropout.md) layers reduce co-dependence between the neurons in a network by randomly (with a probability p) setting neuron activations to 0. This layer is applied to Dense (Fully connected) layers in a network.
[Dropout](../../KB/Dropout.md) can help performance as more information is recovered. Similarly, if the dataset is too large, the model performance might also worsen.
During testing, the weights are scaled by the probability p.

[IMAGE {2} Dropout START SAMPLE]
![Dropout](https://hackmd.io/_uploads/BJq2-845i.png)
[IMAGE {2} FINISH SAMPLE]


### Data Augmentation

Neural networks are extremely data-hungry, and training them requires many training examples. It is, of course, only sometimes possible to have a large amount of training data. We can use a method called Data Augmentation to artificially expand the number of available examples. In essence, Data Augmentation is the process of tweaking the given examples multiple times in different ways to generate new training samples from the existing images. Some examples of Data Augmentation for image data include Random Flipping, Jittering Brightness/Contrast, Random Resizing, and Random [Cropping](../../KB/Cropping.md).
Some Data Augmentations are shown below.

[IMAGE {3} Augmentation START SAMPLE]
![Augmentation](https://hackmd.io/_uploads/Hk_p-84cs.png)
[IMAGE {3} FINISH SAMPLE]


Data augmentation is a good method for improving image classification accuracy. This technique is not restricted to images; we can apply similar concepts to every other data domain. Data Augmentation also has the added benefit of being a regularizer by showing the model data from different perspectives.

### [Regularization](../../KB/Regularization.md)

One of the biggest challenges neural networks face during training is Overfitting. Penalizing complex models that have better performance during training but not during validation is one way of reducing the effects of Overfitting. The objective of training neural networks is for them to be used on real data outside the training set. Penalizing models that learn too much of the training set is called [Regularization](../../KB/Regularization.md) term is used to control the penalty applied to the model. This term is also a hyperparameter, as increasing it too much may hurt model performance. 
Many algorithms perform [Regularization](../../KB/Regularization.md), etc.

### Early Stopping

Early Stopping is a [Regularization](../../KB/Regularization.md) technique that improves image classification accuracy by intentionally stopping the training when validation loss increases. Training is stopped as training a model for too many epochs sometimes causes Overfitting. In Early Stopping, the number of epochs becomes a tunable hyperparameter. We continuously store the best parameters during training, and when these parameters no longer change for several epochs, we stop training. 
The idea of Early Stopping can be seen in this diagram.
[IMAGE {4} Early Stopping START SAMPLE]
![Early Stopping](https://hackmd.io/_uploads/Bkr0W849j.png)
[IMAGE {4} FINISH SAMPLE]


### Transfer Learning

Training large-scale image models are time and energy-consuming. Since most vision datasets have some common features, it is possible to take a network trained on a similar dataset and use the trained features to reduce training time on a different dataset. 
Transfer learning is a procedure that lets a pre-trained model be used either as a feature extractor or as a weight initializer. In most cases, Transfer learning is used for fine-tuning. We can transfer knowledge from a network trained on a complex task to a simpler one or from a network trained on large amounts of data to one with fewer data. 
Transfer learning is thus a potential key to multi-task learning, an active field of research in deep learning. This technique is also key in quickly improving image classification accuracy with fewer data.
The following diagram shows the concept behind using Transfer learning to improve image classification accuracy.

### Hyperparameter tuning

Every DL model and training pipeline has parameters we can tune to optimize performance. Parameters can include - how many epochs to train the network, weight decay, optimizers, learning rate, and a lot more. Each hyperparameter can have multiple values, and these quickly add up to hundreds or more different cases to try. 
Hyperparameter tuning is the art of tweaking these parameters to create an optimal model in the shortest amount of time. We can test only some parameters, but a tuning service can estimate which hyperparameter to keep and which to discard. Many algorithms enable such a service, one of them being a grid search over the hyperparameter space. If the hyperparameter in question reduces model performance, it is dropped, and sometimes similar hyperparameters are also dropped. 
Hyperparameter tuning is a challenging problem as every task requires different requirements. Tuning hundreds of parameters is a balancing act between the choices. 
This technique is one of the final bits of the pipeline that leads to improving image classification accuracy. 

:::
:::section{.summary}

# Conclusion
- In this article, we learned the importance of other algorithms in improving image classification accuracy.
- We looked at the concepts of Overfitting and Underfitting and understood how they affect model training.
- We also looked at many algorithms that improve performance by modifying the architecture or changing how we train the network.
- We understood what techniques to use when we lack data.
- We also tackled improving the existing model's performance by tuning its hyperparameters.
:::



