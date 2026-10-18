"""R6 — machine-local freshness state.

Records under ``$XDG_STATE_HOME/redge/`` (default ``~/.local/state/redge``):
``last-fetch`` advances only on a successful fetch; ``blocked-since``
resets only when a clean ``ff-only`` clears the reason. Never committed,
synced, or backed up; stores no URLs or userinfo. "Good run" derives from
these records, never from exit 0 (SPEC R6).

Skeleton; the store contract lands before any sync logic (see backlog/).
"""
