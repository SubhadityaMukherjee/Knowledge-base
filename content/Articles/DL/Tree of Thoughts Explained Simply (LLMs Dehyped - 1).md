
---
toc: true
title: Tree of Thoughts Explained Simply (LLMs Dehyped - 1)

tags: ["article"]
date modified: 
date created: 
---

<!--section: 1-->

# Tree of Thoughts Explained From Foundations (LLMs Unhyped - 1)
> “Programmers are, in their hearts, architects, and the first thing they want to do when they get to a site is to bulldoze the place flat and build something grand.” : Joel Spolsky, co-founder of Stack Overflow

## Introduction
Large language models like GPT4 have taken over the world and has left every second IT person to scramble towards the next great AI solution. Given the monetary benefits, a lot of research has popped up in a very short time. While this is very exciting, it is wise to look a little deeper beneath the hype. The “new groundbreaking research from {X} that will change your company” is sometimes a tiny change or a creative use of an existing concept. 
This is not to pour cold water over your dreams, but a way to help you understand these concepts better. If you did not come from a technical computer science background, this constant influx of “groundbreaking research” can get very overwhelming.

So here is a more sober, in depth view of how the “Tree of thoughts” [1] paradigm came into being from concepts that have been around for decades and creatively applied to LLMs.

Note : Both the research and my understanding of it fluctuates over time and if something changes, I will try to come back and correct it. If you notice something weird, do drop a comment!

<!--section: 2-->

## What is the Tree of Thought?
If you have not already encountered it, the Tree of Thoughts claims to help an LLM arrive at a more logical conclusion and also generate the steps it took to come to it.

It was first mentioned in a paper by Yao et al. [1] and was further expanded on by a LOT of articles and papers. As the authors say, it is a way of “Deliberate Problem Solving with Large Language Models”.

But you might ask, why do we care? I just want my assignment done for me.

<!--section: 3-->

## Why Bother Adding it to an LLM?
To better understand why we care about algorithms like this, we need to dig into some of the shortcomings behind LLMs.
- **Fixed Knowledge** : A LLM is trained on a large text database encompassing a huge chunk of the web. But the web is not a fixed resource, neither is the information in it. Unless the model is trained with new data or an external data source is given to it, it’s “knowledge” is essentially fixed.
- **Cost of training** : Training a LLM like ChatGPT is extremely costly, and it is just not possible to keep updating the model everytime something new pops up on the internet. 
- **Knowing everything is not the point** : At it’s heart, an LLM is not meant to know everything. It is just a text model - it predicts the next word in a sentence. Using it as a model that can understanding text and it’s underlying relations is a better and cheaper way to use it.
- **Logic** : It is not easy to understand the steps an LLM took to arrive at an answer. Neither is it easy to make it follow logical steps without knowing the logic in the first place.
- **Structured Data** : LLMs are great at making sense of large amounts of unstructured data. But it is not meant to be good at working with structured data like graphs by itself. There are workarounds, but it is not something an LLM can do by itself.

Given these shortcomings, the Tree of Thought is an attempt at combining classical “logical search algorithms” with LLMs. How? Well, read on.

<!--section: 4-->

## Theoretical Background
This section is for you, the reader who want to dig deeper and understand the actual concepts that led to the research. If you just want to mash together models and don’t really care how they work. Just skip to the next section.

Now, if you have a background in computers, you will recognize these terms. If you don’t, then pay attention. It will help you understand a lot of research in this domain.

<!--section: 4.1-->

### Chain of Thought
The Tree of Thought is derived from a theoretical computer science concept - the “Chain of Thought”. 
Simply put, the Chain of Thought is a logical breakdown of a task into it’s simplest steps. Instead of trying to solve a problem as a whole, we try to solve it in parts and then combine the result.
Why? Well, it is a lot easier to do and writing it formally makes it possible for others to understand how you arrived at the solution. (Think of trying to solve for x in a math equation.)
It also adds in error checking. If something went wrong, you can backtrack and find the bug.

Eg: You want to check if it’s raining outside. How would you break down the steps?
Look outside the window -> Check for rain clouds -> Check if there are raindrops -> Check the ground to see if it is wet -> If all the conditions are satisfied, you know it is raining.

<!--section: 4.2-->

### Trees
In computing, a tree is a way of representing this chain of thought. It’s main advantage is that once we create a tree of steps, it is possible to iterate over it and reach a logical conclusion or explore options.

A tree has a root node (eg: Is it raining) and leaf nodes (eg: rain clouds, wetness). The leaf nodes are arranged in levels and are connected to previous levels (eg: clouds -> ((present) , (absent)) )

<!--section: 4.2.1-->

### Traversing a Tree
Once we have a tree, there are many ways of traversing on it. Choosing an algorithm usually depends on what you need, and how much compute you are willing to use. Some of the approaches used in the paper are as follows (high level explanations): 

- **Breadth First Search** : This is used to find the shortest path from the root to a leaf. The tree is traversed layer by layer and all nodes at each level are evaluated. If a match is found, the algorithm stops. This is quite fast.
- **Depth First Search** : This is used if you want to explore your options and find new possibilites. The tree is traversed by starting at a node and going as deep as possible from there until the end. If a match is found, the algorithm stops. If not, it backtracks and goes to the next node. This is much slower, but is useful in certain cases.
- **Other Options** : Covering the whole lot (like A*) is beyond the scope of this article, but you can refer to [4] if you want to learn more.

<!--section: 4.3-->

