---
title: Accessibility Checker for Blind Visitors of Websites
toc: true
tags:
  - alfie
date modified: Friday 2nd May 2025, Fri
date created: Friday 2nd May 2025, Fri
---

# Accessibility Checker for Blind Visitors of Websites
```toc
```
- UAB use case
- Interacts with automl using a screenreader + Speech to text
## Input
- website url or uploads html/css files
## Requirements
- missing alternative text for images
- lack of proper semantic HTML structure
- insufficient colour contrast
- absence of ARIA roles.
- Ensure that the website is navigable and understandable using popular screen readers.
- compliance with WCAG 2.1 (Web Content Accessibility Guidelines) criteria relevant for blind users.
- Simulate screen reader behavior
## Output
- Provide specific recommendations to fix detected issues.
- Dashboard with an accessibility score, highlights etc
- List of issues by severity
- WCAG 2.1 compliance
## Clarifications
- Do we need the automl system to generate a model or just use the automl system to do this. Eg: we would run an llm over the users code and then have results. 
	- There is no normal "model" that can do this reliably.
	- We need two kinds of models essentially - one thats an LLM like chatgpt that can do many things and another that does a model search + refinement over existing architectures to find the best model. 
- How would user intera ction using a screen reader look like? For the output that is

## Meeting Notes
- 2025-05-09
	- UAB Barcelona
	- People
		- Kate - communication
		- Chiara - anthropologist, vulnerable groups
		- Hari S - Philosophy of science 
	- Difficulties
		- voice interaction
		- cannot type
	- Person who will use automl system - designer user
	- Ethical models and suggestions