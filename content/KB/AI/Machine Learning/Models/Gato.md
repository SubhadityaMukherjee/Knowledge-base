---
toc: true
title: Gato

tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:27 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Gato
- [A Generalist Agent](https://storage.googleapis.com/deepmind-media/A%20Generalist%20Agent/Generalist%20Agent.pdf)
- Gato
- single generalist agent beyond the realm of text outputs, inspired by progress in large-scale language modeling
- multi-modal, multi-task, multi-embodiment generalist policy
- same network with the same weights can play Atari, caption images, chat, stack blocks with a real robot arm and much more, deciding based on its context whether to output text, joint torques, button presses, or other tokens
- To enable processing this multi-modal data from different tasks and modalities, it is serialized into a flat sequence of tokens
- In this representation, Gato can be trained and sampled from akin to a standard large-scale language model
- Masking is used such that the loss function is applied only to target outputs, i.e text and various actions
- During deployment, sampled tokens are assembled into dialogue responses, captions, button presses, or other actions based on the context
- Transformer sequence models are effective as multi-task multi-embodiment policies, including for real-world text, vision and [robotics](robotics.md) tasks



