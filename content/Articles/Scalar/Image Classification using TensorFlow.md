---
toc: true
title: Image Classification using TensorFlow

tags: ["article"]
date modified: 
date created: 
---
# Image Classification using TensorFlow

:::section{.abstract}

## Overview 
Image Classification is one of the basic tasks in Deep Learning. Given a dataset with images of different categories, we create a Deep Learning model and a pipeline to classify these images. We can create models in any library, but Tensorflow is a good starting point for beginners, and we will use this library to create an image classifier.
:::
:::section{.main}

## What are we building?
This article will tackle a Tensorflow image classification problem by creating a neural network that can classify images from the **CIFAR10** dataset. We will explore the concepts of **Pre-Processing**, **Augmentation**, and **Performance Optimisation**. We will learn how to load a dataset, build the model and finally train the model we created using the dataset. We will also learn how to use the trained model to make predictions on custom images. 
The following sections explain these concepts and how to implement them using Tensorflow.

### Pre-requisites
Before we get to the actual code, we must understand a few pre-requisite terms. They are explained here.

#### Data Loaders
A Data Loader is a utility function that enables Tensorflow to optimize the data loading performance. The Loader does this by pre-allocating memory, creating batched containers, and applying many other tweaks to improve performance. 

#### Data Augmentation
Data Augmentation is a [[Regularization]], and many others.

