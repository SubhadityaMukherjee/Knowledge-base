---
toc: true
title: CheckList

tags: ['benchmark']
date modified: Monday, October 10th 2022, 2:02:31 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# CheckList
- [Beyond Accuracy: Behavioral Testing of NLP Models with CheckList](https://arxiv.org/abs/2005.04118)
- ML systems can run to completion without throwing any errors (indicating functional correctness) but can still produce incorrect outputs (indicating behavioral [Issues](Issues.md))
- CheckList
- model-agnostic and task-agnostic methodology for testing NLP models inspired by principles of behavioral testing
- matrix of general linguistic capabilities and test types that facilitate comprehensive test ideation
- Minimum Functionality Test (MFT): A Minimum Functionality Test (MFT) uses simple examples to make sure the model can perform a specific task well. For example, they might want to test the performance of a sentiment model when dealing with negations
- Invariance Test: Besides testing the functionality of a model, they might also want to test if the model prediction stays the same when trivial parts of inputs are slightly perturbed. These tests are called Invariance Tests (IV)
- Directional Expectation Test: In the Invariance Test, they expect the outputs after the perturbation to be the same. However, sometimes they might expect the output after perturbation to change. That is when Directional Expectation Tests comes in handy



