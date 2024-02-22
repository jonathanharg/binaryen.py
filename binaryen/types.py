"""Core Binaryen types"""
from .lib import lib as _lib, ffi as _ffi
from . import internals as _internals
from typing import cast as _cast

# THESE TYPES ARE STATIC AND NEVER CHANGE
# We have to ignore the types here because the methods on lib are unknown
none = _cast(_internals.BinaryenNone, _lib.BinaryenTypeNone())
i32 = _cast(_internals.BinaryenInt32, _lib.BinaryenTypeInt32())
i64 = _cast(_internals.BinaryenInt64, _lib.BinaryenTypeInt64())
f32 = _cast(_internals.BinaryenFloat32, _lib.BinaryenTypeFloat32())
f64 = _cast(_internals.BinaryenFloat64, _lib.BinaryenTypeFloat64())
v128 = _cast(_internals.BinaryenVec128, _lib.BinaryenTypeVec128())
funcref = _cast(_internals.BinaryenFuncref, _lib.BinaryenTypeFuncref())
externref = _cast(_internals.BinaryenExternref, _lib.BinaryenTypeExternref())
anyref = _cast(_internals.BinaryenAnyref, _lib.BinaryenTypeAnyref())
eqref = _cast(_internals.BinaryenEqref, _lib.BinaryenTypeEqref())
i31ref = _cast(_internals.BinaryenI31ref, _lib.BinaryenTypeI31ref())
structref = _cast(_internals.BinaryenStructref, _lib.BinaryenTypeStructref())
arrayref = _cast(_internals.BinaryenArrayref, _lib.BinaryenTypeArrayref())  # NOTE: Do we need this?
stringref = _cast(_internals.BinaryenStringref, _lib.BinaryenTypeStringref())
stringview_wtf8 = _cast(_internals.BinaryenStringviewWTF8, _lib.BinaryenTypeStringviewWTF8())
stringview_wtf16 = _cast(_internals.BinaryenStringviewWTF16, _lib.BinaryenTypeStringviewWTF16())
stringview_iter = _cast(_internals.BinaryenStringviewIter, _lib.BinaryenTypeStringviewIter())
nullref = _cast(_internals.BinaryenNullref, _lib.BinaryenTypeNullref())
nullexternref = _cast(_internals.BinaryenNullExternref, _lib.BinaryenTypeNullExternref())
nullfuncref = _cast(_internals.BinaryenNullFuncref, _lib.BinaryenTypeNullFuncref())
unreachable = _cast(_internals.BinaryenUnreachable, _lib.BinaryenTypeUnreachable())
auto = _cast(_internals.BinaryenAuto, _lib.BinaryenTypeAuto())

NULL = _ffi.NULL


def create(types: list[_internals.BinaryenType]) -> _internals.BinaryenType:
    return _lib.BinaryenTypeCreate(types, len(types))


# Number of arguments
def arity(binaryen_type: _internals.BinaryenType) -> int:
    return _lib.BinaryenTypeArity(binaryen_type)


# TODO: _internals.BinaryenTypeExpand

# TODO: BinaryenPackedType

# TODO: BinaryenHeapType

# TODO: BinaryenStructType

# TODO: BinaryenArrayType

# TODO: BinaryenHeapType


def is_nullable(binaryen_type: _internals.BinaryenType) -> bool:
    return _lib.BinaryenTypeIsNullable(binaryen_type)


# TODO: BinaryenTypeFromHeapType

# TODO: BinaryExpressionId

# TODO: BinaryExternalKind

# TODO: BinaryFeatures
