# Branching Strategy

GitHub flow, trunk based, short lived branches.

- main: always releasable, protected, no direct commits.
- batch branches: one per 1 to 3 task batch, named feat|fix|refactor|test|docs|chore|perf|security/<scope>.
- lifecycle: branch from main, implement, prove, open pull request, pass checks and review, squash merge, delete branch.
- parallelism: independent batches on parallel branches, dependent batches serialized.
- never: direct commit to main, force push to shared branches, long lived divergent branches.
