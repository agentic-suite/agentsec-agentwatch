# ISO/IEC 27001:2022 Annex A appendix

> A controls-mapping aid, not an audit opinion. Each row names an evidence
> command that exists.

## A.8.15 — Logging

| Control expectation | agentwatch feature | Evidence |
|---|---|---|
| Event logs record activities, exceptions, faults | Tool calls, denials, errors, security events, harness drift, compaction | `agentsec-agentwatch tail`, `agentsec-agentwatch search --outcome error` |
| Logs protected against tampering | Hash-chained append-only store; tombstones, never silent deletion | `agentsec-agentwatch verify-store` |
| Logs retained per policy | Configurable retention with a visible purge marker | `agentsec-agentwatch retention show` |
| Clock accuracy for logs | Clock-skew detection recorded as a health reason | `agentsec-agentwatch status` |

## A.8.16 — Monitoring activities

| Control expectation | agentwatch feature | Evidence |
|---|---|---|
| Monitor networks/systems for anomalous behavior | Deterministic drift signals and behavior fingerprints | `agentsec-agentwatch drift`, `agentsec-agentwatch sessions --group-by-behavior` |
| Analyze events and act | Coverage reconciliation against ground truth; secret-exposure tracing | `agentsec-agentwatch coverage`, `agentsec-agentwatch secrets` |
| Records of monitoring activities | The monitoring output is itself recorded | `agentsec-agentwatch replay <id>` |

## Not applicable / elsewhere

| Control | Note |
|---|---|
| A.8.16 change/upgrade monitoring | Manual process; agentwatch records the acting revision instead | `agentsec-agentwatch search`, `agentsec-agentwatch union` |
| Cryptographic key management | Signing keys only sign digests (W9); no encryption at rest (PRD 14) | `agentsec-agentwatch checkpoint export --sign` |
