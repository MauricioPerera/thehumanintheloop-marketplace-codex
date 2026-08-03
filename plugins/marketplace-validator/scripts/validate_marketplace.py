#!/usr/bin/env python3
"""Validate the shared Claude Code/Codex marketplace layout."""
import argparse, json, re, sys
from pathlib import Path

def load(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise ValueError(f"Invalid JSON: {path}: {exc}")

def validate_skill(skill_path, errors):
    lines = skill_path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        errors.append(f"Skill missing frontmatter: {skill_path.relative_to(skill_path.parents[3])}")
        return
    try:
        end = lines[1:].index("---") + 1
    except ValueError:
        errors.append(f"Skill frontmatter not closed: {skill_path}")
        return
    frontmatter = "\n".join(lines[1:end])
    name_match = re.search(r"^name:\s*['\"]?([^'\"\n]+)", frontmatter, re.MULTILINE)
    description_match = re.search(r"^description:\s*['\"]?(.+?)['\"]?$", frontmatter, re.MULTILINE)
    if not name_match:
        errors.append(f"Skill frontmatter missing name: {skill_path}")
    elif name_match.group(1).strip() != skill_path.parent.name:
        errors.append(f"Skill name does not match directory: {skill_path}")
    if not description_match or not description_match.group(1).strip():
        errors.append(f"Skill frontmatter missing description: {skill_path}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    errors = []
    claude_path = root / ".claude-plugin" / "marketplace.json"
    codex_path = root / ".agents" / "plugins" / "marketplace.json"
    if not claude_path.exists(): errors.append(f"Missing {claude_path.relative_to(root)}")
    if not codex_path.exists(): errors.append(f"Missing {codex_path.relative_to(root)}")
    manifests = []
    for path in (claude_path, codex_path):
        if path.exists():
            try: manifests.append(load(path))
            except ValueError as exc: errors.append(str(exc))
    names = []
    category_maps = []
    for manifest in manifests:
        entries = manifest.get("plugins", [])
        names.append({entry.get("name") for entry in entries})
        category_maps.append({entry.get("name"): entry.get("category") for entry in entries})
        for entry in entries:
            name = entry.get("name")
            source = entry.get("source")
            relative = source if isinstance(source, str) else (source or {}).get("path")
            if not name or not relative: errors.append("Every plugin entry needs name and source/path")
            elif not (root / relative).is_dir(): errors.append(f"Plugin path does not exist: {relative}")
            else:
                plugin_root = root / relative
                if not (plugin_root / ".claude-plugin" / "plugin.json").exists(): errors.append(f"Missing Claude plugin manifest: {relative}")
                if not (plugin_root / ".codex-plugin" / "plugin.json").exists(): errors.append(f"Missing Codex plugin manifest: {relative}")
                skills = list((plugin_root / "skills").glob("*/SKILL.md"))
                if not skills: errors.append(f"Plugin has no discoverable skills: {relative}")
                for skill in skills: validate_skill(skill, errors)
    if len(names) == 2 and names[0] != names[1]: errors.append(f"Marketplace plugin mismatch: Claude={sorted(names[0])}, Codex={sorted(names[1])}")
    if len(category_maps) == 2 and category_maps[0] != category_maps[1]: errors.append(f"Marketplace category mismatch: Claude={category_maps[0]}, Codex={category_maps[1]}")
    if errors:
        print(json.dumps({"status": "FAILED", "errors": errors}, indent=2, ensure_ascii=False)); return 1
    print(json.dumps({"status": "PASSED", "plugins": sorted(names[0]) if names else []}, indent=2, ensure_ascii=False)); return 0

if __name__ == "__main__": sys.exit(main())
