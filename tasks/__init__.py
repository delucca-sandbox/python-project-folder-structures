from invoke import task

from tasks.lint.constants import LINT_SCOPES_ALLOWED
from tasks.lint.handlers import run_lint
from tasks.test.constants import TEST_PHASES_ALLOWED
from tasks.test.handlers import run_tests

from .actions import echo_message
from .constants import (
    MESSAGE_FINISHED_TASK,
    MESSAGE_STARTING_TASK,
    TASK_NAME_LINT,
    TASK_NAME_TEST,
)


@task
def test(ctx, phases=TEST_PHASES_ALLOWED):
    phases = phases.split(",")
    message_starting = MESSAGE_STARTING_TASK.format(TASK_NAME_TEST)
    message_finished = MESSAGE_FINISHED_TASK.format(TASK_NAME_TEST)

    echo_message(message_starting)
    run_tests(ctx, phases)
    echo_message(message_finished)


@task
def lint(ctx, scopes=LINT_SCOPES_ALLOWED):
    scopes = scopes.split(",")
    message_starting = MESSAGE_STARTING_TASK.format(TASK_NAME_LINT)
    message_finished = MESSAGE_FINISHED_TASK.format(TASK_NAME_LINT)

    echo_message(message_starting)
    run_lint(ctx, scopes)
    echo_message(message_finished)
