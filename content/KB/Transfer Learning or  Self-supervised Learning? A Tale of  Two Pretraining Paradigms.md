---
toc: true
title: Transfer Learning or  Self-supervised Learning? A Tale of  Two Pretraining Paradigms

tags: ['deeplearning']
date modified: Monday 27th March 2023, Mon
date created: Monday 27th March 2023, Mon
---

# Transfer Learning or Self-supervised Learning? A Tale of Two Pretraining Paradigms


- @yangTransferLearningSelfsupervised2020
- [Transfer Learning]  vs [Self Supervised](Transfer Learning]  vs [Self Supervised.md) 

## Comparison Using
- 5 different image-based source domains
- 4 target tasks
	1. from daily-life objects
	2. general scenes
	3. nature
	4. medical pictures areas.
- Four different experimental setups 

1. Effect of domain difference between source and target task
2. Effect of amount of pretraining data
3. Effect of class imbalance in source data
4. Effect of using target data for additional pretraining
- ResNet-50

## Results

### Domain Difference
- Large
	- SSL outperforms TL
- Small
	- TL outperforms SSL
	- SSL is less sensitive to domain difference than TL.

### Amount of Pretraining Data
- Small(for same source task)
	- SSL outperforms TL
- Large(for same source task)
	- TL outperforms SSL
	- SSL is less sensitive to amount of pretraining data than TL, when domain difference is small

### Class Imbalance (Source Data)
- SSL is more robust to class imbalance than TL

### Additional Pretraining
- For SSL, using target task for additional pretraining works better vs using only source data, but not for TL.

## What is Left
- can be extended to other forms of data including speech, signals and text
- Only used ResNet architecture, need to investigate other architectures
- Image Transformers etc. are not considered
- Correlation between performance and factors is studied and potential reasons behind it are discussed, a deeper investigation of these potential reasons might be beneficial



