#!/usr/bin/env bash
# Seed the redge backlog from BOOTSTRAP.md's sequencing (inert -> behaviour
# -> activating). Run once; the task files are committed, never regenerated.
set -euo pipefail
cd "$(dirname "$0")/.."
BP=(uvx --from backlog-md-py backlog-py)

"${BP[@]}" task create --id 1 "Implement the R7 remote normalizer (pure) with property tests" \
 -d "Pure function normalize(remote) -> host/owner/repo covering SSH vs HTTPS, trailing .git, host aliases. Manifest and registry key repos by this identity, never basename (SPEC R7)." \
 --ac "normalize() handles SSH, HTTPS, trailing .git, host aliases" \
 --ac "property tests over generated remote forms pass" \
 --ac "distinct URL forms of one repo normalize identically"

"${BP[@]}" task create --id 2 "Implement the manifest: catalogue, local overlay, groups, pins" \
 -d "Committed catalogue of personal repos; unversioned local overlay for private/work entries and the per-machine pick. No hostname committed; no work identifier leaves its machine. Groups first-class: listable, selectable, addressable. Pins are records (R1, R2)." \
 --ac "catalogue + overlay load and validate" \
 --ac "group select/list works for every multi-repo command" \
 --ac "pins recorded per repo; personal pins may commit, work pins stay local" \
 --dep 1

"${BP[@]}" task create --id 3 "Implement the R6 state store contract" \
 -d "Machine-local store under \$XDG_STATE_HOME/redge: last-fetch advances only on successful fetch; blocked-since resets only when a clean ff-only clears the reason. Never committed/synced/backed up; no URLs or userinfo. Good run derives from these records, never exit 0 (R6)." \
 --ac "state records persist machine-locally under XDG_STATE_HOME" \
 --ac "last-fetch does not advance on a failed fetch (mutation-proven)" \
 --ac "blocked-since resets only on cleared reason" \
 --ac "store contains no URLs or userinfo"

"${BP[@]}" task create --id 4 "Implement the GitHub registry with R3 truncation discipline" \
 -d "Registry seam: enumerate an owner via gh/API list endpoints (never Search; Search caps at 1000 and hides incomplete_results). Full/truncated/auth-failed/rate-limited pages read UNKNOWN, never empty; never unregister from an incomplete listing. At most 10 additions per run; archived skipped by default; account scope recorded (R3). Auth via gh auth / SSH; no persisted plaintext token (R8)." \
 --ac "owner enumeration uses list endpoints" \
 --ac "truncation/auth/rate-limit failures read UNKNOWN, never empty" \
 --ac "at most 10 repos added per run" \
 --ac "account scope of listing recorded" \
 --ac "no plaintext token persisted anywhere"

"${BP[@]}" task create --id 5 "Implement redge update: fetch-all, never mutate a working tree" \
 -d "Fetch every repo including dirty ones (fetch never touches the working tree); refresh index/available state. A failed fetch reads UNKNOWN freshness and must not advance last-fetch (R4)." \
 --ac "every repo fetched; dirty repos fetched too" \
 --ac "no working-tree mutation under any input (mutation-proven)" \
 --ac "failed fetch -> UNKNOWN, last-fetch not advanced" \
 --dep 2 --dep 3

"${BP[@]}" task create --id 6 "Implement redge upgrade: ff-only, clean attached non-diverged only" \
 -d "The binding safety contract: git merge --ff-only toward the locked/upstream ref, only when clean + attached + non-diverged. Never merge/rebase/reset/stash. Verdicts per repo: fast-forwarded / skipped:reason; diverged or detached sets blocked-since. Advance the pin only when the merge succeeds. Repo-local problem exits 0; provider/config defect fails the run (R4, R5)." \
 --ac "clean ahead-only repo fast-forwards" \
 --ac "dirty repo fetched, skipped: dirty, tree untouched" \
 --ac "diverged repo blocked-since set, tree untouched, no merge/rebase/reset/stash ever invoked (mutation-proven)" \
 --ac "pin advances only on successful ff merge" \
 --ac "repo-local failure exits 0; provider/config defect fails the run" \
 --dep 5

"${BP[@]}" task create --id 7 "Implement lock/unlock/pin and the status read with JSON output" \
 -d "lock/unlock record or clear a pinned ref (explicit, user-initiated); never enforce by rewriting the tree. status reports per-repo verdicts + staleness from the state store. JSON output mode; stable machine-readable contract (SPEC The pinning split, R5)." \
 --ac "lock/unlock record and clear pins without tree mutation" \
 --ac "status reports verdicts + staleness from state records" \
 --ac "JSON output contract stable and tested" \
 --dep 6

"${BP[@]}" task create --id 8 "Land the Ansible role: install + trigger, never logic or state" \
 -d "role/ installs redge (uvx/pip/git) and may trigger runs; it never contains redge logic or state (SPEC Boundary). Graduates to an installable role later." \
 --ac "role installs redge and smoke-checks redge --version" \
 --ac "no redge logic or state in the role" \
 --dep 6

"${BP[@]}" task create --id 9 "Wire CI to the quality gates" \
 -d "GitHub Actions: uv sync, ruff check + format, mypy, pytest. Same commands mise exposes (quality) so CI and local agree." \
 --ac "CI runs lint, format-check, type-check, tests" \
 --ac "CI commands match the mise quality task" \
 --dep 6

"${BP[@]}" task create --id 10 "Reserve redge-cli on PyPI (author action)" \
 -d "Author action, accounts are the author's: publish a 0.0.1 placeholder named redge-cli to reserve the namespace (BOOTSTRAP.md). uv build; uv publish." \
 --ac "redge-cli 0.0.1 visible on PyPI" \
 --ac "placeholder clearly marked (README points to the repo)"

"${BP[@]}" task create --id 11 "Reserve redge-cli on crates.io (author action)" \
 -d "Author action: cargo new redge-cli --lib placeholder; cargo login; cargo publish 0.0.1 reserves the name for the possible Rust port (R11)." \
 --ac "redge-cli 0.0.1 visible on crates.io"

echo "seeded:"
ls backlog/tasks/