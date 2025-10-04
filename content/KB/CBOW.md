---
toc: true
title: CBOW

tags: ['nlp']
date modified: Wednesday, December 7th 2022, 11:45:39 pm
date created: Wednesday, December 7th 2022, 11:00:00 pm
---

# CBOW


- Continous implementation of [Bag of words](Bag%20of%20words.md)
- tries to predict the current target word (the center word) based on the source context words (surrounding words)
- **_“the quick brown fox jumps over the lazy dog”_**, this can be pairs of **_(context_window, target_word)_** where if we consider a context window of size 2, we have examples like **_([quick, fox], brown), ([the, brown], quick), ([the, dog], lazy)_** and so on
- context window
- ![[Pasted image 20221207231047.png]]
- several times faster to train than the skip-gram, slightly better accuracy for the frequent words.
- CBOW is prone to overfit frequent words because they appear several time along with the same context.
- tends to find the probability of a word occurring in a context
- it generalizes over all the different contexts in which a word can be used
- also a 1-hidden-layer neural network
- The synthetic training task now uses the average of multiple input context words, rather than a single word as in skip-gram, to predict the center word.
- Again, the projection weights that turn one-hot words into averageable vectors, of the same width as the hidden layer, are interpreted as the word embeddings.



