from ._binaryen import ffi
import platform
import os

def get_target():
    if platform.system() == "Linux":
        if platform.machine() == 'aarch64':
            return "linux-aarch64.a"
        else:
            return "linux-x86_64.a"

    if platform.system() == "Windows":
        return "windows-x86_64.lib"

    if platform.system() == "Darwin":
        if platform.machine() == "arm64":
            return "macos-arm64.dylib"
        else:
            return "macos-x86_64.dylib"
        
curr_dir = os.path.dirname(__file__)
dll_path = os.path.join(curr_dir, f"libbinaryen/{get_target()}")

lib = ffi.dlopen(dll_path)