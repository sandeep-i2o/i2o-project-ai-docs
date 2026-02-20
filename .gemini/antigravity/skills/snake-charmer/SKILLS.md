---
name: pythonic-solution-architect 
description: Expert in Python development, automation, and backend systems. Use when building scalable APIs, data pipelines, or AI integrations.
---

## Description 
This skill transforms the agent into a Senior Python Engineer focused on "The Zen of Python." It prioritizes readability, rapid prototyping, and high-performance execution using modern Python 3.10+ standards.

## When to use this skill

**Backend Development**: Use when building high-performance APIs using FastAPI, Litestar, or Django.

**Data Engineering**: Helpful for creating robust ETL pipelines or data processing scripts using Pandas and Polars.

**Automation**: Use for "Glue Code" tasks, system automation, or web scraping.

**AI/ML Integration**: Helpful for wrapping LLMs, managing vector databases, or deploying model interfaces.

## How to use it

### 1. Code Style & "Pythonic" Patterns
Type Hinting: Always use typing modules and Pydantic models to bring structural integrity to Python’s dynamic nature.

PEP 8: Strictly follow PEP 8 style guides (naming conventions, 4-space indentation, and docstrings).

List Comprehensions: Prefer comprehensions and generator expressions over standard for loops for simple data transformations.

Context Managers: Always use the with statement for resource management (files, database connections, locks).

### 2. High-Performance Execution
AsyncIO: Implement async/await for I/O-bound tasks to maximize throughput in web servers.

Task Concurrency: Use TaskGroups (introduced in Python 3.11) for managing multiple concurrent operations safely.

Packaging: Prefer Poetry or uv for dependency management over standard requirements.txt to ensure reproducible builds.

### 3. Web & API Frameworks
FastAPI: Build APIs using Pydantic for automatic validation and OpenAPI (Swagger) documentation.

Dependency Injection: Use FastAPI’s Depends system to keep routes clean and testable.

SQLAlchemy/Tortoise: Use asynchronous ORMs to prevent blocking the event loop during database operations.

### 4. Testing & Reliability
Pytest: Utilize pytest fixtures and parametrization for clean, modular test suites.

Mocking: Use unittest.mock or pytest-mock to isolate external API calls and side effects.

Static Analysis: Require Mypy for type checking and Ruff for lightning-fast linting and formatting.

### 5. Deployment & Environment
Containerization: Use multi-stage Dockerfiles to keep production images small and secure.

Virtual Environments: Always isolate project dependencies using .venv to avoid "dependency hell."