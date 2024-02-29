from typing import NewType as __NewType
from typing import TypeAlias as __TypeAlias
from typing import Union as __Union
from typing import final as __final

from .libbinaryen.binaryen_cffi import ffi as __ffi
from .libbinaryen.binaryen_cffi import lib as __lib

CData: __TypeAlias = __ffi.CData


# Empty type, under the hood all BinaXryen types are integers
# we don't want users to believe that they can modify types with
# traditional integer operations, because they can't.
@__final
class __BaseType:
    pass


none = __NewType("none", __BaseType)
Int32 = __NewType("Int32", __BaseType)
Int64 = __NewType("Int64", __BaseType)
Float32 = __NewType("Float32", __BaseType)
Float64 = __NewType("Float64", __BaseType)
Vec128 = __NewType("Vec128", __BaseType)
Funcref = __NewType("Funcref", __BaseType)
Externref = __NewType("Externref", __BaseType)
Anyref = __NewType("Anyref", __BaseType)
Eqref = __NewType("Eqref", __BaseType)
I31ref = __NewType("I31ref", __BaseType)
Structref = __NewType("Structref", __BaseType)
Arrayref = __NewType("Arrayref", __BaseType)
Stringref = __NewType("Stringref", __BaseType)
StringviewWTF8 = __NewType("StringviewWTF8", __BaseType)
StringviewWTF16 = __NewType("StringviewWTF16", __BaseType)
StringviewIter = __NewType("StringviewIter", __BaseType)
Nullref = __NewType("Nullref", __BaseType)
NullExternref = __NewType("NullExternref", __BaseType)
NullFuncref = __NewType("NullFuncref", __BaseType)
Unreachable = __NewType("Unreachable", __BaseType)
Auto = __NewType("Auto", __BaseType)

numtype = __Union[Int32, Int64, Float32, Float64]
vectype = __Union[Vec128]
reftype = __Union[Funcref, Externref]


Type: __TypeAlias = __Union[
    none,
    Int32,
    Int64,
    Float32,
    Float64,
    Vec128,
    Funcref,
    Externref,
    Anyref,
    Eqref,
    I31ref,
    Structref,
    Arrayref,
    Stringref,
    StringviewWTF8,
    StringviewWTF16,
    StringviewIter,
    Nullref,
    NullExternref,
    NullFuncref,
    Unreachable,
]

Op = __NewType("Op", __BaseType)
Literal = __NewType("Literal", __BaseType)
