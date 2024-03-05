import binaryen
from binaryen.type import Int32, NotPacked


mod = binaryen.Module()
mod.set_feature(binaryen.Feature.GC | binaryen.Feature.ReferenceTypes)

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
        [
            set_array,
            array,
            mod.Return(mod.array_len(array))
        ],
        Int32,
    ),
)

mod.add_function_export(b"indexArray", b"indexArray")
mod.auto_drop()

# mod.optimize()

mod.print()
mod.write_text("array.wat")
mod.write_binary("array.wasm")


if not mod.validate():
    raise RuntimeError("Invalid module!")

# Can either print with `myModule.print()` or write to file with `myModule.write_binary(__file__)`

# Run the written binary with `wasmtime addTen.wasm --invoke addTen 12`
