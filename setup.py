from setuptools import setup

setup(
    cffi_modules=["scripts/binaryen_build.py:ffibuilder"],
)
