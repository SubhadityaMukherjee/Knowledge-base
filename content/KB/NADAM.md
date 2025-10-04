---
toc: true
title: NADAM

tags: ['optimizer']
date modified: Sunday 12th February 2023, Sun
date created: Sunday 12th February 2023, Sun
---

# NADAM


- extension of Adam that uses the Nesterov momentum technique to accelerate the optimization convergence further
- combines the momentum of Nesterov’s method with the adaptive learning rates of Adam
- $$ m_t = \beta_1 * m_{(t-1)} + (1 - \beta_1) * g_t $$ $$ v_t = \beta_2 * v_{(t-1)} + (1 - \beta_2) * g_t2$$ $$ \hat{m_t} = \frac{m_t}{1-\beta_1t} $$ $$ \hat{v_t} = \frac{v_t}{1-\beta_2t} $$ $$ \text{parameter} = \text{parameter} - learning\_rate * \frac{\hat{m_t} + (1-\beta_1) * g_t}{\sqrt{\hat{v_t}} + \epsilon}$$
- Where beta1 and beta2 are two hyperparameters, m_t and v_t are moving averages of the gradients, g_t is the gradient at time t, and learning_rate; epsilon is the same as before.



