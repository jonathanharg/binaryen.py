from .__expression import Expression
from ._binaryen import lib


class Global:
    def __init__(self, ref):
        self.ref = ref

    def get_name(self):
        return str(lib.BinaryenGlobalGetName(self.ref))

    def get_type(self):
        return lib.BinaryenGlobalGetType(self.ref)

    def is_mutable(self):
        return bool(lib.BinaryenGlobalIsMutable(self.ref))

    def get_init_expr(self):
        return Expression(lib.BinaryenGlobalGetInitExpr(self.ref))
