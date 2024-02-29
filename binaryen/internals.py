from typing import NewType as __NewType
from typing import TypeAlias as __TypeAlias
from typing import Union as __Union
from typing import final as __final

from .binaryen_lib import ffi as __ffi
from .binaryen_lib import lib as __lib

# Empty type, under the hood all Binaryen types are integers
# we don't want users to believe that they can modify types with
# traditional integer operations, because they can't.
@__final
class __BaseType:
    pass

BinaryenType = __NewType("BinaryenType", __BaseType)
BinaryenPackedType = __NewType("BinaryenPackedType", __BaseType)
BinaryenHeapType = __NewType("BinaryenHeapType", __BaseType)
BinaryenOp = __NewType("BinaryenOp", __BaseType)
BinaryenLiteral = __NewType("BinaryenLiteral", __BaseType)
