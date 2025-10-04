---
toc: true
title: The Behavior of Tutoring Systems

tags: ['usermodel']
date modified: Wednesday, October 12th 2022, 2:23:48 pm
date created: Wednesday, October 12th 2022, 2:04:53 pm
---

# The Behavior of Tutoring Systems
- Kurt VanLehn


## Intro
- Tutoring systems are described as having two loops.
- The outer loop executes once for each task, where a task usually consists of solving a complex, multi-step problem
- The inner loop executes once for each step taken by the student in the solution of a task. The inner loop can give feedback and hints on each step. The inner loop can also assess the student's evolving competence and update a student model, which is used by the outer loop to select a next task that is appropriate for the student.
- A task usually takes several minutes to an hour or so. Most tutors assume that the student is working alone on a task, but some (e.g., Zachary et al., 1999) have the student work as one member of a multi-student team.
- The tasks and the tutor's user interface are usually designed so that completing a task requires multiple steps, where a step is a user interface action that the student takes in order to achieve a task.
- Let us use knowledge for the information possessed by students that determines their behavior on task. Let us also assume that knowledge can be decomposed, and let us use the term [Knowledge Component](Knowledge%20Component.md) for the units into which it is decomposed.
- [Knowledge Component](Knowledge%20Component.md)
- [Learning Event](Learning%20Event.md)
- [Modeling Transfer](Modeling%20Transfer.md)
- [Predicting Student learning Curve](Predicting%20Student%20learning%20Curve.md)
- [Tutor](Tutor.md)

## THE OUTER LOOP
- The main responsibility of the outer loop is to decide which task the student should do next. Its other responsibilities, such as presenting the task to the student, are more mundane and will not be mentioned again. The main design issues are (1) selecting a task intelligently and (2) obtaining a rich set of tasks to select from.

### Task Selection
- The outer loop displays a menu and lets the student select the next task.
- The outer loop assigns tasks in a fixed sequence
- [Mastery learning](Mastery%20learning.md)
- [Macroadaptation](Macroadaptation.md)
- In addition to selecting a task, some tutoring systems also select a mode for the task. For instance, [Steve](Steve.md) can either (1) demonstrate how to do the task by taking each step itself and explaining it, or (2) hint each step before the student attempts it, or (3) let the student try to solve the task without such unsolicited hints.
- In addition to providing some kind of mechanism for selecting tasks, the designer must provide a set of tasks for the outer loop to select from. It is often surprising how many problems are necessary in order to field a tutoring system. For a 13 week semester at 10 problems per week, the tutoring system needs 130 problems at minimum
- Ideally, the tutor can generate its own tasks when given a specification of the desired characteristics.
- For instance, given a specification of a [Knowledge Component](Knowledge%20Component.md) to be taught, the SQL- Tutor (Martin & Mitrovic, 2002) generates a database query, written in SQL, that involves the [Knowledge Component](Knowledge%20Component.md). A human author then writes text for a problem that has this database query as its solution. Using this technique, a human author was able to create 200 problems in about 3 hours— enough for a 6 week instructional module in an SQL course. Such programs are called problem generators.

## THE INNER LOOP
- Whereas the outer loop is about tasks, the inner loop is about steps within a task

### MINIMAL FEEDBACK
- Minimal feedback usually indicates whether a step is correct or incorrect, although other categories are sometimes used as well.

