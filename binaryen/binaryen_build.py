import cffi
import os
import platform
from pathlib import Path

host_platform = platform.system().lower()
if host_platform == "Darwin":
    host_platform = "macos"

host_machine = platform.machine().lower()

root_path_override = os.environ.get("BINARYEN_PY_ROOT")

print("==== BUILD ====")
print(f"Building binaryen.py for {host_machine}-{host_platform}")

file_path = Path(__file__).resolve().parent.parent
root_path = Path(file_path) / f"binaryen/libbinaryen/{host_machine}-{host_platform}/"

if root_path_override is not None:
    root_path = Path(root_path_override).resolve()
    print(f"INFO: Overriding root path to {root_path.absolute()}")


def valid(path):
    return "valid" if path else "INVALID!"


include_path = root_path / "include"
cdef_path = include_path / "binaryen-c.c"
header_path = include_path / "binaryen-c.h"
wasm_path = include_path / "wasm-delegations.def"
lib_path = root_path / "lib"

print("== Paths ==")
print(f"include    {valid(include_path.is_dir())}    {include_path.absolute()}")
print(f"binaryen-c.h   {valid(header_path.is_file())}    {header_path.absolute()}")
print(f"delegations   {valid(wasm_path.is_file())}    {wasm_path.absolute()}")
print(f"binaryen-c.c   {valid(cdef_path.is_file())}    {cdef_path.absolute()}")

print(f"lib   {valid(lib_path.is_dir())}    {lib_path.absolute()}")

ffibuilder = cffi.FFI()
ffibuilder.set_source(
    "binaryen._binaryen",
    '#include "binaryen-c.h"',
    libraries=["binaryen"],
    library_dirs=[str(lib_path.absolute())],
    include_dirs=[str(include_path.absolute())],
    language="c++",
)

with open(cdef_path, "r", encoding="utf-8") as file:
    cdef = file.read()
    ffibuilder.cdef(cdef)

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
