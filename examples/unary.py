import binaryen

mod = binaryen.Module()

# f_sub = mod.unary(binaryen.operations.NegFloat32(), mod.f32(6.7))
f_sub = mod.unary(
    binaryen.operations.NegFloat32(), mod.local_get(0, binaryen.type.Float32)
)

mod.add_function(b"float_test", binaryen.type.Float32, binaryen.type.Float32, [], f_sub)
mod.add_function_export(b"float_test", b"float_test")

# i_sub = mod.binary(binaryen.operations.SubInt32(), mod.i32(0), mod.i32(10))
# i_sub = mod.binary(binaryen.operations.S, mod.i32(0), mod.local_get(0, binaryen.type.Int32))

mod.add_function(b"int_test", binaryen.type.Int32, binaryen.type.Int32, [], i_sub)
mod.add_function_export(b"int_test", b"int_test")

mod.optimize()

mod.print()
