---
title: Hosting on prem LLM (SSC)
toc: true
tags:
date modified: Thursday 18th September 2025, Thu
date created: Thursday 18th September 2025, Thu
---

# Hosting on prem LLM (SSC)
```toc
```

- Hengjian Zhang - AI application support engineer
- Nvidia ai blueprint
- monitoring
	- zipkin, grafana
	- prometheus
- RAG : NeMO retriever + paddle ocr
- Milvus vector DB
- Why
	- uva has a chatbot already (so we should as well ;p)
- Advantages
	- monitoring and safety control
	- NVIDIA inference microservice (higher throughput)
	- "dont need to maintain software" (aka someone else does it for you)
- spike - license obtained by tue
	- its an AI supercomputer (DGX B200) 
- nvidia/llama-3.3-nemotron-super-49b-v1
	- send data to tue server instead of openai being the only selling point
- at the moment
	- deployed on a vm
	- no dynamic scaling yet
	- no money to do this atm so doesnt "really" exist
		- if demand, then the tue will spend money on it
	- has guardrails but that requires even more GPU resources
- SURF 
	- self hosted GPUs are not okay
		- so azure is to be used
	- 4xA100 but not enough
	- edu genai is a service by them
	- spike-1 is not too stable rn
- supercomputing@tue.nl
- IMO : kinda sucks right now (I guess) (or not????)