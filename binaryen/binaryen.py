from .types import BinaryenType
from .lib import lib

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


