import binaryen
from binaryen.type import Int32, TypeNone


# Equivalent python function
def addTen(x):
    return x + 10


myModule = binaryen.Module()
myModule.add_function(
    b"addTen",
    Int32,
    Int32,
    [Int32],
    myModule.block(
        None,
        [
            myModule.local_set(
                1,
                myModule.binary(
                    binaryen.operations.AddInt32(),
                    myModule.local_get(0, Int32),
                    myModule.i32(10),
                ),
            ),
            myModule.Return(myModule.local_get(1, Int32)),
        ],
        TypeNone,
    ),
)

if not myModule.validate():
    raise Exception("Invalid module!")

myModule.add_function_export(b"addTen", b"addTen")

myModule.optimize()

myModule.print()

# Can either print with `myModule.print()` or write to file with `myModule.write_binary(__file__)`

# Run the written binary with `wasmtime addTen.wasm --invoke addTen 12`
