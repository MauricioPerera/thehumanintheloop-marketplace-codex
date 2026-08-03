#!/usr/bin/env python3
"""Run the complete local validation suite for the marketplace."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parents[1]
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
