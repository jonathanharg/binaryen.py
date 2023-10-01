# Binaryen.py

Binaryen.py is a python wrapper for [Binaryen](https://github.com/WebAssembly/binaryen). Use this to create, optimise and interpret WebAssembly binaries in python.

## Installation

First make sure [Binaryen](https://github.com/WebAssembly/binaryen) is installed and accessible from your path. For Linux/MacOS it's recommended to install it from your package manager or [homebrew](https://formulae.brew.sh/formula/binaryen) (on MacOS). Alternatively, download [precompiled binaries](https://github.com/WebAssembly/binaryen/releases) of Binaryen.

Install through PyPI.

```bash
pip install binaryen.py
```

## Test

```bash
pytest --doctest-modules --doctest-continue-on-failure
```

## Format

```bash
black --extend-exclude binaryen/_binaryen_cffi.py .
```

## Docs

```bash
mkdocs serve
```

## Updating the Python header file

Get the latest binaryen header file and binaries.

Comment out `#include <stdbool.h>`, `#include <stddef.h>` and `#include <stdint.h>`

```bash
cpp -nostdinc -E -P binaryen-c.h | sed '/^\/\//d; s/##//g; s/;;/;/g;' | tr '\n' ' ' | sed '1s/^[[:space:]]*//; s/  */ /g;s/; /;\n/g;' | sed '/^__attribute__((deprecated))/d' | clang-format -style "{ColumnLimit: 0}" > binaryen-py.h
```

> This cleans up the header file and removes deprecated code

Replace Union types with the largest type of that Union. E.g.

```c
struct BinaryenLiteral
{
  uintptr_t type;
  union
  {
    int32_t i32;
    int64_t i64;
    float f32;
    double f64;
    uint8_t v128[16];
    const char *func;
  };
};
```

Becomes

```c
struct BinaryenLiteral
{
  uintptr_t type;
  uint8_t v128[16];
};
```

Build the cffi interface by running `python binaryen_build.py`
