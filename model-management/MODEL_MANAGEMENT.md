# Model Management

The project must manage AI models like production dependencies.

The AI agent must never treat a model as a magic default.

It must control:
- provider
- model
- task type
- context sensitivity
- cost
- token budget
- rate limits
- fallback
- output schema
- evaluation score
- prompt version
- privacy rules
- logging

## Model Tiers

### Local
Use for:
- sensitive code
- secrets scan
- private files
- offline analysis
- low-cost classification

### Small
Use for:
- formatting
- CSV cleanup
- simple documentation
- mechanical classification

### Standard
Use for:
- routine implementation
- code review
- test generation
- documentation

### Reasoning
Use for:
- architecture decisions
- complex debugging
- security review
- migration plans
- high-risk batches

## Routing Rules

Do not send sensitive data to remote models unless:
1. data is redacted
2. policy allows it
3. human approval is recorded

## Canary Rule

Before running a large batch:
1. run 1 to 3 prompts
2. validate output quality
3. validate schema
4. validate cost
5. continue only if gates pass

## Fallback Rule

Fallback is allowed only when:
- the original model is unavailable
- the fallback model is approved for the same data sensitivity
- the fallback model passes minimum eval score
- the model change is logged

## Cost Rule

Stop immediately if:
- batch budget is exceeded
- daily budget is exceeded
- projected cost exceeds allowed limit
- output quality is too low
