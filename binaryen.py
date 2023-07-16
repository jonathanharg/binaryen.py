from cffi import FFI


ffibuilder = FFI()
ffibuilder.cdef(
    """
typedef struct BinaryenModule* BinaryenModuleRef;;
             BinaryenModuleRef BinaryenModuleCreate(void);
"""
)
ffibuilder.set_source(
    "_binaryen_cffi",
"""
#include "binaryen-c.h"
""",)

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
