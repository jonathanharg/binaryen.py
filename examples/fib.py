import binaryen

# Equivalent python function
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


myModule = binaryen.Module()
myModule.add_function(
    b"fib",
    binaryen.i32,
    binaryen.i32,
    [],
    myModule.block(
        None,
        [
            myModule.If(
                myModule.binary(
                    binaryen.lib.BinaryenLeSInt32(),
                    myModule.local_get(0, binaryen.i32),
                    myModule.const(binaryen.lib.BinaryenLiteralInt32(1)),
                ),
                myModule.Return(myModule.local_get(0, binaryen.i32)),
                myModule.Return(
                    myModule.binary(
                        binaryen.lib.BinaryenAddInt32(),
                        myModule.call(
                            b"fib",
                            [
                                myModule.binary(
                                    binaryen.lib.BinaryenSubInt32(),
                                    myModule.local_get(0, binaryen.i32),
                                    myModule.const(
                                        binaryen.lib.BinaryenLiteralInt32(1)
                                    ),
                                )
                            ],
                            binaryen.i32,
                        ),
                        myModule.call(
                            b"fib",
                            [
                                myModule.binary(
                                    binaryen.lib.BinaryenSubInt32(),
                                    myModule.local_get(0, binaryen.i32),
                                    myModule.const(
                                        binaryen.lib.BinaryenLiteralInt32(2)
                                    ),
                                )
                            ],
                            binaryen.i32,
                        ),
                    )
                ),
            )
        ],
        binaryen.none,
    ),
)

if not myModule.validate():
    raise Exception("Invalid module!")

myModule.add_function_export(b"fib", b"fib")

myModule.optimize()

# Can either print with `myModule.print()` or write to file with `myModule.write_binary(__file__)`

# Run the written binary with `wasmtime fib.wasm --invoke fib 23`
