from typing import Any, TypeAlias, TypeVar
from .types import BinaryenType
from .lib import lib
from ._binaryen_cffi import ffi, _cffi_backend

BinaryenExpressionRef: TypeAlias = Any
BinaryenExpression: TypeAlias = Any
BinaryenLiteral: TypeAlias = Any
BinaryenOp: TypeAlias = Any
BinaryenExpressionId: TypeAlias = Any
BinaryenExportRef: TypeAlias = Any

T = TypeVar("T")


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


def type_create(types: list[BinaryenType]) -> BinaryenType:
    """Create a Binaryen type

    Args:
        types (list[BinaryenType]): List of input types

    Returns:
        BinaryenType: Combined type

    Examples:
        Under the hood, BinaryenTypes are stored as numeric ids
        >>> twoStrings = binaryen.type_create([binaryen.stringref, binaryen.stringref])
        >>> isinstance(twoStrings, int)
        True
    """
    return lib.BinaryenTypeCreate(types, len(types))


# Number of arguments
def type_arity(binaryen_type: BinaryenType) -> int:
    return lib.BinaryenTypeArity(binaryen_type)


# TODO: BinaryenTypeExpand

# TODO: BinaryenPackedType

# TODO: BinaryenHeapType

# TODO: BinaryenStructType

# TODO: BinaryenArrayType

# TODO: BinaryenHeapType


def type_is_nullable(binaryen_type: BinaryenType) -> bool:
    """Get if a Binaryen type is nullable (possibly none) or not.

    Args:
        binaryen_type (BinaryenType): The type to be tested

    Returns:
        bool: If the type is nullable

    Examples:
        >>> binaryen.type_is_nullable(binaryen.i32)
        False
        >>> binaryen.type_is_nullable(binaryen.anyref)
        True
    """
    return lib.BinaryenTypeIsNullable(binaryen_type)


# TODO: BinaryenTypeFromHeapType

# TODO: BinaryExpressionId

# TODO: BinaryExternalKind

# TODO: BinaryFeatures


