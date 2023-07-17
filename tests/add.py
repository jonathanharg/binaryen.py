import binaryen

def add(x, y):
    return x + y

myModule = binaryen.Module()
myModule.add_function(
    b"add",
    binaryen.type_create([binaryen.i32, binaryen.i32]),
    binaryen.i32,
    [binaryen.i32],
    myModule.block(
        None,
        [
            myModule.local_set(
                2,
                myModule.binary(
                    binaryen.lib.BinaryenAddInt32(),
                    myModule.local_get(0, binaryen.i32),
                    myModule.local_get(1, binaryen.i32),
                ),
            ),
            myModule.Return(myModule.local_get(2, binaryen.i32)),
        ],
        binaryen.none,
    ),
)

if not myModule.validate():
    raise Exception("Invalid module!")

myModule.add_function_export(b"add", b"add")

myModule.optimize()
myModule.print()
# myModule.write_binary(__file__)

# Test with: wasmtime add10.wasm --invoke at 85
