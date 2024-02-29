import subprocess
import re
import os

curr_dir = os.path.dirname(__file__)
header_path = os.path.join(curr_dir, "./binaryen-c.h")
output_path = os.path.join(curr_dir, "./binaryen-c.c")

if __name__ == "__main__":
    header = open(header_path, "r", encoding="utf-8").read()

    # Remove C standard library includes which cause errors if included
    lines = header.split("\n")
    libs = ["#include <stdbool.h>", "#include <stddef.h>", "#include <stdint.h>"]
    header = "\n".join([line for line in lines if line not in libs])

    # Run the C pre-processor on the Binaryen header file
    pre_processor = subprocess.run(
        ["cpp", "-nostdinc", "-E", "-P", f"-I{curr_dir}"],
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
    
    with open(output_path, "x", encoding="utf-8") as output:
        output.write(header)
