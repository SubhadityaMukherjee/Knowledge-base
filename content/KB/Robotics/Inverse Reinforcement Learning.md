---
toc: true
title: Inverse Reinforcement Learning

tags: ['robotics']
date modified: Wednesday, October 26th 2022, 9:16:22 am
date created: Wednesday, October 26th 2022, 9:16:13 am
---

# Inverse Reinforcement Learning


- Basically, IRL is about studying from humans.
- Inverse reinforcement learning is the sphere of studying an agent’s objectives, values, or rewards with the aid of using insights of its behavior.
- We can fit a reward function with the use of professional demonstrations. Once a reward feature is fitted, we are able to use Policy Gradient, Model-based RL or different RL to locate the ideal policy.
- For example, we are able to compute the policy gradient with the use of the reward feature as opposed to sampled rewards. With the policy gradient calculated, we optimize the policy closer to the finest rewards gain.
- As part of the IRL, the task is to collect a set of human-generated driving data and extract an approximation of that human's reward function for the task. Of course, this approximation necessarily relates to a simplified driving model.
- As Ng and Russell put it, "the reward function, rather than the guideline, is the most concise, robust, and transferable definition of the task" because it quantifies how good or bad certain actions are. Once we have the right reward function, the problem is finding the right guideline and can be solved using standard reinforcement learning methods.
- For our autonomous car example, we would use human driving data to automatically learn the correct functional weights for the reward. Since the task is fully described by the reward function, we don't even need to know the details of human politics as long as we have the right reward function to optimize.



