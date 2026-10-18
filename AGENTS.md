# redge

redge: Repositories as a package manager: declarative catalogue, update/upgrade/lock split, safe one-way fast-forward, named groups, pluggable registry discovery.

## Commands

- `mise run install` — bootstrap tools and the agentic layer (idempotent)
- `mise run test` — pytest (`uv run` auto-syncs the venv first)
- `mise run quality` — lint + format-check + type-check
- `mise run format` — auto-fix

## Repo map

- `src/redge/` — the package; `cli.py` is the entry point
- `tests/` — pytest suite
- `docs/` — project documentation
- `backlog/` — task store (backlog-py; work is assigned here before it starts)

## Context loading (on demand)

- Normative requirements → `docs/research/repo-manager/SPEC.md`
- Design sketch → `docs/research/repo-manager/REDGE-ARCHITECTURE.md`
- Bootstrap brief (sequencing, namespace reservation) →
  `docs/research/repo-manager/BOOTSTRAP.md`
- Task store → `uv run backlog-py board`

The section below is managed by agentic-project-template.

<!-- BEGIN managed: agentic-project-template -->
## Agentic layer

This repository carries an agentic layer managed by
`agentic-project-template`. The rules live in `.context/ai-rules.md`
(injected into opencode sessions); terms in `.context/glossary.md`.

- **Fast loop:** every commit is queued for background review by roborev;
  check open findings with `mise run roborev-status` before claiming work
  done (skill: `review-findings`).
- **Slow loop:** `mise run review-deep` reviews the branch and writes a dated
  report to `docs/reviews/`.
- **Agent dependencies:** skills, subagents, and MCP servers are declared in
  `agents.toml` and installed with `mise run dotagents-install`. Do not
  hand-edit dotagents-managed files.
- **Isolation:** one worktree per task — `wt switch <task-id-slug>` creates
  it and bootstraps via the post-create hook; merge and clean up when done.
- **Tasks:** agent work starts only after a backlog task exists stating what
  done means (`uvx --from backlog-md-py backlog-py task create …`).
- **Experiments:** record repeated AI usage worth converting to deterministic
  tooling in `docs/experiments.md`.
<!-- END managed: agentic-project-template -->
