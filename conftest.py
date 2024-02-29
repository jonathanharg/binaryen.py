import pytest

import binaryen


@pytest.fixture(autouse=True)
def add_binaryen(doctest_namespace):
    doctest_namespace["binaryen"] = binaryen
