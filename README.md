# Binaryen.py

Binaryen.py is a python wrapper for [Binaryen](https://github.com/WebAssembly/binaryen). Use this to create, optimise and interpret WebAssembly binaries in python.

## Installation

Install through PyPI.

```bash
pip install binaryen.py
```

## Test

```bash
pytest --doctest-modules --doctest-continue-on-failure --ignore=binaryen/libbinaryen/binaryen --ignore=binaryen/libbinaryen/macos-arm
```

## Format

```bash
black --extend-exclude binaryen/_binaryen_cffi.py .
```

## Docs

```bash
mkdocs serve
```

## Build cffi

Build the cffi interface by running `python binaryen/libbinaryen/build.py`
