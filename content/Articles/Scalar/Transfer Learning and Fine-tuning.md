
---
toc: true
title: Transfer Learning and Fine-tuning

tags: ["article"]
date modified: 
date created: 
---
# Transfer Learning and Fine-tuning

:::section{.abstract}

## Overview
Training deep learning models requires a massive amount of labeled data. In most cases, this data needs to be made available or easier to clean up. Many approaches for working with limited data sets have been created over the years, **Transfer Learning** being one of the breakthroughs. Transfer learning enables us to **fine-tune** a model pre-trained on a large dataset on our task. 
:::
:::section{.scope}

## Scope
- This article explains the principles behind **Transfer Learning**.
- It covers the method of **fine-tuning** using a pre-trained model.
- It elaborates on the principles of **freezing and unfreezing** weights.
- The article also discusses implementing the Transfer Learning **pipeline** in Tensorflow.
:::
:::section{.main}

## Introduction
Transfer Learning is useful for smaller datasets and can be considered an intelligent weight [Initialization](../../KB/Initialization.md) scheme. Instead of randomly initializing the weights of the model like we usually do, we obtain weights from a model trained on a larger dataset. Any company/individual with the funds can train a larger model and make its weights public. After doing so, we can train these models on any other similar dataset much faster than before. 
This article explores the concept of Transfer Learning by creating a network that can identify ten different classes from the **CIFAR10** dataset by fine-tuning a model pre-trained on the **ImageNet** dataset (1000 classes). 

## Transfer Learning
In a DL pipeline, Transfer Learning is usually done when the data available is too less to train a network properly. The general approach for a Transfer Learning workflow is as follows.
- Obtain a pre-trained model on data similar to your current dataset. For example, many models are pre-trained on the **ImageNet** dataset in computer vision approaches. Since the ImageNet dataset has classes relating to real-life objects and things, models pre-trained on it already have some knowledge of the world.
- Load the model and understand its layer structure.
- **Freeze** the weights of the model. Freezing the weights sets these layers to be un-trainable and prevents them from having their existing knowledge destroyed by the Transfer Learning process.
- Append new layers to the frozen part of the model. These new layers can be trained and use the pre-trained weights to learn faster.
- Train the new model on a new dataset.

