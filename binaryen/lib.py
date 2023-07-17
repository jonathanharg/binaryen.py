import platform
from typing import Any, cast
from ._binaryen_cffi import ffi

__lib_string = ""
if platform.system() == "Linux":
    __lib_string = "libbinaryen.so"
if platform.system() == "Windows":
    __lib_string = "libbinaryen.dll"
if platform.system() == "Darwin":
    __lib_string = "libbinaryen.dylib"
lib = cast(Any, ffi.dlopen(__lib_string))
