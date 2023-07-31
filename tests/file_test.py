import binaryen


def test_complicated_features():
    module = binaryen.Module()
    assert module
