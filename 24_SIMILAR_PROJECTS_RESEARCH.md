# Similar Projects Research

The goal is to learn what comparable and competing projects offer, then turn the difference into concrete backlog items, so the project reaches the standard of the best in its category and beyond.

## With web access

1. Identify the project category precisely, from the real code, not the README.
2. Search for comparable projects: established products, well regarded open source projects, and direct competitors in the same category.
3. For each comparable, extract: core features, the quality bar users expect, the architecture pattern, the documentation standard, the security and privacy posture, the packaging and onboarding experience, and any notable differentiator.
4. Compare against the current project's real state from the audits.
5. Produce a gap analysis and an opportunity list. Separate table stakes, the features expected by default, from differentiators, the features that would make this project stand out.

## Without web access

Do not invent current facts or pretend to have searched. Use general knowledge and the provided files only. Produce the same analysis at the level general knowledge allows, and mark every item as needing later verification once web access exists.

## Copyright and originality

- Learn patterns and capabilities. Do not copy code, text, or assets from other projects.
- Do not reproduce proprietary content. Describe a capability in your own words, then design an original implementation.
- Cite the source of a factual claim taken from the web, briefly, so it can be verified.

## Outputs

- SIMILAR_PROJECT_GAP_ANALYSIS.md: one row per pattern or capability, with the current gap, a recommended action, and a priority.
- FEATURE_OPPORTUNITY_LIST.md: features worth adding, with value, effort, risk, and priority.
- FEATURE_KILL_LIST.md: features worth removing because they add risk or maintenance without value.

## Turning research into tasks

Every gap and every opportunity that is worth doing becomes a task in the normalized backlog, with acceptance criteria and a proof requirement, exactly like tasks discovered in code. Research that does not become a provable task is noted but not counted as work.