class Module:
    ptr = None

    def __init__(self) -> None:
        self.ptr = lib.BinaryenModuleCreate()
        return

    def __del__(self) -> None:
        # Free the module when it is garbage collected
        lib.BinaryenModuleDispose(self.ptr)

    # TODO: binaryenLiteral

    # TODO: binaryenOp

    def block(
        self,
        name: bytes | None,
        children: list[BinaryenExpression],
        binaryen_type: BinaryenType,
    ) -> BinaryenExpressionRef:
        return lib.BinaryenBlock(
            self.ptr, _none_to_null(name), children, len(children), binaryen_type
        )

    def If(
        self,
        condition: BinaryenExpressionRef,
        if_true: BinaryenExpressionRef,
        if_false: BinaryenExpressionRef,
    ) -> BinaryenExpressionRef:
        return lib.BinaryenIf(self.ptr, condition, if_true, if_false)

    # TODO: Loop, Break, Switch, Call, CallIndirect, ReturnCall, ReturnCallIndirect,

    def local_get(self, index: int, local_type: BinaryenType) -> BinaryenExpressionRef:
        return lib.BinaryenLocalGet(self.ptr, index, local_type)

    def local_set(
        self, index: int, value: BinaryenExpressionRef
    ) -> BinaryenExpressionRef:
        return lib.BinaryenLocalSet(self.ptr, index, value)

    def local_tee(
        self, index: int, value: BinaryenExpressionRef, value_type: BinaryenType
    ) -> BinaryenExpressionRef:
        return lib.BinaryenLocalTee(self.ptr, index, value, value_type)

    def global_get(
        self, name: bytes, global_type: BinaryenType
    ) -> BinaryenExpressionRef:
        return lib.BinaryenGlobalGet(self.ptr, name, global_type)

    def global_set(
        self, name: bytes, value: BinaryenExpressionRef
    ) -> BinaryenExpressionRef:
        return lib.BinaryenGlobalSet(self.ptr, name, value)

    # TODO: Load, Store

    def const(self, value: BinaryenLiteral) -> BinaryenExpressionRef:
        return lib.BinaryenConst(self.ptr, value)

    def unary(
        self, op: BinaryenOp, left: BinaryenExpressionRef, right: BinaryenExpressionRef
    ) -> BinaryenExpressionRef:
        return lib.BinaryenUnary(self.ptr, op, left, right)

    def binary(
        self, op: BinaryenOp, left: BinaryenExpressionRef, right: BinaryenExpressionRef
    ) -> BinaryenExpressionRef:
        return lib.BinaryenBinary(self.ptr, op, left, right)

    def select(
        self,
        condition: BinaryenExpressionRef,
        if_true: BinaryenExpressionRef,
        if_false: BinaryenExpressionRef,
        select_type: BinaryenType,
    ) -> BinaryenExpressionRef:
        return lib.BinaryenSelect(self.ptr, condition, if_true, if_false, select_type)

    def drop(self, value: BinaryenExpressionRef) -> BinaryenExpressionRef:
        return lib.BinaryenDrop(self.ptr, value)

    # TODO: Come up with a better name for this
    def Return(self, value: BinaryenExpressionRef | None) -> BinaryenExpressionRef:
        return lib.BinaryenReturn(self.ptr, _none_to_null(value))

    # TODO: MemorySize, MemoryGrow

    def nop(self) -> BinaryenExpressionRef:
        return lib.BinaryenNop(self.ptr)

    def unreachable(self) -> BinaryenExpressionRef:
        return lib.BinaryenUnreachable(self.ptr)

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

    # TODO This should probably be some sort of inner class
    def expression_get_id(self, expr: BinaryenExpressionRef) -> BinaryenExpressionId:
        return lib.BinaryenExpressionGetId(expr)

    def expression_get_type(self, expr: BinaryenExpressionRef) -> BinaryenType:
        return lib.BinaryenExpressionGetType(expr)

    def expression_set_type(
        self, expr: BinaryenExpressionRef, expr_type: BinaryenType
    ) -> None:
        return lib.BinaryenExpressionSetType(expr, expr_type)

    def expression_print(self, expr: BinaryenExpressionRef) -> None:
        return lib.BinaryenExpressionPrint(expr)

    def expression_finalize(self, expr: BinaryenExpressionRef) -> None:
        return lib.BinaryenExpressionFinalize(expr)

    def expression_copy(self, expr: BinaryenExpressionRef) -> BinaryenExpressionRef:
        return lib.BinaryenExpressionCopy(expr, self.ptr)

    def block_get_name(self, expr: BinaryenExpressionRef) -> bytes | None:
        return lib.BinaryenBlockGetName(expr)

    def block_set_name(self, expr: BinaryenExpressionRef, name: bytes) -> None:
        return lib.BinaryenBlockSetName(expr, name)

    def block_get_num_children(self, expr: BinaryenExpressionRef) -> int:
        return lib.BinaryenBlockGetNumChildren(expr)

    def block_get_child_at(
        self, expr: BinaryenExpressionRef, index: int
    ) -> BinaryenExpressionRef:
        return lib.BinaryenBlockGetChildAt(expr, index)

    def block_set_child_at(
        self, expr: BinaryenExpressionRef, index: int, child: BinaryenExpressionRef
    ) -> None:
        return lib.BinaryenBlockSetChildAt(expr, index, child)

    def block_append_child(
        self, expr: BinaryenExpressionRef, child: BinaryenExpressionRef
    ) -> int:
        return lib.BinaryenBlockAppendChild(expr, child)

    def block_insert_child_at(
        self, expr: BinaryenExpressionRef, index: int, child: BinaryenExpressionRef
    ) -> None:
        return lib.BinaryenBlockInsertChildAt(expr, index, child)

    def block_remove_child_at(
        self, expr: BinaryenExpressionRef, index: int
    ) -> BinaryenExpressionRef:
        return lib.BinaryenBlockRemoveChildAt(expr, index)

    def add_function(
        self,
        name: bytes,
        params: BinaryenType,
        results: BinaryenType,
        var_types: list[BinaryenType],
        body: BinaryenExpressionRef,
    ) -> None:
        return lib.BinaryenAddFunction(
            self.ptr, name, params, results, var_types, len(var_types), body
        )

    def call(
        self,
        target: bytes,
        operands: list[BinaryenExpressionRef],
        return_type: BinaryenType,
    ):
        return lib.BinaryenCall(self.ptr, target, operands, len(operands), return_type)

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
