---
toc: true
title: gensim

tags: ['language']
date modified: Monday, January 16th 2023, 7:00:22 pm
date created: Wednesday, December 7th 2022, 10:38:13 pm
---

# Gensim
- library


## w2vec Code
```py
nltk==3.6.1  
node2vec==0.4.3  
pandas==1.2.4  
matplotlib==3.3.4  
gensim==4.0.1  
scikit-learn=0.24.1
```
```py
import nltk  
nltk.download('stopwords')  
nltk.download('punkt')

import pandas as pd

import nltk

import string

import matplotlib.pyplot as plt

from nltk.corpus import stopwords

from nltk import word_tokenize

from gensim.models import Word2Vec as w2v

from sklearn.decomposition import PCA

# constants

PATH = 'data/shakespeare.txt'

sw = stopwords.words('english')

plt.style.use('ggplot')

# nltk.download('punkt')

# nltk.download('stopwords')

# import data

lines = []

with open(PATH, 'r') as f:

for l in f:
	lines.append(l)

# remove new lines
lines = [line.rstrip('\n') for line in lines]

# make all characters lower
lines = [line.lower() for line in lines]

# remove punctuations from each line
lines = [line.translate(str.maketrans('', '', string.punctuation)) for line in lines]

# tokenize
lines = [word_tokenize(line) for line in lines]

def remove_stopwords(lines, sw = sw):
    '''
    The purpose of this function is to remove stopwords from a given array of 
    lines.
    
    params:
        lines (Array / List) : The list of lines you want to remove the stopwords from
        sw (Set) : The set of stopwords you want to remove
        
    example:
        lines = remove_stopwords(lines = lines, sw = sw)
    '''
    
    res = []
    for line in lines:
        original = line
        line = [w for w in line if w not in sw]
        if len(line) < 1:
            line = original
        res.append(line)
    return res
    
filtered_lines = remove_stopwords(lines = lines, sw = sw)

w = w2v(
    filtered_lines,
    min_count=3,  
    sg = 1,       # 1 for skip gram, 0 for cbow
    window=7      
)       

print(w.wv.most_similar('thou'))

emb_df = (
    pd.DataFrame(
        [w.wv.get_vector(str(n)) for n in w.wv.key_to_index],
        index = w.wv.key_to_index
    )
)
print(emb_df.shape)
emb_df.head()

pca = PCA(n_components=2, random_state=7)
pca_mdl = pca.fit_transform(emb_df)

emb_df_PCA = (
    pd.DataFrame(
        pca_mdl,
        columns=['x','y'],
        index = emb_df.index
    )
)

plt.clf()
fig = plt.figure(figsize=(6,4))

plt.scatter(
    x = emb_df_PCA['x'],
    y = emb_df_PCA['y'],
    s = 0.4,
    color = 'maroon',
    alpha = 0.5
)

plt.xlabel('PCA-1')
plt.ylabel('PCA-2')
plt.toc: true
title('PCA Visualization')
plt.plot()
```



