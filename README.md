# Binaryen.py

Binaryen.py is a python wrapper for [Binaryen](https://github.com/WebAssembly/binaryen). Use this to create, optimise and interpret WebAssembly binaries in python.

## Installation

Install through PyPI.

```bash
pip install binaryen.py
```

Windows, Mac (Intel & ARM) and Linux (manylinux, musllinux) are supported.

### Build from source

1. (If upgrading binaryen version) Update `BINARYEN_VERSION` in `pyproject.toml` and `.github/workflows/build.yaml`
2. Run `bash scripts/build_libbinaryen.sh`
3. Run `python -m pip install -e .`, `cibuildwheel`, `python -m pip wheel .`,  or whichever supported build command you would prefer

## How To Use

```py
import binaryen
from binaryen.type import Int32, TypeNone


# Equivalent python function
def add(x, y):
    return x + y


mod = binaryen.Module()
mod.add_function(
    b"add",
    binaryen.type.create([Int32, Int32]),
    Int32,
    [Int32],
    mod.block(
        None,
        [
            mod.local_set(
                2,
                mod.binary(
                    binaryen.operations.AddInt32(),
                    mod.local_get(0, Int32),
                    mod.local_get(1, Int32),
                ),
            ),
            mod.Return(mod.local_get(2, Int32)),
        ],
        TypeNone,
    ),
)

if not mod.validate():
    raise RuntimeError("Invalid module!")

mod.add_function_export(b"add", b"add")

mod.optimize()

mod.print()
```

Results in the following Wasm

```wasm
(module
 (type $0 (func (param i32 i32) (result i32)))
 (export "add" (func $add))
 (func $add (; has Stack IR ;) (param $0 i32) (param $1 i32) (result i32)
  (i32.add
   (local.get $0)
   (local.get $1)
  )
 )
)
```

Reference the [Binaryen header file](https://github.com/WebAssembly/binaryen/blob/main/src/binaryen-c.h) to understand how to use Binaryen. This package makes no significant changes to how Binaryen is used. The majority of the work this module does is interoperating between C and Python and creating more pythonic classes for Modules, Expressions and Functions.

For more examples see [examples](examples/).

## Missing Functions

You can still call any missing functions that haven't been implemented by the wrapper yet by calling them directly. To do this use `binaryen.lib.BinaryenFullFunctionName()` and call the full function name as described in the [Binaryen header file](https://github.com/WebAssembly/binaryen/blob/main/src/binaryen-c.h).
