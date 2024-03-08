import binaryen
from binaryen.type import Int32, TypeNone


# Equivalent python function
def addTen(x):
    return x + 10


mod = binaryen.Module()
mod.add_function(
    b"addTen",
    Int32,
    Int32,
    [Int32],
    mod.block(
        None,
        [
            mod.local_set(
                1,
                mod.binary(
                    binaryen.operations.AddInt32(),
                    mod.local_get(0, Int32),
                    mod.i32(10),
                ),
            ),
            mod.Return(mod.local_get(1, Int32)),
        ],
        TypeNone,
    ),
)

if not mod.validate():
    raise RuntimeError("Invalid module!")

mod.add_function_export(b"addTen", b"addTen")

mod.optimize()

mod.print()

# Run the written binary with `wasmtime --invoke addTen addTen.wasm 12`
