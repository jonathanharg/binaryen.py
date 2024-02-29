from .. import internals as __internals
from .._binaryen import lib as __lib


def get_element_type(
    heap_type: __internals.BinaryenHeapType,
) -> __internals.BinaryenType:
    return __lib.BinaryenArrayTypeGetElementType(heap_type)


def get_element_packed_type(
    heap_type: __internals.BinaryenHeapType,
) -> __internals.BinaryenPackedType:
    return __lib.BinaryenArrayTypeGetElementPackedType(heap_type)


def is_element_mutable(heap_type: __internals.BinaryenHeapType):
    return bool(__lib.BinaryenArrayTypeIsElementMutable(heap_type))
