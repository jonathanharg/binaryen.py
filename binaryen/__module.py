"""Binaryen representation of WebAssembly modules"""

from typing import Any

from . import literal
from .__expression import Block, Expression
from .__feature import Feature
from .__functionref import FunctionRef
from .__global import Global
from ._binaryen import ffi, lib
from .internals import BinaryenHeapType, BinaryenLiteral, BinaryenOp, BinaryenType
from .type import TypeNone

type BinaryenExportRef = Any


def _none_to_null[T](possibly_none: T | None) -> ffi.CData | T:
    if possibly_none is None:
        return ffi.NULL
    return possibly_none


def _none_to_binaryen(possibly_none: BinaryenType | None) -> BinaryenType:
    if possibly_none is None:
        return TypeNone
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

    def i32(self, value: int):
        return self.const(literal.int32(value))

    def i64(self, value: int):
        return self.const(literal.int64(value))

    def f32(self, value: float):
        return self.const(literal.float32(value))

    def f64(self, value: float):
        return self.const(literal.float64(value))

    def block(
        self,
        name: bytes | None,
        children: list[Expression],
        binaryen_type: BinaryenType,
    ) -> Block:
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
        if_false: Expression | None,
    ) -> Expression:
        if_false_safe = ffi.NULL if if_false is None else if_false.ref
        ref = lib.BinaryenIf(self.ref, condition.ref, if_true.ref, if_false_safe)
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

    # TODO: Switch

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

    # TODO: CallIndirect, ReturnCall, ReturnCallIndirect,

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

    def load(
        self,
        load_bytes: bytes,
        signed: bool,
        offset: int,
        align: int,
        load_type: BinaryenType,
        ptr: Expression,
        memory_name: bytes,
    ) -> Expression:
        ref = lib.BinaryenLoad(
            self.ref, load_bytes, signed, offset, align, load_type, ptr.ref, memory_name
        )
        return Expression(ref)

    def store(
        self,
        bytes_store: bytes,
        offset: int,
        align: int,
        ptr: Expression,
        value: Expression,
        store_type: BinaryenType,
        memory_name: bytes,
    ) -> Expression:
        ref = lib.BinaryenStore(
            self.ref,
            bytes_store,
            offset,
            align,
            ptr.ref,
            value.ref,
            store_type,
            _none_to_null(memory_name),
        )
        return Expression(ref)

    def const(self, value: BinaryenLiteral) -> Expression:
        ref = lib.BinaryenConst(self.ref, value)
        return Expression(ref)

    def unary(self, op: BinaryenOp, value: Expression) -> Expression:
        ref = lib.BinaryenUnary(self.ref, op, value.ref)
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

    def Return(self, value: Expression | None) -> Expression:
        expression_ref = ffi.NULL if value is None else value.ref
        result_ref = lib.BinaryenReturn(self.ref, expression_ref)
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
    # TODO: MemoryInit, DataDrop, MemoryCopy, MemoryFill,
    # TODO: RefNull, RefIsNull, RefAs, RefFuc, RefEq
    # TODO: TableGet, TableSet, TableSize, TableGrow
    # TODO: Try, Throw, Rethrow,
    # TODO: TupleMake, TupleExtract, Pop, RefI31, I31Get
    # TODO: CallRef, ReftTest, RefCast, BrOn
    # TODO: StructNew, StructGet, StructSet

    def array_new(
        self, heap_type: BinaryenHeapType, size: Expression, init: Expression
    ):
        ref = lib.BinaryenArrayNew(self.ref, heap_type, size.ref, init.ref)
        return Expression(ref)

    def array_new_data(
        self,
        heap_type: BinaryenHeapType,
        name: bytes,
        offset: Expression,
        size: Expression,
    ):
        ref = lib.BinaryenArrayNewData(self.ref, heap_type, name, offset.ref, size.ref)
        return Expression(ref)

    def array_new_fixed(self, heap_type: BinaryenHeapType, values: list[Expression]):
        num_values = len(values)
        value_refs = list(map(lambda x: x.ref, values))
        ref = lib.BinaryenArrayNewFixed(self.ref, heap_type, value_refs, num_values)
        return Expression(ref)

    def array_get(
        self, ref: Expression, index: Expression, array_type: BinaryenType, signed: bool
    ):
        ref = lib.BinaryenArrayGet(self.ref, ref.ref, index.ref, array_type, signed)
        return Expression(ref)

    def array_set(self, ref: Expression, index: Expression, value: Expression):
        ref = lib.BinaryenArraySet(self.ref, ref.ref, index.ref, value.ref)
        return Expression(ref)

    def array_len(self, ref: Expression):
        ref = lib.BinaryenArrayLen(self.ref, ref.ref)
        return Expression(ref)

    def array_copy(
        self,
        dest_ref: Expression,
        dest_index: Expression,
        src_ref: Expression,
        src_index: Expression,
        length: Expression,
    ):
        ref = lib.BinaryenArrayCopy(
            self.ref,
            dest_ref.ref,
            dest_index.ref,
            src_ref.ref,
            src_index.ref,
            length.ref,
        )
        return Expression(ref)

    # TODO: StringNew

    def string_const(self, name: bytes) -> Expression:
        ref = lib.BinaryenStringConst(self.ref, name)
        return Expression(ref)

    # TODO: StringMeasure, StringEncode, StringConcat, StringEq, StringAs, StringWTF8Advance, StringTWF16Get, StringIterNext, StringIterMove, StringSliceWTF, StringSliceIter

    #### Getters/Setters for BinaryenExpression ####

    # TODO: If: GetCondition ... SetIfFalse

    # TODO: Loop: GetName ... SetBody

    # TODO: Break: GetName ... SetValue

    # TODO: Switch: GetNumNames ... SetValue

    # TODO: Call: GetTarget ... SetReturn

    # TODO: CallIndirect: GetTarget ... SetResults

    # TODO: LocalGet ... StringSliceItter

    def add_function(
        self,
        name: bytes,
        params: BinaryenType | None,
        results: BinaryenType | None,
        var_types: list[BinaryenType] | None,
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

    # TODO: BinaryenAddFunctionWithHeapType

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

    # Imports

    def add_function_import(
        self,
        internal_name: bytes,
        external_module_name: bytes,
        external_base_name: bytes,
        params: BinaryenType,
        results: BinaryenType,
    ) -> None:
        lib.BinaryenAddFunctionImport(
            self.ref,
            internal_name,
            external_module_name,
            external_base_name,
            params,
            results,
        )

    # TODO: AddTableImport, AddMemoryImport, AddGlobalImport, AddTagImport

    def add_function_export(
        self, internal_name: bytes, external_name: bytes
    ) -> BinaryenExportRef:
        return lib.BinaryenAddFunctionExport(self.ref, internal_name, external_name)

    # TODO: AddTableExport, AddMemoryExport, AddGlobalExport, AddTagExport

    # TODO: GetExport, RemoveExport, GetNumExports, GetExportByIndex

    def add_global(
        self, name: bytes, global_type: BinaryenType, mutable: bool, init: Expression
    ):
        ref = lib.BinaryenAddGlobal(self.ref, name, global_type, mutable, init.ref)
        return Global(ref)

    def get_global(self, name: bytes):
        ref = lib.BinaryenGetGlobal(self.ref, name)
        if ref == ffi.NULL:
            return None
        return Global(ref)

    def remove_global(self, name: bytes):
        lib.BinaryenRemoveGlobal(self.ref, name)

    def get_num_globals(self):
        return int(lib.BinaryenGetNumGlobals(self.ref))

    def get_global_by_index(self, index: int):
        ref = lib.BinaryenGetGlobalByIndex(self.ref, index)
        return Global(ref)

    # TODO: AddTag, GetTag, RemoveTag

    # TODO: AddTable, RemoveTable, GetNumTables, GetTable, GetTableByIndex

    # TODO: ElementSegments

    def set_memory(
        self,
        initial: int,
        maximum: int,
        export_name: bytes,
        segment_names: list[bytes],
        segment_datas: list[bytes],
        segment_passive: list[bool],
        segment_offsets: list[Expression],
        segment_sizes: list[int],
        shared: bool,
        memory64: bool,
        name: bytes,
    ):
        if not (
            len(segment_names)
            == len(segment_datas)
            == len(segment_passive)
            == len(segment_offsets)
            == len(segment_sizes)
        ):
            raise RuntimeError("Segment sizes do not match")

        segment_offset_refs = list(map(lambda x: x.ref, segment_offsets))
        segment_names_charptr = list(map(lambda x: ffi.new("char[]", x), segment_names))
        segment_datas_charptr = list(map(lambda x: ffi.new("char[]", x), segment_datas))

        lib.BinaryenSetMemory(
            self.ref,
            initial,
            maximum,
            export_name,
            segment_names_charptr,
            segment_datas_charptr,
            segment_passive,
            segment_offset_refs,
            segment_sizes,
            len(segment_names),
            shared,
            memory64,
            name,
        )

    # TODO: HasMemory, MemoryGetInitial, MemoryHasMax, MemoryGetMax, MemoryImportGetModule, MemoryImportGetBase, MemoryIsShared, MemoryIs64

    # TODO: GetNumMemorySegments, GetMemorySegmentByteOffset, GetMemorySegmentByteLength, GetMemorySegmentPassive, CopyMemorySegmentData

    def set_start(self, start: FunctionRef):
        lib.BinaryenSetStart(self.ref, start.ref)

    def get_features(self):
        bit_flags = lib.BinaryenModuleGetFeatures(self.ref)
        return Feature(bit_flags)

    def set_feature(self, feature: Feature):
        lib.BinaryenModuleSetFeatures(self.ref, feature.value)

    # TODO: Module Parse

    def print(self) -> None:
        lib.BinaryenModulePrint(self.ref)

    # TODO: PrintStackIR, PrintAsmjs

    def validate(self) -> bool:
        return lib.BinaryenModuleValidate(self.ref)

    def optimize(self) -> None:
        return lib.BinaryenModuleOptimize(self.ref)

    # TODO: ModuleUpdateMaps, GetOptimizeLevel, SetOptimizeLevel, GetShrinkLevel, SetShrinkLevel, GetDebugInfo, SetDebugInfo
    # TODO: GetLowMemoryUnused, SetLowMemoryUnused, GetZeroFilledMemory, SetZeroFilledMemory, GetFastMath, SetFastMath
    # TODO: GetPassArgument, SetPassArgument, ClearPassArguments
    # TODO: Optimisation settings.....

    def auto_drop(self):
        lib.BinaryenModuleAutoDrop(self.ref)

    # TODO: WriteText, WriteStackIR, WriteWithSourceMap

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

    # TODO: Function Operations, Table Operations, Elem Segment Operations, Global Operations, Tag Operations, Import Operations, Export Operations, custom Sections
    # TODO: SideEffects
    # TODO: CFG/Relooper
    # TODO: Expression Runner

    # TODO: SetTypeName, SetFieldName

    # TODO: Utilities
