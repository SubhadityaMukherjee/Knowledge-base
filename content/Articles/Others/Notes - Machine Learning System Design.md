
---
toc: true
title: Notes - Machine Learning System Design

tags: ["article"]
date modified: 
date created: 
---
# Notes on “Machine Learning System Design” (for Interviews) by Chip Huyen #deeplearning

These are my notes on [this article](https://github.com/chiphuyen/machine-learning-systems-design/blob/master/build/build1/consolidated.pdf) by [Chip Huyen](https://huyenchip.com/). 

The article that these notes are based on, talks about some factors that are involved in designing machine learning systems, and what to watch out for in interviews on the same. I wanted to write a summary of what I read and add my take on it for future reference.

As a note, I found Chip’s book [Designing Machine Learning Systems](https://www.amazon.com/Designing-Machine-Learning-Systems-Production-Ready/dp/1098107969) an excellent resource for anyone starting or willing to improve their skills in this field. I would recommend a read. (This is not sponsored by any means.)

## Interviews
- The major issue with Machine Learning interviews seems to be the lack of a standard criterion by which to judge a candidate. This makes a lot of sense considering how varied the requirements of each project are.
- Interviewers generally look for what they are familiar with and often this means that an ideal candidate would be someone who thinks along similar lines. This is especially interesting in ML because there are an infinite number of ways to approach a problem.
- It would be helpful for the candidate to understand what kind of answers the company would be looking for based on their previous work. 

## Compute requirements 
- Contrary to the vast amount of research in the ML space on improving models and focusing on metrics, in production, users might barely notice a tiny improvement in accuracy. In return, this would further increase the complexity of the system and thus its latency.
- It is important to first understand exactly what you wish to achieve and what you need to optimize for. 
- You cannot do everything.

## Setting Up The Project
- At the end of the day, an ML system also requires skills from Software Engineering. A complete system is not just a model but a lot of moving parts. Thus there are quite a few tradeoffs to consider.
- An initial thought process
	- Pick the top 2 goals that your solution needs
	- What does the user interaction look like?
		- Do you care about personalized results? 
		- Does latency matter?
		- How much of your system relies on ML?
		- What kind of devices are you looking at for deployment?
		- Does privacy matter?
	- Data
		- Do you have the data? 
		- Is it usable? Is it clean?
		- Where is it stored? How much of it is stored?
	- What metrics are useful in this context? (Domain expertise would be very helpful here)
	- What resources do you have/can acquire? People, time, users, etc

## Baselines
- These systems can get complex pretty fast. So start with the simplest possible algorithm. You might not even need a very complex Deep learning system. And it might not be feasible at the start.
- To evaluate if it is worth shifting to a more complex implementation, looking at baselines is essential.
	- Random Baseline: How well would a random guess do?
	- How well does a human do on this task? (If that is feasible)
	- What minimum results do you need for a functioning solution?

## Debugging Models
This is one endless minefield. 
In my experience, [this list](http://karpathy.github.io/2019/04/25/recipe/) by [Andrej Karpathy](http://karpathy.github.io/) is a pretty comprehensive guide. I do not have anything to add to it so I will skip this section.

As a recommendation though, I would suggest considering the use of a framework such as [fast.ai](http://fast.ai). These are built with a lot of issues in mind and take care of a lot of them. 

## Model Scaling
- Most large-scale systems these days use Parallel and Distributed computing. Multiple GPUs/TPUs etc.
- If your data does not fit into memory, there are many ways of getting it - Gradient checkpointing, Mixed Precision, and Parallelism are some of them. (Future blogs will go a lot more in-depth. Putting it here will make it pretty huge.)

## Inference
- There are a lot of steps and tradeoffs involved in inference. 
	- Where will you run your model? How long does it take? Can you say with certainty why a particular result is obtained? Can you retrain it? 
	- Before deployment, it is advisable to turn off all the modifications one by one and test how well the system performs without them.
	- Check for biases in the results. (For example: Does your model prefer colored people?)
	- Does your data remain constant? Or keep changing?

## Fin
The list of things to consider to make an efficient and thought-out model is endless. I do not think it is possible to take everything into account in the real world, but the more you think these through and follow these guidelines, the better and more stable your implementation will be.
Of course, this is more of a short primer rather than a comprehensive guide. Future articles will cover more details.

This article is in the hopes that it will help someone out. Maybe have the help that I did not. I do not know who it will reach. But to whoever it does, best of luck :)

You can contact me on [LinkedIn](https://www.linkedin.com/in/subhaditya-mukherjee-a36883100), drop me an [[mailto:msubhaditya@gmail.com|Email]]



