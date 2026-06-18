# One Shot Context Prompt

Use this when giving the whole project to an AI agent.

You receive:
1. An existing codebase
2. The ai-work package
3. A CSV backlog
4. Project constraints
5. Model management policies

Mission:
Improve the project massively but progressively, with control and proof.

You must:
1. Read real code.
2. Ignore unproven README claims.
3. Map architecture.
4. Detect unfinished work.
5. Detect hardcoding.
6. Read all CSV tasks.
7. Add implicit tasks found in code.
8. Compare with similar project patterns.
9. Create a normalized backlog.
10. Prioritize.
11. Propose first batch.
12. Implement only first batch.
13. Add tests.
14. Validate.
15. Log execution.
16. Respect model routing, budget, fallback, and rate-limit rules.

You cannot mark a task done without proof.
