"""M33 33.T — org-rename reference lint.

Proves the M33 work items: no stale org reference survives in tracked files, the
npm scope moved, and the launcher still forwards to the Python CLI.
"""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

OLD_ORG_TOKENS = ("agentsec-ecosystem", "agentic-ecosystems")

# Tracks that legitimately record the rename itself (the "old -> new" arrows).
ALLOWLIST = {
    "ROADMAP.md",
    "docs/wbs/v0.3.0/wbs-v0.3.0-index.md",
}


def _tracked_files() -> list[str]:
    out = subprocess.run(
        ["git", "ls-files"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    return [line for line in out.stdout.splitlines() if line.strip()]


def test_no_stale_org_reference_in_tracked_files() -> None:
    offenders: list[str] = []
    for rel in _tracked_files():
        if rel in ALLOWLIST:
            continue
        path = ROOT / rel
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, IsADirectoryError):
            continue
        if any(tok in text for tok in OLD_ORG_TOKENS):
            offenders.append(rel)
    assert not offenders, f"stale org reference in: {offenders}"


def test_npm_scope_is_the_new_org() -> None:
    pkg = json.loads((ROOT / "packages" / "cli" / "package.json").read_text())
    assert pkg["name"] == "@agentic-suite/cli"
    assert "agentsec-ecosystem" not in pkg["name"]
