from setuptools import setup

setup(
    cffi_modules=["binaryen/binaryen_build.py:ffibuilder"],
)
