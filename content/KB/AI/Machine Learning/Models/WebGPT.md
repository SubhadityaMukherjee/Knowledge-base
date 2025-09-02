---
toc: true
title: WebGPT

tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:13 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# WebGPT
- [WebGPT: Browser-assisted Question-answering with Human Feedback](https://arxiv.org/abs/2112.09332)
- fine-tuned version of [GPT](GPT.md)-3 to more accurately answer open-ended questions using a text-based web browser.
- submits search queries, follows links, and scrolls up and down web pages
- trained to cite its sources
- By setting up the task so that it can be performed by humans, they are able to train models on the task using imitation learning
- models must collect references while browsing in support of their answers
- ELI5
- dataset of questions asked by Reddit users
- fine-tuning [GPT](GPT.md)-3 using behavior cloning, and then performing [Rejection Sampling](Rejection%20Sampling.md) against a reward model trained to predict human preferences



