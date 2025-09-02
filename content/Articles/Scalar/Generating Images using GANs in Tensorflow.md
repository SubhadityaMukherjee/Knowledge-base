---
toc: true
title: Generating Images using GANs in Tensorflow

tags: ["article"]
date modified: 
date created: 
---
# Generating Images using GANs in Tensorflow
:::section{.abstract}
# Overview
This article explains using a Generative Adversarial Network (GAN) to generate new images of handwritten digits. A GAN is a machine-learning model consisting of a generator and a discriminator. The generator creates novel images from random, while the Discriminator attempts to prove that the images generated are fake. The GAN is trained on the MNIST dataset of handwritten digits and is evaluated by testing it on unseen data and creating new images using the generator. The final output of the GAN is a batch of images that look like handwritten digits. The article provides code for reading the dataset, creating the required architecture, computing loss functions, training the network, and testing the network.

:::
:::section{.scope}
# Scope
- The article provides a general overview of Generative Adversarial Networks (GANs) and their use in image generation.
- The specific goal of the article is to demonstrate how to create a GAN from scratch using the Tensorflow library and train it on the MNIST dataset to generate new images of handwritten digits.
- The article explains the architecture and components of a GAN, including the generator and Discriminator.
- The article also provides code for reading and preprocessing the MNIST dataset, creating the GAN architecture, computing loss functions, training the network, and testing the network.
- The article also discusses the final output of the GAN, which should be a batch of images that look like handwritten digits.

:::
:::section{.main}

## What are we building?
Creating novel images given an image dataset is one of the strengths of a specific branch of models called Generative Adversarial Networks (GAN). These networks specialize in unsupervised/semi-supervised image generation given any image data. 
This article uses the GANs image generation ability to create novel handwritten digits. We perform this generation by training the network on a dataset of handwritten digits. We will create a simple GAN from scratch using the Tensorflow library, train it on the MNIST dataset and generate new images of handwritten digits. 

## Pre-requisites

#### What are GANs
GANs, or Generative Adversarial Networks, are a family of networks used for unsupervised image generation, converting between images to another, and many other applications. They are composed of two parts - a Generator and a Discriminator. The Generator creates novel images from random. The Discriminator attempts to prove that the images generated are fake. This game leads to a training approach dubbed "Adversarial Learning". This article focuses on implementing a GAN and its image-generation ability to create new handwritten digits.

### How are we going to build this?
In this article, we focus on the GAN's image generation ability. To let the GAN learn about images, we must first load an image dataset and preprocess it. After loading the data, we must create the GAN and write the training and testing code. The below sections focus on implementing these features and generating new images from the MNIST dataset.

### Final Output 
The final output we want should be a batch of images that look like handwritten digits. The image shown below is what we get after training the GAN for 10000 epochs on the MNIST dataset.

