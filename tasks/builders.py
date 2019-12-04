from typing import Callable

from invoke import Context


def build_options_object(
    commands: dict, context: Context, log_pattern: str
) -> Callable:
    def merge(option: str) -> dict:
        return dict(
            selected_option=option,
            avaiable_commands=commands,
            log_pattern=log_pattern,
            runner=context.run,
        )

    return merge


def build_option_validator(allowed_options: str) -> Callable:
    def validate_option(prev: dict, option: str) -> dict:
        return {**prev, option: option in allowed_options}

    return validate_option
