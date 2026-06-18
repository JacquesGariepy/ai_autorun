# AI Project Acceleration Package, version 3

Drop this into any existing software project as `/ai-work`. It prepares you to extract maximum value from an AI agent, and in particular to be ready the moment a much more capable model becomes available, possibly for a short window.

## Two modes

This package serves two situations.

1. Steady state. A capable model works your backlog with discipline: it reads the real code, ignores unproven documentation claims, audits unfinished and faked work, manages model cost and routing, implements in small validated batches, and proves every task. This is the original engine, files 00 through 15 and the model-management subsystem.

2. Frontier burst. A very capable model becomes available, possibly briefly. You must extract what only it can produce, freeze it into durable files, and leave an autonomous plan that cheaper models finish without it. This is the new layer, files 16 through 22 plus the megaprompt.

## You provide one thing: a path

The only input a human gives is the path to the run file. Everything else is auto detected by the preflight in 28_PREFLIGHT_AUTOCONFIG.md: the operating system, the stack, the build and test commands, the Git host, the remote permission level, CI, web access, the available tools, the model tiers, and the data sensitivity. Whatever cannot be detected gets a safe default, recorded as an assumption in reports/ENV_PROFILE.md. The agent does not stop to ask for configuration. It pauses only at real safety boundaries. At the very start it asks one set of setup questions: whether you want human in the loop and at what level, the type and verbosity of information, and confirmation of full journaling. Answer them, or let it apply safe defaults and proceed. Everything it undertakes is journaled in JOURNAL.md, including explorations, tool choices, errors, and recoveries.

## Three ways to run it

1. Maximization, the full build. Point an agent at AUTORUN_MAX.md. It discovers every task in CSV and in code and in docs, audits unfinished work and hardcoding, researches comparable projects online, builds the maximal plan, and implements in a proven loop until the project reaches its practical maximum. It works as a coordinated engineering organization: a chain of roles (architect, planner, implementer, reviewer, tester, security, integrator, release manager) with quality gates, and it follows Git and GitHub best practices, one branch and pull request per batch, conventional commits, required CI checks, and protected main. When a real fork appears between viable approaches, it explores the options on parallel branches, evaluates them, keeps the best, and preserves the rest so they can be revisited. Use this to bring a project, new or existing, to its peak.

2. Frontier burst, the short window. Point an agent at AUTORUN.md. It extracts what only a very capable model can produce, decisions, the hardest problem, and the oracle, and freezes it into files so cheaper models finish the rest.

3. Manual, full control. Use the numbered prompts and the master prompt yourself.

## Start here

- A powerful model just dropped: open `22_QUICKSTART.md`, then `16_FRONTIER_BURST_PROTOCOL.md`.
- You want the exact questions to ask: `16_FRONTIER_BURST_PROTOCOL.md` for the ordered core, `17_FRONTIER_QUESTION_BANK.md` for the exhaustive reserve.
- You want one paste that bootstraps everything: `MEGAPROMPT.md`.
- You are doing normal disciplined work: `00_MASTER_PROMPT.md`.

## The doctrine in one paragraph

A frontier model is most valuable as a designer, a prover, and an oracle author, not as a typist. Mechanical implementation is the cheap part of any project. Correct decisions, hard algorithms, authoritative specifications, and executable acceptance tests are the irreplaceable part. Capture those first, freeze them into files, and let cheaper or local models do the typing. A project is autonomous when, given only the frozen files and the codebase, a weak model could finish the backlog and prove each task done.

## What is new in version 3

- 16: Frontier Burst Protocol, the ordered first contact question script.
- 17: Frontier Question Bank, the exhaustive reserve of high leverage questions.
- 18: Model Arrival Checklist, what to run the moment a new model appears.
- 19: Capture and Freeze, turning frontier output into an autonomous package.
- 20: Session Handoff, continuity across sessions and models.
- 21: Data Boundary and Governance, including a Law 25 and GDPR note.
- 22: Quickstart, a ten minute runbook.
- MEGAPROMPT.md, a single paste bootstrap.
- GLOSSARY.md and new templates: executor guide, autonomy test.
- A provider agnostic frontier tier added to the model registry and routing policy.
- An expanded intake that prepares the frontier window in advance.

## Core rules

- No task is done without proof.
- Use code reality, not documentation claims.
- Classify and redact data before any remote call.
- Use the strong model to decide, prove, and write the oracle. Let cheap models type.
- Freeze every frontier output into a named file before the window closes.

## Language agnostic

Works with command line agents, IDE agents, and custom API based agents. The prompts are model neutral. Point the frontier tier at whichever model is strongest when you need it.
