
---
toc: true
title: Siamese Network

tags: ["article"]
date modified: 
date created: 
---
# Siamese Network

:::section{.abstract}

## Overview
The lack of data is a huge hurdle for any Deep learning task. Finding large datasets is nearly impossible in domains such as facial recognition, signature verification, text similarity, and many others. In many cases, a single example of each class is present. A regular CNN fails to perform in these cases, but if a network learns to minimize a similarity metric between images, it can easily perform this task. The Siamese Network is a class of architectures that excel at this one-shot learning task. 
This article explains the workings behind the Siamese Network and provides an implementation for Signature Verification.
:::
:::section{.scope}

## Scope
- This article explains the concept of Siamese Networks and why they are useful.
- It explains the multiple loss functions behind Siamese Networks.
- It talks about **few-shot learning** and how to apply it to tasks.
- It talks about some of the use cases of Siamese Networks.
- The article also explains how to create a Siamese Network for a **Signature Verification** task using PyTorch.
:::
:::section{.main}


## Introduction
Siamese networks are a one-shot classification paradigm where only a single example is enough for the network to classify images accurately. This network uses the concept of **Contrastive Loss**, which finds a pairwise similarity score between the images in the Dataset. Instead of learning the content of the images, the Siamese network learns the differences and similarities between them. This unique learning paradigm makes these networks much more robust to the lack of data and improves performance without needing domain-specific information.

Signature verification is a task in which these networks excel. This task aims to identify forged signatures given a single signature sample for thousands of people. This task is quite challenging due to the vast differences between individual signatures and the need for more training data. 

In this article, we will explore the task of Signature Verification using these Siamese Networks and create a working model using PyTorch.

## What Are Siamese Networks?
Siamese Networks are a family of networks that uses two identical subnetworks for one-shot classification. The sub-networks share the same configuration, parameters, and weights but have different inputs. Unlike a regular CNN that learns to predict multiple classes using vast amounts of data, a Siamese Network learns a similarity function. We can use the learned function to differentiate between classes without needing a lot of data. These networks are specialized in one-shot classification, which means that in many cases, they only need a single example to classify images accurately.

As a real-life use case, Siamese Networks are applied to face recognition and signature verification tasks. Consider the face recognition task done for a company that wants to take an automated face-based attendance. The company would only have a single picture of its employees. A regular CNN would have been incapable of accurately classifying thousands of employees based on a single image of each of them. A Siamese network, on the other hand, excels at this task.

## Exploring Few-Shot Learning
Few shot models are a family of architectures that rely not on the number of training examples but on exploiting the differences between a small number of samples. This property allows them to make predictions ranging from a few samples to a single sample.
The advantage of few-shot learning comes into play when the training data is very small. For large datasets, this training paradigm could be more helpful.

## Architecture of Siamese Networks
The objective of the Siamese network is to find similar inputs and magnify the differences between dissimilar pairs. The architecture of this network is shown in the figure below.

