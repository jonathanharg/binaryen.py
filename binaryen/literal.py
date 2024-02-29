from .libbinaryen.binaryen_cffi import lib as __lib
from .internals import Literal as __Literal

def int32(x:int) -> __Literal:
    return __lib.BinaryenLiteralInt32(x)

def int64(x: int) -> __Literal:
    return __lib.BinaryenLiteralInt64(x)

def float32(x: float) -> __Literal:
    return __lib.BinaryenLiteralFloat32(x)

def float64(x: float) -> __Literal:
    return __lib.BinaryenLiteralFloat64(x)

def float32_bits(x: int) -> __Literal:
    return __lib.BinaryenLiteralFloat32Bits(x)

def float64_bits(x: int) -> __Literal:
    return __lib.BinaryenLiteralFloat64Bits(x)