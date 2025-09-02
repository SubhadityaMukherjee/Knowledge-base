---
title: ALFIE
toc: true
tags: 
date modified: Wednesday 16th April 2025, Wed
date created: Wednesday 16th April 2025, Wed
---

# ALFIE
```toc
```
## Requirements for TUe
## 1. Lead The Design of AutoML Platform Architecture (T4.2)

- Perform mapping of user requirements to system functionalities.
    - Reference: User stories from T2.3/T4.1, like: "A healthcare expert wants to classify patient risk without knowing ML."
        
- Define functional and non-functional modules (hardware/software diversity, interoperability).
    
    - Example: A scalable ML module that can run both on HPC clusters and edge devices.
        
- Design the orchestration layer integrating WP3 and WP4 components.
    
    - Reference: Use a microservices architecture with APIs linking understanding layer (T3.2), AutoML (T3.4), and XAI (T3.6).

## 2. Develop AI Tools for Multilingual Interaction & Auto-Generation of AI Models

- Support multilingual LLMs (translate inputs, prompts, outputs).
    
    - Example: Using multilingual BERT or BLOOMZ for understanding user queries in various languages.
        
- Implement tools to auto-generate models from user descriptions.
    
    - Reference: Combine OpenML metadata with GAMA pipelines to create an AutoML pipeline from: "I want a fair and green classifier for tabular health data."

## 3. Ensure Green, Fair, and Ethical AutoML

- Integrate Green AI practices (energy-efficient pipelines, runtime monitoring).
    
    - Example: Avoid brute-force grid searches; implement meta-learning based model selection.
        
- Include Fairness-aware modeling (bias detection/mitigation).
    
    - Example: Add fairness metrics like demographic parity into evaluation metrics.
        
- Address ethical considerations: transparency, privacy, EU AI Act compliance.
    
    - Reference: Implement opt-in explanations (XAI) and data privacy constraints at model training level (e.g., differential privacy).

## 4. Enable Declarative Interfaces for Domain Experts

- Design interfaces to let users specify _what_, not _how_.
    
    - Example: "I want a model that predicts churn with high recall and uses no sensitive features."
        
    - Backend translates this to: model constraints, search space restrictions, metrics, etc.

## 5. Custom Technical Solutions for Diverse Use Cases

- Find Pareto-optimal models (accuracy vs fairness vs energy).
    
    - Example: Use multi-objective optimization in AutoML pipeline selection.
        
- Solve new domain-specific challenges.
    
    - Reference: Healthcare ML with missing data + fairness constraints.

## 6. Integrate TU/e Technologies (OpenML, GAMA)

- Connect OpenML datasets and results to the AutoML platform.
    
    - Example: Pull datasets, meta-features and past performance data from OpenML for warm-starting AutoML.
        
- Use GAMA to generate and evaluate pipelines in real time.
    
    - Reference: Customize GAMA to use constraints (green, fair, multilingual).

## 7. Connect XAI to AutoML (T3.6 Integration)

- Ensure AutoML outputs include explanations (XAI).
    
    - Example: Integrate SHAP, LIME, or GNNExplainer tools depending on model type.
        
    - Output: "Why did the model predict high risk for this patient?"

## 8. Recruit Stakeholders for Co-Design

- Involve academic + industrial partners in user-centered design (UCD).
    
    - Reference: Workshops, surveys, feedback loops from T4.1.

## 9. Contribute To EU Policy Recommendations

- Ensure all tools align with AI Act and GDPR.
    
    - Example: AutoML output includes risk assessment and audit trail logs.
        
- Draft contributions to EU policy on trustworthy, sustainable AI.
    
    - Reference: Whitepapers co-authored with policy partners.

## 10. Connect Data Warehouse with AutoML (Set Rules)

- Define access, privacy, and structure rules for feeding data into the platform.
    
    - Example: Only anonymized data is accepted; data catalogued with quality and fairness scores.

### 🗂 Deliverables & Timeline References

| Milestone / Deliverable | Deadline                                           | What to Deliver                             |
| ----------------------- | -------------------------------------------------- | ------------------------------------------- |
| M3–M28 (T4.2 Task Span) | Ongoing                                            | System architecture, orchestration design   |
| D4.1, D4.2              | M12, M28                                           | Docs on architecture + functional prototype |
| M18, M33                | Tools for multilingual + auto-generation of models |                                             |
|                         |                                                    |                                             |
