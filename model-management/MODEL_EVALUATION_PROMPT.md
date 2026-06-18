# Model Evaluation Prompt

Evaluate the model response.

Score on 100:
- code grounding: /20
- no hallucination: /20
- correctness: /20
- actionability: /15
- safety/security: /10
- respects constraints: /10
- cost effectiveness: /5

Verdict:
- excellent
- usable
- partial
- dangerous
- rejected

Also identify:
1. unsupported claims
2. missing proof
3. risky recommendations
4. tasks requiring human review
5. whether this model should be used again for this task type
