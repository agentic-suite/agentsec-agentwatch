# Runbook — Upgrade & Rollback

## Upgrade (v0.1.0 → v0.2.0 example)

```sh
pip install --upgrade agentwatch
agentsec-agentwatch migrate        # applies any store-format migration
agentsec-agentwatch status         # confirm recording
```

If a store-format change is breaking, `agentwatch migrate` emits a backup and a documented migration
(record-format spec §Versioning).

## Rollback

```sh
pip install agentsec-agentwatch==0.1.0
agentsec-agentwatch migrate --rollback    # restore the pre-migration store
```

## Uninstall

```sh
agentsec-agentwatch uninstall            # remove hooks, stop daemon
# optional: rm -rf ~/.local/share/agentwatch   # purge records
```

## Principle

Upgrades preserve records; rollbacks restore them. No silent format changes.
