import binaryen as b

# mod.const(b.lib.BinaryenLiteralInt32(8)).ref

strings_flag = b.lib.BinaryenFeatureStrings()
reference_flag = b.lib.BinaryenFeatureReferenceTypes()
gc_flag = b.lib.BinaryenFeatureGC()
flags = strings_flag | gc_flag | reference_flag

mod = b.Module()
b.lib.BinaryenModuleSetFeatures(mod.ref, flags)
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


# s = b.ffi.new("char[]", b"Hello WASM!\n")
# b.lib.BinaryenSetMemory(mod.ref,1,1,b"memory", [s],[False],[const(9).ref],[12], 1, False, False, b"wasmmemory")


class Object(object):
    pass


str_const = Object()
str_const.ref = b.lib.BinaryenStringConst(mod.ref, b"Hello WASM!\n")
# str_ptr = Object()
# str_ptr.ref = b.lib.BinaryenStringNewGetPtr(str_const.ref)
# str_length = Object()
# str_length.ref = b.lib.BinaryenStringNewGetLength(str_const.ref)
array = Object()
array.ref = b.lib.BinaryenArrayNewFixed(
    mod.ref,
    b.lib.BinaryenHeapTypeArray(),
    [
        const(0).ref,
        const(1).ref,
        const(2).ref,
        b.lib.BinaryenStringMeasure(
            mod.ref, b.lib.BinaryenStringMeasureUTF8(), str_const.ref
        ),
    ],
    4,
)
# test.ref = b.lib.BinaryenStore(mod.ref, 4, 0, 0, const(0).ref, const(9).ref, b.i32, b.NULL)
# test2 = Object()
# test2.ref = b.lib.BinaryenStore(mod.ref, 4, 0, 2, const(4).ref, const(12).ref, b.i32, b.NULL)
# call = mod.call(b"print", [const(1), const(0), const(1), const(20)], b.i32)
# drop = Object()
# drop.ref = b.lib.BinaryenDrop(mod.ref, call.ref)
# block = mod.block(b"test", [test, test2, call], b.none)
block = mod.block(b"test", [str_const, array], b.none)
func = mod.add_function(b"main", None, None, [], block)
b.lib.BinaryenSetStart(mod.ref, func)
b.lib.BinaryenModuleAutoDrop(mod.ref)
# mod.optimize()
mod.validate()
print("===============================")
mod.print()
# mod.write_text("hello_world")
