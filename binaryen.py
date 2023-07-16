import platform


from _binaryen_cffi import ffi

if platform.system() == "Linux":
    __lib_string = "libbinaryen.so"
if platform.system() == "Windows":
    __lib_string = "libbinaryen.dll"
if platform.system() == "Darwin":
    __lib_string = "libbinaryen.dylib"
lib = ffi.dlopen(__lib_string)


NULL = ffi.NULL

WasmNone = lib.BinaryenTypeNone()
Int32 = lib.BinaryenTypeInt32()
Int64 = lib.BinaryenTypeInt64()
Float32 = lib.BinaryenTypeFloat32()
Float64 = lib.BinaryenTypeFloat64()
Vec128 = lib.BinaryenTypeVec128()
Funcref = lib.BinaryenTypeFuncref()
Externref = lib.BinaryenTypeExternref()
Anyref = lib.BinaryenTypeAnyref()
Eqref = lib.BinaryenTypeEqref()
I31ref = lib.BinaryenTypeI31ref()
Structref = lib.BinaryenTypeStructref()
Arrayref = lib.BinaryenTypeArrayref()
Stringref = lib.BinaryenTypeStringref()
StringviewWTF8 = lib.BinaryenTypeStringviewWTF8()
StringviewWTF16 = lib.BinaryenTypeStringviewWTF16()
StringviewIter = lib.BinaryenTypeStringviewIter()
Nullref = lib.BinaryenTypeNullref()
NullExternref = lib.BinaryenTypeNullExternref()
NullFuncref = lib.BinaryenTypeNullFuncref()
Unreachable = lib.BinaryenTypeUnreachable()
Auto = lib.BinaryenTypeAuto()

class Module:
    ptr = None

    def __init__(self):
        self.ptr = lib.BinaryenModuleCreate()
        return
    
    def addFunction(self, name: bytes, params, results, varTypes, numVarTypes, body):
        return lib.BinaryenAddFunction(self.ptr, name, params, results, varTypes, numVarTypes, body)

    def localGet(self, index, type):
        return lib.BinaryenLocalGet(self.ptr, index, type)

    def localSet(self, index, value):
        return lib.BinaryenLocalSet(self.ptr, index, value)

    def print(self):
        lib.BinaryenModulePrint(self.ptr)

    def dispose(self):
        lib.BinaryenModuleDispose(self.ptr)