from typing import Callable, List

from invoke import Context, run

from . import builders, selectors
from .constants import (
    COLORS_ERROR,
    COLORS_INFO,
    COLORS_RESET,
    COLORS_RUNNING,
    ECHO_LEVEL_DEFAULT,
    ECHO_LEVEL_ERROR,
    ECHO_LEVEL_RUNNING,
    ECHO_MESSAGE_PATTERN,
    INDENT_CHAR_DEFAULT,
    INDENT_CHAR_SUFIX,
    INDENT_ERROR,
    INDENT_INFO,
    INDENT_RUNNING,
    MESSAGE_FINISHED_TASK,
    MESSAGE_OPTION_NOT_FOUND,
    MESSAGE_RUNNING_OPTION,
    MESSAGE_STARTING_TASK,
)


def run_handler(ctx: Context, options: str, task_name: str, handler: Callable) -> None:
    selected_options: List[str] = options.split(",")
    message_starting = MESSAGE_STARTING_TASK.format(task_name)
    message_finished = MESSAGE_FINISHED_TASK.format(task_name)

    echo_message(message_starting)
    handler(ctx, selected_options)
    echo_message(message_finished)


def echo_message(message: str, level: str = ECHO_LEVEL_DEFAULT) -> None:
    colors = dict(INFO=COLORS_INFO, RUNNING=COLORS_RUNNING, ERROR=COLORS_ERROR,)

    indents = dict(INFO=INDENT_INFO, RUNNING=INDENT_RUNNING, ERROR=INDENT_ERROR,)

    color = colors.get(level)
    reset = COLORS_RESET
    indent = indents.get(level) or 1

    prefix = INDENT_CHAR_DEFAULT * indent + INDENT_CHAR_SUFIX
    message = ECHO_MESSAGE_PATTERN.format(color, prefix, level, reset, message)

    run(f'echo "{message}"')


def warn_invalid_option(still_valid: bool, relation: tuple) -> bool:
    option, is_valid = relation

    if not is_valid:
        message = MESSAGE_OPTION_NOT_FOUND.format(option)
        echo_message(message, level=ECHO_LEVEL_ERROR)

    return is_valid if still_valid else still_valid


def run_multiple_commands(
    ctx: Context, options: list, commands: dict, pattern: str = MESSAGE_RUNNING_OPTION
) -> list:
    new_object = builders.build_options_object(commands, ctx, pattern)

    option_objects = map(new_object, options)
    option_objects = map(selectors.select_option_command, option_objects)
    result = map(run_command, option_objects)

    return list(result)


def run_command(option_object: dict) -> None:
    pattern = option_object.get("log_pattern") or MESSAGE_RUNNING_OPTION
    selected_option = option_object.get("selected_option")
    command = option_object.get("command")
    run_on_context = option_object.get("runner") or run
    message = pattern.format(selected_option)

    echo_message(message, level=ECHO_LEVEL_RUNNING)
    run_on_context(command, pty=True)
