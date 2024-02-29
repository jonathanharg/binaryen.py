# Binaryen.py

Binaryen.py is a python wrapper for [Binaryen](https://github.com/WebAssembly/binaryen). Use this to create, optimise and interpret WebAssembly binaries in python.

## Installation

Install through PyPI.

```bash
pip install binaryen.py
```

## How To Use

Reference the [Binaryen header file](https://github.com/WebAssembly/binaryen/blob/main/src/binaryen-c.h) to understand how to use Binaryen. This package makes no significant changes to the Binaryen API, apart from creating more pythonic objects for Modules, Expressions and Functions.

## Missing Functions

You can still call any missing functions that haven't been implemented by the wrapper yet by calling them directly. To do this use `binaryen.lib.BinaryenFullFunctionName()` and call the full function name as described in the [Binaryen header file](https://github.com/WebAssembly/binaryen/blob/main/src/binaryen-c.h).
