from cffi import FFI

ffibuilder = FFI()
import os

dirname = os.path.dirname(__file__)
source_path = os.path.join(dirname, "./libbinaryen/binaryen-py.h")
header_path = os.path.join(dirname, "./libbinaryen/binaryen-c.h")
library_mac_arm = os.path.join(dirname, "./libbinaryen/arm64-macos")
library_mac = os.path.join(dirname, "./libbinaryen/x86_64-macos")
library_linux = os.path.join(dirname, "./libbinaryen/x86_64-linux")
library_windows = os.path.join(dirname, "./libbinaryen/x86_64-windows")

source = open(source_path, encoding="utf-8")

ffibuilder.cdef(source.read())

ffibuilder.set_source(
    "_binaryen_cffi",
    f"""
     #include "{header_path}"   // the C header of the library
""",
    libraries=["binaryen"],
    library_dirs=[library_mac_arm]
#     , library_mac, library_linux, library_windows
)

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
