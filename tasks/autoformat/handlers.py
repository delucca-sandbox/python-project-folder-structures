from invoke import Context

from tasks.actions import run_multiple_commands
from tasks.validators import validate_options

from .constants import AUTOFORMAT_SCOPES_ALLOWED, COMMANDS, MESSAGE_SCOPE_RUNNING


@validate_options(AUTOFORMAT_SCOPES_ALLOWED)
def run_autoformat(ctx: Context, scopes: list) -> None:
    run_multiple_commands(ctx, scopes, COMMANDS, pattern=MESSAGE_SCOPE_RUNNING)
