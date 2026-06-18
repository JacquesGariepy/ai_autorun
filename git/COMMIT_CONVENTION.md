# Commit Convention

Conventional Commits.

```
type(scope): imperative summary under ~72 chars

Why this change. What it does. How it was validated.
Task: <task id>. Proof: <command or test reference>.

Closes #<issue>. BREAKING CHANGE: <describe> if applicable.
```

Types: feat, fix, refactor, test, docs, chore, perf, security, build, ci.

Rules:
- One logical change per commit. Atomic.
- No secrets, keys, tokens, or generated artifacts.
- Reference the task id and the proof in the body.
