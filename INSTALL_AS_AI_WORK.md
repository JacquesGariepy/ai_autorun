# Install and trigger

## Install, without creating a double nested path

When you unzip, you get a folder containing the files. Place it in your repo, for example at <repo>/ai-work, so that AUTORUN.md sits directly inside it:

```
<repo>/ai-work/AUTORUN.md
<repo>/ai-work/16_FRONTIER_BURST_PROTOCOL.md
...
```

Do not nest it twice. You should never end up with <repo>/ai-work/ai-work/AUTORUN.md. The folder name does not matter, because every file inside resolves its references against its own folder. Only the location of AUTORUN.md matters, because that is the one path you give the agent.

## The trigger

Give the agent the real path to AUTORUN.md and nothing else about paths. AUTORUN.md handles its own path resolution.

```
Execute AUTORUN.md at ./ai-work/AUTORUN.md. You have my standing approval to
proceed through every step without asking me between steps. Stop only on the
stop conditions defined in the file. Produce saved files, not conversation.
```

Replace ./ai-work/AUTORUN.md with wherever you placed it. That single path is the only thing you need to provide.

## Steady state work, not a burst

For ordinary disciplined work instead of a frontier burst, point the agent at 00_MASTER_PROMPT.md in the same folder and follow its initial phase.

## One shot, no file access

If the agent cannot read your files, use MEGAPROMPT.md: paste its content plus your codebase and goal. It returns the artifacts in the conversation for you to save yourself.

## Maximization mode, push the project to its maximum

To discover every task, audit, research comparable projects online, plan, and then implement in a proven loop until the project reaches its practical maximum, point the agent at AUTORUN_MAX.md instead of AUTORUN.md:

```
Execute AUTORUN_MAX.md at ./ai-work/AUTORUN_MAX.md. You have my standing approval
to proceed through every phase and every batch without asking me between steps.
Stop only on the stop conditions defined in the file. Produce saved files and
working code with proof, not conversation.
```

Replace the path with wherever you placed it. Use this when you want the full build, not just the analysis. The burst trigger AUTORUN.md remains the right choice for a short window with a very capable model, where you want decisions, the hardest problem, and the oracle, fast.

## Git, GitHub, and the team workflow

In maximization mode the agent works like a coordinated team and follows Git and GitHub best practices: one branch and pull request per batch, conventional commits, code review and quality gates, required CI checks, and protected main. See 26_GIT_GITHUB_WORKFLOW.md and 27_ROLE_ORCHESTRATION.md, and the git/ folder for the branching strategy, commit convention, pull request template, review checklist, and an example CI workflow.

Remote actions, pushing, opening or merging pull requests, and tagging releases, happen only if your environment grants the agent repository permissions. Without them, the agent does all the work locally on branches and prepares the pull request content for you to push. It never commits to main directly, never force pushes shared history, and never commits secrets.
