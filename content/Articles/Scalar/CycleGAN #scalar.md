
---
toc: true
title: CycleGAN #scalar

tags: ["article"]
date modified: 
date created: 
---
# Translating Images Using a CycleGAN #scalar
:::section{.abstract}

## Overview
The field of computer vision has been trying to create AI that creates never seen before images for decades. Generative networks such as the CycleGAN are part of a long line of such research, but one that performs extremely well in tasks ranging from converting images to paintings to changing the weather in images. The CycleGAN is rather different from many approaches before it as it is an unpaired Image2Image translation task with these tasks being cyclic in nature. In this article, we will explore what all these terms mean and how to put them into practise in a CycleGAN.

## Disclaimer
This is an intermediate level article and introduces a significant number of new terms. Attempting to understand this article is not recommended before mastering how a [Basic GAN](../../KB/Basic%20GAN.md) (eg: DCGAN) works.
Being so complex, it is advised to slow down and understand a section before moving on to the next.
:::
:::section{.scope}

## Scope of the Article
This article covers the following concepts
- What is an unpaired Image2Image task
- What is GAN and subsequently, what is a CycleGAN
- Concepts such as Generators, Discriminator, Encoder Decoder architectures
- Latent space as an easier means of understanding CycleGANs
- Architectural Details and Training procedure of CycleGANs
- How to use CycleGANs in various domains
:::
:::section{.main}

