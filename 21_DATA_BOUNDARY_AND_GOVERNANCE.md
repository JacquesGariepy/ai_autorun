# Data Boundary and Governance

Apply this before any call to a remote model. The faster and more capable a model is, the greater the temptation to feed it everything. That temptation is the risk. A single window of high productivity is not worth a data incident.

## The core rule

Classify before you send. Nothing leaves the machine until it has been classified and, if needed, redacted. When in doubt, keep it local.

## Data classes

- Public: open source code, public documentation. Remote models allowed.
- Internal non sensitive: project code with no secrets or personal data. Remote allowed if policy permits, after a quick scan.
- Sensitive: personal data, client data, credentials, keys, proprietary algorithms, anything under confidentiality obligations. Remote forbidden unless redacted and explicitly approved.
- Restricted: government, regulated, or contractually confidential data. Local or approved private deployment only. Never to a general remote model.

## The redaction step

Before any remote call on internal or higher data:
1. Remove secrets, tokens, keys, connection strings, and credentials.
2. Replace personal data with placeholders.
3. Replace client and project identifiers with neutral names.
4. Remove anything that, combined with public knowledge, would identify a person or a confidential system.
5. Keep enough structure that the model can still help.

If redaction would remove so much that the question becomes meaningless, that is a signal to use a local model instead.

## Remote versus local decision

Use a local model when:
- The data is sensitive or restricted.
- The task is a secret scan or a private audit.
- You are offline or under a strict confidentiality obligation.
- The task is cheap and mechanical, where a local model is enough.

Use a remote model when:
- The data is public or safely redacted.
- The task needs reasoning depth a local model cannot provide.
- The budget and policy allow it, and the boundary has been applied.

## Governance note for Quebec and Europe

If your project handles personal data of people in Quebec or the European Union, two regimes are likely in play.

- Quebec Law 25 imposes obligations on the collection, use, communication, and retention of personal information, including consent, purpose limitation, and breach handling. Sending personal information to a remote model can count as a communication of that information to a third party. Treat it accordingly.
- The GDPR imposes parallel obligations for data subjects in the European Union, including lawful basis, data minimization, and restrictions on transfers.

Practical consequences for this package:
1. Do not send personal or confidential information to a general remote model without a documented basis and approval.
2. Prefer local or approved private deployment for anything touching regulated data.
3. Record the decision: what data, which model, why it was allowed, who approved it. Use a Model Decision Record.
4. Keep logging minimal so you do not create a new store of personal data while trying to be careful.

This note is operational guidance for handling data in this workflow, not legal advice. For a regulated or government project, confirm the specifics with the person or team responsible for compliance.

## Enforcement checklist

- [ ] Data classified.
- [ ] Redaction applied where required.
- [ ] Remote call only on public or safely redacted data.
- [ ] Sensitive and restricted data kept local.
- [ ] Decision recorded for any borderline case.
