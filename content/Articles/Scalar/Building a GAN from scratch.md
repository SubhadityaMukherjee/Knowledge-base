
---
toc: true
title: Building a GAN from scratch

tags: ["article"]
date modified: 
date created: 
---
# Building a GAN from scratch 

:::section{.abstract}

## Overview
Generating images from scratch is a huge deal in computer vision. A **Generative Adversarial Network**(GAN) was one of the first models to generate new images in an unsupervised manner efficiently. A GAN is not a single model but a family of different architectures used for image generation.

This article will look at the first Generative Adversarial Network, a **vanilla GAN**. We will learn how to make a Generative Adversarial Network from scratch.
:::
:::section{.scope}

## Scope
This article covers the following topics:
- What is a Generative Adversarial Network, and how to make a Generative Adversarial Network from scratch?
- What is the architecture of a GAN, and what are the loss functions and optimizers required to train one?
- How to feed a custom dataset to a GAN and use it to generate novel images.

:::
:::section{.main}


## Introduction
A GAN is a network we can use to create novel images given any vision dataset. In most cases, they are unsupervised, but many architectures also consider labels during training. Some examples of outputs GANs are shown here.

[IMAGE {1} Summer to Winter START SAMPLE]
![Summer to Winter](https://hackmd.io/_uploads/r13OxIA_o.png)
[IMAGE {1} FINISH SAMPLE]

[IMAGE {2} Face Generation START SAMPLE]
![Face Generation](https://hackmd.io/_uploads/Hk6FgLRdo.png)
[IMAGE {2} FINISH SAMPLE]


GANs have much bigger and more complex architectural pipelines than a standard Convolutional network. They generally have two major structures, the Generator and the Discriminator. These structures are Convolutional networks that we can substitute for other networks that perform similar functions. 

The training paradigm for GANs is called **Adversarial Training** and relies on an interplay between the Generator and the Discriminator. 

This article will look at what a Generative Adversarial Network is and its components. After we understand the parts, we will build our own GAN from scratch and train it on a dataset of handwritten images (MNIST). 

## Architecture of a GAN
One of the hardest parts of understanding how to make a Generative Adversarial Network is comprehending the architecture. GANs are very different from regular neural networks in that they are composed of two completely different neural networks - The Generator and the Discriminator.

Consider the architecture diagram shown below.
[IMAGE {3} Architecture Diagram START SAMPLE]
![Architecture Diagram](https://hackmd.io/_uploads/SkB31LCui.jpg)
[IMAGE {3} FINISH SAMPLE]


The first part of the architecture is the Generator, whose job is to create images realistic enough that the Discriminator cannot tell the difference between a fake image and a real one.

[IMAGE {4} Generator And Discriminator START SAMPLE]
![Generator And Discriminator](https://hackmd.io/_uploads/SJJYWLC_j.jpg)
[IMAGE {4} FINISH SAMPLE]



### Generator
The Generator can be considered a network that takes a random noise and then arranges the pixels to make it look like a real image. It is also a simple neural network composed of blocks of fully connected linear layers (FC) and Leaky ReLU activations. In the final layer of the Generator, the LeakyReLU is replaced by a Tanh activation. The Tanh activation is chosen as we do not want probabilities but want to take the generated image and squish it to the range of (-1,1). This range is the range of the MNIST data images.

### Discriminator

The second part of the network is the Discriminator, whose job is to take the images that the Generator creates and return the probability that the image is real. 
The Discriminator is a binary classifier and comprises blocks of fully connected linear layers (FC), Leaky ReLU activations, and [Dropout](../../KB/Dropout.md) layers. The final layer of the Discriminator is a block with an FC layer and a Sigmoid at the end. The Sigmoid is responsible for returning the classification probability that we want.

## Demystifying the loss function
Loss functions are an essential part of any neural network pipeline. Before we learn how to make a Generative Adversarial Network, we first need to understand the loss functions.

### Discriminator loss
The Discriminator's job is to classify the generated images into real or fake and return the probability that it is real. To do so, it needs to do extremely well at ensuring that the input it gets belongs to the real dataset. It should also ensure that if the input is fake, it is not classified as belonging to the real dataset. 
Mathematically, this can be understood as **maximizing** $D(x)$ and **minimizing** $D(G(z))$.

### Generator loss
The Generator is tasked with ensuring that the Discriminator is fooled. It can do so by creating realistic images that the Discriminator thinks are real. This process can be thought of as ensuring that the Discriminator classifies an image sampled from the fake dataset as belonging to the real one. 
Mathematically, this is formulated as **maximizing** $D(G(z))$.
Using this as the loss might lead to the network becoming extremely confident, even if it is wrong. To prevent this from happening, $log(D(G(z)))$ is used instead. 

### Total loss
There is no net loss that is used in practice. Still, while learning to make a Generative Adversarial Network, we must consider the total theoretical loss the network is trying to optimize.
Training a Generative Adversarial Network is a game between two enemies (aka adversaries). In other words, this is a MinMax game where one party attempts to reduce the probability of the other winning. Both parties are simultaneously also trying to increase their chances of winning.
Mathematically, this can be represented as $$\underset{G}{min} \underset{D}{max} V(D,G) = \mathbb{E}_{x \sim p_{data}(x)}[log(D(x)] + \mathbb{E}_{z \sim p_{z}}[log(1 - D(G(z))]$$

### Heuristic loss
Another aspect of knowing how to make a Generative Adversarial Network is understanding heuristics. These heuristics are not part of any network directly but are training guidelines that work for most GANs. (Any GAN created before 2016, at least.)
We can use these heuristics to ensure stable reductions in the loss landscape, which is key to training a Generative Adversarial Network well.
- If the network has any pooling layers, they can be replaced with [Strided](../../KB/Strided.md) convolutions in the Generator.
- We can use Batch Normalization layers in the Generator and the Discriminator.
- If the architecture is deep, we should remove FC layers for better performance.
- As for activations, the ReLU activation should be used for all the layers. The only exception is the output layer, where a TanH activation should be used.

## Training a GAN
We need an optimization algorithm that performs gradient descent on the network weights to train the GAN. The SGD (Stochastic Gradient Descent) algorithm is used for a vanilla GAN such as ours. The Generator and the Discriminator are assigned to their SGD optimizer for training. This procedure ensures that they both learn independent weights. Since the outputs of both networks flow to and from each other, they are influenced by each other as well.

The general training paradigm for any GAN is as follows. This paradigm is always a good place to refer to when figuring out how to build a Generative Adversarial Network.
- Obtain an image, and create a random noise of the same size as the image. 
- Pass these images to the Discriminator and obtain the probability of the image passed being real or fake.
- Create another noise of the same size as before, and pass it to the Generator.
- Train the Generator with this input data.
- Repeat all the previous steps until the weights are successfully optimized and satisfactory results are obtained. 

## Coding a GAN
In this article, we will create a GAN that can create novel handwritten digits every time it is called. We will take all the concepts we have learnt and, finally, learn how to make a Generative Adversarial Network in Python using the Tensorflow library. Before actually building the network and training pipeline, we need to choose a dataset and set up the optimizers and loss functions. 
After the initial set-up is completed, we can train the network and generate our handwritten digits (or any other data).

## Imports
First, we import all the required libraries. We will import the plotting library matplotlib and the numerical processing library numpy. In this case, we will import all the required functions from Tensorflow.
```python
from __future__ import print_function, division

from keras.datasets import mnist
from keras.layers import Input, Dense, Reshape, Flatten, [[../../Dropout.md|Dropout.md|../../Dropout|Dropout]]
from keras.layers import BatchNormalization, Activation, ZeroPadding2D
from keras.layers import LeakyReLU
from keras.layers.convolutional import UpSampling2D, Conv2D
from keras.models import Sequential, Model
from keras.optimizers import Adam, SGD

import matplotlib.pyplot as plt
import sys
import numpy as np
```

### Setup Configuration
To further understand how to make a Generative Adversarial Network, we need to explore our configuration options.
We first define the size of the image we want to load and generate. Since we are using the MNIST dataset, we set this to 28x28.
The MNIST dataset is grayscale, and this only has one channel.
We can set the size of the latent space to 100. If the dataset was more complex, We could choose a higher number.

```python
num_rows = 28
num_cols = 28
num_channels = 1
input_shape = (num_rows, num_cols, num_channels)
z_size = 100
opt = SGD()
```

## Dataset
The dataset we use in this article is the *Modified National Institute of Standards and Technology database* or **MNIST**. It is a dataset of handwritten digits almost ubiquitous in deep learning. A sample of this dataset is shown below. 
[IMAGE {5} MNIST START SAMPLE]
![MNIST](https://hackmd.io/_uploads/B1q0kI0di.jpg)
[IMAGE {5} FINISH SAMPLE]

The MNIST is a very simple dataset for modern networks to model, so it is a good challenge for our vanilla GAN.

The MNIST dataset comes pre-installed with Keras, and we can directly use it. We need to pre-process the images by normalizing them and converting them to 3 dimensions to pass them to the network (a Generative Adversarial Network cannot directly process 2D images without changing the architecture). We also create proxy containers for the real and fake images to save memory during training.

```python
(train_ims, _), (_, _) = mnist.load_data()
train_ims = train_ims / 127.5 - 1.
train_ims = np.expand_dims(train_ims, axis=3)

valid = np.ones((batch_size, 1))
fake = np.zeros((batch_size, 1))
```

## Networks
We now look at the network architecture to understand how to make a Generative Adversarial Network from scratch. 

### Discriminator
To create the Discriminator, we define a function that returns a model with the network defined. This function does not compile the model as we need to call it multiple times, and pre-compiling it will lead to issues when we do.

```python
def build_discriminator():

	disc_model = Sequential()
	disc_model.add(Flatten(input_shape=input_shape))
	disc_model.add(Dense(512))
	disc_model.add(LeakyReLU(alpha=0.2))
	disc_model.add(Dense(256))
	disc_model.add(LeakyReLU(alpha=0.2))
	disc_model.add(Dense(1, activation='sigmoid'))
	
	disc_img = Input(shape=input_shape)
	validity = disc_model(disc_img)
	return Model(disc_img, validity)
```

### Generator
The Generator is built similarly to the Discriminator. We define a custom function to create the Generator but do not compile it for now. The noise is also generated and passed through the network here.

```python
def build_generator():

    gen_model = Sequential()
    gen_model.add(Dense(256, input_dim=z_size))
    gen_model.add(LeakyReLU(alpha=0.2))
    gen_model.add(BatchNormalization(momentum=0.8))
    gen_model.add(Dense(512))
    gen_model.add(LeakyReLU(alpha=0.2))
    gen_model.add(BatchNormalization(momentum=0.8))
    gen_model.add(Dense(1024))
    gen_model.add(LeakyReLU(alpha=0.2))
    gen_model.add(BatchNormalization(momentum=0.8))
    gen_model.add(Dense(np.prod(input_shape), activation='tanh'))
    gen_model.add(Reshape(input_shape))

    gen_noise = Input(shape=(z_size,))
    gen_img = gen_model(gen_noise)
    return Model(gen_noise, gen_img)
```

## Optimization
We define the following functions to set up the optimizers for both networks. We will be using an SGD optimizer in this case for both models.

```python
# discriminator
disc= build_discriminator()
disc.compile(loss='binary_crossentropy',
    optimizer='sgd',
    metrics=['accuracy'])

z = Input(shape=(z_size,))
# generator
img = generator(z)

disc.trainable = False

validity = disc(img)

# combined model
combined = Model(z, validity)
combined.compile(loss='binary_crossentropy', optimizer='sgd')
```

## Training
Before we can train, we need to define a few utility functions.
The first function sets up both the Generator and the Discriminator for training. It compiles the combined model and also creates noise.

```python
def intialize_model():
    disc= build_discriminator()
    disc.compile(loss='binary_crossentropy',
        optimizer='sgd',
        metrics=['accuracy'])

    generator = build_generator()

    z = Input(shape=(z_size,))
    img = generator(z)

    disc.trainable = False

    validity = disc(img)

    combined = Model(z, validity)
    combined.compile(loss='binary_crossentropy', optimizer='sgd')
    return disc, generator, combined
```


The entire training loop is then as follows. This loop follows the exact procedure described in previous sections.
We also add a running counter that tells us how far along we are in training and saves the outputs every *sample_interval* epochs.

```python
def train(epochs, batch_size=128, sample_interval=50):
    # load images	
    (train_ims, _), (_, _) = mnist.load_data()
    # preprocess
    train_ims = train_ims / 127.5 - 1.
    train_ims = np.expand_dims(train_ims, axis=3)

    valid = np.ones((batch_size, 1))
    fake = np.zeros((batch_size, 1))
    # training loop
    for epoch in range(epochs):

        batch_index = np.random.randint(0, train_ims.shape[0], batch_size)
        imgs = train_ims[batch_index]
    # create noise
        noise = np.random.normal(0, 1, (batch_size, z_size))
    # predict using Generator
        gen_imgs = gen.predict(noise)
    # calculate loss functions
        real_disc_loss = disc.train_on_batch(imgs, valid)
        fake_disc_loss = disc.train_on_batch(gen_imgs, fake)
        disc_loss_total = 0.5 * np.add(real_disc_loss, fake_disc_loss)

        noise = np.random.normal(0, 1, (batch_size, z_size))

        g_loss = full_model.train_on_batch(noise, valid)
    # show progress
        print ("%d [D loss: %f, acc.: %.2f%%] [G loss: %f]" % (epoch, disc_loss_total[0], 100*disc_loss_total[1], g_loss))
    # save outputs every few epochs
        if epoch % sample_interval == 0:
            one_batch(epoch)
disc, gen, full_model = intialize_model()
train(epochs=10000, batch_size=32, sample_interval=200)
```

After defining these functions, we train it for as many epochs as we want. For the sake of this article, we can train it for 10,000 epochs. Longer epochs do not necessarily mean better performance.

## Testing
We also need a function that samples a batch of data to generate images on demand during/after training.
This function creates a random noise vector and uses the trained Generator to perform a prediction on the noise. The generated images are then plotted for a batch of images.

```python
def one_batch(epoch):
    row, col = 5, 5
    noise = np.random.normal(0, 1, (r * c, z_size))
    gen_imgs = gen.predict(noise)

    # Rescale images 0 - 1
    gen_imgs = .5 * gen_imgs + .5

    fig, axs = plt.subplots(r, c)
    cnt_axis = 0
    plt.cla()
    plt.clf()
    for i in range(row):
        for j in range(col):
            axs[i,j].imshow(gen_imgs[cnt_axis, :,:,0], cmap='gray')
            axs[i,j].axis('off')
            cnt_axis += 1
    fig.savefig("images/%d.png" % epoch)
    plt.close()
```

In the training loop, if the number of passed epochs is a multiple of the sample interval (how many epochs to skip before saving the outputs), we call this function and save the images.
We can also do this later on.

```python
if epoch % sample_interval == 0:
    one_batch(epoch)
```

## Results
The code we wrote saves images at an interval of 200 epochs. For clarity, we can look at the images generated at the start, at 400 epochs, at 5000 epochs and finally after 10,000 epochs.

At the start, we have random noise.
[IMAGE {6} Epoch 0 START SAMPLE]
![Epoch 0](https://hackmd.io/_uploads/Sk-zl8COo.png)
[IMAGE {6} FINISH SAMPLE]


After 400 epochs, we are getting somewhere slowly. But these results are different from real digits.
[IMAGE {7} Epoch 400 START SAMPLE]
![Epoch 400](https://hackmd.io/_uploads/SJxNgI0_j.png)
[IMAGE {7} FINISH SAMPLE]


After 5000 epochs, we can see figures that resemble the MNIST dataset.
[IMAGE {8} Epoch 5000 START SAMPLE]
![Epoch 5000](https://hackmd.io/_uploads/rJbSgIRui.png)
[IMAGE {8} FINISH SAMPLE]


After training the network for the entire 10,000 epochs, we get the following outputs. 
[IMAGE {9} Final results START SAMPLE]
![Final results](https://hackmd.io/_uploads/Bk6rgIRuo.png)
[IMAGE {9} FINISH SAMPLE]


These images look very close to the handwritten number data we fed the network. Note that none of these exact images was previously shown to the network, and the network generated these as we trained it.
:::
:::section{.summary}

## Conclusion
- This article taught us how to make a Generative Adversarial Network from scratch.
- We looked at the architecture of a vanilla GAN and understood the loss functions required to train it.
- We also made our own Generative Adversarial Network in Python and trained it on MNIST data.
- Finally, we looked at the stepwise results we obtained from training our GAN.
:::



