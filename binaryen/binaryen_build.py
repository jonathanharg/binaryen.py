import cffi
import os
import platform
from pathlib import Path

root_path = os.environ["BINARYEN_PY_ROOT"]

if root_path is None:
    raise RuntimeError("Set BINARYEN_PY_ROOT environment variable to the root folder of binaryen.py")


lib_path = (Path(root_path)/"binaryen/libbinaryen")
cdef_path = (Path(root_path)/"binaryen/libbinaryen/binaryen-c.c")

if not lib_path.is_dir():
    raise RuntimeError("Cannot find libbinaryen folder, is BINARYEN_PY_ROOT set correctly?")

if not cdef_path.is_file():
    raise RuntimeError("Cannot find binaryen-c.c, have you run create_cdef.py?")

lib_path = str(lib_path)

ffibuilder = cffi.FFI()
ffibuilder.set_source("binaryen._binaryen", "#include \"binaryen-c.h\"", libraries=["binaryen"], library_dirs=[lib_path], include_dirs=[lib_path], language="c++")

with open(cdef_path, "r", encoding="utf-8") as file:
    cdef = file.read()
    ffibuilder.cdef(cdef)

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
