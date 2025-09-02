---
tags: ['temp']
date created: Thursday, August 11th 2022, 12:32:22 am
date modified: Monday, October 10th 2022, 2:02:29 pm
---

# Disparate Treatment
- Factoring subjects' sensitive attributes into an algorithmic decision-making process such that different subgroups of people are treated differently.
- For example, consider an algorithm that determines Lilliputians’ eligibility for a miniature-home loan based on the data they provide in their loan application. If the algorithm uses a Lilliputian’s affiliation as Big-Endian or Little-Endian as an input, it is enacting disparate treatment along that dimension.
- Contrast with [[Disparate Impact.md]], which focuses on disparities in the societal impacts of algorithmic decisions on subgroups, irrespective of whether those subgroups are inputs to the model.
- Because sensitive attributes are almost always correlated with other features the data may have, explicitly removing sensitive attribute information does not guarantee that subgroups will be treated equally. For example, removing sensitive demographic attributes from a training data set that still includes postal code as a feature may address disparate treatment of subgroups, but there still might be [[Disparate Impact.md]] upon these groups because postal code might serve as a proxy for other demographic information.



