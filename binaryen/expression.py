from __future__ import annotations

from .lib import lib
from .types import BinaryenType


class Expression:
    def __init__(self, ref):
        self.ref = ref

    def get_id(self) -> int:
        return lib.BinaryenExpressionGetId(self.ref)

    def get_type(self) -> BinaryenType:
        return lib.BinaryenExpressionGetType(self.ref)

    def set_type(self, expr_type: BinaryenType) -> None:
        return lib.BinaryenExpressionSetType(self.ref, expr_type)

    def print(self) -> None:
        return lib.BinaryenExpressionPrint(self.ref)

    def finalize(self) -> None:
        return lib.BinaryenExpressionFinalize(self.ref)

    def copy(self, module: "Module") -> Expression:
        ref = lib.BinaryenExpressionCopy(self.ref, module.ref)
        return Expression(ref)


class Block(Expression):
    def get_name(self) -> bytes | None:
        return lib.BinaryenBlockGetName(self.ref)

    def set_name(self, name: bytes) -> None:
        return lib.BinaryenBlockSetName(self.ref, name)

    def get_num_children(self) -> int:
        return lib.BinaryenBlockGetNumChildren(self.ref)

    def get_child_at(self, index: int) -> Expression:
        ref = lib.BinaryenBlockGetChildAt(self.ref, index)
        return Expression(ref)

    def set_child_at(self, index: int, child: Expression) -> None:
        return lib.BinaryenBlockSetChildAt(self.ref, index, child.ref)

    def append_child(self, child: Expression) -> int:
        return lib.BinaryenBlockAppendChild(self.ref, child.ref)

    def insert_child_at(self, index: int, child: Expression) -> None:
        return lib.BinaryenBlockInsertChildAt(self.ref, index, child.ref)

    def remove_child_at(self, index: int) -> Expression:
        ref = lib.BinaryenBlockRemoveChildAt(self.ref, index)
        return Expression(ref)
