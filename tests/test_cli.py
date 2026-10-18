"""Tests for the redge CLI surface (inert scaffold).

The scaffold contract: every subcommand from REDGE-ARCHITECTURE.md § cli
is registered, --version reports, and bodies are honest stubs. Behaviour
tests land with the behaviour tasks (see backlog/).
"""

import pytest
from typer.testing import CliRunner

from redge import __version__
from redge.cli import app

runner = CliRunner()

REGISTERED_COMMANDS = {
    "add",
    "groups",
    "lock",
    "pin",
    "status",
    "sync",
    "unlock",
    "update",
    "upgrade",
}


def test_version_flag() -> None:
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert __version__ in result.output


def test_help_lists_every_architecture_command() -> None:
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    for command in REGISTERED_COMMANDS:
        assert command in result.output


@pytest.mark.parametrize("command", sorted(REGISTERED_COMMANDS))
def test_stub_bodies_raise_not_implemented(command: str) -> None:
    """A stub must fail loudly, never pretend to succeed (SPEC R5 honesty)."""
    result = runner.invoke(app, [command])
    assert result.exit_code != 0
    assert isinstance(result.exception, NotImplementedError)
    assert command in str(result.exception) or "redge-" in str(result.exception)


def test_hello_sample_command_is_gone() -> None:
    """The base template's sample command is not part of redge's surface."""
    result = runner.invoke(app, ["hello"])
    assert result.exit_code != 0
