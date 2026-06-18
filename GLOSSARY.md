# Glossary

- Frontier model: the most capable model available to you at a given moment, possibly for a limited window.
- Burst: a short, high value session with a frontier model, run under the Frontier Burst Protocol.
- Oracle: the authoritative specification plus executable acceptance tests for a feature. It lets a weaker model verify its own work without the frontier model.
- Golden reference implementation: a correct, possibly slow, implementation of a hard component, used as a reference to test faster implementations against.
- Freeze: saving a frontier output as a named file with a status, so it becomes a durable authority rather than lost conversation.
- Frozen authority: a file accepted as the governing decision for a topic. A later model must justify a change through a new decision record, not a silent overwrite.
- Autonomy test: the check that a cheaper model, given only the frozen files and the codebase, could finish the backlog and prove each task done.
- Model tier: the routing level for a task, from local, to small, to standard, to reasoning, to a frontier tier.
- Proof: the evidence that a task is done, including files changed, tests added, commands run, and results.
- Canary: a small first run used to validate quality, schema, and cost before scaling a batch.
- Data boundary: the rule set for what may be sent to a remote model versus kept local.
