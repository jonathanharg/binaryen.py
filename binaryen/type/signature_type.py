from .. import internals as __internals
from .._binaryen import lib as __lib


def get_params(heap_type: __internals.BinaryenHeapType) -> __internals.BinaryenType:
    return __lib.BinaryenSignatureTypeGetParams(heap_type)


def get_results(heap_type: __internals.BinaryenHeapType) -> __internals.BinaryenType:
    return __lib.BinaryenSignatureTypeGetParams(heap_type)
