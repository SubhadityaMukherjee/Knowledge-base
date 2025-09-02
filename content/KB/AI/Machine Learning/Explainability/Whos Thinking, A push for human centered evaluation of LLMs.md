---
toc: true
title: Whos Thinking, A push for human centered evaluation of LLMs

tags: ['explainability']
date modified: Wednesday 24th May 2023, Wed
date created: Wednesday 24th May 2023, Wed
---

# Whos Thinking, A Push for Human Centered Evaluation of LLMs


- @dattaWhoThinkingPush2023

## ABSTRACT
- In this paper, we draw parallels between the relatively mature field of XAI and the rapidly evolving research boom around large language models (LLMs)
- Specifically, we argue that humans' tendencies— again, complete with their cognitive biases and quirks—should rest front and center when evaluating deployed LLMs

## Large Language Models
- Current LLM evaluation mechanisms include quantitative metrics measuring notions of accuracy (how similar are the generated outputs to the expected outputs), robustness (how resilient is the model to transformations of the input), calibration (how meaningful are the generated probabilities in respect to uncertainty), efficiency (what are the energy, carbon, and time costs for training and inference) and more [35].
- There are substantial environmental costs associated with the volume of computational power required for training and inference [6, 49]
- Counterfactual fairness [24] examines how perturbing the demographic signals of existing test examples can change the performance of the model (e.g. "He worked at the local hospital" versus "She worked at the local hospital")
- other concerning forms of biases such as stereotypical associations, erasure, and over-representation in the semantics of its output [35, 38]
- LLMs have been shown to produce toxic outputs.
- LLMs often suffer from factual errors—they can "hallucinate" information [50] by providing very confident-sounding but entirely false responses
- Chatbot LLMs have also been found to engage in disturbingly emotional personal conversations when session lengths are not limited [47].
- There are also privacy concernswork has shown that LLMs are susceptible to training data leakage under adversarial attack [11].

## PARALLELS BETWEEN XAI AND LLMS
- LLM outputs are often meant for some downstream decision or task—what email to send to your client, what quick summary of an important document you will read, what answer is provided for a pertinent question
- Advocates push for first identifying a specific use case, then understanding the types of transparency useful and relevant for each stakeholder in that context, then designing the explanation method with these learnings held front and center, and finally evaluating how helpful the explanation was for specific tasks through practitioner user studies
- A system is valid if it does what it purports to do. If it doesn't, it is likely because there are issues of alignment between the intent of the system builder and the property the algorithm optimizes [40].

- [Cognitive Engagement](Cognitive Engagement.md)

- [Mental Model Matching](Mental Model Matching.md)

- [Use Case Utility](Use Case Utility.md)

## WHY IS THIS IMPORTANT
- the potential scale of LLM usage is massive as a fundamentally lower-level ML-
based building block than XAI
- ChatGPT [43] set historic records for its customer growth, with over 100 million users in its first 2 months [2].
- Unlike XAI, whose users are largely technical practitioners [7] focusing on one pipeline, LLMs are often designed for public use and are meant to help with a wide variety of tasks.
- The ability to influence or make decisions is a form of inherent power, and offloading cognition onto AI agents must first be met with caution.
- The consequences of not having a qualitative understanding of how humans interact with LLM outputs is grave



