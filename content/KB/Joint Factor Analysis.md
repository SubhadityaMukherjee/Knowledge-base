---
toc: true
title: Joint Factor Analysis

tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:24 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Joint Factor Analysis
- [Front-end Factor Analysis for Speaker Verification](http://groups.csail.mit.edu/sls/publications/2010/Dehak_IEEE_Transactions.pdf)
- Joint Factor Analysis (JFA)
- eature extractor to learn a low-dimensional speaker representation for [Speaker Verification](Speaker%20Verification.md), which is also used to model session and channel effects/variabilities
- In this new space, a given speech utterance is represented by a new vector named total factors (called the identity-vector or the “i-vector”)
- The i-vector is thus a feature that represents the characteristics of the frame-level [Features](Features.md)’ distributive pattern
- [dimensionality reduction](dimensionality reduction.md) of the GMM supervector (although the GMM supervector is not extracted when computing the i-vector)
- extracted in a similar manner with the eigenvoice adaptation scheme or the JFA technique
- extracted per sentence
- Support-Vector-Machine-based system that uses the cosine kernel to estimate the similarity between the input data
- [Cosine Similarity](Cosine%20Similarity.md) as the final decision score
- removed the SVM from the decision proces
- no speaker enrollment
- EER
- MinDCF
- [NIST 2008 Speaker Recognition Evaluation dataset](NIST%202008%20Speaker%20Recognition%20Evaluation%20dataset.md)
- Up until d-vectors, the state-of-the-art [Speaker Verification](Speaker%20Verification.md) systems were based on the concept of i-vectors



