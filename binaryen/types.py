from typing import NewType, TypeAlias, Union, cast, final
from .lib import lib
from ._binaryen_cffi import ffi

NULL = ffi.NULL

CData: TypeAlias = ffi.CData

# Empty type, under the hood all Binaryen types are integers
# we don't want users to believe that they can modify types with 
# traditional integer operations, because they can't.
@final
class BType:
    pass

BinaryenNone = NewType("BinaryenNone", BType)
BinaryenInt32 = NewType("BinaryenInt32", BType)
BinaryenInt64 = NewType("BinaryenInt64", BType)
BinaryenFloat32 = NewType("BinaryenFloat32", BType)
BinaryenFloat64 = NewType("BinaryenFloat64", BType)
BinaryenVec128 = NewType("BinaryenVec128", BType)
BinaryenFuncref = NewType("BinaryenFuncref", BType)
BinaryenExternref = NewType("BinaryenExternref", BType)
BinaryenAnyref = NewType("BinaryenAnyref", BType)
BinaryenEqref = NewType("BinaryenEqref", BType)
BinaryenI31ref = NewType("BinaryenI31ref", BType)
BinaryenStructref = NewType("BinaryenStructref", BType)
BinaryenArrayref = NewType("BinaryenArrayref", BType)
BinaryenStringref = NewType("BinaryenStringref", BType)
BinaryenStringviewWTF8 = NewType("BinaryenStringviewWTF8", BType)
BinaryenStringviewWTF16 = NewType("BinaryenStringviewWTF16", BType)
BinaryenStringviewIter = NewType("BinaryenStringviewIter", BType)
BinaryenNullref = NewType("BinaryenNullref", BType)
BinaryenNullExternref = NewType("BinaryenNullExternref", BType)
BinaryenNullFuncref = NewType("BinaryenNullFuncref", BType)
BinaryenUnreachable = NewType("BinaryenUnreachable", BType)
BinaryenAuto = NewType("BinaryenAuto", BType)

# THESE TYPES ARE STATIC AND NEVER CHANGE
# We have to ignore the types here because the methods on lib are unknown
none = cast(BinaryenNone, lib.BinaryenTypeNone())
i32 = cast(BinaryenInt32, lib.BinaryenTypeInt32())
i64 = cast(BinaryenInt64, lib.BinaryenTypeInt64())
f32 = cast(BinaryenFloat32, lib.BinaryenTypeFloat32())
f64 = cast(BinaryenFloat64, lib.BinaryenTypeFloat64())
v128 = cast(BinaryenVec128, lib.BinaryenTypeVec128())
funcref = cast(BinaryenFuncref, lib.BinaryenTypeFuncref())
externref = cast(BinaryenExternref, lib.BinaryenTypeExternref())
anyref = cast(BinaryenAnyref, lib.BinaryenTypeAnyref())
eqref = cast(BinaryenEqref, lib.BinaryenTypeEqref())
i31ref = cast(BinaryenI31ref, lib.BinaryenTypeI31ref())
structref = cast(BinaryenStructref, lib.BinaryenTypeStructref())
arrayref = cast(BinaryenArrayref, lib.BinaryenTypeArrayref())  # NOTE: Do we need this?
stringref = cast(BinaryenStringref, lib.BinaryenTypeStringref())
stringview_wtf8 = cast(BinaryenStringviewWTF8, lib.BinaryenTypeStringviewWTF8())
stringview_wtf16 = cast(BinaryenStringviewWTF16, lib.BinaryenTypeStringviewWTF16())
stringview_iter = cast(BinaryenStringviewIter, lib.BinaryenTypeStringviewIter())
nullref = cast(BinaryenNullref, lib.BinaryenTypeNullref())
nullexternref = cast(BinaryenNullExternref, lib.BinaryenTypeNullExternref())
nullfuncref = cast(BinaryenNullFuncref, lib.BinaryenTypeNullFuncref())
unreachable = cast(BinaryenUnreachable, lib.BinaryenTypeUnreachable())
auto = cast(BinaryenAuto, lib.BinaryenTypeAuto())

BinaryenType: TypeAlias = Union[
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
    BinaryenAuto,
]