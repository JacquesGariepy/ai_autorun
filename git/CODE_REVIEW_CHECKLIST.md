# Code Review Checklist

The reviewer role applies this before a pull request is ready.

## Correctness
- [ ] Acceptance criteria met, proven by tests or a clear manual check.
- [ ] No fake, mocked, or hardcoded behavior presented as real.
- [ ] Edge cases handled.

## Scope and quality
- [ ] Diff limited to the batch. No unrelated refactor or rename.
- [ ] No needless duplication, no dead code added.
- [ ] Readable, consistent with project conventions.

## Safety
- [ ] No secrets, keys, or tokens.
- [ ] Untrusted input validated where it enters.
- [ ] No new sensitive data sent to a remote model.

## Tests and reliability
- [ ] Meaningful tests added for the change.
- [ ] No silent failure paths introduced.

## History
- [ ] Atomic conventional commits.
- [ ] Task ids and proof referenced.
