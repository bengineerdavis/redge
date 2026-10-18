# redge

`redge` treats git repositories the way a package manager treats packages:
a declarative manifest, an `update` / `upgrade` / `lock` split, safe one-way
sync, named groups, and a pluggable registry for discovery.

The package is `redge-cli` on PyPI (namespace reserved); the command is
`redge`. The name never depends on the registry token. Python first; a Rust
port may reuse the same `redge-cli` namespace (SPEC R11). Fair Source
licensed (FSL-1.1-MIT): everything except a competing use now, MIT after two
years.

## Status

Inert scaffold. The command surface is registered (`redge --help`), every
subcommand is an honest stub, and the normative requirements
(`docs/research/repo-manager/SPEC.md`, R1–R11), the design sketch
(`docs/research/repo-manager/REDGE-ARCHITECTURE.md`), and the bootstrap
brief are migrated into `docs/`. Implementation is queued in the task
store (`backlog/`, ids `redge-…`) in the BOOTSTRAP.md sequencing: normalize →
manifest/state → registry → sync → role → CI.

## The safety contract (R4, binding)

`redge` is *declarative presence* with *safe fast-forward* — not a lockfile
that pins and enforces revisions. The only permitted working-tree mutation
is `git merge --ff-only` on a clean, attached, non-diverged repository:

- `update` fetches every repo (fetch never touches the working tree) and
  refreshes available state. Never mutates.
- `upgrade` fast-forwards toward the locked/upstream ref only when clean +
  attached + non-diverged. Dirty → `skipped: dirty`. Diverged/detached/no
  upstream → `blocked-since` set, tree untouched. The pin advances only when
  the merge succeeds.
- A failed fetch reads UNKNOWN freshness, never "up to date".

## Development

    uv sync --all-groups
    uv run pytest
    mise run install   # tools + hooks + agentic state (dotagents)
    mise run quality   # lint + format-check + type-check

Agent work is assigned in `backlog/` before it starts, one worktree per
task (`wt switch <redge-N-slug>`). The fast loop (roborev) reviews every
commit; check findings with `mise run roborev-status`.

## License

FSL-1.1-MIT — see [LICENSE](LICENSE).