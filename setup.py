from setuptools import setup, find_packages

setup(
    packages=find_packages(),
    install_requires=['cffi'],
    package_data={'libbinaryen': ['libbinaryen/binaryen_cffi.cpython-311-darwin.so']},
)