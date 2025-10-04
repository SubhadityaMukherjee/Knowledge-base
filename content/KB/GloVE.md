---
toc: true
title: GloVE

tags: ['architecture']
date modified: Wednesday, December 7th 2022, 10:58:44 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---


# GloVE

## Explanation
- [GloVe: Global Vectors for Word Representation](https://www.aclweb.org/anthology/D14-1162/)
- [Word2Vec](Word2Vec.md) relies only on local information of language. That is, the semantics learnt for a given word, is only affected by the surrounding words.
- [Unsupervised Learning](Unsupervised%20Learning.md) algorithm which captures both global statistics and local statistics of a corpus
- aggregated global word co-occurrence statistics from a corpus, and the resulting representations showcase interesting linear substructures of the word vector space
- whether distributional word representations are best learned from count-based methods or from prediction-based methods
- probe the underlying co-occurrence statistics of the corpus
- reformulated [Word2Vec](Word2Vec.md) optimizations as a special kind of factorization for word co-occurence matrices
- Note that GloVe does not use neural networks
- utilizes this main benefit of count data while simultaneously capturing the meaningful linear substructures prevalent in recent log-bilinear prediction-based methods like [Word2Vec](Word2Vec.md)
- global log-bilinear [LinearRegression](LinearRegression.md) model for the [Unsupervised Learning](Unsupervised%20Learning.md) of word representations
- ![](../images/Pasted%20image%2020221207225733.png)
- There’s a straight red column through all of these different words. They’re similar along that dimension (and we don’t know what each dimensions codes for)
- There are clear places where “king” and “queen” are similar to each other and distinct from all the others. Could these be coding for a vague concept of royalty?

## Analogies
- ![](assets/king-man+woman-gensim.png)



