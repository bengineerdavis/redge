"""CLI entry point for redge — commands per REDGE-ARCHITECTURE.md § cli.

Inert scaffold: every subcommand is registered (so the surface is
reviewable) and every body is a stub pointing at its backlog task.
JSON output mode and per-repo exit semantics land with the behaviour
tasks (SPEC R5).
"""

import typer

from redge import __version__

app = typer.Typer(
    help="Repositories as a package manager: declarative catalogue, "
    "safe one-way fast-forward, named groups, registry discovery.",
    no_args_is_help=True,
)


@app.callback(invoke_without_command=True)
def main(
    version: bool = typer.Option(False, "--version", help="Show version and exit"),
) -> None:
    """redge — repositories as a package manager."""
    if version:
        typer.echo(__version__)
        raise typer.Exit()


@app.command()
def update() -> None:
    """Fetch every repo; refresh index/available state. Never mutates a tree."""
    raise NotImplementedError("redge-5: implement update (SPEC R4)")


@app.command()
def upgrade() -> None:
    """Fast-forward each repo toward its locked/upstream ref (ff-only, clean only)."""
    raise NotImplementedError("redge-6: implement upgrade (SPEC R4)")


@app.command()
def lock() -> None:
    """Record a pinned ref (explicit, user-initiated)."""
    raise NotImplementedError("redge-7: implement lock (SPEC The pinning split)")


@app.command()
def pin() -> None:
    """Alias of lock: record the current ref as the pin."""
    raise NotImplementedError("redge-7: implement lock (SPEC The pinning split)")


@app.command()
def unlock() -> None:
    """Clear a pinned ref."""
    raise NotImplementedError("redge-7: implement unlock (SPEC The pinning split)")


@app.command()
def sync() -> None:
    """Ergonomic alias: update then upgrade."""
    raise NotImplementedError("redge-5/redge-6: update then upgrade")


@app.command()
def status() -> None:
    """Per-repo verdicts (fast-forwarded / skipped-reason / failed) + staleness."""
    raise NotImplementedError("redge-4: implement status read (SPEC R6)")


@app.command()
def groups() -> None:
    """List named groups (first-class: listable, selectable, addressable)."""
    raise NotImplementedError("redge-3: implement group listing (SPEC R2)")


@app.command()
def add() -> None:
    """Add a repo to the catalogue (at most ten additions per run, SPEC R3)."""
    raise NotImplementedError("redge-8: implement registry-driven add (SPEC R3)")


if __name__ == "__main__":
    app()
