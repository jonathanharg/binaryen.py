import binaryen as b
from binaryen.types import i32, none

mod = b.Module()
mod.add_function_import(b"log", b"env", b"printf", i32, none)
mod.add_function(
    b"logi32",
    None,
    None,
    [i32],
    mod.block(
        None,
        [
            mod.call(b"log", [mod.const(b.literal.int32(7))], none),
        ],
        none,
    ),
)
mod.print()
mod.validate()
mod.write_binary("import.wasm")
