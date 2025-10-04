---
toc: true
title: Masked Language Modeling

tags: ['nlp']
date modified: Friday, December 9th 2022, 11:38:02 am
date created: Thursday, December 8th 2022, 11:40:39 pm
---

# Masked Language Modeling

- In Masked Language Modeling, an input sequence of tokens is provided, but with some of these tokens masked. The goal of the model is then to learn to predict the correct tokens that are hidden by the mask. If it can do so, it can learn token-level information given the context of the token.
- In BERT, this is done as follows. 15% of all word embedded tokens is masked at random. From this 15%, 80% of the tokens is represented with a token called , 10% is replaced with a random token and 10% is left alone. This ensures that masking is both relatively random and that the model does not zoom in to the token, which is available during pretraining but not during fine-tuning.
- This model is also capable of predicting words using the two masked sentences. It concatenates two masked words and tries to predict.
- these models where we are required to predict the context of words. Since the words can have different meanings in different places the model needs to learn deep and multiple representations of words.
- These models have shown improved performance levels in the downstream tasks such as syntactic tasks that require lower layer representation of certain models in place of a higher layer representation.
- We may also find their use in learning the deep bidirectional representations of words. The model should be able to learn the context of words from the start of the sentence as well as from the behind.

## Tokenizing Data BERT
- In the tokenizer method, **text_lst** is the text corpus, **max_length** suggests the maximum number of allowable input tokens (the maximum is 512 for BERT base), and **truncation** set to True indicates that if the input size is more than the max_length, then the token from index number equal to max_length would be truncated i.e., for our example input tokens from index 100 would be dropped, **padding** set to True indicates the input length shorter than the max_length are padded, with padding token 0 and lastly, **return_tensors** indicates in what format do we want the output tensor and **tf** suggests that we expect **tensorflow** tensor. The tokenizer here returns three fields, as we have mentioned earlier.
- Now if we look at the “**inputs”** with the code print(inputs), we can see that the **input_ids** tensor is of shape 1567×100, and each row starts with the token 101, which is the id for the Special token [CLS] and ends with 0 which is the padding token indicating that the sentence length is less than 100. Also, there is a Special token 102, the [SEP] token, which is not visible, indicating the end of a sentence. Secondly, the **token_type_ids** are all 0 as there is only a single sentence as input. Finally, the **attention_mask** has ones at locations for the actual input tokens and zeros for the padding tokens.

## Masking Input Tokens BERT
- In the original research paper, 15% of the input tokens were masked, of which 80% were replaced with [MASK] tokens, 10% were replaced with random tokens, and another 10% were left as is. However, in our fine-tuning task, we are replacing 15% of the input tokens except for the special ones with only [MASK] i.e., we will not replace token numbers 101,102, and 0 with mask token 103. In the following lines of codes, the same logic is implemented



