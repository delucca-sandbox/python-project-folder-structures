from functools import reduce
from typing import Callable

from tasks.actions import echo_message
from tasks.constants import ECHO_LEVEL_ERROR

from .constants import LINT_SCOPES_ALLOWED, MESSAGE_SCOPE_NOT_FOUND


def validate_scopes(fn: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> Callable:
        ctx, scopes, *_ = args

        allowed_scopes = reduce(validate_scope, scopes, dict())
        only_valid_scopes = reduce(warn_invalid_scope, allowed_scopes.items(), True)

        return fn(*args, **kwargs) if only_valid_scopes else None

    return wrapper


def validate_scope(prev: dict, scope: str) -> bool:
    return {**prev, scope: scope in LINT_SCOPES_ALLOWED}


def warn_invalid_scope(still_valid: bool, relation: tuple) -> bool:
    scope, is_valid = relation

    if not is_valid:
        message = MESSAGE_SCOPE_NOT_FOUND.format(scope)
        echo_message(message, level=ECHO_LEVEL_ERROR)

    return is_valid if still_valid else still_valid
