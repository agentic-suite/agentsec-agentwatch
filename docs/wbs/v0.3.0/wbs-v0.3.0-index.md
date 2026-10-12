# WBS — agentwatch v0.3.0 (Index)

**BLUF:** **v0.3.0 is the identity & structure release.** It (1) renames the GitHub org
`agentsec-ecosystem` → `agentic-suite`, (2) stands up the new ecosystem skeleton (parent profile, template,
governance, SSOT index), and (3) completes the deferred **ADR-0026** rename (distribution + import + CLI + npm
scope). Four milestones (**M33–M36**), every ticket with a deliverable, an acceptance seed, and a tracking issue.

> **Scope: renames and structure only — NO new features, NO bug fixes.** v0.3.0 changes names, scopes, and the org
> skeleton; it adds and fixes nothing else. Every ticket below is a rename, a structural move, or release process.

**Parent:** agentic-suite #209 · **Branch:** `release/v0.3.0` · **GitHub milestones:** #37–#40 · **Issues:** #500–#538.

## Standard milestone exit criteria (applies to EVERY milestone)

- [x] All tests pass (`make test`) — M33 gate run: python-sdk 2473 · api 53 · analytics 742 · repo guard 49
- [x] Coverage ≥ 95% (CI-enforced, no waivers) — SDK 95.25% · api 95.75% · analytics 96.28%
- [x] Lint strict clean — `ruff` zero violations; `mypy --strict` clean (401 + 14 + 58 files)
- [x] WBS updated — every ticket checked off; deferred items re-pointed (ORG-9 → M36)
- [x] Issues updated — every M33 ticket closed or re-pointed
- [x] All affected docs updated at close-out (SSOT index, `CHANGELOG.md`, `README.md`, `.github` governance)
- [x] Committed + pushed to `release/v0.3.0`; `security.yml` green on the pushed HEAD (fixed: it never parsed)

## Milestones

| M | Name | Tickets | GitHub # | Theme |
|---|---|---|---|---|
| **M33** | Org Rename & New Structure | ORG-1 … ORG-9 | #37 | `agentsec-ecosystem` → `agentic-suite`; skeleton; SSOT index |
| **M34** | Identity & Distribution (ADR-0026) | NAME-1 … NAME-7 | #38 | Distribution + import + CLI + npm scope rename; shim; migration guide |
| **M35** | Field Tests | FT-1 … FT-5 | #39 | Rename + distribution + fresh-install verification + **full functional regression** + **release-readiness test** |
| **M36** | Release Readiness | REL-1 … REL-6 | #40 | Scan, **all-docs sweep**, **dev.to article links**, tag, publish from the new org |

> **M35 (Field Tests) and M36 (Release Readiness) are always last.** Do not tag `v0.3.0` before M36.
> Every milestone also carries its `N.T` / `N.D` / `N.R` support tickets (listed per milestone below).

## Progress

> **Updated 2026-10-12.** Org handle landed as **`agentic-suite`** (the decided `agentic-ecosystems` was already
> taken on GitHub). Statuses below reflect that handle.