## Note About The Code
This article does not contain the code to run a CycleGAN. This was done to prevent the article from becoming extremely huge. Instead, every concept that would be required to understand the code is explained in detail below.
The entire code with examples can be found on the [official Tensorflow/Keras documentation website](https://keras.io/examples/generative/cyclegan/). On understanding this article, this code will become extremely easy to comprehend and use.

## Quick Recap
This section gives a recap of the important concepts we need to understand CycleGAN. 

### Image2Image Translation
An image translation task’s objective is to convert from one image to either text or another image. An example of the same would be taking a picture of a sunset and converting that picture to the style of the artist Van Gogh. There are many such Image translation tasks, but the one in consideration in this article is specifically converting from an image to another image aka Image2Image.

### Paired vs Unpaired Translation
An important detail about the CycleGAN is that unlike most other GANs or UNet style architectures, it uses an unpaired translation. This means that the image, label pairs that are being passed into the model are not related to each other. In contrary to say, a classification task where the label passed is the exact label of the image passed. This might be slightly confusing to understand without knowledge of latent space. More explanations can be found in the next section

### GAN
GANs are a special class of architectures that have two components, one that tries to get better at a task, and the other that tries to find out how badly the first part is performing. The training procedure is somewhat similar to a game with one component being an “adversary” of the other, hence the term “Adversarial network”. The generative term comes into play as these networks are used to create novel images from existing data.

### Adversarial Training
A useful analogy to understand how a GAN is trained is the classic “cop” vs “thief” analogy. Assume that the thief in this case is trying to forge a painting by Van Gogh, while the cop tries to prove the thief wrong. The thief first comes up with a forgery, and the cop says no, this is fake and is not the real one because of some reason. The thief then shows a modified image to the cop with minor differences. This scenario repeats until the cop can no longer tell the difference between the real and the fake images.
This type of training is called adversarial training. Using a second opinion to improve the outputs of the first component of the model. A useful advantage here is that the data does not need to be labelled. 

### Generator
The generator is the “thief”. It starts with random noise to create a fake image and traverses the latent space until the Discriminator can no longer tell the difference between the fake and the real images.

### Discriminator
Consequently, the discriminator is the “cop”. It is essentially a classifier that returns a metric of how fake the image looks. 

### Encoder Decoder Architecture 
Many networks such as the UNet and GANs have a two sided architecture that involves [Downsampling](../../KB/Downsampling.md) the image until a point and then upsampling from there on. The Encoder is the first half which downsamples the image and condenses the information in a batch of data down into the smallest possible unit. 
The decoder does the opposite, it takes this smallest possible unit and attempts to recreate the original input. In the process, it learns how to traverse the latent space and create the required translation. 

### Residual Block
The Encoder Decoder architecture has a major drawback, in the process of compressing the image information and reconstructing it, a lot of information is lost during the operations. The Residual Block is the answer to this dilemma. It essentially contains a “Skip Connection” that ensures that the gradients from the previous layer are carried over to the next layer. 
This is done very simply. If $F(x)$ is the network, then for an input $x_{i}$, $x_i = F(x_{i-1}) + x_{i-1}$. 

### Cost Function
A cost function is the objective that the network tries to minimise. In essence, it is a metric of how well the network performs with respect to a task. For image classification, it could be CrossEntropy. CycleGAN has a rather complex cost function that is explained in later sections.

## Latent Space
Understanding latent space is the key to fully comprehending the CycleGAN. It can be thought of as an n-dimensional vector space that contains every possible image that can be generated from the given data. It is not possible to entirely visualise this directly but a useful analogy is considering faces. 
If we consider the faces of every person that we know and “average” them together, we would end up with a “generic face” that has traits from every face that we considered. From this “generic face”, if we were to attempt to recreate any of the other faces, we would have to “add” or “subtract” some features from the face to reach the other one.
This can be thought of as “traversing” the latent space. Thus in essence, the latent space contains all such possible faces. In theory then, it makes sense to assume that if we can approximate this latent space, we can translate any image to the other by traversing it. The CycleGAN attempts to do just that. Traversal can go in both directions, hence it’s “cyclic” nature.

## CycleGAN Architecture
The CycleGAN architecture is divided into two major parts - The Generator and the Discriminator. The Generator further has the Encoder, the Transformer and the Decoder as components.

### Encoder Block
The encoder uses convolution layers to consolidate information from the data and compress it into the least possible representational unit. The number of channels consequently increase. In the current model, there are 3 convolution operations. The final output of the model reduces the original image size by 3/4th and passes it to the Transformer Block.

### “Transformer” Block
The Transformer Block has nothing to do with “Transformer architectures” but is called so because it takes the output of the encoder and transformers it so the decoder can use it. In the CycleGAN, this block has around 6-9 Residual blocks. This is done to ensure maximum information extraction from the compressed representation that the encoder generates.

### Decoder Block
The decoder block then takes the inputs from the transformer block and passes it through two de-convolution layers. 

### Discriminator
The Discriminator in the CycleGAN is another type of GAN - “PatchGAN”. This special type of Discriminator uses patches of the input image to map to outputs. Unlike a normal GAN that maps from a 256x256 sized image to a scalar result (“real” or “fake), the PatchGAN maps it to NxN sized arrays of outputs $X$ where each $X_{i,j}$ maps to (“real”, “fake”).
This is run as a convolution through the entire image and the results are averaged out.

## Loss Functions
CycleGAN uses a mix of three loss functions. Along with adversarial loss, a cycle consistency loss and an identity loss are used to create the final objective function.

### Cycle Consistency Loss
This is the most important part of the CycleGAN research. Considering two image domains $X$ and $Y$, the Cycle consistency loss uses two different mappings $G: X \rightarrow Y$ and $F : Y \rightarrow X$. These mappings are bijections, aka reverses of each other. (Hence “cyclic”). As a mathematical expression, the Cycle Consistency Loss $\mathcal{L}_{cyc}$ can then be represented as $$\mathcal{L}_{cyc}(G, F, X, Y) = \frac{1}{m}\Sigma_{i=1}^{m}[(F(G(x_{i})-x_{i})+ (G(F(y_{i}))-y_{i})]$$.

### Identity Loss
Another loss function that CycleGAN proposes is the Identity loss. $$L_{identity}(G,F) = \mathbb{E}_{y \sim p_{data}(y)}[||G(y)-y)||_{1}] + \mathbb{E}_{x \sim p_{data}(x)}[||F(x)-x)||_{1}]$$
This is especially useful for converting to and from photos and paintings. The loss is used to preserve the color information during transformation and attempts to make sure that the reverse color is not used. If a part of the image looks like it belongs to the target image already, it is not mapped to something else. In principle, it makes the model more conservative if the content to be transformed is not known.

