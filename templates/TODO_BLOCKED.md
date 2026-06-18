# TODO Blocked

Items the autonomous run deferred instead of stopping to ask. The human reviews this at the end and decides. Each row is reserved, not lost, and recoverable.

| id | title | type (irreversible / security / data boundary / remote-permission / budget / gate-failure) | evidence (files) | options | recommended default | recover ref | status |
|---|---|---|---|---|---|---|---|

Rules:
- Nothing here was attempted in a way that cannot be undone.
- Each item has enough context for a human to decide quickly.
- When a human approves an item, it returns to the backlog with that decision recorded as an ADR if it is expensive to reverse.
