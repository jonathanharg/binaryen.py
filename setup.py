from setuptools import setup

setup(
    setup_requires=["cffi>=1.15.0"],
    cffi_modules=["binaryen/binaryen_build.py:ffibuilder"],
    install_requires=["cffi>=1.15.0"],
)