- ✅ **ORG-1** (#500) — org renamed `agentsec-ecosystem` → `agentic-suite`; repo URLs 301-redirect, branch rulesets,
  org 2FA, secret scanning/push protection verified.
- ✅ **ORG-2** (#501) — all 12 active repos prefixed `agentsec-*` (per `strategy/02` + runbook 228); `template`/
  `.github` unchanged; remotes, badges, CI updated.
- ✅ **ORG-4** (#503) — reference sweep complete; no `agentsec-ecosystem` left in build/CI/badges (only the
  intentional `old → new` arrows in this WBS + `ROADMAP.md`).
- ✅ **ORG-5** (#504) — `.github` profile README + ROADMAP/CONTRIBUTING/TRADEMARK/SECURITY updated to the new org.
- ⛔ **ORG-3** (#502) — **descoped**: npm is not used; distribution publishes to PyPI (`agentsec-agentwatch`),
  which is a PyPI concern, not an npm-scope migration. Closed as not planned.
- ✅ **ORG-6** (#505) — new skeleton: `template` + governance floor; **`agentsec-agentlens`** repo scaffolded
  (TS local-first trace debugger; scaffold only) with the security floor enabled.
- ✅ **ORG-7** (#506) — SSOT index: [`docs/ssot-index.md`](../../ssot-index.md) (contract → owning repo/file).
- ✅ **ORG-8** (#507) — live vault docs swept to `agentic-suite` (metrics, work schedule, MOCs, notes 209–221);
  historical journal entries + published articles left untouched.
- ⏭️ **ORG-9** (#508) — **deferred to M36** (#40): install verification runs against the PyPI publish (REL-3).
- ✅ **33.T** (#523) — org-reference lint test (`tests/test_org_reference_lint.py`) + npm-scope assertion.
- ✅ **33.D** (#524) — SSOT index, `CHANGELOG.md`, README/ROADMAP, `.github` profile/governance.
- ✅ **33.R** (#525) — review + risk sign-off recorded; exit gate green.

> **M33 complete (2026-10-12).** ORG-1/2/4/5/6/7/8 done · ORG-3 **descoped** (no npm) · ORG-9 **→ M36**.
> Exit gate green; `security.yml` CI fixed (it never parsed) and green on the pushed HEAD.

### M34 progress

- ✅ **NAME-1** (#509) — target name recorded in ADR-0026: distribution `agentsec-agentwatch` (unchanged),
  import `agentsec_agentwatch`, CLI `agentsec-agentwatch`. Availability checked.
- ✅ **NAME-2** (#510) — renamed import module `agentwatch` → `agentsec_agentwatch` and console scripts to
  `agentsec-agentwatch[-hook|-daemon|-mcp-proxy|-a2a-proxy]` (code, services, packaging, tests, hook contract).
- ✅ **NAME-3** (#511) — `agentwatch` compatibility shim (`import agentwatch` + legacy CLI aliases), v0.3.x window.
- ✅ **NAME-4** (#512) — migration guide at `docs/release/v0.3.0/migration-guide.md` (full name chain).
- ✅ **NAME-5** (#513) — live-doc sweep to `agentsec_agentwatch` / `agentsec-agentwatch`; historical records kept.
- ⛔ **NAME-6** (#514) — **descoped**: npm is not used (PyPI install path); no npx launcher deliverable.
- ✅ **NAME-7** (#515) — namesake guard detects the new module + legacy shim; wired into `--version`/`init`/`doctor`.
- ✅ **34.T** (#526) / **34.D** (#527) / **34.R** (#528) — tests / docs / review.

> **M34 complete (2026-10-12).** Gate run once: failures (analytics coverage omit, doc links, mutation inventory,
> npm launcher, org-lint allowlist, release-tooling path) fixed and re-verified with the specific failing tests;
> analytics coverage back to 96.11%.

### M35 progress

> **Updated 2026-10-12.** No code change in v0.3.0 → no v0.3.0 field-test plan and no field-test report. The
> existing field-test runner (`scripts/fieldtest/run-v020-all.sh`) is re-pointed to write results under
> `field-test/0.3.0/`.

- ⛔ **FT-1** (#516) — **descoped**: no v0.3.0 field-test plan (renames/structure only).
- ✅ **FT-2** (#517) — field tests executed with the existing runner; results under `field-test/0.3.0/results/`
  (committed as evidence). **No report** produced.
- ✅ **FT-3** (#518) — fresh-install cases in the suite passed (`FT-01`, `FT-01b`, `FT-ENV-0`).
- ✅ **FT-4** (#535) — full functional regression on the renamed build: **92 pass · 1 declared · 0 fail**.
- ✅ **FT-5** (#536) — release-readiness: end-to-end cases (install → record → export → replay → detectors →
  console) all passed.
- ✅ **35.T** (#529) / **35.D** (#530) / **35.R** (#531) — tests / docs / review.

> **M35 complete (2026-10-12).** Field run: 92 pass · 1 declared (`FT-XHT-2`, OpenCode binary absent — P/F|D by
> design) · 0 fail.

### M36 progress

- ✅ **REL-1** (#519) — security scan clean (gitleaks/trufflehog/pip-audit/egress); evidence committed.
- ✅ **REL-2** (#520) — CHANGELOG/README/compatibility/known-limitations to v0.3.0.
- ✅ **REL-3** (#521) — **released v0.3.0**: PyPI `agentsec-agentwatch 0.3.0`, tag `v0.3.0`, GitHub release
  (wheel+sdist+SBOM+checksums).
- ⏳ **REL-4** (#522) — launch article ("The Security-Event Schema Agents Need") — **external** (dev.to), not
  produced here.
- ✅ **REL-5** (#537) — full live-doc sweep to v0.3.0.
- ⏳ **REL-6** (#538) — update published dev.to article links — **external** (dev.to account).
- ✅ **ORG-9** (#508) — redirects + clean-machine install verified against the published package.
- ✅ **36.T** (#532) / **36.D** (#533) / **36.R** (#534) — tests / docs / review.

> **M36 (Release Readiness).** v0.3.0 released from `agentic-suite`. Remaining: REL-4/REL-6 (external dev.to
> content/link updates — not automatable here).

---

## M33 — Org Rename & New Structure · milestone [#37]

**Goal:** the org and its structure are renamed and rebuilt before anything ships.

| ID | Title | Deliverable | Acceptance | Issue |
|---|---|---|---|---|
| ORG-1 | Rename the GitHub org | `agentsec-ecosystem` → `agentic-suite` | Repo URLs redirect; branch rulesets, 2FA, secret scanning/push protection survive | #500 |
| ORG-2 | Repo naming — **ecosystem prefixes (decided 2026-10-11)** | Rename every repo to its ecosystem prefix (`agentsec-agentwatch`, `agentops-loopguard`, …) | Repos disambiguated by ecosystem; remotes/badges/CI updated | #501 |
| ORG-3 | npm scope migration | `@agentsec-ecosystem/*` → `@agentic-suite/*` | New scope published; old deprecated with redirect note | #502 |
| ORG-4 | Reference sweep | Badges, CI/CD URLs, GHCR image names, Codecov | No `agentic-suite` reference left in build/CI/badges | #503 |
| ORG-5 | Org profile + governance docs | `.github` profile, GOVERNANCE, TRADEMARK, install-UX | Docs reference the new org | #504 |
| ORG-6 | New skeleton | Parent profile + `template` + governance floor + **AgentLens project skeleton** — scaffold the repo (from `template` + governance) for the TypeScript local-first trace debugger (the `agent-inspect` equivalent; vault #235) under `agentsec`/`agentwatch`; **scaffold only — implementation is a later effort** | A new ecosystem can be stood up from the skeleton; the AgentLens repo is scaffolded (not built) | #505 |
| ORG-7 | SSOT index | Contracts → owning repo/file — [`docs/ssot-index.md`](../../ssot-index.md) | Every shared contract has one owner + link | #506 |
| ORG-8 | Live-doc sweep | Vault metrics/schedule/MOCs + notes 209/210–221 | Live docs updated; historical journal/articles untouched | #507 |
| ORG-9 | Verification | Redirects + clean-machine install | `npx @agentic-suite/cli init` works on a clean machine in ≤15 min | #508 |

**Support tickets:** 33.T [#523] · 33.D [#524] · 33.R [#525]

## M34 — Identity & Distribution (ADR-0026) · milestone [#38]

**Goal:** the deferred rename lands — distribution, import, CLI, and npm.

| ID | Title | Deliverable | Acceptance | Issue |
|---|---|---|---|---|
| NAME-1 | Choose the target name | ADR-0026 updated with the decision | Name recorded; availability checked (PyPI/npm) | #509 |
| NAME-2 | Rename distribution + import + CLI | New package/import/console names | Install + import + CLI under the new name | #510 |
| NAME-3 | Compatibility shim | Alias for `import agentwatch` + `agentwatch` CLI | Old names work across the v0.3.x window | #511 |
| NAME-4 | Migration guide | `agent-exec-trace` → `agentwatch` → new name | Guide published in `docs/release/v0.3.0/` | #512 |
| NAME-5 | Doc/example sweep | Every doc, example, compatibility row | No stale name outside the migration guide | #513 |
| NAME-6 | npx launcher + npm publish | `@agentic-suite/cli` launcher | `npx @agentic-suite/cli init` works; publish wired in CI | #514 |
| NAME-7 | Namesake guard | Distribution-check warning in `--version`/`init`/`doctor`; FAQ | Wrong-package install detected + warned | #515 |

**Support tickets:** 34.T [#526] · 34.D [#527] · 34.R [#528]

## M35 — Field Tests · milestone [#39]

| ID | Title | Deliverable | Acceptance | Issue |
|---|---|---|---|---|
| FT-1 | v0.3.0 field-test plan | Plan covering rename + distribution + org | Plan reviewed; cases enumerated | #516 |
| FT-2 | Execute field tests | Report in `docs/field-test/v0.3.0/` | All cases run; pass/fail declared honestly | #517 |
| FT-3 | Fresh-install verification | Clean-machine run across harnesses | New install + shim both verified | #518 |
| FT-4 | **Full functional regression run** | Run the whole suite + all pre-existing field cases on the renamed build | **100% of pre-existing functional tests pass unchanged; zero regressions vs the v0.2.1 baseline** | #535 |
| FT-5 | **Release-readiness test** | End-to-end functional test on the RC (install → record → export → replay → detectors → console) | RC functionally identical to v0.2.1; all readiness checks pass | #536 |

**Support tickets:** 35.T [#529] · 35.D [#530] · 35.R [#531]

## M36 — Release Readiness · milestone [#40]

| ID | Title | Deliverable | Acceptance | Issue |
|---|---|---|---|---|
| REL-1 | Security scan + audit | trufflehog / pip-audit / Scorecard | Clean; findings triaged | #519 |
| REL-2 | Docs update | `CHANGELOG.md`, `README.md`, compatibility matrix, `known-limitations.md` | All reflect the renamed org + package | #520 |
| REL-3 | Release | Tag + GitHub release + PyPI publish from the new org | Artifacts published from `agentic-suite` | #521 |
| REL-4 | Launch content | Article ("The Security-Event Schema Agents Need") | Published after the release | #522 |
| REL-5 | **Update all documents** | Full doc sweep — PRDs, design, reference, guides, README, ROADMAP, CHANGELOG, compatibility matrix, known-limitations, THIRD_PARTY_NOTICES | No stale name/org reference except the migration guide | #537 |
| REL-6 | **Update published article links (dev.to)** | Update article links pointing at the old repo/org | All dev.to article links resolve to the new org | #538 |

**Support tickets:** 36.T [#532] · 36.D [#533] · 36.R [#534]
