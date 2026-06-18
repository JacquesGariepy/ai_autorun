# Role Orchestration

This file makes the agent act as a coordinated engineering organization rather than a single coder. The work flows through a chain of roles, each with a clear mandate and a gate, so that every change is designed, built, reviewed, tested, hardened, integrated, and released with the discipline of a strong team.

The metaphor of a thousand engineers working together is achieved not by a thousand voices at once, but by a disciplined pipeline of role passes with handoffs and gates, parallelized where work is independent. Many small, well reviewed, well tested changes compounding is exactly how a large effective team produces quality.

## The roles

Each role is a mode the agent enters, with its own objective and its own definition of done. A single agent plays them in sequence. A multi agent setup assigns them to separate agents that hand off through files and pull requests.

- Orchestrator: owns the plan and the queue. Selects the next batch, assigns the role chain, enforces gates, resolves conflicts, decides parallel versus serial, and decides when a fork is worth exploring versus taking a safe default.
- Architect: owns decisions that are expensive to reverse. Produces and updates ADRs. Approves designs before implementation. Frames the options for a genuine fork and the criteria that decide between them, per 29_EXPLORATION_AND_SPIKES.md.
- Planner: turns a backlog item into a concrete task spec with acceptance criteria, impacted files, and the proof required.
- Implementer: writes the minimal change to satisfy the spec, on a batch branch, with atomic conventional commits.
- Reviewer: applies git/CODE_REVIEW_CHECKLIST.md. Blocks on scope creep, missing tests, weak quality, or safety issues.
- Test engineer: writes and runs tests, including edge cases, and captures results as proof.
- Security and privacy: checks for secrets, unvalidated input, and sensitive data leaving the boundary. Can block a merge.
- Performance: checks the hot path for obvious waste and unacceptable behavior under load, when relevant.
- Integrator: opens the pull request, runs CI, ensures checks are green, and merges per the merge policy.
- Release manager: applies 13_RELEASE_READINESS.md, versions, tags, and writes the changelog.
- Technical writer: keeps the README, docs, and changelog truthful to the code.
- Scribe: updates execution-log.md, the proof matrix, decision records, and 20_SESSION_HANDOFF.md.

## The work chain for one batch

Every batch of 1 to 3 tasks flows through this chain. A stage may pass quickly when there is little to do, but no stage is skipped silently.

1. Orchestrator selects the batch and opens a branch per 26_GIT_GITHUB_WORKFLOW.md.
2. Architect confirms no expensive decision is implied, or records an ADR if one is.
3. Planner writes the task spec with acceptance criteria and proof requirements.
4. Implementer writes the minimal change with atomic commits.
5. Test engineer adds and runs tests, captures results.
6. Reviewer applies the review checklist. If it fails, return to Implementer. This loop repeats until the checklist passes.
7. Security and privacy, and Performance where relevant, run their checks. Either can block.
8. Quality gates from QUALITY_GATES.md are applied. All must be green.
9. Integrator opens the pull request with the template, runs CI, and merges only on green checks and a passed review.
10. Scribe records proof and updates the logs. Release manager acts only when a release boundary is reached.

A batch is done only when it has merged with proof, or is explicitly blocked with a reason.

## Gates between stages

A gate is a hard checkpoint. Work does not advance past a gate that is not satisfied.

- Design gate: no implementation starts on an expensive decision without an ADR.
- Review gate: no pull request is ready while the review checklist fails.
- Safety gate: no merge while a secret, an unvalidated dangerous input, or a sensitive data leak is present.
- CI gate: no merge while required checks are red.
- Release gate: no release while go criteria are unmet.

## Parallelization, the many engineers effect

- The Orchestrator builds a dependency graph of the backlog.
- Independent batches run on parallel branches, as separate role chains, like separate engineers on separate features.
- Dependent batches are serialized by the graph.
- Shared files are coordinated to avoid conflicting edits. Conflicts are resolved by the Orchestrator, not by overwriting.
- Throughput comes from many small proven changes in flight, each fully reviewed, not from one large unreviewed change.

## Conflict and disagreement

- When the Architect and Implementer disagree, the ADR decides. If no ADR covers it, the Architect writes one before work proceeds.
- When the Reviewer blocks, the Implementer fixes or escalates to the Orchestrator. The block stands until resolved.
- Safety and CI gates cannot be overridden by any role.

## Honest bound

This produces the discipline and throughput of a strong, well run team. It does not literally multiply intelligence. The quality comes from the chain, the gates, the proof, and the parallelization, applied relentlessly to many small changes.
