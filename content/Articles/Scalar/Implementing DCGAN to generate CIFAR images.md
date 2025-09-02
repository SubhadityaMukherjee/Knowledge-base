---
toc: true
title: Implementing DCGAN to generate CIFAR images

tags: ["article"]
date modified: 
date created: 
---
# Implementing DCGAN to generate [[CIFAR]] images

## What are we building?
Creating novel images is one of the strengths of Generative Adversarial Networks (GANs). In this article, we will build a DCGAN for image generation using the [[CIFAR]] dataset. The DCGAN is a type of GAN that builds upon the Vanilla GAN and addresses some of its issues. The DCGAN is a good choice if the image data size is larger than 28x28. This network also leads to fewer chances of a mode collapse and is thus a better network than a standard GAN. 
Here, we want the network to create realistic images to resemble any of the ten classes of the [[CIFAR]] dataset. We will create the DCGAN from scratch using PyTorch, train it and write scripts to generate our images. 

### What are DGANs
Researchers created the Vanilla GAN architecture to generate images in an unsupervised manner from image datasets. But this GAN had quite a few flaws that impacted its training. DCGANs are a modification of the Vanilla GAN architecture. The implementation of the Discriminator and Generator is configured to tackle some of the issues of the original GAN. Some of the changes are as follows. 
Convolutional layers are used explicitly in the Discriminator. In this architecture, the Generator explicitly uses Transposed Convolution layers. The Discriminator relies on Batch Normalization along with LeakyReLU activations. The Generator, on the other hand, uses ReLU activations. 
The DCGAN image generation process is almost similar to the Vanilla GAN except for a few tweaks to the optimizer and the architecture itself.

### How are we going to build this?
To build the DCGAN, we will use the Python library **PyTorch**. We will first import PyTorch and other required libraries. We then load the image dataset using a **DataLoader**, which is the CIFAR10 dataset in this case. After we load the data, we create the functions that make up the DCGAN. We can then train the network on this dataset and generate new photorealistic images that look like they were part of the CIFAR10 dataset. 
The below sections focus on implementing all the functions required to create a DCGAN image generation pipeline.

### Final Output
The final output we want is photorealistic images that look like they might belong to the CIFAR10 dataset. The result that we get is shown below. 

