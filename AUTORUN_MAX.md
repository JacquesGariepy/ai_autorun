# Autorun Max

This file makes the package self driving in maximization mode. Point an agent at this file and it takes a project, existing or new, discovers every task that exists anywhere, audits the real state, researches comparable projects online, builds the maximal plan, then implements in small proven batches in a loop until the project reaches its practical maximum.

## How paths work

Every file named in this document lives in the same folder as this file. Resolve each name against this file's own folder, and create any output folder such as reports, adr, batch-reports, or model-management inside that same folder if it does not exist.

## Honest framing

The goal is to push the project to its maximum credible quality and feature completeness, with proof at every step. Quality is bounded by two things: what can be proven, and what the agent and its tools can actually do. This orchestrator maximizes within those bounds. It does not fake progress to look impressive, and it does not implement a giant unauditable change. It compounds many small proven improvements, which is how real quality is reached.

For this to run automatically, the agent must have read access to the repository, the ability to write files, and permission to proceed without confirmation between steps. Web access is used if available and skipped cleanly if not.

## Phase setup: oversight and journaling

Read 30_OVERSIGHT_AND_JOURNALING.md and run it first. Ask me once whether I want human in the loop and at what level, the type and verbosity of information, and confirm full journaling. If my launch granted standing approval to proceed through every phase and batch, set oversight to L0 fully autonomous: do not pause at phase boundaries, do not stop after planning, run end to end. Otherwise, if I do not answer shortly, apply the safe defaults (L1 checkpoints, decisions and risks, summary verbosity, journaling on) and proceed. Record the chosen settings in reports/ENV_PROFILE.md and open JOURNAL.md. From here on, journal everything you undertake, including explorations, tool choices, errors, and recoveries. This is the only setup interaction; do not ask me for configuration again.

## Phase 0: Preflight and self configuration

Read 28_PREFLIGHT_AUTOCONFIG.md and run it first. Detect the operating system, the stack, the build, test, and lint commands, the Git host, the remote permission level, CI presence, web access, available tools, model tiers, data sensitivity, and whether the project is new or existing. Choose safe defaults for anything not detectable, record every assumption in reports/ENV_PROFILE.md, and proceed. Do not ask me for configuration. The only reasons to pause are the real safety boundaries listed below.

## Phase 1: Discover every task source

Read 23_TASK_SOURCE_DISCOVERY.md and apply it fully. Find tasks everywhere they hide, not only in the obvious CSV:
- Every CSV, including features.csv and any backlog or task spreadsheet.
- Markers in code: TODO, FIXME, HACK, WIP, XXX, BUG, NOTE, NotImplemented, and equivalents.
- Issue files, backlog files, planning documents, and any file whose name or content lists work to do.
- Documentation promises, including "coming soon" and "planned".
- Failing tests, skipped tests, build errors, runtime errors.
- Commented out code and disconnected features.

Output: templates TASK_SOURCE_INVENTORY.md, DISCOVERED_TASKS_FROM_CODE.md, and CSV_TASK_ANALYSIS.md, saved under reports/. Nothing is dropped. Every discovered item becomes a candidate task.

## Phase 2: Audit the real state

Run these audits and save each report under reports/:
- Product reality, from 16_FRONTIER_BURST_PROTOCOL.md wave 1, into PRODUCT_REALITY_REPORT.md and ARCHITECTURE_MAP.md.
- Unfinished work, from 06_UNFINISHED_WORK_AUDIT.md.
- Hardcoding, from 07_HARDCODING_AUDIT.md.
- Feature completeness, into FEATURE_COMPLETENESS_MATRIX.md, marking each feature DONE, PARTIAL, FAKE, MOCKED, HARDCODED, NOT_CONNECTED, BROKEN, or UNKNOWN.
- Security and privacy, from the SECURITY_AUDIT.md and PRIVACY_AUDIT.md templates.

Every claim is cited to files. Facts are separated from assumptions. No invented files, no invented completed features.

## Phase 3: Research comparable projects online

Read 24_SIMILAR_PROJECTS_RESEARCH.md and apply it. If web access exists, find comparable and competing projects, extract their real feature sets and quality bars, and turn the difference into concrete backlog items. If web access does not exist, use general knowledge and the provided files only, and mark these items as needing later verification.

Output: SIMILAR_PROJECT_GAP_ANALYSIS.md, FEATURE_OPPORTUNITY_LIST.md, and FEATURE_KILL_LIST.md under reports/. Do not copy code from other projects. Learn patterns and capabilities, then design original implementations.

## Phase 4: Build the maximal plan

Merge everything from phases 1 to 3 into one normalized, deduplicated, prioritized backlog using 05_BACKLOG_TRIAGE_PROMPT.md. Then lay it out as levels using the MODERNIZATION_PLAN.md template and as time horizons using ROADMAP.md.

Each task carries: id, title, source, priority, dependencies, risk, effort, likely files, required model tier, acceptance criteria, and the proof required to mark it done. Tasks that cannot be proven are marked blocked with the reason. Tasks that need frontier level reasoning are reserved for a frontier window.

Output: NORMALIZED_BACKLOG.md, MODERNIZATION_PLAN.md, ROADMAP.md under reports/, plus FIRST_BATCH_PLAN.md.