[IMAGE {1} { Final results } START SAMPLE]
![Final results](https://hackmd.io/_uploads/Bk6rgIRuo.png)
[IMAGE {1} FINISH SAMPLE]

## Requirements (List the libraries, modules, and other requirements needed for the project)
Before creating the GAN's image generation module, we must import a few libraries. We will import all the functions, layers and dataset loaders from *Tensorflow*. We will also import *numpy* (a math library) and *matplotlib* (a plotting library). 

We also need to set up some that will make up our configuration for running the module. The shape of the image is defined as a matrix of 28x28x1. The last dimension corresponds to the number of channels in an image. Since we are using the MNIST dataset in black and white, we only have a single channel.

The *zsize* is the shape of the latent space we want to generate. In this case, we set it to 100. This number could be modified if required. 

```python
from __future__ import print_function, division

from keras.datasets import mnist
from keras.layers import Input, Dense, Reshape, Flatten, [[../../Dropout.md|Dropout.md|../../Dropout|Dropout]]
from keras.layers import BatchNormalization, Activation, ZeroPadding2D
from keras.layers import LeakyReLU
from keras.layers.convolutional import UpSampling2D, Conv2D
from keras.models import Sequential, Model
from keras. optimizers import Adam, SGD

import matplotlib.pyplot as plt
import sys
import numpy as np

num_rows = 28
num_cols = 28
num_channels = 1
input_shape = (num_rows, num_cols, num_channels)
z_size = 100
```

## Building the Model
The GAN we want to create comprises two major parts - The Generator and the Discriminator. The Generator is responsible for creating novel images, while the Discriminator is responsible for understanding how good the generated image is. 
The entire architecture we want to build for the GANs image generation is shown in the following diagram.

[IMAGE {2} { Architecture Diagram } START SAMPLE]
![Architecture Diagram](https://hackmd.io/_uploads/SkB31LCui.jpg)
[IMAGE {2} FINISH SAMPLE]

The sections below explain how to read a dataset, create the required architecture, compute the loss functions and train the network. Finally, the code to test the network and create new images is also shown.

### Reading the dataset

This article will use the **MNIST** (Modified National Institute of Standards and Technology) dataset. This dataset has a larger number of handwritten digits of 28x28 and is one of the most widely used datasets in computer vision. The MNIST is an easy dataset for a GAN such as the one we are building, as it has small, single channels images. 
A sample of the dataset is shown below.

We only need to write a little code to load the MNIST dataset as Tensorflow comes with it inbuilt. After loading the dataset, we normalize it and then reshape it to 3 dimensions. This reshaping enables the GAN architecture to use this 2D data. We also pre-allocate some memory for our training and validation data. 

```python
(train_ims, _), (_, _) = mnist.load_data()
train_ims = train_ims / 127.5 - 1.
train_ims = np.expand_dims(train_ims, axis=3)

valid = np.ones((batch_size, 1))
fake = np.zeros((batch_size, 1))
```

### Defining the Generator

[IMAGE {3} { Generator And Discriminator } START SAMPLE]
![Generator And Discriminator](https://hackmd.io/_uploads/SJJYWLC_j.jpg)
[IMAGE {3} FINISH SAMPLE]


The job of the Generator (D) is to create realistic images that the Discriminator fails to understand are fake. Thus, the Generator is an essential component that enables a GANs image generation ability. The architecture we consider in this article comprises fully connected layers (FC) and Leaky ReLU activations. The final layer of the Generator has a TanH activation rather than a LeakyReLU. This replacement was done because we wanted to convert the generated image to the same range as the original MNIST dataset (-1,1).

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

### Defining the Discriminator
The GAN uses the Discriminator (D) to identify how real the Generator's outputs look by returning a probability of real vs fake. This part of the network can be thought of as a binary classification problem. To solve this binary classification problem, we need a rather simple network composed of blocks of Fully Connect Layers (FC), Leaky ReLU activations and [[Dropout]] layers. Note that the final layer has a block with an FC layer and a Sigmoid. 
The final Sigmoid activation returns the classification probability that we require.
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

### Computing the loss function
To make the GANs image generation procedure smoother, we need to supply it with metrics that show how well it is performing now. Loss functions do just that.

The Discriminator classifies the generated images into real or fake and returns the probability of it being real. To make this distinction, it needs to ensure that the input it receives is part of the real dataset. And if the input received is fake, it is not classified as part of the real dataset.
We can mathematically understand this difference as **maximizing** $D(x)$ and **minimizing** $D(G(z))$.

Building on these concepts, the Generator is tasked with fooling the Discriminator by creating realistic images. We can understand this procedure as ensuring that when the Discriminator gets an image sampled from the fake dataset, it thinks that the image belongs to the real dataset instead.
We can mathematically understand this procedure as **maximizing** $D(G(z))$. It is to be. Note that just using this part of the formulae as a loss function sometimes makes the network confident about the wrong outputs. To prevent this assumption, we use $log(D(G(z)))$ instead.

The net cost function for the GAN's image generation can be thus mathematically represented as $$\underset{G}{min} \underset{D}{max} V(D, G) = \mathbb{E}_{x \sim p_{data}(x)}[log(D(x)] + \mathbb{E}_{z \sim p_{z}}[log(1 - D(G(z))]$$

Training a GAN such as this is a delicate balance and can be considered a game between two enemies. (Hence the name - **Adversarial Learning**.) Since either party attempts to influence the opposition and reduce the others' chance of winning, this is a **MinMax game**.

We can then create the Generator and Discriminator with a **Binary Crossentropy loss**.
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

### Optimizing the loss
To train the network, we need the GAN to play the **MinMax game**. The training procedure hinges on performing Gradient Descent on the network weights. To reduce the training time and ensure that the training does not get stuck on the loss landscape, we use a Stochastic version of GD, aka **Stochastic Gradient Descent**. 
Both the Discriminator and the Generator have *different* losses. If We gave both these networks a single loss function, they would not be able to optimize each other. 
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
    return disc, Generator, and combined
```

Having defined all the required functions, we can train the network to optimize the losses. The steps we follow for the GAN's image generation are as follows.
- Load an image, and generate random noise of the same size as the loaded image.
- Send these images to the Discriminator and calculate the real vs fake probability for the same.
- Generate another noise of the same size. Send this noise to the Generator.
- Run training for the Generator for a few epochs.
- Repeat all the steps until a satisfactory image is generated.

These steps are directly translated into the code shown below.

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
```

### Generating handwritten digits
Finally, we can generate handwritten digits from the MNIST dataset. To look at how far the network has trained the images, we create a helper function to store predictions from the Generator for a batch of images. This function creates random noise, passes them to the Generator, processes it for displaying and then saves it to a folder. We run this helper function every 200 epochs.

```python
def one_batch(epoch):
    r, c = 5, 5
    noise = np.random.normal(0, 1, (r * c, z_size))
    gen_imgs = gen.predict(noise)

    # Rescale images 0 - 1
    gen_imgs = 0.5 * gen_imgs + 0.5

    fig, axs = plt.subplots(r, c)
    cnt = 0
    for i in range(r):
        for j in range(c):
            axs[i,j].imshow(gen_imgs[cnt, :,:,0], cmap='gray')
            axs[i,j].axis('off')
            cnt += 1
    fig.savefig("images/%d.png" % epoch)
    plt.close()
```

For this article, we trained the GAN for around 10,000 epochs with a batch size of 32. We save the generated images every 200 epochs in the images folder.
```python
disc, gen, full_model = intialize_model()
train(epochs=10000, batch_size=32, sample_interval=200)
```
We can now look at the results of the GAN's image generation at the start, at 400 epochs, at 5000 epochs and the final result at 10000 epochs.

At the start, we have random noise.
[IMAGE {4} { Epoch 0 } START SAMPLE]
![Epoch 0](https://hackmd.io/_uploads/Sk-zl8COo.png)
[IMAGE {4} FINISH SAMPLE]


After 400 epochs, we are getting somewhere slowly. But these results are different from real digits.
[IMAGE {5} { Epoch 400 } START SAMPLE]
![Epoch 400](https://hackmd.io/_uploads/SJxNgI0_j.png)
[IMAGE {5} FINISH SAMPLE]


After 5000 epochs, we can see figures that resemble the MNIST dataset.
[IMAGE {6} { Epoch 5000 } START SAMPLE]
![Epoch 5000](https://hackmd.io/_uploads/rJbSgIRui.png)
[IMAGE {6} FINISH SAMPLE]


After training the network for the entire 10,000 epochs, we get the following outputs. 
[IMAGE {7} { Final results } START SAMPLE]
![Final results](https://hackmd.io/_uploads/Bk6rgIRuo.png)
[IMAGE {7} FINISH SAMPLE]

These images look very close to the handwritten number data we fed the network. These images were not shown to the network during training and were generated from scratch.

## What's next
The output we got from the GANs image generation is good, but there are many ways we can improve it. Without leaving the scope of this article, we can experiment with a few parameters. Some of them are as follows:
- Try different values of the latent space variable *z_size* to see if the performance improves.
- Try training the model for a larger number of epochs. We trained it for 10000; try doubling or tripling that to see if the results improve or worsen.
- Try different datasets such as the [Fashion MNIST](https://www.kaggle.com/datasets/zalando-research/fashionmnist) or the [Moving MNIST](https://paperswithcode.com/dataset/moving-mnist). These datasets follow the same structure as the MNIST, making it possible to use the code we wrote directly.
- Finally, it is worth experimenting with other architectures such as CycleGAN, DCGAN etc. Many of them would only require changing the functions of the Generator and Discriminator.

:::
:::section{.summary}

# Conclusion

- GANs are machine learning models that can generate new images from a dataset.
- In this article, a simple GAN is created using the Tensorflow library and trained on the MNIST dataset.
- The GAN comprises two parts: a Generator that creates novel images from random and a Discriminator that attempts to prove that the images generated are fake.
- The final output is a batch of images that look like handwritten digits, as shown in the example image provided.
- The GAN is trained by supplying it with metrics and loss functions that show how well it correctly classifies real and fake images. 
- The GAN is then evaluated by testing it on unseen data and creating new images using the generator.


:::



