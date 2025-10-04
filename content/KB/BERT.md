---
toc: true
title: BERT
tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:34 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# BERT
- Bidirectional Encoder rep from transformers
- Uses [Token Embedding](Token%20Embedding.md)
- [Self Supervised](Self%20Supervised.md)
- Masked [language](language.md) modeling, next sentence prediction
- ![[Pasted image 20220307183916.png]]
- [CLS] : start of classification task, [SEP] between sentences, [MASK] : masked token
- [christianversloot](https://github.com/christianversloot/machine-learning-articles/blob/main/intuitive-introduction-to-bert.md) #[[Roam-Highlights]]
    - BERT base $\text{BERT}_\text{BASE}$, which has 12 Encoder Segments stacked on top of each other, has 768-dimensional intermediate state, and utilizes 12 [Attention](Attention.md) heads (with hence 768/12 = 64-dimensional [Attention](Attention.md) heads).
    - BERT large ($\text{BERT}_\text{LARGE}$), which has 24 Encoder Segments, 1024-dimensional intermediate state, and 16 [Attention](Attention.md) heads (64-dimensional [Attention](Attention.md) heads again).
    - BERT utilizes the encoder segment, meaning that it outputs some vectors $T_i$ for every token. The first vector, $T_0$, is also called $C$ in the BERT paper: it is the "class vector" that contains sentence-level information (or in the case of multiple sentences, information about the sentence pair). All other vectors are vectors representing information about the specific token.
    - In other words, structuring BERT this way allows us to perform sentence-level tasks and token-level tasks. If we use BERT and want to work with sentence-level information, we build on top of the $C$ token.
    - [Masked Language Modeling](Masked%20Language%20Modeling.md)

	- Next Sentence Prediction (NSP)
	    - This task ensures that the model learns sentence-level information. It is also really simple, and is the reason why the BERT inputs can sometimes be a pair of sentences. NSP involves textual entailment, or understanding the relationship between two sentences.
	    - Constructing a training dataset for this task is simple: given an unlabeled corpus, we take a phrase, and take the next one for the 50% of cases where BERT has a next sentence. We take another phase at random given A for the 50% where this is not the case (Devlin et al., 2018). This way, we can construct a dataset where there is a 50/50 split between 'is next' and 'is not next' sentences.
    - [BooksCorpus](BooksCorpus.md)
    - [English Wikipedia](English%20Wikipedia.md)
    - It thus does not matter whether your downstream task involves single text or text pairs: BERT can handle it.
        - Sentence pairs in paraphrasing tasks.
        - Hypothesis-premise pairs in textual entailment tasks.
        - Question-answer pairs in question answering.
        - Text-empty pair in text classification.
    - Yes, you read it right: sentence B is empty if your goal is to fine-tune for text classification. There simply is no sentence after the token.
    - Fine-tuning is also really inexpensive



