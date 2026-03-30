---
name: deploy-to-dev
description: Deploy the current git repository branch to a Jenkins dev job and wait for completion. Use when asked to deploy to dev, trigger Jenkins for the current branch, or run a branch-based CI/CD dev deployment with one-time Jenkins credential capture in `.jenkins/config.json`.
---

# Deploy to Dev

## Goal
Trigger Jenkins for the current git branch, wait until the build finishes, and return a concise success/failure message.

## Command Interface
Use this skill for requests like:

- "Deploy this repo to dev"
- "Run Jenkins dev deploy for current branch"
- "Trigger dev instance deployment"

Run:

```bash
./scripts/deploy_to_dev.sh
```

Optional non-interactive arguments:

```bash
./scripts/deploy_to_dev.sh \
  --jenkins-url "https://jenkins.example.com/job/my-job" \
  --jenkins-user "my-user" \
  --jenkins-token "my-token"
```

## Inputs and Persistence
Collect these values only if missing, then persist to `<repo>/.jenkins/config.json`:

- `JENKINS_USER`
- `JENKINS_URL` (job URL, for example `https://jenkins.example.com/job/my-job`)
- `JENKINS_API_TOKEN`

Rules:
- If `.jenkins/config.json` already contains values, reuse them without asking again.
- Use current git branch for `JENKINS_BRANCH` via `git rev-parse --abbrev-ref HEAD`.

## Required Process
Follow this sequence exactly.

1. Extract `JOB_NAME` from `JENKINS_URL`.
2. Initialize variables for Jenkins trigger:
   - `JENKINS_URL` = base URL
   - `JOB_NAME` = extracted job name
   - `USER` = `JENKINS_USER`
   - `TOKEN` = `JENKINS_API_TOKEN`
3. Trigger build and wait until completion.
4. If success: print `Build is successful`.
5. If failure: print relevant error message only; do not print full stacktrace.

## Build Trigger and Monitoring
The bundled script implements the required curl/jq queue polling flow and adds safe defaults:

- Attempts `buildWithParameters` first with current branch (`JENKINS_BRANCH` and `BRANCH` params)
- Falls back to `build` if parameterized trigger is unavailable
- Polls Jenkins queue until executable build URL appears
- Polls build status until `building=false`
- Reads final result from build API

## Failure Output Policy
On build failure:

- Report Jenkins result and concise relevant error lines
- Filter noisy stack frames (for example Java `at ...` frames)
- Avoid dumping full console stacktraces

## Dependencies
Ensure these commands are available before running:

- `curl`
- `jq`
- `git`
