# Prompt Versioning

Every production prompt must have:
- prompt id
- version
- owner
- purpose
- input variables
- output schema
- allowed models
- risk level
- eval cases
- changelog

Prompt changes must be treated like code changes.

A prompt cannot be considered stable unless:
1. it has an output schema
2. it has regression examples
3. it has bad-case examples
4. it has cost expectations
5. it has a fallback behavior