[IMAGE {1} Data Augmentation  START SAMPLE]
![Data Augmentation ](https://hackmd.io/_uploads/Syb2UUV9s.png)
[IMAGE {1} FINISH SAMPLE]

#### Lambda functions
Lambda functions are special functions in Tensorflow that lets the user create functions without explicitly defining a function call. These functions are useful for improving the readability of the code and avoiding defining extra functions for single use. 

#### Map functions
In deep learning, there are many times when we need to apply a function over a batch of data. Sequentially performing these tasks is extremely time-consuming, so we use map functions to apply a function in parallel over any batch of data.

### How are we going to build this?
In this article, we will be building a Tensorflow image classification model. After loading the required libraries, we first load the data. Here, we will use the CIFAR10 dataset. After loading the data, we split it into the train, test, and validation components and then create batches of the same. To optimize performance, we will also be using caching and pre-fetching. After creating the required data loaders, we can create the model. This demo will use a ResNet50 model with the Adam optimizer and a Sparse Cross-Entropy loss function. Once we have loaded both the data and the model, we can finally train the model on the data and then evaluate its performance.
All of these steps are detailed in the sections below.

### Final Output
The final output we want is a Tensorflow image classification model that can identify the class of a given image. We want our model to learn from the CIFAR10 dataset and understand all ten classes accurately.
For example, if we pass this 64x64 image to the model, it should classify it as a horse.
[IMAGE {2} Classified Data START SAMPLE]
![Classified Data](https://hackmd.io/_uploads/SyKJPLV5j.jpg)
[IMAGE {2} FINISH SAMPLE]



## Requirements
Before creating a Tensorflow image classification model, we need to import the required modules. Apart from the base Tensorflow library, we also import the Keras package. Keras is a wrapper around Tensorflow that simplifies building neural networks. We will also import a library called Tensorflow Datasets that will enable us to load and pre-process our dataset faster.

```python 
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import tensorflow_datasets as tfds
import os
```

## Building the Classifier
We can now move on to building the classifier with the libraries we implemented. The below sections explain how to load the dataset, pre-process it, optimize it for use, and pass it to the model. We also explore how to create a model using Tensorflow and how to train it on the CIFAR10 dataset. Finally, we also learn how to evaluate a trained model on the test dataset. 

### Download and explore the dataset

For this article, we will be using the **CIFAR10** dataset. This dataset has 60000 32x32 color images grouped into ten classes. Before we create the model, we need to load and pre-process the dataset. A sample of images is shown below.

[IMAGE {3} CIFAR10 START SAMPLE]
![CIFAR10](https://hackmd.io/_uploads/HJr-DUV9i.png)
[IMAGE {3} FINISH SAMPLE]


We split the dataset into training, testing, and validation and loaded the dataset with labels using the **as_supervised** option.
To verify that we loaded the data correctly, we checked the size of the splits we had just created. If they are not zero or tiny numbers, we can know that our code has worked so far.

```python
train_dataset, validation_dataset, test_dataset = tfds.load(
    "cifar10",
    split=["train[:40%]", "train[40%:50%]", "train[50%:60%]"],
    as_supervised=True,
)

print("Number of training samples: %d" % tf.data.experimental.cardinality(train_dataset))
print(
    "Number of validation samples: %d" % tf.data.experimental.cardinality(validation_dataset)
)
print("Number of test samples: %d" % tf.data.experimental.cardinality(test_dataset))
```

### Configure the dataset for performance
Simply loading the data and passing it to the model works out of the box but leads to a sharp down in performance. We need to perform some tweaks to ensure that we use our resources optimally.
We first define our image size as 128x128x3 pixels and use a **lambda** function to resize all the images in our dataset to this image size. 
The next optimization we perform is converting the dataset into batches of 64 and informing Keras that we wish to **cache** the data and **prefetch** 10 samples. 
Prefetching data reduces the time it takes to pass the data to the memory by preallocating memory and fetching a few extra samples for the next time the model is called.
```python
size = (128, 128)
bs = 64

train_dataset = train_dataset.map(lambda x, y: (tf.image.resize(x, size), y))
validation_dataset = validation_dataset.map(lambda x, y: (tf.image.resize(x, size), y))
test_dataset = test_dataset.map(lambda x, y: (tf.image.resize(x, size), y))

train_dataset = train_dataset.cache().batch(bs).prefetch(buffer_size=10)
validation_dataset = validation_dataset.cache().batch(bs).prefetch(buffer_size=10)
test_dataset = test_dataset.cache().batch(bs).prefetch(buffer_size=10)
```

### Create the model
Since we wish to maximize performance, we also use two simple Data Augmentation techniques. The first one randomly flips the images along the horizontal axis to ensure that the model learns some spatial information. The second Augmentation we use is Random Rotation. We only want to apply this for some images, so we use a lower probability. Applying it to every image might make the model perform worse.

In this article, we use the Tensorflow image classification model ResNet50. This model uses the concept of **Skip Connections** to improve performance. We will not create the model from scratch but use the Keras implementation. To the function call, we need to pass in the weights from which we wish to use the pre-trained model. Since we are training the model from scratch here, we will pass the option as None. If we were using transfer learning, we would use the option "imagenet". We also need to pass the image size (128x128x3), the number of classes (10), and whether we want to include the whole model. This final option is only useful for transfer learning.

[IMAGE {4} Skip Connections START SAMPLE]
![Skip Connections](https://hackmd.io/_uploads/H1NQwIV5i.png)
[IMAGE {4} FINISH SAMPLE]


Once we load the model, we create an input, pass the current batch through the Augmentation, and finally, a Fully Connected (FC) layer with a size of 10 (CIFAR10 has ten classes). This final model is the one we will be used for training on our data. 
We will use the summary function to check the layers to verify if we created the model correctly.

```python
aug_transforms = keras.Sequential(
    [layers.RandomFlip("horizontal"), layers.RandomRotation(0.1),]
)

model_base = keras.applications.ResNet50(
    weights=None, 
    input_shape=(128, 128, 3),
    classes = 10,
    include_top=True
)

inputs = keras.Input(shape=(128, 128, 3))

x = aug_transforms(inputs) 
x = model_base(x, training=False)
outputs = keras.layers.Dense(10)(x)
final_model = keras.Model(inputs, outputs)
final_model.summary()
```


### Train the model
We can finally move on to training our model on the CIFAR10 data. Since we have defined our model, we need to define all the parameters required for training it.
In this article, we will use the Adam optimizer with the default parameters. We choose a Sparse Categorical Crossentropy function for the loss function as this task is a multi-class classification problem. The metric we use here is a Categorical Accuracy metric that checks how well the classifier performed across all the classes.
We will now train the model for five epochs. We can perform further training by increasing the number of epochs.

```python
final_model.compile(
    optimizer=keras.optimizers.Adam(),
    loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=[keras.metrics.SparseCategoricalAccuracy()],
)

num_epochs = 5
final_model.fit(train_dataset, epochs=num_epochs, validation_data=validation_dataset)
``` 

[IMAGE {5} Training START SAMPLE]
![Training](https://hackmd.io/_uploads/rkhNP8N9o.jpg)
[IMAGE {5} FINISH SAMPLE]


### Evaluating the Model
Five epochs are very small since we are not using transfer learning, and it is only done as a demo. After our model is done training, we can perform a full evaluation on it by performing predictions on the test dataset. While performing inference, we can increase the batch size as we are not training a network. 
We can perform this evaluation by using the evaluate function from Keras. 
```python
results = final_model.evaluate(test_dataset, batch_size=128)
print("test loss, test acc:", results)
```
A single prediction can be performed with the following code.

```python
from PIL import Image
import numpy as np
from skimage import transform
def load(filename):
   np_image = Image.open(filename)
   np_image = np.array(np_image).astype('float32')/255
   np_image = transform.resize(np_image, (256, 256, 3))
   np_image = np.expand_dims(np_image, axis=0)
   return np_image

image = load('my_file.jpg')
final_model.predict(image)
```
:::
:::section{.summary}

## Conclusion
- This article taught us how to build a Tensorflow Image Classification model.
- The article showed how to load the CIFAR10 dataset and pre-process it for training.
- It also explained how to create a simple ResNet50 model and how to train it on the CIFAR10 dataset.
- The article also explained how to evaluate the model and perform inference using the trained model.
:::



