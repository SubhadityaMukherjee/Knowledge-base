---
toc: true
title: bitter_lesson
tags:
  - deeplearning

date modified: Monday 24th June 2024, Mon
date created: Monday 24th June 2024, Mon
---

<!--section: 1-->

# The Bitter Lesson

- [Richard sutton](https://www.cs.utexas.edu/~eunsol/courses/data/bitter_lesson.pdf)
- The biggest lesson that can be read from 70 years of AI research is that general methods that leverage computation are ultimately the most effective, and by a large margin
- Seeking an improvement that makes a difference in the shorter term, researchers seek to leverage their human knowledge of the domain, but the only thing that matters in the long run is the leveraging of computation

<!--section: 1.1-->
- In computer chess, the methods that defeated the world champion, Kasparov, in 1997, were based on massive, deep search. At the time, this was looked upon with dismay by the majority of computer chess researchers who had pursued methods that leveraged human understanding of the special structure of chess. When a simpler, search-based approach with special hardware and software proved vastly more effective, these human-knowledge-based chess researchers were not good losers. They said that \`\`brute force\" search may have won this time, but it was not a general strategy, and anyway it was not how people played chess. These researchers wanted methods based on human input to win and were disappointed when they did not.
- Learning by self play, and learning in general, is like search in that it enables massive computation to be brought to bear.
- statistical methods won out over the human-knowledge-based methods
- Deep learning methods rely even less on human knowledge, and use even more computation, together with learning on huge training sets, to produce dramatically better speech recognition systems.
- The bitter lesson is based on the historical observations that 1) AI researchers have often tried to build knowledge into their agents, 2) this always helps in the short term, and is personally satisfying to the researcher, but 3) in the long run it plateaus and even inhibits further progress, and 4) breakthrough progress eventually arrives by an opposing approach based on scaling computation by search and learning

<!--section: 1.2-->
- great power of general purpose methods, of methods that continue to scale with increased computation even as the available computation becomes very great
- scale arbitrarily in this way are search and learning.
- the actual contents of minds are tremendously, irredeemably complex; we should stop trying to find simple ways to think about the contents of minds, such as simple ways to think about space, objects, multiple agents, or symmetries.
- They are not what should be built in, as their complexity is endless; instead we should build in only the meta-methods that can find and capture this arbitrary complexity
- they can find good approximations, but the search for them should be by our methods, not by us
