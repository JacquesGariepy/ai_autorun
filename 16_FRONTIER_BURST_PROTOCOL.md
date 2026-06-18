# Frontier Burst Protocol

## Why this file exists

A very capable model may become available for a short, uncertain window. You may not control when it arrives, how long it stays, or whether it leaves again. The mistake to avoid is spending that scarce window on work a weaker model can already do.

This protocol does three things, in order:
1. Extract only what a frontier model can produce better than anything else.
2. Freeze that output into durable artifacts that survive after the model is gone.
3. Leave behind a fully autonomous execution plan that cheaper or local models can finish without the frontier model.

The governing idea: a frontier model is most valuable as a designer, prover, and oracle author, not as a typist. Mechanical implementation is the cheapest part of your project. Correct decisions, hard algorithms, authoritative specifications, and executable acceptance tests are the irreplaceable part. Capture those first.

## What only a frontier model should produce (the irreplaceable list)

Spend the burst on these and nothing else:
1. Architecture decisions with explicit tradeoffs, recorded as decision records you can defend later.
2. The single hardest algorithm or design problem in your project, solved with a correctness or complexity argument.
3. A test oracle: the authoritative specification plus executable acceptance tests. This is the autonomy lever. If the oracle is strong, a weak model can iterate to green on its own.
4. A golden reference implementation of the 1 to 3 most critical components.
5. A threat model and privacy design, including the data that must never leave the machine.
6. A frozen, dependency ordered execution plan, where every task carries acceptance criteria and an assigned model tier.
7. The unknown unknowns: the questions you did not think to ask, and the assumptions most likely to be wrong.

Everything else is execution. Hand it to a cheaper tier.

## Operating rules for the burst

1. Front load capability and boundary probing. You must know what you are talking to before you trust it.
2. One artifact per answer. Every question ends with "produce file X". A burst that yields conversation but no files is a wasted burst.
3. Redact before sending. Apply `21_DATA_BOUNDARY_AND_GOVERNANCE.md` before any remote call. Confidential, client, or government data does not go to a remote model.
4. Capture continuously. After each wave, save outputs into the package directories and update `20_SESSION_HANDOFF.md`. Assume the model disappears after the next message.
5. Prefer durable over impressive. A frozen spec beats a long brilliant explanation.
6. Do not let the model implement the whole project in one shot. You want a verifiable plan and an oracle, not an unauditable mega diff.

## The waves

Each wave below gives you the exact prompt to paste, the expected output, and the file to save it as. Run them in order. Skip a wave only if you already have its artifact.

### Wave 0: Identify and bound the model (5 minutes, before trusting anything)

Paste:

```
Before any project work, answer precisely and briefly:
1. Which model and version are you, and what is your training knowledge cutoff?
2. What is your maximum input context size and maximum output size in this session?
3. Which tools can you actually call right now: web access, code execution, file reading, image input? List only what is truly available.
4. Are you deterministic at temperature 0, or should I expect variation across runs?
5. What categories of request will you refuse or partially refuse, so I do not waste the window discovering limits by trial?
6. If I give you a large codebase, what is the best way to feed it to you given your context limit?
State unknowns as unknown. Do not guess.
```

Expected output: a capability sheet. Save to `model-management/decision-records/` as a Model Decision Record, and copy the limits into `18_MODEL_ARRIVAL_CHECKLIST.md`. This sizing decision determines how you feed the project in every later wave.

### Wave 1: Ground truth of the project

Goal: get the reality of your codebase, not the story the README tells. This is where a strong model earns its keep, because it catches disconnected features, silent failure paths, and load bearing assumptions that weaker models miss.

Paste (attach the codebase or the most relevant slice):

```
You are a senior delivery architect. Analyze the real system, not its documentation.
Produce a single report named PRODUCT_REALITY_REPORT.md with these sections:
- What the system actually does, proven by specific files and lines.
- What the documentation claims that the code does not support.
- The true architecture, including the data and control flow of the main path.
- Features that are present in the UI or API but disconnected, mocked, or hardcoded.
- The five load bearing assumptions that, if wrong, break the system.
- The five highest risk areas, ranked, each with the evidence that makes it risky.
Rules: cite files for every claim. Separate facts from assumptions. Do not invent files. If you cannot verify something, mark it unverified.
```