## Implementation
This article will explore how to take a model trained on ImageNet and fine-tune it on new data. We will create this implementation in Tensorflow and use the [Cats and Dogs dataset](https://www.kaggle.com/c/dogs-vs-cats) from Kaggle.

### Pre-Requisites.
Before we can fine-tune a model, we must decide what base model we need. We also need to load and preprocess the dataset. Since Transfer Learning is generally used for small datasets, we take a subset of the Cats and Dogs dataset for this example.

#### Imports
We first import the required libraries. We use Tensorflow for the entire pipeline. 
```python 
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import tensorflow_datasets as tfds
import os
import zipfile
``` 

#### Loading the Data
Since the Cats and Dogs dataset is not a part of Tensorflow, we download it from Kaggle and then use the **tensorflow_datasets** library to load it into memory.
After loading, we split the data into train and test while also sub-setting it.

```python 
train_dataset, validation_dataset, test_dataset = tfds.load(
    "cats_vs_dogs",
    split=["train[:40%]", "train[40%:50%]", "train[50%:60%]"],
    as_supervised=True,
)
```
An example subset of the data is shown below.
[IMAGE {1} CatsDogs START SAMPLE]
![CatsDogs](https://hackmd.io/_uploads/H1dHnm4co.png)
[IMAGE {1} FINISH SAMPLE]

We can then convert the data into batches, split them into data loaders, and optimize the data loading using **caching** and **pre-fetching**. We use a **batch size** of 32 for this example. After loading, we can also apply some simple data augmentation methods. For example, we use **Random Horizontal Flipping** and **Random Rotation**.

```python 
size = (150, 150)
bs = 32
aug_transforms = keras.Sequential(
    [layers.RandomFlip("horizontal"), layers.RandomRotation(0.1),]
)

train_dataset = train_dataset.map(lambda x, y: (tf.image.resize(x, size), y))
validation_dataset = validation_dataset.map(lambda x, y: (tf.image.resize(x, size), y))
test_dataset = test_dataset.map(lambda x, y: (tf.image.resize(x, size), y))


train_dataset = train_dataset.cache().batch(bs).prefetch(buffer_size=10)
validation_dataset = validation_dataset.cache().batch(bs).prefetch(buffer_size=10)
test_dataset = test_dataset.cache().batch(bs).prefetch(buffer_size=10)
```

This article uses an **[Xception](../../KB/Xception.md)** model pre-trained on the ImageNet dataset and applied to images 150x150x3 in size. The important point is to exclude the pre-trained model's final classification layer. This final layer is just for classification, and we only care about the layers before it.

```python
model_pretrained = keras.applications.Xception(
    weights="imagenet", 
    input_shape=(150, 150, 3),
    include_top=False,
)
```

The [Xception](../../KB/Xception.md) model architecture is shown here.
[IMAGE {2} arch START SAMPLE]
![arch](https://hackmd.io/_uploads/Hygq2Q4qi.png)
[IMAGE {2} FINISH SAMPLE]


### Fine-Tuning
Now, we freeze the layers of the model we just loaded by setting the trainable parameter to False.
After that, we create a model on top of the frozen layers and apply the data augmentations we defined.
The [Xception](../../KB/Xception.md) model's caveat is that it defines the inputs are scaled from the original range of (0,255) to the range of (-1.0, 1.0). We perform this rescaling using the **Rescaling** layer as follows.

```python
model_pretrained.trainable = False

inputs = keras.Input(shape=(150, 150, 3))
rescale_layer = keras.layers.Rescaling(scale=1 / 127.5, offset=-1)

x = aug_transforms(inputs) 
x = rescale_layer(x)
```

### Unfreeze the top layers of the model
The [Xception](../../KB/Xception.md)** layers to improve performance further. Global Average Pooling is an alternative to the Fully Connected layer (FC) that preserves spatial information better. Since our pre-trained model uses different data, these layers are useful here. The final layer is an FC layer for a binary classification task. 
```python 
x = model_pretrained(x, training=False)
x = keras.layers.GlobalAveragePooling2D()(x)
x = keras.layers.Dropout(0.2)(x) 

outputs = keras.layers.Dense(1)(x)
final_model = keras.Model(inputs, outputs)
```

We can now train the new layers that we created.

```python
final_model.compile(
    optimizer=keras.optimizers.Adam(),
    loss=keras.losses.BinaryCrossentropy(from_logits=True),
    metrics=[keras.metrics.BinaryAccuracy()],
)

num_epochs = 5
final_model.fit(train_dataset, epochs=num_epochs, validation_data=validation_dataset)
```

Now that we trained the new layers, we unfreeze the entire model and then train it with a very small learning rate. This gradual training leads to much better performance. Note that the **Batch Normalization** layers are not updating during this training, as if they did, it would badly hurt performance.

```python
model_pretrained.trainable = True
final_model.summary()

final_model.compile(
    optimizer=keras.optimizers.Adam(1e-5),
    loss=keras.losses.BinaryCrossentropy(from_logits=True),
    metrics=[keras.metrics.BinaryAccuracy()],
)

num_epochs = 5
final_model.fit(train_dataset, epochs=num_epochs, validation_data=validation_dataset)
```

### Evaluation and prediction
This example shows how useful Transfer Learning is for quickly training small datasets. After training the model, we evaluate the test dataset. The model still performs quite well despite the few training epochs and fewer data. 
[IMAGE {3} Results START SAMPLE]
![Results](https://hackmd.io/_uploads/rkYfp7Vcj.png)
[IMAGE {3} FINISH SAMPLE]


:::
:::section{.summary}

## Conclusion
- Transfer Learning is a powerful method when fewer data is present.
- As long as the pre-trained model uses similar data, a niche model can be fine-tuned using it.
- Selectively freezing the pre-trained layers and training the rest is a way to achieve the effects of fine-tuning.
- After an initial round of selective training, unfreezing the model and training the entire model improves performance.
- The Transfer Learning approach is thus an invaluable breakthrough in Deep Learning.
:::



