---
toc: true
title: DT Tutor

tags: ['usermodel']
date modified: Wednesday, October 12th 2022, 2:14:20 pm
date created: Wednesday, October 12th 2022, 2:14:02 pm
---

# DT Tutor


- DT Tutor (Murray, VanLehn, & Mostow, 2004) implements a version of this ideal tutoring policy.
- The tutor applies decision theory to make its choice about whether to give a hint.
- For each tutor action it can make (e.g., to give a hint, and which kind of hint), it uses a probabilistic model of the student to predict all possible student reactions to the tutor's action and their probability.
- The predicted student state includes the likelihood of learning, of becoming frustrated, of entering the next step correctly, etc.
- DT Tutor evaluates the utility of each of the predicted student states, multiplies the state's utility by the state's probability, and eventually produces the expected utility of each proposed tutor action.
- It then takes the tutor action with the highest expected utility. Although advances in probabilistic reasoning make it feasible for DT Tutor to perform this calculation in real time, considerable data from human students is needed in order to set the parameters in its model of student learning



