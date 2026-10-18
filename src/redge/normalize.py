"""R7 — remote-identity normalizer (pure).

normalize(remote) -> host/owner/repo, covering SSH vs HTTPS, the trailing
``.git`` suffix, and host aliases. A pure function, property-tested; the
registry is keyed by this identity, never by basename (SPEC R7).

This module is a skeleton; the property tests land with the first
behaviour task (see backlog/).
"""


def normalize(remote: str) -> str:
    """Normalize a git remote URL to ``host/owner/repo``.

    Raises NotImplementedError until the first behaviour task lands.
    """
    raise NotImplementedError("redge-2: implement normalize (SPEC R7)")
