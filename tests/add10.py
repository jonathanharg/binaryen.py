import binaryen

def at(x):
    return x + 10

myModule = binaryen.Module()
myModule.add_function(
    b"at",
    binaryen.i32,
    binaryen.i32,
    [binaryen.i32],
    myModule.block(
        None,
        [
            myModule.local_set(
                1,
                myModule.binary(
                    binaryen.lib.BinaryenAddInt32(),
                    myModule.local_get(0, binaryen.i32),
                    myModule.const(binaryen.lib.BinaryenLiteralInt32(10)),
                ),
            ),
            myModule.return_(myModule.local_get(1, binaryen.i32)),
        ],
        binaryen.none,
    ),
)

if not myModule.validate():
    raise Exception("Invalid module!")

myModule.add_function_export(b"at", b"at")

myModule.optimize()
myModule.print()
# myModule.write_binary(__file__)

# Test with: wasmtime add10.wasm --invoke at 85
