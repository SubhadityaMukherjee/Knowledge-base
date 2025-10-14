
---
toc: true
title: Building the Word2Vec Model in Gensim

tags: ["article"]
date modified: 
date created: 
---
# # Building the Word2Vec Model in Gensim

:::section{.abstract}

## Overview
Word2Vec is a family of models that can take large corpora and represent them in vector space. These representations, also known as word embeddings, are extremely useful as they help us perform many tasks in NLP. From recommender systems to analysing sentiments from internet feeds to large-scale chatbots, word embeddings have brought life to the field of NLP for decades. Word2Vec, one of the older models, is relatively simple to implement. After implementing it we will use word embedding [visualization](../../KB/visualization.md) to further understand how the model works.
:::
:::section{.scope}

## Scope
This article covers the following topics:
- What are Word2Vec and Gensim.
- How to train a Word2Vec model using a text corpora.
- Parameters that can be tweaked in a Word2Vec model.
- How to load and pre-process text for Word2Vec.
- How to perform word embedding visualization in TensorBoard. 
:::
:::section{.main}

## What Are We Building?
In this article, we are modeling text data by converting a large corpora of text into a Vector model using Word2Vec. We will be using the Python library gensim to do so. We also will build the pipeline needed for word embedding visualization using the Tensorflow Embedding Projector as well as save the trained model for inference.

### Problem Statement
Our problem statement for this article is to create a pipeline using gensim that uses Word2Vec to process a text corpora, visualize the embeddings, and save the trained model to disk.

### Pre-Requisites
Before moving to the actual implementation, there are some pre-requisite topics that we need to know. A summary of them is as follows.

#### Embeddings and Word Embedding Visualization
The output of a Word2Vec model is a word embedding. There are many other models which give similar embeddings, some better than Word2Vec as well. These are synonymous with word vectors for our use case. 

#### Stopwords
Common words like "the", "to", etc., do not add much to the model but can negatively influence the embedding.

#### CBOW
A continuous bag of words uses a single hidden layer NN to predict a source word based on its neighbouring words. It uses a sliding window over the sentence to generate these pairs. Consider these examples as (X, Y) pairs to be passed into a model. 
An example: Given the sentence "I love gensim a lot" and a sliding window of 2, we get ([I, gensim], love), ([love, a], gensim) etc

#### Skip-gram
Skip Grams are a mirror of CBOW. It also uses a similar single hidden layer NN with a sliding window but uses the context words to predict the source word. 
An example: Given the sentence "I love gensim a lot" and a sliding window of 2, we get (love, [I, gensim]), (gensim, [love, a]) etc

### How Are We Going To Build This?
We are going to load a custom data file as an input to the model and preprocess it to make it fit for the model. After that, we will load the gensim implementation of Word2Vec and train it on the data we loaded. Once the model is done training, we will export the model to disk and load it the trained model using Tensorflow Embedding Projector for word embedding visualization. In the process, we also will save and load the model for further inference. 

### Final Output
The final output that we will get from the model is the text corpora that we load converted to vector space. This vector space can then be used to find similar words from the text and be passed to other neural network models if required. An example word embedding might look something like this.
 

## Requirements
To create a Word2Vec model, we need to first understand what it is. We will also be looking at the library Gensim where we obtain the Word2Vec model from.

### What Is Word2Vec?
Word vectors are a numerical representation of text content. Word2Vec is a model that converts large text corpora to a vector representation as  doing so provides the corpora with the following properties :
- Since they are converted to numerical vectors, they can be fed into any numerical model, such as a neural network. 
- The converted vectors can be compared by using distance metrics such as the [Cosine Distance](../../KB/Cosine%20Distance.md) function $cos(\theta) = \frac{A\cdot B}{||A||\cdot||B||}$ ( where A and B are vectors). These metrics make it easy to find related words like the one we want to achieve.

### What is Gensim?
Gensim is a text processing library that lets us train models like Word2Vec very quickly. The library has many more features, such as finding related documents using trained word embeddings and other methods of vectorization that are beyond the scope of this article.

## Building Word2Vec Model with Gensim
Now that we have understood the problem statement, we can start building the model using gensim. We first load all the required packages and data. 

### Loading Packages and Data
Before we build the Word2Vec Model, we need to load a few packages along with the data. These packages can be installed using pip. (Eg : `pip install gensim`) if they are not already present on the system that is being used.
We also download the stopwords and punctuation data from nltk.

```python
import nltk  
nltk.download('stopwords')  
nltk.download('punkt')
nltk.download('gutenberg')
import string
from nltk.corpus import stopwords
from nltk import word_tokenize
from gensim.models import Word2Vec as w2v
```

