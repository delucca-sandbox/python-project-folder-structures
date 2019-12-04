from functools import reduce
from typing import Callable

from tasks.actions import echo_message
from tasks.constants import ECHO_LEVEL_ERROR

from .constants import MESSAGE_PHASE_NOT_FOUND, TEST_PHASES_ALLOWED


def validate_phases(fn: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> Callable:
        ctx, phases, *_ = args

        allowed_phases = reduce(validate_phase, phases, dict())
        only_valid_phases = reduce(warn_invalid_phase, allowed_phases.items(), True)

        return fn(*args, **kwargs) if only_valid_phases else None

    return wrapper


def validate_phase(prev: dict, phase: str) -> bool:
    return {**prev, phase: phase in TEST_PHASES_ALLOWED}


def warn_invalid_phase(still_valid: bool, relation: tuple) -> bool:
    phase, is_valid = relation

    if not is_valid:
        message = MESSAGE_PHASE_NOT_FOUND.format(phase)
        echo_message(message, level=ECHO_LEVEL_ERROR)

    return is_valid if still_valid else still_valid
