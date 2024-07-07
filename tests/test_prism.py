"""Tests for pynsted.prism."""

from typing import Any

import pytest

from pynsted.prism import PynstedPrism

_FOO = "foo"


@pytest.mark.parametrize(
    "input_dict,path",
    (
        [{}, [1]],
        [{}, [1, 2]],
        [{1: 2}, [2]],
        [{1: 2}, [2, 1]],
        [{1: {2: {3: 4}}}, [0]],
        [{1: {2: {3: 4}}}, [1, 0]],
        [{1: {2: {3: 4}}}, [1, 2, 0]],
    ),
)
def test_no_value(input_dict: dict[Any, Any], path: list[Any]) -> None:
    """Test that prism returns None at getting nonexisting value."""
    p: PynstedPrism[dict[Any, Any], int] = PynstedPrism(input_dict, path)
    assert p.get() is None


@pytest.mark.parametrize(
    "input_dict,path",
    (
        [{}, [1]],
        [{}, [1, 2]],
        [{1: 2}, [2]],
        [{1: 2}, [2, 1]],
        [{1: {2: {3: 4}}}, [0]],
        [{1: {2: {3: 4}}}, [1, 0]],
        [{1: {2: {3: 4}}}, [1, 2, 0]],
    ),
)
def test_use_default_value(
    input_dict: dict[Any, Any], path: list[Any]
) -> None:
    """Test that prism returns the given default at getting nonexisting value."""
    p: PynstedPrism[dict[Any, Any], str] = PynstedPrism(input_dict, path)
    assert p.get("foo") == _FOO


@pytest.mark.parametrize(
    "input_dict,path,expected_dict",
    (
        [{}, [1], {1: "foo"}],
        [{}, [1, 2], {1: {2: "foo"}}],
        [{2: "xyzzy"}, [1], {1: "foo", 2: "xyzzy"}],
        [{2: "xyzzy"}, [1, 2], {1: {2: "foo"}, 2: "xyzzy"}],
        [
            {1: {1: "gnusto"}, 2: "xyzzy"},
            [1, 2],
            {1: {1: "gnusto", 2: "foo"}, 2: "xyzzy"},
        ],
        [
            {1: {1: "gnusto"}, 2: "xyzzy"},
            [1, 2, 3],
            {1: {1: "gnusto", 2: {3: "foo"}}, 2: "xyzzy"},
        ],
    ),
)
def test_set_absent(
    input_dict: dict[Any, Any],
    path: list[Any],
    expected_dict: dict[Any, Any],
) -> None:
    """Test that prisms sets correctly non-existing value."""
    p: PynstedPrism[dict[Any, Any], Any] = PynstedPrism(input_dict, path)
    p.set("foo")
    assert input_dict == expected_dict
