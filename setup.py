from setuptools import setup

setup(
    setup_requires=["cffi>=1.15.0"],
    cffi_modules=["binaryen/binaryen_build.py:ffibuilder"],
    install_requires=["cffi>=1.15.0"],
    # include_package_data=True
    # package_data={
    #     "binaryen": ["libbinaryen/binaryen-c.c","libbinaryen/binaryen-c.h", "libbinaryen/wasm-delegations.def", "libbinaryen/*.dylib", "libbinaryen/*.a", "libbinaryen/*.lib"]
    # },
)
