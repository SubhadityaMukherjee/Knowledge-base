---
toc: true
title: RAGAS - automated evaluation of RAG
tags:
  - architecture
date modified: Wednesday 29th May 2024, Wed
date created: Wednesday 29th May 2024, Wed
---

# RAGAS - Automated Evaluation of RAG


# RAGAS: Automated Evaluation of Retrieval Augmented Generation

- (Note : Well. I am not convinced. They did come up with some ways of testing it. But all of those ways used the LLM to test itself, which is uh. Not very nice or representative. I am unsure of how accurate any of these are.
- Logically it seems slightly flawed, but I respect the hustle)

## RAGAS (Retrieval Augmented Generation Assessment)
- framework for reference-free evaluation of Retrieval Augmented Generation (RAG) pipelines
- evaluate these different dimensions without having to rely on ground truth human annotations
- While the usefulness of retrieval-augmented strategies is clear, their implementation requires a significant amount of tuning, as the overall performance will be affected by the retrieval model, the considered corpus, the LM, or the prompt formulation, among others

## **Evaluation Strategies**
- standard RAG setting
- given a question q, the system first retrieves some context c(q) and then uses the retrieved context to generate an answer as(q)
- (Note : This seems like an interesting start so far)
- we usually do not have access to human-annotated datasets or reference answers

## Faithfulness
- answer should be grounded in the given context
- important to avoid hallucinations, and to ensure that the retrieved context can act as a justification for the generated answer
- RAG systems are often used in applications where the factual consistency of the generated text w.r.t. the grounded sources is highly important
- ![](../images/3762eb5a12b51651a8e1b7eb38b484f43a391fd7.png)
- (Note : Basically they use an LLM to generate an answer and then check with the ground truth to see how closely it matched by comparing the number of matches/total number of statements)

## Answer Relevance
- generated answer should address the actual question that was provided
-  (Note : Basically uses cosine similarity. I am unsure of how different it is to that usual llm but oh well)
![](../images/07bae6cf89f17bb75cb21014472299549d62e2e4.png)

## Context Relevance
- retrieved context should be focused, containing as little irrelevant information as possible
- gpt-3.5-turbo-16k model
- penalise the inclusion of redundant information.
- (Note : -.-, they just asked the LLM to find the most important sentences and then divided it by the total number of sentences. I am now progressively getting more and more annoyed with this paper)
