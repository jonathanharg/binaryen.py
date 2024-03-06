from ._binaryen import ffi, lib
from .internals import (
    BinaryenExpressionId,
    BinaryenHeapType,
    BinaryenPackedType,
    BinaryenType,
)

type_builder_errors = {
    lib.TypeBuilderErrorReasonSelfSupertype(): "Self Supertype",
    lib.TypeBuilderErrorReasonInvalidSupertype(): "Invalid Supertype",
    lib.TypeBuilderErrorReasonForwardSupertypeReference(): "Forward Supertype Reference",
    lib.TypeBuilderErrorReasonForwardChildReference(): "Forward Child Reference",
}


class TypeBuilder:
    def __init__(self, size: int):
        self.ref = lib.TypeBuilderCreate(size)

    def grow(self, count: int):
        if self.ref is None:
            raise RuntimeError("Cannot access TypeBuilder after it has been built.")
        lib.TypeBuilderGrow(self.ref, count)

    def get_size(self) -> int:
        if self.ref is None:
            raise RuntimeError("Cannot access TypeBuilder after it has been built.")
        return lib.TypeBuilderGetSize(self.ref)

    def set_signature_type(
        self, index: int, param_types: BinaryenType, result_types: BinaryenType
    ):
        if self.ref is None:
            raise RuntimeError("Cannot access TypeBuilder after it has been built.")
        lib.TypeBuilderSetSignatureType(self.ref, index, param_types, result_types)

    # TODO: SetStructType

    def set_array_type(
        self,
        index: int,
        element_type: BinaryenType,
        element_packed_type: BinaryenPackedType,
        element_mutable: bool,
    ):
        if self.ref is None:
            raise RuntimeError("Cannot access TypeBuilder after it has been built.")
        lib.TypeBuilderSetArrayType(
            self.ref, index, element_type, element_packed_type, element_mutable
        )

    # TODO: GetTempHeapType, GetTempTupleType, TempRefType, SetSubType, SetOpen, CreateRecGroup

    def build(self):
        if self.ref is None:
            raise RuntimeError("Cannot access TypeBuilder after it has been built.")

        size = self.get_size()
        heap_types = ffi.new(f"BinaryenHeapType[{size}]")
        error_index = ffi.new("BinaryenIndex[1]")
        error_reason = ffi.new("TypeBuilderErrorReason[1]")
        successful = lib.TypeBuilderBuildAndDispose(
            self.ref, heap_types, error_index, error_reason
        )
        self.ref = None

        if not successful:
            raise RuntimeError(
                f"TypeBuilder Error at type index {error_index[0]}: {type_builder_errors[error_reason[0]]}"
            )

        result: list[BinaryenHeapType] = []
        for i in range(size):
            result.append(heap_types[i])
        return result