#### Categories of Minimal Feedback
- Although most tutoring systems use just two categories, correct and incorrect, it is possible to use others.
- Suppose a step is not part of an ideal solution to the problem, but it might be part of a non-ideal solution. The instructors might wish to consider this as a third category for minimal feedback—correct but non-optimal
- For instance, when students solve physics problems on [Andes](Andes.md), they can enter an equation that is true of the given physical situation but is not necessary for solving the problem.
- If instructors sometimes disagree on what makes for the best solution to the problem, it might be wise to subcategorize non-optimal. For instance, because some [Sherlock](Sherlock.md) instructors emphasize reducing time and others emphasize reducing costs, [Sherlock](Sherlock.md) could subcategorize non-optimal steps as wastes time or wastes parts. In short, the categories used for minimal feedback should reflect the pedagogical policies of the instructors.
- If a step cannot be classified as into one of the minimal feedback categories (correct, incorrect, non-optimal, etc.), then it lands in an unrecognizable classification.
- There are basically just three ways to treat such unrecognizable steps. (1) Some tutoring systems, such as the [Algebra Cognitive Tutor](Algebra%20Cognitive%20Tutor.md), assume that they can recognize all correct steps, so they treat unrecognizable steps as incorrect. (2) Other tutoring systems, such as the [SQL-Tutor](SQL-Tutor.md), assume that students will sometimes produce novel, correct solutions, so they treat unrecognized steps as correct. (3) Lastly, the tutoring system could simply tell the student that the step is unrecognizable. In this case, unrecognizable is yet another category for minimal feedback. When to give minimal feedback
- Immediate feedback: [Andes](Andes.md), [Algebra Cognitive Tutor](Algebra%20Cognitive%20Tutor.md), [Steve](Steve.md) and [AutoTutor](AutoTutor.md) give feedback immediately after each student step. They vary considerably in how the feedback is presented.
- Delayed feedback: Only if the step violates a safety regulation will [Sherlock](Sherlock.md) give immediate feedback as the student solves a problem. However, after the problem is solved, the student can request a reviewing mode where minimal feedback is given. In particular, as [Sherlock](Sherlock.md) replays the student's solution step-by-step, it indicates which steps did not contribute any diagnostic information.
- Demand feedback: The [SQL-Tutor](SQL-Tutor.md) gives feedback only when the student clicks on the Submit button. Because the student can continue working on their solution after receiving such feedback, this does not count as delayed feedback.
- The feedback policy can be a function of the student's competence. For instance, if the student is nearing mastery, then the feedback is delayed whereas a less competent student would be given the same task with immediate feedback
- This policy has been observed in human tutoring, and is one instance of fading the scaffolding, (Collins et al., 1989), because feedback is a kind of scaffolding (pedagogically useful help).

### NEXT-STEP HINTS
- 1. When should the tutor give a hint about the next step? Should it wait for the student to ask? Should it give unsolicited hints when it detects guessing or floundering? 2. What step should the tutor suggest? For instance, if there are multiple paths to a solution, and the student appears to be following a long complex one, should the tutor suggest starting over? 3. How can the tutor give hints that maximize learning, keep frustration under control, and allow the student to finish the problem?
- The common wisdom is that a tutor should give a hint on the next step only if the student really needs it. If the student can enter a correct step by thinking hard enough, then the system should refuse to give a hint even if the student asks for one
- On the other hand, if the student is likely to waste time and get frustrated by trying in vain to enter a correct step, or if the student is making repeated guesses instead of trying to figure out the next step, then the tutoring system should probably give a hint even if the student doesn't ask for one.
- [DT Tutor](DT%20Tutor.md)
- [Help Abuse](Help%20Abuse.md)
- [Help Refusal](Help%20Refusal.md)

#### Which Step to Hint
- The step must be correct.
- The hinted step should not have been done already by the student.
- Instructors' preferences should be honored.
- If the student has a plan for solving the problem or even for just the next step, then the tutor should hint the step that the student is trying to complete.
- A somewhat more complex case occurs when the student has just made an incorrect step and received minimal negative feedback.
- In AI, this is called the [plan recognition problem](plan%20recognition%20problem.md)

#### How to Hint the Next Step
- Perhaps the most common policy is to construct a short sequence of hints for the next step.
- The first hints are weak—they divulge little information so that students are encouraged to do most of the thinking themselves. Later hints are stronger.
- If the step requires only one [Knowledge Component](Knowledge%20Component.md), then a standard hint sequence is Point, Teach and Bottom-out (Hume, Michael, Rovick, & Evens, 1996)
- Pointing hints mention problem conditions that should remind the student of the [Knowledge Component](Knowledge%20Component.md)'s relevance.
- Teaching hints describe the [Knowledge Component](Knowledge%20Component.md) briefly and show how to apply it.
- Bottom-out hints tell the student the step

### ERROR-SPECIFIC FEEDBACK
- The service consists of analyzing an incorrect step in order to determine the incorrect [Learning Event](Learning%20Event.md)(s) that led to it, then giving instruction that is aimed at preventing that incorrect [Learning Event](Learning%20Event.md)(s) from occurring again
- There are many techniques for diagnosing errors. Most require that authors observe student errors, figure out what is causing a common error, write an appropriate error type for it, and implement some way to recognize such errors.
- FOIL: First, Outer, Inner and Last

