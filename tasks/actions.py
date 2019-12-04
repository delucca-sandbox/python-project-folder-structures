from invoke import run

from .constants import (
    COLORS_ERROR,
    COLORS_INFO,
    COLORS_RESET,
    COLORS_RUNNING,
    ECHO_LEVEL_DEFAULT,
    ECHO_MESSAGE_PATTERN,
    INDENT_CHAR_DEFAULT,
    INDENT_CHAR_SUFIX,
    INDENT_ERROR,
    INDENT_INFO,
    INDENT_RUNNING,
)


def echo_message(message: str, level: str = ECHO_LEVEL_DEFAULT) -> None:
    colors = dict(INFO=COLORS_INFO, RUNNING=COLORS_RUNNING, ERROR=COLORS_ERROR,)

    indents = dict(INFO=INDENT_INFO, RUNNING=INDENT_RUNNING, ERROR=INDENT_ERROR,)

    color = colors.get(level)
    reset = COLORS_RESET
    indent = indents.get(level)

    prefix = INDENT_CHAR_DEFAULT * indent + INDENT_CHAR_SUFIX
    message = ECHO_MESSAGE_PATTERN.format(color, prefix, level, reset, message)

    run(f'echo "{message}"')
