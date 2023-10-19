"""Core Binaryen types"""

from typing import NewType as _NewType, TypeAlias as _TypeAlias, Union as _Union, final as _final
from .lib import lib as _lib, ffi as _ffi

CData: _TypeAlias = _ffi.CData

# Empty type, under the hood all Binaryen types are integers
# we don't want users to believe that they can modify types with
# traditional integer operations, because they can't.
@_final
class __BaseType:
    pass


BinaryenNone = _NewType("BinaryenNone", __BaseType)
BinaryenInt32 = _NewType("BinaryenInt32", __BaseType)
BinaryenInt64 = _NewType("BinaryenInt64", __BaseType)
BinaryenFloat32 = _NewType("BinaryenFloat32", __BaseType)
BinaryenFloat64 = _NewType("BinaryenFloat64", __BaseType)
BinaryenVec128 = _NewType("BinaryenVec128", __BaseType)
BinaryenFuncref = _NewType("BinaryenFuncref", __BaseType)
BinaryenExternref = _NewType("BinaryenExternref", __BaseType)
BinaryenAnyref = _NewType("BinaryenAnyref", __BaseType)
BinaryenEqref = _NewType("BinaryenEqref", __BaseType)
BinaryenI31ref = _NewType("BinaryenI31ref", __BaseType)
BinaryenStructref = _NewType("BinaryenStructref", __BaseType)
BinaryenArrayref = _NewType("BinaryenArrayref", __BaseType)
BinaryenStringref = _NewType("BinaryenStringref", __BaseType)
BinaryenStringviewWTF8 = _NewType("BinaryenStringviewWTF8", __BaseType)
BinaryenStringviewWTF16 = _NewType("BinaryenStringviewWTF16", __BaseType)
BinaryenStringviewIter = _NewType("BinaryenStringviewIter", __BaseType)
BinaryenNullref = _NewType("BinaryenNullref", __BaseType)
BinaryenNullExternref = _NewType("BinaryenNullExternref", __BaseType)
BinaryenNullFuncref = _NewType("BinaryenNullFuncref", __BaseType)
BinaryenUnreachable = _NewType("BinaryenUnreachable", __BaseType)
BinaryenAuto = _NewType("BinaryenAuto", __BaseType)

BinaryenType: _TypeAlias = _Union[
    BinaryenNone,
    BinaryenInt32,
    BinaryenInt64,
    BinaryenFloat32,
    BinaryenFloat64,
    BinaryenVec128,
    BinaryenFuncref,
    BinaryenExternref,
    BinaryenAnyref,
    BinaryenEqref,
    BinaryenI31ref,
    BinaryenStructref,
    BinaryenArrayref,
    BinaryenStringref,
    BinaryenStringviewWTF8,
    BinaryenStringviewWTF16,
    BinaryenStringviewIter,
    BinaryenNullref,
    BinaryenNullExternref,
    BinaryenNullFuncref,
    BinaryenUnreachable,
]


def create(types: list[BinaryenType]) -> BinaryenType:
    """Create a Binaryen type

    Args:
        types (list[BinaryenType]): List of input types

    Returns:
        BinaryenType: Combined type

    Note:
        Under the hood, BinaryenTypes are stored as integer ids

    Examples:
        >>> twoStrings = binaryen.types.create([binaryen.stringref, binaryen.stringref])
        >>> isinstance(twoStrings, int)
        True
    """
    return _lib.BinaryenTypeCreate(types, len(types))


# Number of arguments
def arity(binaryen_type: BinaryenType) -> int:
    """The number of arguments or operands a type takes

    Args:
        binaryen_type (BinaryenType): The type to check

    Returns:
        int: The number of operands for this type

    Examples:
        >>> binaryen.types.arity(binaryen.i32)
        1
        >>> binaryen.types.arity(binaryen.types.create([binaryen.i32,binaryen.i32]))
        2
    """
    return _lib.BinaryenTypeArity(binaryen_type)


# TODO: BinaryenTypeExpand

# TODO: BinaryenPackedType

# TODO: BinaryenHeapType

# TODO: BinaryenStructType

# TODO: BinaryenArrayType

# TODO: BinaryenHeapType


def is_nullable(binaryen_type: BinaryenType) -> bool:
    """Get if a Binaryen type is nullable (possibly none) or not.

    Args:
        binaryen_type (BinaryenType): The type to be tested

    Returns:
        bool: If the type is nullable

    Examples:
        >>> binaryen.types.is_nullable(binaryen.i32)
        False
        >>> binaryen.types.is_nullable(binaryen.anyref)
        True
    """
    return _lib.BinaryenTypeIsNullable(binaryen_type)


# TODO: BinaryenTypeFromHeapType

# TODO: BinaryExpressionId

# TODO: BinaryExternalKind

# TODO: BinaryFeatures
