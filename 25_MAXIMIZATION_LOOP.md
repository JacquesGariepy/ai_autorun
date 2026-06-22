# Maximization Loop

This file defines the continuous improvement loop and what maximum means, so the agent knows when to keep going and when to stop.

## The loop

Discover, audit, plan, implement a proven batch, validate, score, reprioritize, repeat. Each pass compounds small proven improvements. Real quality is reached by many validated steps, not by one large change.

The loop has two fuels: fixing what exists, and creating what is missing. When the corrective backlog runs dry, the loop does not stop, it switches fuel and regenerates new work from similar projects research, the completeness matrix, the opportunity list, and feature generation. Maximization means pushing both quality and capability, not only cleaning the current code. An empty marker sweep is a signal to regenerate, not to halt.

## The quality bar the project aims for

A maximized project, where applicable to its category, reaches a strong bar on every axis:
- Correctness: core behavior proven by tests, no fake or mocked feature presented as real.
- Tests: meaningful coverage of the critical paths, including edge cases.
- Security: untrusted input validated, secrets handled properly, top risks mitigated.
- Privacy and governance: sensitive data handled correctly, boundaries enforced.
- Performance: no obvious waste on the hot path, acceptable behavior under real load.
- Reliability: known failure modes handled, no silent wrong results.
- Maintainability: no needless duplication, no dead code, clear structure.
- Documentation: the README reflects code reality, install and usage are accurate.
- User experience: the main workflow is smooth, errors are clear.
- Accessibility and internationalization, where the category expects them.
- Observability: enough logging and signals to diagnose a production issue.
- Packaging and release: a stranger can install and run it, with a rollback path.

## Definition of maximum (stop the loop when all hold)

- All P0 and P1 tasks are done with proof.
- The release readiness go criteria are met.
- Remaining tasks are P2 or lower, and adding one no longer changes the scorecard meaningfully.
- No fake, mocked, or hardcoded feature is presented as real.
- Security, privacy, and cost controls are in place.

Diminishing returns is a real stop. When the next batch would cost more than the value it proves, the project is at its practical maximum. Stop, report, and reserve anything genuinely hard for a frontier window.

## Anti gaming rules

- A task counts as done only with proof. No proof, not done.
- The scorecard measures proven quality, not effort or output length.
- Do not inflate the backlog with low value busywork to appear productive. Value times provability decides priority.
- The anti busywork rule forbids emitting useless or un-wired code. It does not forbid designing and implementing genuinely new, provable features. When the corrective backlog is empty, generating valuable new features is the work, not busywork.
