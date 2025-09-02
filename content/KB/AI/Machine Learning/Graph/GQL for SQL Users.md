---
title: GQL for SQL Users
toc: true
tags:
  - conference
  - sql
date modified: Monday 11th November 2024, Mon
date created: Monday 11th November 2024, Mon
---

# GQL for SQL Users
```toc
```
- by [Keith Hare](https://neo4j.com/blog/bringing-approved-gql-project-into-focus/?ref=blog)
- sql : relational tables
- gql : property graphs

## Why [[Complete AI Pipeline#Data Standards|Standards]]
- less chaos
- competition on performance and not on language
- consistent interfaces: across db vendors
	- not always same syntax but better for db users to migrate what they know
- better knowledge transfer
- RDO?

## Property [[Graphs#Graphs|Graphs]]
- nodes and relationships -> synthetic identity
- query without knowing relationship
- the "problem" -> not recognising the problem is a graph
- node/edge
- case sensitive names
- linear composition
- creating data
	- schema-less
		- just insert data
		- no restrictions on content
	- graph schema
		- create graph type
		- graphs using type
- non procedural languages
- CRUD - create read update and delete
- In sql, constrains are evaluated when the data is inserted, but not automatically encoded in query
	- aka must include the relationship in the query : cartesian product (probably annoying)
- ?? performance vs sql for a large graph esp add and insert for graph traversal?
	- the speaker isnt focused on this for now
	- "thats why we have phd students" xD
- ?? backup and restore graph connections
	- commit and rollback
- nodes have () (cuz when you draw it on a whiteboard you draw a circle)
- edges are by -> and []

## Schema-less
- schema by inserting data so no restriction
- intitial version of GQL - no constraints
	- fixed by having a closed graph

## Graph Pattern Matching
- language for querying graphs
- quantified path patterns
- cheapest path
- multiset alternation
- types
	- simple
	- filtering
	- union
	- alternation
	- aggregation

## SQL/PGQ - Property Graphs in Sql
- sql + all the above
- does not support schema flexible graphs
- duckdb
- postgre sql