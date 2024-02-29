import binaryen as b
from binaryen.types import Int32, TypeNone

mod = b.Module()
mod.add_function_import(b"log", b"env", b"printf", Int32, TypeNone)
mod.add_function(
    b"logi32",
    None,
    None,
    [Int32],
    mod.block(
        None,
        [
            mod.call(b"log", [mod.i32(7)], TypeNone),
        ],
        TypeNone,
    ),
)
mod.print()
mod.validate()
mod.write_binary("import.wasm")
