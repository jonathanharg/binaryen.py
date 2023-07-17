import binaryen

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
            myModule.return_(myModule.local_get(2, binaryen.i32)),
        ],
        binaryen.none,
    ),
)

if not myModule.validate():
    raise Exception("Invalid module!")

myModule.add_function_export(b"add", b"add")

test = myModule.emit_text()
print(test)
test2 = myModule.emit_binary()
print(test2)

myModule.write_text(__file__)
myModule.write_binary(__file__)

myModule.optimize()
# myModule.print()
