# NIST SP 800-92 (log management) appendix

> The operational shape of agentwatch's logs, mapped to NIST SP 800-92's
> log-management guidance. A companion aid, not an audit opinion.

| SP 800-92 area | agentwatch feature | Evidence |
|---|---|---|
| Log sources identified | Harness hooks, MCP interposition, SDK spans, ingested foreign traces | `agentsec-agentwatch inventory`, `agentsec-agentwatch union` |
| Log generation — sufficient detail | Tool calls, outcomes, approvals, boundaries, security events | `agentsec-agentwatch replay <id>` |
| Log storage — integrity | Append-only JSONL with a per-line hash chain | `agentsec-agentwatch verify-store` |
| Log rotation / retention | Configurable retention; tombstones preserve the chain | `agentsec-agentwatch retention apply` |
| Log protection — access control | Store directory `0700`, files `0600`; store-access records | `agentsec-agentwatch doctor` |
| Log analysis | Coverage reconciliation, drift signals, behavior grouping | `agentsec-agentwatch coverage`, `agentsec-agentwatch drift` |
| Log disposal | Purge/tombstone with a visible marker, never a silent delete | `agentsec-agentwatch purge --yes` |
| Log record format / interoperability | Published JSON schemas; OCSF/CloudEvents/CycloneDX export | `agentsec-agentwatch export-session <id> --format ocsf` |

## Limits

agentsec-agentwatch is local-first and per-installation; it is not a central SIEM. See
[forensic-soundness.md](../design/forensic-soundness.md) for what the chain does
and does not prove.
