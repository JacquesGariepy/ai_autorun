# Task Source Discovery

The goal is to find every task that exists anywhere in the project, so nothing is forgotten. Tasks hide in many places, not only in an obvious CSV. Scan all of these, then turn each finding into a candidate task in the backlog.

## Where tasks hide

### Structured task files
- features.csv and any other CSV listing features, stories, or tasks.
- Spreadsheets, JSON, or YAML backlogs.
- Planning documents: ROADMAP, BACKLOG, TODO, PLAN, TASKS, ISSUES, files in any case or extension.
- Issue exports or tracker dumps committed to the repo.

### Markers in source code
Search the whole codebase, including comments and strings, for:
- TODO, FIXME, HACK, WIP, XXX, BUG, NOTE, OPTIMIZE, REFACTOR, REVIEW, DEPRECATED.
- NotImplemented, NotImplementedException, raise NotImplementedError.
- throw new Error("not implemented"), pass with a comment, empty method bodies.
- Commented out blocks that look like unfinished features.

### Behavior that implies work
- Failing tests, skipped tests, tests marked only or focused.
- Build errors and warnings.
- Runtime errors and unhandled exceptions on the main path.
- UI elements without handlers, endpoints without implementation, commands registered but never called.
- Configuration defined but never read, models configured but never invoked, prompts defined but never tested.

### Documentation promises
- README and docs claims not supported by code.
- Phrases such as coming soon, planned, future work, not yet implemented, beta, experimental.
- Changelog entries that promise things the code does not do.

### Data and contract gaps
- Schemas without migrations, migrations without rollback.
- API contracts the UI does not match.
- Validation missing where untrusted input enters.

## How to extract

For each finding, record: source, file, line if applicable, the marker or signal, a one line task statement, an inferred priority, and whether it is provable.

## Outputs

- TASK_SOURCE_INVENTORY.md: one row per source, with a count and notes.
- DISCOVERED_TASKS_FROM_CODE.md: one row per code marker found.
- CSV_TASK_ANALYSIS.md: every row of every CSV, normalized, with status and gaps.

## Rules

- Do not drop a task because it looks small or unclear. Mark unclear tasks blocked with the reason, do not delete them.
- Do not invent tasks that have no source. Every task traces to evidence.
- Deduplicate later, during triage, not during discovery. Discovery captures everything first.
