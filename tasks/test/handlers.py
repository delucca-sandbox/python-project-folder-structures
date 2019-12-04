from invoke import Context

from tasks.actions import echo_message
from tasks.constants import ECHO_LEVEL_RUNNING

from .constants import COMMANDS, MESSAGE_PHASE_RUNNING
from .validators import validate_phases


@validate_phases
def run_tests(ctx: Context, phases: list) -> None:
    for phase in phases:
        command = COMMANDS.get(phase)
        message = MESSAGE_PHASE_RUNNING.format(phase)

        echo_message(message, level=ECHO_LEVEL_RUNNING)
        ctx.run(command, pty=True)
