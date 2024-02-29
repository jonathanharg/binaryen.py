"""Binaryen representation of WebAssembly modules"""

from typing import Any

from . import literal
from .__expression import Block, Expression
from .__feature import Feature
from .__functionref import FunctionRef
from .internals import Auto, CData, Literal, Op, Type, BinaryenNone
from .binaryen_lib import ffi, lib
from .types import none

type BinaryenExportRef = Any


def _none_to_null[T](possibly_none: T | None) -> CData | T:
    if possibly_none is None:
        return ffi.NULL
    return possibly_none


def _none_to_binaryen[T](possibly_none: T | None) -> BinaryenNone | T:
    if possibly_none is None:
        return none
    return possibly_none


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

    def i32(self, value: int):
        return self.const(literal.int32(value))

    def i64(self, value: int):
        return self.const(literal.int64(value))

    def f32(self, value: int):
        return self.const(literal.float32(value))

    def f64(self, value: int):
        return self.const(literal.float64(value))

    def block(
        self,
        name: bytes | None,
        children: list[Expression],
        binaryen_type: Type | Auto,
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

    def loop(self, label: bytes, body: Expression):
        ref = lib.BinaryenLoop(self.ref, label, body.ref)
        return Expression(ref)

    def Break(
        self, name: bytes, condition: Expression | None, value: Expression | None
    ):
        condition_ref = ffi.NULL if condition is None else condition.ref
        value_ref = ffi.NULL if value is None else value.ref

        ref = lib.BinaryenBreak(self.ref, name, condition_ref, value_ref)
        return Expression(ref)

    # TODO: Switch, Call, CallIndirect, ReturnCall, ReturnCallIndirect,

    def local_get(self, index: int, local_type: Type) -> Expression:
        ref = lib.BinaryenLocalGet(self.ref, index, local_type)
        return Expression(ref)

    def local_set(self, index: int, value: Expression) -> Expression:
        ref = lib.BinaryenLocalSet(self.ref, index, value.ref)
        return Expression(ref)

    def local_tee(self, index: int, value: Expression, value_type: Type) -> Expression:
        ref = lib.BinaryenLocalTee(self.ref, index, value.ref, value_type)
        return Expression(ref)

    def global_get(self, name: bytes, global_type: Type) -> Expression:
        ref = lib.BinaryenGlobalGet(self.ref, name, global_type)
        return Expression(ref)

    def global_set(self, name: bytes, value: Expression) -> Expression:
        ref = lib.BinaryenGlobalSet(self.ref, name, value.ref)
        return Expression(ref)

    def load(
        self,
        signed: bool,
        offset: int,
        align: int,
        load_type: Type,
        ptr: Expression,
        memory_name: bytes,
    ) -> Expression:
        ref = lib.BinaryenLoad(
            self.ref, signed, offset, align, load_type, ptr.ref, memory_name
        )
        return Expression(ref)

    def store(
        self,
        bytes_num: int,
        offset: int,
        align: int,
        ptr: Expression,
        value: Expression,
        store_type: Type,
        memory_name: bytes,
    ) -> Expression:
        ref = lib.BinaryenStore(
            self.ref,
            bytes_num,
            offset,
            align,
            ptr.ref,
            value.ref,
            store_type,
            memory_name,
        )
        return Expression(ref)

    def const(self, value: Literal) -> Expression:
        ref = lib.BinaryenConst(self.ref, value)
        return Expression(ref)

    def unary(self, op: Op, value: Expression) -> Expression:
        ref = lib.BinaryenUnary(self.ref, op, value.ref)
        return Expression(ref)

    def binary(self, op: Op, left: Expression, right: Expression) -> Expression:
        ref = lib.BinaryenBinary(self.ref, op, left.ref, right.ref)
        return Expression(ref)

    def select(
        self,
        condition: Expression,
        if_true: Expression,
        if_false: Expression,
        select_type: Type,
    ) -> Expression:
        ref = lib.BinaryenSelect(
            self.ref, condition.ref, if_true.ref, if_false.ref, select_type
        )
        return Expression(ref)

    def drop(self, value: Expression) -> Expression:
        ref = lib.BinaryenDrop(self.ref, value.ref)
        return Expression(ref)

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
    # TODO: ArrayNew

    def array_new_fixed(self, heap_type: any, values: list[Expression]):
        # TODO: Fix type
        num_values = len(values)
        value_refs = list(map(lambda x: x.ref, values))
        ref = lib.BinaryenArrayNewFixed(self.ref, heap_type, value_refs, num_values)
        return Expression(ref)

    # TODO: ArrayGet, ArraySet, ArrayLen, ArrayCopy
    # TODO: StringNew

    def string_const(self, name: bytes) -> Expression:
        ref = lib.BinaryenStringConst(self.ref, name)
        return Expression(ref)

    # TODO: StringMeasure, StringEncode, StringConcat, StringEq, StringAs, StringWTF8Advance, StringTWF16Get, StringIterNext, StringIterMove, StringSliceWTF, StringSliceIter

    # TODO: Carry on from here

    # if_get_condition
    # if_set_condition
    # if_get_if_true
    # if_set_if_true
    # if_get_if_false
    # if_set_if_false

    # loop_get_name
    # loop_set_name
    # loop_get_body
    # loop_set_body

    # break_get_name
    # break_set_name
    # break_set_condition
    # break_get_value
    # break_set_value

    # switch_get_num_names
    # switch_get_name_at
    # switch_set_name_at
    # switch_append_name
    # switch_insert_name_at
    # switch_remove_name_at
    # switch_get_default_name
    # switch_set_default_name
    # switch_get_condition
    # switch_get_value
    # switch_set_value

    # call_get_target
    # call_set_target

    # call_get_num_operands
    # call_get_operand_at
    # call_set_operand_at
    # call_append_operand
    # call_insert_operand_at
    # call_remove_operand_at
    # call_is_return
    # call_set_return

    # Imports

    def add_function_import(
        self,
        internal_name: bytes,
        external_module_name: bytes,
        external_base_name: bytes,
        params: Type,
        results: Type,
    ) -> None:
        lib.BinaryenAddFunctionImport(
            self.ref,
            internal_name,
            external_module_name,
            external_base_name,
            params,
            results,
        )

    # EXTRA:

    def add_function(
        self,
        name: bytes,
        params: Type | None,
        results: Type | None,
        var_types: list[Type] | None,
        body: Expression,
    ):
        if var_types is None or (len(var_types) == 0):
            length = 0
            c_var_types = _none_to_null(var_types)
        else:
            length = len(var_types)
            c_var_types = var_types

        ref = lib.BinaryenAddFunction(
            self.ref,
            name,
            _none_to_binaryen(params),
            _none_to_binaryen(results),
            c_var_types,
            length,
            body.ref,
        )
        return FunctionRef(ref)

    def get_function(self, name: bytes) -> FunctionRef:
        ref = lib.BinaryenGetFunction(self.ref, name)
        return FunctionRef(ref)

    def remove_function(self, name: bytes) -> None:
        lib.BinaryenRemoveFunction(self.ref, name)

    def get_num_functions(self) -> int:
        return lib.BinaryenGetNumFunctions(self.ref)

    def get_function_by_index(self, index: int):
        ref = lib.BinaryenGetFunctionByIndex(self.ref, index)
        return FunctionRef(ref)

    def call(
        self,
        target: bytes,
        operands: list[Expression],
        return_type: Type,
    ) -> Expression:
        operand_refs = list(map(lambda x: x.ref, operands))
        ref = lib.BinaryenCall(
            self.ref, target, operand_refs, len(operand_refs), return_type
        )
        return Expression(ref)

    def auto_drop(self):
        lib.BinaryenModuleAutoDrop(self.ref)

    def set_memory(
        self,
        initial: int,
        maximum: int,
        export_name: bytes,
        segments: list[bytes],
        segment_passive: list[bool],
        segment_offsets: list[Expression],
        segment_sizes: list[int],
        shared: bool,
        memory64: bool,
        name: bytes,
    ):
        if len(segment_sizes) != len(segments):
            raise RuntimeError("Segment sizes do not match")

        segment_offset_refs = list(map(lambda x: x.ref, segment_offsets))
        segments_char_arr = list(map(lambda x: ffi.new("char[]", x), segments))

        lib.BinaryenSetMemory(
            self.ref,
            initial,
            maximum,
            export_name,
            segments_char_arr,
            segment_passive,
            segment_offset_refs,
            segment_sizes,
            len(segments),
            shared,
            memory64,
            name,
        )

    def set_start(self, start: FunctionRef):
        lib.BinaryenSetStart(self.ref, start.ref)

    def get_features(self):
        bit_flags = lib.BinaryenModuleGetFeatures(self.ref)
        return Feature(bit_flags)

    def set_feature(self, feature: Feature):
        lib.BinaryenModuleSetFeatures(self.ref, feature.value)

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

    def emit_binary(self) -> bytes:
        struct = lib.BinaryenModuleAllocateAndWrite(self.ref, ffi.NULL)

        binary_ptr = ffi.cast("char *", struct.binary)  # char * pointer to the binary
        binary_len = struct.binaryBytes

        binary = ffi.unpack(binary_ptr, binary_len)  # reads binary buffer into python

        # print([x for x in binary]) # Debug: print int values of memory buffer
        return binary

    def write_text(self, filename: str):
        with open(filename, "w", encoding="utf-8") as file:
            text = self.emit_text()
            file.write(text)

    def write_binary(self, filename: str):
        with open(filename, "wb") as file:
            binary = self.emit_binary()
            file.write(binary)
