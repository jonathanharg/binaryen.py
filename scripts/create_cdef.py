import re
import subprocess
import platform
from pathlib import Path

host_platform = platform.system().lower()
if host_platform == "Darwin":
    host_platform = "macos"

host_machine = platform.machine().lower()

include_dir = (Path(__file__).parent.parent / f"./binaryen/libbinaryen/{host_machine}-{host_platform}/include")
header_path = (include_dir /"./binaryen-c.h")
output_path =(include_dir / "./binaryen-c.c")

# Note: manually replace unions with the largest type (uint8_t v128[16];)

if __name__ == "__main__":
    header = open(header_path, "r", encoding="utf-8").read()

    # Remove C standard library includes which cause errors if included
    lines = header.split("\n")
    libs = ["#include <stdbool.h>", "#include <stddef.h>", "#include <stdint.h>"]
    header = "\n".join([line for line in lines if line not in libs])

    # Run the C pre-processor on the Binaryen header file
    pre_processor = subprocess.run(
        ["cpp", "-nostdinc", "-E", "-P", f"-I{include_dir}"],
        input=header.encode("utf-8"),
        check=True,
        stdout=subprocess.PIPE,
    )

    header = pre_processor.stdout.decode(encoding="utf-8")

    # Clean up build artifacts & comments
    header = re.sub(r"//.*\n", "", header)
    header = re.sub(r"##", "", header)
    header = re.sub(r";;", ";", header)

    # Clean up new lines
    header = re.sub(r"\n", " ", header)
    header = re.sub(r"  *", " ", header)
    header = re.sub(r"; ", ";\n", header)

    # Remove deprecated code
    header = re.sub(
        r"^__attribute__\(\(deprecated\)\).*$", "", header, flags=re.MULTILINE
    )

    with open(output_path, "w", encoding="utf-8") as output:
        output.write(header)
