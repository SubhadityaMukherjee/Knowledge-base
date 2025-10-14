
---
toc: true
title: Masked Language Modeling in BERT #scalar

tags: ["article"]
date modified: 
date created: 
---
# [Masked Language Modeling](../../KB/Masked%20Language%20Modeling.md) in BERT #scalar
masked language model explained

:::section{.abstract}

## Overview
Language modelling is a massive domain and has many sub-research areas. One such domain involves understanding contextual information about words in a sentence. This task can be done in many ways, and masked language modelling is one such method. In the past few years, Transformer based models have reached SOTA(state of the art) in many NLP domains. BERT is one such model. In this article, we will understand how to train BERT to fill in missing words in a sentence using MLM.

:::
:::section{.scope}

## Scope of the Article
This article covers the following topics:
- [Masked Language Modeling](../../KB/Masked%20Language%20Modeling.md) explained in an easy-to-understand manner
- Quickly recap all the pre-requisite terms to build an MLM model
- Go over some libraries that are essential to MLM
- How to build a BERT-based MLM model using our data in Tensorflow/Keras

:::
:::section{.main}

## [Masked Language Modeling](../../KB/Masked%20Language%20Modeling.md) Explained
To a NN model, the word context has no meaning. So, we need to find ways to make the model consider surrounding words to learn which context words appear. For example, consider the sentence, "I am eating an ice cream". In this, the "ice cream" is being "eaten". What would an appropriate word be if we now remove the word "eating" and have the sentence as "I am ___ an ice cream"? We can consider something along the lines of "licking", "eating", "sharing", etc. However, we cannot say "drowning", "cycle", "chair", or other random words.

In the same way, to ensure the model learns which word is appropriate, it needs to understand the structure of language. As modellers, we need to help it do so. 
Quite simply, all we do is give the model inputs with blanks as a "token" `<MASK>` along with the word that should be there. We can create data in this format by taking any text and running over it. How to do so will be explained later on.

## Quick Recap
This section gives a small recap of all the important concepts we need to understand the code.

### Tokens
Tokens can be considered parts of a sentence that contribute to understanding. A sentence such as "I am Jane Austen" can have the tokens `["I", "am", "Jane", "Austen"]`. As a computer does not understand words, we need to convert these to numerical values. To do so, we give each word a unique ID. Something like `[100, 101, 102, 103]` etc.

### Attention
One of the most important concepts in Machine learning today, attention mechanisms give models the power to decide where to look in an input. Compared to CNNs, this makes models such as Transformers perform much better as it simultaneously learns which parts of the input would be better along with what the input could be classified. 

### Transformers
Transformers are a large family of models that employ different variants of attention mechanisms. They first started in NLP but have also branched out to computer vision due to their immense potential. They generally have an Encoder-Decoder architecture with multiple "heads". Each head is responsible for its attention.

### BERT
BERT is part of a sub-family of transformer architectures made for NLP and led to a sea of other new models that reached SOTA. It can be used in many different contexts, especially MLM, next-word prediction, question answering and many more.

### Transfer Learning
A training paradigm that changed the DL world by allowing any researcher with limited resources to use SOTA models for inference and fine-tune them to their needs. A model like BERT requires Terabytes of data before it can be trained to extremely high levels. This level of computing is almost impossible for most people to have apart from companies with massive funding and resources. However, now we can use their trained models and make them work for our tasks.

### Stopwords
Words that do not add much value to the model but are repeated enough times for it to become a problem. These are generally removed before modelling.

## MLM vs CLM vs Word2Vec
The major difference between MLM and CLM is that CLM can only take into account words that occur before it in a sentence, unlike MLM, which is bi-directional. This difference means that CLM does better for generating large amounts of text. However, MLM is better for contextually understanding text (refer to the [Masked Language Modeling](../../KB/Masked%20Language%20Modeling.md) Explained section).
Word2Vec, on the other hand, has similar ideas but the embeddings it generates have weaker contextual information than Transformer based models. The outputs it produces can also be used as a part of BERT training, although it is not usually required.

