# Exploration and Spikes

The safe default rule resolves uncertainty about configuration. This file resolves a different kind of uncertainty: when there are several viable ways to do something real, the agent does not guess one. It explores the paths, builds each on its own branch with its own commits and a draft pull request, evaluates them with evidence, keeps the best, and preserves the others so they can be revisited later.

Governing rule: for a setup unknown, default safely and note it. For a genuine fork between viable approaches, explore the options in parallel, let evidence decide, and keep every path recoverable.

## When to default versus when to explore

Default safely, do not explore, when the uncertainty is about configuration or environment, or when one path is clearly correct. Examples: which build command, which branch name, whether a remote is present. Pick the safe default, record it, move on.

Explore, do not just guess, when there is a real fork that affects the result and more than one option is plausible. Signals of a real fork:
- Two or more reasonable architectures, libraries, data models, or algorithms.
- A performance or design tradeoff with no obvious winner from reading alone.
- A migration or refactor that could be done in materially different ways.
- A feature whose best shape is genuinely unclear.

If you cannot tell whether an option is better by reasoning, that is the signal to build it and measure it.

## How exploration works

For a fork worth exploring:

1. The Architect frames the options crisply: name each one, state its hypothesis, and state the criteria that will decide between them, drawn from the oracle tests and the scorecard.
2. The Orchestrator opens one branch per option, named explore/<topic>-<option>, from the same base. Independent options run in parallel, like separate engineers trying separate ideas.
3. On each branch, the Implementer builds the smallest honest version of that option, with atomic conventional commits, enough to evaluate it. This is a spike: real but minimal.
4. The Test engineer runs the deciding criteria against each option: oracle tests, the scorecard, performance numbers, complexity, and risk.
5. The Integrator opens a draft pull request per option, each carrying its results, so the comparison is visible and reviewable.
6. The Architect records the comparison in an ADR and in OPTION_COMPARISON.md: the options, the measured results, the chosen winner, and the conditions under which a rejected option should be revisited.

## Convergence, and keeping every path recoverable

When a winner is chosen:

- The winning branch is finished to full quality and merged through the normal gates.
- Every rejected option is preserved, never silently discarded. Tag each one experiment/<topic>/<option> so its history is permanent, and keep or archive its branch reference. Its draft pull request is closed with a note pointing to the tag, not deleted in a way that loses the work.
- EXPERIMENT_LOG.md records, for each explored path: the hypothesis, the result, the decision, the exact ref to recover it, and a one line resume command. This is what makes returning to a path real, not theoretical.
- The ADR records why the winner won and the trigger conditions that would justify reopening a rejected path.

## Returning to a path later

A rejected path can be revisited at any time, because its history is tagged and logged. To return: check out the tagged ref into a fresh explore branch, rebase onto current main, and resume from where it stopped. A path is reopened when its ADR trigger condition is met, for example the winner hits a limit the rejected option would not have, or a new requirement changes the tradeoff.

Nothing explored is ever lost. Every fork leaves a recoverable trail.

## Reversibility as a standing property

Beyond exploration, all work stays reversible:
- Every change lands through a branch and a pull request, so it can be reverted as a unit.
- Decisions that are expensive to reverse are recorded as ADRs with their reversal cost, so the path back is known before it is needed.
- Releases are tagged with a rollback path, per the release readiness criteria.

## Honest bound on cost

Exploration costs more than guessing, so it is reserved for real forks where the decision matters. Trivial choices take the safe default. The Orchestrator caps the number of options per fork, usually two or three, and caps the spike effort, so exploration informs the decision without consuming the whole budget. Exploration also respects the data boundary and the model budget like any other work.

## Exploration applies in every sphere

Exploration is not only for architecture. The same discipline applies wherever more than one path is plausible:

- Solutions and designs: competing ways to implement a feature.
- Algorithms: competing approaches with different bounds.
- Tools and libraries: when several could do the job, try the strongest candidates on a small real task and compare, rather than picking by reputation alone.
- Ideas: when the best shape of a feature is unclear, generate two or three candidate ideas, prototype the most promising minimally, and let evidence choose.
- Prompts and model choices: when a prompt or a model tier is uncertain, evaluate candidates against the eval suite before committing.
- Errors and failures: treat a failure as a fork, explore likely causes and fixes, do not abandon at the first dead end.

In every sphere the pattern is the same: name the options, set the deciding criteria, try them minimally and recoverably, measure, choose, and keep the rejected paths logged so they can be revisited.

## Error and failure recovery loop

When something fails, an error, a failing test, a broken build, a tool that does not work, a model output that does not validate, do not stop at the first failure and do not hide it. Run this loop:

1. Capture the failure precisely: the exact error, the context, and how to reproduce it. Journal it.
2. Form two or three hypotheses for the cause, ordered by likelihood.
3. Try the most likely fix on a branch. If it resolves and passes the gates, keep it.
4. If it does not, try the next hypothesis. Keep attempts bounded, usually three.
5. If hypotheses are exhausted, try a different approach or a different tool entirely, as an exploration with its own branch.
6. If it still fails after the cap, stop on this item, journal everything tried and why each failed, mark the task blocked with the evidence, and either reserve it or escalate per the chosen oversight level. Move on to unblocked work so the run continues.

Rules during recovery:
- Never suppress or skip a test to make a failure disappear.
- Never hide an error or fake a success.
- Every attempt is journaled, including the ones that failed, so the path is recoverable and the next session does not repeat dead ends.
- Recovery respects the data boundary, the model budget, and the attempt cap.
