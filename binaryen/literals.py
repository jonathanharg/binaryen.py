from .lib import lib, ffi
from . import types
from typing import cast

# THESE TYPES ARE STATIC AND NEVER CHANGE
# We have to ignore the types here because the methods on lib are unknown
none = cast(types.BinaryenNone, lib.BinaryenTypeNone())
i32 = cast(types.BinaryenInt32, lib.BinaryenTypeInt32())
i64 = cast(types.BinaryenInt64, lib.BinaryenTypeInt64())
f32 = cast(types.BinaryenFloat32, lib.BinaryenTypeFloat32())
f64 = cast(types.BinaryenFloat64, lib.BinaryenTypeFloat64())
v128 = cast(types.BinaryenVec128, lib.BinaryenTypeVec128())
funcref = cast(types.BinaryenFuncref, lib.BinaryenTypeFuncref())
externref = cast(types.BinaryenExternref, lib.BinaryenTypeExternref())
anyref = cast(types.BinaryenAnyref, lib.BinaryenTypeAnyref())
eqref = cast(types.BinaryenEqref, lib.BinaryenTypeEqref())
i31ref = cast(types.BinaryenI31ref, lib.BinaryenTypeI31ref())
structref = cast(types.BinaryenStructref, lib.BinaryenTypeStructref())
arrayref = cast(types.BinaryenArrayref, lib.BinaryenTypeArrayref())  # NOTE: Do we need this?
stringref = cast(types.BinaryenStringref, lib.BinaryenTypeStringref())
stringview_wtf8 = cast(types.BinaryenStringviewWTF8, lib.BinaryenTypeStringviewWTF8())
stringview_wtf16 = cast(types.BinaryenStringviewWTF16, lib.BinaryenTypeStringviewWTF16())
stringview_iter = cast(types.BinaryenStringviewIter, lib.BinaryenTypeStringviewIter())
nullref = cast(types.BinaryenNullref, lib.BinaryenTypeNullref())
nullexternref = cast(types.BinaryenNullExternref, lib.BinaryenTypeNullExternref())
nullfuncref = cast(types.BinaryenNullFuncref, lib.BinaryenTypeNullFuncref())
unreachable = cast(types.BinaryenUnreachable, lib.BinaryenTypeUnreachable())
auto = cast(types.BinaryenAuto, lib.BinaryenTypeAuto())

NULL = ffi.NULL