import cffi


ffibuilder = cffi.FFI()
ffibuilder.set_source("_binaryen_cffi", None)

header = open("./libbinaryen/binaryen-py.h", encoding="utf-8")

ffibuilder.cdef(header.read())

if __name__ == "__main__":
    ffibuilder.compile()
