# Frontier Question Bank

A categorized reserve of high leverage questions. The Frontier Burst Protocol gives you the ordered core sequence. This file is the exhaustive reserve, so that nothing important is forgotten. Pick the questions that fit your project and your remaining time. Every question is written so the answer should end in a saved artifact.

How to use: scan the categories, mark the ones that apply, paste them, and demand a file as output. Do not ask a frontier model a question whose answer a weak model could produce.

## 1. Architecture and design

- What is the smallest architecture that satisfies the real requirements, and what am I overbuilding?
- Where are the hidden couplings that will make future change expensive?
- Which boundaries in this system are wrong, and where should they actually be?
- If this project must scale by 100 times, what breaks first and what is the cheapest change now that avoids a rewrite later?
- Which abstraction is leaking, and what is the cost of fixing it now versus later?

## 2. Algorithms and research level problems

- State the core computational problem formally, then give the best known approach and its bounds.
- Is there a known result, paper, or technique that solves this better than my current approach?
- What is the correctness argument for this algorithm, and which inputs violate its assumptions?
- Where am I paying an avoidable complexity cost, in time, memory, or coordination?
- What is the simplest version that is provably correct, even if slower, so I have a reference to test against?

## 3. Performance

- Profile the described workload on paper: where is the dominant cost?
- Which optimization gives the largest real gain for the least risk, and which are premature?
- What is the theoretical lower bound for this operation, so I know when to stop optimizing?
- Where will latency or memory behave nonlinearly under real load?

## 4. Security

- Build a threat model: assets, attackers, entry points, and the trust boundaries.
- What are the top vulnerabilities given this stack, ranked by exploitability times impact?
- Where does untrusted input reach a dangerous sink without validation?
- What secrets, tokens, or keys are at risk of exposure, and how should they be handled?
- What is the minimal set of controls that removes the most risk?

## 5. Privacy, governance, and compliance

- Which data in this system is personal, sensitive, or confidential, and where does it flow?
- What must never be sent to a remote model, and how do I enforce that boundary technically?
- For a Quebec or European context, what does Law 25 or the GDPR require for this data flow, and where am I non compliant today?
- What is the minimal logging that meets audit needs without storing more personal data than necessary?
- What is my data retention and deletion story, and is it actually implemented?

## 6. Data model and migration

- Is the data model correct for the real access patterns, or shaped by accident?
- Where will a schema change be painful later, and what should change now while it is cheap?
- Design a safe, reversible migration path from the current state to the target state.
- What invariants must hold across the migration, and how do I test them?

## 7. AI and agent subsystems

- Is my agent architecture sound, or am I adding agents where a function call would do?
- Where can model output corrupt state without a validation gate?
- Design the routing between local, small, standard, and reasoning tiers for my real task mix.
- What is the fallback behavior when a provider is down, rate limited, or degraded?
- How do I evaluate my own prompts so that a prompt change is treated like a code change?
- Where am I trusting model output as truth without proof, and how do I close that gap?

## 8. Testing and the oracle

- What is the authoritative specification of correct behavior for the core feature?
- Write the acceptance tests that any implementation must pass, including edge cases.
- Where is my current test suite giving false confidence?
- What is the minimal set of tests that would catch the regressions I actually fear?
- Which properties are best tested with property based or fuzz testing rather than examples?

## 9. Reliability and failure modes

- Enumerate the failure modes of the main path, ranked by likelihood times impact.
- Where does this system fail silently, returning wrong results without an error?
- What is the blast radius of each external dependency failing?
- What is the recovery story after a crash mid operation?

## 10. Packaging, release, and operations

- What is the gap between "runs on my machine" and "a stranger can install and run this"?
- What is the minimal observability that would let me diagnose a production issue?
- Design a release checklist that a non author could follow.
- What is the rollback plan if a release is bad?

## 11. Product and scope

- What is the minimum credible version that a real user would find useful?
- Which features should I kill because they add risk without adding value?
- What is the single strongest demo this project can give, and what is missing to reach it?
- Where is the gap between what users need and what the system does?

## 12. Cost

- What is the realistic monthly cost of running this at the expected scale, broken down by component?
- Where is model spend wasted on tasks a cheaper tier could do?
- What is the cost of one full pass of my agent pipeline, and where is it concentrated?

## 13. Autonomy and handoff

- Produce a frozen plan a weaker model can execute without you.
- Which tasks must a weaker model never attempt, and why?
- Write the operating guide for an executor model: read order, definition of done, stop conditions.
- What context must persist across sessions for the work to continue safely?

## 14. Unknown unknowns (the anti forgetting set)

- What are the five questions I should have asked but did not?
- What am I deciding implicitly without realizing it is a decision?
- What is the assumption in this project most likely to be wrong and most expensive if it is?
- If you could change one thing about how I am approaching this, what would it be and why?
- Given uncertain availability, what is the single most valuable artifact you could produce for me right now? Produce it.

## Selection guidance

- Short window: Architecture, the hardest algorithm with its oracle tests, the frozen plan, and the unknown unknowns set. Skip the rest.
- Medium window: add Security, Privacy and governance, and Failure modes.
- Long window: work the full list, but always end each session by saving artifacts and updating the handoff file.
