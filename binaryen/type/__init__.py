"""Core Binaryen types"""

from typing import cast as __cast

from .. import internals as __internals
from .._binaryen import ffi as __ffi
from .._binaryen import lib as __lib
from . import array_type, heap_type, signature_type, struct_type
from .to_str import to_str

# These "types" are actually integers representing the type
# e.g. none = 0, i32 = 2 etc.
# We cast these integers ("types") to python types which are actually just an empty class
# see internals.py
TypeNone = __cast(__internals.BinaryenType, __lib.BinaryenTypeNone())
Int32 = __cast(__internals.BinaryenType, __lib.BinaryenTypeInt32())
Int64 = __cast(__internals.BinaryenType, __lib.BinaryenTypeInt64())
Float32 = __cast(__internals.BinaryenType, __lib.BinaryenTypeFloat32())
Float64 = __cast(__internals.BinaryenType, __lib.BinaryenTypeFloat64())
Vec128 = __cast(__internals.BinaryenType, __lib.BinaryenTypeVec128())
Funcref = __cast(__internals.BinaryenType, __lib.BinaryenTypeFuncref())
Externref = __cast(__internals.BinaryenType, __lib.BinaryenTypeExternref())
Anyref = __cast(__internals.BinaryenType, __lib.BinaryenTypeAnyref())
Eqref = __cast(__internals.BinaryenType, __lib.BinaryenTypeEqref())
I31ref = __cast(__internals.BinaryenType, __lib.BinaryenTypeI31ref())
Structref = __cast(__internals.BinaryenType, __lib.BinaryenTypeStructref())
Arrayref = __cast(__internals.BinaryenType, __lib.BinaryenTypeArrayref())
Stringref = __cast(__internals.BinaryenType, __lib.BinaryenTypeStringref())
StringviewWTF8 = __cast(__internals.BinaryenType, __lib.BinaryenTypeStringviewWTF8())
StringviewWTF16 = __cast(__internals.BinaryenType, __lib.BinaryenTypeStringviewWTF16())
StringviewIter = __cast(__internals.BinaryenType, __lib.BinaryenTypeStringviewIter())
Nullref = __cast(__internals.BinaryenType, __lib.BinaryenTypeNullref())
NullExternref = __cast(__internals.BinaryenType, __lib.BinaryenTypeNullExternref())
NullFuncref = __cast(__internals.BinaryenType, __lib.BinaryenTypeNullFuncref())
Unreachable = __cast(__internals.BinaryenType, __lib.BinaryenTypeUnreachable())
Auto = __cast(__internals.BinaryenType, __lib.BinaryenTypeAuto())


def create(types: list[__internals.BinaryenType]) -> __internals.BinaryenType:
    return __lib.BinaryenTypeCreate(types, len(types))


# Number of arguments
def arity(binaryen_type: __internals.BinaryenType) -> int:
    return __lib.BinaryenTypeArity(binaryen_type)


# TODO: BinaryenTypeExpand: Can't do this, I have no idea how this works

NotPacked = __cast(__internals.BinaryenPackedType, __lib.BinaryenPackedTypeNotPacked())
PackedInt8 = __cast(__internals.BinaryenPackedType, __lib.BinaryenPackedTypeInt8())
PackedInt16 = __cast(__internals.BinaryenPackedType, __lib.BinaryenPackedTypeInt16())

HeapExt = __cast(__internals.BinaryenHeapType, __lib.BinaryenHeapTypeExt())
HeapFunc = __cast(__internals.BinaryenHeapType, __lib.BinaryenHeapTypeFunc())
HeapAny = __cast(__internals.BinaryenHeapType, __lib.BinaryenHeapTypeAny())
HeapEq = __cast(__internals.BinaryenHeapType, __lib.BinaryenHeapTypeEq())
HeapI31 = __cast(__internals.BinaryenHeapType, __lib.BinaryenHeapTypeI31())
HeapStruct = __cast(__internals.BinaryenHeapType, __lib.BinaryenHeapTypeStruct())
HeapArray = __cast(__internals.BinaryenHeapType, __lib.BinaryenHeapTypeArray())
HeapString = __cast(__internals.BinaryenHeapType, __lib.BinaryenHeapTypeString())
HeapStringviewWTF8 = __cast(
    __internals.BinaryenHeapType, __lib.BinaryenHeapTypeStringviewWTF8()
)
HeapStringviewWTF16 = __cast(
    __internals.BinaryenHeapType, __lib.BinaryenHeapTypeStringviewWTF16()
)
HeapStringviewIter = __cast(
    __internals.BinaryenHeapType, __lib.BinaryenHeapTypeStringviewIter()
)
HeapNone = __cast(__internals.BinaryenHeapType, __lib.BinaryenHeapTypeNone())
HeapNoext = __cast(__internals.BinaryenHeapType, __lib.BinaryenHeapTypeNoext())
HeapNofunc = __cast(__internals.BinaryenHeapType, __lib.BinaryenHeapTypeNofunc())


def get_heap_type(
    binaryen_type: __internals.BinaryenType,
) -> __internals.BinaryenHeapType:
    return __lib.BinaryenTypeGetHeapType(binaryen_type)


def is_nullable(binaryen_type: __internals.BinaryenType) -> bool:
    return __lib.BinaryenTypeIsNullable(binaryen_type)


def from_heap_type(
    heap_type: __internals.BinaryenHeapType, nullable: bool
) -> __internals.BinaryenType:
    return __lib.BinaryenTypeFromHeapType(heap_type, nullable)


ExternalFunction = __cast(
    __internals.BinaryenExternalKind, __lib.BinaryenExternalFunction()
)
ExternalTable = __cast(__internals.BinaryenExternalKind, __lib.BinaryenExternalTable())
ExternalMemory = __cast(
    __internals.BinaryenExternalKind, __lib.BinaryenExternalMemory()
)
ExternalGlobal = __cast(
    __internals.BinaryenExternalKind, __lib.BinaryenExternalGlobal()
)
ExternalTag = __cast(__internals.BinaryenExternalKind, __lib.BinaryenExternalTag())
