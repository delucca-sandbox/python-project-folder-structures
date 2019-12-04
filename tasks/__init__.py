from invoke import task

from tasks.autoformat.constants import AUTOFORMAT_SCOPES_ALLOWED
from tasks.autoformat.handlers import run_autoformat
from tasks.lint.constants import LINT_SCOPES_ALLOWED
from tasks.lint.handlers import run_lint
from tasks.test.constants import TEST_PHASES_ALLOWED
from tasks.test.handlers import run_tests

from .actions import run_handler
from .constants import TASK_NAME_AUTOFORMAT, TASK_NAME_LINT, TASK_NAME_TEST


@task
def test(ctx, phases=TEST_PHASES_ALLOWED):
    run_handler(ctx, phases, TASK_NAME_TEST, run_tests)


@task
def lint(ctx, scopes=LINT_SCOPES_ALLOWED):
    run_handler(ctx, scopes, TASK_NAME_LINT, run_lint)


@task
def autoformat(ctx, scopes=AUTOFORMAT_SCOPES_ALLOWED):
    run_handler(ctx, scopes, TASK_NAME_AUTOFORMAT, run_autoformat)
