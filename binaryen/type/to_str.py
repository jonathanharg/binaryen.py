from .._binaryen import lib
from ..internals import BinaryenType


def to_str(type: BinaryenType) -> str:
    return {
        lib.BinaryenTypeNone(): "None",
        lib.BinaryenTypeInt32(): "Int32",
        lib.BinaryenTypeInt64(): "Int64",
        lib.BinaryenTypeFloat32(): "Float32",
        lib.BinaryenTypeFloat64(): "Float64",
        lib.BinaryenTypeVec128(): "Vec128",
        lib.BinaryenTypeFuncref(): "Funcref",
        lib.BinaryenTypeExternref(): "Externref",
        lib.BinaryenTypeAnyref(): "Anyref",
        lib.BinaryenTypeEqref(): "Eqref",
        lib.BinaryenTypeI31ref(): "I31ref",
        lib.BinaryenTypeStructref(): "Structref",
        lib.BinaryenTypeArrayref(): "Arrayref",
        lib.BinaryenTypeStringref(): "Stringref",
        lib.BinaryenTypeStringviewWTF8(): "StringviewWTF8",
        lib.BinaryenTypeStringviewWTF16(): "StringviewWTF16",
        lib.BinaryenTypeStringviewIter(): "StringviewIter",
        lib.BinaryenTypeNullref(): "Nullref",
        lib.BinaryenTypeNullExternref(): "NullExternref",
        lib.BinaryenTypeNullFuncref(): "NullFuncref",
        lib.BinaryenTypeUnreachable(): "Unreachable",
        lib.BinaryenTypeAuto(): "Auto",
    }[type]
