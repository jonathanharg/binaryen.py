from binaryen import NULL, Int32, Module, lib


module = Module()
params = lib.BinaryenTypeCreate([Int32, Int32], 2)
results = Int32
x = module.localGet(0, Int32)
y = module.localGet(1, Int32)
add = lib.BinaryenBinary(module.ptr, lib.BinaryenAddInt32(), x, y)
# adder = lib.BinaryenAddFunction(module.ptr, b"adder", params, results, NULL, 0, add)
adder = module.addFunction(b"adder", params, results, NULL, 0, add)
module.print()
module.dispose()
