import cffi
import os

ffibuilder = cffi.FFI()
ffibuilder.set_source("_binaryen_cffi", None)

dirname = os.path.dirname(__file__)
header_path = os.path.join(dirname, "./libbinaryen/binaryen-py.h")

header = open(header_path, encoding="utf-8")

ffibuilder.cdef(header.read())

if __name__ == "__main__":
    ffibuilder.compile()