## Libraries We Need
We need a few libraries to make this work.

### Tensorflow/Keras
TF is one of the major DL libraries in Python. We will be using it for training our model.

### Hugging Face Transformers
This library is one of the recent developments in the open-source community. It is a database of trained models and datasets that can be directly used in any codebase. They have thousands of tasks, making it extremely easy to get results fast. We will use their pre-trained BERT model.

### NLTK
A text processing library that we will use to clean up our text before passing it to the model.

### Seaborn/Matplotlib
These libraries are used for plotting our training performance.

## Implementation
Now for the code.

### Imports
We first import all the required packages. We also download the stopwords and punctuation data from nltk.

"`python
import nltk  
nltk.download('stopwords')  
nltk.download('punkt')
nltk.download('gutenberg')
import string
from nltk.corpus import stopwords
import seaborn as sns

from transformers import BertTokenizer, TFBertForMaskedLM
import tensorflow as tf
import numpy as np
import re
import matplotlib.pyplot as plt
sns.set()
```

### Data
For this demo, we use text from the book "Emma" by "Jane Austen". This dataset is a public domain dataset from Project Gutenberg that comes with nltk. We can download it using the following code. 
"`python
import nltk
nltk.download('gutenberg')
!cp /root/nltk_data/corpora/gutenberg/austen-emma.txt sample.txt
```
We can also use custom text by creating a text file called "sample.txt" in the same directory as the code and pasting whatever we want. (Make sure it is English text).

We then pre-process the data by removing stopwords and punctuation and converting the words into tokens BERT needs. Since every Transformer model has their configuration of tokens in the pre-trained model, we will use the tokenizer that Hugging face provides us. 

(Note: Here, we only take the first 1000 lines from the text. Language models take a long time to train; this is just a demo. If we have GPUs, the entire data can be used.)
"`Python
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

sw = stopwords.words('english') # this is a list of stopwords

# Take first 1000 sentences for demo purposes
with open('sample.txt', 'r') as f:
    lines = f.readlines()[:1000]
# Remove new lines, convert all to lowercase, remove punctuation and stop words and tokenize

lines = [line.rstrip('\n').lower() for line in lines]
lines = [line.translate(str.maketrans('', '', string.punctuation)) for line in lines]

def rem_stops_line(line, words):
    # Function to remove stopwords per line if they are present in the line
    if len(line) >1:
        return [w for w in line if w not in words]
    else:
        return line
        
def remove_stops(text, words = sw):
    # Remove stop words for an entire text. Separate functions make it easier to parallelize if required.
    return [rem_stops_line(line, words) for line in text]
    
filtered_lines = remove_stops(text = lines, words = sw)
inputs = tokenizer(lines,max_length=100,truncation=True,padding='max_length',return_tensors='tf')
```

### Masked Language Model Explained Further
We use the model from the Transformers library directly. The uncased model converts all text into lowercase. Other models do not, and any of them can be used. This one was chosen for the sake of this demo.
"`Python
model = TFBertForMaskedLM.from_pretrained('bert-base-uncased')
```

In [Masked Language Modeling](../../KB/Masked%20Language%20Modeling.md), we explained that every sentence needs to be converted to a format with words masked using a special token, `<MASK>`. We can do that by using the tokenized words and making the model aware of which token number corresponds to this special token. (In this case, it is 103). In the original paper, token numbers 101 and 102 were replaced, but we ignore that here. (It is not relevant for now.)

"`Python
# MASK
inp_ids = []
lbs = []
for idx, inp in enumerate(inputs.input_ids.numpy()):
    current_tokens = list(set(range(100)) - 
                         set(np.where((inp == 101) | (inp == 102) 
                            | (inp == 0))[0].tolist()))
    # Find number of tokens to mask
    num_token_masked = 0.15 * len(current_tokens)
    token_to_mask = np.random.choice(np.array(actual_tokens), 
                                     size=int(num_token_masked), 
                                     replace=False)
    # Store special token and inform model
    inp[token_to_mask.tolist()] = 103
    inp_ids.append(inp)
    
