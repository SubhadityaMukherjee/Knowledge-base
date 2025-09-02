---
toc: true
title: Steve

tags: ['usermodel']
date modified: Wednesday, October 12th 2022, 2:21:04 pm
date created: Wednesday, October 12th 2022, 2:21:03 pm
---

# Steve


- Outer loop: Steve is a tutoring system that teaches hierarchical, multi-step procedures, such as how to start a large air compressor
- take Inner loop: Students steps by manipulating graphical widgets, such as clicking on a valve icon to open it or on a dipstick to check the oil level
- Steve can give immediate feedback
- Steve can also execute a step for the student. In fact, it can demonstrate the whole procedure for a student, explaining each step as it goes.
- Step analysis: Steve interprets the student's step by matching it to a set of anticipated steps. In particular, after each student step, Steve computes all possible correct next steps (usually there is just one).
- Notice that there is a one-to-one relationship between the step, the [Learning Event](Learning%20Event.md) and the [Knowledge Component](Knowledge%20Component.md). This is a major contributor to the simplicity of Steve's analysis.
- Step generation: The student's most recent correct step is, by definition, part of the procedure being taught
- Steve uses immediate feedback to block incorrect steps, so Steve always knows where in the procedure the student is.
- When it needs to give hints on what to do next, it merely picks the next step. If there are multiple steps that could follow the student's most recent correct step, then Steve lists them and lets the student choose.



