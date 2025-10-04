---
toc: true
title: Beware of Inmates Running the Asylum

tags: ['explainability']
date modified: Saturday, December 3rd 2022, 5:19:07 pm
date created: Saturday, December 3rd 2022, 5:10:11 pm
---

- # Beware of Inmates Running the Asylum
  ```toc
  ```
  
  * Tim Miller∗ and Piers Howe† and Liz Sonenberg
- [[@Explainable AI: Beware of Inmates Running the Asylum Or: How I Learnt to Stop Worrying and Love the Social and Behavioural Sciences.md|@Explainable AI: Beware of Inmates Running the Asylum Or: How I Learnt to Stop Worrying and Love the Social and Behavioural Sciences]]

## TL;DR
- Essentially proposes to look at behavioral science research as well. Not particularly useful but is a good reminder to look at other research because [XAI](XAI.md) is meant for people and not programmers.

## Abstract

* programmers design software for themselves, rather than for their target audience; a phenomenon he refers to as the ‘inmates running the asylum’.
* This paper argues that explainable AI risks a similar fate.
* evaluation of these models is focused more on people than on technology
* considerable scope to infuse more results from the social and behavioural sciences into explainable AI, and present some key results from these fields that are relevant to explainable AI.

## Explainable AI Survey

## Survey Method
- On topic
  
  	* Each paper was categorised as either being about explainable AI or not, based on our understanding of the topic
  * Data Driven
  	* Each paper was given a score from 0–2 inclusive.
  	* A score of 1 was given if and only if one or more of the references of the paper was an article on explanation in social science
  * Validation
  	* Each paper was given a binary 0/1. A score of 1 was given if and only if the evaluation in the survey article (note, not the referenced article) was based on data from human behavioural studies.

## Results

* These results show that for the on-topic papers, only four articles referenced relevant social science research, and only one of them truly built a model on this
* Further, serious human behavioural experiments are not currently being undertaken.
* For off topic papers, the results are similar: limited input from social sciences and limited human behavioural experiments.
* Where to? A Brief Pointer to Relevant Work Contrastive Explanation
* explanations are contrastive why–questions are contrastive
* That is, why–questions are of the form “Why P rather than Q?”, where P is the fact that requires explanation, and Q is some foil case that was expected
* Importantly, the contrast case helps to frame the possible answers and make them relevant
* This is a challenge for explainable AI, because it may not be easy to elicit a contrast case from an observer.
* However, it is also an opportunity: as Lipton [1990] argues, answering a contrastive question is often easier than giving a full cause attribution because one only needs to understand the difference between the two cases, so one can provide a complete explanation without determining or even knowing all causes of the event.

## Attribution Theory

* study of how people attribute causes to events Social Attribution
* The book from Malle [2004], based on a large body of work from himself and other researchers in the field, describes a mature model of how people explain behaviour of others using folk psychology
* people attribute behaviour based on the beliefs, desires, intentions, and traits of people
* important for systems in which intentional action will be cited as a cause important for systems doing deliberative reasoning

## Causal Connection

* Research on how people connect causes shows that they do so by undertaking a mental simulation of what would have happened had some other event turned out differently


