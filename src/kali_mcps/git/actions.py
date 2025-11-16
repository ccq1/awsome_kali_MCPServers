"""Utilities for interacting with git from the MCP server."""
from typing import Tuple

from src.kali_mcps.base.kali_command import CommandRunner


class GitCommand(CommandRunner):
    """Command runner configured for git invocations."""

    def __init__(self):
        super().__init__(
            "git",
            network_enabled=False,
            memory_limit="256m",
            timeout=60,
        )


def _format_response(stdout: str, stderr: str) -> Tuple[str, str]:
    """Merge stdout/stderr strings for multi-step commands."""
    formatted_stdout = stdout.strip()
    formatted_stderr = stderr.strip()
    return formatted_stdout, formatted_stderr


def git_status_action() -> Tuple[str, str]:
    """Return the current repository status using `git status`."""

    cmd = GitCommand()
    stdout, stderr = cmd.execute(["git", "status", "--short", "--branch"])
    return _format_response(stdout, stderr)


def git_commit_action(message: str, add_all: bool = True) -> Tuple[str, str]:
    """Stage files (optionally) and create a commit with the provided message."""

    git = GitCommand()
    stdout_parts = []
    stderr_parts = []

    if add_all:
        add_stdout, add_stderr = git.execute(["git", "add", "-A"])
        if add_stdout:
            stdout_parts.append(add_stdout.strip())
        if add_stderr:
            stderr_parts.append(add_stderr.strip())

    commit_stdout, commit_stderr = git.execute(["git", "commit", "-m", message])
    if commit_stdout:
        stdout_parts.append(commit_stdout.strip())
    if commit_stderr:
        stderr_parts.append(commit_stderr.strip())

    stdout = "\n".join(part for part in stdout_parts if part)
    stderr = "\n".join(part for part in stderr_parts if part)
    return stdout, stderr
