# Autonomy Test

The project is autonomous when a cheaper or local model, given only the frozen files and the codebase, can finish the backlog and prove each task done.

- [ ] Every remaining task has acceptance criteria a weak model can read.
- [ ] Every high risk task has an executable test or a precise manual check.
- [ ] The oracle tests exist and run.
- [ ] The executor guide states read order, definition of done, and stop conditions.
- [ ] Frozen authorities are listed in the handoff file.
- [ ] No remaining task secretly needs frontier level reasoning. Such tasks are marked reserved.

Result: pass means the frontier window can close safely. Fail means name the missing artifact and produce it before closing the window.
