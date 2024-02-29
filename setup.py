from setuptools import setup

setup(
    setup_requires=["cffi>=1.16.0"],
    cffi_modules=["binaryen/binaryen_build.py:ffibuilder"],
    install_requires=["cffi>=1.16.0"],
    package_data={
        "binaryen": ["libbinaryen/*.dylib", "libbinaryen/*.a", "libbinaryen/*.lib"]
    },
)
