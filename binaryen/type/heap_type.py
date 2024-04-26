from .. import internals as __internals
from .._binaryen import lib as __lib


def is_basic(heap_type: __internals.BinaryenHeapType | __internals.BinaryenType):
    return bool(__lib.BinaryenHeapTypeIsBasic(heap_type))


def is_signature(heap_type: __internals.BinaryenHeapType):
    return bool(__lib.BinaryenHeapTypeIsSignature(heap_type))


def is_struct(heap_type: __internals.BinaryenHeapType):
    return bool(__lib.BinaryenHeapTypeIsStruct(heap_type))


def is_array(heap_type: __internals.BinaryenHeapType):
    return bool(__lib.BinaryenHeapTypeIsArray(heap_type))


def is_bottom(heap_type: __internals.BinaryenHeapType):
    return bool(__lib.BinaryenHeapTypeIsBottom(heap_type))


def get_bottom(heap_type: __internals.BinaryenHeapType) -> __internals.BinaryenHeapType:
    return __lib.BinaryenHeapTypeGetBottom(heap_type)


def is_sub_type(
    left: __internals.BinaryenHeapType, right: __internals.BinaryenHeapType
):
    return bool(__lib.BinaryenHeapTypeIsSubType(left, right))
