from cffi import FFI
import shutil
import re
import subprocess
import platform

ffibuilder = FFI()
import os

libbinaryen_dir = os.path.dirname(__file__)
header_path = os.path.join(libbinaryen_dir, "./binaryen-c.h")
wasm_def_path = os.path.join(libbinaryen_dir, "./wasm-delegations.def")

def copy_header():
    """Copy the necessary binaryen header files into the package.
    """
    if not os.path.isfile(header_path):
        print("COPYING HEADER")
        header_source = os.path.join(libbinaryen_dir, "./binaryen/src/binaryen-c.h")
        shutil.copy(header_source, header_path)

    if not os.path.isfile(wasm_def_path):
        print("COPYING DELEGATIONS")
        wasm_def_source = os.path.join(libbinaryen_dir, "./binaryen/src/wasm-delegations.def")
        shutil.copy(wasm_def_source, wasm_def_path)

# FIXME: This is broken on Windows
def create_c_source():
    """Use the binaryen header file to generate a C source file with every function prototype. This allows Python to execute binaryen functions.
    

    Returns:
        str: The C source file
    """    
    copy_header()

    header = open(header_path, "r", encoding="utf-8").read()
    temp = os.path.join(libbinaryen_dir, "tmp")

    # Remove C standard library includes which cause errors if included
    lines = header.split('\n')
    libs = ["#include <stdbool.h>", "#include <stddef.h>", "#include <stdint.h>"]
    header = '\n'.join([line for line in lines if line not in libs])

    with open(temp, "w", encoding="utf-8") as t:
        t.write(header)

    # Run the C pre-processor on the Binaryen header file
    pre_processor = subprocess.run(["cpp", "-nostdinc", "-E", "-P", temp], input=header.encode("utf-8"), check=True, stdout=subprocess.PIPE)

    header = pre_processor.stdout.decode(encoding='utf-8')
    os.remove(temp)

    # Clean up build artifacts & comments
    header = re.sub(r'//.*\n', '', header)
    header = re.sub(r'##', '', header)
    header = re.sub(r';;', ';', header)
    
    # Clean up new lines
    header = re.sub(r'\n', ' ', header)
    header = re.sub(r'  *', ' ', header)
    header = re.sub(r'; ', ';\n', header)

    # Remove deprecated code
    header = re.sub(r'^__attribute__\(\(deprecated\)\).*$', '', header, flags=re.MULTILINE)
    print("GENERATED C SOURCE FILE")
    return header

def get_target():
    if platform.system() == "Linux":
        return "linux-x86_64"

    if platform.system() == "Windows":
        return "windows-x86_64"

    if platform.system() == "Darwin":
        if platform.machine() == "arm64":
            return "macos-arm64"
        else:
            return "macos-x86_64"

def compile_binaryen():
    """Compile binaryen to platform specific static libraries, that can then be linked to python.
    """
    src_dir = os.path.join(libbinaryen_dir, "binaryen")

    # Assert correct binaryen version is used
    git_describe = subprocess.run(["git", "describe", "--tags", "--abbrev=0"], check=True, stdout=subprocess.PIPE, cwd=src_dir)
    git_version = git_describe.stdout.decode(encoding='utf-8').rstrip()

    version_file = open(os.path.join(libbinaryen_dir,"version.txt"), encoding="utf-8").read()
    required_version = "version_" + version_file

    assert git_version == required_version

    # Construct platform specific build arguments
    platform_specifc_args = ['-G', 'Ninja']

    if platform.system() == "Windows":
        # Don't use Ninja on windows
        platform_specifc_args = []

    if platform.system() == "Darwin":
        if platform.machine() == "arm64":
            platform_specifc_args.append("-DCMAKE_OSX_ARCHITECTURES=arm64")
        else:
            platform_specifc_args.append("-DCMAKE_OSX_ARCHITECTURES=x86_64")

    target_dir = os.path.join(libbinaryen_dir, get_target()) # type: ignore
    comiler_args = ['cmake', '-S', src_dir, '-B', target_dir, f"-DCMAKE_INSTALL_PREFIX={target_dir}/install", "-DCMAKE_BUILD_TYPE=Release", "-DBUILD_TESTS=OFF", "-DBUILD_TOOLS=OFF", "-DBUILD_STATIC_LIB=ON"]

    subprocess.run(comiler_args, check=True)
    subprocess.run(["cmake", "--build", target_dir, "-v", "--config", "Release", "--target", "install"], check=True)


if __name__ == "__main__":
    # Save and restore current directory
    current_directory = os.getcwd()
    os.chdir(libbinaryen_dir)

    compile_binaryen()

    ffibuilder.cdef(create_c_source())
    ffibuilder.set_source(
        "binaryen_cffi",
        f"""
        #include "{header_path}"
    """,
        libraries=["binaryen"],
        library_dirs=[os.path.join(libbinaryen_dir,f"{get_target()}/install/lib/")]
    )
    ffibuilder.compile(verbose=True)

    os.chdir(current_directory)
