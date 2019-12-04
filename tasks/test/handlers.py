from invoke import Context

from tasks.actions import run_multiple_commands
from tasks.validators import validate_options

from .constants import COMMANDS, MESSAGE_PHASE_RUNNING, TEST_PHASES_ALLOWED


@validate_options(TEST_PHASES_ALLOWED)
def run_tests(ctx: Context, phases: list) -> None:
    run_multiple_commands(ctx, phases, COMMANDS, pattern=MESSAGE_PHASE_RUNNING)
