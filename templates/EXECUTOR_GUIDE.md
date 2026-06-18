# Executor Guide

This guide is for the model that executes the frozen plan after the frontier window has closed. Read it fully before starting.

## Read first, in this order
1. The frozen authorities listed in 20_SESSION_HANDOFF.md.
2. NORMALIZED_BACKLOG.md for the task order.
3. The oracle tests for the feature you are about to touch.

## How to work
- Take only the next 1 to 3 tasks. Do not work ahead.
- Implement against the oracle. A task is correct when its acceptance tests pass.
- Keep the diff minimal. Do not refactor outside the task scope. Do not rename unnecessarily.
- Add tests. Do not suppress or hide failing tests.

## Definition of done
A task is done only when its acceptance criteria are covered, its validation has been run, the proof is recorded in the proof matrix, no unrelated changes were introduced, and the execution log is updated.

## Stop conditions
Stop and escalate to a human or reserve for a frontier window when:
- A task is marked do not attempt, or blocked.
- The oracle is missing for a hard task.
- You would need to make a decision that is expensive to reverse and is not already covered by an ADR.
- Tests fail in a way you cannot resolve with a minimal change.
- A change would touch a data or security boundary.

## Never
- Never mark a task done without proof.
- Never invent a completed feature.
- Never overwrite a frozen authority. Propose a new decision record instead.
