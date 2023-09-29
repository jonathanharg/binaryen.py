import platform
from typing import Any, cast
from ._binaryen_cffi import ffi

__macos_error = """You either do not have the binaryen library installed, or it is not in your standard C library path.

Recommended: Using the brew package manager (https://brew.sh/) run brew install binaryen

Alternatively add the precompiled libbinaryen.dylib from https://github.com/WebAssembly/binaryen/releases to your path.
"""

__windows_error = """You either do not have the binaryen library installed, or it is not in your standard C library path.

Add the precompiled libbinaryen.dll from https://github.com/WebAssembly/binaryen/releases to your path.
"""

__linux_error = """You either do not have the binaryen library installed, or it is not in your standard C library path.

Recommended: Use your distributions package manager to install binaryen.

Alternatively add the precompiled libbinaryen.so from https://github.com/WebAssembly/binaryen/releases to your path.
"""

__lib_string = ""
__error_message = ""
if platform.system() == "Linux":
    __error_message = __linux_error
    __lib_string = "libbinaryen.so"
if platform.system() == "Windows":
    __error_message = __windows_error
    __lib_string = "libbinaryen.dll"
if platform.system() == "Darwin":
    __error_message = __macos_error
    __lib_string = "libbinaryen.dylib"

try:
    lib = cast(Any, ffi.dlopen(__lib_string))
except OSError as error:
    raise OSError(__error_message) from error
