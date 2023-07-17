import binaryen


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
            myModule.return_(
                myModule.If(
                    myModule.binary(
                        binaryen.lib.BinaryenLeSInt32(),
                        myModule.local_get(0, binaryen.i32),
                        myModule.const(binaryen.lib.BinaryenLiteralInt32(1)),
                    ),
                    myModule.return_(myModule.local_get(0, binaryen.i32)),
                    myModule.return_(
                        myModule.binary(
                            binaryen.lib.BinaryenAddInt32(),
                            binaryen.lib.BinaryenCall(
                                myModule.ptr,
                                b"fib",
                                myModule.binary(
                                    binaryen.lib.BinaryenSubInt32(),
                                    myModule.local_get(0, binaryen.i32),
                                    myModule.const(binaryen.lib.BinaryenLiteralInt32(1)),
                                ),
                                1,
                                binaryen.i32,
                            ),
                            binaryen.lib.BinaryenCall(
                                myModule.ptr,
                                b"fib",
                                myModule.binary(
                                    binaryen.lib.BinaryenSubInt32(),
                                    myModule.local_get(0, binaryen.i32),
                                    myModule.const(binaryen.lib.BinaryenLiteralInt32(2)),
                                ),
                                1,
                                binaryen.i32,
                            ),
                        )
                    ),
                )
            )
        ],
        binaryen.none,
    ),
)

if not myModule.validate():
    raise Exception("Invalid module!")

myModule.print()
