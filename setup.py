from setuptools import find_packages, setup

setup(
    packages=find_packages(),
    install_requires=["cffi"],
    package_data={"libbinaryen": ["libbinaryen/binaryen_cffi.cpython-311-darwin.so"]},
    # cffi_modules=["binaryen/libbinaryen/build.py:ffibuilder"],
)
