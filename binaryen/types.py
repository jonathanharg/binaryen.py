"""Core Binaryen types"""
from .libbinaryen.binaryen_cffi import lib as __lib, ffi as __ffi
from . import internals as __internals
from typing import cast as __cast

# THESE TYPES ARE STATIC AND NEVER CHANGE
# We have to ignore the types here because the methods on lib are unknown
none = __cast(__internals.BinaryenNone, __lib.BinaryenTypeNone())
i32 = __cast(__internals.BinaryenInt32, __lib.BinaryenTypeInt32())
i64 = __cast(__internals.BinaryenInt64, __lib.BinaryenTypeInt64())
f32 = __cast(__internals.BinaryenFloat32, __lib.BinaryenTypeFloat32())
f64 = __cast(__internals.BinaryenFloat64, __lib.BinaryenTypeFloat64())
v128 = __cast(__internals.BinaryenVec128, __lib.BinaryenTypeVec128())
funcref = __cast(__internals.BinaryenFuncref, __lib.BinaryenTypeFuncref())
externref = __cast(__internals.BinaryenExternref, __lib.BinaryenTypeExternref())
anyref = __cast(__internals.BinaryenAnyref, __lib.BinaryenTypeAnyref())
eqref = __cast(__internals.BinaryenEqref, __lib.BinaryenTypeEqref())
i31ref = __cast(__internals.BinaryenI31ref, __lib.BinaryenTypeI31ref())
structref = __cast(__internals.BinaryenStructref, __lib.BinaryenTypeStructref())
arrayref = __cast(__internals.BinaryenArrayref, __lib.BinaryenTypeArrayref())  # NOTE: Do we need this?
stringref = __cast(__internals.BinaryenStringref, __lib.BinaryenTypeStringref())
stringview_wtf8 = __cast(__internals.BinaryenStringviewWTF8, __lib.BinaryenTypeStringviewWTF8())
stringview_wtf16 = __cast(__internals.BinaryenStringviewWTF16, __lib.BinaryenTypeStringviewWTF16())
stringview_iter = __cast(__internals.BinaryenStringviewIter, __lib.BinaryenTypeStringviewIter())
nullref = __cast(__internals.BinaryenNullref, __lib.BinaryenTypeNullref())
nullexternref = __cast(__internals.BinaryenNullExternref, __lib.BinaryenTypeNullExternref())
nullfuncref = __cast(__internals.BinaryenNullFuncref, __lib.BinaryenTypeNullFuncref())
unreachable = __cast(__internals.BinaryenUnreachable, __lib.BinaryenTypeUnreachable())
auto = __cast(__internals.BinaryenAuto, __lib.BinaryenTypeAuto())

NULL = __ffi.NULL

def create(types: list[__internals.BinaryenType]) -> __internals.BinaryenType:
    return __lib.BinaryenTypeCreate(types, len(types))


# Number of arguments
def arity(binaryen_type: __internals.BinaryenType) -> int:
    return __lib.BinaryenTypeArity(binaryen_type)


# TODO: BinaryenTypeExpand

# TODO: BinaryenPackedType

# TODO: BinaryenHeapType

# TODO: BinaryenStructType

# TODO: BinaryenArrayType

# TODO: BinaryenHeapType


def is_nullable(binaryen_type: __internals.BinaryenType) -> bool:
    return __lib.BinaryenTypeIsNullable(binaryen_type)


# TODO: BinaryenTypeFromHeapType

# TODO: BinaryExpressionId

# TODO: BinaryExternalKind

# TODO: BinaryFeatures
