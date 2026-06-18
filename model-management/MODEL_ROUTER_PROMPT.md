# Model Router Prompt

Given a task, classify the correct model tier.

Input:
- task id
- task description
- files involved
- data sensitivity
- risk level
- required reasoning depth
- expected output
- budget limit

Return:
1. task type
2. data sensitivity
3. model tier
4. allowed providers
5. forbidden providers
6. max cost
7. max tokens
8. requires redaction: yes/no
9. requires human approval: yes/no
10. fallback model tier
11. reason

Rules:
- Use local model for sensitive data by default.
- Use cheapest sufficient model.
- Use reasoning model only for high complexity or high risk.
- Do not route secrets to remote models.
- Do not run high-cost models without budget check.
