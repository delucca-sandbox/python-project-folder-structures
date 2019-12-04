from invoke import Context

from tasks.actions import echo_message
from tasks.constants import ECHO_LEVEL_RUNNING

from .constants import COMMANDS, MESSAGE_SCOPE_RUNNING
from .validators import validate_scopes


@validate_scopes
def run_lint(ctx: Context, scopes: list) -> None:
    for scope in scopes:
        command = COMMANDS.get(scope)
        message = MESSAGE_SCOPE_RUNNING.format(scope)

        echo_message(message, level=ECHO_LEVEL_RUNNING)
        ctx.run(command, pty=True)
