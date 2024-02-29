import binaryen
from binaryen.types import Int32, TypeNone


# Equivalent python function
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


myModule = binaryen.Module()
myModule.add_function(
    b"fib",
    Int32,
    Int32,
    [],
    myModule.block(
        None,
        [
            myModule.If(
                myModule.binary(
                    binaryen.operations.LeSInt32(),
                    myModule.local_get(0, Int32),
                    myModule.i32(1),
                ),
                myModule.Return(myModule.local_get(0, Int32)),
                myModule.Return(
                    myModule.binary(
                        binaryen.operations.AddInt32(),
                        myModule.call(
                            b"fib",
                            [
                                myModule.binary(
                                    binaryen.operations.SubInt32(),
                                    myModule.local_get(0, Int32),
                                    myModule.i32(1),
                                )
                            ],
                            Int32,
                        ),
                        myModule.call(
                            b"fib",
                            [
                                myModule.binary(
                                    binaryen.operations.SubInt32(),
                                    myModule.local_get(0, Int32),
                                    myModule.const(binaryen.literal.int32(2)),
                                )
                            ],
                            Int32,
                        ),
                    )
                ),
            )
        ],
        TypeNone,
    ),
)

if not myModule.validate():
    raise Exception("Invalid module!")

myModule.add_function_export(b"fib", b"fib")

myModule.optimize()

myModule.print()

# Can either print with `myModule.print()` or write to file with `myModule.write_binary(__file__)`

# Run the written binary with `wasmtime fib.wasm --invoke fib 23`
