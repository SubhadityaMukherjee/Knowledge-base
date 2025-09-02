---
toc: true
title: PEER
tags: ['architecture']
---

## PEER
- trained on edit histories to cover the entire writing process
- Plan, Edit, Explain and Repeat
- These steps are repeated until the text is in a satisfactory state that requires no further updates
- The model allow to decompose the task of writing a paper into multiple easier subtasks
- the model allows humans to intervene at any time and steer the model in any direction
- Wikipedia edit histories
- The approach is a selftraining, using models to infill missing data and then train
other models on this synthetic data
- The downside of this comes from comments being very noisy and a lack of citations, which tries to be compensated by a retrieval system which does not always work
- The entire process of formulating a plan, collecting documents, performing an edit and explaining it can be repeated multiple times until arriving at a sequence of text
- a DeepSpeed transformer is used



