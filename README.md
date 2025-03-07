# pynsted

This is a Python library which in a hackish way adds to Python dictionaries
a method for getting nested values. It can be installed with
`pip install pynsted`.

## Usage

Start by importing the module: `import pynsted`.

Now access nested values in dictionaries by specifing path to them and using
`getn` method:

```python
>>> import pynsted
>>> a = {1: {2: {"foo": "bar"}}}
>>> a.getn([1, 2, "foo"])
'bar'
>>>
```

If at some moment there is no value, corresponding to the next key in path,
`None` is returned:

```python
>>> print(a.getn([1, 3, "foo"]))
None
>>>
```

It is possible to specify the default value, which will be returned instead of
`None` if there is no value at the given path:

```python
>>> a.getn([1, 3, "foo"], "new default")
'new default'
>>>
```

## Linters

There are two problems with this module and linters:

- unused import
- nonexisting `.getn()` method for dictionaries

### Unused import

If the import is really unused (see below why it may not be), do the following:

- for `pylint` put `# pylint: disable=unused-import` in the line right before
  the import and `# pylint: disable=unused-import` in the line right after, or
  `pylint: disable=unused-import` as an end comment into the import line
- for `ruff` put `noqa: F401` as an end comment into the import line
- for `pyright`: put `# pyright: reportUnusedImport=false` in the line right
  before the import line and `# pyright: reportUnusedImport=false` in the line
  right after, or `pyright: ignore` as an end comment into the import line

Notice that in the case of multiple linters combination of end of line comments
in the import line will not work, and you will need to do something like

```python
# pylint: disable=unused-import
# pyright: reportUnusedImport=false
import pynsted  # noqa: F401
# pyright: reportUnusedImport=true
# pylint: enable=unused-import
```

### Nonexisting method

#### Quick and dirty pylint solution

Add inte yoir pylint configuration file something like
`extension-pkg-whitelist=pynsted`. Notice that method is insecure and allows
the authors of `pynsted` to do whatever they want with your computer, and maybe
also kill your cat.

### Using protocol

The benefit of this approach that it will pacify not only `pylint` but
`pyright`, `ruff`, and `mypy`, and will make import used. The idea is that
`pytested` module defines `SupportsGetn` protocol, which claims the presence of
`getn` method. You have to assert that your dictionary is BOTH `dict` and
`SupportsGetn`:

```python
assert isinstance(input_dict, dict)
assert isinstance(input_dict, pynsted.SupportsGetn)
```

## Development

The project uses `poetry` tool (highly recommended!), you should know your way
around. The supplied `Makefile` defines the following targets:

- `test` -- runs `pytest` and demands 100% test coverage
- `qa` -- runs `test` target and then runs a bunch of linters
- `format` -- formats the code with `black` and `isort`
