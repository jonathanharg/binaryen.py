from .. import internals as __internals
from .._binaryen import lib as __lib


def get_num_fields(heap_type: __internals.BinaryenHeapType):
    return __lib.BinaryenStructTypeGetNumFields(heap_type)


def get_field_type(
    heap_type: __internals.BinaryenHeapType, index: int
) -> __internals.BinaryenType:
    return __lib.BinaryenStructTypeGetFieldType(heap_type, index)


def get_field_packed_type(
    heap_type: __internals.BinaryenHeapType, index: int
) -> __internals.BinaryenPackedType:
    return __lib.BinaryenStructTypeGetFieldPackedType(heap_type, index)


def is_field_mutable(heap_type: __internals.BinaryenHeapType, index: int):
    return bool(__lib.BinaryenStructTypeIsFieldMutable(heap_type, index))
