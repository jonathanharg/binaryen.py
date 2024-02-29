import binaryen as b
from binaryen.types import NULL, Int32, TypeNone

mod = b.Module()
mod.set_feature(b.Feature.Strings | b.Feature.GC | b.Feature.ReferenceTypes)
mod.add_function_import(
    b"print",
    b"wasi_snapshot_preview1",
    b"fd_write",
    b.types.create([Int32, Int32, Int32, Int32]),
    Int32,
)


# length = Object()
# length.ref = b.lib.BinaryenStringMeasure(
#             mod.ref, b.operations.StringMeasureUTF8(), str_const.ref
#         )

# # str_ptr = Object()
# # str_ptr.ref = b.lib.BinaryenStringNewGetPtr(str_const.ref)
# # str_length = Object()
# # str_length.ref = b.lib.BinaryenStringNewGetLength(str_const.ref)
# array = mod.array_new_fixed(
#     b.lib.BinaryenHeapTypeArray(),
#     [
#         mod.mod.i32(b.literal.int32(0)),
#         mod.mod.i32(b.literal.int32(1)),
#         mod.mod.i32(b.literal.int32(2)),
#         length,
#     ],
# )
# # test.ref = b.lib.BinaryenStore(mod.ref, 4, 0, 0, mod.i32(0).ref, mod.i32(9).ref, i32, b.NULL)
# # test2 = Object()
# # test2.ref = b.lib.BinaryenStore(mod.ref, 4, 0, 2, mod.i32(4).ref, mod.i32(12).ref, i32, b.NULL)
# # call = mod.call(b"print", [mod.i32(1), mod.i32(0), mod.i32(1), mod.i32(20)], i32)
# # drop = Object()
# # drop.ref = b.lib.BinaryenDrop(mod.ref, call.ref)
# # block = mod.block(b"test", [test, test2, call], none)
# block = mod.block(b"test", [str_const, array], none)
# func = mod.add_function(b"main", None, None, [], block)
# b.lib.BinaryenSetStart(mod.ref, func.ref)
# mod.auto_drop()
# # mod.optimize()
# mod.validate()
# # print("===============================")
# # mod.print()
# # mod.write_text("hello_world")


# Store "Hello Wasm!\n" at an offset of 8 with a size of 12

# | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
#                                   H   e   l    l    o    \    W    a    s    m    !    \n   \0
mod.set_memory(
    1,
    1,
    b"memory",
    [b"Hello Wasm!\n"],
    [False],
    [mod.i32(8)],
    [12],
    False,
    False,
    b"wasmmemory",
)

str_const = mod.string_const(b"Hello Wasm GC!\n")
str_loc = mod.local_set(0, str_const)
str_get = mod.local_get(0, Int32)
leng_ref = b.lib.BinaryenStringMeasure(
    mod.ref, b.operations.StringMeasureUTF8(), str_get.ref
)
leng = b.Expression(leng_ref)

# Pointer to start of string and length of string
# string_pointer = mod.store(4, 0, 0, mod.i32(0), mod.i32(8), i32, NULL)
string_pointer = mod.store(4, 0, 0, mod.i32(0), mod.i32(8), Int32, NULL)
# string_length = mod.store(4,0,2,mod.i32(4), mod.i32(12), i32, NULL)
string_length = mod.store(4, 0, 2, mod.i32(4), leng, Int32, NULL)
# | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
#  [      8      ] [      12     ]  H   e   l    l    o    \    W    a    s    m    !    \n   \0

# Args:
# - file_descriptor: 1 for stdout
# - *iovs - The pointer to the iov array, which is stored at memory location 0
# - iovs_len - We're printing 1 string stored in an iov - so one.
# - nwritten - A place in memory to store the number of bytes written
call = mod.call(b"print", [mod.i32(1), mod.i32(0), mod.i32(1), mod.i32(20)], Int32)
# block = mod.block(b"test", [string_pointer, string_length, call], none)
block = mod.block(b"test", [str_loc, string_pointer, string_length, call], TypeNone)
func = mod.add_function(b"main", None, None, [], block)


mod.add_function_export(b"main", b"main")
# mod.set_start(func)

mod.auto_drop()
# mod.optimize()
mod.validate()

# mod.print()
mod.write_text("hello_world_bin.wat")
mod.write_binary("hello_world_bin.wasm")
