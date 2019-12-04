from functools import reduce
from typing import Callable

from . import actions, builders


def validate_options(allowed_options: str) -> Callable:
    def decorator(fn: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> Callable:
            ctx, options, *_ = args

            validate_option = builders.build_option_validator(allowed_options)
            options_exist: dict = reduce(validate_option, options, dict())
            only_valid_options = reduce(
                actions.warn_invalid_option, options_exist.items(), True
            )

            return fn(*args, **kwargs) if only_valid_options else None

        return wrapper

    return decorator
