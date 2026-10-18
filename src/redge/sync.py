"""R4/R5 — the sync engine: update / upgrade / lock / pin / status.

The binding safety contract: fetch every repo (fetch never touches the
working tree); fast-forward only a clean, attached, non-diverged repo
via ``git merge --ff-only``; never merge, rebase, reset, or stash local
work; never enforce a pinned revision by rewriting the tree. Verdicts
are per-repo and non-aborting: a repo-local problem exits 0, a provider
or configuration defect fails the run (SPEC R4, R5, The pinning split).

Skeleton; sync behaviour lands last, after the state contract is proven
(BOOTSTRAP.md sequencing).
"""
