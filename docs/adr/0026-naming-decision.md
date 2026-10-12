# ADR-0026 — Naming decision (agentwatch)

- **Status:** accepted — **decision revised (2026-10-08): defer the full rename to v0.3.0; ship v0.2.0 under the
  current names + guardrails** (originally: full rename at v0.2.0, option D, 2026-10-05)
- **Decision:** **Keep `agentsec-agentwatch` as the import module and CLI for v0.2.0.** The v0.2.0 release ships under the
  existing `agentsec-agentwatch` distribution / `agentsec-agentwatch` import + CLI, protected by the guardrails below. The
  **full rename (option D) is deferred to v0.3.0**, where the target name is chosen and recorded. Rationale: the
  rename is a large, launch-blocking cross-cutting change (a shim + migration guide + a sweep of every
  doc/example/compatibility row + the npx launcher), and the guardrails already mitigate the supply-chain risk for
  v0.2.0. This is a **named carry-forward**, not a dropped decision.
- **Consequences (accepted):** *deferred with the rename* — when it lands (v0.3.0) it will break the shipped
  identity and ecosystem references and carry the highest cost: a migration guide, an alias/shim for
  `import agentwatch` and the `agentsec-agentwatch` CLI across the v0.3.x window, updates to every doc/example/compatibility
  row, and the npx launcher; every package version string must move together. For v0.2.0 the guardrails below carry
  the risk.
- **Context:** The name `agentsec-agentwatch` is used by five or more active projects, several in the exact category
  (`agentwatch-core`, `agentwatch-monitor`, `agentwatch-io` on PyPI; `@nicofains1/agentwatch` on npm;
  `sreerevanth/AgentWatch`; `dhanraj176/agentwatch`, a near-identical MCP-proxy recorder; plus a Berkeley CLTC
  research report titled "AgentWatch"). Our package is `agentsec-agentwatch`, but the import name and CLI are
  `agentsec-agentwatch`, so `pip install agentwatch` installs a different, unaudited project — a support and
  supply-chain-reputation risk. No trademark is held by us for "agentwatch" (verify; not legal advice).
- **Actions that happen regardless:** fully-qualified install in every doc example; a distribution-check
  warning in `--version`/`init`/`doctor` (detect the wrong package); an honest namesake FAQ.

## Decision recorded (2026-10-12, v0.3.0 — closes NAME-1)

The deferred target name is chosen. The ecosystem brand is `agentsec`; the tool keeps its
**ecosystem-prefixed** identity and drops the colliding bare name.

| Layer | Name |
|---|---|
| Distribution (PyPI) | **`agentsec-agentwatch`** *(unchanged — already ecosystem-prefixed)* |
| Import module | **`agentsec_agentwatch`** *(was `agentsec-agentwatch`)* |
| Console script | **`agentsec-agentwatch`** *(was `agentsec-agentwatch`)* |

**Availability (checked 2026-10-12):** PyPI `agentsec-agentwatch` is owned by us. `agentsec-agentwatch` remains
unpublishable (PyPI rejects it as too similar to `agent-watch`); `agentsec`, `agentsec-cli` are taken by
others. npm is not used (distribution is PyPI-only). No new PyPI reservation is required — the distribution
name is unchanged; only the import module and CLI move off the bare `agentsec-agentwatch`.

**Shim:** `import agentwatch` and the `agentsec-agentwatch` CLI stay working across the v0.3.x window (NAME-3).
**Migration guide:** `docs/release/v0.3.0/` (NAME-4).
