# AI Project Acceleration Package

A package you drop into any project, new or existing. You give an AI agent one path, and it audits, decides, plans, and builds, following Git and GitHub best practices, working like a coordinated engineering team, exploring real forks, recovering from errors, and journaling everything.

This README is the launch manual. It lists every way to run it, the exact triggers, the oversight options, how to resume, and how to tell whether your agent can actually do the work.

## The one input you provide

The only thing a human supplies is the path to a run file. Everything else is auto detected by the preflight in 28_PREFLIGHT_AUTOCONFIG.md: operating system, stack, build and test commands, Git host, remote permission level, CI, web access, available tools, model tiers, and data sensitivity. Whatever cannot be detected gets a safe default, recorded in reports/ENV_PROFILE.md. The agent does not stop to ask for configuration. It pauses only at real safety boundaries.

## Install

Unzip the folder and place it anywhere in your project, for example at <repo>/ai-work, so the run files sit directly inside it:

```
<repo>/ai-work/AUTORUN.md
<repo>/ai-work/AUTORUN_MAX.md
<repo>/ai-work/MEGAPROMPT.md
...
```

The folder name does not matter. Every file resolves its references against its own folder. Only one rule: do not nest it twice, you should never have <repo>/ai-work/ai-work/AUTORUN.md. The only path you give the agent is the path to the run file you choose.

## The most powerful launch (copy this)

For the strongest run, full build in true autonomy, give the agent the project and paste this, replacing the path with yours:

```
Execute AUTORUN_MAX.md at ./ai_autorun/AUTORUN_MAX.md.

Oversight: L0 fully autonomous. Do not hand control back to me during the run.
For the oversight setup, do not ask me; use these settings. Decisions and risks,
summary verbosity, full journaling on.

Run end to end: do not pause at phase boundaries and do not stop after planning.
Phase 5 implementation is mandatory. A run that produces only analysis or plan
files is incomplete. Implement real code changes in the loop, on branches, with
conventional commits, tests, and proof, behind the quality gates.

For any risky or irreversible item (expensive to reverse, security, data boundary,
or a remote action without permission): do not ask me and do not attempt it blindly.
Record it in TODO_BLOCKED.md with evidence, options, and a recommended default,
mark it reserved, and continue with all other work.

When a genuine fork between viable approaches appears, explore the options on
parallel branches, evaluate against the oracle and the scorecard, keep the winner,
and preserve the rest as recoverable experiments. On any error or failure, run the
recovery loop and try alternatives; never hide a failure or fake a success.

The only events that end the run early are true capability failures: files cannot
be written, or a remote action is impossible without credentials. Otherwise proceed
to the end. Then present the MAXIMIZATION_REPORT.md and the consolidated
TODO_BLOCKED.md for me to decide on.
```

To resume a previously analyzed run, add one line: Read 20_SESSION_HANDOFF.md, skip re-analysis, go straight to Phase 5.

This single block encodes everything: real autonomy without handing control back, mandatory implementation, deferral of risky items to TODO_BLOCKED.md instead of blocking, fork exploration, error recovery, and full journaling. For it to mean anything, the agent must be able to edit and execute files on the repository. With a command line agent or an IDE extension it runs Phase 5 and produces commits. If you still get only analysis files, the agent lacks code tools; reports/ENV_PROFILE.md confirms this in its detected tools list.

## The run files, at a glance

| File | What it does | Use it when |
|---|---|---|
| AUTORUN_MAX.md | Full build. Discovers every task, audits, researches comparable projects, plans, then implements in a proven loop with branches, pull requests, tests, and gates, until the project reaches its practical maximum. | You want real code changes and a maximized project. |
| AUTORUN.md | Burst. Extracts what only a strong model produces, decisions, the hardest problem, and the oracle, and freezes it into files. Does not implement. | A powerful model is available briefly and you want durable artifacts fast. |
| MEGAPROMPT.md | One shot. A single paste that bootstraps a capable model. Returns artifacts in the conversation. | The agent cannot read or write your files. |
| 00_MASTER_PROMPT.md and 01 to 15 | Manual, step by step prompts you drive yourself. | You want full control over each stage. |

## Way 1: full build, push the project to its maximum

This is the one that writes code. Give the agent the project, then send:

```
Execute AUTORUN_MAX.md at ./ai-work/AUTORUN_MAX.md. You have my standing approval
to proceed through every phase and every batch without asking me between steps.
Implement real code changes in the loop, not only audit files. Stop only on the
stop conditions defined in the file. Produce saved files and working code with
proof, not conversation.
```

Replace ./ai-work/AUTORUN_MAX.md with your real path. Standing approval sets fully autonomous mode, so it does not pause at phase boundaries and does not stop after planning. It runs end to end and reports at the finish.

## Way 2: frontier burst, a short window with a strong model

Use this to extract decisions, the hardest problem, and the oracle, then freeze them. It does not implement.

```
Execute AUTORUN.md at ./ai-work/AUTORUN.md. You have my standing approval to
proceed through every step without asking me between steps. Stop only on the
stop conditions defined in the file. Produce saved files, not conversation.
```

After a burst, you can run Way 1 to build on top of the frozen artifacts, or hand the work to a cheaper model with EXECUTOR_GUIDE.md.

## Way 3: one shot, when the agent cannot touch your files

If you are in a plain chat with no file access, open MEGAPROMPT.md, copy its full block, paste it, then add your codebase and your goal where it says to. It returns the artifacts in the conversation for you to save.

## Way 4: manual, full control

Point the agent at 00_MASTER_PROMPT.md and follow its initial phase, then use the numbered prompts 01 to 15 in order. The model management prompts live under model-management. This gives you a stage by stage workflow you drive yourself.

## Choosing how much oversight you want

