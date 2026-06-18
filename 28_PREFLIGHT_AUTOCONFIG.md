# Preflight and Autoconfiguration

This step runs first, before any other work. Its job is to make the package self configuring, so the only thing a human provides is the path to the run file. The agent detects the environment, chooses safe defaults for everything it cannot detect, records the choices, and proceeds without asking. It asks a human only when a true safety boundary is reached, never for setup details.

Governing rule: detect what you can, default safely for what you cannot, record every assumption, and proceed. Do not stop to ask for configuration. A recorded assumption that can be corrected later is always preferred over a question that blocks the work.

This safe default rule applies to configuration and environment unknowns. It does not apply to genuine forks between viable technical approaches. For those, do not guess: explore the options in parallel and decide by evidence, per 29_EXPLORATION_AND_SPIKES.md. Default safely for setup, explore for real forks, never block to ask.

## What to detect, and how

Inspect the repository and environment directly. Do not ask the human for any of this.

### Operating system and shell
Detect from the environment. Choose command syntax accordingly. If unknown, assume a POSIX shell and note it.

### Language, stack, and toolchain
Detect from the files present: package.json means Node, requirements.txt or pyproject.toml means Python, a csproj or sln means .NET, pom.xml or build.gradle means Java, Cargo.toml means Rust, go.mod means Go, and so on. A repository may have several. Record all detected stacks.

### Build, test, lint, run commands
Derive from the stack and from scripts already defined in the project, for example the scripts section of package.json, a Makefile, a Taskfile, or CI files. If none exist, use the conventional commands for the detected stack from 11_TESTING_VALIDATION.md, and note that they are assumed.

### Version control and host
Run the local checks: is there a .git folder, what remotes exist, and what host do they point to. Map the remote to a host: GitHub, GitLab, Bitbucket, Azure DevOps, or self hosted. If there is no remote, operate in local only mode. If there is no git at all and this is a new project, initialize git locally with a sensible .gitignore and proceed local only.

### CI presence
Detect CI config: a .github/workflows folder, .gitlab-ci.yml, azure-pipelines.yml, or similar. If present, adapt to it. If absent, prepare a CI workflow from git/ci.example.yml but do not assume permission to enable it remotely.

### Remote permission level
Do not assume you can push or open pull requests. Probe gently and safely. If a read only or no credential situation is detected, operate in local mode: real branches, real commits, prepared pull request content, but no remote actions. Treat any remote write as requiring granted permission. When in doubt, stay local and record it.

### Web access
Test whether web access is available with one harmless request. If yes, the similar projects research in 24_SIMILAR_PROJECTS_RESEARCH.md runs fully. If no, it runs at the general knowledge level and marks items for later verification.

### Model and tool availability
Detect which tools you actually have: file read, file write, code execution, web, and which model tiers are reachable. Record them. If file write is unavailable, full autonomy is impossible; produce artifacts in the response and say so.

### Data sensitivity
Scan for signals of sensitive or regulated content: secrets and keys, personal data, and markers of confidential, client, or government context. If found, default to local only handling and apply 21_DATA_BOUNDARY_AND_GOVERNANCE.md. When unsure whether data is sensitive, treat it as sensitive.

### Project age
Detect whether this is an existing project with history or a new or empty one. For a new project, scaffold sensibly: initialize git, add .gitignore, a README, a basic structure for the detected or chosen stack, and a first CI workflow, then proceed.

## The defaults matrix

When something cannot be detected, use the safe default and record the assumption.

| Unknown | Safe default |
|---|---|
| OS or shell | POSIX shell, portable commands |
| Stack | Infer from files; if truly none, ask nothing, scaffold the simplest reasonable stack for the stated goal and record it |
| Build, test, lint commands | Conventional commands for the stack, marked assumed |
| Git host | Map from remote; if none, local only mode |
| Remote write permission | Assume none; local branches and prepared pull requests only |
| CI | Prepare config, do not enable remotely without permission |
| Web access | Test once; if unavailable, degrade research gracefully |
| Model tier | Cheapest sufficient tier; escalate only for hard or risky work |
| Data sensitivity | Treat as sensitive; local only until proven safe |
| Branch naming | Conventional types and scopes from the Git workflow |
| Versioning | Semantic versioning |

## Output

Write ENV_PROFILE.md under reports/ with: detected OS, stacks, commands, git host, remote permission level, CI status, web access, available tools, model tiers, data sensitivity, project age, and a list of every default assumed. This profile drives all later phases. Update it if detection improves mid run.

## After preflight

Proceed directly into the chosen run, AUTORUN.md for a burst or AUTORUN_MAX.md for maximization, using the profile. Do not return to the human for configuration. The only reasons to pause are the real safety boundaries: sensitive data leaving the machine, a remote action without granted permission, a budget breach, an unrecoverable error, or an expensive irreversible decision with no covering record.