Expected output: `PRODUCT_REALITY_REPORT.md`. Save to `reports/`. Also produce `ARCHITECTURE_MAP.md` and `templates/ARCHITECTURE_DIAGRAM.mmd` if not already present.

### Wave 2: The irreversible decisions

Goal: get the decisions that are expensive to reverse made well, once, and recorded. These are the decisions you do not want a weaker model improvising later.

Paste:

```
Identify every decision in this project that is expensive to reverse: data model, persistence, concurrency model, public API contracts, security boundary, AI provider abstraction, packaging, and offline versus online operation.
For each one, produce a decision record with: context, the options, the tradeoffs, your recommended choice, the conditions under which the choice would be wrong, and the cost of reversing it later.
Output one Markdown file per decision named ADR-XX-short-title.md.
Recommend, do not just enumerate. Where you are uncertain, say what evidence would resolve it.
```

Expected output: a set of `ADR-XX-*.md` files. Save to `adr/`. These are durable. They remain valid after the model is gone.

### Wave 3: Solve the hardest problem, with a proof

Goal: use the frontier model on the one problem that is genuinely hard in your project. Pick the algorithm, the distributed protocol, the performance bottleneck, the formal model, or the tricky correctness property. You want a solution plus an argument for why it is correct or within bounds, because that argument is what lets you trust the result after the model leaves.

Paste (replace the bracket):

```
The hardest problem in this project is: [STATE THE PROBLEM PRECISELY, WITH CONSTRAINTS].
Solve it. Then defend the solution:
- Give the algorithm or design in enough detail to implement.
- State its correctness argument or its complexity and resource bounds.
- State the failure modes and the inputs that break it.
- Give a golden reference implementation of the core, with inline comments explaining the non obvious steps.
- Give the edge case tests that any implementation must pass.
Output two files: SOLUTION_<name>.md and oracle_tests_<name> in the project test format.
```

Expected output: a solution document and an oracle test file. Save the solution to `reports/` and the oracle tests into your test suite. The oracle tests are the most valuable artifact in the entire burst.

### Wave 4: Build the autonomy package (the freeze)

Goal: convert everything above into a frozen, dependency ordered plan that a cheaper or local model can execute without ever needing the frontier model again. This is what makes the project "autonomous" after the window closes.

Paste:

```
Produce a frozen execution package so that a less capable model can finish this project without you.
1. A dependency ordered backlog as a table: order, id, title, acceptance criteria, files likely touched, required model tier (local, small, standard, reasoning), risk, and the proof required to mark it done.
2. For each high risk task, a short executable acceptance test or a precise manual check.
3. A list of tasks that must NOT be attempted by a weaker model, with the reason.
4. A one page operating guide for the executor model: what to read first, the definition of done, and the stop conditions.
Output files: NORMALIZED_BACKLOG.md, FIRST_BATCH_PLAN.md, and EXECUTOR_GUIDE.md.
Every task must be provable. If a task cannot be proven, mark it blocked and say what is missing.
```

Expected output: `NORMALIZED_BACKLOG.md`, `FIRST_BATCH_PLAN.md`, and `EXECUTOR_GUIDE.md`. Save to the package root or `reports/`. After this, the frontier model is optional.

### Wave 5: Catch the omissions (the anti forgetting wave)

Goal: directly serve the requirement of forgetting nothing. Ask the model to find the gaps in your own questioning.

Paste:

```
Review this entire session. Then tell me:
1. The five most important questions I should have asked you in this window but did not.
2. The decisions I am about to make implicitly, without realizing I am deciding them.
3. The parts of this project most likely to fail silently in production.
4. The single highest leverage thing I could ask you to produce in the next message, given that your availability is uncertain.
Answer 4 by actually producing that artifact now, not by describing it.
```

Expected output: a gap analysis plus one more artifact. Save the gap analysis to `reports/OMISSIONS_AND_GAPS.md`.

## After the burst

1. Verify you have saved, as files: the capability sheet, the reality report, the ADRs, the solution and oracle tests, the frozen backlog, the executor guide, and the omissions report.
2. Update `20_SESSION_HANDOFF.md` so the next session, with any model, can continue.
3. Switch execution to the cheapest tier that passes the oracle. Reserve any future frontier window for the next genuinely hard problem only.

## One line summary

Use the strong model to decide, to prove, and to write the oracle. Use cheap models to type. Freeze everything into files before the window closes.
