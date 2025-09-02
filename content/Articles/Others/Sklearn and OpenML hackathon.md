---
title: Sklearn and OpenML hackathon
toc: true
tags:
  - articles
  - openml
  - conference
date modified: Thursday 19th September 2024, Thu
date created: Thursday 19th September 2024, Thu
---

<!--section: 1-->
# Sklearn and OpenML Hackathon
```toc
```

<!--section: 2-->
## Intro

Scikit-learn is a free and open-source machine learning library for the Python programming language. If you are reading this article though, chances are that you have probably used it already. 

OpenML is an open platform for sharing datasets, algorithms, and experiments - to learn how to learn better, together.

Our teams have been working together for many years and both of us share the goal of developing the open-source ML space. 

We recently had a developers hackathon at the :Probabl. (a company built around scikit-learn focused on maintaining and expanding open-source ML in Europe) office in Paris. We met to discuss not only the state of AI and how both our organizations fit in, but also to brainstorm solutions to challenges faced by our developers and communities.

Many interesting topics were brought up, most of which were not only relevant to us but also to the broader open-source community. In the spirit of open-source, we wanted to share these insights with you.

<!--section: 3-->
## Community Engagement and Onboarding Contributors

The focus of this discussion was around community engagement and emphasized the importance of effectively attracting, onboarding, and retaining contributors, especially newcomers.

Over the past few years, both in OpenML and scikit-learn, we have been noticing that a majority of contributors are only active for short durations and do not stick around for too long. The ones that do are distributed between a smaller number of more experienced senior developers and a much larger pool of junior developers. This then leads to many PR's being of lower quality and thus requiring a lot more verification and correction. 

The question at hand then, is not only how we can attract new contributors to our projects but also how we can make it easier for them and our developers to maintain these projects. Some of the ideas that came up have been tried and tested by communities our colleagues have founded or been part of across the globe.

Takeaways:

<!--section: 3.1-->

- Emotional connection : All of the participants agreed that the most important part of any community is its people. Contributors only stick around if they have an emotional connection to either the project, or the people contributing to the project. In this vein, it would be nice if the maintainers of the project could also be present at events. It also helps if the contributors use the projects themselves.

<!--section: 3.2-->

- Focus on beginners : Since we see that most of our contributors are beginners, it serves to organize sprints that are inclusive of them with a focus on beginner-friendly issues, especially documentation tasks. Having these would not only help them understand the project and contribute better, but also let them form a connection with the project.

<!--section: 3.3-->

- Curated issues : Most of our external contributors have enough on their plate already. Having a curated list of issues before sprints would ensure that no time is wasted and let our contributors focus on the tasks suitable for them.

<!--section: 3.4-->

- Different tiers of events : To ensure that everyone is given tasks they can handle, it would be nice to have separate events for contributors with varying levels of expertise. This would also have the added benefit of retaining beginner-friendly issues for sprints to prevent more experienced contributors from claiming them early.

<!--section: 3.5-->

- Mentoring : Incorporating one-to-one mentoring to help new contributors set up their development environments would help them feel more connected to the project. It is understandable that this is time consuming, so perhaps some way of deciding who gets mentored can be set up in time.

<!--section: 3.6-->

- Contributors guide : Simplifying the contributor's guide and adding video tutorials would make it a lot more beginner-friendly, especially to those who have never filed a PR before.

<!--section: 3.7-->

- Semi regular events : Some of our colleagues found that they tended to care about a project more if there were semi regular events they could set time aside for. Having these helped them slowly build a sense of community as well.

<!--section: 3.8-->

- Incentives : A common question that many developers have is why they should even bother contributing. Helping them understand how contributing to open source projects can aid their careers, bring them closer to the community and also help them get internships would be a good start.

<!--section: 4-->
## Governance, Funding, and Sponsorship

This focus of this discussion was the governance structures of open-source projects, sustainable funding models, and the role of sponsorships in supporting project activities.

Takeaways:

<!--section: 4.1-->

- Evolving Governance : Since governance is not static, we can treat it as a living document that evolves with the needs of the community.

<!--section: 4.2-->

- Communication: It is good practise to maintain open communication channels, such as mailing lists and monthly meetings. This keeps all interested contributors in the loop.

<!--section: 4.3-->

- Reviews: A major challenge is that of approving new reviews in a large organization without passing through too many hoops. How to manage this is still an open question.

