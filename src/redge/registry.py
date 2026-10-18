"""R3 — pluggable registry seam (GitHub first).

One list verb: enumerate an owner -> ``(identity, url,
archived/fork/template)`` records. List endpoints, never Search; full,
  truncated, auth-failed, or rate-limited pages read UNKNOWN — never
"empty" — and never unregister a repo from an incomplete listing. At most
ten additions per run; archived repos skipped by default; the account
scope of the listing is recorded (SPEC R3).

Skeleton; the GitHub implementation lands with the registry task.
"""