# Convert the tokens to tensor format
inp_ids = tf.convert_to_tensor(inp_ids)
inputs['input_ids'] = inp_ids
```

### Training the Model
Now that we have all the required data and the model, we need to train it on our data.
If the system does not have a GPU or access to a cloud GPU is unavailable, this model will take a very long time to train. Consider using lesser data.

Considering we have a GPU, we first check if TF can find it.
"`Python
print('GPU name: ', tf.config.experimental.list_physical_devices('GPU'))
```

We use a Sparse Categorical Crossentropy loss with logits enabled. (logits are enabled if the model does not end with a Softmax. BERT does not.). We use a learning rate of 1e-3 for the Adam Optimizer. 
Finally, we run training for around ten epochs.
"`Python
# Compile and Train
lr = 1e-3
loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=lr),loss=loss)
history = model.fit([inputs.input_ids,inputs.attention_mask],inputs.labels,verbose=1,batch_size=16,epochs=10)
```

### Loss
We plot the loss per epoch to see if our model is learning anything.
We can see that the loss has decreased, which is a good sign! Our model is learning. More data and longer training will help the model be better than before.

### Prediction
Just training a model is useless. We need to be able to use it for prediction. To do that, we need to define a few functions. We need to be able to find the `<MASK>` tokens in the sentence, we need to tokenize the sentence and pass it into the model for prediction. And finally, we need to do this for multiple sentences. 
The following functions do exactly these. 

```python
def find_masks(inp):
    # Find position of the masks in a sentence
    return np.where(inp.input_ids.numpy()[0] == 103)[0].tolist()

def single_prediction(model, inp, mask_loc):
    # Prediction for all the positions of the masks
    return model(inp).logits[0].numpy()[mask_loc]

def return_prediction(model, query):
    # Return a prediction for a single sentence
    inp = tokenizer(query,return_tensors='tf')
    mask_loc = find_masks(inp)
    # Find prediction with the highest confidence
    predicted_tokens = np.argmax(single_prediction(model, inp, mask_loc),axis=1).tolist()
    # Decode the numerical value of the returned ID back to the word 
    return tokenizer.decode(predicted_tokens)

def multiple_preds(model, query_list):
    # Return predictions for a list of queries
    preds = [f"{x} -> {return_prediction(model, x).split(' ')}" for x in query_list]
    for i in preds: print(i)
```

## Predictions
After training, we can finally give the model a practice exam! Since we fine-tuned it on the book "Emma", we give it the following sentences. `["too well [MASK] for her", "nice to [MASK] her", "Emma [MASK] a girl who wanted a [MASK]"]`

"`Python
query_list = ["too well [MASK] for her", "nice to [MASK] her", "Emma [MASK] a girl who wanted a [MASK]"]
multiple_preds(model, query_list)
```

As an output we get the following. We see that it performs quite well even with such a short training! 

"`plaintext
too well [MASK] for her -> ['suited']
nice to [MASK] her -> ['see']
Emma [MASK] a girl who wanted a [MASK] -> ['was', 'chance']
```

## Further Tips
- Language models are generally very heavy to use. If possible, using Mixed Precision training helps
- Having more GPU memory is more useful than having a faster GPU for language models
- Multiple GPUs are useful for expanding available memory
- There are smaller variants of BERT that use less memory. 
- Hugging Face has a huge list of models that we can use. Trying them might lead to better results.
- To get over the overwhelming number of pre-trained models, pick the task and find benchmarks in that task. [PaperswithCode](https://paperswithcode.com/methods) is a great place to start.

:::
:::section{.summary}

## Conclusion
This article showed us masked language modelling explained. We learnt the following:
- What MLM is and when to use it. 
- How to pre-process our data for MLM
- How to fine-tune pre-trained BERT models for MLM
- How to perform predictions over multiple sentences with our fine-tuned models.

:::