#### How to Give Error-specific Feedback
- The main purpose of error-specific feedback is to get the student to change their knowledge so that they will not make this mistake again
- Correcting one's knowledge is sometimes compared to debugging a piece of software (Ohlsson, 1996). A programmer must first find evidence that the bug exists, then find out what the bug is, and then fix the bug. When tutees are not working with a tutor, they must do the whole self-debugging process themselves. They must first notice that a step is incorrect, then find the flaw in their reasoning and knowledge, then figure out what the correct learning events and knowledge components should be
- Many tutors present feedback as a sequence of hints that are loosely associated with the stages of self-debugging. When the student enters an incorrect step, the tutor begins the sequence by simply giving minimal feedback. This is like providing the student with evidence of a knowledge bug but giving no further help toward identifying the bug or correcting it.

#### When to Give Error-specific Feedback
- Students sometimes make careless errors, called slips in psychology (Norman, 1981), but fail to notice that they have made them, which can cause them to waste time looking for deep, potential misconceptions.
- To ameliorate into slips and potential this, [Andes](Andes.md) divides error misunderstandings. types
- Slips are often made by the experts, including the instructors.
- A potential misunderstanding is an error type that could be due to many factors, including incorrect beliefs, but it is almost never seen in expert's work
- When a student enters an incorrect step that is classified as a slip, then [Andes](Andes.md) gives the error specific remediation immediately, e.g., You forgot to include a unit on a number. If the error is classified as a potential misunderstanding, then [Andes](Andes.md) merely turns the incorrect step red, and lets the student ask for an error-specific hint if they want one.
- Some student steps contain two or more errors. In order to keep the communication simple, the tutoring system should probably respond to only one of them. Students typically fix that error only, so the tutoring system can then mention the second error

## What Kind of Assessment is Required?
- A fundamental issue is the grain-size or granularity of the assessment.
- The granularity of an assessment refers to the degree of aggregation over the task domain's knowledge. An assessment is fine-grained if it provides, for instance, a probability of mastery for each [Knowledge Component](Knowledge%20Component.md) in the task domain. An assessment is coarse-grained if it provides a single number that indicates the student's overall competence.
- Assessments are decision aids, and as a general heuristic, the bigger the decision, the coarser the required assessment. If a decision affects a whole semester, e.g., whether the student needs to retake a
- required course, then the assessment should cover the whole semester and lead ultimately to a yes-no decision, so a single number per student is appropriate.
- If a decision affects only, say, whether the tutor starts at the beginning of a hint sequence or in the middle, then only a small part of a fine-grained assessment is relevant
- The general idea is that if the decision is small, in that it affects only a small amount of instructional time, then only a small amount of the domain's knowledge can be accessed during that time and thus the relevant decision aid is the student's competence on just that knowledge.
- Tutors make many small decisions, so they are the main customers for fine-grained assessments.
- [Coarse-grained assessment](Coarse-grained%20assessment.md)
- [Fine Grained assesment](Fine%20Grained%20assesment.md)

### Issues with Assesment
- There are many other issues involved with assessment. Here are a few:
- There is a big difference between little evidence and mixed evidence. If one merely takes the frequency of success relative to opportunities, then 0.5 can mean both 1 success and 1 failure (little evidence) or 20 successes and 20 failures (mixed evidence).
- Students should be learning, so their knowledge should be changing. When should old evidence be ignored?
- Should help given by the tutoring system be counted as evidence of learning or of lack of knowledge?
- Are all learning events equally difficult? If not, then item response theory ([IRT](IRT.md)) can be used so that success on easy learning events provides less evidence of competence than success on difficult learning events.
- If the tutoring system includes error-specific feedback based on error types, should it somehow include the frequency of occurrence of the error types in its assessments?
- Prior probabilities of mastery are not independent. If a student has not mastered a [Knowledge Component](Knowledge%20Component.md) that is taught early in the course, then it is less likely that the student has mastered.
- Knowledge components that appear later.

## Examples of Tutoring Systems
- [Steve](Steve.md)
- [Algebra Cognitive Tutor](Algebra%20Cognitive%20Tutor.md)
- [Andes](Andes.md)
- [Sherlock](Sherlock.md)
- [AutoTutor](AutoTutor.md)
- [SQL-Tutor](SQL-Tutor.md)



