import binaryen
from binaryen.type import Int32


# Equivalent python function
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


mod = binaryen.Module()

n = mod.local_get(0, Int32)

condition = mod.binary(
    binaryen.operations.LeSInt32(),
    n,
    mod.i32(1),
)

n_minus_one = mod.binary(
    binaryen.operations.SubInt32(),
    n,
    mod.i32(1),
)

n_minus_two = mod.binary(
    binaryen.operations.SubInt32(),
    n,
    mod.i32(2),
)

mod.add_function(
    b"fib",
    Int32,
    Int32,
    [],
    mod.If(
        condition,
        mod.Return(n),
        mod.Return(
            mod.binary(
                binaryen.operations.AddInt32(),
                mod.call(
                    b"fib",
                    [n_minus_one],
                    Int32,
                ),
                mod.call(
                    b"fib",
                    [n_minus_two],
                    Int32,
                ),
            )
        ),
    ),
)

if not mod.validate():
    raise RuntimeError("Invalid module!")

mod.add_function_export(b"fib", b"fib")

mod.optimize()

mod.print()

# Run the written binary with `wasmtime --invoke fib fib.wasm 23`
