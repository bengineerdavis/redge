"""R1/R2 — declarative catalogue: repos, groups, pins, local overlay.

One committed catalogue of personal repos and remotes; an unversioned
local overlay carries private/work entries and the per-machine pick. No
hostname is committed; no work identifier leaves its machine. Groups are
first-class: listable, selectable, addressable by every multi-repo
command. Pins are records, never enforced constraints (SPEC R1, R2,
Boundary).

Skeleton; loading lands with the manifest task (see backlog/).
"""


def load(*, overlay: bool = True) -> "Manifest":
    """Load the committed catalogue plus (by default) the local overlay."""
    raise NotImplementedError("redge-3: implement manifest loading (SPEC R1/R2)")


class Manifest:
    """The parsed catalogue: repos, groups, pins. Skeleton."""
