# Binaryen.py

Binaryen.py is a python wrapper for [Binaryen](https://github.com/WebAssembly/binaryen). Use this to create, optimise and interpret WebAssembly binaries in python.

## Installation

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

```bash
sed "/^#include <stdbool.h>/d; /^#include <stddef.h>/d; /^#include <stdint.h>/d;" binaryen-c.h | cpp -nostdinc -E -P | sed '/^\/\//d; s/##//g; s/;;/;/g;' | tr '\n' ' ' | sed '1s/^[[:space:]]*//; s/  */ /g;s/; /;\n/g;' | sed '/^__attribute__((deprecated))/d' | clang-format -style "{ColumnLimit: 0}" > binaryen-py.c
```

> This cleans up the header file and removes deprecated code

Build the cffi interface by running `python binaryen_build.py`

cmake -S . -B ../macos-arm64 -G Ninja -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=../macos-arm64/install -DCMAKE_OSX_ARCHITECTURES=arm64 -DBUILD_TESTS=OFF -DBUILD_TOOLS=OFF -DBUILD_STATIC_LIB=ON

cmake --build ../macos-arm64 -v --config Release --target install

cmake -S . -B ../macos-x86_64 -G Ninja -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=../macos-x86_64/install -DCMAKE_OSX_ARCHITECTURES=x86_64 -DBUILD_TESTS=OFF -DBUILD_TOOLS=OFF -DBUILD_STATIC_LIB=ON

cmake --build ../macos-x86_64 -v --config Release --target install