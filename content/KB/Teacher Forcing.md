---
toc: true
title: Teacher Forcing

tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:15 pm
date created: Thursday, July 28th 2022, 5:59:06 pm
---

# Teacher Forcing
- [from](https://publish.obsidian.md/fabian-groeger/Machine+Learning+%26+Deep+Learning/Deep+Learning/Architectures/RNN/Teacher+Forcing)
- Technique where the target word (ground truth word) is passed as the next input to the decoder instead of its last prediction.
- common technique to train [Basic RNN Architectures](Basic%20RNN%20Architectures.md) or [Transformer](Transformer.md)
    - used in [imageCaptioning](imageCaptioning.md) , Machine Translation
    - but also in Time Series forecasting
- intuition
    - math exam with dependent questions, e.g. a) depends on b), b) on c) and so on
    - if a) is wrong, all subsequent questions are also wrong
    - teacher forcing: after answering question a), the teacher compares it to the correct solution and grades it and then gives us the correct answer for a) to continue with
- for example in sequence generation with RNN the situation is similar
    - each prediction depends on the last one, thus when one is wrong all subsequent will be wrong as well
- no memorization can happen
    - the network can not look into the future
    - ground truth is only fed as last $y_{t-1}$ prediction not as the current $y_{t}$
- [loss](../Tag%20Pages/loss.md) does not need to be updated at each timestep, only needs to have a list with the true predictions of the model from which then the [loss](../Tag%20Pages/loss.md) is calculated
- pros
    - training converges faster, because early predictions are very bad
- cons
    - no ground truth label during inference, thus no teacher forcing
    - discrepancy between training and inference scores
        - can lead to poor model performance and instability
        - known as _Exposure Bias_



