
---
toc: true
title: DCGAN – Adding convolution to a GAN

tags: ["article"]
date modified: 
date created: 
---
# DCGAN – Adding convolution to a GAN

:::section{.abstract}

## Overview

Generative networks are a fascinating subfield of Computer vision. The GAN, in particular, is a training paradigm and a family of network architectures that convert a simple convolutional network to generate novel images based on an image dataset. This training is generally unpaired and does not require any labels. The original GAN architecture was unstable and had issues returning random noise as an output. The DCGAN was proposed as an alternative architecture with many tweaks over the original to counter issues such as **mode collapse**, **diminished gradients**, and **non-convergence**.
:::
:::section{.scope}

## Scope
- This article explains the concept of GANs and how DCGANs differ from Vanilla GANs.
- It shows how to build a DCGAN from scratch using PyTorch for image generation using the [CIFAR](../../KB/CIFAR.md) dataset.
- It explains the preprocessing and loading of the [CIFAR](../../KB/CIFAR.md) dataset using a DataLoader.
- It describes the architecture of the DCGAN and the reasoning behind the choices of layers and activation functions.
- The article also describes how to train the network, generate new images, and improve the training time and the results.



:::
:::section{.main}

## Introduction to DGGAN
This article will explore using a Deep Convolutional Generative Adversarial Network (DCGAN) to generate new images from the [CIFAR](../../KB/CIFAR.md) dataset. GANs are neural networks designed to generate new, previously unseen data similar to the input data the model trained on. DCGANs are a variation of GANs that address issues that can arise with standard GANs by using deep convolutional neural networks in both the Generator and the Discriminator.

This architecture allows larger image sizes than in standard GANs, as convolutional layers can efficiently process images with many pixels. Additionally, DCGANs use batch normalization and leaky ReLU activations in the Discriminator and transposed convolutional layers in the Generator, improving performance and stability during training.

We will use PyTorch to build the DCGAN from scratch, train it on the [CIFAR](../../KB/CIFAR.md) dataset. Before we begin, we will set up the necessary libraries and create folders to store the models' images and weights. This article will guide the implementation process and explain the reasoning for some architectural choices.


:::

:::section{.main}

## Need for DCGAN

- A simple convolutional GAN needs to be more stable to generate images with a high resolution and suffers from mode collapse. 
- DCGAN, on the other hand, has an architecture that uses not just convolutions but also transposed convolutions and other improvements. 
- These changes help the network learn better and generate images more stably compared to other architectures that came before it. 
- The DCGAN research was a monumental step for GANs as it was one of the earliest stable unsupervised image generators. 
- Understanding how it works is the gateway to creating more advanced GANs.

:::section{.main}

## Pre-requisites

To understand the DCGAN Architecture, we need to know some pre-requisite concepts. Since the entire architecture is made up of blocks of the same components, knowing them is helpful.


### Transposed Convolutions/De-Convolution

