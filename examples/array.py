import binaryen
from binaryen.type import Int32, NotPacked

# Enable WasmGC and reference types
mod = binaryen.Module()
mod.set_feature(binaryen.Feature.GC | binaryen.Feature.ReferenceTypes)

# Create the Array type
tb = binaryen.TypeBuilder(1)
tb.set_array_type(0, Int32, NotPacked, True)
Int32ArrayHeap = tb.build()[0]
Int32Array = binaryen.type.from_heap_type(Int32ArrayHeap, True)

contents = mod.array_new(Int32ArrayHeap, mod.i32(10), mod.i32(0))
set_array = mod.local_set(0, contents.copy(mod))
array = mod.local_get(0, Int32Array)

mod.add_function(
    b"indexArray",
    None,
    Int32,
    [Int32Array],
    mod.block(
        None,
        [set_array, array, mod.Return(mod.array_len(array))],
        Int32,
    ),
)

mod.add_function_export(b"indexArray", b"indexArray")
mod.auto_drop()

if not mod.validate():
    raise RuntimeError("Invalid module!")

mod.print()
