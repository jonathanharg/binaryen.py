import binaryen as b
from binaryen.types import i32, none

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
    b.types.create([i32, i32, i32, i32]),
    i32,
)
# b.lib.BinaryenSetMemory(mod.ref,1,1,b"memory", [b"Hello WASM!\n"], [False], [b.NULL], [12], 1, False, False, b"wasmmemory")

# s = b.ffi.new("char[]", b"Hello WASM!\n")
# b.lib.BinaryenSetMemory(mod.ref,1,1,b"memory", [s],[False],[const(9).ref],[12], 1, False, False, b"wasmmemory")


class Object(object):
    pass

str_const = mod.string_const(b"Hello WASM!\n")

length = Object()
length.ref = b.lib.BinaryenStringMeasure(
            mod.ref, b.operations.StringMeasureUTF8(), str_const.ref
        )

# str_ptr = Object()
# str_ptr.ref = b.lib.BinaryenStringNewGetPtr(str_const.ref)
# str_length = Object()
# str_length.ref = b.lib.BinaryenStringNewGetLength(str_const.ref)
array = mod.array_new_fixed(
    b.lib.BinaryenHeapTypeArray(),
    [
        mod.const(b.literal.int32(0)),
        mod.const(b.literal.int32(1)),
        mod.const(b.literal.int32(2)),
        length,
    ],
)
# test.ref = b.lib.BinaryenStore(mod.ref, 4, 0, 0, const(0).ref, const(9).ref, i32, b.NULL)
# test2 = Object()
# test2.ref = b.lib.BinaryenStore(mod.ref, 4, 0, 2, const(4).ref, const(12).ref, i32, b.NULL)
# call = mod.call(b"print", [const(1), const(0), const(1), const(20)], i32)
# drop = Object()
# drop.ref = b.lib.BinaryenDrop(mod.ref, call.ref)
# block = mod.block(b"test", [test, test2, call], none)
block = mod.block(b"test", [str_const, array], none)
func = mod.add_function(b"main", None, None, [], block)
b.lib.BinaryenSetStart(mod.ref, func.ref)
mod.auto_drop()
# mod.optimize()
mod.validate()
print("===============================")
mod.print()
# mod.write_text("hello_world")
