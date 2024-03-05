import cffi
import os
import platform
from pathlib import Path

root_path = os.environ.get("BINARYEN_PY_ROOT", None)

if root_path is None:
    # raise RuntimeError("Set BINARYEN_PY_ROOT environment variable to the root folder of binaryen.py")
    root_path = Path(__file__).resolve().parent.parent
    print(f"No path specified!!! Defaulting to: {root_path.absolute()}")


lib_path = (Path(root_path)/"binaryen/libbinaryen")
cdef_path = (Path(root_path)/"binaryen/libbinaryen/binaryen-c.c")
header_path = (Path(root_path)/"binaryen/libbinaryen/binaryen-c.h")

if not lib_path.is_dir():
    raise RuntimeError("Cannot find libbinaryen folder, is BINARYEN_PY_ROOT set correctly?")

if not cdef_path.is_file():
    raise RuntimeError("Cannot find binaryen-c.c, have you run create_cdef.py?")

library_str = str(lib_path.absolute())
print(f"LIBRARY DIR IS: {library_str}")

ffibuilder = cffi.FFI()
ffibuilder.set_source("binaryen._binaryen", "#include \"binaryen-c.h\"", libraries=["binaryen"], library_dirs=[library_str], include_dirs=[library_str], language="c++")

with open(cdef_path, "r", encoding="utf-8") as file:
    cdef = file.read()
    ffibuilder.cdef(cdef)

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
