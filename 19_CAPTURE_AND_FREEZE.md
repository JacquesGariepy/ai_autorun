# Capture and Freeze

The purpose of this file is to make the project autonomous after a frontier window closes. A burst that lives only in a chat history is lost. A burst that has been frozen into files keeps working for you while the strong model is gone.

## The principle

A frontier model is a temporary resource. Its output is a permanent asset only if you save it as files with clear status. Treat every strong answer as something to be captured, named, and frozen, not as a conversation.

## What to capture, and where

| Artifact | Source wave | Save to | Why it is durable |
|---|---|---|---|
| Capability sheet | Wave 0 | model-management/decision-records/ | Tells future sessions what the model could do |
| Product reality report | Wave 1 | reports/ | Ground truth that does not change with the model |
| Architecture decision records | Wave 2 | adr/ | Decisions stay valid after the model leaves |
| Solution plus oracle tests | Wave 3 | reports/ and the test suite | The oracle lets weak models self verify |
| Frozen backlog and executor guide | Wave 4 | package root or reports/ | The autonomous execution plan |
| Omissions and gaps | Wave 5 | reports/ | The anti forgetting record |

## The freeze procedure

1. After each wave, save the output as a file immediately. Do not wait until the end of the session.
2. Stamp each file with: source model and version, date, and a status of draft, reviewed, or frozen.
3. Mark a file frozen only when you have read it and accept it as the authority for that topic.
4. Once frozen, the file governs. A later model that disagrees must justify the change through a new decision record, not a silent overwrite.

## The autonomy test

Your project is autonomous when this is true: if the frontier model never returns, a cheaper or local model, given only the frozen files and the codebase, can finish the backlog and prove each task done.

Check it directly:
- [ ] Every remaining task has acceptance criteria a weak model can read.
- [ ] Every high risk task has an executable test or a precise manual check.
- [ ] The executor guide states read order, definition of done, and stop conditions.
- [ ] The oracle tests exist and run.
- [ ] No remaining task secretly depends on frontier level reasoning. Tasks that do are marked blocked and reserved for the next window.

If all boxes are checked, you can close the window safely.

## The oracle is the keystone

The single most important captured artifact is the oracle: the authoritative specification plus executable acceptance tests for the hard parts. With a strong oracle, a weak model can iterate to a correct result on its own, because it has a way to know when it is right. Without it, every task silently needs the strong model again. Spend frontier time on the oracle before anything optional.
