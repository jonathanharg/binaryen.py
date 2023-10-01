import binaryen as b

# mod.const(b.lib.BinaryenLiteralInt32(8)).ref
mod = b.Module()
mod.add_function_import(
    b"print",
    b"wasi_unstable",
    b"fd_write",
    b.type_create([b.i32, b.i32, b.i32, b.i32]),
    b.i32,
)
# b.lib.BinaryenSetMemory(mod.ref,1,1,b"memory", [b"Hello WASM!\n"], [False], [b.NULL], [12], 1, False, False, b"wasmmemory")
def const(x: int):
    return mod.const(b.lib.BinaryenLiteralInt32(x))


s = b.ffi.new("char[]", b"Hello WASM!\n")
b.lib.BinaryenSetMemory(
    mod.ref,
    1,
    1,
    b"memory",
    [s],
    [False],
    [const(9).ref],
    [12],
    1,
    False,
    False,
    b"wasmmemory",
)
# b.lib.BinaryenStore(mod.ref, uint32_t bytes, uint32_t offset, uint32_t align, BinaryenExpressionRef ptr, BinaryenExpressionRef value, BinaryenType type, const char* memoryName)
# b.lib.BinaryenStore(mod.ref, 8, 0, 0, const(0).ref, const(9).ref, b.i32, b"iov_base")
class Object(object):
    pass


test = Object()
test.ref = b.lib.BinaryenStore(
    mod.ref, 4, 0, 0, const(0).ref, const(9).ref, b.i32, b.NULL
)
test2 = Object()
test2.ref = b.lib.BinaryenStore(
    mod.ref, 4, 0, 2, const(4).ref, const(12).ref, b.i32, b.NULL
)
call = mod.call(b"print", [const(1), const(0), const(1), const(20)], b.i32)
drop = Object()
# drop.ref = b.lib.BinaryenDrop(mod.ref, call.ref)
block = mod.block(b"test", [test, test2, call], b.none)
func = mod.add_function(b"main", None, None, [], block)
b.lib.BinaryenSetStart(mod.ref, func)
b.lib.BinaryenModuleAutoDrop(mod.ref)
# mod.optimize()
# mod.validate()
mod.print()
mod.write_text("hello_world")
