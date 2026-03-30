# Report Format

Ensure report contains these sections:
1. Context: ticket, branch, project/release, PRD path.
2. Generated test files.
3. Summary metrics: total, passed, failed, skipped, errors, duration.
4. Failure details for failed/error cases.
5. Artifact pointers (JUnit XML and report path).
6. Video artifacts:
   - video output root (for example `artifacts/playwright-results`)
   - video inventory path (for example `artifacts/playwright-videos.txt`)
   - count of `.webm` files
   - list of `.webm` paths or a pointer to the inventory file

Prefer concise Markdown so users can paste into Jira comments.
