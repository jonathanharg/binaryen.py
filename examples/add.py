import binaryen
from binaryen.types import i32, none


# Equivalent python function
def add(x, y):
    return x + y


myModule = binaryen.Module()
myModule.add_function(
    b"add",
    binaryen.types.create([i32, i32]),
    i32,
    [i32],
    myModule.block(
        None,
        [
            myModule.local_set(
                2,
                myModule.binary(
                    binaryen.operations.AddInt32(),
                    myModule.local_get(0, i32),
                    myModule.local_get(1, i32),
                ),
            ),
            myModule.Return(myModule.local_get(2, i32)),
        ],
        none,
    ),
)

if not myModule.validate():
    raise Exception("Invalid module!")

myModule.add_function_export(b"add", b"add")

myModule.optimize()

myModule.write_text("out.wat")

# Can either print with `myModule.print()` or write to file with `myModule.write_binary(__file__)`

# Run the written binary with `wasmtime add.wasm --invoke add 85 20`
