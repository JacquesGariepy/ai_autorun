# Backlog Triage Prompt

Read all sources of work:
- features.csv
- issues
- TODO/FIXME/HACK/WIP markers
- code comments
- README promises
- bugs visible in code
- failing tests
- build errors
- runtime errors
- unfinished features
- hardcoding
- security findings
- privacy findings
- documentation gaps
- AI/model findings
- release readiness gaps

Produce one normalized backlog.

Rules:
1. P0 before P1 before P2.
2. Technical dependencies before dependent features.
3. Blocking bugs before improvements.
4. Critical tests before refactors.
5. High-impact, low-risk changes first.
6. Large refactors must be isolated.
7. Ambiguous tasks remain blocked.
8. Non-provable tasks cannot be done.
9. AI/model tasks must include model policy and cost constraints.
10. Remote model tasks must be blocked if sensitive data handling is unclear.

Output:
| order | id | title | source | priority | dependencies | risk | effort | likely files | model policy | done criteria |
