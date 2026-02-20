---
name: java-17-springboot-expert 
description: Provides expert-level guidance for building, refactoring, and optimizing Spring Boot applications using Java 17+ features.
---

## Description

This skill enables the agent to act as a Senior Backend Engineer specialized in the modern Java ecosystem. It focuses on leveraging Java 17 language enhancements (Records, Sealed Classes, Pattern Matching) alongside Spring Boot 3.x standards to create scalable, maintainable, and high-performance microservices.

## When to use this skill
Modernizing Legacy Code: Use this when refactoring Java 8 or 11 codebases to Java 17/21.

Bootstrapping Services: Helpful for setting up new Spring Boot 3.x projects with "Golden Path" configurations.

Domain Modeling: Use this to design robust domain models using Records and Sealed hierarchies.

Performance Tuning: Helpful for optimizing JVM settings, Garbage Collection (G1/ZGC), and writing non-blocking code.

## How to use it

1. Language Conventions (Java 17+)
Data Carriers: Always prefer records over standard classes for DTOs, request/response objects, and internal data holders.

Pattern Matching: Use instanceof pattern matching and switch expressions to reduce boilerplate and casting.

Immutability: Default to final variables and unmodifiable collections to ensure thread safety.

Text Blocks: Use text blocks (""") for SQL queries, JSON templates, or HTML to maintain readability.

2. Spring Boot 3.x Patterns
Dependency Injection: Use constructor-based injection exclusively (no @Autowired on fields).

Global Exception Handling: Implement @ControllerAdvice with ProblemDetail (the RFC 7807 standard supported in Spring 6).

Validation: Use jakarta.validation annotations on Records to enforce data integrity at the entry point.

Observability: Always include Spring Boot Actuator and Micrometer for production readiness.

3. Database & Persistence
Soft Deletes: Implement logic-based deletions rather than hard SQL deletes where audit trails are required.

Projections: Use Spring Data JPA interface or record-based projections for read-only operations to save memory.

Migrations: Require Flyway or Liquibase scripts for every schema change—no ddl-auto=update in production.

4. Testing Standards
Mocking: Use Mockito for unit tests but prefer Testcontainers for integration tests involving databases or message brokers.

Assertions: Use AssertJ for fluent, readable assertions (e.g., assertThat(result).hasSize(1)).