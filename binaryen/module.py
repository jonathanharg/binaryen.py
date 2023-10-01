"""Binaryen representation of WebAssembly modules"""

from typing import TypeVar, TypeAlias, Any

from .lib import lib
from .types import BinaryenType, BinaryenAuto, NULL, BinaryenNone, none
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


def _none_to_binaryen(possibly_none: T | None) -> BinaryenNone | T:
    if possibly_none is None:
        return none
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
    """A WebAssembly Module

    Modules contain lists of functions, imports, exports, function types. The module owns them and will free
    their memory when the module is no longer in use.

    Expressions are also allocated inside modules, and freed with the module. Expressions are not added directly on the module, instead, they are arguments to other expressions (and then they
    are the children of that AST node), or to a function (and then they are the body of that function).

    A module can also contain a function table for indirect calls, a memory, and a start method.

    Attributes:
        ref (cdata): A pointer to the Binaryen module. Only access this if you know what you're doing. Modifying this or using this, unless done very carefully, will almost certainly lead to errors or a crash.
    """

    def __init__(self):
        self.ref = lib.BinaryenModuleCreate()
        return

    def __del__(self):
        # Free the module when it is garbage collected
        lib.BinaryenModuleDispose(self.ref)

    # TODO: binaryenLiteral

    # TODO: binaryenOp

    def block(
        self,
        name: bytes | None,
        children: list[Expression],
        binaryen_type: BinaryenType | BinaryenAuto,
    ) -> Block:
        # Convert children object list to list of children pointers
        children_refs = list(map(lambda x: x.ref, children))
        ref = lib.BinaryenBlock(
            self.ref,
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
        ref = lib.BinaryenIf(self.ref, condition.ref, if_true.ref, if_false.ref)
        return Expression(ref)

    # TODO: Loop, Break, Switch, Call, CallIndirect, ReturnCall, ReturnCallIndirect,

    def local_get(self, index: int, local_type: BinaryenType) -> Expression:
        ref = lib.BinaryenLocalGet(self.ref, index, local_type)
        return Expression(ref)

    def local_set(self, index: int, value: Expression) -> Expression:
        ref = lib.BinaryenLocalSet(self.ref, index, value.ref)
        return Expression(ref)

    def local_tee(
        self, index: int, value: Expression, value_type: BinaryenType
    ) -> Expression:
        ref = lib.BinaryenLocalTee(self.ref, index, value.ref, value_type)
        return Expression(ref)

    def global_get(self, name: bytes, global_type: BinaryenType) -> Expression:
        ref = lib.BinaryenGlobalGet(self.ref, name, global_type)
        return Expression(ref)

    def global_set(self, name: bytes, value: Expression) -> Expression:
        ref = lib.BinaryenGlobalSet(self.ref, name, value.ref)
        return Expression(ref)

    # TODO: Load, Store

    def const(self, value: BinaryenLiteral) -> Expression:
        ref = lib.BinaryenConst(self.ref, value)
        return Expression(ref)

    def unary(self, op: BinaryenOp, left: Expression, right: Expression) -> Expression:
        ref = lib.BinaryenUnary(self.ref, op, left.ref, right.ref)
        return Expression(ref)

    def binary(self, op: BinaryenOp, left: Expression, right: Expression) -> Expression:
        ref = lib.BinaryenBinary(self.ref, op, left.ref, right.ref)
        return Expression(ref)

    def select(
        self,
        condition: Expression,
        if_true: Expression,
        if_false: Expression,
        select_type: BinaryenType,
    ) -> Expression:
        ref = lib.BinaryenSelect(
            self.ref, condition.ref, if_true.ref, if_false.ref, select_type
        )
        return Expression(ref)

    def drop(self, value: Expression) -> Expression:
        ref = lib.BinaryenDrop(self.ref, value.ref)
        return Expression(ref)

    # TODO: Come up with a better name for this
    def Return(self, value: Expression | None) -> Expression:
        expression_ref = getattr(value, "ref", None)
        result_ref = lib.BinaryenReturn(self.ref, _none_to_null(expression_ref))
        return Expression(result_ref)

    # TODO: MemorySize, MemoryGrow

    def nop(self) -> Expression:
        ref = lib.BinaryenNop(self.ref)
        return Expression(ref)

    def unreachable(self) -> Expression:
        ref = lib.BinaryenUnreachable(self.ref)
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

    # TODO: Carry on from here

    # Imports

    def add_function_import(
        self,
        internalName: bytes,
        externalModuleName: bytes,
        externalBaseName: bytes,
        params: BinaryenType,
        results: BinaryenType,
    ) -> None:
        lib.BinaryenAddFunctionImport(
            self.ref,
            internalName,
            externalModuleName,
            externalBaseName,
            params,
            results,
        )

    # EXTRA:

    def add_function(
        self,
        name: bytes,
        params: BinaryenType | None,
        results: BinaryenType | None,
        var_types: list[BinaryenType] | None,
        body: Expression,
    ) -> None:
        if var_types is None or (len(var_types) == 0):
            length = 0
            c_var_types = _none_to_null(var_types)
        else:
            length = len(var_types)
            c_var_types = var_types

        return lib.BinaryenAddFunction(
            self.ref,
            name,
            _none_to_binaryen(params),
            _none_to_binaryen(results),
            c_var_types,
            length,
            body.ref,
        )

    def call(
        self,
        target: bytes,
        operands: list[Expression],
        return_type: BinaryenType,
    ) -> Expression:
        operand_refs = list(map(lambda x: x.ref, operands))
        ref = lib.BinaryenCall(
            self.ref, target, operand_refs, len(operand_refs), return_type
        )
        return Expression(ref)

    def set_memory():
        raise NotImplementedError

    def add_function_export(
        self, internal_name: bytes, external_name: bytes
    ) -> BinaryenExportRef:
        return lib.BinaryenAddFunctionExport(self.ref, internal_name, external_name)

    def optimize(self) -> None:
        return lib.BinaryenModuleOptimize(self.ref)

    def print(self) -> None:
        lib.BinaryenModulePrint(self.ref)

    def validate(self) -> bool:
        return lib.BinaryenModuleValidate(self.ref)

    def emit_text(self) -> str:
        text_ptr = lib.BinaryenModuleAllocateAndWriteText(self.ref)
        text_bytes = ffi.string(text_ptr)
        text = text_bytes.decode("ascii")

        # text_ptr is automatically freed by python garbage collector
        return text

    def emit_stack_ir(self, optimize: bool) -> str:
        text_ptr = lib.BinaryenModuleAllocateAndWriteStackIR(self.ref, optimize)
        text_bytes = ffi.string(text_ptr)
        text = text_bytes.decode("ascii")

        # text_ptr is automatically freed by python garbage collector
        return text

    def emit_text(self) -> str:
        text_ptr = lib.BinaryenModuleAllocateAndWriteText(self.ref)
        text_bytes = ffi.string(text_ptr)
        text = text_bytes.decode("ascii")

        # text_ptr is automatically freed by python garbage collector
        return text

    def emit_binary(self) -> bytes:
        struct = lib.BinaryenModuleAllocateAndWrite(self.ref, ffi.NULL)

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
