# Oversight and Journaling

This runs once, at the very start, before preflight. It is the single setup interaction. The agent asks the human how much oversight they want and confirms journaling, then runs autonomously according to that choice. If the human does not answer within a short moment, the agent applies the safe defaults below and proceeds, so nothing blocks forever.

## The initial questions (ask once, then proceed)

1. Human in the loop, yes or no. Do you want to be involved during the run, or should the agent run fully autonomously and report at the end.

2. If yes, the oversight level:
   - L1 Checkpoints: pause at phase boundaries, before merging to main, and before any remote action.
   - L2 Batch approval: approve each batch plan before it is implemented.
   - L3 Step approval: approve each significant action. Most hands on.

3. Information type: what to surface.
   - Decisions only.
   - Decisions and risks.
   - Everything, including tool calls and explorations.

4. Information verbosity:
   - Silent: only checkpoints and the final report.
   - Summary: a short note per batch.
   - Detailed: per step notes.
   - Verbose: a full trace.

5. Journaling: confirm that the agent keeps a complete, append only journal of everything it undertakes. Default is yes. The journal is separate from the chat and survives the session.

## Standing approval overrides the default

If the launch instruction grants standing approval to proceed through every phase and every batch without asking, that sets oversight to L0 fully autonomous. In L0 the agent does not pause at phase boundaries and does not treat planning as a stopping point. It runs end to end and reports at the finish. The only pauses are the hard safety stops. Do not downgrade L0 to L1 on your own; standing approval means autonomous.

## Safe defaults if unanswered

- Human in the loop: on, at L1 Checkpoints, ONLY if the launch did not grant standing approval. If standing approval was granted, default to L0 fully autonomous and run end to end.
- Information type: decisions and risks.
- Verbosity: summary.
- Journaling: on, full.

These defaults give autonomy with a safety net, and can be changed at any checkpoint by the human saying so. The agent records the chosen settings in reports/ENV_PROFILE.md.

## Changing the settings mid run

The human can change oversight or verbosity at any time with a plain instruction, for example raise to L2, drop to silent, or go fully autonomous. The agent applies it from the next step and notes the change in the journal.

## The journal

The agent maintains JOURNAL.md as an append only record of everything it undertakes. It is the master narrative that ties together the other logs. Each entry has: a timestamp, the role acting, the action, the reason, the inputs and outputs or file refs, the tool used, the result, and any error. Explorations, tool choices, errors, and recoveries are all journaled, not only successes.

The journal complements, it does not replace, the focused logs: execution-log.md for batches, the proof matrix for proof, the decision log and ADRs for decisions, and EXPERIMENT_LOG.md for explored paths. The journal references those by id so the full story is reconstructable.

Journaling rules:
- Append only. Never rewrite history to look cleaner.
- Record failures and dead ends honestly. A hidden error is worse than a logged one.
- Never write secrets or sensitive data into the journal. Reference redacted artifacts instead.
- Stamp each entry with the model name and version in effect.

## Relationship to autonomy

This file decides how visible and how interactive the run is. It does not lower the safety boundaries. Regardless of the chosen level, the agent still pauses at the hard safety stops: sensitive data leaving the machine, a remote action without granted permission, a budget breach, an unrecoverable failure, or an expensive irreversible decision with no covering record.
