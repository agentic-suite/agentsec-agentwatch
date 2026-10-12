# Runbook — Install & Verify

Goal: record the first Claude Code tool call in ≤15 minutes and confirm it.

```sh
# install hooks + local daemon (monitor-only)
agentsec-agentwatch init      # or: pipx run agentsec-agentwatch init
# default scope is the project file .claude/settings.local.json;
# use `init --scope user` to install for all projects (~/.claude/settings.json)

# confirm recording is on
agentsec-agentwatch status

# use Claude Code normally, then:
agentsec-agentwatch sessions      # list recorded sessions
agentsec-agentwatch replay <id>   # reconstruct the timeline
```

## Verify

- [ ] `agentsec-agentwatch status` shows recording active.
- [ ] A tool call appears in `agentsec-agentwatch sessions` within the ingestion window.
- [ ] Redaction self-test passes before any export.

## Troubleshoot

- No session appears → check the hooks are installed and the daemon is running; recording must **fail
  closed**, never silently.
