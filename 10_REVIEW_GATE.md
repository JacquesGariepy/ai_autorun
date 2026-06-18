# Review Gate

A batch is rejected if any critical item fails.

Checklist:
- Code compiles.
- Tests pass or limitation is clearly explained.
- Acceptance criteria are covered.
- No new hardcoding.
- No new secret.
- No unrelated file modified.
- No out-of-scope refactor.
- Existing conventions respected.
- Names not changed unnecessarily.
- Errors handled.
- Logs do not expose sensitive data.
- Batch is logged.
- Proof matrix updated.
- CSV status updated only if proven.
- Model policy respected.
- Cost limit respected.
- Rate-limit policy respected.
- Output schemas validated.
- AI-generated outputs are not treated as truth without verification.

Verdict:
ACCEPTED / REJECTED / PARTIAL