## Implementation is mandatory, not optional

Phases 1 to 4 produce analysis and a plan. They are not the deliverable. A run that stops after planning, producing only audit and plan files, is an incomplete run and must not be reported as done. Unless a hard safety stop is hit, you must enter Phase 5 and make real code changes with proof. If you cannot make code changes because you lack file write or execution tools, or because repository write access is missing, stop and say so explicitly, naming the missing capability. Do not substitute more analysis files for implementation.

## Phase 5: Implement in a proven loop, as a coordinated team

Before starting, read 26_GIT_GITHUB_WORKFLOW.md, 27_ROLE_ORCHESTRATION.md, and 29_EXPLORATION_AND_SPIKES.md. From here on, act as an engineering organization: every batch flows through the role chain, on its own Git branch, behind gates, and merges only with proof. Independent batches may run on parallel branches; dependent batches are serialized by the dependency graph.

Run the loop without pausing for me, until a stop condition or the definition of maximum is met.

For each batch:
1. Orchestrator selects the next 1 to 3 tasks by priority and dependency order, highest impact and lowest risk first, blockers before dependents, and opens a branch named by type and scope per the Git workflow.
2. Architect confirms no expensive decision is implied, or records an ADR. If the task has a genuine fork between viable approaches, the Architect frames the options and the Orchestrator runs exploration per 29_EXPLORATION_AND_SPIKES.md: one explore/<topic>-<option> branch per option, a minimal spike and a draft pull request each, evaluated by the oracle and the scorecard, with the winner merged and every rejected option tagged and logged in EXPERIMENT_LOG.md so it can be revisited. Otherwise the Planner writes the task spec directly with acceptance criteria, impacted files, the proof required, and the model tier per the routing policy, using the cheapest sufficient tier.
3. Implementer makes only this batch's change, with atomic conventional commits. Minimal diff. No refactor outside scope, no needless rename, no new hardcoding or secrets.
4. Test engineer adds tests against the acceptance criteria and any oracle tests, then runs build, tests, and lint using 11_TESTING_VALIDATION.md, capturing results. If no tests exist, do the minimal validation defined there.
5. Reviewer applies git/CODE_REVIEW_CHECKLIST.md. If it fails, return to the Implementer and repeat until it passes. Security and privacy, and Performance where relevant, run their checks and can block.
6. Apply the quality gates from QUALITY_GATES.md. A batch advances only if every gate is green.
7. Integrator opens a pull request using git/PULL_REQUEST_TEMPLATE.md, runs CI per git/ci.example.yml adapted to the stack, and merges only on green checks and a passed review, then deletes the branch. If remote actions are not permitted, prepare the pull request content locally and record it instead.
8. Scribe records proof in IMPLEMENTATION_PROOF_MATRIX.md, updates execution-log.md and JOURNAL.md, and writes a short batch report under batch-reports/. Surface information to me at the level chosen in the oversight setup. Score the batch with 14_SCORECARD.md. If the score is below usable twice in a row, stop and report.
9. Move to the next batch. Release manager acts only when a release boundary is reached, applying 13_RELEASE_READINESS.md, versioning, tagging, and updating the changelog.

After every few batches, re run the relevant audits so the backlog reflects new reality, and reprioritize.

## Definition of maximum (when to stop the loop)

Stop the loop and declare the project at its practical maximum when all of these hold, per 25_MAXIMIZATION_LOOP.md:
- All P0 and P1 tasks are done with proof.
- The release readiness go criteria in 13_RELEASE_READINESS.md are met.
- Remaining tasks are P2 or lower, and each added one no longer changes the scorecard meaningfully (diminishing returns).
- No fake, mocked, or hardcoded feature is presented as real.
- Security, privacy, and cost limits are in place.
- Real code changes have been implemented and proven. Analysis and planning files alone never satisfy completion.

At that point, produce a final report and stop.

## Stop conditions (pause and ask me even with standing approval)

- A step would send sensitive, confidential, or government data to a remote model. Apply 21_DATA_BOUNDARY_AND_GOVERNANCE.md.
- A remote Git action is required (push, open or merge a pull request, tag a release) but repository permissions are not clearly granted, or the action would touch main directly or rewrite shared history. Apply 26_GIT_GITHUB_WORKFLOW.md.
- A budget or rate limit from the model-management folder would be exceeded.
- A batch fails the quality gates or scores below usable, twice in a row.
- A decision that is expensive to reverse is required and is not covered by an ADR you can write with confidence.
- The repository cannot be read or files cannot be written.
- Five consecutive tool or model errors.

Outside these, proceed to the end.

## Final output

When the loop ends, produce MAXIMIZATION_REPORT.md under reports/ containing:
- What the project did at the start versus now, proven.
- The full list of tasks done, with proof references.
- The features added and the features killed, with reasons.
- The gap closed against comparable projects.
- Remaining P2 and lower items, and reserved frontier tasks.
- Explored forks and their outcomes, with the recover refs of rejected options and their revisit triggers.
- The current scorecard and release readiness status.
- An index of every file created, with absolute paths.

Update 20_SESSION_HANDOFF.md so any future session can continue.
