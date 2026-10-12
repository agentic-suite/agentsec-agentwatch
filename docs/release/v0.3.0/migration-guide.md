# Migration Guide — v0.2.x → v0.3.0

**BLUF:** v0.3.0 is an **identity & structure** release — renames only, no new features. The package,
import module, CLI, and org/repo names move; the **PyPI distribution stays `agentsec-agentwatch`**. Every old
import path and old CLI name keeps working through a compatibility shim across the **v0.3.x** window. No store
format, record contract, or API-shape change.

Status: **release-ready** (v0.3.0). Preceded by the `agent-exec-trace` → `agentwatch` rename
([v0.1.0 guide](../v0.1.0/migration-guide.md)) and the org rename (`agentsec-ecosystem` → `agentic-suite`).

## The name chain

| Era | Distribution (PyPI) | Import module | CLI |
|---|---|---|---|
| ≤ v0.1.0 | `agent-exec-trace` | `agent_exec_trace` | `agent-exec-trace` |
| v0.1.0 – v0.2.x | `agentsec-agentwatch` | `agentwatch` | `agentwatch` |
| **v0.3.0+** | **`agentsec-agentwatch`** (unchanged) | **`agentsec_agentwatch`** | **`agentsec-agentwatch`** |

## What changes

| Area | v0.2.x | v0.3.0 | Breaking? |
|---|---|---|---|
| PyPI distribution | `agentsec-agentwatch` | `agentsec-agentwatch` | **no** |
| Import module | `agentwatch` | `agentsec_agentwatch` (`agentwatch` still works — shim) | no (shimmed) |
| Console scripts | `agentwatch`, `agentwatch-hook`, `agentwatch-daemon`, `agentwatch-mcp-proxy`, `agentwatch-a2a-proxy` | `agentsec-agentwatch`, `agentsec-agentwatch-hook`, … (**old names still work — aliases**) | no (aliased) |
| GitHub org | `agentsec-ecosystem` | `agentic-suite` | no (URLs redirect) |
| Repo | `agentwatch` | `agentsec-agentwatch` | no (URLs redirect) |
| Store format / record schema / read API / config keys | — | unchanged | no |

## Steps

1. **Upgrade the package** (distribution name is unchanged):

   ```sh
   pip install -U agentsec-agentwatch
   ```

2. **Move your imports** (optional — the `agentwatch` shim keeps the old path working):

   ```python
   # before
   from agentwatch import conformance
   from agentwatch.store import RecordStore
   # after
   from agentsec_agentwatch import conformance
   from agentsec_agentwatch.store import RecordStore
   ```

3. **Move your CLI invocations** (optional — the old names are aliased):

   ```sh
   agentsec-agentwatch verify-store      # was: agentwatch verify-store
   agentsec-agentwatch doctor
   ```

4. **Update URLs.** `github.com/agentsec-ecosystem/agentwatch` → `github.com/agentic-suite/agentsec-agentwatch`
   (old URLs 301-redirect). CI/badge/GHCR references move with the org.

5. **Leave the store alone.** No format change; open it directly and `agentsec-agentwatch verify-store` passes.

## Compatibility promises (v0.3.x window)

- `import agentwatch` and `from agentwatch.<submodule> import …` resolve to `agentsec_agentwatch` via a
  meta-path shim (`src/agentwatch/`), returning the **same module objects**.
- The legacy CLI names (`agentwatch`, `agentwatch-hook`, `agentwatch-daemon`, `agentwatch-mcp-proxy`,
  `agentwatch-a2a-proxy`) are declared as console-script aliases.
- The `agent_exec_trace` import path keeps working through its own shim (DD-12).
- The store format, record/schema contract, read-API shapes, and config keys are **unchanged**.
- The old org and repo URLs remain valid via GitHub redirects.

## Namesake note

`pip install agentwatch` still installs a **different, unaudited** project. Always install the
fully-qualified distribution `agentsec-agentwatch` (see the [namesake FAQ](../../reference/namesake-faq.md)).
