import binaryen

# Equivalent python function
def addTen(x):
    return x + 10


myModule = binaryen.Module()
myModule.add_function(
    b"addTen",
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
            myModule.Return(myModule.local_get(1, binaryen.i32)),
        ],
        binaryen.none,
    ),
)

if not myModule.validate():
    raise Exception("Invalid module!")

myModule.add_function_export(b"addTen", b"addTen")

myModule.optimize()

# Can either print with `myModule.print()` or write to file with `myModule.write_binary(__file__)`

# Run the written binary with `wasmtime addTen.wasm --invoke addTen 12`
