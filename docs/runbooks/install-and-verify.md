# Runbook — Install & Verify

Goal: record the first Claude Code tool call in ≤15 minutes and confirm it.

```sh
# install hooks + local daemon (monitor-only)
npx @agentic-suite/cli init      # or: pipx run agentwatch init
# default scope is the project file .claude/settings.local.json;
# use `init --scope user` to install for all projects (~/.claude/settings.json)

# confirm recording is on
agentsec-agentwatch status

# use Claude Code normally, then:
agentsec-agentwatch sessions      # list recorded sessions
agentsec-agentwatch replay <id>   # reconstruct the timeline
```

## Verify

- [ ] `agentwatch status` shows recording active.
- [ ] A tool call appears in `agentwatch sessions` within the ingestion window.
- [ ] Redaction self-test passes before any export.

## Troubleshoot

- No session appears → check the hooks are installed and the daemon is running; recording must **fail
  closed**, never silently.