[IMAGE {1} Final Output START SAMPLE]
![Final Output](https://hackmd.io/_uploads/ByNRyFQYs.png)
[IMAGE {1} FINISH SAMPLE]

Note that longer training might yield better results but take significantly longer.

## Requirements
Before starting the DCGAN image generation process, we must import some libraries and perform set-up operations.
First, we must create folders to store the models' images and weights using the `mkdir` command.
We import the PyTorch library and all the required features we need that comes with it. We also import the numerical processing library *numpy* and the plotting library *matplotlib*. 
Training a GAN takes quite a long time. To further improve performance, we enable a flag in Pytorch that enables **benchmarking**. Pytorch runs a few checks on your current device during the benchmarking process to determine which algorithms perform the best. These checks let you run slightly more optimized code for your current device. 

```python
!mkdir images
!mkdir weights
from __future__ import print_function
import os
import random
import torch
import torch.nn as nn
import torch.nn.parallel
import torch.backends.cudnn as cudnn
import torch.optim as optim
import torch.utils.data
import torchvision.datasets as tv_data
import torchvision.transforms as transforms
import torchvision.utils as vutils
from tqdm import tqdm
import numpy as np
import matplotlib.pyplot as plt

cudnn.benchmark = True
```

## Implementing DCGAN to generate [[CIFAR]] images 
We can now move on to the main DCGAN image generation process. To generate the images, we need to create a DataLoader, load the [[CIFAR]] images,  preprocess them, and send batches of this data to the GPU memory. We also need to create the network architecture and initialize the weights of its components. This network also needs to be sent to the GPU memory. 
After these initial steps have been completed, we can finally train the network and generate new images. 

The DCGAN architecture is similar to many other GAN architectures and consists of a Generator and a Discriminator. The Generator is responsible for creating photo-realistic images from random noise to fool the Discriminator. On the other hand, the Discriminator takes the outputs of the Generator and returns the probability that the generated image is real. The Generator uses this probability to improve its generation capabilities by training the model.
The architecture diagram of the DCGAN is shown below.
[IMAGE {2} Architecture START SAMPLE]
![Architecture](https://hackmd.io/_uploads/S1jHJSsdj.png)
[IMAGE {2} FINISH SAMPLE]

[IMAGE {3} Generator START SAMPLE]
![Generator](https://hackmd.io/_uploads/Bk9TkSoOj.png)
[IMAGE {3} FINISH SAMPLE]

In the architecture, *ngpu* stands for the number of GPUs. In this case, we will only be using a single one. *nz* stands for the width of the input. *ngf* and *ndf* denote the shape of the maps that the Generator and Discriminator create, respectively. *nc* is the number of channels that the image has.

We first start by loading our data and understanding how it looks.

### Exploring the dataset
This article uses the CIFAR10 (Canadian Institute for Advanced Research) dataset. This dataset contains ten classes of images similar to the MNIST format but in 3-channel RGB. The CIFAR10 is a very common dataset for benchmarking image classification models and is easy for a model to learn.

Before we can explore the dataset, we must load and preprocess it. PyTorch comes with the CIFAR10 dataset inbuilt, and we can directly load it. If this is the first time we have used this dataset, it may not exist locally, and we need to download it first. After that, we need to resize all the images to a common size of 64x64x3. CIFAR10 is a clean dataset, and this resizing step is probably unnecessary, but it is a good practice to uphold.
We also normalize the images and convert them to the PyTorch tensors.
In PyTorch, we need to create a DataLoader, simply a class that creates optimized batches of data to pass to the model. 
We send this DataLoader to the GPU if we are using one to enhance the speed of the DCGAN image generation process.

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

After loading the data, we can see how it looks. To visualize a batch of data, we iterate over the DataLoader to grab a single batch of images. After obtaining the images, we can create a grid the size of a single batch, pad the images to make them look neater and normalize them. This batch of images is still on the GPU, which means that we cannot plot it on the CPU without sending it back.  
```python
single_batch = next(iter(dataloader))
plt.figure(figsize=(8,8))
plt.axis("off")
plt.toc: true
title("Training Images")
plt.imshow(np.transpose(vutils.make_grid(single_batch[0].to(current_device)[:64], padding=2, normalize=True).cpu(),(1,2,0)))
```

[IMAGE {4} Training Images START SAMPLE]
![Training Images](https://hackmd.io/_uploads/ryOfbFmti.png)
[IMAGE {4} FINISH SAMPLE]


As we can see, the dataset comprises ten classes of images from which we plot a random sample.

### Defining the Discriminator
The Discriminator in the DCGAN is responsible for classifying the images returned by the Generator as real or fake. Architecturally, the Discriminator is almost a mirror of the Generator with minor differences. The Discriminator uses a **[[Strided]] Convolution** and a **LeakyReLU** along with **Batch Normalization layers**. The final layer is a Sigmoid layer that returns the probability we want. 
For DCGAN image generation, the Discriminator uses [[Strided]] Convolutions instead of Pooling layers. This choice allows the network to learn custom padding functions that, in turn, improve performance.

```python 
ngpu = 1
nz = 100
ngf = 64
ndf = 64

def weights_normal_init(m):
    classname = m.__class__.__name__
    if classname.find('Conv') != -1:
        m.weight.data.normal_(0.0, 0.02)
    elif classname.find('BatchNorm') != -1:
        m.weight.data.normal_(1.0, 0.02)
        m.bias.data.fill_(0)

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

The Generator is responsible for mapping the input data from the latent space to the vector data space. In this part of the network, we get an RGB image as an output that can then be passed to the Discriminator. The generated image size is the same as the original training images but in channel first indexing (3x64x64).
The Generator comprises blocks with **Transposed Convolutions**, **Batch Normalizations** and **ReLU** layers. The final layer has a **Tanh** activation used to make the data to a range of [-1,1].
In this part of the DCGAN image generation process, the DCGAN uses Batch Normalization layers after Transposed convolutions. This shift enables a smoother gradient flow between the layers of the network. 
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
We need to set up some empty containers for an optimized workflow. We first create a fixed noise with the shape (128, size of latent space, 1, 1) and send it to the GPU. We also denote the label of the real image as one and the fake image as 0. For this article, we will run the network for 25 epochs. 
We also pre-allocate arrays to store the Generator and Discriminator loss during training. 
```python
fixed_noise = torch.randn(128, nz, 1, 1).to(current_device)
real_label = 1
fake_label = 0

niter = 25
g_loss = []
d_loss = []
```

### Computing the loss function
The DCGAN image generation pipeline has two loss functions, for the Generator and Discriminator, respectively. 
The Discriminator penalizes wrongly classifying a real image as a fake or a fake image as real. This concept can be thought of as **maximizing** the following function.
$$\nabla_{\theta_{d}} \frac{1}{m} \Sigma_{i=1}^{m}[log D(x^{(i)}) + log(1-D(G(z^{(i)})))]$$

The Generator loss takes the output of the Discriminator into account and rewards it if the Generator is fooled into thinking the fake image is real. If this condition is not satisfied, the Generator is penalized.
This concept can be thought of as **minimizing** the following function.
$$\nabla_{\theta_{g}} \frac{1}{m} \Sigma_{i=1}^{m}log(1-D(G(z^{(i)})))$$

```python
model_Gen = Gen_model(ngpu).to(current_device)
model_Gen.apply(weights_normal_init)
model_Disc = Disc_model(ngpu).to(current_device)
model_Disc.apply(weights_normal_init)
loss_func = nn.BCELoss()
```

### Optimizing the loss
We will use the ADAM optimizer with a learning rate of 0.0002 and the beta parameters set to (0.5m, 0.999) to optimize the loss. The Generator and Discriminator have different optimizers to ensure that they both learn independently.

```python
optimizerD = optim.Adam(model_Disc.parameters(), lr=0.0002, betas=(0.5, 0.999))
optimizerG = optim.Adam(model_Gen.parameters(), lr=0.0002, betas=(0.5, 0.999))
```

### Train the DCGAN
To run DCGAN image generation, we need to train the network first. The general procedure is as follows.
For each epoch, the noise is sent to the Generator. The Discriminator also gets a random image sampled from the dataset. The Generator then uses the weights it has learned to modify the noise to be closer to the target image. In doing so, the Generator learns a mapping between random noise and the latent space of the image dataset. The Generator then sends the tweaked image to the Discriminator. The Discriminator then predicts how real it thinks the generated image is and informs the Generator using a probability metric. 

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

In this article, we train the network for 25 epochs. After the training is complete and even during training, we can periodically check the `./images` folder to see outputs every 100 steps. 
The results we get are as follows.

To understand the training progression, we look at the original sample and then the outputs at 0, ten, and 25 epochs.

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

## What's next
We can apply a few tweaks to the DCGAN in further experiments. Some of them are mentioned below.
- Tweaking the *z_size* variable and either increasing or decreasing it might lead to better performance.
- Longer training might also lead to better results.
- Using Label Smoothing Cross Entropy Loss instead of just a Cross Entropy Loss might also improve performance.
- There is a [long list of tweaks](https://github.com/soumith/ganhacks) proposed by one of the creators of the PyTorch library regarding the DCGAN. The article mentioned is quite a few years old but gives a good background for further experiments on the DCGAN image generation process.

## Conclusion
- A DCGAN was built using PyTorch to generate images from the CIFAR10 dataset.
- The DCGAN is a modified version of a Vanilla GAN that addresses some issues and leads to fewer chances of mode collapse.
- Suggestions for further experimentation with the DCGAN include adjusting the z_size variable, increasing training time, and using Label Smoothing Cross Entropy Loss.