At the very start the agent runs the oversight setup in 30_OVERSIGHT_AND_JOURNALING.md and asks once: human in the loop or not, the level, the information type, the verbosity, and journaling. You can answer, or set it directly in your launch, or let it default.

Set it in the launch to avoid the question. Examples you can append to any trigger:

Fully autonomous, no questions at all:
```
Oversight: L0 fully autonomous, do not pause at phase boundaries, do not stop
after planning. For the oversight setup, do not ask me; use these settings.
```

Checkpoints at phase boundaries and before merges and remote actions:
```
Oversight: L1 checkpoints. Pause at phase boundaries, before merging to main,
and before any remote action.
```

Approve each batch before it is implemented:
```
Oversight: L2 batch approval. Show me each batch plan and wait for my approval.
```

Approve each significant action:
```
Oversight: L3 step approval. Confirm each significant action with me first.
```

Information type and verbosity can be added too, for example:
```
Surface decisions and risks only, summary verbosity, full journaling on.
```

If you grant standing approval in the trigger, oversight is treated as L0 fully autonomous. If you want checkpoints, say so explicitly with L1, L2, or L3.

## Fully autonomous, no human in the loop

L0 means the agent never hands control back to you during a run. It does not ask you to decide anything, including for P0 risks. Anything safe and reversible is implemented now behind the gates. Anything that would need your decision, an irreversible change, a security or data boundary, or a remote action without permission, is not attempted: it is recorded in TODO_BLOCKED.md with evidence, options, and a recommended default, then the run continues with everything else. You review the consolidated TODO_BLOCKED.md at the very end. The run only ends early on a true capability failure, for example the files cannot be written. Set it with:

```
Oversight: L0 fully autonomous. Do not hand control back to me during the run.
For any risky or irreversible item, do not ask me: record it in TODO_BLOCKED.md
with evidence, options, and a recommended default, and continue. Present the
consolidated TODO_BLOCKED.md at the end.
```

## Resuming a previous run

A previous run leaves frozen files: the backlog, the ADRs, the oracle, and 20_SESSION_HANDOFF.md. To continue without redoing the analysis:

```
Execute AUTORUN_MAX.md at ./ai-work/AUTORUN_MAX.md. Oversight: L0 fully autonomous.
You already have the analysis, ADRs, backlog and oracle from the previous run;
read 20_SESSION_HANDOFF.md, skip re-analysis, and go straight to Phase 5.
Implement real code changes in the loop, on branches, with tests and proof.
A run that produces only analysis or plan files is incomplete. Stop only on the
hard safety stops defined in the file.
```

Any session, with any model, starts by reading 20_SESSION_HANDOFF.md and the frozen authorities, not by re deriving the project.

## What each run produces

Burst and the analysis phases produce, as saved files: a capability sheet, PRODUCT_REALITY_REPORT.md, ARCHITECTURE_MAP.md, ADR files, a SOLUTION with oracle tests, NORMALIZED_BACKLOG.md, FIRST_BATCH_PLAN.md, EXECUTOR_GUIDE.md, OMISSIONS_AND_GAPS.md, and an updated handoff.

The full build adds real code: branches per batch, conventional commits, pull requests, tests, proof in IMPLEMENTATION_PROOF_MATRIX.md, batch reports, a running JOURNAL.md, and a final MAXIMIZATION_REPORT.md.

## If it only produced analysis files and no code

The build is supposed to write code in Phase 5. If you got only Markdown, check three things in order:

1. Open JOURNAL.md or execution-log.md and read the last entry. If it says it paused at a checkpoint, set oversight to L0 in the trigger and relaunch. If it names a hard safety stop, that was deliberate.
2. Open reports/ENV_PROFILE.md and look at the detected tools. If file write or code execution is not available, the agent cannot implement. No trigger fixes a missing capability.
3. Confirm the agent has write access to the repository root, not only to an output folder.

The decisive factor is the agent. An agent with real file edit and execution tools, such as a command line agent or an IDE extension, runs Phase 5 and produces commits. An assistant that only reads and writes text artifacts will never implement, regardless of the trigger. Use a code capable agent for the full build.

## Safety stops, the only reasons it pauses under full autonomy

- Sensitive, confidential, or government data would be sent to a remote model.
- A remote Git action is required but repository permissions are not clearly granted, or it would touch main directly or rewrite shared history.
- A budget or rate limit would be exceeded.
- A decision expensive to reverse is required and no record covers it.
- The repository cannot be read or files cannot be written.
- Repeated unrecoverable errors.

Outside these, under standing approval, it runs to the end.

## File map

- AUTORUN_MAX.md, AUTORUN.md, MEGAPROMPT.md: the run files.
- 00 to 15: the master prompt and the staged manual prompts.
- 16 to 22: the frontier burst protocol, question bank, arrival checklist, capture and freeze, handoff, data boundary, quickstart.
- 23 to 30: task source discovery, similar projects research, maximization loop, Git and GitHub workflow, role orchestration, preflight autoconfig, exploration and spikes, oversight and journaling.
- model-management: registry, routing, budget, rate limits, evals, decision records.
- git: branching strategy, commit convention, pull request template, code review checklist, example CI.
- templates: every output template, including the proof matrix, scorecard, experiment log, journal, and autonomy test.
- scripts: validate_package.py and the structure checks.
- reports, adr, batch-reports, experiments, logs, outputs: where the agent writes its work.

## Core rules the agent always follows

- No task is done without proof. Analysis and plans alone never count as done.
- Use code reality, not documentation claims.
- Classify and redact data before any remote call.
- One branch and pull request per batch, conventional commits, gates before merge, protected main.
- Explore real forks on parallel branches, keep every path recoverable.
- Recover from errors by trying alternatives, never hide a failure.
- Journal everything.
