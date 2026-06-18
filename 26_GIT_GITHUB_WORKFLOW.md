# Git and GitHub Workflow

The agent treats version control as a first class part of the work. Every change is traceable, reviewed, tested, and reversible. No change lands without proof on a branch and a clean history.

## Branching strategy

- main is always releasable. Never commit directly to main. Never force push to main or to any shared branch.
- One branch per batch of 1 to 3 tasks. Name it by type and scope: feat/<scope>, fix/<scope>, refactor/<scope>, test/<scope>, docs/<scope>, chore/<scope>, perf/<scope>, security/<scope>.
- Exploration branches for forks, named explore/<topic>-<option>, one per option, per 29_EXPLORATION_AND_SPIKES.md. Rejected options are tagged experiment/<topic>/<option> and preserved, never lost, so they can be revisited.
- Keep branches short lived. Open, implement, prove, integrate, delete.
- Independent batches may run on parallel branches. Dependent batches are serialized by dependency order.

## Commit convention

Use Conventional Commits. Format: type(scope): summary, then a body, then a footer.
- Types: feat, fix, refactor, test, docs, chore, perf, security, build, ci.
- Summary in the imperative, under about 72 characters.
- Body explains why, not just what. Reference the task id and the proof.
- Footer links issues and notes breaking changes with BREAKING CHANGE.
- Commits are atomic: one logical change each. Do not mix a refactor with a feature.
- Never commit secrets, keys, tokens, large binaries, or generated artifacts. Maintain .gitignore.

## Pull requests

- One pull request per batch branch into main.
- The pull request body uses git/PULL_REQUEST_TEMPLATE.md and includes: tasks covered, summary of changes, validation commands and their results, the proof matrix rows, risks, and rollback notes.
- The pull request must pass the review checklist in git/CODE_REVIEW_CHECKLIST.md before it can be marked ready.
- Link the issues or task ids the pull request closes.

## Merge policy

- A pull request may merge only when: required CI checks pass, the review checklist passes, the quality gates pass, and no unresolved blocking comment remains.
- Prefer squash merge for a clean history, unless the project standard says otherwise. Keep the conventional commit summary on the squash.
- Delete the merged batch branch. For exploration, merge the winner and tag each rejected option experiment/<topic>/<option> before closing its draft pull request, so its work stays recoverable.

## CI and protection

- Required checks on main: build, tests, lint, and the security scan, per git/ci.example.yml adapted to the project stack.
- Treat main as protected: no direct pushes, checks required, review required.
- A red pipeline blocks merge. Do not bypass it.

## Releases and versioning

- Use semantic versioning. feat is a minor bump, fix is a patch, BREAKING CHANGE is a major bump.
- Tag releases. Maintain a changelog generated from conventional commits.
- Every release meets 13_RELEASE_READINESS.md and has a rollback path.

## Safety boundaries (pause and ask, even under standing approval)

- Pushing to a remote, opening or merging a pull request, or tagging a release, when remote credentials or repository permissions are not clearly granted.
- Any operation that would rewrite shared history, delete branches other than the current batch branch, or touch main directly.
- Committing anything that looks like a secret. Stop and flag it.

Local work, branch creation, local commits, and preparing pull request content are always allowed. Remote actions follow the project's granted permissions.
