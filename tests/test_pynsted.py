"""Tests for getn() method."""

from typing import Any

import pytest

import pynsted


@pytest.mark.parametrize(
    "input_dict,path,expected",
    [
        ({}, [1, 2, 3], None),
        (
            {
                1: {1: "foo", 2: {1: "a", 2: "b", 3: "c"}, 3: "bar"},
                2: "foo",
                3: "bar",
            },
            [1, 2, 3],
            "c",
        ),
        (
            {
                1: {1: "foo", 2: {1: "a", 2: "b", 3: "c"}, 3: "bar"},
                2: "foo",
                3: "bar",
            },
            [4, 2, 3],
            None,
        ),
        (
            {
                1: {1: "foo", 2: {1: "a", 2: "b", 3: "c"}, 3: "bar"},
                2: "foo",
                3: "bar",
            },
            [1, 4, 3],
            None,
        ),
        (
            {
                1: {1: "foo", 2: {1: "a", 2: "b", 3: "c"}, 3: "bar"},
                2: "foo",
                3: "bar",
            },
            [1, 2, 4],
            None,
        ),
        ({1: 2}, [1], 2),
        ({1: 2}, [3], None),
    ],
)
def test_no_default(input_dict: Any, path: list[Any], expected: Any) -> None:
    """Test getting nested value from dictionary if the default is not
    given.
    """
    assert isinstance(input_dict, dict)
    assert isinstance(input_dict, pynsted.SupportsGetn)
    assert input_dict.getn(path) == expected


@pytest.mark.parametrize(
    "input_dict,path,default",
    [
        ({}, [1, 2, 3], 0),
        ({1: 2}, [3], "foo"),
        (
            {
                1: {1: "foo", 2: {1: "a", 2: "b", 3: "c"}, 3: "bar"},
                2: "foo",
                3: "bar",
            },
            [4, 2, 3],
            {"a": "b"},
        ),
        (
            {
                1: {1: "foo", 2: {1: "a", 2: "b", 3: "c"}, 3: "bar"},
                2: "foo",
                3: "bar",
            },
            [1, 4, 3],
            ["a", "b"],
        ),
        (
            {
                1: {1: "foo", 2: {1: "a", 2: "b", 3: "c"}, 3: "bar"},
                2: "foo",
                3: "bar",
            },
            [1, 2, 4],
            True,
        ),
        ({1: 2}, [3], None),
    ],
)
def test_with_default(
    input_dict: pynsted.SupportsGetn, path: list[Any], default: Any
) -> None:
    """Test getting nested value from dictionary if the default is
    given.
    """
    assert isinstance(input_dict, dict)
    assert isinstance(input_dict, pynsted.SupportsGetn)
    assert input_dict.getn(path, default) == default