[IMAGE {1} {Architecture} START SAMPLE]
![Architecture](https://hackmd.io/_uploads/B1F3TwYqs.png)
[IMAGE {1} FINISH SAMPLE]


Some features that set Siamese networks apart from the usual CNN architecture are as follows.
- The network has two different inputs. Each of these inputs is passed into identical subnetworks.
- The inputs are passed through a Convolutional network first and then encoded. 
- Any changes to one side of the network are reflected on the other.
- The network returns an encoding that is a similarity score. This score can be used to differentiate between classes. 
- The network is a one-shot classifier and does not require a lot of examples per class. 

## Loss Functions Used in Siamese Networks
The Siamese Network uses multiple loss functions. They are explained below.

### Binary Cross Entropy Loss
This loss is one of the common image classification loss functions. The Siamese network uses this loss to classify the image pairs as similar or dissimilar.

### Contrastive Loss
The Contrastive Loss function finds the difference between image pairs by using distance as a similarity measure. This function is useful when there are few training examples per class. 
A caveat of using Contrastive loss is that it requires pairs of both negative and positive training samples. We can visualize this loss in the figure below.


[IMAGE {2} {Contrastive Loss} START SAMPLE]
![Contrastive Loss](https://hackmd.io/_uploads/H1AlADKco.png)
[IMAGE {2} FINISH SAMPLE]


The Contrastive Loss equation is $$(1-Y) \frac{1}{2} D^{2}_{w} + (Y) + \frac{1}{2} (max(0, m - D^{2}_{\omega}))$$
When Y is 0, the inputs share the same class. When the value of Y is 1, they are from different classes.
The margin m defines the margin that the distance function uses to identify pairs that contribute to the loss. The value of m is always greater than 0.
D denotes Euclidean distance.

### Triplet Loss
The triplet loss uses triples of data. These triples can be seen in the image below.
[IMAGE {3} {Triplet Loss} START SAMPLE]
![Triplet Loss](https://hackmd.io/_uploads/ryAGCDtco.png)
[IMAGE {3} FINISH SAMPLE]

The objective of the triplet loss function is to maximize the distance between the anchor and the negative samples while minimizing the distance between the anchor and the positive samples.
This task is shown in the below image.

The Triplet loss is defined as $$L = max(d(a,p) - d(a,n) + margin, 0)$$

## Building a Signature Verification Model With Siamese Networks
Signature verification is the task of identifying forged signatures given a dataset of real ones. For this task, a model has to learn the difference between hundreds of signatures. Given a fake or a real signature, the model has to differentiate between them.
This verification task is extremely hard for a regular CNN due to the complexity of changes and lack of training samples. In most cases, only a single signature is available per person, and the model needs to learn how to verify signatures for thousands of people.
The following sections explore building a model to tackle this task using PyTorch.

### Dataset
The Dataset we will be using is a signature verification dataset known as **ICDAR 2011**. This Dataset contains Dutch signatures that are either forged or original. An example of the data is shown below.

[IMAGE {4} {Examples} START SAMPLE]
![Examples](https://hackmd.io/_uploads/HJq7RDK9s.png)
[IMAGE {4} FINISH SAMPLE]

We can download the Dataset from this [drive link](https://drive.google.com/drive/folders/1hFljH9AKhxxIqH-3fj72mCMA6Xh3Vv0m?usp=sharing).

### Description of problem statement
This article considers recognizing fake signatures as part of a signature verification problem. We aim to take a dataset of signatures and use a Siamese network to predict which of the test signatures belong to real people and which are forged. 
We need to create a pipeline that reads the Dataset, creates image pairs, and passes them to the Siamese network. After training the network on the Dataset, we need to create functions for inference.

### Imports
To create the Siamese Network, we need to import a few libraries. We import the **Pillow** library(PIL) for image processing. We will import the plotting package **matplotlib**, the numerical library **numpy**, and the progress bar library **tqdm** for other utilities. We will use **Pytorch** and **torchvision**to train and build the network.

```python
from PIL import Image
from torch.autograd import Variable
from torch.utils.data import DataLoader, Dataset
import PIL.images
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.utils.data as utils
import torchvision
import torchvision.transforms as transforms
import torchvision.utils
from tqdm import tqdm
```

### Utility Functions
To visualize the network's outputs, we create a function that takes the images and the labels as inputs and plots them in an easy-to-visualize grid.

```python
def imshow(img, text=None, should_save=False):
    npimg = img.numpy()
    plt.axis("off")
    if text:
        plt.text(
            75,
            8,
            style= "italic",
            fontweight= "bold",
            bbox={"face color": "white", "alpha": 0.8, "pad": 10},
        )
    plt.imshow(np.transpose(npimg, (1, 2, 0)))
    plt.show()
```

### Data preprocessing
The data structure used by the Siamese network is very different from the usual image classification networks. Instead of providing an image and a label, the Dataset Generator for the Siamese network must provide pairs of images. These pairs are converted to Black and white and are then resized and converted to Tensors. 
There are two types of pairs - the positive pair, where both the inputs images are identical, and the negative pair, where the images are not identical.
We also create a function that returns the size of the Dataset when called.

```python
dir_train = "train"
df_train = "train_data.csv"
df_val = "test_data.csv"
dir_val = "test"
bs = 32
num_epoch = 20

class PairedDataset:
    def __init__(self, df_train=None, dir_train=None, transform=None, load_subset = None):
        self.train_df = PD.read_csv(df_train)
        if load_subset!=None:
            self.train_df = self.train_df[:load_subset]
        self.train_df.columns = ["image1", "image2", "label"]
        self.train_dir = dir_train
        self.transform = transform

    def __getitem__(self, index):
        pair1 = os.path.join(self.train_dir, self.train_df.iat[index, 0])
        pair2 = os.path.join(self.train_dir, self.train_df.iat[index, 1])

        pair_left = Image.open(pair1).convert("L")
        pair_right = Image.open(pair2).convert("L")

        if self.transform is not None:
            pair_left = self.transform(pair_left)
            pair_right = self.transform(pair_right)

        return (
            pair_left,
            pair_right,
            torch.from_numpy(
                np.array([int(self.train_df.iat[index, 2])], dtype=np.float32)
            ),
        )

    def __len__(self):
        return len(self.train_df)

```

### Brief Description of the features
The features that the network gets are pairs of images. There are positive or negative data pairs. Both the pairs are image data and are Tensor representations of the underlying images. 
The labels provided to the Siamese network are categorical. 

### Standardization of the features
To standardize the features, we first convert them to Black and White. We also resized all the images to be (105x105) square as the Siamese Network requires this size. Finally, we convert all the images to Tensors to improve performance and be able to use the GPU.

```python
transform=transforms.Compose(
        [transforms.Resize((105, 105)), transforms.ToTensor()]
)
```

### Splitting the Dataset
To ensure that the model can be used for prediction and not just training, we split the Dataset into training and testing parts. 
For simplicity, we only use the first 1000 data points. Setting the *load_subset* function to *None* would use the entire Dataset but take much longer. We do not perform Data Augmentation here, but that is an option to make the network perform better in the long run.

```python
train_ds = PairedDataset(
    df_train,
    dir_train,
    transform=transforms.Compose(
        [transforms.Resize((105, 105)), transforms.ToTensor()]
    ),
    load_subset=1000
)
eval_ds = PairedDataset(
    df_val,
    dir_val,
    transform=transforms.Compose(
        [transforms.Resize((105, 105)), transforms.ToTensor()]
    ),
    load_subset=1000
)
```

### Neural Network Architecture 
We can create the architecture that we described above in a few steps. 
First, we create a function that creates blocks of Convolutions, Batch Normalisation, and ReLU with different input and output channels. We give this function the option of having a [Dropout](../../KB/Dropout.md) layer at the end or skipping that layer.
We also create another function that generates blocks of FC layers followed by ReLU layers.
We can use these functions to create the Sequential model that defines the Siamese Network. After creating the CNN part of the architecture using the functions we defined earlier, we have to create the FC part of the network. Note that different padding and kernel sizes are used across the network. 
The FC part of the network is blocks of Linear layers followed by ReLU activations. 
Once we have defined the architecture, we can run a forward pass for the data we pass to the network. Note that the *view* function is used to resize the output of the previous block by flattening dimensions. After creating this function, we can start training the Siamese network on the data. 

```python
class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()

        self.cnn1 = nn.Sequential(
            self.conv_bn_relu(1, 96, 11, 1, False),
            self.conv_bn_relu(96, 256, 5, 2, True),
            nn.Conv2d(256,384 , kernel_size=3,stride=1,padding=1),
            nn.BatchNorm2d(384),
            nn.ReLU(inplace=True),
            self.conv_bn_relu(384, 256, 3, 1, True),
        )
        
        self.fc1 = nn.Sequential(
            self.linrel(30976, 1024),
            nn.Dropout2d(p=0.5),
            self.linrel(1024, 128),
            nn.Linear(128,2))
    
    def linrel(self, inc, outc): return nn.Sequential(nn.Linear(inc, outc), nn.ReLU(inplace=True))
        
    def conv_bn_relu(self,inc, outc, ks, pad,dropout = True):
        if dropout == True:
            return nn.Sequential(
                nn.Conv2d(inc, outc, kernel_size=ks,stride=1,padding=pad),
                nn.BatchNorm2d(outc),
                nn.ReLU(inplace=True),
                nn.MaxPool2d(3, stride=2),
                nn.Dropout2d(p=0.3),
            )
        else:
            return nn.Sequential(
                nn.Conv2d(inc, outc, kernel_size=ks,stride=1),
                nn.BatchNorm2d(outc),
                nn.ReLU(inplace=True),
                nn.MaxPool2d(3, stride=2),
            )

    def forward_once(self, x):
        output = self.cnn1(x)
        output = output.view(output.size()[0], -1)
        output = self.fc1(output)
        return output

    def forward(self, input1, input2):
        out1 = self.forward_once(input1)
        out2 = self.forward_once(input2)
        return out1, out2
```

### Loss Function 
The loss function that the Siamese Network uses is contrastive loss. We can define this loss using the equations mentioned earlier in the article. 
To improve code performance, instead of defining the loss as a simple function, we inherit from nn.Module and create a class that returns the outputs of the function. This wrapper will allow PyTorch to optimize the code for better runtime performance.

```python
class ContrastiveLoss(nn.Module):
    def __init__(self, margin=2.0):
        super(ContrastiveLoss, self).__init__()
        self.margin = margin

    def forward(self, out1, out2, label):
        euclidean_distance = F.pairwise_distance(out1, out2)
        return torch.mean(
            (1 - label) * torch.pow(euclidean_distance, 2)
            + (label)
            * torch.pow(torch.clamp(self.margin - euclidean_distance, min=0.0), 2)
        )
```

### Training the Siamese Network
Now that we have loaded and cleaned up the data, we can start training the Siamese network using it. To do so, we first create the training and testing data loaders. Note that the evaluation DataLoader has a batch size of 1 as we want to perform one-by-one evaluations.
We then send the model to the GPU and define the Contrastive Loss and the Adam optimizer.

```python
dl_train = DataLoader(train_ds,
                        shuffle=True,
                        num_workers=8,
                        batch_size=bs) 
dl_eval = DataLoader(eval_ds,
                        shuffle=True,
                        num_workers=8,
                        batch_size=1) 

net = Model().cuda()
criterion = ContrastiveLoss()
optimizer = torch.optim.Adam(net.parameters(), lr=1e-3, weight_decay=0.0005)
```
We then write a function that takes the train DataLoader as an argument. We keep a running array of the loss and the counter to plot it later. After that, we iterate over the points in the DataLoader. For every point, we send the pairs to the GPU, run the pairs through the network, and calculate the Contrastive Loss. We can then perform the backward pass and return the net loss for a batch of data.

```python
def train(dl_train):
    loss=[] 
    counter=[]
    iteration_number = 0
    for i, data in tqdm(enumerate(dl_train,0), total = len(dl_train)):
      pair_left, pair_right , label = data
      pair_left, pair_right , label = pair_left.cuda(), pair_right.cuda() , label.cuda()
      optimizer.zero_grad()
      out1,out2 = net(pair_left,pair_right)
      loss_contrastive = criterion(out1,out2,label)
      loss_contrastive.backward()
      optimizer.step()
      loss.append(loss_contrastive.item())
    loss = np.array(loss)
    return loss.mean()/len(dl_train)

```

We can train the model for several epochs using the function we just created. This article only trains the model for a few epochs as a demo.
If the evaluation loss is the best we have seen across the entire training period, we save the model for inference at that epoch.

```python
for epoch in tqdm(range(1,num_epoch)):
  best_eval_loss = 9999
  train_loss = train(dl_train)
  eval_loss = eval(dl_eval)

  print(f"Training loss {train_loss}")
  print(f"Eval loss {eval_loss}")

  if eval_loss<best_eval_loss:
    best_eval_loss = eval_loss
    print(f"Best Eval loss{best_eval_loss}")
    torch.save(net.state_dict(), "model.pth")
    print("Model Saved Successfully") 
```

[IMAGE {5} {Training} START SAMPLE]
![Training](https://hackmd.io/_uploads/H1eDCDtcj.png)
[IMAGE {5} FINISH SAMPLE]


### Testing the model 
After training the model, we can evaluate it and run inference for a single data point.
Similar to the training function, we create an evaluation function that takes the test data loader as input. We iterate the data loader one at a time and obtain the pairs of images we wish to test. We pass these image pairs to the GPU and run the model over them. After obtaining the output from the model, we find the Contrastive loss and save it to a list.

```python
def eval(dl_eval):
    loss=[] 
    counter=[]
    iteration_number = 0
    for i, data in tqdm(enumerate(dl_eval,0), total=len(dl_eval)):
      pair_left, pair_right , label = data
      pair_left, pair_right , label = pair_left.cuda(), pair_right.cuda() , label.cuda()
      out1,out2 = net(pair_left,pair_right)
      loss_contrastive = criterion(out1,out2,label)
      loss.append(loss_contrastive.item())
    loss = np.array(loss)
    return loss.mean()/len(dl_eval)
```

We can now run the code for a single evaluation over all the test data points. To visualize the performance, we will plot the image and print the pairwise distances between the data points the model identifies. We can then plot these results as a grid.

```python
for i, data in enumerate(dl_eval, 0):
    x0, x1, label = data
    concat = torch.cat((x0, x1), 0)
    out1, out2 = net(x0.to('cuda'), x1.to('cuda'))

    eucledian_distance = F.pairwise_distance(out1, out2)
    print(label)
    if label == torch.FloatTensor([[0.md|0]]):
        label = "Original Pair Of Signature"
    else:
        label = "Forged Pair Of Signature"

    imshow(torchvision.utils.make_grid(concat))
    print("Predicted Euclidean Distance:-", eucledian_distance.item())
    print("Actual Label:-", label)
    if i == 4:
        break

```

[IMAGE {6} {Outputs} START SAMPLE]
![Outputs](https://hackmd.io/_uploads/H1N_ADKci.png)
[IMAGE {6} FINISH SAMPLE]


## Pros and Cons of Siamese Networks
Like all Deep Learning applications, Siamese Networks have multiple pros and cons. Some of them are listed below.

### Cons
- The biggest disadvantage of using a Siamese network is that it returns only a similarity score. Since the network's output is a *distance metric*, it does not sum up to 1. This property makes it harder to use in some cases.

### Pros
- Siamese networks are robust to varying numbers of examples in classes. This robustness is due to the network requiring very little information about the classes.
- Domain-specific information does not need to be provided to the network to classify images.
- Siamese networks can perform predictions even with a single image per class.

## Applications
Siamese Networks have quite a few applications. Some of them are as follows.

### Facial Recognition
Due to the paired nature of the Siamese networks, one-short facial recognition is a good use case to use this network. The contrastive loss is used to *push* different faces away from each other and *pull* similar faces closer. In doing so, the Siamese network learns to identify faces without requiring too many examples.

### Fingerprints
Similar to facial recognition, we can also use Siamese Networks for fingerprint recognition. Once the fingerprints in the database have been cleaned and pre-processed, we can feed them pairwise to the network. The Siamese network then learns to find their differences and identify which fingerprint is valid and invalid.

### Signature Verification
This article focused on implementing Signature Verification using Siamese networks. As we saw in this article, we can create a pairwise dataset using signatures and the network to identify which signatures are forged and which are real. 

### Text Similarity
Another useful application of Siamese Networks is Text similarity. Given multiple pieces of text, the network can be fed a pairwise dataset and tasked with identifying which are similar. Examples of such tasks include - finding similar questions from a question bank and using Siamese networks to find similar documents from a text database.

:::
:::section{.summary}

## Conclusion
- Siamese networks are a powerful tool for classifying datasets with few examples per class.
- We learned the concepts behind Siamese networks and understood the architecture, loss functions used, and how to train such a network.
- We explored the Signature verification task using the ICDAR 2011 dataset and implemented a model to identify forged signatures.
- We also understood the entire training and testing pipeline for Siamese networks, including its paired data representation.
:::



