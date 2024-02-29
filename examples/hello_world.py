import binaryen as b
from binaryen.types import NULL, Int32, TypeNone

mod = b.Module()
mod.add_function_import(
    b"print",
    b"wasi_snapshot_preview1",
    b"fd_write",
    b.types.create([Int32, Int32, Int32, Int32]),
    Int32,
)

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

# Pointer to start of string and length of string
string_pointer = mod.store(4, 0, 0, mod.i32(0), mod.i32(8), Int32, NULL)
string_length = mod.store(4, 0, 2, mod.i32(4), mod.i32(12), Int32, NULL)
# | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
#  [      8      ] [      12     ]  H   e   l    l    o    \    W    a    s    m    !    \n   \0

# Args:
# - file_descriptor: 1 for stdout
# - *iovs - The pointer to the iov array, which is stored at memory location 0
# - iovs_len - We're printing 1 string stored in an iov - so one.
# - nwritten - A place in memory to store the number of bytes written
call = mod.call(b"print", [mod.i32(1), mod.i32(0), mod.i32(1), mod.i32(20)], Int32)
block = mod.block(b"test", [string_pointer, string_length, call], TypeNone)
func = mod.add_function(b"main", None, None, [], block)


mod.add_function_export(b"main", b"main")
# mod.set_start(func)

mod.auto_drop()
mod.optimize()
mod.validate()

mod.print()
mod.write_text("hello_world.wat")
mod.write_binary("hello_world.wasm")
