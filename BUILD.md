# Building or updating Binaryen.py

1. Put the new precompiled dynamic libraries in `binaryen/libbinaryen` for all architectures for all operating systems
2. Update the `binaryen-c.h` and `wasm-delegations.def`
3. Delete the existing `binaryen-c.c` and run `python binaryen/libbinaryen/create_cdef.py`
4. Replace any unions in the ouputed `binaryen-c.c` to the largest of their contents
5. Copy the contents of `binaryen-c.c` to the `cdef` variable in `binaryen_build.py`
6. *Optional* run `python binaryen_build.py`

## Replacing unions

Replace all unions so that the largest type of the union is used instead. CFFI can't do this automatically without the full C source.

```c
// Change
struct BinaryenLiteral {
  uintptr_t type;
  union {
    int32_t i32;
    int64_t i64;
    float f32;
    double f64;
    uint8_t v128[16];
    const char* func;
  };
};
// to
struct BinaryenLiteral {
  uintptr_t type;
  uint8_t v128[16];
};
```
