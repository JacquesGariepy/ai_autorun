#!/usr/bin/env python3
"""Validate the AI work package: required files present and all JSON parses."""
import json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

required = [
    "00_MASTER_PROMPT.md",
    "01_PROJECT_INTAKE.md",
    "16_FRONTIER_BURST_PROTOCOL.md",
    "17_FRONTIER_QUESTION_BANK.md",
    "18_MODEL_ARRIVAL_CHECKLIST.md",
    "19_CAPTURE_AND_FREEZE.md",
    "20_SESSION_HANDOFF.md",
    "21_DATA_BOUNDARY_AND_GOVERNANCE.md",
    "22_QUICKSTART.md",
    "MEGAPROMPT.md",
    "AUTORUN.md",
    "AUTORUN_MAX.md",
    "23_TASK_SOURCE_DISCOVERY.md",
    "24_SIMILAR_PROJECTS_RESEARCH.md",
    "25_MAXIMIZATION_LOOP.md",
    "26_GIT_GITHUB_WORKFLOW.md",
    "27_ROLE_ORCHESTRATION.md",
    "28_PREFLIGHT_AUTOCONFIG.md",
    "29_EXPLORATION_AND_SPIKES.md",
    "30_OVERSIGHT_AND_JOURNALING.md",
    "git/PULL_REQUEST_TEMPLATE.md",
    "git/CODE_REVIEW_CHECKLIST.md",
    "GLOSSARY.md",
    "package-manifest.json",
    "model-management/model-registry.template.json",
    "model-management/routing-policy.template.json",
    "model-management/budget-policy.template.json",
]

errors = []

for rel in required:
    if not os.path.isfile(os.path.join(ROOT, rel)):
        errors.append("Missing required file: " + rel)

for dirpath, _, files in os.walk(ROOT):
    for name in files:
        if name.endswith(".json"):
            path = os.path.join(dirpath, name)
            try:
                json.load(open(path))
            except Exception as exc:
                errors.append("Invalid JSON in " + os.path.relpath(path, ROOT) + ": " + str(exc))

if errors:
    print("VALIDATION FAILED")
    for e in errors:
        print(" - " + e)
    sys.exit(1)

print("Package valid: required files present, all JSON parses.")
