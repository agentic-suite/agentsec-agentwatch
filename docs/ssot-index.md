# SSOT Index — one owner per shared contract

**BLUF:** Every shared schema/contract in the `agentic-suite` ecosystem has exactly **one owning repo** and
**one source file**. All other repos **consume** it. There are no parallel registries and no forked schemas —
duplicated contracts were the single biggest failure mode found in the code analysis (3 cost ledgers, 3 trace
schemas, 3 tool registries, 2 OPA integrations).

Source of truth for the decision: ecosystem `strategy/03-ssot-ownership.md` (runbook
[228](https://github.com/deghosal-2026/my-2nd-brain)).

## Contracts → owning repo/file

| Contract | Owning repo | Source file | Consumers |
|---|---|---|---|
| **Security-event schema** | `agentsec-agentwatch` | `schema/security-event.schema.json` | all ecosystems |
| **OTel `gen_ai.*` + run-health (`gen_ai.agent.*`)** | `agentsec-agentwatch` | `packages/python-sdk/src/agentsec_agentwatch/semconv.py`, `spans.py` | agentops, agentplane, agentforge, devops |
| **Policy engine** | `agentsec-agentpolicy` | `agentpolicy` (ported from `agent-tooltrust`) | agentmesh, agentplane |
| **Capability + policy-binding schema** | `agentmesh-fabric` | `Capability` / `CapabilityMapping` model | agentplane |
| **Workload / budget / permission / certification schema** | `agentplane-hiveplane` | `core/` (`workload.py`, `spec.py`, `certification/models.py`, `auth/rbac.py`) | agentops (budget), agentmesh |
| **Trajectory + eval + standing-rule schema** | `agentforge-cauterule` | `models/trajectory.py` (richest of 3) | agentsec (evidence), agentops (replay) |
| **Paved-road + release-evidence schema** | `devops-guardian` | `guardian-policy.yml` | agentsec (policy checks) |
| **Template + org governance** | `agentic-suite/template`, `agentic-suite/.github` | — (parent) | all ecosystems |
| **Agent-record schema** (records) | `agentsec-agentwatch` | `schema/agent-record.schema.json` | agentsec (evidence) |

## Duplications to collapse (code-verified)

| Duplication | Where | Collapse to |
|---|---|---|
| Cost ledgers × 3 | `agentops-loopguard`, `agentops-tierforge`, `agentops-incident` | one shared cost model (agentsec run-health) |
| Escalation events × 2 | `agentops-loopguard`, `agentops-tierforge` | one event type |
| Trace/trajectory schemas × 3 | `agentsec-agent-eval-forge`, `agentforge-self-edit`, `agentforge-cauterule` | CauterRule's trajectory |
| MCP tool registries × 3 | `agentmesh-fabric`, `agentmesh-mcplex`, `agentsec-agent-tooltrust` | one capability schema |
| OPA integrations × 2 | `agentmesh-fabric` (HTTP), `agentsec-agent-tooltrust` (subprocess) | `agentsec-agentpolicy` |
| GitHub API clients × 5 | devops members | one shared client |
| OMLX/OpenAI clients × 4+ | agentops + devops | one provider-agnostic client |

## Enforcement

- A contract may only be **modified** in its owning repo; consumers open issues there.
- This index links every contract to its **owner + source file**.
- Quarterly review re-checks that no second implementation has appeared.
