---
toc: true
title: Easier Deep Learning Research for Beginners

tags: ["article"]
date modified: 
date created: 
---
# Starting Deep Learning Research (PART 1): A start using FastAI #deeplearning
{{TOC}}
So, you took your first steps into Deep Learning. Maybe you read a few articles, did a course or two, and watched a bunch of videos. Or maybe you just heard so much about it that you wanted to learn more. 
Welcome. 
This is a beautiful world. It is also very overwhelming. There is so much to learn and understand. But we need to start somewhere.
This is your ticket. Enjoy the ride.

Note: This will be very long-winded as it is meant for complete beginners. It might seem very scary at first. But don’t panic. The hardest part is getting started. Hold on. Come back to it. It will take time. Slow down. Read through it. It will save you a lot of pain later on.

## Entry Requirements
- Go to this link for the code and follow along [kaggle_notebook](https://www.kaggle.com/code/subhaditya/complete-starter-fastai-v2-classification). Once that opens up, click the button next to “Accelerator” and choose GPU. Accept the terms.
- You have learned some Python. If not, go to YouTube and learn as much as you can first. Do as many examples and problems as you deem enough to understand. Come back.
- You know what a GPU is and if you have one.
- You have a computer and an internet connection.
	- If you have a powerful computer, you can set this up locally. [fastai](https://docs.fast.ai)
		- You will need an editor. I would recommend [VSCode](https://code.visualstudio.com). 
		- If you do not, that’s alright. You can still follow along.
	- Watch a small tutorial on how to use a Jupyter Notebook [here](https://www.youtube.com/watch?v=inN8seMm7UI).

## What we want to do
Today we will be teaching our little “AI” how to categorize different fruits. To do that, we need to give examples - aka the “dataset”. You can grab it from [Kaggle](https://www.kaggle.com/datasets/moltean/fruits). 
We will show our little “AI” quite a lot of images and tell it “hey, this is an Apple, this is not one” and so on, in the hope that it will learn.
The exact algorithms are not important at this stage. I believe it is first good to be able to see where to use it in practice and play around with it before diving deep. 
In the end, we want our “AI” to accurately classify the fruits that it has learned about.

## Libraries we will use
- Major Framework : [Pytorch](https://pytorch.org). Deep learning is quite a vast field, which means that code quickly starts to become complicated. There is a lot of boilerplate code that needs to be written every time you want to make something. Writing the same 200 lines of code every time is not efficient, and leads to bugs and weird errors. To avoid that, we use a framework that handles most of the hard work for us so we can focus on innovation and application. There are quite a few of these frameworks, PyTorch and [Tensorflow/Keras](https://www.tensorflow.org/) are the two major ones in Python. \
	I prefer Pytorch. There are many reasons for that. Instead of me adding to this blog about them, read this little article by the creator of the next library we will use, [link](https://www.fast.ai/2017/09/08/introducing-pytorch-for-fastai/)
- [fastai](https://www.fast.ai) FastAI was one of my first introductions to research grade Deep Learning. It is a wrapper around Pytorch that does live up to its name. Pytorch, being a general framework, focuses on the core components of Deep Learning. FastAI was made to provide a lot of ease-of-use functions that Pytorch did not. But because it’s just a wrapper, any functions that Pytorch offers can be easily accessed. 

## Grab the Data and Set Everything Up

- Make an account on [Kaggle](https://www.kaggle.com). This is not promoted or anything. It is probably one of the biggest hubs for AI code, and you will make an account sooner or later. Better to do it now.
- If you are using this [link](https://www.kaggle.com/code/subhaditya/complete-starter-fastai-v2-classification), click the 3 dots, and then click “Copy and Edit”. That will set up the data and the code for you. 
- If you are working on your machine, you can download the notebook by clicking the 3 dots, and then clicking “Download code”. Open this up in VSCode. The data can be found from [Kaggle](https://www.kaggle.com/datasets/moltean/fruits). 

## Code Imports
We will need to first import the libraries we will use.
```py
import os
from fastai.vision.all import *
from fastai.vision.widgets import *

# Set the base directory where Kaggle saves its data. Change this if you are on your machine.
root_dir = "../input/fruits/fruits-360_dataset/fruits-360/Training"
```

## Load Data
Fastai provides quite a few convenient functions to load data. Now slow down. What do we have? Think about it for a second.
We have an image and a label right? And we need to “map” the image to the label. If this does not make sense. Think about it some more. This is important.
Okay. 

Now, what does the file path for an image look like?
Something like : "../input/fruits/fruits-360_dataset/fruits-360/Test/Cantaloupe 1/r_140_100.jpg”.
What will the label be? “Cantaloupe 1” right? This is the “parent” of the path, aka the parent folder.
*This fully depends on how the data is structured. More on that later.*

```py
def get_parent_name(x): 
    return x.parent.name
```

Okay, now we need to tell the system the kind of data we are giving it.   In this case, it is Image -> Category (Label). Then we can find all the image files in the folders, and use the “get_parent_name” function to assign labels to all our data.

When we learn something in school, we are tested on it with questions we have never seen right? This helps us understand if we comprehended the topic or not. Similarly, we split the data into Train and Test sets.
We also resize the images to a single size (for convenience). 
Since we want our little “AI” to recognize objects from any angle, lighting condition, etc, we provide some “augmentation” to the data. Things like randomly changing the brightness, rotating the image, etc. The objective is to provide variation, that further improves how well our network learns.

We can then pass these instructions are create a “Data-loader”. The definition is the name itself.
```py
path = Path(root_dir) # base path
fields = DataBlock(
    blocks=(ImageBlock, CategoryBlock),
    get_items=get_image_files,
    get_y=get_parent_name,
    splitter=RandomSplitter(valid_pct=0.2, seed=42),
    item_tfms=RandomResizedCrop(64, min_scale=0.5),
    batch_tfms=aug_transforms(),
)
dls = fields.dataloaders(path)
```
‌
Okay. Does this work? Let us get a sample (or a batch as it is called in this field.) 
```py
dls.show_batch()
```
How many categories of fruits do we have?
```py
dls.c # no of categories
```

## Teaching our AI: Part 1
We have the data. Now we need the “AI”.
You must be wondering why the word has been in quotes the whole time. It is because what we are training is not an “AI”, but just a component of it, called a “Neural Network”. 
```py
learn = vision_learner(dls,
                resnet18, #architecture
                loss_func=LabelSmoothingCrossEntropy(), #loss function/objective
                opt_func=partial(OptimWrapper, opt=torch.optim.AdamW), # Optimizer
                metrics=[accuracy, error_rate],
                cbs=[MixUp]).to_fp16() #callbacks, mixed precision
```
The only things you need to know about it for now are : 
- There are many types of networks, each better at something else. These are called “architectures”. ResNet18 is one of them.
- You can train a network to learn a specific type of mapping. Be it an image -> text, audio -> labels , image -> image etc. 
- This training takes time and is mathematically pretty hard. Which is why this field is still in research. Further explanations about all of this will be given in later articles. (And others that I have written about in the past, linked at the end.)
- In addition to the architectures, we have algorithms called “Optimisers” that enable smoother learning. This will not make any sense right now. But all in due time.
- A “loss function” is fancy speak that is a way of seeing how well our network is doing while it’s learning. A mini exam if you will, in the sense that the network tries to “optimise” for this exam. The better it gets, the better your final results.
- Metrics give us somewhat precise values. Such as the grade in an exam. The “Accuracy”. Etc.
- The other weird things that you see here are:
	- cbs: [[Mixup]]

## Teaching our AI : Part 2
Let the Neural network.. drumroll.. learn!
```py
learn.fine_tune(1, wd=0.5)
learn.export("model.pkl") # Save the model
```
Fine-tune? Huh? 1? Huh? Don’t worry too much about that right now. It is called [Transfer Learning](https://ruder.io/transfer-learning/). And we are training the model for 1 epoch. (One run over all the data.). More epochs generally lead to better results.

AND WE ARE DONE!! We have a working model already. This can recognize fruits. Congratulations!!!! 

(Too many words and terms. How will I ever learn them all? I should just give up now. Breathe. One thing at a time. Go through this. Come back. Go through bits you do not understand. More intermediate articles will follow. But in the meanwhile, the links are excellent resources on getting started.)

## How Well Did We Do?
```py
from fastai.interpret import *
from fastai.vision.widgets import *
interp = ClassificationInterpretation.from_learner(learn)
interp.plot_top_losses(5, nrows=1)
```
We can use this to see what our model gets confused about. This will change as you train it more.
```py
interp.most_confused()
```

## Using The Model
Okay, the last little bit here. We now need to use this trained model on images the network has never seen. (They were in a different folder. Also called the Validation set.)
Fine, It’s an exam. Best of luck little model. I hope you do well.
```py
predictions_path = "../input/fruits/fruits-360_dataset/fruits-360/Test"

def predict_batch(self, item, rm_type_tfms=None, with_input=False): # this bit is slightly complicated. ignore it for now
    dl = self.dls.test_dl(item, rm_type_tfms=rm_type_tfms, num_workers=15)
    ret = self.get_preds(dl=dl, with_input=False, with_decoded=True)
    return ret
import random
predictions_path = Path(predictions_path)
Learner.predict_batch = predict_batch

# This is important
learn = load_learner("model.pkl")

tst_files = get_image_files(predictions_path) #same as before
tst_files = tst_files.shuffle() 
```

Now running the predictions. 
```
preds = learn.predict_batch(tst_files)
classes = learn.dls.vocab # the original categories
preds_mapped = list(map(lambda x: classes[int(x)], preds[2])) #just saving them out
```

So did it work? tst_files are the images we gave it. Preds is the output. Would you look at that?? It got most of them right :)

## Fin
What’s next? More articles. In the meanwhile, you can look at [this](https://gist.github.com/SubhadityaMukherjee/6a70d6dc74783e2addac8bed475ac220) little link with resources I have collected over the years.

You have a long way to go. But I do hope this was a good start. I know you didn’t read the whole thing. Maybe you didn’t make it till here either. I get that. I also did that when I was starting. 
This article is in the hopes that it will help someone out. Maybe have the help that I did not. I do not know who it will reach. But to whoever it does, best of luck :)

You can contact me on [LinkedIn](https://www.linkedin.com/in/subhaditya-mukherjee-a36883100), drop me an [[mailto:msubhaditya@gmail.com|Email]]



