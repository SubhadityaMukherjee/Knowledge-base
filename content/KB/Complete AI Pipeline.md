---
toc: true
title: Complete AI Pipeline
tags:
  - deeplearning
date modified: Tuesday 27th February 2024, Tue
date created: Tuesday 27th February 2024, Tue
---

# Complete AI Pipeline


## Planning

- Data Availability
- Applicability
- Legal Constraints
- Robustness
- Scalability
- Explainability
- Availability of Resources

## Data Collection

### Data Standards

- Healthcare
	- [DICOM](DICOM.md)
	- [HL7](HL7.md)
	- [FHIR](FHIR.md)

### Data Formats

- Healthcare    
	- Next generation sequencing
		- Raw sequencing data
			- FASTQ
				- BioPython
		- Aligned Reads
			- SAM/BAM
				- pysam
		- Variant Calls
			- VCF
				- pyVCF
	- Mass spectrometry
		- mzML/mzXML
			- pyteomics
		- MGF
			- pyOpenMS
	- MRI
		- [DICOM](DICOM.md)
	- CT
		- [DICOM](DICOM.md)
	- Ultrasound
		- [DICOM](DICOM.md)
		- SCU
		- ACR-NEMA
	- Functional (pre)clinical studies
	- E-health and m-health technology
	- Wearable Device monitoring
	- Unstructured vocal information
	- Unstructured textual information

## Data Processing and Transformation

### AWS Services

- Glue
	- Fully managed ETL (Extract, Transform, Load) service for preparing and loading data.

## Data Annotation

## Data Integration

## Data Storage

### AWS Services

- S3
	- Object storage service, suitable for storing and retrieving any amount of data at any time.
    
- Dynamo DB
	- Modern
	- High activity
	- High Velocity data (sensors and stuff)
	- Structured/unstructured
	- multi data, multi cloud
	- NoSQL database service designed for high-performance applications that require seamless scalability.
    
- RDS
	- Tables
	- low velocity/activity
	- Harder to modify
	- Relational Database Service, supports multiple database engines, managing backups, and software patching.

- HealthImaging

- HealthLake
	- A HIPAA-eligible service for storing, transforming, and analyzing healthcare data.

- Lake Formation
	- Simplifies the process of setting up, securing, and managing a data lake.

## Data Analysis and Querying

### AWS Services
- Redshift
	- Fully managed data warehouse service, designed for high-performance analysis using SQL queries.
    

## Streaming Data Processing

### AWS Services
- Kinesis
	- Streaming data service that enables real-time processing of large data streams.
    

## Model Development

### Model Architectures

### Model Metrics

## CI/CD

### Tracking Experiments, Metadata, Features, Code Changes
- MLFlow

### State of the Models
- Staging
- Production
- Archived

## Model Evaluation

## Machine Learning

## AWS Services

- SageMaker
	- Machine learning service that helps build, train, and deploy machine learning models at scale.

## Model Deployment

## Real Time Prediction

## Monitoring and Maintenance

## Interpretability and Explainability

## Regulatory Compliance

- HIPAA

## Collaboration
