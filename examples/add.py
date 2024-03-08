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
mod.write_binary("add.wasm")
# You can print the module with `mod.print()`
# Write it to a text format with `mod.write_text("fileName.wat")`
# Write it to a binary format with `mod.write_binary("fileName.wasm")`

# Run the written binary with `wasmtime --invoke add add.wasm 85 20`
