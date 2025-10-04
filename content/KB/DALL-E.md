---
toc: true
title: DALL-E

tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:30 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# DALL-E
- [AdaIn](AdaIn.md)
- it was capable of generating text that could not be distinguished from human-written text
- named after Salvador Dalí and Pixar's WALL·E
- based on the [GPT3](GPT3.md)
- Previous approaches like [BERT](BERT.md) and the original [GPT](GPT.md) model followed the fine-tuning approach.
- [GPT](GPT.md)-2 and [GPT](GPT.md)-3 recognized that even while pretraining already provided lots of benefits compared to training from scratch, so-called zero-shot learning - where the model is finetuned and then applied to language tasks, without pretraining - could be the way forward.
- DALL·E is capable of performing a variety of tasks:
	- Controlling attributes, instructing the model what particular attributes of an object should look like. For example: "a collection of glasses is sitting on a table" (OpenAI, 2021). Here, we instruct the model about the glasses, and more precisely, their location.
	- Drawing multiple objects is also possible, but is more challenging, because it can be unknown whether certain characteristics belong to one object or another (OpenAI, 2021). DALL·E is however also capable of performing that task, but at the risk of making mistakes - once again due to the issue mentioned previously. The success rate decreases rapidly when the number of objects increases.
	- Visualizing perspective and three-dimensionality, meaning that DALL·E can be instructed to take a particular "perspective" when generating the image (OpenAI, 2021).
	- Visualizing across many levels, from "extreme close-up" to "higher-level concepts" (OpenAI, 2021).
	- Inferring context, meaning that particular elements can be added to an image that normally do not belong to a particular context (e.g. the OpenAI logo in the image above; this is normally not displayed on a store front).
- Uses
	- Industrial and interior design, to aid designers when creating a variety of household and other objects.
	- Architecture, to guide the creation of buildings and other forms of constructions.
	- Photography, to create an image specifically tailored to one's requirements.
	- Graphic design, with e.g. the creation of a variety of icons.
- [Zero-Shot Text-to-Image Generation](https://arxiv.org/abs/2102.12092)
- DALL-E which offers a simple approach for text-to-image generation based on an [Autoregressive](Autoregressive.md) transformer which models the text and image tokens as a single stream of data
- simple decoder-only transformer that receives both the text and the image as a single stream of 1280 tokens—256 for the text and 1024 for the image—and models all of them autoregressively
- They find that sufficient data and scale can lead to improved generalization, both in terms of zero-shot performance relative to previous domain-specific approaches
- and in terms of the range of capabilities that emerge from a single generative model.



