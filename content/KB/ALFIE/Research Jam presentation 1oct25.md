---
title: Research Jam presentation 1oct25
toc: true
tags:
date modified: Tuesday 30th September 2025, Tue
date created: Tuesday 30th September 2025, Tue
theme: moon
height: "1200"
---

# Alfie - research jam 

```toc
```

## Overview
- Generate AI models based on user constraints
- User : Wants an AI model, might not know what that entails
	- Pitfalls : Bias, loads of extra time, no proper evaluation or explainability
- Extra sources of information to help guide the user
- Use cases - Website Accessibility checker, Compliance screening, Driver drowsiness detection
- Spot the problem? :o (remember this is AutoML)


## AutoML and AutoML+ 
- Initial idea : use an LLM to create, train and deploy models. But sustainably, cheaply and as fast as ChatGPT :)
- New idea:
	- Transfer learning (Hugging face, other sources) (for vision atleast)
	- Tabular - AutoGluon (for now atleast)
	- Basically function calling a model + data (image/prompt)
	- Eg: Website accessibility - Alt text checker model (qwen2.5vl for now) + Using LLMs to check guidelines (gemma3:4b for now)

## Architecture (fun landmarks)
![[images/image21.png]]



## Demos (well, screenshots)

### Website Accessibility
- ![[Pasted image 20250930182016.png]]
#### Chunk 0 - **Score:** 6
- **Missing ARIA attributes**  
    The page lacks ARIA attributes to enhance accessibility for users with assistive technologies. Consider adding roles and attributes to elements like the `container` div to provide semantic meaning and improve navigation.  
    Example:
    ```html
    <div class="container" role="region" aria-label="Content Area">
    ```
- **Color Contrast**  
    Evaluate the color contrast between text and background colors for sufficient readability, especially for users with low vision. While the current colors are generally acceptable, automated tools can identify potential issues.  
    Use a contrast checker to verify compliance with WCAG guidelines (at least **4.5:1** for normal text and **3:1** for large text).

- **Keyboard Navigation**  
    Ensure that all interactive elements (links, buttons, form fields) are accessible and navigable using the keyboard. Check that the tab order is logical and predictable.
- **Link Text**  
    Review link text to ensure it’s descriptive enough for users to understand where the link leads. Avoid generic phrases like _“click here.”_  
    Example:
    
    ```html
    <a href="#">Learn more about the Rubin Observatory</a>
    ```


#### Chunk 1 - **Score:** 6
- **Image `alt` text**  
    The `alt` text `"This is a dog"` is inaccurate and misleading. The image shows a monkey, not a dog. It should accurately describe the content.  
    Example:
    
    ```html
    <img src="https://media.cnn.com/api/v1/images/stellar/prod/160107100400-monkey-selfie.jpg?q=w_1160,c_fill/f_webp" 
         alt="Monkey selfie">
    ```
    
- **Color Contrast**  
    While not explicitly stated, it’s recommended to verify text-to-background contrast for readability. Use a contrast checker to ensure compliance with WCAG guidelines (**minimum 4.5:1** for normal text, **3:1** for large text).

#### Readability Report
- **Flesch Reading Ease:** 23.75 (very difficult to read)
    
- **Difficult Words:** 205
    
- **Lexicon Count:** 653
    
- **Average Sentence Length:** 18.66


### Tabular

![[Pasted image 20250930182755.png]]
#### Results

|     | model               | score_test | score_val | eval_metric | pred_time_test | pred_time_val |   fit_time | pred_time_test_marginal | pred_time_val_marginal | fit_time_marginal | stack_level | can_infer | fit_order |
| --: | :------------------ | ---------: | --------: | :---------- | -------------: | ------------: | ---------: | ----------------------: | ---------------------: | ----------------: | ----------: | :-------- | --------: |
|   0 | NeuralNetFastAI     |      0.942 |   0.94368 | accuracy    |      0.0114009 |    0.00471711 |     4.5952 |               0.0114009 |             0.00471711 |            4.5952 |           1 | True      |         3 |
|   1 | LightGBM            |      0.941 |  0.952441 | accuracy    |      0.0684869 |      0.023917 |    6.77049 |               0.0684869 |               0.023917 |           6.77049 |           1 | True      |         5 |
|   2 | WeightedEnsemble_L2 |       0.94 |  0.953692 | accuracy    |      0.0863461 |     0.0385489 |    6.78659 |              0.00211716 |            0.000275135 |          0.012337 |           2 | True      |         6 |
|   3 | LightGBMXT          |      0.932 |  0.941176 | accuracy    |      0.0894179 |     0.0278277 |    13.5024 |               0.0894179 |              0.0278277 |           13.5024 |           1 | True      |         4 |
|   4 | KNeighborsDist      |     0.2235 |  0.244055 | accuracy    |      0.0157421 |     0.0143569 | 0.00376296 |               0.0157421 |              0.0143569 |        0.00376296 |           1 | True      |         2 |
|   5 | KNeighborsUnif      |      0.201 |  0.236546 | accuracy    |      0.0157351 |     0.0151029 |    5.04704 |               0.0157351 |              0.0151029 |           5.04704 |           1 | True      |         1 |

### Vision
![[Pasted image 20250930184959.png]]
#### Results
![[Pasted image 20250930185030.png]]
## New things

### Neovim
![[Pasted image 20250930175549.png]]
![[Pasted image 20250930175621.png]]


### [llms.txt](https://llmstxt.org)
<im src = "/Users/smukherjee/Documents/Resources/Knowledge-base/content/images/Pasted image 20250930180210.png"></im>
