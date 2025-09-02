---
toc: true
title: Modeling motivation using goal competition in mental fatigue studies

tags: ['cognitivemodel']
date modified: Wednesday 1st February 2023, Wed
date created: Wednesday 1st February 2023, Wed
---

# Modeling motivation using goal competition in mental fatigue studies
- Mega B. Herlambang a,b,∗, Niels A. Taatgen a, Fokie Cnossen


- Motivation can counteract the effects of mental fatigue
- goal competition as a paradigm to understand the role of motivation and built three models of mental fatigue studies to demonstrate the mechanism in a cognitive architecture named PRIM
- model changes in performance levels by adjusting the value of the main task goals
- which controls the competition with distractions
- best model fits were obtained by a linear decrease in goal activation
- Modeling fatigue and motivation decline in PRIMs
- The assumption in this paper is that the decrease in task performance in mental fatigue is the result of a reduction in task motivation.
- reflected in a reduction in activation of the task goal over time
- As time progresses, individuals may experience an increase in the feeling of fatigue that reduces the subjective value of the main task, i.e., task motivation (Müller & Apps, 2019) or goal activation (Agoal) in our models
- Consequently, goal activation is discounted by the feeling of fatigue
- perceived reward from doing the task (extrinsically or intrinsically) maintains the goal activation from declining.
- $$A_{goal(t)} = min(1 \vee (P(t) - F(t)))$$,
- Therefore, the relationship between the perceived reward (P), the feeling of fatigue (F), and goal activation (Agoal) at any given time (t) is
- goal activation value of one means that the model mainly focuses its attention on the main goal.
- The value P is influenced by previous perceived rewards. For example, when the previous incentive at t − 1 is perceived as more valuable than the recent one at t, then the value Pt is smaller than Pt−1
- In contrast, the value of Pt is higher if the reward at t is perceived as more valuable than the previous one at t−1
- It is evident that motivation affects the ability to stay focused on a task and not be distracted by internal or external distractions (Herlambang et al., 2019)
- In the case of external distractions, task-unrelated stimuli may shift attention away from the main task, while internal distractions may manifest itself in the form of mind-wandering

## Discussion
- that goal competition is one of the key factors to understand the underlying mechanism of motivation in mental fatigue.
- decrease in performance is not due to a decrease in the capacity of the cognitive system (e.g., lower working memory capacity, slower motor system, less reliable long-term memory) but by a decrease in the ratio of cognitive ''cycles'' spent on the task as opposed to distractions.
- have modeled this by a decrease in the activation of the goal, which represents the level of motivation, which indirectly affects performance
- modeler can tune some parameters to obtain a good fit
- However, overdoing such parameter tuning may lead to overfitting, which makes the models difficult to generalize and does not represent the empirical data

## Goal activation and performance
- To lower performance in the nonreward conditions in all tasks, we decreased task goal activation values over time
- The goal activation values in our models represent the subjective value of performing the tasks, with a high subjective value corresponds to a high level of motivation
- The reduction of goal activation was due to an increase in the feeling of fatigue (see Müller & Apps, 2019) and a continuous decrease in the perceived reward from doing the tasks
- What our modeling efforts suggest is that over time, while the activation value of the main active goal is decreasing, which is due to an increase in the feeling of fatigue and a decrease in the perceived reward (see Eq. (3)), another future goal of an activity/stimulus, for example, a distraction, may start winning the competition with the main task, when the activation value of the distraction exceeds that of the main goal (i.e., it strongly attracts the individual), in which case the individual may start paying attention to the distraction. The distraction can become the new active goal, and the individual may forget the main goal, or choose to pay attention to both, but this will sacrifice performance.
- Goal competition is a continuous process that compares several future goals, and when the main task goal is perceived to be less valuable, another competing goal may start winning the competition, causing the individual to invest less mental effort in the main task and start investing in the competing goal

## Limitation, challenge, and future research
- solely adjusting goal activation levels may not be enough to model changes in performance.
- There are many parameters in PRIMs that can affect performance
- Although adjusting goal activation values as a way to model mental fatigue showed good results for the experiments we modeled, it is possible that this does not directly generalize to other studies

## Images
- ![](../images/Pasted%20image%2020230201115702.png)
- ![](../images/Pasted%20image%2020230201115832.png)
- ![](../images/Pasted%20image%2020230201115840.png)
- ![](../images/Pasted%20image%2020230201115851.png)
- ![](../images/Pasted%20image%2020230201115902.png)
- ![](../images/Pasted%20image%2020230201115918.png)
- 



