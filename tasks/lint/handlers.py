from invoke import Context

from tasks.actions import run_multiple_commands
from tasks.validators import validate_options

from .constants import COMMANDS, LINT_SCOPES_ALLOWED, MESSAGE_SCOPE_RUNNING


@validate_options(LINT_SCOPES_ALLOWED)
def run_lint(ctx: Context, scopes: list) -> None:
    run_multiple_commands(ctx, scopes, COMMANDS, pattern=MESSAGE_SCOPE_RUNNING)
