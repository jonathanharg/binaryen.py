import cffi
import os

curr_dir = os.path.dirname(__file__)
cdef_path = os.path.join(curr_dir, "libbinaryen/binaryen-c.c")

ffibuilder = cffi.FFI()
ffibuilder.set_source("binaryen._binaryen", None)

with open(cdef_path, "r", encoding="utf-8") as file:
    cdef = file.read()
    ffibuilder.cdef(cdef)

if __name__ == "__main__":
    ffibuilder.compile()
