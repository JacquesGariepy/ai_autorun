# Model Arrival Checklist

Run this the moment a new or more powerful model becomes available. It takes a few minutes and prevents the two classic mistakes: trusting a model you have not bounded, and burning a scarce window on the wrong work.

## Step 1: Identify

- [ ] Model name and version recorded.
- [ ] Training knowledge cutoff recorded.
- [ ] Provider and access method recorded (API, app, local).
- [ ] Whether availability is stable or a limited window. If limited, treat it as ephemeral and follow the Frontier Burst Protocol.

## Step 2: Probe the limits

- [ ] Maximum input context size confirmed.
- [ ] Maximum output size confirmed.
- [ ] Tool access confirmed by actual test: web, code execution, file reading, image input. Do not assume, verify with one call each.
- [ ] Determinism behavior noted (stable at temperature 0 or not).
- [ ] Refusal and partial refusal boundaries noted, so you do not discover them mid task.

## Step 3: Set the boundary

- [ ] Data boundary applied from `21_DATA_BOUNDARY_AND_GOVERNANCE.md`.
- [ ] Confirmed what may and may not be sent to this model.
- [ ] Redaction step ready if the model is remote.

## Step 4: Set the budget and limits

- [ ] Per request, per batch, per day limits set from `model-management/budget-policy.template.json`.
- [ ] Rate limit and retry policy set from `model-management/rate-limit-policy.template.json`.
- [ ] Stop conditions reviewed.

## Step 5: Qualify the model

- [ ] Run the standard evaluation from `model-management/eval-suite.template.json`.
- [ ] Score recorded. Below threshold means do not promote this model for high risk work.
- [ ] Decide the tier for this model: local, small, standard, or reasoning, or a new frontier tier.

## Step 6: Record the decision

- [ ] Create a Model Decision Record in `model-management/decision-records/` using the template. Capture: which tasks this model is now approved for, which it is forbidden for, its cost class, and its fallback.
- [ ] Update `model-management/model-registry.template.json` with the new model entry and status.

## Step 7: Decide how to spend the window

- [ ] If this is a frontier model with uncertain availability, open `16_FRONTIER_BURST_PROTOCOL.md` and run the waves in order.
- [ ] If this is a stable new default, route normal work to it per the routing policy and reserve frontier waves for genuinely hard problems only.

## Quick capability sheet to fill

```
Model:
Version:
Knowledge cutoff:
Max input context:
Max output:
Tools available:
Determinism:
Known refusals:
Availability (stable or window):
Approved tiers:
Forbidden tasks:
Eval score:
Fallback model:
Date assessed:
```
