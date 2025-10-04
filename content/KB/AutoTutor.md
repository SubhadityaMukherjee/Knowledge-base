---
toc: true
title: AutoTutor

tags: ['usermodel']
date modified: Wednesday, October 12th 2022, 2:22:47 pm
date created: Wednesday, October 12th 2022, 2:22:19 pm
---

# AutoTutor


- Outer loop: AutoTutor (<http://demo.autotutor.org/)> teaches by engaging students in a natural language (English) dialogue
- For AutoTutor, a task corresponds to a single question, such as the one shown in the upper right of Figure 4, that has a complex answer. Its outer loop consists of selecting such a question and working with the student to get it completely answered.
- Inner loop: The inner loop starts with the student typing in an initial answer to the top level question (see Figure 4; the student types into the lower right window; the whole dialogue is displayed in the lower left window).
- AutoTutor has been used to compare output modalities.
- An AutoTutor dialogue is composed of tutor turns alternating with student turns. On most of the student turns, the student makes a small contribution toward completing the whole task. Those student turns count as steps, because they are a user interface event that contributes to a solution of the whole task
- Step analysis:
- These are conclusions that are produced by applying knowledge components. For instance, the first two items above correspond to distinct learning events, wherein the student has applied the same [Knowledge Component](Knowledge%20Component.md),
- In addition to having a list of all anticipated correct learning events, such as the ones mentioned above, AutoTutor has a list of several of the most important incorrect learning events
- To find out which learning events underlie the student's step, AutoTutor measures the semantic similarity between the text of the [Learning Event](Learning%20Event.md) and the text of the step. It uses a measure called [Latent Semantic Analysis](Latent%20Semantic%20Analysis.md)