After this, we load the data.
For this demo, we will be using text from the book "Emma" by "Jane Austen". This dataset is a public domain dataset from Project Gutenberg that comes with nltk. We can get it using the following code. 
```python
import nltk
nltk.download('gutenberg')
!cp /root/nltk_data/corpora/gutenberg/austen-emma.txt sample.txt
```
We can also use custom text by creating a text file called "sample.txt" in the same directory as the code and pasting whatever we want. (Make sure it is English text).

### Data Preprocessing
After loading the data, we need to pre-process it to be able to pass it to the model by removing stopwords and punctuation and converting the words into lowercase tokens. We should get something like this `['emma', 'jane', 'Austen', '1816']`

```python
sw = stopwords.words('English') # this is a list of stopwords
# Function to remove stopwords per line if they are present in the line
def rem_stops_line(line, words):
    if len(line) >1:
        return [w for w in line if w not in words]
    else:
        return line
        
# Remove stop words for an entire text. Separate functions make it easier to parallelise if required.
def remove_stops(text, words = SW):
    return [rem_stops_line(line, words) for line in text]
    
# Open the file and convert it to a list of lines
with open('sample.txt', 'r') as f:
    lines = f.readlines()

# Remove new lines, convert all to lowercase, remove punctuation and stop words and tokenise
lines = [line.rstrip('\n').lower() for line in lines]
lines = [line.translate(str.maketrans('', '', string.punctuation)) for line in lines]
lines = [word_tokenize(line) for line in lines]
filtered_lines = remove_stops(text = lines, words = SW)

print(filtered_lines[:10])
```

### Gensim Word2Vec Model Training
Once both the data and the model have been loaded, we can train it on the data using the following code.

```python
w = w2v(
    filtered_lines,
    min_count=3,  
    sg = 1,       # 1 for skip-gram, 0 for cbow
    window=7   # sliding window size
)      
```

### Parameters of the Word2Vec Model
The Word2Vec model implemented in gensim has a few parameters that we can tune based on the task. They are explained as follows:
- **sentences** : This is the preprocessed input text.
- **size** : This is the maximum dimension size of the output vector.
- **window** : This is the sliding window size.
- **min_count** : The minimum word frequency below which words would not be passed to the model.
- **workers** : This is the number of parallel threads for processing.
- **sg** : 1 for the Skip Gram model, 0 for the CBOW model.
	- CBOW is prone to overfitting words that frequently appear in the same contexts, so try SkipGrams as well.
	- Skip grams need more data and are more resource intensive but perform better. Choose it based on the task at hand.
- **iter** : This is the number of iterations the model will update it's gradients for.
Tweaking these parameters also help improving the accuracy of the word embedding visualization.

### Compute Similarities
The Word2Vec model can also be used to find similar words in a text. 
We can find words similar to a random word we pick from the text to see our model works.
Since we used data from Emma, let us try searching for the word "book".
```python
print(w.wv.most_similar('book'))
```
We get the following words and how related the model thinks they are to the word "book".
```plaintext
[('peace', 0.9995625615119934), ('exercise', 0.999549388885498), ('burst', 0.9995266199111938), ('purpose', 0.9995185732841492), ('meet', 0.9995156526565552), ('mei', 0.9995115995407104), ('move', 0.9995064735412598), ('week', 0.9995056986808777), ('views', 0.9995036125183105), ('persons', 0.9995019435882568)]
```

### T-SNE Visualizations
To see what the embedding space looks like, we can give these embeddings to Tensorboard.
To do so, make sure the model is saved. Here we have saved it as "wvecemma". Now we use a script that comes inbuilt with gensim to convert our Word2Vec model to the Tensorboard format.

```sh
python -m gensim.scripts.word2vec2tensor -i "wvecemma" -o "model"
```
We get two files, "model_tensor.tsv" and "model_metadata.tsv".

 To convert the model to a Keras Embedding, use the code (for model w), `w.wv.get_keras_embedding()`

Now we can either open Tensorboard (if you have it installed) and navigate to this folder and open the generated files, or go to this website [Tensorflow Projector](http://projector.tensorflow.org/).
On the website, click the Load button. For Step 1, choose the "model_tensor.tsv" file, and for Step 2, choose the other one. 

We can then see the embeddings directly.

[IMAGE {1} {Embedding Projector} START SAMPLE]
![Embedding Projector](https://hackmd.io/_uploads/SJXZRrJuo.png)
[IMAGE {1} FINISH SAMPLE]

### Saving and Loading the Model
To prevent having to train again, we save the model to disk using the following code. 
```python
w.wv.save_word2vec_format("wvecemma") # save to disk 
```
This model can then be loaded for inference during production using the following code.

```python
model = gensim.models.KeyedVectors.load_word2vec_format("wvecemma.bin.gz", binary=True) # load from disk
```

:::
:::section{.summary}

## Conclusion
- This article taught us how to implement the Word2Vec model in gensim. 
- We learnt how to perform word embedding visualization using the TensorBoard Embedding Projector.
- We also learnt how to use our own data to train a Word2Vec model.

:::



