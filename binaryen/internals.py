from .libbinaryen.binaryen_cffi import lib as __lib, ffi as __ffi
from typing import NewType as __NewType, TypeAlias as __TypeAlias, Union as __Union, final as __final

CData: __TypeAlias = __ffi.CData

# Empty type, under the hood all Binaryen types are integers
# we don't want users to believe that they can modify types with
# traditional integer operations, because they can't.
@__final
class __BaseType:
    pass


BinaryenNone = __NewType("BinaryenNone", __BaseType)
BinaryenInt32 = __NewType("BinaryenInt32", __BaseType)
BinaryenInt64 = __NewType("BinaryenInt64", __BaseType)
BinaryenFloat32 = __NewType("BinaryenFloat32", __BaseType)
BinaryenFloat64 = __NewType("BinaryenFloat64", __BaseType)
BinaryenVec128 = __NewType("BinaryenVec128", __BaseType)
BinaryenFuncref = __NewType("BinaryenFuncref", __BaseType)
BinaryenExternref = __NewType("BinaryenExternref", __BaseType)
BinaryenAnyref = __NewType("BinaryenAnyref", __BaseType)
BinaryenEqref = __NewType("BinaryenEqref", __BaseType)
BinaryenI31ref = __NewType("BinaryenI31ref", __BaseType)
BinaryenStructref = __NewType("BinaryenStructref", __BaseType)
BinaryenArrayref = __NewType("BinaryenArrayref", __BaseType)
BinaryenStringref = __NewType("BinaryenStringref", __BaseType)
BinaryenStringviewWTF8 = __NewType("BinaryenStringviewWTF8", __BaseType)
BinaryenStringviewWTF16 = __NewType("BinaryenStringviewWTF16", __BaseType)
BinaryenStringviewIter = __NewType("BinaryenStringviewIter", __BaseType)
BinaryenNullref = __NewType("BinaryenNullref", __BaseType)
BinaryenNullExternref = __NewType("BinaryenNullExternref", __BaseType)
BinaryenNullFuncref = __NewType("BinaryenNullFuncref", __BaseType)
BinaryenUnreachable = __NewType("BinaryenUnreachable", __BaseType)
BinaryenAuto = __NewType("BinaryenAuto", __BaseType)

numtype = __Union[BinaryenInt32, BinaryenInt64, BinaryenFloat32, BinaryenFloat64]
vectype = __Union[BinaryenVec128]
reftype = __Union[BinaryenFuncref, BinaryenExternref]


BinaryenType: __TypeAlias = __Union[
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

BinaryenOp = __NewType("BinaryenOp", __BaseType)
BinaryenLiteral = __NewType("BinaryenLiteral", __BaseType)