---
toc: true
title: GRAD

tags: ["article"]
date modified: 
date created: 
---
# GRAD-Cam #deeplearning
Note: This is a slightly advanced article. If you are not comfortable with training neural networks, this is probably not for you yet. Start [here](https://msubhaditya.medium.com/easier-deep-learning-research-for-beginners-935c1a6721c3?source=your_stories_page-------------------------------------) instead.

## Intro
So you want to train a Neural Network to classify images. Woah. That’s awesome! How well did it do? Did you get a good score? Oh? You want to do better? I hear you.
What if you could see what the network sees to make the choice? That would help understand how to make it perform better right? Read on!

A few years ago, a [paper](https://openaccess.thecvf.com/content_ICCV_2017/papers/Selvaraju_Grad-CAM_Visual_Explanations_ICCV_2017_paper.pdf) toc: true
titled “Grad-CAM:
Visual Explanations from Deep Networks via Gradient-based Localization” by Selvaraju et al. talked about how we could visually see the activation maps of a trained CNN by looking at the gradients in the final layer. This post will show you how to use that for your own needs. 

Note: We will be using PyTorch and the [fast.ai](https://www.fast.ai) library. But the concepts stay the same, so you should be able to use it in any other library.

## The Objective and Data
Before we can go to the code, what exactly are we trying to achieve? In short, we want to first train a network such as the “resnet34” architecture on any kind of data. In today’s example, I will be using the [Fish Dataset](https://www.kaggle.com/datasets/crowww/a-large-scale-fish-dataset). This dataset has 9 types of sea creatures.
You can of course, use any other image based classification data that you want.
Knowing how the Dataset is structured is essential, so let’s see that.


Once the training is completed, we want to be able to give the trained network any image for inference and then have it spit out a visual heat map of exactly what it saw in the image. The brighter the color, the more the network focused on that particular spot to make it’s decision.
Have a look at the below example. 

In this image, we can see a yellow border around the fish. (Apologies if it is a disturbing image. Feel free to use any other dataset.) This shows that the network has identified the boundary of the fish and probably tried to use that information to decide what kind of fish it is.

Examining these, we can see if the network is looking at the wrong thing, and find ways to show it what we want it to see. 

## Code

### Training
Okay, let’s not waste any more time and delve right into the code. If you are not familiar with fastai, you can look at this [tiny blog](https://msubhaditya.medium.com/easier-deep-learning-research-for-beginners-935c1a6721c3?source=your_stories_page-------------------------------------) for reference. The complete code can be found here on [github](https://github.com/SubhadityaMukherjee/pytorchTutorialRepo/tree/main/gradcam).

First, we import fastai as the deep learning library, matplotlib for plots, and IPython.display.Image to display the image inline.
https://gist.github.com/SubhadityaMukherjee/grad_imports.py

Training a classifier in fastai is just a few lines. We first decide where the dataset is. 
Then we create a DataBlock. (Think of it as a constructor for a dataloader). This DataBlock is given the following information
- Type of task : Image -> Label
- What to do : get the images from the directory
- How to label the images : use the folder where the images are. For example, if the file name is “/media/hdd/Datasets/Fish_Dataset/Fish_Dataset/Shrimp/Shrimp/00001.png” , then it’s parent is “Shrimp”. 
- How to split the data: Randomly with an 80/20 train/test split.
- Transforms : Basic vision transforms, Crop and resize to 224x224 px.

Once we have that, we can pass it to the main trainer class - the “vision_learner”. To it, we pass in the network we want to use (You can use any other as well), and the metrics we care about.
The to_fp16() enables [Mixed Precision Training](https://pytorch.org/docs/stable/notes/amp_examples.html) that would further increase the training speed and decrease the memory consumption.

Awesome! Now let’s train the network. We are using a pre-trained resnet34 and performing transfer learning, so we use fine_tune. If you want to train from scratch, you can use “learn.fit(1)” instead. I trained it for a single epoch as a demo.

https://gist.github.com/SubhadityaMukherjee/grad_train.py

### Hooks
I mentioned previously that we would be looking at the gradients of the trained network. But how do we access them? 
In PyTorch, we can modify the components of the training loop using the concept of “Hooks”. As the name suggests, it involves inserting a hook in the training loop and execute arbitrary code. Using that, we need to save the gradients during training.
PyTorch has functions for the same called “register_forward_hook” for the forward pass, and “register_backward_hook” for the backward pass. We can take this information and write the following classes as a wrapper around our training loop. 


### Plotting Activations
Now for the intense bit. Let’s pick a random image from the dataset. The original image is slightly disturbing so I blurred it a bit. 

Okay, we need to now pass the image through the model. The FastAI syntax for this kind of patching is slightly complicated. But let us walk through it.
We first create the test data loader with the new image that we picked. We can then convert that into a Tensor. Once we pass the image to the network, it performs a full forward and backward pass on that image through every layer. Now for every layer in the model, we can get the computed gradients that we stored away using the Hook class. 
Selvaraju et al. defined the activation map as the weighted combination of the forward activation maps. Which is what we perform. 
The rest of the code is just matplotlib convenience functions to plot the nice grid heatmap that you see.
The only weird line of code you might see is “cam_map.detach().cpu()”. This is done because we cannot plot a Tensor on the GPU, so we first detach it from the computational graph, then bring it back to the CPU to plot it.

Well, yay! You made it. Try it with your own network and/or data. Just a word of warning, the 0 in line “with HookBwd(learn.model[0][layer]) as hookg”, needs to be modified based on the network architecture. If you get errors, try with a 1 and so forth.

https://gist.github.com/SubhadityaMukherjee/grad_plot.py

## What’s next?
Firstly, good job on making it so far! Pat yourself on the back or go grab something nice to eat.
Then look at what the network sees. Does it make sense? Is the model looking at something weird? Train for a few more epochs, rinse and repeat.
Try it for different images. You might find examples that make no sense. Sometimes it might be because of random augmentation, other times it might be because of model bias or the data itself being not okay. You will find ways to improve on it eventually. If you can, look for examples that the model gets wrong, and apply GRADCam on those.

## Fin
Woah. That was long.
What’s next? More articles. In the meanwhile, you can look at [this](https://gist.github.com/SubhadityaMukherjee/6a70d6dc74783e2addac8bed475ac220) little link with resources I have collected over the years.
You have a long way to go. But I do hope this was a good start. I know you didn’t read the whole thing. Maybe you didn’t make it till here either. I get that. I also did that when I was starting. This article is in the hopes that it will help someone out. Maybe have the help that I did not. I do not know who it will reach. But to whoever it does, best of luck :)
You can contact me on [LinkedIn](https://www.linkedin.com/in/subhaditya-mukherjee-a36883100), drop me an [[mailto:msubhaditya@gmail.com|Email]]



