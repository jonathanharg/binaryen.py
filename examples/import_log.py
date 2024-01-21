import binaryen as b

# mod.const(b.lib.BinaryenLiteralInt32(8)).ref
mod = b.Module()
mod.add_function_import(b"log", b"env", b"printf", b.i32, b.none)
mod.add_function(
    b"logi32",
    None,
    None,
    [b.i32],
    mod.block(
        None,
        [
            mod.call(b"log", [mod.const(b.lib.BinaryenLiteralInt32(7))], b.none),
        ],
        b.none,
    ),
)
mod.print()
mod.validate()
mod.write_binary("import.wasm")