### Objective/Cost Function
The net loss function is therefore a combination of all the three losses just described. A hyper parameter $\lambda$ is used to control the strength of the transfer. It is usually set to 10.
$$\mathcal{L}_{GAN}(G, F, D_{X}, D_{Y}) = \mathcal{L}_{GAN}(G, D_{Y}, X, Y) + \mathcal{L}_{GAN}(F, D_{X}, X, Y) + \lambda \mathcal{L}_{cyc}(G,F)$$

Thus the function that we wish to solve is finding the value of the optimisers that gives the best loss while maintaining the ability to convert to and from the target image. This can be seen in the formula. $$G^{*},F^{*} =\underset{G,F}{argmin} \underset{D_{X}, D_{Y}}{max} \mathcal{L}_{GAN}(G, F, D_{X}, D_{Y})$$

## Other Useful Details About The Architecture
The CycleGAN paper and code have a lot of interesting tweaks that were done to improve performance. Some of the ones that are not usually mentioned are as follows.

## Separate Optimizers
There are two optimisers for the discriminator and the generator each. (Four in total.) Using two separate optimisers ensure that the model learns to convert images in both directions and minimises the loss for both sets of generators and discriminators.

### Instance Normalisation
Instance normalisation is a regularisation technique that allows the network to remove specific contrast information when transferring style information between images. This technique makes CycleGANs extremely useful for image stylisation tasks.
The formula is similar to that of Batch Normalisation and is left in this article as a reference. 
$$y_{tijk} = \frac{x_{tijk} - \mu_{ti}}{\sqrt{\sigma_{ti}^2 + \epsilon}},
    \quad
    \mu_{ti} = \frac{1}{HW}\sum_{l=1}^W \sum_{m=1}^H x_{tilm},
    \quad
    \sigma_{ti}^2 = \frac{1}{HW}\sum_{l=1}^W \sum_{m=1}^H (x_{tilm} - mu_{ti})^2$$

### Fractional Stride
Most networks use a stride that is a whole number. CycleGAN has two types of convolutions. One type that has a stride of 2, while the other that has a stride of $\frac{1}{2}$. This is a special case of convolution that is also known as a “de-convolution”. A fractional stride upsamples an image from a smaller dimension to a larger one. A whole number stride downsamples it.

### Reflection Padding
When performing convolutions, the sliding window does not always fit the size of the image to be convolved, padding is used in those cases to make up for the missing pixels. In CycleGAN, a reflection padding is used which just means that the missing pixels are filled in with its neighbouring pixels before being convolved instead of being filled with a “black” 0 pixel. This helps to preserve some more content information.

## Photos To Paintings
To convert photos to paintings, the procedure remains exactly the same as before. The only difference is the dataset. As long as the dataset contains images in different folders with different painting style information alongside a folder of plain photos, CycleGAN can convert between them.
The original paper has many such results. Some of which are shown below.

## More Use Cases
Just like converting photos to paintings, a similar thought process can be applied to find other uses cases. The ones that the paper mention are as follows :
- Style Transfer : Same as photos to and from paintings except with other types of imagery than just paintings.
- Object Transformation : Convert to and from objects within ImageNet classes by traversing the latent space. Eg: Converting apples to oranges, zebras to horses etc.
- Season Transfer : Converting images taken in Winter to summer and vice versa.

## Limitations
Every method has its limitations. CycleGAN performs poorly when given geometrical transformations. This is because it is trained to change appearances but it does not penalise changes in geometry. 
:::
:::section{.summary}

## Conclusion
In this article, we learnt about CycleGAN and all the architectural details required to create it. We explored the concept of a latent space and understood how a GAN works by traversing it. We also looked at many applications of a CycleGAN and how to train one on our own data.
:::



