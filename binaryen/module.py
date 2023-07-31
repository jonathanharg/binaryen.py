from typing import TypeVar, TypeAlias, Any

from .lib import lib
from .types import BinaryenType
from .expression import Expression, Block
from ._binaryen_cffi import ffi, _cffi_backend

T = TypeVar("T")

BinaryenLiteral: TypeAlias = Any
BinaryenOp: TypeAlias = Any
BinaryenExportRef: TypeAlias = Any

def _none_to_null(possibly_none: T | None) -> _cffi_backend.FFI.CData | T:
    if possibly_none is None:
        return ffi.NULL
    return possibly_none


def _change_file_extension(filename: str, extension: str) -> str:
    # TODO: Change this to actual file handling
    if filename.lower().endswith("." + extension):
        return filename
    split_filename = filename.split(".")
    if len(split_filename) > 1:
        split_filename[-1] = extension
    return ".".join(split_filename)

class Module:
    ptr = None

    def __init__(self):
        self.ptr = lib.BinaryenModuleCreate()
        return

    def __del__(self):
        # Free the module when it is garbage collected
        lib.BinaryenModuleDispose(self.ptr)

    # TODO: binaryenLiteral

    # TODO: binaryenOp

    def block(
        self,
        name: bytes | None,
        children: list[Expression],
        binaryen_type: BinaryenType,
    ) -> Block:
        # Convert children object list to list of children pointers
        children_refs = list(map(lambda x: x.ref, children))
        ref = lib.BinaryenBlock(
            self.ptr,
            _none_to_null(name),
            children_refs,
            len(children_refs),
            binaryen_type,
        )
        return Block(ref)

    def If(
        self,
        condition: Expression,
        if_true: Expression,
        if_false: Expression,
    ) -> Expression:
        ref = lib.BinaryenIf(self.ptr, condition.ref, if_true.ref, if_false.ref)
        return Expression(ref)

    # TODO: Loop, Break, Switch, Call, CallIndirect, ReturnCall, ReturnCallIndirect,

    def local_get(self, index: int, local_type: BinaryenType) -> Expression:
        ref = lib.BinaryenLocalGet(self.ptr, index, local_type)
        return Expression(ref)

    def local_set(self, index: int, value: Expression) -> Expression:
        ref = lib.BinaryenLocalSet(self.ptr, index, value.ref)
        return Expression(ref)

    def local_tee(
        self, index: int, value: Expression, value_type: BinaryenType
    ) -> Expression:
        ref = lib.BinaryenLocalTee(self.ptr, index, value.ref, value_type)
        return Expression(ref)

    def global_get(self, name: bytes, global_type: BinaryenType) -> Expression:
        ref = lib.BinaryenGlobalGet(self.ptr, name, global_type)
        return Expression(ref)

    def global_set(self, name: bytes, value: Expression) -> Expression:
        ref = lib.BinaryenGlobalSet(self.ptr, name, value.ref)
        return Expression(ref)

    # TODO: Load, Store

    def const(self, value: BinaryenLiteral) -> Expression:
        ref = lib.BinaryenConst(self.ptr, value)
        return Expression(ref)

    def unary(self, op: BinaryenOp, left: Expression, right: Expression) -> Expression:
        ref = lib.BinaryenUnary(self.ptr, op, left.ref, right.ref)
        return Expression(ref)

    def binary(self, op: BinaryenOp, left: Expression, right: Expression) -> Expression:
        ref = lib.BinaryenBinary(self.ptr, op, left.ref, right.ref)
        return Expression(ref)

    def select(
        self,
        condition: Expression,
        if_true: Expression,
        if_false: Expression,
        select_type: BinaryenType,
    ) -> Expression:
        ref = lib.BinaryenSelect(
            self.ptr, condition.ref, if_true.ref, if_false.ref, select_type
        )
        return Expression(ref)

    def drop(self, value: Expression) -> Expression:
        ref = lib.BinaryenDrop(self.ptr, value.ref)
        return Expression(ref)

    # TODO: Come up with a better name for this
    def Return(self, value: Expression | None) -> Expression:
        expression_ref = getattr(value, "ref", None)
        result_ref = lib.BinaryenReturn(self.ptr, _none_to_null(expression_ref))
        return Expression(result_ref)

    # TODO: MemorySize, MemoryGrow

    def nop(self) -> Expression:
        ref = lib.BinaryenNop(self.ptr)
        return Expression(ref)

    def unreachable(self) -> Expression:
        ref = lib.BinaryenUnreachable(self.ptr)
        return Expression(ref)

    # TODO: AtomicLoad, AtomicStore, AtomicRMW, AtomicCmpxchg, AtomicWait, AtomicNotify, AtomicFence
    # TODO: SIMDExtract, SIMDReplace, SIMDShuffle, SIMDTernary, SIMDShift, SIMDLoad, SIMDLoadStoreLane
    # TODO: MemoryInit, MemoryCopy, MemoryFill,
    # TODO: RefAs, RefFuc, RefEq
    # TODO: TableGet, TableSet, TableGrow
    # TODO: Try, Throw, Rethrow,
    # TODO: TupleMake, TupleExtract, Pop, I31New, I31Get
    # TODO: CallRef, ReftTest, RefCast, BrOn
    # TODO: StructNew, StructGet, StructSet
    # TODO: ArrayNew, ArrayNewFixed, ArrayGet, ArraySet, ArrayLen, ArrayCopy
    # TODO: StringNew, StringConst, StringMeasure, StringEncode, StringConcat, StringEq, StringAs, StringWTF8Advance, StringTWF16Get, StringIterNext, StringIterMove, StringSliceWTF, StringSliceIter

    # NOTE: Done - expression getId to BlockRemoveChildAt

    # EXTRA:

    def add_function(
        self,
        name: bytes,
        params: BinaryenType,
        results: BinaryenType,
        var_types: list[BinaryenType],
        body: Expression,
    ) -> None:
        return lib.BinaryenAddFunction(
            self.ptr, name, params, results, var_types, len(var_types), body.ref
        )

    def call(
        self,
        target: bytes,
        operands: list[Expression],
        return_type: BinaryenType,
    ) -> Expression:
        operand_refs = list(map(lambda x: x.ref, operands))
        ref = lib.BinaryenCall(
            self.ptr, target, operand_refs, len(operand_refs), return_type
        )
        return Expression(ref)

    def add_function_export(
        self, internal_name: bytes, external_name: bytes
    ) -> BinaryenExportRef:
        return lib.BinaryenAddFunctionExport(self.ptr, internal_name, external_name)

    def optimize(self) -> None:
        return lib.BinaryenModuleOptimize(self.ptr)

    def print(self) -> None:
        lib.BinaryenModulePrint(self.ptr)

    def validate(self) -> bool:
        return lib.BinaryenModuleValidate(self.ptr)

    def emit_text(self) -> str:
        text_ptr = lib.BinaryenModuleAllocateAndWriteText(self.ptr)
        text_bytes = ffi.string(text_ptr)
        text = text_bytes.decode("ascii")

        # text_ptr is automatically freed by python garbage collector
        return text

    def emit_stack_ir(self, optimize: bool) -> str:
        text_ptr = lib.BinaryenModuleAllocateAndWriteStackIR(self.ptr, optimize)
        text_bytes = ffi.string(text_ptr)
        text = text_bytes.decode("ascii")

        # text_ptr is automatically freed by python garbage collector
        return text

    def emit_text(self) -> str:
        text_ptr = lib.BinaryenModuleAllocateAndWriteText(self.ptr)
        text_bytes = ffi.string(text_ptr)
        text = text_bytes.decode("ascii")

        # text_ptr is automatically freed by python garbage collector
        return text

    def emit_binary(self) -> bytes:
        struct = lib.BinaryenModuleAllocateAndWrite(self.ptr, ffi.NULL)

        binary_ptr = ffi.cast("char *", struct.binary)  # char * pointer to the binary
        binary_len = struct.binaryBytes

        binary = ffi.unpack(binary_ptr, binary_len)  # reads binary buffer into python

        # print([x for x in binary]) # Debug: print int values of memory buffer
        return binary

    def write_text(self, filename: str):
        filename_wat = _change_file_extension(filename, "wat")

        with open(filename_wat, "x", encoding="utf-8") as file:
            text = self.emit_text()
            file.write(text)

    def write_binary(self, filename: str):
        filename_wasm = _change_file_extension(filename, "wasm")

        with open(filename_wasm, "xb") as file:
            binary = self.emit_binary()
            file.write(binary)
