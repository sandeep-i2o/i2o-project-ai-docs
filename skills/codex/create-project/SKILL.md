---
name: create-project
description: Create the standard i2o project documentation folder structure under `projects/<project_name>/<release>/docs` with required `design`, `requirements`, and `tests` subfolders. Use when users ask to initialize project documentation directories in `i2o-project-ai-docs` using `create_project --project_name ... [--release ...]`.
---

# Create Project

Create the project release documentation scaffold quickly and consistently.

## Inputs

Collect:
- `project_name` (required)
- `release` (optional; default `latest`)

## Workflow

1. Confirm current directory is the root of `sandeep-i2o/i2o-project-ai-docs`.
2. Run the bundled script:
   - `./scripts/create_project --project_name "<project_name>" --release "<release>"`
3. If `release` is not provided, omit it and let the script use `latest`.
4. Return the created directory paths.

## Command Examples

Use explicit release:

```bash
./scripts/create_project --project_name "Project Name" --release release_7.5
```

Use default release:

```bash
./scripts/create_project --project_name "Project Name"
```

## Output Contract

Ensure:
1. Working directory is the root of `https://github.com/sandeep-i2o/i2o-project-ai-docs`.
2. Create `projects/<project_name>/<release>/docs`.
3. Create these subfolders inside `docs`: `design`, `requirements`, `tests`.
