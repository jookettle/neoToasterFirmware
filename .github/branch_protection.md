# Branch Protection Guidance

This repository enforces safer branch management via workflows and recommendations.

Recommended branch protection settings for `main` / `master`:

- Require pull request reviews before merging (1 or 2 reviewers)
- Require status checks to pass before merging (include `Lint Code`, builds)
- Include administrators: optional, but consider requiring for consistency
- Restrict who can push to matching branches (optional)
- Enforce linear history (optional)

How to add protection:
1. Go to the repository Settings → Branches → Branch protection rules.
2. Add a rule for `main` (and `master`) with the options above.
3. Add trusted users or teams if `Restrict who can push` is enabled.

Automated checks
- `branch-protection-check.yml` runs weekly and fails if `main`/`master` are not protected.
- `pr-cleanup.yml` will not delete branches that are reported protected via the API.

If you want, I can: 
- Open a PR that documents these policies and automates checks (already added `branch-protection-check.yml`).
- Help configure branch protection via the GitHub UI or guide an admin through the API.
