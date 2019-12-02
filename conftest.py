from functools import reduce
from typing import Callable

import pytest


def pytest_collection_modifyitems(items: list) -> list:
    marked_tests = map(apply_markers, items)

    return list(marked_tests)


def apply_markers(test: Callable) -> Callable:
    markers_common, markers_avaiable = build_markers()
    markers_test = reduce(
        lambda prev, nxt: select_markers(test, prev, nxt),
        markers_avaiable,
        markers_common,
    )

    return mark_test(test, markers_test)


def build_markers() -> tuple:
    common = list()
    avaiable = [
        dict(rule="foo/", marker=pytest.mark.unit),
        dict(rule="/integration/", marker=pytest.mark.integration),
    ]

    return common, avaiable


def select_markers(test: Callable, markers: list, marker: dict) -> list:
    return [*markers, marker.get("marker")] if should_mark(test, marker) else markers


def should_mark(test: Callable, marker: dict) -> bool:
    return marker.get("rule") in test.nodeid


def mark_test(test: Callable, markers: list) -> Callable:
    for mark in markers:
        test.add_marker(mark)

    return test
