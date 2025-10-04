---
toc: true
title: SQL-Tutor

tags: ['usermodel']
date modified: Wednesday, October 12th 2022, 2:23:16 pm
date created: Wednesday, October 12th 2022, 2:23:15 pm
---

# SQL-Tutor


- Outer loop: SQL-Tutor (<http://www.aw-bc.com/databaseplacedemo/sqltutor.html)> teaches students how to write a query to a relational database (B. Martin & Mitrovic, 2002; Mitrovic, 2003; Mitrovic & Ohlsson, 1999). Each task consists of a database and information to be retrieved from it. In Figure 5, for instance, the student has been given a database of movie information and has been asked to write a query that will List the toc: true
titles and numbers of all movies that have won at least one Academy Award and have been made in or after 1988.
- Inner loop: Students write a query in the SQL language by clicking on buttons and filling in blanks. This may take several minutes. At any point, they can press the Submit Answer button. The tutor, which has been completely silent up until now, analyzes the student's query to find its flaws. It gives a variety of levels of feedback and hints.
- One way to think of SQL-Tutor's inner loop is that the student takes multiple steps, each comprised of filling in a blank in the query
- Unlike tutors that give feedback as soon as a student had taken a step, SQL-Tutor delays its feedback until the student requests it.
- Step analysis: In order to analyze steps, SQL-Tutor has a set of constraints, where a constraint consists of a relevance condition and a satisfaction condition. If the relevance condition is false of the students' step, then the constraint is irrelevant, so the tutor says nothing about it. If the constraint has a true relevance condition and a true satisfaction condition, then the constraint is satisfied and the tutor says nothing about it.
- If the relevance condition is true, and the satisfaction condition is false, then the student's step violates the constraint and the tutor has identified a topic worth talking about. In particular, every constraint has two messages.
- Depending on the feedback level selected by the tutor or the student, one of them may be presented to the student when the constraint is violated. One message describes the constraint and its violation briefly. The other presents more details.
- Although the constraints are task independent, many of them refer to a correct solution of the problem, which is stored in the tutoring system.
- The relationship between steps, learning events and constraints is quite simple in the SQL-Tutor. Each constraint corresponds to a [Knowledge Component](Knowledge%20Component.md).