<!--section: 4.4-->

- Sponsorship: It would be nice to explore sponsorship models like the INRIA foundation, where companies contribute to meetings and have a say in setting priorities.

<!--section: 4.5-->

- Corporate partnerships: To keep investors interested, it would also be interesting to look into corporate partnerships (similar to those used by the Linux Foundation) that are of mutual benefit.

<!--section: 5-->
## Development Tooling and Workflows

<!--section: 5.1-->

Setting up and maintaning CI/CD pipelines across multiple repositories and programming languages puts a huge burden on the maintainers of the repositories.

Having to keep up with the trends and learn new technology very frequently also makes developers more reluctant to change the stack, even if doing so would be beneficial.

This discussion looked at how to tackle these challenges and make it easier for developers to handle such complex workloads.

<!--section: 5.2-->

Takeaways:

<!--section: 5.2.1-->

- Automation: Automating as much of the CI/CD pipeline as possible by using bots for linting and code coverage checks makes PR quality control easier.

<!--section: 5.2.2-->

- Better workflows: Migrating to Github Actions and Azure workflows for testing and deployment also seems to help significantly.

<!--section: 5.2.3-->

- Better tools: There are many open source platforms/tools that offer comparable convenience to tools that are currently used. Some examples of these are CodeBerg and Forgejo. Eventually migrating to using these tools might also help manage projects like Scikit-Learn and OpenML.

<!--section: 5.2.4-->

- CircleCI: Tools for rendering documentation examples directly in the browser can also be used to enhance the review process.

<!--section: 6-->
## Broader Ecosystem and Scope of Collaboration

<!--section: 6.1-->

While both OpenML and Scikit-Learn focus on the open source ML community, it is sometimes hard to explain how we fit into the broader AI ecosystem. 

Especially with the rise of LLMs and Generative AI, stakeholders are somewhat inclined to think that frameworks such as ours are just not "enough". Of course, this is not true at all.

<!--section: 6.2-->

Takeaways:

<!--section: 6.2.1-->

- Community projects: There are so many successful examples of open source projects, and a lot can be learned from their efforts. Projects like Scientific Python for example, has very well setup CI documentation and governance processes that can be quite readily applied to any open source project.

<!--section: 6.2.2-->

- Exploring connections: A longer term focus for both our teams would be to explore connections with other open-source ML frameworks, such as PyTorch, Tensorflow and other AutoML tools. Doing so would also help integrate and strengthen the open-source ML communities and ecosystems.

<!--section: 7-->
## Discussion on Croissant

<!--section: 7.1-->

Machine Learning datasets are a combination of structured and unstructured data, which makes them all the more complicated to manage. This has led to the rise of multiple "dataset formats" which further make it hard to consistently load data across platforms and tools.

[Croissant](https://github.com/mlcommons/croissant) is one such dataset format which directly tackles the issue of consistency. This format is now not only compatible with the most popular ML libraries/platforms (sklearn, PyTorch, Tensorflow, Kaggle, Hugging Face), it is also recommended by NeurIPS (one of the topmost conferences in the AI space).

<!--section: 7.2-->

Features of Croissant:

<!--section: 7.2.1-->

- Schema.org: Croissant was built on top of schema.org with more metadata information specific to ML datasets. Since it does not require any changes to the underlying data structure, existing datasets can quite easily be converted to use it.

<!--section: 7.2.2-->

- Layers: The format has 4 layers - Dataset level metadata, resource descriptions, content structure, and ML semantics. Each of which make it possible to encode and maintain structural information about datasets regardless of platform.

<!--section: 7.2.3-->

- XAI and Visualization: Analysis and visualisation of the data works out of the box for all datasets and across multiple platforms. Croissant also supports the Core RAI vocabulary for explainable AI.

<!--section: 7.2.4-->

- Supported Platforms: Every dataset in OpenML has a Croissant representation, while a majority of data on Kaggle and Google Dataset search also support it.

<!--section: 8-->
## Conclusion

Overall, this discussion was quite a successful one for both of our teams. We learnt a lot from each other and found new ways of collaborating on our shared dream of open-source ML. So much infact, that we wanted to share our discussion with you, dear reader.

We hope you learnt something new. We would love to welcome you to our community and would be glad to support your journey in this ML space.

❤️ The OpenML and Scikit-Learn team