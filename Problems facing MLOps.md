---
toc: true
title: Problems facing MLOps
tags:
  - architecture
date modified: Friday 20th October 2023, Fri
date created: Friday 20th October 2023, Fri
---

# Problems Facing MLOps


## General
- Coding is not the whole story
- It’s easier for great engineers to pick up ML knowledge, but it’s a lot harder for ML experts to become great engineers.
- Use "off the shelf models"
- Companies focus on improving data, but not model
- Model sizes are hard
- Dataset/model versioning is hard
- Experiment Tracking
	- Hyperparameter tuning is important and it’s not surprising to find several that focus on it, 
	- none seems to catch on because the bottleneck for hyperparameter tuning is not the setup, but the computing power needed to run it.
- Data monitoring
	- Distribution shift
- Labelling
	- How often do we need to re-label
- CI/CD
	- Testing
	- Re-train model
- Deployment
	- How often to package and deploy
	- One reason for the lack of serving solutions is the lack of communication between researchers and production engineers.
	- Small companies, whose employees can see the entire stack, are constrained by their immediate product needs
- Model Compression
	- Compress ML Models
- Optimizing Inference
- Edge devices
- Privacy
	- GDPR
- OSS vs Open Core
	- Since OSS has become a standard, it’s challenging for startups to figure out a business model that works.
	- Any tooling company started has to compete with existing open-source tools.
