---
title: Pragmatic engineer blogs
toc: true
tags:
  - blog_notes
  - software
date modified: Thursday 6th February 2025, Thu
date created: Thursday 6th February 2025, Thu
---

# Pragmatic Engineer Blogs
```toc
```
## [stackoverflow vs chatgpt](https://blog.pragmaticengineer.com/are-llms-making-stackoverflow-irrelevant/)

- ![](https://blog.pragmaticengineer.com/content/images/2025/01/2.webp)
- **The drop in questions indicates that trouble is ahead.** Most of StackOveflow's traffic comes from search engines, so this decline is unlikely to have an equally dramatic _immediate_ drop in visits. However, any fall can turn into a vicious cycle: with fewer questions asked, the content on the site becomes dated and less relevant, as fewer questions mean fewer up-to-date answers. In turn, the site gets less search engine traffic, and visitors who get to the site via search find answers woefully out of date.
- where will LLMs get new training data from if stack overflow is not being used
## [Is the “AI developer”a threat to jobs – or a marketing stunt? - The Pragmatic Engineer](https://blog.pragmaticengineer.com/ai-developer-marketing-stunt/)
- "Devin is the new state-of-the-art on the SWE-Bench coding benchmark, has successfully passed practical engineering interviews from leading AI companies, and has even completed real jobs on Upwork.
- Devin is an autonomous agent that solves engineering tasks through the use of its own shell, code editor, and web browser.
- even Cognition AI admits that the tool only solved about 1 in 7 GitHub issues unassisted in tests.
- What if it's a well-choreographed show performed out of necessity?
- **What if AI dev tool startups have been backed into a corner by Microsoft, which has eaten their lunch?**
- the only major source control platforms that don't have AI assistants yet are GitLab and Bitbucket, and this is surely just a matter of time.
- This means, one of the few ways to launch an AI dev tools startup is to claim you will _fully_ replace software engineers. Anything less, and there's no reason why developers should swap their existing coding assistant, and open up their codebase for a brand new tool to crawl and contribute to.
- **The good news is the claim "you will not need software engineers" has been on repeat since the 1960s**
- Efficient frameworks are continuously created so that fewer developers can build the same application; no-code tools promise to build software without the need of developers. And while all of these initiatives partially succeed: we keep observing a need for software developers.
- LLMs have a core problem with hallucination, and coding is one of the few use cases of adding a second validation loop to test the modified code and eliminate this hallucination
## [A Comment Is An Invitation For Refactoring - The Pragmatic Engineer](https://blog.pragmaticengineer.com/a-comment-is-an-invitation-for-refactoring/)
- **A comment is an apology** for not choosing a more clear name, or a more reasonable set of parameters, or for the failure to use explanatory variables and explanatory functions.
- The problem with comments is that they have no compile-time check and _tend to be forgotten_. It's very easy to change your code but forget about the comments.
- I come across this pattern fairly often, where there are several comments splitting up parts of a long method
- This is an invitation to again extract the sections the comments refer to.
- explain how a bug is eliminated by some otherwise hard to understand line(s) of code
- Commented out code is dead code, and dead code rots your codebase.

## [Stop Calling it Bad Code - The Pragmatic Engineer](https://blog.pragmaticengineer.com/bad-code/)

- **Be specific** on the flaws you see, even at the cost of being more verbose. _"I find this function too complicated".__"This class has multiple responsibilities". "The variable name does not describe its purpose clearly"._
- **Give a specific suggestion ** on how to improve the issue, if it not obvious from your description.
- **Talk about the future implications of the code you see, if not changed**.
- **Ask the person writing the code**, what they think about your comments.
- By not using generic and negative terms like "bad", conversations about code become constructive.

## [Talk First, Code Later - The Pragmatic Engineer](https://blog.pragmaticengineer.com/talk-first-code-later/)

- **When making changes to a system you are not familiar with, follow these steps to reduce churn**:
- **Summarize the problem** you're trying to solve. Talk with people owning the system, sharing your problem.
- **Share and validate** the fix you're thinking of. Reach out to engineers on the owning team: in-person, over chat/email or a call, and talk
- **Describe your code changes clearly**,
- It's interesting how problems like this are mostly nonexistent when the whole team is colocated.
- However, when working across locations, the "t
- talk first, code later" _approach is an un-intuitive tool that speeds development up and leads to better communication between engineers and teams

## [Efficient Software Project Management at its Roots - The Pragmatic Engineer](https://blog.pragmaticengineer.com/efficient-software-project-management-at-its-roots/)

- Many projects I've seen go south were ones where stakeholders were not aligned
- A common tool I see used is via a **project kickoff with all stakeholders present **_and_** involved**. By all stakeholders, I mean everyone who will be working on the project or will have some sort of input.
- Given this is an expensive meeting, the person leading the meeting typically prepares an overview about the background ("why"), goals ("what") suggested approach ("how") and end state.
- In order to keep clarity throughout the project, as well as an ongoing sense of focus, milestones that help the team focus are something I've seen work exceptionally well.
- **no-BS update**
	- For distributed teams, an email to all internal stakeholders can work well. For teams onsite, a team check-in with stakeholders locally present also works nice
	- It's meant to be a quickly thrown together description on where the team is against the milestones, what the upcoming goals are for the next period and what progress was made the last period
	- By creating a culture where people commit to short-term goals, then hold themselves accountable and check in with each other helps keep both feet on the ground.
- have a culture that rewards raising concerns early on and be pragmatic in tradeoffs to mitigate risk
- Most of the risk in software projects is discovered by engineers, on the ground. The best engineers love problem-solving and are naturally optimistic. So when they come across a problem, they see a challenge to solve, not a potential delay to the project.

## [Pull request best practices - The Pragmatic Engineer](https://blog.pragmaticengineer.com/pull-request-or-diff-best-practices/)

- Easy to review means easy to understand
- **Keep the title short, but expressive enough to signal what the reviewer can expect**
- People reviewing the code spend a lot less time thinking about the change as the author
- Providing the context in the description
- "before" and "after" screenshots

## [The Product-Minded Software Engineer - The Pragmatic Engineer](https://blog.pragmaticengineer.com/the-product-minded-engineer/)

- At companies building world-class products, product-minded engineers take teams to a new level of impact.
- _Once you have the product foundations, you need devs who engage with the 'why', actively._
- Great product engineers know that minimum lovable products need the right depth**_ to be considered during the build phase._
- They often challenge existing specifications, suggesting alternative product approaches, that might work better.
- They take the time to understand how the business works, how the product fits in, and what its goals are.
- Why build this feature for the product, why not the other one? Why ship this first milestone, instead of choosing another one, that's a lot simpler to build? How will things be measured - why don't we choose a more thorough way to measure things?
- Product-minded engineers like talking with people outside engineering, learning about what and why they do
- both looking for engineering tradeoffs and what the product impact is.
- They also start making product tradeoffs, evaluating the engineering impact. They often go back to the product manager, suggesting a completely different feature to be built, given the product impact would be similar, but the engineering effort vastly smaller.
- They are focused on the "minimum lovable product concept" and evaluate the impact of an edge case and the effort of handling it.
- Even before the feature they are working on is production-ready, product-minded engineers find creative ways to get early feedback.
- They consider their work done only after getting results on user behavior and business metrics. After rollout, they still actively engage with product managers, data scientists, and customer support channels, to learn how the feature is being used in the real world.
- **Understand how and why your company is successful**. What is the business model? How is money made? What parts are most profitable, what parts of the company are expanding the most? Why? How does your team fit into all of this?
- Most product managers jump at the opportunity to mentor engineers.
- Being a great product-minded engineer means you have built up good product skills, on top of your existing engineering skillset.

## [Growth hacks: coffee with an experienced engineer you don’t know - The Pragmatic Engineer](https://blog.pragmaticengineer.com/growth-hacks-coffee-with-an-engineer/)

- **Developers buying coffee and having a chat with other, local developers is an underrate hack for professional growth. It is also under-used**.
- Whenever I get a reach-out from a person in the local developer community, I make a point to try to make time for this.
- **Shared connections **help with these kind of reach-outs.
- **You're the one asking for a favor **
- You might feel that you have less to offer, but do some research on what this person does.
- You want to get the most out of this time, so draft up topics you'd like to get their input on
## [Readable Code - The Pragmatic Engineer](https://blog.pragmaticengineer.com/readable-code/)

- Principles of readable code
- All building blocks - classes, methods, variables - follow the single responsibility principle: every building block does exactly one thing.
- The codebase is easy to navigate around, as functions, classes, modules follow a logical structure.
- Class, function, and variable names all help understand what is happening, and making reading more seamless.
- The code tries to be as humble and simple as possible.
- Functions are mostly short, making them easy to read. Classes are also not overly large.
- Most of the code can be understood by itself. Comments fill in the remaining gaps.
- Well-tested code can be modified quickly and without fear of breaking things.
- Without tests, refactoring the code becomes risky, and developers eventually stop doing it. With tests, there is no excuse on why not to make even large and risky refactors, that keep the code easy to read.

## [Tech Debt and the Pragmatic Middle Ground - The Pragmatic Engineer](https://blog.pragmaticengineer.com/tech-debt/)
- **Tech debt is the incremental cost of doing software development**. Tech debt is what happens when more code builds up, and things become more complex.
- For a new codebase and a greenfield project, this incremental cost is zero
- But the more complex the code gets, the more effort is to change the code while keeping things working.
- Codebases that are hacked together and have little to no automated testing or documentation become very time consuming to change.
- Debt used smartly can accelerate progress. When used poorly, it can become expensive to maintain. And bankruptcy through tech debt is also a thing: this happens when it's cheaper to delete and rewrite the codebase than it is to maintain or fix it.
- readable code
- Testing
- Code reviews
- CI / CD
- Documentation
- Sane architecture decisions
- Beware of broken windows.
- When there's a lot of something - like tech debt - you won't be able to tackle it all.
- Sure, there is duplication across the code. What would the impact be if you moved things to a shared library? And what is the cost? The impact will be far higher with a codebase that's frequently used. On the other hand, a soon-to-be deprecated codebase might mean a large effort, and a small reward.
- Slow build times? If the build is run frequently by many people, the impact could be large.
- Flaky tests? The impact likely high, the effort hopefully low. Verbose boilerplate code? Perhaps lower impact, some work. Naming you personally don't like? Probably small impact, and could be lots of effort. All of this will depend on your environment.
- Reliability, cost savings, faster development cycles, and fewer bugs are the most common impact factors I've seen people pitch to get larger tech debt removal or migration projects funded from the top.
- **Pair tech debt removal with high-impact projects**. Unfortunately, most of the time, it will be hard to make a case for an only-tech-debt-removal project. Why is this? It's because teams always aim to work on the most impactful project - the one delivering the most business value. Business value often being revenue, user metrics, and the like.
- Touching systems that have high tech debt means they're much slower to change already.
- If you want to see your large tech debt reducing proposals through, couple them with high-impact projects.
- The name of too little tech debt is premature optimization - and it can slow down teams and companies at critical times.
- The startups I've worked at that grew to be successful all went for the tech debt-heavy approach in the early days.
