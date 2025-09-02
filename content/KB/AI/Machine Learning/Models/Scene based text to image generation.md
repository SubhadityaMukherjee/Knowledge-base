---
toc: true
title: Scene based text to image generation

tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:17 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Scene Based Text to Image Generation
- [Make-A-Scene: Scene-Based Text-to-Image Generation with Human Priors](https://arxiv.org/abs/2203.13131)
- text-to-image generation
- enabling a simple control mechanism complementary to text in the form of a scene
- introducing elements that substantially improve the tokenization process by employing domain-specific knowledge over key image regions
- adapting classifier-free guidance for the transformer use case
- They attempt to progress text-to-image generation towards a more interactive experience, where people can perceive more control over the generated outputs, thus enabling real-world applications such as storytelling
- focus on improving key image aspects that are significant in human [Perception](Perception.md), such as faces and salient objects, resulting in higher favorability of their method in human evaluations and objective metrics
- Through scene controllability, they introduce several new capabilities: (i) scene editing, (ii) text editing with anchor scenes, (iii) overcoming out-of-distribution text prompts, and (iv) story illustration generation



