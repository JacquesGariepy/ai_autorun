# Autorun

This file makes the package self driving. Point an agent at this file and it runs the whole burst over your repository without asking you between steps. It only stops on the defined stop conditions.

## How paths work

Every file named in this document lives in the same folder as this file. Resolve each name against this file's own folder, and create any output folder such as reports, adr, or model-management inside that same folder if it does not exist.

For this to be automatic, the agent must have: read access to the repository, the ability to write files, and permission to proceed without confirmation between steps. If any is missing, fall back to the manual waves in 16_FRONTIER_BURST_PROTOCOL.md.

## What the agent must do, in order, without pausing for me

0a. Read 30_OVERSIGHT_AND_JOURNALING.md and run it first. Ask me once about human in the loop, the level, the information type and verbosity, and confirm journaling. If unanswered shortly, apply the safe defaults and proceed. Open JOURNAL.md and journal everything from here, including explorations, tool choices, errors, and recoveries.

0. Read 28_PREFLIGHT_AUTOCONFIG.md and run it first. Detect the environment, the stack, the Git host, the permission level, web access, available tools, and data sensitivity. Choose safe defaults for anything not detectable, record them in reports/ENV_PROFILE.md, and proceed without asking me for configuration.

1. Read 21_DATA_BOUNDARY_AND_GOVERNANCE.md. Classify the data. If anything sensitive, confidential, or government related would be sent to a remote model, do not send it. Keep that work local or mark it reserved. Never echo secrets.

2. Read 18_MODEL_ARRIVAL_CHECKLIST.md. In two lines, state your model, version, context limit, and available tools. Save a capability sheet under model-management/decision-records/.

3. Read 16_FRONTIER_BURST_PROTOCOL.md. Run waves 1 through 5 in order. After each wave, immediately save the named output file. Do not wait until the end.
   - Wave 1: reports/PRODUCT_REALITY_REPORT.md and ARCHITECTURE_MAP.md, every claim cited to files.
   - Wave 2: one adr/ADR-XX-title.md per decision that is expensive to reverse, each with a recommendation.
   - Wave 3: reports/SOLUTION_<name>.md plus oracle tests in the project test format, for the single hardest problem.
   - Wave 4: NORMALIZED_BACKLOG.md, FIRST_BATCH_PLAN.md, EXECUTOR_GUIDE.md, every task with acceptance criteria and an assigned model tier.
   - Wave 5: reports/OMISSIONS_AND_GAPS.md, the questions I should have asked but did not.

4. Stamp every saved file with your model name, version, date, and a status of draft.

5. Update 20_SESSION_HANDOFF.md so the next session can continue.

6. Run the autonomy test in templates/AUTONOMY_TEST.md. Report pass or fail. If fail, name the missing artifact and produce it.

7. Produce a final index: list every file you created, with one line each on what it contains, and give the absolute path of each so I can find them.

## Rules the agent never breaks

- Cite files for every claim. Mark anything unverified as unverified.
- Do not invent files or completed features.
- Do not implement the whole project as one unauditable change. Produce a verifiable plan and an oracle.
- Every remaining task must be provable by a weaker model. If not, mark it blocked or reserved and say why.
- Apply the data boundary before any remote call.

## Under full autonomy (L0), defer instead of asking

If running L0 fully autonomous, do not hand control back for risky or irreversible items. Record them in TODO_BLOCKED.md with evidence, options, and a recommended default, and continue. Present the consolidated list at the end. The list below are capability failures that end the run, not requests for a decision.

## Stop conditions (capability failures that end the run)

- A step would send sensitive, confidential, or government data to a remote model.
- A budget or rate limit from the model-management folder would be exceeded.
- A decision that is expensive to reverse is required and is not covered by an ADR you can write with confidence.
- The repository cannot be read, or files cannot be written.
- Five consecutive tool or model errors.

Outside these, do not stop and do not ask. Proceed to the end and report.

## After autorun

Everything is frozen in files. Route execution to the cheapest tier that passes the oracle, using EXECUTOR_GUIDE.md. Reserve any future frontier window for the next genuinely hard problem only.
