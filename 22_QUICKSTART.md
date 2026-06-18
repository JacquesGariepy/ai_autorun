# Quickstart: a powerful model just became available

A ten minute runbook. Follow it top to bottom. Detailed files are referenced at each step.

## Minute 0 to 2: bound the model

Open `18_MODEL_ARRIVAL_CHECKLIST.md`. Run Wave 0 of `16_FRONTIER_BURST_PROTOCOL.md` to get the capability sheet. Now you know what you are working with.

## Minute 2 to 3: set the boundary

Open `21_DATA_BOUNDARY_AND_GOVERNANCE.md`. Decide what may be sent. Redact if remote. Confidential and government data stays local.

## Minute 3 to 4: set the budget

Apply `model-management/budget-policy.template.json` and `rate-limit-policy.template.json`. Set the stop conditions.

## Minute 4 to 9: run the burst

Run the waves of `16_FRONTIER_BURST_PROTOCOL.md` in order:
1. Ground truth report.
2. Architecture decisions.
3. The hardest problem, solved with an oracle.
4. The frozen autonomous plan.
5. The omissions sweep.

Save a file after every wave. Do not collect conversation, collect files.

## Minute 9 to 10: freeze and hand off

Open `19_CAPTURE_AND_FREEZE.md` and confirm every artifact is saved and stamped. Update `20_SESSION_HANDOFF.md`. Run the autonomy test. If it passes, you can lose the model safely and let cheaper models finish.

## The one rule if you only remember one thing

Use the strong model to decide, to prove, and to write the oracle. Freeze the result into files. Let cheap models type.

## If you have only two minutes, not ten

Paste this single prompt and demand files:

```
My access to you may be brief. Given my codebase and goal below, produce, as saved files, in this order until you run out of room:
1. The true architecture and the top five risks, cited to files.
2. The architecture decisions that are expensive to reverse, each as a short decision record with a recommendation.
3. The hardest problem solved, with a reference implementation and the acceptance tests any solution must pass.
4. A dependency ordered backlog where each task has acceptance criteria and an assigned model tier, so a weaker model can finish without you.
5. The five questions I should have asked but did not.
Codebase and goal: [PASTE]
```
