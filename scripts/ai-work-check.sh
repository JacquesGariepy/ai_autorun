#!/usr/bin/env bash
set -euo pipefail

# Resolve the package root relative to this script, not to the caller's CWD.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

echo "AI Work Package Check"
echo "Package root: $ROOT"

required=(
  "00_MASTER_PROMPT.md"
  "16_FRONTIER_BURST_PROTOCOL.md"
  "17_FRONTIER_QUESTION_BANK.md"
  "18_MODEL_ARRIVAL_CHECKLIST.md"
  "19_CAPTURE_AND_FREEZE.md"
  "20_SESSION_HANDOFF.md"
  "21_DATA_BOUNDARY_AND_GOVERNANCE.md"
  "22_QUICKSTART.md"
  "AUTORUN.md"
  "AUTORUN_MAX.md"
  "26_GIT_GITHUB_WORKFLOW.md"
  "27_ROLE_ORCHESTRATION.md"
  "28_PREFLIGHT_AUTOCONFIG.md"
  "29_EXPLORATION_AND_SPIKES.md"
  "30_OVERSIGHT_AND_JOURNALING.md"
  "MEGAPROMPT.md"
  "03_FEATURES_BACKLOG_TEMPLATE.csv"
  "model-management/model-registry.template.json"
  "model-management/routing-policy.template.json"
  "model-management/budget-policy.template.json"
)

missing=0
for f in "${required[@]}"; do
  if [ ! -f "$ROOT/$f" ]; then
    echo "Missing: $f"
    missing=1
  fi
done

if [ "$missing" -ne 0 ]; then
  exit 1
fi

echo "AI work package structure looks valid."
