# Building or updating Binaryen.py

set -x BINARYEN_PY_ROOT (pwd)
$env:BINARYEN_PY_ROOT=pwd

STOP REQUIRING SETTING ENVIRONMENT VARIABLE, COMPUTE IF LOCAL OR JUST INCLUDE IT

1. For Windows and Linux 


cmake -S . -B ../macos-arm64 -G Ninja -DCMAKE_INSTALL_PREFIX=../macos-arm64/install -DCMAKE_OSX_ARCHITECTURES=arm64 -DCMAKE_BUILD_TYPE=Release -DBUILD_TESTS=OFF -DBUILD_TOOLS=OFF -DBUILD_STATIC_LIB=ON
cmake --build ../macos-arm64 -v --config Release --target install

cmake -S . -B ../macos-x86_64 -G Ninja -DCMAKE_INSTALL_PREFIX=../macos-arm64/install -DCMAKE_OSX_ARCHITECTURES=x86_64 -DCMAKE_BUILD_TYPE=Release -DBUILD_TESTS=OFF -DBUILD_TOOLS=OFF -DBUILD_STATIC_LIB=ON
cmake --build ../macos-x86_64 -v --config Release --target install


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
