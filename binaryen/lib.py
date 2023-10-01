import platform
from typing import Any, cast
import os
from ._binaryen_cffi import ffi

__dirname = os.path.dirname(__file__)

__lib_string = ""
if platform.system() == "Linux":
    __lib_string = os.path.join(__dirname, "./libbinaryen/x86_64-linux/libbinaryen.a")
if platform.system() == "Windows":
    __lib_string = os.path.join(__dirname, "./libbinaryen/x86_64-windows/binaryen.lib")
if platform.system() == "Darwin":
    if platform.machine() == "arm64":
        __lib_string = os.path.join(
            __dirname, "./libbinaryen/arm64-macos/libbinaryen.dylib"
        )
    else:
        __lib_string = os.path.join(
            __dirname, "./libbinaryen/x86_64-macos/libbinaryen.dylib"
        )

lib = cast(Any, ffi.dlopen(__lib_string))