### Ensemble Learning
A large portion of ML algorithms are stochastic (if you run it again, you will get a different result). While this is good for tasks like creative writing, it is not great if you want logical answers. 
One way around this is to use multiple similar models on the same data and then “average” out the results. This somewhat helps to counter the randomness and usually leads to better performance. 

There are many ways of combining these results - Weight them and use a mix of them, use a majority vote, use a separate model to evaluate which result is better etc. 

Can you see how this would be useful for an LLM when trying to solve a logical problem?

Want to learn more? Refer to [3].

<!--section: 5-->

## Tricking an LLM
Now that you understand the background, let us dive into how this works with an LLM. 
So, what do we want to do? Simply put, we want the LLM to come up with different answers that we can then put into a graph. We can then use this graph to arrive at a more logical solution.
Spoiler : Can you see why this would not always be a good idea?

<!--section: 5.1-->

### Prompts
How do we do it? Quite simple really, we first define a format such as “the answer is {n} because {x1} and {x2} lead to {n}”. We then prompt multiple times using a prompt like “solve it in multiple ways while pretending to be three different experts” and save the results. We also add a prompt like “only use the information give”, and voila! We have a graph.

Well, mostly. The answers you get might or might not be useful.

<!--section: 5.2-->

### Ensemble
Now that you have the answers, provided your prompt has the logic you want, you can decide how to traverse the graph and find the best answer. You can also then repeat this multiple times and vote on the best result from multiple graphs.

<!--section: 6-->

### Evaluation
If you know exactly how to evaluate the task (eg: The best step for a robot to take when choosing to get left or right depends on if it will hit something or not), then you can use that as a criteria. But well, this is neither always possible. If you already knew what you wanted, then you would probably not be using an LLM.

The paper asks the model to evaluate how well it did itself. Respectfully, this might be a bit dubious for real world issues if unchecked.

<!--section: 7-->

## Immediate Shortcomings
While the Tree of Thought is quite a nice idea, there are quite a few issues that immediately crop up.
- **Evaluation** : How can we decide if the answer is correct. Say for a math problem, if you knew how to get to the right step, why would you use an LLM? And for say a creative writing task, how can you even evaluate if the answer was correct?
- **Manual Effort** : Using a Tree of Thought in practise requires a bit of manual effort in creating the perfect logical prompt, and knowing the evaluation steps beforehand. This might not always be useful.
- **Bias** : Asking a model to evaluate how well it did is to ask a math student to see if they got the problem right. If they knew how to check, why would they want to explore other paths? But perhaps it could encourage them to think deeper about other aspects of a problem.
- **Computation** : This is a big one. Running an LLM is expensive. For most tasks, running a model multiple times and then further algorithms is not exactly compute friendly. 
- **Not everything needs an LLM** : As they say, “when you have a hammer, everything starts looking like a nail”. An LLM is useful, but not everywhere.

<!--section: 8-->

## Perks
So when would you actually want to use them?
- **Generating Data** : An LLM comes with a lot of knowledge inbuilt. Perhaps this is a good way to generate data for a different task. Using a Tree of Thought would enable an LLM to come up with much better and more logical examples.
- **Forcing an LLM to think more** : Instead of taking the first result for granted, you can force the LLM to think a step deeper. Like a kid asking “why?” multiple times, perhaps a better answer can be reached.
- **Combining with Knowledge Bases** : Combining the language understanding capabilites of LLMs with existing knowledge bases is pretty useful. While this area is a little different from the Tree of Thought, they are related concepts. Perhaps in the future these ideas will be combined to improve LLMs even further [6].
- **Domain Specific Information** : This could be used as a means of injecting domain specific logical steps to the results obtained from an LLM.

<!--section: 9-->

## Why “LLMs Unhyped”?
This is the first article in the series *LLMs Unhyped*. A rather weird name, I know. But why even have this series in the first place?
LLMs are amazing, but they are still in the research phase. With companies like OpenAI and Hugging face, it is now possible for a lot of people to work with these massive AI pipelines without much effort.

While that is an amazing feat in itself, and so many great ideas come out of it, it also leads to a lot of misinformation. In the hype of AI, many people who don’t fully understand the background research end up  using these massive models in places where they were probably not needed. 

Sometimes, it’s awesome. But in other times, it is a massive waste of money. Now ultra large corporations want you to spend your money on them, why wouldn’t they? But occasionally it’s like using a helicopter to get to a supermarket 100m away. 

AI has it’s uses. But not everywhere. By no means is this a critique against research or enjoying the magic of AI. Please, continue to do that! But consider your options too. At the end of the day, this is just yet another tool.

<!--section: 10-->

## Some More Resources for You :)
- [1] Tree of Thoughts : https://arxiv.org/abs/2305.10601
- [2] Graph of Thoughts : https://arxiv.org/abs/2308.09687
- [3] Voting Algorithms : https://scikit-learn.org/stable/modules/ensemble.html#voting-classifier
- [4] Graph Search Algorithms : https://en.wikipedia.org/wiki/Graph_traversal , https://en.wikipedia.org/wiki/Pathfinding
- [5] Roadmap of KB + LLM : https://arxiv.org/abs/2306.08302

<!--section: 11-->

## Fin
This article is in the hopes that it will help someone out. Maybe have the help that I did not. I do not know who it will reach. But to whoever it does, best of luck :)

Like these/Want more? Buy me a coffee! [Kofi](https://ko-fi.com/subhadityamukherjee)

Want articles on something specific? Just ask!

You can always contact me on [LinkedIn](https://www.linkedin.com/in/subhaditya-mukherjee-a36883100), or drop me an [[mailto:msubhaditya@gmail.com|Email]]
