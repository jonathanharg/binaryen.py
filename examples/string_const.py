import binaryen as b
from binaryen.types import NULL, i32, none

mod = b.Module()
mod.set_feature(b.Feature.Strings | b.Feature.GC | b.Feature.ReferenceTypes)

mod.set_memory(
    0,
    1,
    b"memory",
    [],
    [],
    [],
    [],
    False,
    False,
    b"memory",
)

str_const = mod.string_const(b"Hello Wasm!\n")
str_var_set = mod.local_set(0, str_const)
str_var = mod.local_get(0, b.types.stringref)

# str2 = str_const.copy(mod)
# str2_var_set = mod.local_set(1, str2)
# str2_var = mod.local_get(1, b.types.stringref)

# ret = mod.Return(str_const)

# concat = b.lib.BinaryenStringConcat(mod.ref, str_var.ref, str2_var.ref)

# count = mod.string(b.operations.StringEqEqual(), str_const, str_2)
count_ref = b.lib.BinaryenStringMeasure(
    mod.ref, b.operations.StringMeasureUTF8(), str_var.ref
)
count = b.Expression(count_ref)
# # ret_count = mod.Return(count)

# block = mod.block(b"test", [str_var_set, str2_var_set,count], b.types.auto)
block = mod.block(b"test", [str_var_set, count], b.types.auto)

# func = mod.add_function(b"main", None, i32, [b.types.stringref,b.types.stringref], block)
func = mod.add_function(b"main", None, i32, [b.types.stringref], block)

mod.add_function_export(b"main", b"main")
# mod.set_start(func)

mod.auto_drop()
# mod.optimize()
mod.validate()

# mod.print()
mod.write_text("string_const.wat")
mod.write_binary("string_const.wasm")
