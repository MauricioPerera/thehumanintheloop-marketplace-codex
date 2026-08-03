#!/usr/bin/env python3
"""Run the complete local validation suite for the marketplace."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    workflow_errors = []
    for workflow in (root / ".github" / "workflows").glob("*.yml"):
        content = workflow.read_text(encoding="utf-8")
        if "actions/checkout@v4" in content:
            workflow_errors.append(f"{workflow.name}: uses deprecated checkout@v4")
        if "actions/checkout@" in content and "FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true" not in content:
            workflow_errors.append(f"{workflow.name}: missing Node.js 24 opt-in")
    if workflow_errors:
        for error in workflow_errors:
            print(error, file=sys.stderr)
        return 1
    commands = [
        [sys.executable, "plugins/marketplace-validator/scripts/validate_marketplace.py", "."],
        [sys.executable, "scripts/validate_catalog_metadata.py"],
        [sys.executable, "scripts/validate_analysis_metadata.py"],
        [sys.executable, "scripts/validate_llms_catalog.py"],
        ["node", "--check", "docs/app.js"],
    ]
    for command in commands:
        print(f"$ {' '.join(command)}")
        completed = subprocess.run(command, cwd=root)
        if completed.returncode:
            return completed.returncode
    print("ALL VALIDATIONS PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
