# Building or updating Binaryen.py

1. Put the new precompiled dynamic libraries in `binaryen/libbinaryen` for all architectures for all operating systems
2. Update the `binaryen-c.h` and `wasm-delegations.def`
3. Delete the existing `binaryen-c.c` and run `python binaryen/libbinaryen/create_cdef.py`
4. Replace any unions in the ouputed `binaryen-c.c` to the largest of their contents

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

*Optional* run `python binaryen_build.py`
