"""M34 identity & distribution guards (ADR-0026).

Proves the M34 work items: the target name is recorded, the compatibility shim
resolves, the migration guide exists, and the console scripts declare both the
new names and the v0.3.x legacy aliases.
"""

from __future__ import annotations

import importlib
import tomllib
from pathlib import Path

SDK = Path(__file__).resolve().parents[1]
REPO = Path(__file__).resolve().parents[3]


def test_adr_0026_records_the_target_name() -> None:
    text = (REPO / "docs" / "adr" / "0026-naming-decision.md").read_text(encoding="utf-8")
    assert "agentsec_agentwatch" in text
    assert "agentsec-agentwatch" in text


def test_migration_guide_exists() -> None:
    assert (REPO / "docs" / "release" / "v0.3.0" / "migration-guide.md").is_file()


def test_console_scripts_declare_new_and_legacy_names() -> None:
    data = tomllib.loads((SDK / "pyproject.toml").read_text(encoding="utf-8"))
    scripts = data["project"]["scripts"]
    assert scripts["agentsec-agentwatch"] == "agentsec_agentwatch.cli:main"
    assert scripts["agentsec-agentwatch-hook"] == "agentsec_agentwatch.hook:main"
    # v0.3.x legacy aliases keep the old CLI names working.
    assert scripts["agentwatch"] == "agentsec_agentwatch.cli:main"
    assert scripts["agentwatch-hook"] == "agentsec_agentwatch.hook:main"


def test_legacy_module_shim_resolves() -> None:
    assert importlib.import_module("agentwatch") is importlib.import_module(
        "agentsec_agentwatch"
    )
