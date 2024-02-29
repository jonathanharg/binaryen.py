"""Core Binaryen types"""
from .libbinaryen.binaryen_cffi import lib as __lib, ffi as __ffi
from . import internals as __internals
from typing import cast as __cast

# THESE TYPES ARE STATIC AND NEVER CHANGE
# We have to ignore the types here because the methods on lib are unknown
none = __cast(__internals.none, __lib.BinaryenTypeNone())
i32 = __cast(__internals.Int32, __lib.BinaryenTypeInt32())
i64 = __cast(__internals.Int64, __lib.BinaryenTypeInt64())
f32 = __cast(__internals.Float32, __lib.BinaryenTypeFloat32())
f64 = __cast(__internals.Float64, __lib.BinaryenTypeFloat64())
v128 = __cast(__internals.Vec128, __lib.BinaryenTypeVec128())
funcref = __cast(__internals.Funcref, __lib.BinaryenTypeFuncref())
externref = __cast(__internals.Externref, __lib.BinaryenTypeExternref())
anyref = __cast(__internals.Anyref, __lib.BinaryenTypeAnyref())
eqref = __cast(__internals.Eqref, __lib.BinaryenTypeEqref())
i31ref = __cast(__internals.I31ref, __lib.BinaryenTypeI31ref())
structref = __cast(__internals.Structref, __lib.BinaryenTypeStructref())
arrayref = __cast(__internals.Arrayref, __lib.BinaryenTypeArrayref())  # NOTE: Do we need this?
stringref = __cast(__internals.Stringref, __lib.BinaryenTypeStringref())
stringview_wtf8 = __cast(__internals.StringviewWTF8, __lib.BinaryenTypeStringviewWTF8())
stringview_wtf16 = __cast(__internals.StringviewWTF16, __lib.BinaryenTypeStringviewWTF16())
stringview_iter = __cast(__internals.StringviewIter, __lib.BinaryenTypeStringviewIter())
nullref = __cast(__internals.Nullref, __lib.BinaryenTypeNullref())
nullexternref = __cast(__internals.NullExternref, __lib.BinaryenTypeNullExternref())
nullfuncref = __cast(__internals.NullFuncref, __lib.BinaryenTypeNullFuncref())
unreachable = __cast(__internals.Unreachable, __lib.BinaryenTypeUnreachable())
auto = __cast(__internals.Auto, __lib.BinaryenTypeAuto())

NULL = __ffi.NULL

def create(types: list[__internals.Type]) -> __internals.Type:
    return __lib.BinaryenTypeCreate(types, len(types))


# Number of arguments
def arity(binaryen_type: __internals.Type) -> int:
    return __lib.BinaryenTypeArity(binaryen_type)


# TODO: BinaryenTypeExpand

# TODO: BinaryenPackedType

# TODO: BinaryenHeapType

# TODO: BinaryenStructType

# TODO: BinaryenArrayType

# TODO: BinaryenHeapType


def is_nullable(binaryen_type: __internals.Type) -> bool:
    return __lib.BinaryenTypeIsNullable(binaryen_type)


# TODO: BinaryenTypeFromHeapType

# TODO: BinaryExpressionId

# TODO: BinaryExternalKind

# TODO: BinaryFeatures
