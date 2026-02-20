---
name: bigquery-data-strategist 
description: Expert in petabyte-scale data warehousing, SQL optimization, and GCP data ecosystems. Use when designing schemas, optimizing query costs, or building analytical pipelines.
---

## Description

This skill represents a specialist in Google Cloud's serverless data warehouse. It prioritizes "Cloud-Native SQL," moving beyond traditional relational database thinking to master denormalization, slot utilization, and cost-effective analytical processing.

## When to use this skill
Data Warehousing: Use when designing large-scale analytical schemas (Star/Snowflake/Flat).

Cost Optimization: Helpful for auditing expensive queries and implementing partitioning/clustering strategies.

Data Modeling: Use when working with complex, nested data structures (JSON, Arrays, Structs).

ELT Pipelines: Helpful for transforming raw data within the warehouse using BigQuery's specialized SQL syntax.

## How to use it

1. Schema & Performance Engineering
Partitioning: Always implement time-unit or integer-range partitioning to limit data scanned per query.

Clustering: Use clustering on high-cardinality columns (like IDs or Names) to improve sort performance and further reduce costs.

Denormalization: Prefer NESTED and REPEATED fields (Structs and Arrays) over complex many-to-many joins to leverage BigQuery’s columnar storage.

Search Optimization: Utilize BigQuery Search Indexes for efficient lookups in unstructured text or log data.

2. Advanced SQL Patterns
Analytical Functions: Use WINDOW functions (RANK, LEAD, LAG) for complex time-series and ranking analysis.

User-Defined Functions (UDFs): Write JavaScript or SQL UDFs for reusable, complex business logic that standard SQL cannot handle.

DML Best Practices: Use MERGE statements for upserts and avoid frequent single-row INSERT statements to stay within quota limits.

BigQuery ML: Implement machine learning models (Linear Regression, K-means) directly in SQL for rapid prototyping.

3. Cost & Resource Management
Dry Run Implementation: Always check the "Bytes Processed" estimate before executing a query.

Slot Management: Monitor slot utilization to ensure high-priority jobs aren't being throttled.

Materialized Views: Use Materialized Views for frequently aggregated data to save on repetitive processing costs.

4. Integration & Ecosystem
External Tables: Query data directly in GCS (Google Cloud Storage) or Bigtable using Federated Queries.

BigQuery Data Transfer: Automate data ingestion from SaaS platforms (Google Ads, YouTube, Salesforce).

Analytics Hub: Securely share datasets across organizational boundaries without moving data.