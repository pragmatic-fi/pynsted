"""Working with nested values in Python dictionaries."""

from typing import Any, Generic, TypeVar, cast

_PT = TypeVar("_PT", bound=dict[Any, Any])
_PV = TypeVar("_PV")


def _create_dict(path: list[Any], value: _PV) -> dict[Any, Any] | _PV:
    if not path:
        return value
    key = path.pop(0)
    return {key: _create_dict(path, value)}


class PynstedPrism(Generic[_PT, _PV]):
    """Class implementing prism for Python dictionary."""

    def __init__(self, initial_dict: dict[Any, Any], path: list[Any]) -> None:
        self._parent = initial_dict
        # This class will not work for empty path
        assert path
        self._path = path

    def get(self, default: None | _PV = None) -> None | _PV:
        """Get nested value from the dictionary."""
        cur = self._parent
        for key in self._path:
            if not isinstance(cur, dict) or key not in cur:
                return default
            cur = cur[key]
        return cast(None | _PV, cur)

    def set(self, value: _PV) -> bool:
        """Set nested value in the dictionary."""
        # Indicates success
        cur = self._parent
        parent = cur
        path = self._path.copy()
        while isinstance(cur, dict) and path:  # pylint: disable=while-used
            if (key := path.pop(0)) not in cur:
                cur[key] = _create_dict(path, value)
                return True
            parent = cur
            cur = cur[key]
        if not path:
            parent[self._path[-1]] = value
            return True
        return False
