# redge Ansible role — install + trigger, never logic or state

Provisioning (chezmoi/Ansible) installs redge and may trigger runs; it
never contains redge's logic or state (SPEC § Boundary). This role is a
sibling artifact inside the redge repository, graduating to an installable
dependency later (BOOTSTRAP.md).

## Vars

- `redge_install_method` — `uvx` (default) pins via `uvx --from redge-cli==<ver>`; `pip` installs from PyPI; `git` installs from this repository.

## Tasks

- install redge (vars-driven)
- `redge --version` smoke-check

## Status

Skeleton — the role lands with the provisioning task (see backlog/).