A De-Convolution is an upsampling method that uses transforms opposite to a normal convolution operation. It maintains the input's shape and pattern that a standard convolution would possess. 
[IMAGE {1} { Transposed Convolution } START SAMPLE]
![Transposed Convolution](https://hackmd.io/_uploads/H1RlJBoOi.png)
[IMAGE {1} FINISH SAMPLE]


### [Strided](../../KB/Strided.md) Convolutions

The stride in a Convolution determines how many steps the moving filter skips over in an image. In a general Convolution, the stride is set to 1. To perform [Downsampling](../../KB/Downsampling.md), we can set the stride to any number above 1. Larger numbers are only sometimes good; only experimenting with the parameter can be used to understand which to pick.
[IMAGE {2} {Strided Convolution} START SAMPLE]
![Strided Convolution](https://hackmd.io/_uploads/ByXX1Sodj.png)
[IMAGE {2} FINISH SAMPLE]


### Leaky ReLU

The Leaky ReLU activation is a small modification over the ReLU that is useful for networks with sparse gradients like the DCGAN. Due to the GAN architecture and training methodology, some nodes that use ReLU tend to die out and do nothing. The Leaky ReLU accounts for negative values by having a smaller slope instead of going straight to zero. 
The change is quite minor but makes a huge difference. While the ReLU is defined as $max(0, x)$, the Leaky ReLU is $max(0,01x, x)$

[IMAGE {3} {Leaky ReLU} START SAMPLE]
![Leaky ReLU](https://hackmd.io/_uploads/S1j4yBsus.png)
[IMAGE {3} FINISH SAMPLE]
:::
:::section{.main}

## Architecture

The DCGAN architecture follows a similar pattern to many GAN architectures, with a Generator and a Discriminator to process inputs. 

[IMAGE {4} {Architecture} START SAMPLE]
![Architecture](https://hackmd.io/_uploads/S1jHJSsdj.png)
[IMAGE {4} FINISH SAMPLE]


The general flow of input looks something like the following. For every iteration, randomly generated noise is passed to the Generator. The Discriminator gets a random image sampled from the dataset. The Generator uses the learned weights to modify the noise closer to the target image. The Generator then passes this modified image to the Discriminator, which predicts how real the image looks and returns a probability of the same. The loss from both parts is combined to minimize the loss functions for the Generator and the Discriminator using back-propagation. 

An important point to note for both parts is that the weights are initialized differently for the Convolutional and Batch Normalization layers. If the layer is Convolutional, the weights are from a random normal distribution with a standard deviation of 0.02 and a mean of 0. If the layer is a Batch Normalization layer, a standard deviation of 0.02 means of 1.0 with a bias of 0 is used. 

### Deconvolutional Generator
[IMAGE {5} {Generator} START SAMPLE]
![Generator](https://hackmd.io/_uploads/Bk9TkSoOj.png)
[IMAGE {5} FINISH SAMPLE]


The Generator maps the input from its latent space to the vector data space. This part of the network outputs an RGB image the same size as the training image (3x64x64). 
The Generator comprises blocks of **Transposed Convolutions**, **Batch Normalizations**, and **ReLU** layers. The output is passed through a **Tanh** activation that maps it to a range of [-1,1]. 
The DCGAN authors also found that using a Batch Normalization layer after a Transposed Convolution led to the best results by aiding the gradient flow between the layers. This effect was previously never studied in depth.
In the architecture diagram of this component, *nz* stands for the width of the input, *ngf* stands for the shape of the maps that the network creates, and *nc* refers to a count of the channels that the output will have (Eg : 3 channels for RGB, 4 for RGBA).

### Convolutional Discriminator

The Discriminator is a mirror of the Generator except for a few changes. The input size remains the same as the Generator (3x64x64). Instead of a De-Convolution, a **[Strided](../../KB/Strided.md) Convolution** is used. A **Leaky ReLU** version of ReLU replaces the ReLU activations. The final layer is a **Sigmoid** layer to return the probability of real vs. fake. 
The DCGAN architecture also uses [Strided](../../KB/Strided.md) Convolutions to downsample the images instead of Pooling, allowing the network to learn a custom pooling function. 

## Implementation
To generate images using a DCGAN, we first need to prepare our dataset. This process includes creating a DataLoader to load the images, preprocessing them as necessary, and sending batches of the data to the GPU memory for efficient processing.

Next, we need to define the architecture of the DCGAN, including the Generator and Discriminator networks. This process involves specifying the number and type of layers and initializing the weights of these layers. We must also send the network architecture to the GPU memory for efficient processing.

Once the data and network are ready, we can train the DCGAN. During training, the network learns to map random noise from the latent space to images that resemble the training data. After training, we can use the Generator to generate new images by providing random noise from the latent space.

### Defining the Discriminator

In the DCGAN, the Discriminator differentiates between the images generated by the Generator as real or fake. Its architecture resembles the Generator but with a few modifications. Specifically, the Discriminator incorporates [Strided](../../KB/Strided.md) Convolution layers, a LeakyReLU activation function, and several layers of Batch Normalization. Lastly, the output is passed through a Sigmoid layer that returns a probability value.

For the process of DCGAN image generation, the Discriminator uses [Strided](../../KB/Strided.md) Convolutions in place of Pooling layers. This approach enables the network to develop custom padding functions, improving performance. This approach is a key technique that helps the Discriminator to distinguish between real and fake images more accurately.

```python 
ngpu = 1
nz = 100
ngf = 64
ndf = 64

class Disc_model(nn.Module):
    def __init__(self, ngpu):
        super(Disc_model, self).__init__()
        self.ngpu = ngpu
        self.main = nn.Sequential(
            nn.Conv2d(num_channels, ndf, 4, 2, 1, bias=False),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Conv2d(ndf, ndf * 2, 4, 2, 1, bias=False),
            nn.BatchNorm2d(ndf * 2),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Conv2d(ndf * 2, ndf * 4, 4, 2, 1, bias=False),
            nn.BatchNorm2d(ndf * 4),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Conv2d(ndf * 4, ndf * 8, 4, 2, 1, bias=False),
            nn.BatchNorm2d(ndf * 8),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Conv2d(ndf * 8, 1, 4, 1, 0, bias=False),
            nn.Sigmoid()
        )

    def forward(self, input):
        if input.is_cuda and self.ngpu > 1:
            output = nn.parallel.data_parallel(self.main, input, range(self.ngpu))
        else:
            output = self.main(input)

        return output.view(-1, 1).squeeze(1)
```

### Defining the Generator
The Generator in a DCGAN is responsible for taking a random vector from the latent space and mapping it to an image in the vector data space. This mapping uses a series of transposed convolutional layers, batch normalization layers, and ReLU activation layers. Using batch normalization after the transposed convolutional layers helps improve the gradient flow through the network, resulting in better performance and stability during the training process. The final layer of the Generator uses a Tanh activation function to ensure that the output image is in the range of [-1, 1], which is the expected range for image data.

```python
class Gen_model(nn.Module):
    def __init__(self, ngpu):
        super(Gen_model, self).__init__()
        self.ngpu = ngpu
        self.main = nn.Sequential(
            nn.ConvTranspose2d(nz, ngf * 8, 4, 1, 0, bias=False),
            nn.BatchNorm2d(ngf * 8),
            nn.ReLU(True),
            nn.ConvTranspose2d(ngf * 8, ngf * 4, 4, 2, 1, bias=False),
            nn.BatchNorm2d(ngf * 4),
            nn.ReLU(True),
            nn.ConvTranspose2d(ngf * 4, ngf * 2, 4, 2, 1, bias=False),
            nn.BatchNorm2d(ngf * 2),
            nn.ReLU(True),
            nn.ConvTranspose2d(ngf * 2, ngf, 4, 2, 1, bias=False),
            nn.BatchNorm2d(ngf),
            nn.ReLU(True),
            nn.ConvTranspose2d(ngf, num_channels, 4, 2, 1, bias=False),
            nn.Tanh()
        )

    def forward(self, input):
        if input.is_cuda and self.ngpu > 1:
            output = nn.parallel.data_parallel(self.main, input, range(self.ngpu))
        else:
            output = self.main(input)
            return output
```

### Defining the inputs
The CIFAR10 dataset is utilized in this article provided by the Canadian Institute for Advanced Research. This dataset consists of ten classes of images that are similar to the MNIST format but with 3-channel RGB. The CIFAR10 dataset is widely used for benchmarking image classification models and is an easily learned dataset.

Before using the dataset, it must be loaded and preprocessed. PyTorch has an inbuilt CIFAR10 dataset implementation that we can load directly. If the dataset is being used for the first time, it must be downloaded. Once the dataset is loaded, images are resized to a common size of 64x64x3. Although CIFAR10 is a clean dataset, this resizing step is still important to standardize the images. Finally, the images are normalized and converted to PyTorch tensors.

A DataLoader is then created, a class that creates optimized batches of data to pass to the model. If available, this DataLoader is sent to the GPU to accelerate the DCGAN image generation process.

```python
dataset = tv_data.CIFAR10(root="./data", download=True,
                           transform=transforms.Compose([
                               transforms.Resize(64),
                               transforms.ToTensor(),
                               transforms. Normalize ((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
                           ]))
num_channels=3

dataloader = torch.utils.data.DataLoader(dataset, batch_size=128,
                                         shuffle=True, num_workers=2)
current_device = 'cuda' if torch.cuda.is_available() else 'cpu'
```

### Starting the DCGAN
To streamline the workflow, some empty containers are set up at the beginning of the process. A fixed noise of shape (128, size of latent space, 1, 1) is created and transferred to the GPU memory. The labels for real images are also set as one and for fake images as 0. The network will run for 25 epochs in this example.
For tracking progress and analyzing performance, arrays are created to store the Generator and Discriminator loss during training.
```python
fixed_noise = torch.randn(128, nz, 1, 1).to(current_device)
real_label = 1
fake_label = 0

niter = 25
g_loss = []
d_loss = []
```

### Computing the loss function
The DCGAN image generation process involves two loss functions, one for the Generator and another for the Discriminator.

The Discriminator loss function penalizes the model for incorrectly classifying a real image as fake or a fake image as real. This loss can be thought of as **maximizing** the following function:
$$\nabla_{\theta_{d}} \frac{1}{m} \Sigma_{i=1}^{m}[log D(x^{(i)}) + log(1-D(G(z^{(i)})))]$$

The Generator loss function considers the Discriminator's output, rewarding the Generator if it can fool the Discriminator into thinking the fake image is real. If this condition is not met, the Generator is penalized. This loss can be thought of as **minimizing** the following function:
$$\nabla_{\theta_{g}} \frac{1}{m} \Sigma_{i=1}^{m}log(1-D(G(z^{(i)})))$$

In summary, the Discriminator's role is to maximize its loss function, and Generator's role is to minimize its loss function, which results in Generator creating an image similar to real images. These fake images should be identified as real by the Discriminator.

```python
model_Gen = Gen_model(ngpu).to(current_device)
model_Gen.apply(weights_normal_init)
model_Disc = Disc_model(ngpu).to(current_device)
model_Disc.apply(weights_normal_init)
loss_func = nn.BCELoss()
```

### Optimizing the loss
In this implementation, for DCGAN image generation, the ADAM optimizer is used with a learning rate of 0.0002, and the beta parameters are set to (0.5, 0.999) to minimize the loss function. Different optimizers are used for each of them to ensure that the Generator and Discriminator learn independently.
```python
optimizerD = optim.Adam(model_Disc.parameters(), lr=0.0002, betas=(0.5, 0.999))
optimizerG = optim.Adam(model_Gen.parameters(), lr=0.0002, betas=(0.5, 0.999))
```

### Train the DCGAN 

The DCGAN image generation process involves training the network before generating new images. The procedure is done in the following steps.

- For each epoch, random noise is sent as an input to the Generator.
- The Discriminator also receives a random image sampled from the dataset.
- The Generator then uses its learned weights to transform the noise to be more similar to the target image. These weights allow the Generator to learn the mapping between random noise and the latent space of the image dataset.
- The Generator sends the modified image to the Discriminator.
- The Discriminator evaluates the realism of the generated image and communicates it to the Generator through a probability metric.
- This process of the Generator creating new images and the Discriminator evaluating it continues until the desired number of epochs.
- Once the training is completed, the Generator can generate new images by inputting random noise.

```python
for epoch in tqdm(range(niter), total = niter):
    for i, data in enumerate(dataloader, 0):
        model_Disc.zero_grad()
        device_model = data[0].to(current_device)
        batch_size = device_model.size(0)
        label = torch.full((batch_size,), real_label).to(current_device)

        output = model_Disc(device_model) # Discriminator output
        disc_error_real = loss_func(output.float(), label.float()) 
        disc_error_real.backward() # disc loss for real image
        D_x = output.mean().item()

        noise = torch.randn(batch_size, nz, 1, 1).to(current_device) # create noise
        fake = model_Gen(noise) # Fake image
        label.fill_(fake_label) # Fill with 0
        output = model_Disc(fake.detach())
        disc_error_fake = loss_func(output.float(), label.float()) # disc loss for fake image
        disc_error_fake.backward() 
        D_G_z1 = output.mean().item()
        disc_error = disc_error_real + disc_error_fake
        optimizerD.step()

        model_Gen.zero_grad()
        label.fill_(real_label) # fill with 1
        output = model_Disc(fake.float()) # disc output
        gen_error = loss_func(output.float(), label.float())
        gen_error.backward()
        D_G_z2 = output.mean().item()
        optimizerG.step()

        print('[%d/%d][%d/%d] Loss_D: %.4f Loss_G: %.4f D(x): %.4f D(G(z)): %.4f / %.4f' % (epoch, niter, i, len(dataloader), disc_error.item(), gen_error.item(), D_x, D_G_z1, D_G_z2))
        
        if i % 100 == 0: # save images every 100 steps
            print('saving the output')
            vutils.save_image(device_model,'./images/real_samples.png',normalize=True)
            fake = model_Gen(fixed_noise)
            vutils.save_image(fake.detach(),'./images/fake_samples_epoch_%03d.png' % (epoch),normalize=True)
    
    torch.save(model_Gen.state_dict(), 'weights/model_Gen_epoch_%d.pth' % (epoch))
    torch.save(model_Disc.state_dict(), 'weights/model_Disc_epoch_%d.pth' % (epoch))
```

This article trains the network for 25 epochs. To get a better understanding of the progression of the training, we compare the original sample to the outputs generated at the 0th, 10th, and 25th epochs. As the training progresses, the ./images folder is periodically checked every 100 steps to observe the output. After the training is completed, the final results are as follows.

[IMAGE {5} Original Sample/Target START SAMPLE]
![Original Sample/Target](https://hackmd.io/_uploads/B11dlYXFi.png)
[IMAGE {5} FINISH SAMPLE]

[IMAGE {6} Epoch 0 START SAMPLE]
![Epoch 0](https://hackmd.io/_uploads/Hy-KgtQKs.png)
[IMAGE {6} FINISH SAMPLE]

[IMAGE {7} Epoch 10 START SAMPLE]
![Epoch 10](https://hackmd.io/_uploads/H1x9ltmKj.png)
[IMAGE {7} FINISH SAMPLE]

[IMAGE {8} Final Results START SAMPLE]
![Final Results](https://hackmd.io/_uploads/HJ5qetmti.png)
[IMAGE {8} FINISH SAMPLE]

### Weight Initialization
The DCGAN model requires a careful weight [Initialization](../../KB/Initialization.md) scheme. If the layer is a Convolutional layer, we can take the [Initialization](../../KB/Initialization.md) values from a Normal distribution in the range of (0.0,0.02). On the other hand, if the layer is a Batch Normalization layer, we can take the weights from a Normal distribution in the range of (0.0, 0.02) while we can set the bias to 0.

```python
def weights_normal_init(m):
    classname = m.__class__.__name__
    if classname.find('Conv') != -1:
        m.weight.data.normal_(0.0, 0.02)
    elif classname.find('BatchNorm') != -1:
        m.weight.data.normal_(0.0, 0.02)
        m.bias.data.fill_(0)
```


:::
:::section{.summary}

## Conclusion
- The article has explained the concept of GANs and the specific architecture of DCGANs, which are a variation that can handle larger images.
- It has also provided a step-by-step guide on how to build a DCGAN from scratch using the PyTorch library and the [CIFAR](../../KB/CIFAR.md) dataset.
- The implementation process, including loading the dataset and preprocessing it, creating the network architecture and [Initialization](../../KB/Initialization.md) of weights, as well as training the network, has been explained.
- The final output is expected to be a set of photorealistic images that resemble one of the classes in the [CIFAR](../../KB/CIFAR.md) dataset, which is a significant achievement.
- GANs, particularly DCGANs, have a wide range of applications and can generate images of different objects, depending on the dataset used to train the network. This article provides a foundation for further research and experimentation with GANs.

:::



