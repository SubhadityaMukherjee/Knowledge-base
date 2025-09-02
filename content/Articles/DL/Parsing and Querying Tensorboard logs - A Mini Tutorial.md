---
toc: true
title: Parsing and Querying Tensorboard logs - A Mini Tutorial

tags: ["article"]
date modified: 
date created: 
---
# Parsing and Querying Tensorboard logs: A Mini Tutorial

So, you wanted to parse your Tensorboard logs, didn’t you? Did you try using GPT-3? OH! GPT-4? Well. Guess that didn’t give you what you wanted. 
Yeah, me neither. So here we are.
Read on and you will find out how to take all the runs you logged to Tensorboard, clean them up, and put them in a single DataFrame. From there, you can query it as you would any other table. 

## What do we want?
Tensorboard is one of the more popular means of logging your deep learning experiments. The issue though, is that it is hard to run custom queries over the already-created graphs. Now, if you were saving your results separately, this would not be an issue. But you probably weren’t were you? (Yeah, me neither.)
So we want to iterate over all the logs, for every file we create rows and then columns for each of the tags you saved (eg: Loss, accuracy, etc.)
And as a bonus, this script also takes into account all those juicy images you saved from the last time you wanted to try running a DCGAN, again. (Or a cats and dogs classifier, I don't know)

## Shush and show me the code?!
Yes, I know this could just be a code snippet on Stack Overflow and there was no real need for this article. If you are an intermediate/advanced programmer, honestly just skip ahead and grab the code [here](https://gist.github.com/SubhadityaMukherjee/83b4477bbc0cf0786e61a5f4bb895fe1). 

Now if you did go and skip ahead and realized that it made no sense, welcome back. Read on and hopefully, your doubts will be answered.

## Imports
As usual, we need to grab some libraries for this to work. You probably have most of them anyway. We need *os* and *pathlib* to read the files, *pandas* for the dataframe, and *numpy* if you want to further process your data. *Tqdm* is a little progress bar helper that prints a pretty little progress bar as you wait for your loop to finish running. *PIL* will be used to read the Image files. *BytesIO* and *base64* will be used to decode the images from Tensorboard so we can save them to the dataframe.
Finally, we also do need the *Tensorboard* package, but if you didn’t have that already then what are you doing here? 
Why *pickle* you might ask? You will see.

All of these packages are available either as a pip or a conda/mamba install. So just run `pip install <x>` and it should hopefully work.

Now that we have that out of the way, let’s define the path where your logs are. (The same one you pass to the —logdir argument on Tensorboard)

```python
import os
import pandas as pd
from tensorboard.backend.event_processing.event_accumulator import EventAccumulator
from tqdm import tqdm
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import base64
from io import BytesIO
from PIL import Image
import pickle

main_path = './runs/' # CHANGE THIS
```

## Find TFevent files
Tensorboard uses a custom format that it calls a ‘tfevent’. If you do look at your logs, you will see that the format of the files is either ‘tfevent’, ‘checkpoint’, and of course whatever else you have saved.

The first step is then to just read all the tfevent files from the directory. We will use the walk function and pathlib to find all of the relevant files. 
Why convert it to a Path object? Using the Path function from the pathlib instead of just a string for the directories will allow us to quickly perform operations on the directory if we need it. (For path.name will give us the file name from the full path.) 
We just save the complete paths of each of the files to an array here.

```python
def get_event_files(main_path):
    """Return a list of event files under the given directory"""
    all_files = []
    for root, _, filenames in os.walk(main_path):
        for filename in filenames:
            if "events.out.tfevents" in filename:
                all_files.append(str(Path(root) / Path(filename)))
    return all_files
```

## Create DataFrame
Our objective is to collect all the metadata from the logs and convert it to a single DataFrame. To this accord, we get a list of all the relevant tfevents using the previous function. We then create an empty dictionary to store file-wise information.
The EventAccumulator function uses the Tensorboard API to read the tfevent file and so we run every file through it. To make sure we read the logs from the start, we also reload the object. 
Once we have this object, we can pass it to a function that will return the relevant tags to a dictionary with the file name as a key and the tags as a value. This function will be discussed in the next section.
Once we run over all the files, we have a dictionary of dictionaries with all the information we need. Now, pandas provides a function to convert a nested dictionary to a DataFrame, so we use it directly. 
If you look at this output, you will see that the rows are the tags while the columns are individual files. If this version works for you, then do use it! 
I find it easier to have the tags as column names and each row of the DataFrame for file information. I also wish to access the file names later so I use the *reset_index()* function that will essentially make sure all the columns have names here. (In this case, the file names will be named ‘index’. You can change this if you want by passing in a *columns=[<list of names>]* that you want to the *from_records* function.)

```python
def process_runs(main_path):
    all_files = get_event_files(main_path=main_path)
    all_dict = {}
    for files in tqdm(all_files, total = len(all_files)):
        event_acc = EventAccumulator(files)
        event_acc.Reload()
        temp_dict = process_event_acc(event_acc)
        all_dict[files] = temp_dict
    return pd.DataFrame.from_records(all_dict).T.reset_index()
```

## Process an Event
Now for the main bit. Depending on what you were training, you probably have many types of logs that you saved. In my case, these are Scalars, Tensors, or Images. The following function processes these, but it is easy enough to extend to whatever you want.
From the *process_runs* function, we pass in the EventAccumulator object to this function. This object contains the tags that we saved each of our logs as. (For eg: ‘Train/Acc’, ‘Train/Loss’ etc.) 
I do not want to manually type these every time, and would rather use a function to do that for me.

These tags are first divided into the category of object it is, for instance, “images”, “scalars”, “histogram” etc. We will need to write a separate pre-processing step for each object depending on what information we want from them.

Note that for each of the tags, the subtags are the names of the actual values that we want. (Eg: For the tag ‘scalars’, we have ‘Train/Acc’).

### Scalars
These are probably numerical values that you saved. Say the loss, accuracy, number of classes, etc. For this type of data, we first read the Scalar value using the event_acc.Scalars command. We need to pass in the name of the subtag that we want to look at (eg: ‘Train/Acc’). 
Now, if you were looking at values that change throughout training, you will probably get a list here. For instance, you will get an epoch-wise accuracy list. Since I only want the final accuracy/loss etc, I am only returning the final index. 
Feel free to customize it to whatever you need.

### Tensors
The name gives it away, but these are the values that you might find have the extra tag ‘/text_summary’. We can access these by using the event_acc.Tensors command. Now if you inspect the object, you will see that the actual value can be found in the first index of this object. The value is stored in the ‘string_val’ field of this object, so we take that out and again index it into the first element. (You will see why if you print the object. No further explanations are given because that’s just how the API is. It also depends on what exactly you want to save of course.) 
Now if you look at the final output, you will find that it looks something like b’some value’. This is an encoded string, and to convert it to a normal string, we have to decode it as an ASCII character string. Pretty easily done.

### Images
Images are a bit of a complicated case here. If you look at the tensor board object that we get from event_acc.Images, you will see that it is a Bytes object and not a numpy array/PIL image. This is just the format Tensorboard chose, so all we can do is accept it and convert it to our needs.
After indexing into the correct component of the object, the field ‘encoded_image_string’ holds, well, the encoded image string. We take that and convert it to a BytesIO object. This is a format that PIL can read as an image, so we read it as one. 

### Other formats
Now if you have something like a histogram, you hopefully get how to process it. Use event_acc.Histogram for instance, and then apply whatever transform you want to it. I do not need them yet, but I might add them to this article later on. 

```python
def process_event_acc(event_acc):
    """Process the EventAccumulator and return a dictionary of tag values"""
    all_tags = event_acc.Tags()
    temp_dict = {}
    for tag in all_tags.keys():
        if tag == 'scalars':
            for subtag in all_tags[tag]:
                temp_dict[subtag] = [tag[-1] for tag in event_acc.Scalars(tag=subtag)][-1]
        if tag == 'tensors':
            for subtag in all_tags[tag]:
                temp_dict[subtag.replace('/text_summary', "")] = [tag[-1] for tag in event_acc.Tensors(tag=subtag)][0].string_val[0].decode('ascii')
        if tag == 'images':
            for subtag in all_tags[tag]:
                temp_dict[subtag] = Image.open(BytesIO(event_acc.Images(subtag)[1].encoded_image_string))
    return temp_dict
```

## A Caveat
Now, there is a catch. After creating the DataFrame, if you save it as a "csv" object, it becomes impossible to load the images back. This happens because the object is saved as a string like ‘<PIL Image>` instead of the actual image. 
Instead of that, you can save the DataFrame as a pickled object. 

```python
import pickle
with open("pickled_df.pkl", "wb+") as f:
	pickle.dump(combined_df, f)

with open("pickled_df.pkl", "rb+") as f:
	combined_df = pickle.load(f)
```

## Load and clean DataFrame
To get the DataFrame we so badly desire, we just run the functions we wrote before. And hopefully, if everything worked fine, you can go home and sleep. (Or if not, sorry! I hope you only have a few hours of your workday left.)
Another step I want to mention is the ability to ignore failed runs. If you were tracking failure, then just use that object. If you weren’t, then just look at the columns that are written at runtime. For instance, I always write the name of the experiment, and if even a single epoch was completed, then there should be a validation loss as well. 
To filter the data, I just take the rows that have values for these. (As usual, depends on what you want.)

```python
combined_df = process_runs(main_path=main_path)
combined_df = combined_df[(~pd.isnull(combined_df['experiment_name'])) & (~pd.isnull(combined_df['Loss/Val']))]
combined_df.head()
```

## Display images
The final part of the code is looking at the images. Filter out what you want, and pick the row and column name as you would index a text object. Done! If you are using a Jupyter notebook, then you should see the image pop up. If you are running this program as a script, you will have to use <image>.show() 
```python
filtered_df = combined_df[(~pd.isnull(combined_df['converted_proxy'])) & (~pd.isnull(combined_df['original_images']))]
filtered_df.iloc[0].original_images
```

## What next?
Depends on how much you are getting paid. :)
Jokes aside, this is just a regular DataFrame now. So you can write all the queries you want. Do you want to know how badly your model did? Sure, look at the columns. Did you write some complex logic and now forgot what your actual project was? Oops. Open the DataFrame in Excel and cry.
But I am sure you will manage. After all, you’ve got this far haven’t you?

## Why not Wandb/W&B etc etc
I do want to mention that I am not against any of the other logging platforms. Honestly, they do some pretty great work. But I am used to Tensorboard, and having my data offline and not on someone else’s cloud (jokes on me, this article is on someone else’s cloud) is nice. 
Use whatever works for you. Or write your own. Heck, use a CSVLogger and save what you want directly to a CSV. 

## Fin
This article is in the hopes that it will help someone out. Maybe have the help that I did not. I do not know who it will reach. But to whoever it does, best of luck :)

Like these/Want more? Buy me a coffee! [Kofi](https://ko-fi.com/subhadityamukherjee)

Want articles on something specific? Just ask!

You can always contact me on [LinkedIn](https://www.linkedin.com/in/subhaditya-mukherjee-a36883100), or drop me an [[mailto:msubhaditya@gmail.com|Email]]. For all the code, drop by my [Github](https://github.com/SubhadityaMukherjee/).



