# UUID v7 and v6

[![codecov](https://codecov.io/gh/YoussefEgla/uuid-v7/branch/main/graph/badge.svg?token=uuid-v7_token_here)](https://codecov.io/gh/YoussefEgla/uuid-v7)
[![CI](https://github.com/YoussefEgla/uuid-v7/actions/workflows/main.yml/badge.svg)](https://github.com/YoussefEgla/uuid-v7/actions/workflows/main.yml)

This package extends the built-in `uuid` module to include UUID v7 and v6.

## Install it from PyPI

```bash
pip install uuid_v7
```

## Usage

```py
from uuid_v7 import uuidv7, uuidv6

print(uuidv7())
print(uuidv6())
```

```bash
$ python
>>> from uuid_v7 import uuidv7, uuidv6
>>> print(uuidv7())
>>> print(uuidv6())
```

## Development

Read the [CONTRIBUTING.md](CONTRIBUTING.md) file.

## Special Thanks to

- [@oittaa](https://github.com/oittaa) The author of UUID v7 and v6 implementation in Python. [Add UUIDv6 and UUIDv7](https://github.com/python/cpython/pull/29824)
- [@rochacbruno](https://github.com/rochacbruno) for the [project template](https://github.com/rochacbruno/python-project-template)
