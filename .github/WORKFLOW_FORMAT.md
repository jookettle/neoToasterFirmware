# CI Formatting Workflow

This repository's CI now applies clang-format automatically but does not push changes directly to the default branch.
Instead, the CI will create a pull request with formatting changes so maintainers can review before merging.

What to expect
- On pushes or PRs the `lint` job runs clang-format.
- If clang-format makes changes, the workflow will create a branch named `auto/clang-format-<sha>` and open a PR with those changes.
- The PR will be labeled `auto-format`.

Why this approach
- Avoids CI directly committing to main/master, which can be blocked or cause unexpected commits.
- Keeps CI with minimal `contents` permission while allowing PR creation via `pull-requests` permission.

Testing the workflow (recommended)
1. Create a test branch and make a small formatting-violating change (e.g. add an extra space or misaligned brace).
2. Push the branch to the repository or a fork.
3. Observe the `lint` job on GitHub Actions — when formatting changes are detected the workflow should open a PR named `chore: apply clang-format`.

Notes about tokens and permissions
- The workflow uses `GITHUB_TOKEN` for PR creation; this token is provided by GitHub and typically works for repository workflows.
- If your organization or repo policy restricts `GITHUB_TOKEN` for PR creation from forks, test in a non-fork branch or configure a Personal Access Token (PAT) in repository secrets and update the workflow to use that secret.

Rollback
- If you need to revert the workflow change, restore `.github/workflows/ci.yml` from `.github/workflows/ci.yml.bak` or revert the commit that modified it.

Contact
- If the PR generation creates many noisy PRs, we can add rate-limiting checks or skip PR creation for small/whitelisted changes.