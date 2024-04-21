from ._binaryen import lib
from .internals import BinaryenType


class FunctionRef:
    def __init__(self, ref):
        self.ref = ref

    def get_name(self) -> str:
        return lib.BinaryenFunctionGetName(self.ref)

    def get_num_vars(self) -> int:
        return lib.BinaryenFunctionGetNumVars(self.ref)

    def get_var(self, index: int) -> BinaryenType:
        return lib.BinaryenFunctionGetVar(self.ref, index)

    def add_var(self, type: BinaryenType) -> int:
        return lib.BinaryenFunctionAddVar(self.ref, type)

    def get_num_locals(self) -> int:
        return lib.BinaryenFunctionGetNumLocals(self.ref)

    def has_local_name(self, index: int) -> bool:
        return bool(lib.BinaryenFunctionHasLocalName(self.ref, index))

    def get_local_name(self, index: int) -> str:
        return lib.BinaryenFunctionGetLocalName(self.ref, index)

    def set_local_name(self, index: int, name: bytes):
        return lib.BinaryenFunctionSetLocalName(self.ref, index, name)
