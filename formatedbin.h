

//================
// Binaryen C API
//
// The first part of the API lets you create modules and their parts.
//
// The second part of the API lets you perform operations on modules.
//
// The third part of the API lets you provide a general control-flow
//   graph (CFG) as input.
//
// The final part of the API contains miscellaneous utilities like
//   debugging for the API itself.
//
// ---------------
//
// Thread safety: You can create Expressions in parallel, as they do not
//                refer to global state. BinaryenAddFunction is also
//                thread-safe, which means that you can create functions and
//                their contents in multiple threads. This is important since
//                functions are where the majority of the work is done.
//                Other methods - creating imports, exports, etc. - are
//                not currently thread-safe (as there is typically no need
//                to parallelize them).
//
//================

typedef long int ptrdiff_t;

typedef long unsigned int size_t;

typedef int wchar_t;

typedef long double max_align_t;

// AIX system headers need stdint.h to be re-enterable while _STD_TYPES_T
// is defined until an inclusion of it without _STD_TYPES_T occurs, in which
// case the header guard macro is defined.

// C99 7.18.3 Limits of other integer types
//
//  Footnote 219, 220: C++ implementations should define these macros only when
//  __STDC_LIMIT_MACROS is defined before <stdint.h> is included.
//
//  Footnote 222: C++ implementations should define these macros only when
//  __STDC_CONSTANT_MACROS is defined before <stdint.h> is included.
//
// C++11 [cstdint.syn]p2:
//
//  The macros defined by <cstdint> are provided unconditionally. In particular,
//  the symbols __STDC_LIMIT_MACROS and __STDC_CONSTANT_MACROS (mentioned in
//  footnotes 219, 220, and 222 in the C standard) play no role in C++.
//
// C11 removed the problematic footnotes.
//
// Work around this inconsistency by always defining those macros in C++ mode,
// so that a C library implementation which follows the C99 standard can be
// used in C++.

typedef signed char int8_t;

typedef short int16_t;

typedef int int32_t;

typedef long long int64_t;

typedef unsigned char uint8_t;

typedef unsigned short uint16_t;

typedef unsigned int uint32_t;

typedef unsigned long long uint64_t;

typedef int8_t int_least8_t;
typedef int16_t int_least16_t;
typedef int32_t int_least32_t;
typedef int64_t int_least64_t;
typedef uint8_t uint_least8_t;
typedef uint16_t uint_least16_t;
typedef uint32_t uint_least32_t;
typedef uint64_t uint_least64_t;

typedef int8_t int_fast8_t;
typedef int16_t int_fast16_t;
typedef int32_t int_fast32_t;
typedef int64_t int_fast64_t;
typedef uint8_t uint_fast8_t;
typedef uint16_t uint_fast16_t;
typedef uint32_t uint_fast32_t;
typedef uint64_t uint_fast64_t;

#define __deprecated_msg(_msg) __attribute__((__deprecated__(_msg)))

#define __deprecated_enum_msg(_msg) __deprecated_msg(_msg)

typedef __signed char __int8_t;

typedef unsigned char __uint8_t;
typedef short __int16_t;
typedef unsigned short __uint16_t;
typedef int __int32_t;
typedef unsigned int __uint32_t;
typedef long long __int64_t;
typedef unsigned long long __uint64_t;

typedef long __darwin_intptr_t;
typedef unsigned int __darwin_natural_t;

typedef int __darwin_ct_rune_t;

typedef union {
  char __mbstate8[128];
  long long _mbstateL;
} __mbstate_t;

typedef __mbstate_t __darwin_mbstate_t;

typedef long int __darwin_ptrdiff_t;

typedef long unsigned int __darwin_size_t;

typedef __builtin_va_list __darwin_va_list;

typedef int __darwin_wchar_t;

typedef __darwin_wchar_t __darwin_rune_t;

typedef int __darwin_wint_t;

typedef unsigned long __darwin_clock_t;
typedef __uint32_t __darwin_socklen_t;
typedef long __darwin_ssize_t;
typedef long __darwin_time_t;

typedef __int64_t __darwin_blkcnt_t;
typedef __int32_t __darwin_blksize_t;
typedef __int32_t __darwin_dev_t;
typedef unsigned int __darwin_fsblkcnt_t;
typedef unsigned int __darwin_fsfilcnt_t;
typedef __uint32_t __darwin_gid_t;
typedef __uint32_t __darwin_id_t;
typedef __uint64_t __darwin_ino64_t;

typedef __darwin_ino64_t __darwin_ino_t;

typedef __darwin_natural_t __darwin_mach_port_name_t;
typedef __darwin_mach_port_name_t __darwin_mach_port_t;
typedef __uint16_t __darwin_mode_t;
typedef __int64_t __darwin_off_t;
typedef __int32_t __darwin_pid_t;
typedef __uint32_t __darwin_sigset_t;
typedef __int32_t __darwin_suseconds_t;
typedef __uint32_t __darwin_uid_t;
typedef __uint32_t __darwin_useconds_t;
typedef unsigned char __darwin_uuid_t[16];
typedef char __darwin_uuid_string_t[37];

// pthread opaque structures

struct __darwin_pthread_handler_rec {
  void (*__routine)(void *); // Routine to call
  void *__arg;               // Argument to pass
  struct __darwin_pthread_handler_rec *__next;
};

struct _opaque_pthread_attr_t {
  long __sig;
  char __opaque[56];
};

struct _opaque_pthread_cond_t {
  long __sig;
  char __opaque[40];
};

struct _opaque_pthread_condattr_t {
  long __sig;
  char __opaque[8];
};

struct _opaque_pthread_mutex_t {
  long __sig;
  char __opaque[56];
};

struct _opaque_pthread_mutexattr_t {
  long __sig;
  char __opaque[8];
};

struct _opaque_pthread_once_t {
  long __sig;
  char __opaque[8];
};

struct _opaque_pthread_rwlock_t {
  long __sig;
  char __opaque[192];
};

struct _opaque_pthread_rwlockattr_t {
  long __sig;
  char __opaque[16];
};

struct _opaque_pthread_t {
  long __sig;
  struct __darwin_pthread_handler_rec *__cleanup_stack;
  char __opaque[8176];
};

typedef struct _opaque_pthread_attr_t __darwin_pthread_attr_t;
typedef struct _opaque_pthread_cond_t __darwin_pthread_cond_t;
typedef struct _opaque_pthread_condattr_t __darwin_pthread_condattr_t;
typedef unsigned long __darwin_pthread_key_t;
typedef struct _opaque_pthread_mutex_t __darwin_pthread_mutex_t;
typedef struct _opaque_pthread_mutexattr_t __darwin_pthread_mutexattr_t;
typedef struct _opaque_pthread_once_t __darwin_pthread_once_t;
typedef struct _opaque_pthread_rwlock_t __darwin_pthread_rwlock_t;
typedef struct _opaque_pthread_rwlockattr_t __darwin_pthread_rwlockattr_t;
typedef struct _opaque_pthread_t *__darwin_pthread_t;

typedef unsigned char u_int8_t;

typedef unsigned short u_int16_t;

typedef unsigned int u_int32_t;

typedef unsigned long long u_int64_t;

typedef int64_t register_t;

typedef unsigned long uintptr_t;

typedef u_int64_t user_addr_t;
typedef u_int64_t user_size_t;
typedef int64_t user_ssize_t;
typedef int64_t user_long_t;
typedef u_int64_t user_ulong_t;
typedef int64_t user_time_t;
typedef int64_t user_off_t;

typedef u_int64_t syscall_arg_t;

typedef __darwin_intptr_t intptr_t;

typedef long int intmax_t;

typedef long unsigned int uintmax_t;

//
// ========== Module Creation ==========
//

// BinaryenIndex
//
// Used for internal indexes and list sizes.

typedef uint32_t BinaryenIndex;

// Core types (call to get the value of each; you can cache them, they
// never change)

typedef uintptr_t BinaryenType;

BinaryenType BinaryenTypeNone(void);
BinaryenType BinaryenTypeInt32(void);
BinaryenType BinaryenTypeInt64(void);
BinaryenType BinaryenTypeFloat32(void);
BinaryenType BinaryenTypeFloat64(void);
BinaryenType BinaryenTypeVec128(void);
BinaryenType BinaryenTypeFuncref(void);
BinaryenType BinaryenTypeExternref(void);
BinaryenType BinaryenTypeAnyref(void);
BinaryenType BinaryenTypeEqref(void);
BinaryenType BinaryenTypeI31ref(void);
BinaryenType BinaryenTypeStructref(void);
BinaryenType BinaryenTypeArrayref(void);
BinaryenType BinaryenTypeStringref(void);
BinaryenType BinaryenTypeStringviewWTF8(void);
BinaryenType BinaryenTypeStringviewWTF16(void);
BinaryenType BinaryenTypeStringviewIter(void);
BinaryenType BinaryenTypeNullref(void);
BinaryenType BinaryenTypeNullExternref(void);
BinaryenType BinaryenTypeNullFuncref(void);
BinaryenType BinaryenTypeUnreachable(void);
// Not a real type. Used as the last parameter to BinaryenBlock to let
// the API figure out the type instead of providing one.
BinaryenType BinaryenTypeAuto(void);
BinaryenType BinaryenTypeCreate(BinaryenType *valueTypes, BinaryenIndex numTypes);
uint32_t BinaryenTypeArity(BinaryenType t);
void BinaryenTypeExpand(BinaryenType t, BinaryenType *buf);

__attribute__((deprecated)) BinaryenType BinaryenNone(void);
__attribute__((deprecated)) BinaryenType BinaryenInt32(void);
__attribute__((deprecated)) BinaryenType BinaryenInt64(void);
__attribute__((deprecated)) BinaryenType BinaryenFloat32(void);
__attribute__((deprecated)) BinaryenType BinaryenFloat64(void);
__attribute__((deprecated)) BinaryenType BinaryenUndefined(void);

// Packed types (call to get the value of each; you can cache them)

typedef uint32_t BinaryenPackedType;

BinaryenPackedType BinaryenPackedTypeNotPacked(void);
BinaryenPackedType BinaryenPackedTypeInt8(void);
BinaryenPackedType BinaryenPackedTypeInt16(void);

// Heap types

typedef uintptr_t BinaryenHeapType;

BinaryenHeapType BinaryenHeapTypeExt(void);
BinaryenHeapType BinaryenHeapTypeFunc(void);
BinaryenHeapType BinaryenHeapTypeAny(void);
BinaryenHeapType BinaryenHeapTypeEq(void);
BinaryenHeapType BinaryenHeapTypeI31(void);
BinaryenHeapType BinaryenHeapTypeStruct(void);
BinaryenHeapType BinaryenHeapTypeArray(void);
BinaryenHeapType BinaryenHeapTypeString(void);
BinaryenHeapType BinaryenHeapTypeStringviewWTF8(void);
BinaryenHeapType BinaryenHeapTypeStringviewWTF16(void);
BinaryenHeapType BinaryenHeapTypeStringviewIter(void);
BinaryenHeapType BinaryenHeapTypeNone(void);
BinaryenHeapType BinaryenHeapTypeNoext(void);
BinaryenHeapType BinaryenHeapTypeNofunc(void);

_Bool BinaryenHeapTypeIsBasic(BinaryenHeapType heapType);
_Bool BinaryenHeapTypeIsSignature(BinaryenHeapType heapType);
_Bool BinaryenHeapTypeIsStruct(BinaryenHeapType heapType);
_Bool BinaryenHeapTypeIsArray(BinaryenHeapType heapType);
_Bool BinaryenHeapTypeIsBottom(BinaryenHeapType heapType);
BinaryenHeapType
BinaryenHeapTypeGetBottom(BinaryenHeapType heapType);
_Bool BinaryenHeapTypeIsSubType(BinaryenHeapType left, BinaryenHeapType right);
BinaryenIndex
BinaryenStructTypeGetNumFields(BinaryenHeapType heapType);
BinaryenType
BinaryenStructTypeGetFieldType(BinaryenHeapType heapType, BinaryenIndex index);
BinaryenPackedType BinaryenStructTypeGetFieldPackedType(
    BinaryenHeapType heapType, BinaryenIndex index
);
_Bool BinaryenStructTypeIsFieldMutable(BinaryenHeapType heapType, BinaryenIndex index);
BinaryenType
BinaryenArrayTypeGetElementType(BinaryenHeapType heapType);
BinaryenPackedType
BinaryenArrayTypeGetElementPackedType(BinaryenHeapType heapType);
_Bool BinaryenArrayTypeIsElementMutable(BinaryenHeapType heapType);
BinaryenType
BinaryenSignatureTypeGetParams(BinaryenHeapType heapType);
BinaryenType
BinaryenSignatureTypeGetResults(BinaryenHeapType heapType);

BinaryenHeapType BinaryenTypeGetHeapType(BinaryenType type);
_Bool BinaryenTypeIsNullable(BinaryenType type);
BinaryenType BinaryenTypeFromHeapType(BinaryenHeapType heapType, _Bool nullable);

// Expression ids (call to get the value of each; you can cache them)

typedef uint32_t BinaryenExpressionId;

BinaryenExpressionId BinaryenInvalidId(void);

BinaryenExpressionId Binaryen##Nop##Id(void);
;
BinaryenExpressionId Binaryen##Block##Id(void);
;
BinaryenExpressionId Binaryen##If##Id(void);
;
BinaryenExpressionId Binaryen##Loop##Id(void);
;
BinaryenExpressionId Binaryen##Break##Id(void);
;
BinaryenExpressionId Binaryen##Switch##Id(void);
;
BinaryenExpressionId Binaryen##Call##Id(void);
;
BinaryenExpressionId Binaryen##CallIndirect##Id(void);
;
BinaryenExpressionId Binaryen##LocalGet##Id(void);
;
BinaryenExpressionId Binaryen##LocalSet##Id(void);
;
BinaryenExpressionId Binaryen##GlobalGet##Id(void);
;
BinaryenExpressionId Binaryen##GlobalSet##Id(void);
;
BinaryenExpressionId Binaryen##Load##Id(void);
;
BinaryenExpressionId Binaryen##Store##Id(void);
;
BinaryenExpressionId Binaryen##AtomicRMW##Id(void);
;
BinaryenExpressionId Binaryen##AtomicCmpxchg##Id(void);
;
BinaryenExpressionId Binaryen##AtomicWait##Id(void);
;
BinaryenExpressionId Binaryen##AtomicNotify##Id(void);
;
BinaryenExpressionId Binaryen##AtomicFence##Id(void);
;
BinaryenExpressionId Binaryen##SIMDExtract##Id(void);
;
BinaryenExpressionId Binaryen##SIMDReplace##Id(void);
;
BinaryenExpressionId Binaryen##SIMDShuffle##Id(void);
;
BinaryenExpressionId Binaryen##SIMDTernary##Id(void);
;
BinaryenExpressionId Binaryen##SIMDShift##Id(void);
;
BinaryenExpressionId Binaryen##SIMDLoad##Id(void);
;
BinaryenExpressionId Binaryen##SIMDLoadStoreLane##Id(void);
;
BinaryenExpressionId Binaryen##MemoryInit##Id(void);
;
BinaryenExpressionId Binaryen##DataDrop##Id(void);
;
BinaryenExpressionId Binaryen##MemoryCopy##Id(void);
;
BinaryenExpressionId Binaryen##MemoryFill##Id(void);
;
BinaryenExpressionId Binaryen##Const##Id(void);
;
BinaryenExpressionId Binaryen##Unary##Id(void);
;
BinaryenExpressionId Binaryen##Binary##Id(void);
;
BinaryenExpressionId Binaryen##Select##Id(void);
;
BinaryenExpressionId Binaryen##Drop##Id(void);
;
BinaryenExpressionId Binaryen##Return##Id(void);
;
BinaryenExpressionId Binaryen##MemorySize##Id(void);
;
BinaryenExpressionId Binaryen##MemoryGrow##Id(void);
;
BinaryenExpressionId Binaryen##Unreachable##Id(void);
;
BinaryenExpressionId Binaryen##Pop##Id(void);
;
BinaryenExpressionId Binaryen##RefNull##Id(void);
;
BinaryenExpressionId Binaryen##RefIsNull##Id(void);
;
BinaryenExpressionId Binaryen##RefFunc##Id(void);
;
BinaryenExpressionId Binaryen##RefEq##Id(void);
;
BinaryenExpressionId Binaryen##TableGet##Id(void);
;
BinaryenExpressionId Binaryen##TableSet##Id(void);
;
BinaryenExpressionId Binaryen##TableSize##Id(void);
;
BinaryenExpressionId Binaryen##TableGrow##Id(void);
;
BinaryenExpressionId Binaryen##Try##Id(void);
;
BinaryenExpressionId Binaryen##Throw##Id(void);
;
BinaryenExpressionId Binaryen##Rethrow##Id(void);
;
BinaryenExpressionId Binaryen##TupleMake##Id(void);
;
BinaryenExpressionId Binaryen##TupleExtract##Id(void);
;
BinaryenExpressionId Binaryen##I31New##Id(void);
;
BinaryenExpressionId Binaryen##I31Get##Id(void);
;
BinaryenExpressionId Binaryen##CallRef##Id(void);
;
BinaryenExpressionId Binaryen##RefTest##Id(void);
;
BinaryenExpressionId Binaryen##RefCast##Id(void);
;
BinaryenExpressionId Binaryen##BrOn##Id(void);
;
BinaryenExpressionId Binaryen##StructNew##Id(void);
;
BinaryenExpressionId Binaryen##StructGet##Id(void);
;
BinaryenExpressionId Binaryen##StructSet##Id(void);
;
BinaryenExpressionId Binaryen##ArrayNew##Id(void);
;
BinaryenExpressionId Binaryen##ArrayNewData##Id(void);
;
BinaryenExpressionId Binaryen##ArrayNewElem##Id(void);
;
BinaryenExpressionId Binaryen##ArrayNewFixed##Id(void);
;
BinaryenExpressionId Binaryen##ArrayGet##Id(void);
;
BinaryenExpressionId Binaryen##ArraySet##Id(void);
;
BinaryenExpressionId Binaryen##ArrayLen##Id(void);
;
BinaryenExpressionId Binaryen##ArrayCopy##Id(void);
;
BinaryenExpressionId Binaryen##ArrayFill##Id(void);
;
BinaryenExpressionId Binaryen##ArrayInitData##Id(void);
;
BinaryenExpressionId Binaryen##ArrayInitElem##Id(void);
;
BinaryenExpressionId Binaryen##RefAs##Id(void);
;
BinaryenExpressionId Binaryen##StringNew##Id(void);
;
BinaryenExpressionId Binaryen##StringConst##Id(void);
;
BinaryenExpressionId Binaryen##StringMeasure##Id(void);
;
BinaryenExpressionId Binaryen##StringEncode##Id(void);
;
BinaryenExpressionId Binaryen##StringConcat##Id(void);
;
BinaryenExpressionId Binaryen##StringEq##Id(void);
;
BinaryenExpressionId Binaryen##StringAs##Id(void);
;
BinaryenExpressionId Binaryen##StringWTF8Advance##Id(void);
;
BinaryenExpressionId Binaryen##StringWTF16Get##Id(void);
;
BinaryenExpressionId Binaryen##StringIterNext##Id(void);
;
BinaryenExpressionId Binaryen##StringIterMove##Id(void);
;
BinaryenExpressionId Binaryen##StringSliceWTF##Id(void);
;
BinaryenExpressionId Binaryen##StringSliceIter##Id(void);
;

// External kinds (call to get the value of each; you can cache them)

typedef uint32_t BinaryenExternalKind;

BinaryenExternalKind BinaryenExternalFunction(void);
BinaryenExternalKind BinaryenExternalTable(void);
BinaryenExternalKind BinaryenExternalMemory(void);
BinaryenExternalKind BinaryenExternalGlobal(void);
BinaryenExternalKind BinaryenExternalTag(void);

// Features. Call to get the value of each; you can cache them. Use bitwise
// operators to combine and test particular features.

typedef uint32_t BinaryenFeatures;

BinaryenFeatures BinaryenFeatureMVP(void);
BinaryenFeatures BinaryenFeatureAtomics(void);
BinaryenFeatures BinaryenFeatureBulkMemory(void);
BinaryenFeatures BinaryenFeatureMutableGlobals(void);
BinaryenFeatures BinaryenFeatureNontrappingFPToInt(void);
BinaryenFeatures BinaryenFeatureSignExt(void);
BinaryenFeatures BinaryenFeatureSIMD128(void);
BinaryenFeatures BinaryenFeatureExceptionHandling(void);
BinaryenFeatures BinaryenFeatureTailCall(void);
BinaryenFeatures BinaryenFeatureReferenceTypes(void);
BinaryenFeatures BinaryenFeatureMultivalue(void);
BinaryenFeatures BinaryenFeatureGC(void);
BinaryenFeatures BinaryenFeatureMemory64(void);
BinaryenFeatures BinaryenFeatureRelaxedSIMD(void);
BinaryenFeatures BinaryenFeatureExtendedConst(void);
BinaryenFeatures BinaryenFeatureStrings(void);
BinaryenFeatures BinaryenFeatureMultiMemories(void);
BinaryenFeatures BinaryenFeatureAll(void);

// Modules
//
// Modules contain lists of functions, imports, exports, function types. The
// Add* methods create them on a module. The module owns them and will free
// their memory when the module is disposed of.
//
// Expressions are also allocated inside modules, and freed with the module.
// They are not created by Add* methods, since they are not added directly on
// the module, instead, they are arguments to other expressions (and then they
// are the children of that AST node), or to a function (and then they are the
// body of that function).
//
// A module can also contain a function table for indirect calls, a memory,
// and a start method.

typedef struct Binaryen##Module *Binaryen##Module##Ref;
;

BinaryenModuleRef BinaryenModuleCreate(void);
void BinaryenModuleDispose(BinaryenModuleRef module);

// Literals. These are passed by value.

struct BinaryenLiteral {
  uintptr_t type;
  union {
    int32_t i32;
    int64_t i64;
    float f32;
    double f64;
    uint8_t v128[16];
    __const char *func;
  };
};

struct BinaryenLiteral BinaryenLiteralInt32(int32_t x);
struct BinaryenLiteral BinaryenLiteralInt64(int64_t x);
struct BinaryenLiteral BinaryenLiteralFloat32(float x);
struct BinaryenLiteral BinaryenLiteralFloat64(double x);
struct BinaryenLiteral BinaryenLiteralVec128(__const uint8_t x[16]);
struct BinaryenLiteral BinaryenLiteralFloat32Bits(int32_t x);
struct BinaryenLiteral BinaryenLiteralFloat64Bits(int64_t x);

// Expressions
//
// Some expressions have a BinaryenOp, which is the more
// specific operation/opcode.
//
// Some expressions have optional parameters, like Return may not
// return a value. You can supply a ((void*)0) pointer in those cases.
//
// For more information, see wasm.h

typedef int32_t BinaryenOp;

BinaryenOp BinaryenClzInt32(void);
BinaryenOp BinaryenCtzInt32(void);
BinaryenOp BinaryenPopcntInt32(void);
BinaryenOp BinaryenNegFloat32(void);
BinaryenOp BinaryenAbsFloat32(void);
BinaryenOp BinaryenCeilFloat32(void);
BinaryenOp BinaryenFloorFloat32(void);
BinaryenOp BinaryenTruncFloat32(void);
BinaryenOp BinaryenNearestFloat32(void);
BinaryenOp BinaryenSqrtFloat32(void);
BinaryenOp BinaryenEqZInt32(void);
BinaryenOp BinaryenClzInt64(void);
BinaryenOp BinaryenCtzInt64(void);
BinaryenOp BinaryenPopcntInt64(void);
BinaryenOp BinaryenNegFloat64(void);
BinaryenOp BinaryenAbsFloat64(void);
BinaryenOp BinaryenCeilFloat64(void);
BinaryenOp BinaryenFloorFloat64(void);
BinaryenOp BinaryenTruncFloat64(void);
BinaryenOp BinaryenNearestFloat64(void);
BinaryenOp BinaryenSqrtFloat64(void);
BinaryenOp BinaryenEqZInt64(void);
BinaryenOp BinaryenExtendSInt32(void);
BinaryenOp BinaryenExtendUInt32(void);
BinaryenOp BinaryenWrapInt64(void);
BinaryenOp BinaryenTruncSFloat32ToInt32(void);
BinaryenOp BinaryenTruncSFloat32ToInt64(void);
BinaryenOp BinaryenTruncUFloat32ToInt32(void);
BinaryenOp BinaryenTruncUFloat32ToInt64(void);
BinaryenOp BinaryenTruncSFloat64ToInt32(void);
BinaryenOp BinaryenTruncSFloat64ToInt64(void);
BinaryenOp BinaryenTruncUFloat64ToInt32(void);
BinaryenOp BinaryenTruncUFloat64ToInt64(void);
BinaryenOp BinaryenReinterpretFloat32(void);
BinaryenOp BinaryenReinterpretFloat64(void);
BinaryenOp BinaryenConvertSInt32ToFloat32(void);
BinaryenOp BinaryenConvertSInt32ToFloat64(void);
BinaryenOp BinaryenConvertUInt32ToFloat32(void);
BinaryenOp BinaryenConvertUInt32ToFloat64(void);
BinaryenOp BinaryenConvertSInt64ToFloat32(void);
BinaryenOp BinaryenConvertSInt64ToFloat64(void);
BinaryenOp BinaryenConvertUInt64ToFloat32(void);
BinaryenOp BinaryenConvertUInt64ToFloat64(void);
BinaryenOp BinaryenPromoteFloat32(void);
BinaryenOp BinaryenDemoteFloat64(void);
BinaryenOp BinaryenReinterpretInt32(void);
BinaryenOp BinaryenReinterpretInt64(void);
BinaryenOp BinaryenExtendS8Int32(void);
BinaryenOp BinaryenExtendS16Int32(void);
BinaryenOp BinaryenExtendS8Int64(void);
BinaryenOp BinaryenExtendS16Int64(void);
BinaryenOp BinaryenExtendS32Int64(void);
BinaryenOp BinaryenAddInt32(void);
BinaryenOp BinaryenSubInt32(void);
BinaryenOp BinaryenMulInt32(void);
BinaryenOp BinaryenDivSInt32(void);
BinaryenOp BinaryenDivUInt32(void);
BinaryenOp BinaryenRemSInt32(void);
BinaryenOp BinaryenRemUInt32(void);
BinaryenOp BinaryenAndInt32(void);
BinaryenOp BinaryenOrInt32(void);
BinaryenOp BinaryenXorInt32(void);
BinaryenOp BinaryenShlInt32(void);
BinaryenOp BinaryenShrUInt32(void);
BinaryenOp BinaryenShrSInt32(void);
BinaryenOp BinaryenRotLInt32(void);
BinaryenOp BinaryenRotRInt32(void);
BinaryenOp BinaryenEqInt32(void);
BinaryenOp BinaryenNeInt32(void);
BinaryenOp BinaryenLtSInt32(void);
BinaryenOp BinaryenLtUInt32(void);
BinaryenOp BinaryenLeSInt32(void);
BinaryenOp BinaryenLeUInt32(void);
BinaryenOp BinaryenGtSInt32(void);
BinaryenOp BinaryenGtUInt32(void);
BinaryenOp BinaryenGeSInt32(void);
BinaryenOp BinaryenGeUInt32(void);
BinaryenOp BinaryenAddInt64(void);
BinaryenOp BinaryenSubInt64(void);
BinaryenOp BinaryenMulInt64(void);
BinaryenOp BinaryenDivSInt64(void);
BinaryenOp BinaryenDivUInt64(void);
BinaryenOp BinaryenRemSInt64(void);
BinaryenOp BinaryenRemUInt64(void);
BinaryenOp BinaryenAndInt64(void);
BinaryenOp BinaryenOrInt64(void);
BinaryenOp BinaryenXorInt64(void);
BinaryenOp BinaryenShlInt64(void);
BinaryenOp BinaryenShrUInt64(void);
BinaryenOp BinaryenShrSInt64(void);
BinaryenOp BinaryenRotLInt64(void);
BinaryenOp BinaryenRotRInt64(void);
BinaryenOp BinaryenEqInt64(void);
BinaryenOp BinaryenNeInt64(void);
BinaryenOp BinaryenLtSInt64(void);
BinaryenOp BinaryenLtUInt64(void);
BinaryenOp BinaryenLeSInt64(void);
BinaryenOp BinaryenLeUInt64(void);
BinaryenOp BinaryenGtSInt64(void);
BinaryenOp BinaryenGtUInt64(void);
BinaryenOp BinaryenGeSInt64(void);
BinaryenOp BinaryenGeUInt64(void);
BinaryenOp BinaryenAddFloat32(void);
BinaryenOp BinaryenSubFloat32(void);
BinaryenOp BinaryenMulFloat32(void);
BinaryenOp BinaryenDivFloat32(void);
BinaryenOp BinaryenCopySignFloat32(void);
BinaryenOp BinaryenMinFloat32(void);
BinaryenOp BinaryenMaxFloat32(void);
BinaryenOp BinaryenEqFloat32(void);
BinaryenOp BinaryenNeFloat32(void);
BinaryenOp BinaryenLtFloat32(void);
BinaryenOp BinaryenLeFloat32(void);
BinaryenOp BinaryenGtFloat32(void);
BinaryenOp BinaryenGeFloat32(void);
BinaryenOp BinaryenAddFloat64(void);
BinaryenOp BinaryenSubFloat64(void);
BinaryenOp BinaryenMulFloat64(void);
BinaryenOp BinaryenDivFloat64(void);
BinaryenOp BinaryenCopySignFloat64(void);
BinaryenOp BinaryenMinFloat64(void);
BinaryenOp BinaryenMaxFloat64(void);
BinaryenOp BinaryenEqFloat64(void);
BinaryenOp BinaryenNeFloat64(void);
BinaryenOp BinaryenLtFloat64(void);
BinaryenOp BinaryenLeFloat64(void);
BinaryenOp BinaryenGtFloat64(void);
BinaryenOp BinaryenGeFloat64(void);
BinaryenOp BinaryenAtomicRMWAdd(void);
BinaryenOp BinaryenAtomicRMWSub(void);
BinaryenOp BinaryenAtomicRMWAnd(void);
BinaryenOp BinaryenAtomicRMWOr(void);
BinaryenOp BinaryenAtomicRMWXor(void);
BinaryenOp BinaryenAtomicRMWXchg(void);
BinaryenOp BinaryenTruncSatSFloat32ToInt32(void);
BinaryenOp BinaryenTruncSatSFloat32ToInt64(void);
BinaryenOp BinaryenTruncSatUFloat32ToInt32(void);
BinaryenOp BinaryenTruncSatUFloat32ToInt64(void);
BinaryenOp BinaryenTruncSatSFloat64ToInt32(void);
BinaryenOp BinaryenTruncSatSFloat64ToInt64(void);
BinaryenOp BinaryenTruncSatUFloat64ToInt32(void);
BinaryenOp BinaryenTruncSatUFloat64ToInt64(void);
BinaryenOp BinaryenSplatVecI8x16(void);
BinaryenOp BinaryenExtractLaneSVecI8x16(void);
BinaryenOp BinaryenExtractLaneUVecI8x16(void);
BinaryenOp BinaryenReplaceLaneVecI8x16(void);
BinaryenOp BinaryenSplatVecI16x8(void);
BinaryenOp BinaryenExtractLaneSVecI16x8(void);
BinaryenOp BinaryenExtractLaneUVecI16x8(void);
BinaryenOp BinaryenReplaceLaneVecI16x8(void);
BinaryenOp BinaryenSplatVecI32x4(void);
BinaryenOp BinaryenExtractLaneVecI32x4(void);
BinaryenOp BinaryenReplaceLaneVecI32x4(void);
BinaryenOp BinaryenSplatVecI64x2(void);
BinaryenOp BinaryenExtractLaneVecI64x2(void);
BinaryenOp BinaryenReplaceLaneVecI64x2(void);
BinaryenOp BinaryenSplatVecF32x4(void);
BinaryenOp BinaryenExtractLaneVecF32x4(void);
BinaryenOp BinaryenReplaceLaneVecF32x4(void);
BinaryenOp BinaryenSplatVecF64x2(void);
BinaryenOp BinaryenExtractLaneVecF64x2(void);
BinaryenOp BinaryenReplaceLaneVecF64x2(void);
BinaryenOp BinaryenEqVecI8x16(void);
BinaryenOp BinaryenNeVecI8x16(void);
BinaryenOp BinaryenLtSVecI8x16(void);
BinaryenOp BinaryenLtUVecI8x16(void);
BinaryenOp BinaryenGtSVecI8x16(void);
BinaryenOp BinaryenGtUVecI8x16(void);
BinaryenOp BinaryenLeSVecI8x16(void);
BinaryenOp BinaryenLeUVecI8x16(void);
BinaryenOp BinaryenGeSVecI8x16(void);
BinaryenOp BinaryenGeUVecI8x16(void);
BinaryenOp BinaryenEqVecI16x8(void);
BinaryenOp BinaryenNeVecI16x8(void);
BinaryenOp BinaryenLtSVecI16x8(void);
BinaryenOp BinaryenLtUVecI16x8(void);
BinaryenOp BinaryenGtSVecI16x8(void);
BinaryenOp BinaryenGtUVecI16x8(void);
BinaryenOp BinaryenLeSVecI16x8(void);
BinaryenOp BinaryenLeUVecI16x8(void);
BinaryenOp BinaryenGeSVecI16x8(void);
BinaryenOp BinaryenGeUVecI16x8(void);
BinaryenOp BinaryenEqVecI32x4(void);
BinaryenOp BinaryenNeVecI32x4(void);
BinaryenOp BinaryenLtSVecI32x4(void);
BinaryenOp BinaryenLtUVecI32x4(void);
BinaryenOp BinaryenGtSVecI32x4(void);
BinaryenOp BinaryenGtUVecI32x4(void);
BinaryenOp BinaryenLeSVecI32x4(void);
BinaryenOp BinaryenLeUVecI32x4(void);
BinaryenOp BinaryenGeSVecI32x4(void);
BinaryenOp BinaryenGeUVecI32x4(void);
BinaryenOp BinaryenEqVecI64x2(void);
BinaryenOp BinaryenNeVecI64x2(void);
BinaryenOp BinaryenLtSVecI64x2(void);
BinaryenOp BinaryenGtSVecI64x2(void);
BinaryenOp BinaryenLeSVecI64x2(void);
BinaryenOp BinaryenGeSVecI64x2(void);
BinaryenOp BinaryenEqVecF32x4(void);
BinaryenOp BinaryenNeVecF32x4(void);
BinaryenOp BinaryenLtVecF32x4(void);
BinaryenOp BinaryenGtVecF32x4(void);
BinaryenOp BinaryenLeVecF32x4(void);
BinaryenOp BinaryenGeVecF32x4(void);
BinaryenOp BinaryenEqVecF64x2(void);
BinaryenOp BinaryenNeVecF64x2(void);
BinaryenOp BinaryenLtVecF64x2(void);
BinaryenOp BinaryenGtVecF64x2(void);
BinaryenOp BinaryenLeVecF64x2(void);
BinaryenOp BinaryenGeVecF64x2(void);
BinaryenOp BinaryenNotVec128(void);
BinaryenOp BinaryenAndVec128(void);
BinaryenOp BinaryenOrVec128(void);
BinaryenOp BinaryenXorVec128(void);
BinaryenOp BinaryenAndNotVec128(void);
BinaryenOp BinaryenBitselectVec128(void);
BinaryenOp BinaryenRelaxedFmaVecF32x4(void);
BinaryenOp BinaryenRelaxedFmsVecF32x4(void);
BinaryenOp BinaryenRelaxedFmaVecF64x2(void);
BinaryenOp BinaryenRelaxedFmsVecF64x2(void);
BinaryenOp BinaryenLaneselectI8x16(void);
BinaryenOp BinaryenLaneselectI16x8(void);
BinaryenOp BinaryenLaneselectI32x4(void);
BinaryenOp BinaryenLaneselectI64x2(void);
BinaryenOp BinaryenDotI8x16I7x16AddSToVecI32x4(void);
BinaryenOp BinaryenAnyTrueVec128(void);
BinaryenOp BinaryenPopcntVecI8x16(void);
BinaryenOp BinaryenAbsVecI8x16(void);
BinaryenOp BinaryenNegVecI8x16(void);
BinaryenOp BinaryenAllTrueVecI8x16(void);
BinaryenOp BinaryenBitmaskVecI8x16(void);
BinaryenOp BinaryenShlVecI8x16(void);
BinaryenOp BinaryenShrSVecI8x16(void);
BinaryenOp BinaryenShrUVecI8x16(void);
BinaryenOp BinaryenAddVecI8x16(void);
BinaryenOp BinaryenAddSatSVecI8x16(void);
BinaryenOp BinaryenAddSatUVecI8x16(void);
BinaryenOp BinaryenSubVecI8x16(void);
BinaryenOp BinaryenSubSatSVecI8x16(void);
BinaryenOp BinaryenSubSatUVecI8x16(void);
BinaryenOp BinaryenMinSVecI8x16(void);
BinaryenOp BinaryenMinUVecI8x16(void);
BinaryenOp BinaryenMaxSVecI8x16(void);
BinaryenOp BinaryenMaxUVecI8x16(void);
BinaryenOp BinaryenAvgrUVecI8x16(void);
BinaryenOp BinaryenAbsVecI16x8(void);
BinaryenOp BinaryenNegVecI16x8(void);
BinaryenOp BinaryenAllTrueVecI16x8(void);
BinaryenOp BinaryenBitmaskVecI16x8(void);
BinaryenOp BinaryenShlVecI16x8(void);
BinaryenOp BinaryenShrSVecI16x8(void);
BinaryenOp BinaryenShrUVecI16x8(void);
BinaryenOp BinaryenAddVecI16x8(void);
BinaryenOp BinaryenAddSatSVecI16x8(void);
BinaryenOp BinaryenAddSatUVecI16x8(void);
BinaryenOp BinaryenSubVecI16x8(void);
BinaryenOp BinaryenSubSatSVecI16x8(void);
BinaryenOp BinaryenSubSatUVecI16x8(void);
BinaryenOp BinaryenMulVecI16x8(void);
BinaryenOp BinaryenMinSVecI16x8(void);
BinaryenOp BinaryenMinUVecI16x8(void);
BinaryenOp BinaryenMaxSVecI16x8(void);
BinaryenOp BinaryenMaxUVecI16x8(void);
BinaryenOp BinaryenAvgrUVecI16x8(void);
BinaryenOp BinaryenQ15MulrSatSVecI16x8(void);
BinaryenOp BinaryenExtMulLowSVecI16x8(void);
BinaryenOp BinaryenExtMulHighSVecI16x8(void);
BinaryenOp BinaryenExtMulLowUVecI16x8(void);
BinaryenOp BinaryenExtMulHighUVecI16x8(void);
BinaryenOp BinaryenAbsVecI32x4(void);
BinaryenOp BinaryenNegVecI32x4(void);
BinaryenOp BinaryenAllTrueVecI32x4(void);
BinaryenOp BinaryenBitmaskVecI32x4(void);
BinaryenOp BinaryenShlVecI32x4(void);
BinaryenOp BinaryenShrSVecI32x4(void);
BinaryenOp BinaryenShrUVecI32x4(void);
BinaryenOp BinaryenAddVecI32x4(void);
BinaryenOp BinaryenSubVecI32x4(void);
BinaryenOp BinaryenMulVecI32x4(void);
BinaryenOp BinaryenMinSVecI32x4(void);
BinaryenOp BinaryenMinUVecI32x4(void);
BinaryenOp BinaryenMaxSVecI32x4(void);
BinaryenOp BinaryenMaxUVecI32x4(void);
BinaryenOp BinaryenDotSVecI16x8ToVecI32x4(void);
BinaryenOp BinaryenExtMulLowSVecI32x4(void);
BinaryenOp BinaryenExtMulHighSVecI32x4(void);
BinaryenOp BinaryenExtMulLowUVecI32x4(void);
BinaryenOp BinaryenExtMulHighUVecI32x4(void);
BinaryenOp BinaryenAbsVecI64x2(void);
BinaryenOp BinaryenNegVecI64x2(void);
BinaryenOp BinaryenAllTrueVecI64x2(void);
BinaryenOp BinaryenBitmaskVecI64x2(void);
BinaryenOp BinaryenShlVecI64x2(void);
BinaryenOp BinaryenShrSVecI64x2(void);
BinaryenOp BinaryenShrUVecI64x2(void);
BinaryenOp BinaryenAddVecI64x2(void);
BinaryenOp BinaryenSubVecI64x2(void);
BinaryenOp BinaryenMulVecI64x2(void);
BinaryenOp BinaryenExtMulLowSVecI64x2(void);
BinaryenOp BinaryenExtMulHighSVecI64x2(void);
BinaryenOp BinaryenExtMulLowUVecI64x2(void);
BinaryenOp BinaryenExtMulHighUVecI64x2(void);
BinaryenOp BinaryenAbsVecF32x4(void);
BinaryenOp BinaryenNegVecF32x4(void);
BinaryenOp BinaryenSqrtVecF32x4(void);
BinaryenOp BinaryenAddVecF32x4(void);
BinaryenOp BinaryenSubVecF32x4(void);
BinaryenOp BinaryenMulVecF32x4(void);
BinaryenOp BinaryenDivVecF32x4(void);
BinaryenOp BinaryenMinVecF32x4(void);
BinaryenOp BinaryenMaxVecF32x4(void);
BinaryenOp BinaryenPMinVecF32x4(void);
BinaryenOp BinaryenPMaxVecF32x4(void);
BinaryenOp BinaryenCeilVecF32x4(void);
BinaryenOp BinaryenFloorVecF32x4(void);
BinaryenOp BinaryenTruncVecF32x4(void);
BinaryenOp BinaryenNearestVecF32x4(void);
BinaryenOp BinaryenAbsVecF64x2(void);
BinaryenOp BinaryenNegVecF64x2(void);
BinaryenOp BinaryenSqrtVecF64x2(void);
BinaryenOp BinaryenAddVecF64x2(void);
BinaryenOp BinaryenSubVecF64x2(void);
BinaryenOp BinaryenMulVecF64x2(void);
BinaryenOp BinaryenDivVecF64x2(void);
BinaryenOp BinaryenMinVecF64x2(void);
BinaryenOp BinaryenMaxVecF64x2(void);
BinaryenOp BinaryenPMinVecF64x2(void);
BinaryenOp BinaryenPMaxVecF64x2(void);
BinaryenOp BinaryenCeilVecF64x2(void);
BinaryenOp BinaryenFloorVecF64x2(void);
BinaryenOp BinaryenTruncVecF64x2(void);
BinaryenOp BinaryenNearestVecF64x2(void);
BinaryenOp BinaryenExtAddPairwiseSVecI8x16ToI16x8(void);
BinaryenOp BinaryenExtAddPairwiseUVecI8x16ToI16x8(void);
BinaryenOp BinaryenExtAddPairwiseSVecI16x8ToI32x4(void);
BinaryenOp BinaryenExtAddPairwiseUVecI16x8ToI32x4(void);
BinaryenOp BinaryenTruncSatSVecF32x4ToVecI32x4(void);
BinaryenOp BinaryenTruncSatUVecF32x4ToVecI32x4(void);
BinaryenOp BinaryenConvertSVecI32x4ToVecF32x4(void);
BinaryenOp BinaryenConvertUVecI32x4ToVecF32x4(void);
BinaryenOp BinaryenLoad8SplatVec128(void);
BinaryenOp BinaryenLoad16SplatVec128(void);
BinaryenOp BinaryenLoad32SplatVec128(void);
BinaryenOp BinaryenLoad64SplatVec128(void);
BinaryenOp BinaryenLoad8x8SVec128(void);
BinaryenOp BinaryenLoad8x8UVec128(void);
BinaryenOp BinaryenLoad16x4SVec128(void);
BinaryenOp BinaryenLoad16x4UVec128(void);
BinaryenOp BinaryenLoad32x2SVec128(void);
BinaryenOp BinaryenLoad32x2UVec128(void);
BinaryenOp BinaryenLoad32ZeroVec128(void);
BinaryenOp BinaryenLoad64ZeroVec128(void);
BinaryenOp BinaryenLoad8LaneVec128(void);
BinaryenOp BinaryenLoad16LaneVec128(void);
BinaryenOp BinaryenLoad32LaneVec128(void);
BinaryenOp BinaryenLoad64LaneVec128(void);
BinaryenOp BinaryenStore8LaneVec128(void);
BinaryenOp BinaryenStore16LaneVec128(void);
BinaryenOp BinaryenStore32LaneVec128(void);
BinaryenOp BinaryenStore64LaneVec128(void);
BinaryenOp BinaryenNarrowSVecI16x8ToVecI8x16(void);
BinaryenOp BinaryenNarrowUVecI16x8ToVecI8x16(void);
BinaryenOp BinaryenNarrowSVecI32x4ToVecI16x8(void);
BinaryenOp BinaryenNarrowUVecI32x4ToVecI16x8(void);
BinaryenOp BinaryenExtendLowSVecI8x16ToVecI16x8(void);
BinaryenOp BinaryenExtendHighSVecI8x16ToVecI16x8(void);
BinaryenOp BinaryenExtendLowUVecI8x16ToVecI16x8(void);
BinaryenOp BinaryenExtendHighUVecI8x16ToVecI16x8(void);
BinaryenOp BinaryenExtendLowSVecI16x8ToVecI32x4(void);
BinaryenOp BinaryenExtendHighSVecI16x8ToVecI32x4(void);
BinaryenOp BinaryenExtendLowUVecI16x8ToVecI32x4(void);
BinaryenOp BinaryenExtendHighUVecI16x8ToVecI32x4(void);
BinaryenOp BinaryenExtendLowSVecI32x4ToVecI64x2(void);
BinaryenOp BinaryenExtendHighSVecI32x4ToVecI64x2(void);
BinaryenOp BinaryenExtendLowUVecI32x4ToVecI64x2(void);
BinaryenOp BinaryenExtendHighUVecI32x4ToVecI64x2(void);
BinaryenOp BinaryenConvertLowSVecI32x4ToVecF64x2(void);
BinaryenOp BinaryenConvertLowUVecI32x4ToVecF64x2(void);
BinaryenOp BinaryenTruncSatZeroSVecF64x2ToVecI32x4(void);
BinaryenOp BinaryenTruncSatZeroUVecF64x2ToVecI32x4(void);
BinaryenOp BinaryenDemoteZeroVecF64x2ToVecF32x4(void);
BinaryenOp BinaryenPromoteLowVecF32x4ToVecF64x2(void);
BinaryenOp BinaryenRelaxedTruncSVecF32x4ToVecI32x4(void);
BinaryenOp BinaryenRelaxedTruncUVecF32x4ToVecI32x4(void);
BinaryenOp BinaryenRelaxedTruncZeroSVecF64x2ToVecI32x4(void);
BinaryenOp BinaryenRelaxedTruncZeroUVecF64x2ToVecI32x4(void);
BinaryenOp BinaryenSwizzleVecI8x16(void);
BinaryenOp BinaryenRelaxedSwizzleVecI8x16(void);
BinaryenOp BinaryenRelaxedMinVecF32x4(void);
BinaryenOp BinaryenRelaxedMaxVecF32x4(void);
BinaryenOp BinaryenRelaxedMinVecF64x2(void);
BinaryenOp BinaryenRelaxedMaxVecF64x2(void);
BinaryenOp BinaryenRelaxedQ15MulrSVecI16x8(void);
BinaryenOp BinaryenDotI8x16I7x16SToVecI16x8(void);
BinaryenOp BinaryenRefAsNonNull(void);
BinaryenOp BinaryenRefAsExternInternalize(void);
BinaryenOp BinaryenRefAsExternExternalize(void);
BinaryenOp BinaryenBrOnNull(void);
BinaryenOp BinaryenBrOnNonNull(void);
BinaryenOp BinaryenBrOnCast(void);
BinaryenOp BinaryenBrOnCastFail(void);
BinaryenOp BinaryenStringNewUTF8(void);
BinaryenOp BinaryenStringNewWTF8(void);
BinaryenOp BinaryenStringNewLossyUTF8(void);
BinaryenOp BinaryenStringNewWTF16(void);
BinaryenOp BinaryenStringNewUTF8Array(void);
BinaryenOp BinaryenStringNewWTF8Array(void);
BinaryenOp BinaryenStringNewLossyUTF8Array(void);
BinaryenOp BinaryenStringNewWTF16Array(void);
BinaryenOp BinaryenStringNewFromCodePoint(void);
BinaryenOp BinaryenStringMeasureUTF8(void);
BinaryenOp BinaryenStringMeasureWTF8(void);
BinaryenOp BinaryenStringMeasureWTF16(void);
BinaryenOp BinaryenStringMeasureIsUSV(void);
BinaryenOp BinaryenStringMeasureWTF16View(void);
BinaryenOp BinaryenStringEncodeUTF8(void);
BinaryenOp BinaryenStringEncodeLossyUTF8(void);
BinaryenOp BinaryenStringEncodeWTF8(void);
BinaryenOp BinaryenStringEncodeWTF16(void);
BinaryenOp BinaryenStringEncodeUTF8Array(void);
BinaryenOp BinaryenStringEncodeLossyUTF8Array(void);
BinaryenOp BinaryenStringEncodeWTF8Array(void);
BinaryenOp BinaryenStringEncodeWTF16Array(void);
BinaryenOp BinaryenStringAsWTF8(void);
BinaryenOp BinaryenStringAsWTF16(void);
BinaryenOp BinaryenStringAsIter(void);
BinaryenOp BinaryenStringIterMoveAdvance(void);
BinaryenOp BinaryenStringIterMoveRewind(void);
BinaryenOp BinaryenStringSliceWTF8(void);
BinaryenOp BinaryenStringSliceWTF16(void);
BinaryenOp BinaryenStringEqEqual(void);
BinaryenOp BinaryenStringEqCompare(void);

typedef struct Binaryen##Expression *Binaryen##Expression##Ref;
;

// Block: name can be ((void*)0). Specifying BinaryenUndefined() as the 'type'
//        parameter indicates that the block's type shall be figured out
//        automatically instead of explicitly providing it. This conforms
//        to the behavior before the 'type' parameter has been introduced.
BinaryenExpressionRef
BinaryenBlock(BinaryenModuleRef module, __const char *name, BinaryenExpressionRef *children, BinaryenIndex numChildren, BinaryenType type);
// If: ifFalse can be ((void*)0)
BinaryenExpressionRef BinaryenIf(BinaryenModuleRef module, BinaryenExpressionRef condition, BinaryenExpressionRef ifTrue, BinaryenExpressionRef ifFalse);
BinaryenExpressionRef BinaryenLoop(BinaryenModuleRef module, __const char *in, BinaryenExpressionRef body);
// Break: value and condition can be ((void*)0)
BinaryenExpressionRef
BinaryenBreak(BinaryenModuleRef module, __const char *name, BinaryenExpressionRef condition, BinaryenExpressionRef value);
// Switch: value can be ((void*)0)
BinaryenExpressionRef
BinaryenSwitch(BinaryenModuleRef module, __const char **names, BinaryenIndex numNames, __const char *defaultName, BinaryenExpressionRef condition, BinaryenExpressionRef value);
// Call: Note the 'returnType' parameter. You must declare the
//       type returned by the function being called, as that
//       function might not have been created yet, so we don't
//       know what it is.
BinaryenExpressionRef BinaryenCall(BinaryenModuleRef module, __const char *target, BinaryenExpressionRef *operands, BinaryenIndex numOperands, BinaryenType returnType);
BinaryenExpressionRef
BinaryenCallIndirect(BinaryenModuleRef module, __const char *table, BinaryenExpressionRef target, BinaryenExpressionRef *operands, BinaryenIndex numOperands, BinaryenType params, BinaryenType results);
BinaryenExpressionRef
BinaryenReturnCall(BinaryenModuleRef module, __const char *target, BinaryenExpressionRef *operands, BinaryenIndex numOperands, BinaryenType returnType);
BinaryenExpressionRef
BinaryenReturnCallIndirect(BinaryenModuleRef module, __const char *table, BinaryenExpressionRef target, BinaryenExpressionRef *operands, BinaryenIndex numOperands, BinaryenType params, BinaryenType results);

// LocalGet: Note the 'type' parameter. It might seem redundant, since the
//           local at that index must have a type. However, this API lets you
//           build code "top-down": create a node, then its parents, and so
//           on, and finally create the function at the end. (Note that in fact
//           you do not mention a function when creating ExpressionRefs, only
//           a module.) And since LocalGet is a leaf node, we need to be told
//           its type. (Other nodes detect their type either from their
//           type or their opcode, or failing that, their children. But
//           LocalGet has no children, it is where a "stream" of type info
//           begins.)
//           Note also that the index of a local can refer to a param or
//           a var, that is, either a parameter to the function or a variable
//           declared when you call BinaryenAddFunction. See BinaryenAddFunction
//           for more details.
BinaryenExpressionRef BinaryenLocalGet(BinaryenModuleRef module, BinaryenIndex index, BinaryenType type);
BinaryenExpressionRef BinaryenLocalSet(
    BinaryenModuleRef module, BinaryenIndex index, BinaryenExpressionRef value
);
BinaryenExpressionRef BinaryenLocalTee(BinaryenModuleRef module, BinaryenIndex index, BinaryenExpressionRef value, BinaryenType type);
BinaryenExpressionRef BinaryenGlobalGet(BinaryenModuleRef module, __const char *name, BinaryenType type);
BinaryenExpressionRef BinaryenGlobalSet(
    BinaryenModuleRef module, __const char *name, BinaryenExpressionRef value
);
// Load: align can be 0, in which case it will be the natural alignment (equal
// to bytes)
BinaryenExpressionRef BinaryenLoad(BinaryenModuleRef module, uint32_t bytes, _Bool signed_, uint32_t offset, uint32_t align, BinaryenType type, BinaryenExpressionRef ptr, __const char *memoryName);
// Store: align can be 0, in which case it will be the natural alignment (equal
// to bytes)
BinaryenExpressionRef BinaryenStore(BinaryenModuleRef module, uint32_t bytes, uint32_t offset, uint32_t align, BinaryenExpressionRef ptr, BinaryenExpressionRef value, BinaryenType type, __const char *memoryName);
BinaryenExpressionRef BinaryenConst(BinaryenModuleRef module, struct BinaryenLiteral value);
BinaryenExpressionRef BinaryenUnary(BinaryenModuleRef module, BinaryenOp op, BinaryenExpressionRef value);
BinaryenExpressionRef BinaryenBinary(BinaryenModuleRef module, BinaryenOp op, BinaryenExpressionRef left, BinaryenExpressionRef right);
BinaryenExpressionRef
BinaryenSelect(BinaryenModuleRef module, BinaryenExpressionRef condition, BinaryenExpressionRef ifTrue, BinaryenExpressionRef ifFalse, BinaryenType type);
BinaryenExpressionRef BinaryenDrop(BinaryenModuleRef module, BinaryenExpressionRef value);
// Return: value can be ((void*)0)
BinaryenExpressionRef BinaryenReturn(BinaryenModuleRef module, BinaryenExpressionRef value);
BinaryenExpressionRef BinaryenMemorySize(BinaryenModuleRef module, __const char *memoryName, _Bool memoryIs64);
BinaryenExpressionRef
BinaryenMemoryGrow(BinaryenModuleRef module, BinaryenExpressionRef delta, __const char *memoryName, _Bool memoryIs64);
BinaryenExpressionRef BinaryenNop(BinaryenModuleRef module);
BinaryenExpressionRef
BinaryenUnreachable(BinaryenModuleRef module);
BinaryenExpressionRef BinaryenAtomicLoad(BinaryenModuleRef module, uint32_t bytes, uint32_t offset, BinaryenType type, BinaryenExpressionRef ptr, __const char *memoryName);
BinaryenExpressionRef
BinaryenAtomicStore(BinaryenModuleRef module, uint32_t bytes, uint32_t offset, BinaryenExpressionRef ptr, BinaryenExpressionRef value, BinaryenType type, __const char *memoryName);
BinaryenExpressionRef
BinaryenAtomicRMW(BinaryenModuleRef module, BinaryenOp op, BinaryenIndex bytes, BinaryenIndex offset, BinaryenExpressionRef ptr, BinaryenExpressionRef value, BinaryenType type, __const char *memoryName);
BinaryenExpressionRef
BinaryenAtomicCmpxchg(BinaryenModuleRef module, BinaryenIndex bytes, BinaryenIndex offset, BinaryenExpressionRef ptr, BinaryenExpressionRef expected, BinaryenExpressionRef replacement, BinaryenType type, __const char *memoryName);
BinaryenExpressionRef
BinaryenAtomicWait(BinaryenModuleRef module, BinaryenExpressionRef ptr, BinaryenExpressionRef expected, BinaryenExpressionRef timeout, BinaryenType type, __const char *memoryName);
BinaryenExpressionRef
BinaryenAtomicNotify(BinaryenModuleRef module, BinaryenExpressionRef ptr, BinaryenExpressionRef notifyCount, __const char *memoryName);
BinaryenExpressionRef
BinaryenAtomicFence(BinaryenModuleRef module);
BinaryenExpressionRef
BinaryenSIMDExtract(BinaryenModuleRef module, BinaryenOp op, BinaryenExpressionRef vec, uint8_t index);
BinaryenExpressionRef
BinaryenSIMDReplace(BinaryenModuleRef module, BinaryenOp op, BinaryenExpressionRef vec, uint8_t index, BinaryenExpressionRef value);
BinaryenExpressionRef
BinaryenSIMDShuffle(BinaryenModuleRef module, BinaryenExpressionRef left, BinaryenExpressionRef right, __const uint8_t mask[16]);
BinaryenExpressionRef BinaryenSIMDTernary(BinaryenModuleRef module, BinaryenOp op, BinaryenExpressionRef a, BinaryenExpressionRef b, BinaryenExpressionRef c);
BinaryenExpressionRef
BinaryenSIMDShift(BinaryenModuleRef module, BinaryenOp op, BinaryenExpressionRef vec, BinaryenExpressionRef shift);
BinaryenExpressionRef BinaryenSIMDLoad(BinaryenModuleRef module, BinaryenOp op, uint32_t offset, uint32_t align, BinaryenExpressionRef ptr, __const char *name);
BinaryenExpressionRef
BinaryenSIMDLoadStoreLane(BinaryenModuleRef module, BinaryenOp op, uint32_t offset, uint32_t align, uint8_t index, BinaryenExpressionRef ptr, BinaryenExpressionRef vec, __const char *memoryName);
BinaryenExpressionRef
BinaryenMemoryInit(BinaryenModuleRef module, __const char *segment, BinaryenExpressionRef dest, BinaryenExpressionRef offset, BinaryenExpressionRef size, __const char *memoryName);
BinaryenExpressionRef BinaryenDataDrop(BinaryenModuleRef module, __const char *segment);
BinaryenExpressionRef
BinaryenMemoryCopy(BinaryenModuleRef module, BinaryenExpressionRef dest, BinaryenExpressionRef source, BinaryenExpressionRef size, __const char *destMemory, __const char *sourceMemory);
BinaryenExpressionRef
BinaryenMemoryFill(BinaryenModuleRef module, BinaryenExpressionRef dest, BinaryenExpressionRef value, BinaryenExpressionRef size, __const char *memoryName);
BinaryenExpressionRef BinaryenRefNull(BinaryenModuleRef module, BinaryenType type);
BinaryenExpressionRef
BinaryenRefIsNull(BinaryenModuleRef module, BinaryenExpressionRef value);
BinaryenExpressionRef BinaryenRefAs(BinaryenModuleRef module, BinaryenOp op, BinaryenExpressionRef value);
BinaryenExpressionRef BinaryenRefFunc(BinaryenModuleRef module, __const char *func, BinaryenType type);
BinaryenExpressionRef BinaryenRefEq(BinaryenModuleRef module, BinaryenExpressionRef left, BinaryenExpressionRef right);
BinaryenExpressionRef BinaryenTableGet(BinaryenModuleRef module, __const char *name, BinaryenExpressionRef index, BinaryenType type);
BinaryenExpressionRef
BinaryenTableSet(BinaryenModuleRef module, __const char *name, BinaryenExpressionRef index, BinaryenExpressionRef value);
BinaryenExpressionRef BinaryenTableSize(BinaryenModuleRef module, __const char *name);
BinaryenExpressionRef
BinaryenTableGrow(BinaryenModuleRef module, __const char *name, BinaryenExpressionRef value, BinaryenExpressionRef delta);
// Try: name can be ((void*)0). delegateTarget should be ((void*)0) in try-catch.
BinaryenExpressionRef
BinaryenTry(BinaryenModuleRef module, __const char *name, BinaryenExpressionRef body, __const char **catchTags, BinaryenIndex numCatchTags, BinaryenExpressionRef *catchBodies, BinaryenIndex numCatchBodies, __const char *delegateTarget);
BinaryenExpressionRef
BinaryenThrow(BinaryenModuleRef module, __const char *tag, BinaryenExpressionRef *operands, BinaryenIndex numOperands);
BinaryenExpressionRef BinaryenRethrow(BinaryenModuleRef module, __const char *target);
BinaryenExpressionRef
BinaryenTupleMake(BinaryenModuleRef module, BinaryenExpressionRef *operands, BinaryenIndex numOperands);
BinaryenExpressionRef BinaryenTupleExtract(
    BinaryenModuleRef module, BinaryenExpressionRef tuple, BinaryenIndex index
);
BinaryenExpressionRef BinaryenPop(BinaryenModuleRef module, BinaryenType type);
BinaryenExpressionRef BinaryenI31New(BinaryenModuleRef module, BinaryenExpressionRef value);
BinaryenExpressionRef BinaryenI31Get(BinaryenModuleRef module, BinaryenExpressionRef i31, _Bool signed_);
BinaryenExpressionRef
BinaryenCallRef(BinaryenModuleRef module, BinaryenExpressionRef target, BinaryenExpressionRef *operands, BinaryenIndex numOperands, BinaryenType type, _Bool isReturn);
BinaryenExpressionRef BinaryenRefTest(BinaryenModuleRef module, BinaryenExpressionRef ref, BinaryenType castType);
BinaryenExpressionRef BinaryenRefCast(BinaryenModuleRef module, BinaryenExpressionRef ref, BinaryenType type);
BinaryenExpressionRef BinaryenBrOn(BinaryenModuleRef module, BinaryenOp op, __const char *name, BinaryenExpressionRef ref, BinaryenType castType);
BinaryenExpressionRef
BinaryenStructNew(BinaryenModuleRef module, BinaryenExpressionRef *operands, BinaryenIndex numOperands, BinaryenHeapType type);
BinaryenExpressionRef BinaryenStructGet(BinaryenModuleRef module, BinaryenIndex index, BinaryenExpressionRef ref, BinaryenType type, _Bool signed_);
BinaryenExpressionRef
BinaryenStructSet(BinaryenModuleRef module, BinaryenIndex index, BinaryenExpressionRef ref, BinaryenExpressionRef value);
BinaryenExpressionRef BinaryenArrayNew(BinaryenModuleRef module, BinaryenHeapType type, BinaryenExpressionRef size, BinaryenExpressionRef init);

// TODO: BinaryenArrayNewSeg

BinaryenExpressionRef
BinaryenArrayNewFixed(BinaryenModuleRef module, BinaryenHeapType type, BinaryenExpressionRef *values, BinaryenIndex numValues);
BinaryenExpressionRef BinaryenArrayGet(BinaryenModuleRef module, BinaryenExpressionRef ref, BinaryenExpressionRef index, BinaryenType type, _Bool signed_);
BinaryenExpressionRef
BinaryenArraySet(BinaryenModuleRef module, BinaryenExpressionRef ref, BinaryenExpressionRef index, BinaryenExpressionRef value);
BinaryenExpressionRef BinaryenArrayLen(BinaryenModuleRef module, BinaryenExpressionRef ref);
BinaryenExpressionRef
BinaryenArrayCopy(BinaryenModuleRef module, BinaryenExpressionRef destRef, BinaryenExpressionRef destIndex, BinaryenExpressionRef srcRef, BinaryenExpressionRef srcIndex, BinaryenExpressionRef length);
BinaryenExpressionRef
BinaryenStringNew(BinaryenModuleRef module, BinaryenOp op, BinaryenExpressionRef ptr, BinaryenExpressionRef length, BinaryenExpressionRef start, BinaryenExpressionRef end, _Bool try_);
BinaryenExpressionRef BinaryenStringConst(BinaryenModuleRef module, __const char *name);
BinaryenExpressionRef BinaryenStringMeasure(
    BinaryenModuleRef module, BinaryenOp op, BinaryenExpressionRef ref
);
BinaryenExpressionRef
BinaryenStringEncode(BinaryenModuleRef module, BinaryenOp op, BinaryenExpressionRef ref, BinaryenExpressionRef ptr, BinaryenExpressionRef start);
BinaryenExpressionRef
BinaryenStringConcat(BinaryenModuleRef module, BinaryenExpressionRef left, BinaryenExpressionRef right);
BinaryenExpressionRef
BinaryenStringEq(BinaryenModuleRef module, BinaryenOp op, BinaryenExpressionRef left, BinaryenExpressionRef right);
BinaryenExpressionRef BinaryenStringAs(BinaryenModuleRef module, BinaryenOp op, BinaryenExpressionRef ref);
BinaryenExpressionRef
BinaryenStringWTF8Advance(BinaryenModuleRef module, BinaryenExpressionRef ref, BinaryenExpressionRef pos, BinaryenExpressionRef bytes);
BinaryenExpressionRef
BinaryenStringWTF16Get(BinaryenModuleRef module, BinaryenExpressionRef ref, BinaryenExpressionRef pos);
BinaryenExpressionRef
BinaryenStringIterNext(BinaryenModuleRef module, BinaryenExpressionRef ref);
BinaryenExpressionRef
BinaryenStringIterMove(BinaryenModuleRef module, BinaryenOp op, BinaryenExpressionRef ref, BinaryenExpressionRef num);
BinaryenExpressionRef
BinaryenStringSliceWTF(BinaryenModuleRef module, BinaryenOp op, BinaryenExpressionRef ref, BinaryenExpressionRef start, BinaryenExpressionRef end);
BinaryenExpressionRef
BinaryenStringSliceIter(BinaryenModuleRef module, BinaryenExpressionRef ref, BinaryenExpressionRef num);

// Expression

// Gets the id (kind) of the given expression.
BinaryenExpressionId
BinaryenExpressionGetId(BinaryenExpressionRef expr);
// Gets the type of the given expression.
BinaryenType BinaryenExpressionGetType(BinaryenExpressionRef expr);
// Sets the type of the given expression.
void BinaryenExpressionSetType(BinaryenExpressionRef expr, BinaryenType type);
// Prints text format of the given expression to stdout.
void BinaryenExpressionPrint(BinaryenExpressionRef expr);
// Re-finalizes an expression after it has been modified.
void BinaryenExpressionFinalize(BinaryenExpressionRef expr);
// Makes a deep copy of the given expression.
BinaryenExpressionRef
BinaryenExpressionCopy(BinaryenExpressionRef expr, BinaryenModuleRef module);

// Block

// Gets the name (label) of a `block` expression.
__const char *BinaryenBlockGetName(BinaryenExpressionRef expr);
// Sets the name (label) of a `block` expression.
void BinaryenBlockSetName(BinaryenExpressionRef expr, __const char *name);
// Gets the number of child expressions of a `block` expression.
BinaryenIndex
BinaryenBlockGetNumChildren(BinaryenExpressionRef expr);
// Gets the child expression at the specified index of a `block` expression.
BinaryenExpressionRef
BinaryenBlockGetChildAt(BinaryenExpressionRef expr, BinaryenIndex index);
// Sets (replaces) the child expression at the specified index of a `block`
// expression.
void BinaryenBlockSetChildAt(BinaryenExpressionRef expr, BinaryenIndex index, BinaryenExpressionRef childExpr);
// Appends a child expression to a `block` expression, returning its insertion
// index.
BinaryenIndex BinaryenBlockAppendChild(
    BinaryenExpressionRef expr, BinaryenExpressionRef childExpr
);
// Inserts a child expression at the specified index of a `block` expression,
// moving existing children including the one previously at that index one index
// up.
void BinaryenBlockInsertChildAt(BinaryenExpressionRef expr, BinaryenIndex index, BinaryenExpressionRef childExpr);
// Removes the child expression at the specified index of a `block` expression,
// moving all subsequent children one index down. Returns the child expression.
BinaryenExpressionRef
BinaryenBlockRemoveChildAt(BinaryenExpressionRef expr, BinaryenIndex index);

// If

// Gets the condition expression of an `if` expression.
BinaryenExpressionRef
BinaryenIfGetCondition(BinaryenExpressionRef expr);
// Sets the condition expression of an `if` expression.
void BinaryenIfSetCondition(BinaryenExpressionRef expr, BinaryenExpressionRef condExpr);
// Gets the ifTrue (then) expression of an `if` expression.
BinaryenExpressionRef
BinaryenIfGetIfTrue(BinaryenExpressionRef expr);
// Sets the ifTrue (then) expression of an `if` expression.
void BinaryenIfSetIfTrue(BinaryenExpressionRef expr, BinaryenExpressionRef ifTrueExpr);
// Gets the ifFalse (else) expression, if any, of an `if` expression.
BinaryenExpressionRef
BinaryenIfGetIfFalse(BinaryenExpressionRef expr);
// Sets the ifFalse (else) expression, if any, of an `if` expression.
void BinaryenIfSetIfFalse(BinaryenExpressionRef expr, BinaryenExpressionRef ifFalseExpr);

// Loop

// Gets the name (label) of a `loop` expression.
__const char *BinaryenLoopGetName(BinaryenExpressionRef expr);
// Sets the name (label) of a `loop` expression.
void BinaryenLoopSetName(BinaryenExpressionRef expr, __const char *name);
// Gets the body expression of a `loop` expression.
BinaryenExpressionRef
BinaryenLoopGetBody(BinaryenExpressionRef expr);
// Sets the body expression of a `loop` expression.
void BinaryenLoopSetBody(BinaryenExpressionRef expr, BinaryenExpressionRef bodyExpr);

// Break

// Gets the name (target label) of a `br` or `br_if` expression.
__const char *BinaryenBreakGetName(BinaryenExpressionRef expr);
// Sets the name (target label) of a `br` or `br_if` expression.
void BinaryenBreakSetName(BinaryenExpressionRef expr, __const char *name);
// Gets the condition expression, if any, of a `br_if` expression. No condition
// indicates a `br` expression.
BinaryenExpressionRef
BinaryenBreakGetCondition(BinaryenExpressionRef expr);
// Sets the condition expression, if any, of a `br_if` expression. No condition
// makes it a `br` expression.
void BinaryenBreakSetCondition(BinaryenExpressionRef expr, BinaryenExpressionRef condExpr);
// Gets the value expression, if any, of a `br` or `br_if` expression.
BinaryenExpressionRef
BinaryenBreakGetValue(BinaryenExpressionRef expr);
// Sets the value expression, if any, of a `br` or `br_if` expression.
void BinaryenBreakSetValue(BinaryenExpressionRef expr, BinaryenExpressionRef valueExpr);

// Switch

// Gets the number of names (target labels) of a `br_table` expression.
BinaryenIndex
BinaryenSwitchGetNumNames(BinaryenExpressionRef expr);
// Gets the name (target label) at the specified index of a `br_table`
// expression.
__const char *BinaryenSwitchGetNameAt(BinaryenExpressionRef expr, BinaryenIndex index);
// Sets the name (target label) at the specified index of a `br_table`
// expression.
void BinaryenSwitchSetNameAt(BinaryenExpressionRef expr, BinaryenIndex index, __const char *name);
// Appends a name to a `br_table` expression, returning its insertion index.
BinaryenIndex BinaryenSwitchAppendName(BinaryenExpressionRef expr, __const char *name);
// Inserts a name at the specified index of a `br_table` expression, moving
// existing names including the one previously at that index one index up.
void BinaryenSwitchInsertNameAt(BinaryenExpressionRef expr, BinaryenIndex index, __const char *name);
// Removes the name at the specified index of a `br_table` expression, moving
// all subsequent names one index down. Returns the name.
__const char *BinaryenSwitchRemoveNameAt(BinaryenExpressionRef expr, BinaryenIndex index);
// Gets the default name (target label), if any, of a `br_table` expression.
__const char *
BinaryenSwitchGetDefaultName(BinaryenExpressionRef expr);
// Sets the default name (target label), if any, of a `br_table` expression.
void BinaryenSwitchSetDefaultName(BinaryenExpressionRef expr, __const char *name);
// Gets the condition expression of a `br_table` expression.
BinaryenExpressionRef
BinaryenSwitchGetCondition(BinaryenExpressionRef expr);
// Sets the condition expression of a `br_table` expression.
void BinaryenSwitchSetCondition(BinaryenExpressionRef expr, BinaryenExpressionRef condExpr);
// Gets the value expression, if any, of a `br_table` expression.
BinaryenExpressionRef
BinaryenSwitchGetValue(BinaryenExpressionRef expr);
// Sets the value expression, if any, of a `br_table` expression.
void BinaryenSwitchSetValue(BinaryenExpressionRef expr, BinaryenExpressionRef valueExpr);

// Call

// Gets the target function name of a `call` expression.
__const char *BinaryenCallGetTarget(BinaryenExpressionRef expr);
// Sets the target function name of a `call` expression.
void BinaryenCallSetTarget(BinaryenExpressionRef expr, __const char *target);
// Gets the number of operands of a `call` expression.
BinaryenIndex
BinaryenCallGetNumOperands(BinaryenExpressionRef expr);
// Gets the operand expression at the specified index of a `call` expression.
BinaryenExpressionRef
BinaryenCallGetOperandAt(BinaryenExpressionRef expr, BinaryenIndex index);
// Sets the operand expression at the specified index of a `call` expression.
void BinaryenCallSetOperandAt(BinaryenExpressionRef expr, BinaryenIndex index, BinaryenExpressionRef operandExpr);
// Appends an operand expression to a `call` expression, returning its insertion
// index.
BinaryenIndex BinaryenCallAppendOperand(
    BinaryenExpressionRef expr, BinaryenExpressionRef operandExpr
);
// Inserts an operand expression at the specified index of a `call` expression,
// moving existing operands including the one previously at that index one index
// up.
void BinaryenCallInsertOperandAt(BinaryenExpressionRef expr, BinaryenIndex index, BinaryenExpressionRef operandExpr);
// Removes the operand expression at the specified index of a `call` expression,
// moving all subsequent operands one index down. Returns the operand
// expression.
BinaryenExpressionRef
BinaryenCallRemoveOperandAt(BinaryenExpressionRef expr, BinaryenIndex index);
// Gets whether the specified `call` expression is a tail call.
_Bool BinaryenCallIsReturn(BinaryenExpressionRef expr);
// Sets whether the specified `call` expression is a tail call.
void BinaryenCallSetReturn(BinaryenExpressionRef expr, _Bool isReturn);

// CallIndirect

// Gets the target expression of a `call_indirect` expression.
BinaryenExpressionRef
BinaryenCallIndirectGetTarget(BinaryenExpressionRef expr);
// Sets the target expression of a `call_indirect` expression.
void BinaryenCallIndirectSetTarget(BinaryenExpressionRef expr, BinaryenExpressionRef targetExpr);
// Gets the table name of a `call_indirect` expression.
__const char *
BinaryenCallIndirectGetTable(BinaryenExpressionRef expr);
// Sets the table name of a `call_indirect` expression.
void BinaryenCallIndirectSetTable(BinaryenExpressionRef expr, __const char *table);
// Gets the number of operands of a `call_indirect` expression.
BinaryenIndex
BinaryenCallIndirectGetNumOperands(BinaryenExpressionRef expr);
// Gets the operand expression at the specified index of a `call_indirect`
// expression.
BinaryenExpressionRef BinaryenCallIndirectGetOperandAt(
    BinaryenExpressionRef expr, BinaryenIndex index
);
// Sets the operand expression at the specified index of a `call_indirect`
// expression.
void BinaryenCallIndirectSetOperandAt(BinaryenExpressionRef expr, BinaryenIndex index, BinaryenExpressionRef operandExpr);
// Appends an operand expression to a `call_indirect` expression, returning its
// insertion index.
BinaryenIndex BinaryenCallIndirectAppendOperand(
    BinaryenExpressionRef expr, BinaryenExpressionRef operandExpr
);
// Inserts an operand expression at the specified index of a `call_indirect`
// expression, moving existing operands including the one previously at that
// index one index up.
void BinaryenCallIndirectInsertOperandAt(BinaryenExpressionRef expr, BinaryenIndex index, BinaryenExpressionRef operandExpr);
// Removes the operand expression at the specified index of a `call_indirect`
// expression, moving all subsequent operands one index down. Returns the
// operand expression.
BinaryenExpressionRef BinaryenCallIndirectRemoveOperandAt(
    BinaryenExpressionRef expr, BinaryenIndex index
);
// Gets whether the specified `call_indirect` expression is a tail call.
_Bool BinaryenCallIndirectIsReturn(BinaryenExpressionRef expr);
// Sets whether the specified `call_indirect` expression is a tail call.
void BinaryenCallIndirectSetReturn(BinaryenExpressionRef expr, _Bool isReturn);
// Gets the parameter types of the specified `call_indirect` expression.
BinaryenType
BinaryenCallIndirectGetParams(BinaryenExpressionRef expr);
// Sets the parameter types of the specified `call_indirect` expression.
void BinaryenCallIndirectSetParams(BinaryenExpressionRef expr, BinaryenType params);
// Gets the result types of the specified `call_indirect` expression.
BinaryenType
BinaryenCallIndirectGetResults(BinaryenExpressionRef expr);
// Sets the result types of the specified `call_indirect` expression.
void BinaryenCallIndirectSetResults(BinaryenExpressionRef expr, BinaryenType params);

// LocalGet

// Gets the local index of a `local.get` expression.
BinaryenIndex BinaryenLocalGetGetIndex(BinaryenExpressionRef expr);
// Sets the local index of a `local.get` expression.
void BinaryenLocalGetSetIndex(BinaryenExpressionRef expr, BinaryenIndex index);

// LocalSet

// Gets whether a `local.set` tees its value (is a `local.tee`). True if the
// expression has a type other than `none`.
_Bool BinaryenLocalSetIsTee(BinaryenExpressionRef expr);
// Gets the local index of a `local.set` or `local.tee` expression.
BinaryenIndex BinaryenLocalSetGetIndex(BinaryenExpressionRef expr);
// Sets the local index of a `local.set` or `local.tee` expression.
void BinaryenLocalSetSetIndex(BinaryenExpressionRef expr, BinaryenIndex index);
// Gets the value expression of a `local.set` or `local.tee` expression.
BinaryenExpressionRef
BinaryenLocalSetGetValue(BinaryenExpressionRef expr);
// Sets the value expression of a `local.set` or `local.tee` expression.
void BinaryenLocalSetSetValue(BinaryenExpressionRef expr, BinaryenExpressionRef valueExpr);

// GlobalGet

// Gets the name of the global being accessed by a `global.get` expression.
__const char *BinaryenGlobalGetGetName(BinaryenExpressionRef expr);
// Sets the name of the global being accessed by a `global.get` expression.
void BinaryenGlobalGetSetName(BinaryenExpressionRef expr, __const char *name);

// GlobalSet

// Gets the name of the global being accessed by a `global.set` expression.
__const char *BinaryenGlobalSetGetName(BinaryenExpressionRef expr);
// Sets the name of the global being accessed by a `global.set` expression.
void BinaryenGlobalSetSetName(BinaryenExpressionRef expr, __const char *name);
// Gets the value expression of a `global.set` expression.
BinaryenExpressionRef
BinaryenGlobalSetGetValue(BinaryenExpressionRef expr);
// Sets the value expression of a `global.set` expression.
void BinaryenGlobalSetSetValue(BinaryenExpressionRef expr, BinaryenExpressionRef valueExpr);

// TableGet

// Gets the name of the table being accessed by a `table.get` expression.
__const char *BinaryenTableGetGetTable(BinaryenExpressionRef expr);
// Sets the name of the table being accessed by a `table.get` expression.
void BinaryenTableGetSetTable(BinaryenExpressionRef expr, __const char *table);
// Gets the index expression of a `table.get` expression.
BinaryenExpressionRef
BinaryenTableGetGetIndex(BinaryenExpressionRef expr);
// Sets the index expression of a `table.get` expression.
void BinaryenTableGetSetIndex(BinaryenExpressionRef expr, BinaryenExpressionRef indexExpr);

// TableSet

// Gets the name of the table being accessed by a `table.set` expression.
__const char *BinaryenTableSetGetTable(BinaryenExpressionRef expr);
// Sets the name of the table being accessed by a `table.set` expression.
void BinaryenTableSetSetTable(BinaryenExpressionRef expr, __const char *table);
// Gets the index expression of a `table.set` expression.
BinaryenExpressionRef
BinaryenTableSetGetIndex(BinaryenExpressionRef expr);
// Sets the index expression of a `table.set` expression.
void BinaryenTableSetSetIndex(BinaryenExpressionRef expr, BinaryenExpressionRef indexExpr);
// Gets the value expression of a `table.set` expression.
BinaryenExpressionRef
BinaryenTableSetGetValue(BinaryenExpressionRef expr);
// Sets the value expression of a `table.set` expression.
void BinaryenTableSetSetValue(BinaryenExpressionRef expr, BinaryenExpressionRef valueExpr);

// TableSize

// Gets the name of the table being accessed by a `table.size` expression.
__const char *BinaryenTableSizeGetTable(BinaryenExpressionRef expr);
// Sets the name of the table being accessed by a `table.size` expression.
void BinaryenTableSizeSetTable(BinaryenExpressionRef expr, __const char *table);

// TableGrow

// Gets the name of the table being accessed by a `table.grow` expression.
__const char *BinaryenTableGrowGetTable(BinaryenExpressionRef expr);
// Sets the name of the table being accessed by a `table.grow` expression.
void BinaryenTableGrowSetTable(BinaryenExpressionRef expr, __const char *table);
// Gets the value expression of a `table.grow` expression.
BinaryenExpressionRef
BinaryenTableGrowGetValue(BinaryenExpressionRef expr);
// Sets the value expression of a `table.grow` expression.
void BinaryenTableGrowSetValue(BinaryenExpressionRef expr, BinaryenExpressionRef valueExpr);
// Gets the delta of a `table.grow` expression.
BinaryenExpressionRef
BinaryenTableGrowGetDelta(BinaryenExpressionRef expr);
// Sets the delta of a `table.grow` expression.
void BinaryenTableGrowSetDelta(BinaryenExpressionRef expr, BinaryenExpressionRef deltaExpr);
// MemoryGrow

// Gets the delta of a `memory.grow` expression.
BinaryenExpressionRef
BinaryenMemoryGrowGetDelta(BinaryenExpressionRef expr);
// Sets the delta of a `memory.grow` expression.
void BinaryenMemoryGrowSetDelta(BinaryenExpressionRef expr, BinaryenExpressionRef deltaExpr);

// Load

// Gets whether a `load` expression is atomic (is an `atomic.load`).
_Bool BinaryenLoadIsAtomic(BinaryenExpressionRef expr);
// Sets whether a `load` expression is atomic (is an `atomic.load`).
void BinaryenLoadSetAtomic(BinaryenExpressionRef expr, _Bool isAtomic);
// Gets whether a `load` expression operates on a __signed value (`_s`).
_Bool BinaryenLoadIsSigned(BinaryenExpressionRef expr);
// Sets whether a `load` expression operates on a __signed value (`_s`).
void BinaryenLoadSetSigned(BinaryenExpressionRef expr, _Bool isSigned);
// Gets the constant offset of a `load` expression.
uint32_t BinaryenLoadGetOffset(BinaryenExpressionRef expr);
// Sets the constant offset of a `load` expression.
void BinaryenLoadSetOffset(BinaryenExpressionRef expr, uint32_t offset);
// Gets the number of bytes loaded by a `load` expression.
uint32_t BinaryenLoadGetBytes(BinaryenExpressionRef expr);
// Sets the number of bytes loaded by a `load` expression.
void BinaryenLoadSetBytes(BinaryenExpressionRef expr, uint32_t bytes);
// Gets the byte alignment of a `load` expression.
uint32_t BinaryenLoadGetAlign(BinaryenExpressionRef expr);
// Sets the byte alignment of a `load` expression.
void BinaryenLoadSetAlign(BinaryenExpressionRef expr, uint32_t align);
// Gets the pointer expression of a `load` expression.
BinaryenExpressionRef
BinaryenLoadGetPtr(BinaryenExpressionRef expr);
// Sets the pointer expression of a `load` expression.
void BinaryenLoadSetPtr(BinaryenExpressionRef expr, BinaryenExpressionRef ptrExpr);

// Store

// Gets whether a `store` expression is atomic (is an `atomic.store`).
_Bool BinaryenStoreIsAtomic(BinaryenExpressionRef expr);
// Sets whether a `store` expression is atomic (is an `atomic.store`).
void BinaryenStoreSetAtomic(BinaryenExpressionRef expr, _Bool isAtomic);
// Gets the number of bytes stored by a `store` expression.
uint32_t BinaryenStoreGetBytes(BinaryenExpressionRef expr);
// Sets the number of bytes stored by a `store` expression.
void BinaryenStoreSetBytes(BinaryenExpressionRef expr, uint32_t bytes);
// Gets the constant offset of a `store` expression.
uint32_t BinaryenStoreGetOffset(BinaryenExpressionRef expr);
// Sets the constant offset of a `store` expression.
void BinaryenStoreSetOffset(BinaryenExpressionRef expr, uint32_t offset);
// Gets the byte alignment of a `store` expression.
uint32_t BinaryenStoreGetAlign(BinaryenExpressionRef expr);
// Sets the byte alignment of a `store` expression.
void BinaryenStoreSetAlign(BinaryenExpressionRef expr, uint32_t align);
// Gets the pointer expression of a `store` expression.
BinaryenExpressionRef
BinaryenStoreGetPtr(BinaryenExpressionRef expr);
// Sets the pointer expression of a `store` expression.
void BinaryenStoreSetPtr(BinaryenExpressionRef expr, BinaryenExpressionRef ptrExpr);
// Gets the value expression of a `store` expression.
BinaryenExpressionRef
BinaryenStoreGetValue(BinaryenExpressionRef expr);
// Sets the value expression of a `store` expression.
void BinaryenStoreSetValue(BinaryenExpressionRef expr, BinaryenExpressionRef valueExpr);
// Gets the value type of a `store` expression.
BinaryenType BinaryenStoreGetValueType(BinaryenExpressionRef expr);
// Sets the value type of a `store` expression.
void BinaryenStoreSetValueType(BinaryenExpressionRef expr, BinaryenType valueType);

// Const

// Gets the 32-bit integer value of an `i32.__const` expression.
int32_t BinaryenConstGetValueI32(BinaryenExpressionRef expr);
// Sets the 32-bit integer value of an `i32.__const` expression.
void BinaryenConstSetValueI32(BinaryenExpressionRef expr, int32_t value);
// Gets the 64-bit integer value of an `i64.__const` expression.
int64_t BinaryenConstGetValueI64(BinaryenExpressionRef expr);
// Sets the 64-bit integer value of an `i64.__const` expression.
void BinaryenConstSetValueI64(BinaryenExpressionRef expr, int64_t value);
// Gets the low 32-bits of the 64-bit integer value of an `i64.__const`
// expression.
int32_t BinaryenConstGetValueI64Low(BinaryenExpressionRef expr);
// Sets the low 32-bits of the 64-bit integer value of an `i64.__const`
// expression.
void BinaryenConstSetValueI64Low(BinaryenExpressionRef expr, int32_t valueLow);
// Gets the high 32-bits of the 64-bit integer value of an `i64.__const`
// expression.
int32_t BinaryenConstGetValueI64High(BinaryenExpressionRef expr);
// Sets the high 32-bits of the 64-bit integer value of an `i64.__const`
// expression.
void BinaryenConstSetValueI64High(BinaryenExpressionRef expr, int32_t valueHigh);
// Gets the 32-bit float value of a `f32.__const` expression.
float BinaryenConstGetValueF32(BinaryenExpressionRef expr);
// Sets the 32-bit float value of a `f32.__const` expression.
void BinaryenConstSetValueF32(BinaryenExpressionRef expr, float value);
// Gets the 64-bit float (double) value of a `f64.__const` expression.
double BinaryenConstGetValueF64(BinaryenExpressionRef expr);
// Sets the 64-bit float (double) value of a `f64.__const` expression.
void BinaryenConstSetValueF64(BinaryenExpressionRef expr, double value);
// Reads the 128-bit vector value of a `v128.__const` expression.
void BinaryenConstGetValueV128(BinaryenExpressionRef expr, uint8_t *out);
// Sets the 128-bit vector value of a `v128.__const` expression.
void BinaryenConstSetValueV128(BinaryenExpressionRef expr, __const uint8_t value[16]);

// Unary

// Gets the operation being performed by a unary expression.
BinaryenOp BinaryenUnaryGetOp(BinaryenExpressionRef expr);
// Sets the operation being performed by a unary expression.
void BinaryenUnarySetOp(BinaryenExpressionRef expr, BinaryenOp op);
// Gets the value expression of a unary expression.
BinaryenExpressionRef
BinaryenUnaryGetValue(BinaryenExpressionRef expr);
// Sets the value expression of a unary expression.
void BinaryenUnarySetValue(BinaryenExpressionRef expr, BinaryenExpressionRef valueExpr);

// Binary

// Gets the operation being performed by a binary expression.
BinaryenOp BinaryenBinaryGetOp(BinaryenExpressionRef expr);
// Sets the operation being performed by a binary expression.
void BinaryenBinarySetOp(BinaryenExpressionRef expr, BinaryenOp op);
// Gets the left expression of a binary expression.
BinaryenExpressionRef
BinaryenBinaryGetLeft(BinaryenExpressionRef expr);
// Sets the left expression of a binary expression.
void BinaryenBinarySetLeft(BinaryenExpressionRef expr, BinaryenExpressionRef leftExpr);
// Gets the right expression of a binary expression.
BinaryenExpressionRef
BinaryenBinaryGetRight(BinaryenExpressionRef expr);
// Sets the right expression of a binary expression.
void BinaryenBinarySetRight(BinaryenExpressionRef expr, BinaryenExpressionRef rightExpr);

// Select

// Gets the expression becoming selected by a `select` expression if the
// condition turns out 1 .
BinaryenExpressionRef
BinaryenSelectGetIfTrue(BinaryenExpressionRef expr);
// Sets the expression becoming selected by a `select` expression if the
// condition turns out 1 .
void BinaryenSelectSetIfTrue(BinaryenExpressionRef expr, BinaryenExpressionRef ifTrueExpr);
// Gets the expression becoming selected by a `select` expression if the
// condition turns out 0 .
BinaryenExpressionRef
BinaryenSelectGetIfFalse(BinaryenExpressionRef expr);
// Sets the expression becoming selected by a `select` expression if the
// condition turns out 0 .
void BinaryenSelectSetIfFalse(BinaryenExpressionRef expr, BinaryenExpressionRef ifFalseExpr);
// Gets the condition expression of a `select` expression.
BinaryenExpressionRef
BinaryenSelectGetCondition(BinaryenExpressionRef expr);
// Sets the condition expression of a `select` expression.
void BinaryenSelectSetCondition(BinaryenExpressionRef expr, BinaryenExpressionRef condExpr);

// Drop

// Gets the value expression being dropped by a `drop` expression.
BinaryenExpressionRef
BinaryenDropGetValue(BinaryenExpressionRef expr);
// Sets the value expression being dropped by a `drop` expression.
void BinaryenDropSetValue(BinaryenExpressionRef expr, BinaryenExpressionRef valueExpr);

// Return

// Gets the value expression, if any, being returned by a `return` expression.
BinaryenExpressionRef
BinaryenReturnGetValue(BinaryenExpressionRef expr);
// Sets the value expression, if any, being returned by a `return` expression.
void BinaryenReturnSetValue(BinaryenExpressionRef expr, BinaryenExpressionRef valueExpr);

// AtomicRMW

// Gets the operation being performed by an atomic read-modify-write expression.
BinaryenOp BinaryenAtomicRMWGetOp(BinaryenExpressionRef expr);
// Sets the operation being performed by an atomic read-modify-write expression.
void BinaryenAtomicRMWSetOp(BinaryenExpressionRef expr, BinaryenOp op);
// Gets the number of bytes affected by an atomic read-modify-write expression.
uint32_t BinaryenAtomicRMWGetBytes(BinaryenExpressionRef expr);
// Sets the number of bytes affected by an atomic read-modify-write expression.
void BinaryenAtomicRMWSetBytes(BinaryenExpressionRef expr, uint32_t bytes);
// Gets the constant offset of an atomic read-modify-write expression.
uint32_t BinaryenAtomicRMWGetOffset(BinaryenExpressionRef expr);
// Sets the constant offset of an atomic read-modify-write expression.
void BinaryenAtomicRMWSetOffset(BinaryenExpressionRef expr, uint32_t offset);
// Gets the pointer expression of an atomic read-modify-write expression.
BinaryenExpressionRef
BinaryenAtomicRMWGetPtr(BinaryenExpressionRef expr);
// Sets the pointer expression of an atomic read-modify-write expression.
void BinaryenAtomicRMWSetPtr(BinaryenExpressionRef expr, BinaryenExpressionRef ptrExpr);
// Gets the value expression of an atomic read-modify-write expression.
BinaryenExpressionRef
BinaryenAtomicRMWGetValue(BinaryenExpressionRef expr);
// Sets the value expression of an atomic read-modify-write expression.
void BinaryenAtomicRMWSetValue(BinaryenExpressionRef expr, BinaryenExpressionRef valueExpr);

// AtomicCmpxchg

// Gets the number of bytes affected by an atomic compare and exchange
// expression.
uint32_t BinaryenAtomicCmpxchgGetBytes(BinaryenExpressionRef expr);
// Sets the number of bytes affected by an atomic compare and exchange
// expression.
void BinaryenAtomicCmpxchgSetBytes(BinaryenExpressionRef expr, uint32_t bytes);
// Gets the constant offset of an atomic compare and exchange expression.
uint32_t
BinaryenAtomicCmpxchgGetOffset(BinaryenExpressionRef expr);
// Sets the constant offset of an atomic compare and exchange expression.
void BinaryenAtomicCmpxchgSetOffset(BinaryenExpressionRef expr, uint32_t offset);
// Gets the pointer expression of an atomic compare and exchange expression.
BinaryenExpressionRef
BinaryenAtomicCmpxchgGetPtr(BinaryenExpressionRef expr);
// Sets the pointer expression of an atomic compare and exchange expression.
void BinaryenAtomicCmpxchgSetPtr(BinaryenExpressionRef expr, BinaryenExpressionRef ptrExpr);
// Gets the expression representing the expected value of an atomic compare and
// exchange expression.
BinaryenExpressionRef
BinaryenAtomicCmpxchgGetExpected(BinaryenExpressionRef expr);
// Sets the expression representing the expected value of an atomic compare and
// exchange expression.
void BinaryenAtomicCmpxchgSetExpected(BinaryenExpressionRef expr, BinaryenExpressionRef expectedExpr);
// Gets the replacement expression of an atomic compare and exchange expression.
BinaryenExpressionRef
BinaryenAtomicCmpxchgGetReplacement(BinaryenExpressionRef expr);
// Sets the replacement expression of an atomic compare and exchange expression.
void BinaryenAtomicCmpxchgSetReplacement(BinaryenExpressionRef expr, BinaryenExpressionRef replacementExpr);

// AtomicWait

// Gets the pointer expression of an `memory.atomic.wait` expression.
BinaryenExpressionRef
BinaryenAtomicWaitGetPtr(BinaryenExpressionRef expr);
// Sets the pointer expression of an `memory.atomic.wait` expression.
void BinaryenAtomicWaitSetPtr(BinaryenExpressionRef expr, BinaryenExpressionRef ptrExpr);
// Gets the expression representing the expected value of an
// `memory.atomic.wait` expression.
BinaryenExpressionRef
BinaryenAtomicWaitGetExpected(BinaryenExpressionRef expr);
// Sets the expression representing the expected value of an
// `memory.atomic.wait` expression.
void BinaryenAtomicWaitSetExpected(BinaryenExpressionRef expr, BinaryenExpressionRef expectedExpr);
// Gets the timeout expression of an `memory.atomic.wait` expression.
BinaryenExpressionRef
BinaryenAtomicWaitGetTimeout(BinaryenExpressionRef expr);
// Sets the timeout expression of an `memory.atomic.wait` expression.
void BinaryenAtomicWaitSetTimeout(BinaryenExpressionRef expr, BinaryenExpressionRef timeoutExpr);
// Gets the expected type of an `memory.atomic.wait` expression.
BinaryenType
BinaryenAtomicWaitGetExpectedType(BinaryenExpressionRef expr);
// Sets the expected type of an `memory.atomic.wait` expression.
void BinaryenAtomicWaitSetExpectedType(BinaryenExpressionRef expr, BinaryenType expectedType);

// AtomicNotify

// Gets the pointer expression of an `memory.atomic.notify` expression.
BinaryenExpressionRef
BinaryenAtomicNotifyGetPtr(BinaryenExpressionRef expr);
// Sets the pointer expression of an `memory.atomic.notify` expression.
void BinaryenAtomicNotifySetPtr(BinaryenExpressionRef expr, BinaryenExpressionRef ptrExpr);
// Gets the notify count expression of an `memory.atomic.notify` expression.
BinaryenExpressionRef
BinaryenAtomicNotifyGetNotifyCount(BinaryenExpressionRef expr);
// Sets the notify count expression of an `memory.atomic.notify` expression.
void BinaryenAtomicNotifySetNotifyCount(BinaryenExpressionRef expr, BinaryenExpressionRef notifyCountExpr);

// AtomicFence

// Gets the order of an `atomic.fence` expression.
uint8_t BinaryenAtomicFenceGetOrder(BinaryenExpressionRef expr);
// Sets the order of an `atomic.fence` expression.
void BinaryenAtomicFenceSetOrder(BinaryenExpressionRef expr, uint8_t order);

// SIMDExtract

// Gets the operation being performed by a SIMD extract expression.
BinaryenOp BinaryenSIMDExtractGetOp(BinaryenExpressionRef expr);
// Sets the operation being performed by a SIMD extract expression.
void BinaryenSIMDExtractSetOp(BinaryenExpressionRef expr, BinaryenOp op);
// Gets the vector expression a SIMD extract expression extracts from.
BinaryenExpressionRef
BinaryenSIMDExtractGetVec(BinaryenExpressionRef expr);
// Sets the vector expression a SIMD extract expression extracts from.
void BinaryenSIMDExtractSetVec(BinaryenExpressionRef expr, BinaryenExpressionRef vecExpr);
// Gets the index of the extracted lane of a SIMD extract expression.
uint8_t BinaryenSIMDExtractGetIndex(BinaryenExpressionRef expr);
// Sets the index of the extracted lane of a SIMD extract expression.
void BinaryenSIMDExtractSetIndex(BinaryenExpressionRef expr, uint8_t index);

// SIMDReplace

// Gets the operation being performed by a SIMD replace expression.
BinaryenOp BinaryenSIMDReplaceGetOp(BinaryenExpressionRef expr);
// Sets the operation being performed by a SIMD replace expression.
void BinaryenSIMDReplaceSetOp(BinaryenExpressionRef expr, BinaryenOp op);
// Gets the vector expression a SIMD replace expression replaces in.
BinaryenExpressionRef
BinaryenSIMDReplaceGetVec(BinaryenExpressionRef expr);
// Sets the vector expression a SIMD replace expression replaces in.
void BinaryenSIMDReplaceSetVec(BinaryenExpressionRef expr, BinaryenExpressionRef vecExpr);
// Gets the index of the replaced lane of a SIMD replace expression.
uint8_t BinaryenSIMDReplaceGetIndex(BinaryenExpressionRef expr);
// Sets the index of the replaced lane of a SIMD replace expression.
void BinaryenSIMDReplaceSetIndex(BinaryenExpressionRef expr, uint8_t index);
// Gets the value expression a SIMD replace expression replaces with.
BinaryenExpressionRef
BinaryenSIMDReplaceGetValue(BinaryenExpressionRef expr);
// Sets the value expression a SIMD replace expression replaces with.
void BinaryenSIMDReplaceSetValue(BinaryenExpressionRef expr, BinaryenExpressionRef valueExpr);

// SIMDShuffle

// Gets the left expression of a SIMD shuffle expression.
BinaryenExpressionRef
BinaryenSIMDShuffleGetLeft(BinaryenExpressionRef expr);
// Sets the left expression of a SIMD shuffle expression.
void BinaryenSIMDShuffleSetLeft(BinaryenExpressionRef expr, BinaryenExpressionRef leftExpr);
// Gets the right expression of a SIMD shuffle expression.
BinaryenExpressionRef
BinaryenSIMDShuffleGetRight(BinaryenExpressionRef expr);
// Sets the right expression of a SIMD shuffle expression.
void BinaryenSIMDShuffleSetRight(BinaryenExpressionRef expr, BinaryenExpressionRef rightExpr);
// Gets the 128-bit mask of a SIMD shuffle expression.
void BinaryenSIMDShuffleGetMask(BinaryenExpressionRef expr, uint8_t *mask);
// Sets the 128-bit mask of a SIMD shuffle expression.
void BinaryenSIMDShuffleSetMask(BinaryenExpressionRef expr, __const uint8_t mask[16]);

// SIMDTernary

// Gets the operation being performed by a SIMD ternary expression.
BinaryenOp BinaryenSIMDTernaryGetOp(BinaryenExpressionRef expr);
// Sets the operation being performed by a SIMD ternary expression.
void BinaryenSIMDTernarySetOp(BinaryenExpressionRef expr, BinaryenOp op);
// Gets the first operand expression of a SIMD ternary expression.
BinaryenExpressionRef
BinaryenSIMDTernaryGetA(BinaryenExpressionRef expr);
// Sets the first operand expression of a SIMD ternary expression.
void BinaryenSIMDTernarySetA(BinaryenExpressionRef expr, BinaryenExpressionRef aExpr);
// Gets the second operand expression of a SIMD ternary expression.
BinaryenExpressionRef
BinaryenSIMDTernaryGetB(BinaryenExpressionRef expr);
// Sets the second operand expression of a SIMD ternary expression.
void BinaryenSIMDTernarySetB(BinaryenExpressionRef expr, BinaryenExpressionRef bExpr);
// Gets the third operand expression of a SIMD ternary expression.
BinaryenExpressionRef
BinaryenSIMDTernaryGetC(BinaryenExpressionRef expr);
// Sets the third operand expression of a SIMD ternary expression.
void BinaryenSIMDTernarySetC(BinaryenExpressionRef expr, BinaryenExpressionRef cExpr);

// SIMDShift

// Gets the operation being performed by a SIMD shift expression.
BinaryenOp BinaryenSIMDShiftGetOp(BinaryenExpressionRef expr);
// Sets the operation being performed by a SIMD shift expression.
void BinaryenSIMDShiftSetOp(BinaryenExpressionRef expr, BinaryenOp op);
// Gets the expression being shifted by a SIMD shift expression.
BinaryenExpressionRef
BinaryenSIMDShiftGetVec(BinaryenExpressionRef expr);
// Sets the expression being shifted by a SIMD shift expression.
void BinaryenSIMDShiftSetVec(BinaryenExpressionRef expr, BinaryenExpressionRef vecExpr);
// Gets the expression representing the shift of a SIMD shift expression.
BinaryenExpressionRef
BinaryenSIMDShiftGetShift(BinaryenExpressionRef expr);
// Sets the expression representing the shift of a SIMD shift expression.
void BinaryenSIMDShiftSetShift(BinaryenExpressionRef expr, BinaryenExpressionRef shiftExpr);

// SIMDLoad

// Gets the operation being performed by a SIMD load expression.
BinaryenOp BinaryenSIMDLoadGetOp(BinaryenExpressionRef expr);
// Sets the operation being performed by a SIMD load expression.
void BinaryenSIMDLoadSetOp(BinaryenExpressionRef expr, BinaryenOp op);
// Gets the constant offset of a SIMD load expression.
uint32_t BinaryenSIMDLoadGetOffset(BinaryenExpressionRef expr);
// Sets the constant offset of a SIMD load expression.
void BinaryenSIMDLoadSetOffset(BinaryenExpressionRef expr, uint32_t offset);
// Gets the byte alignment of a SIMD load expression.
uint32_t BinaryenSIMDLoadGetAlign(BinaryenExpressionRef expr);
// Sets the byte alignment of a SIMD load expression.
void BinaryenSIMDLoadSetAlign(BinaryenExpressionRef expr, uint32_t align);
// Gets the pointer expression of a SIMD load expression.
BinaryenExpressionRef
BinaryenSIMDLoadGetPtr(BinaryenExpressionRef expr);
// Sets the pointer expression of a SIMD load expression.
void BinaryenSIMDLoadSetPtr(BinaryenExpressionRef expr, BinaryenExpressionRef ptrExpr);

// SIMDLoadStoreLane

// Gets the operation being performed by a SIMD load/store lane expression.
BinaryenOp
BinaryenSIMDLoadStoreLaneGetOp(BinaryenExpressionRef expr);
// Sets the operation being performed by a SIMD load/store lane expression.
void BinaryenSIMDLoadStoreLaneSetOp(BinaryenExpressionRef expr, BinaryenOp op);
// Gets the constant offset of a SIMD load/store lane expression.
uint32_t
BinaryenSIMDLoadStoreLaneGetOffset(BinaryenExpressionRef expr);
// Sets the constant offset of a SIMD load/store lane expression.
void BinaryenSIMDLoadStoreLaneSetOffset(BinaryenExpressionRef expr, uint32_t offset);
// Gets the byte alignment of a SIMD load/store lane expression.
uint32_t
BinaryenSIMDLoadStoreLaneGetAlign(BinaryenExpressionRef expr);
// Sets the byte alignment of a SIMD load/store lane expression.
void BinaryenSIMDLoadStoreLaneSetAlign(BinaryenExpressionRef expr, uint32_t align);
// Gets the lane index of a SIMD load/store lane expression.
uint8_t
BinaryenSIMDLoadStoreLaneGetIndex(BinaryenExpressionRef expr);
// Sets the lane index of a SIMD load/store lane expression.
void BinaryenSIMDLoadStoreLaneSetIndex(BinaryenExpressionRef expr, uint8_t index);
// Gets the pointer expression of a SIMD load/store lane expression.
BinaryenExpressionRef
BinaryenSIMDLoadStoreLaneGetPtr(BinaryenExpressionRef expr);
// Sets the pointer expression of a SIMD load/store lane expression.
void BinaryenSIMDLoadStoreLaneSetPtr(BinaryenExpressionRef expr, BinaryenExpressionRef ptrExpr);
// Gets the vector expression of a SIMD load/store lane expression.
BinaryenExpressionRef
BinaryenSIMDLoadStoreLaneGetVec(BinaryenExpressionRef expr);
// Sets the vector expression of a SIMD load/store lane expression.
void BinaryenSIMDLoadStoreLaneSetVec(BinaryenExpressionRef expr, BinaryenExpressionRef vecExpr);
// Gets whether a SIMD load/store lane expression performs a store. Otherwise it
// performs a load.
_Bool BinaryenSIMDLoadStoreLaneIsStore(BinaryenExpressionRef expr);

// MemoryInit

// Gets the index of the segment being initialized by a `memory.init`
// expression.
__const char *
BinaryenMemoryInitGetSegment(BinaryenExpressionRef expr);
// Sets the index of the segment being initialized by a `memory.init`
// expression.
void BinaryenMemoryInitSetSegment(BinaryenExpressionRef expr, __const char *segment);
// Gets the destination expression of a `memory.init` expression.
BinaryenExpressionRef
BinaryenMemoryInitGetDest(BinaryenExpressionRef expr);
// Sets the destination expression of a `memory.init` expression.
void BinaryenMemoryInitSetDest(BinaryenExpressionRef expr, BinaryenExpressionRef destExpr);
// Gets the offset expression of a `memory.init` expression.
BinaryenExpressionRef
BinaryenMemoryInitGetOffset(BinaryenExpressionRef expr);
// Sets the offset expression of a `memory.init` expression.
void BinaryenMemoryInitSetOffset(BinaryenExpressionRef expr, BinaryenExpressionRef offsetExpr);
// Gets the size expression of a `memory.init` expression.
BinaryenExpressionRef
BinaryenMemoryInitGetSize(BinaryenExpressionRef expr);
// Sets the size expression of a `memory.init` expression.
void BinaryenMemoryInitSetSize(BinaryenExpressionRef expr, BinaryenExpressionRef sizeExpr);

// DataDrop

// Gets the index of the segment being dropped by a `data.drop` expression.
__const char *BinaryenDataDropGetSegment(BinaryenExpressionRef expr);
// Sets the index of the segment being dropped by a `data.drop` expression.
void BinaryenDataDropSetSegment(BinaryenExpressionRef expr, __const char *segment);

// MemoryCopy

// Gets the destination expression of a `memory.copy` expression.
BinaryenExpressionRef
BinaryenMemoryCopyGetDest(BinaryenExpressionRef expr);
// Sets the destination expression of a `memory.copy` expression.
void BinaryenMemoryCopySetDest(BinaryenExpressionRef expr, BinaryenExpressionRef destExpr);
// Gets the source expression of a `memory.copy` expression.
BinaryenExpressionRef
BinaryenMemoryCopyGetSource(BinaryenExpressionRef expr);
// Sets the source expression of a `memory.copy` expression.
void BinaryenMemoryCopySetSource(BinaryenExpressionRef expr, BinaryenExpressionRef sourceExpr);
// Gets the size expression (number of bytes copied) of a `memory.copy`
// expression.
BinaryenExpressionRef
BinaryenMemoryCopyGetSize(BinaryenExpressionRef expr);
// Sets the size expression (number of bytes copied) of a `memory.copy`
// expression.
void BinaryenMemoryCopySetSize(BinaryenExpressionRef expr, BinaryenExpressionRef sizeExpr);

// MemoryFill

// Gets the destination expression of a `memory.fill` expression.
BinaryenExpressionRef
BinaryenMemoryFillGetDest(BinaryenExpressionRef expr);
// Sets the destination expression of a `memory.fill` expression.
void BinaryenMemoryFillSetDest(BinaryenExpressionRef expr, BinaryenExpressionRef destExpr);
// Gets the value expression of a `memory.fill` expression.
BinaryenExpressionRef
BinaryenMemoryFillGetValue(BinaryenExpressionRef expr);
// Sets the value expression of a `memory.fill` expression.
void BinaryenMemoryFillSetValue(BinaryenExpressionRef expr, BinaryenExpressionRef valueExpr);
// Gets the size expression (number of bytes filled) of a `memory.fill`
// expression.
BinaryenExpressionRef
BinaryenMemoryFillGetSize(BinaryenExpressionRef expr);
// Sets the size expression (number of bytes filled) of a `memory.fill`
// expression.
void BinaryenMemoryFillSetSize(BinaryenExpressionRef expr, BinaryenExpressionRef sizeExpr);

// RefIsNull

BinaryenExpressionRef
BinaryenRefIsNullGetValue(BinaryenExpressionRef expr);
// Sets the value expression tested by a `ref.is_null` expression.
void BinaryenRefIsNullSetValue(BinaryenExpressionRef expr, BinaryenExpressionRef valueExpr);

// RefAs

// Gets the operation performed by a `ref.as_*` expression.
BinaryenOp BinaryenRefAsGetOp(BinaryenExpressionRef expr);
// Sets the operation performed by a `ref.as_*` expression.
void BinaryenRefAsSetOp(BinaryenExpressionRef expr, BinaryenOp op);
// Gets the value expression tested by a `ref.as_*` expression.
BinaryenExpressionRef
BinaryenRefAsGetValue(BinaryenExpressionRef expr);
// Sets the value expression tested by a `ref.as_*` expression.
void BinaryenRefAsSetValue(BinaryenExpressionRef expr, BinaryenExpressionRef valueExpr);

// RefFunc

// Gets the name of the function being wrapped by a `ref.func` expression.
__const char *BinaryenRefFuncGetFunc(BinaryenExpressionRef expr);
// Sets the name of the function being wrapped by a `ref.func` expression.
void BinaryenRefFuncSetFunc(BinaryenExpressionRef expr, __const char *funcName);

// RefEq

// Gets the left expression of a `ref.eq` expression.
BinaryenExpressionRef
BinaryenRefEqGetLeft(BinaryenExpressionRef expr);
// Sets the left expression of a `ref.eq` expression.
void BinaryenRefEqSetLeft(BinaryenExpressionRef expr, BinaryenExpressionRef left);
// Gets the right expression of a `ref.eq` expression.
BinaryenExpressionRef
BinaryenRefEqGetRight(BinaryenExpressionRef expr);
// Sets the right expression of a `ref.eq` expression.
void BinaryenRefEqSetRight(BinaryenExpressionRef expr, BinaryenExpressionRef right);

// Try

// Gets the name (label) of a `try` expression.
__const char *BinaryenTryGetName(BinaryenExpressionRef expr);
// Sets the name (label) of a `try` expression.
void BinaryenTrySetName(BinaryenExpressionRef expr, __const char *name);
// Gets the body expression of a `try` expression.
BinaryenExpressionRef
BinaryenTryGetBody(BinaryenExpressionRef expr);
// Sets the body expression of a `try` expression.
void BinaryenTrySetBody(BinaryenExpressionRef expr, BinaryenExpressionRef bodyExpr);
// Gets the number of catch blocks (= the number of catch tags) of a `try`
// expression.
BinaryenIndex
BinaryenTryGetNumCatchTags(BinaryenExpressionRef expr);
// Gets the number of catch/catch_all blocks of a `try` expression.
BinaryenIndex
BinaryenTryGetNumCatchBodies(BinaryenExpressionRef expr);
// Gets the catch tag at the specified index of a `try` expression.
__const char *BinaryenTryGetCatchTagAt(BinaryenExpressionRef expr, BinaryenIndex index);
// Sets the catch tag at the specified index of a `try` expression.
void BinaryenTrySetCatchTagAt(BinaryenExpressionRef expr, BinaryenIndex index, __const char *catchTag);
// Appends a catch tag to a `try` expression, returning its insertion index.
BinaryenIndex BinaryenTryAppendCatchTag(BinaryenExpressionRef expr, __const char *catchTag);
// Inserts a catch tag at the specified index of a `try` expression, moving
// existing catch tags including the one previously at that index one index up.
void BinaryenTryInsertCatchTagAt(BinaryenExpressionRef expr, BinaryenIndex index, __const char *catchTag);
// Removes the catch tag at the specified index of a `try` expression, moving
// all subsequent catch tags one index down. Returns the tag.
__const char *BinaryenTryRemoveCatchTagAt(BinaryenExpressionRef expr, BinaryenIndex index);
// Gets the catch body expression at the specified index of a `try` expression.
BinaryenExpressionRef
BinaryenTryGetCatchBodyAt(BinaryenExpressionRef expr, BinaryenIndex index);
// Sets the catch body expression at the specified index of a `try` expression.
void BinaryenTrySetCatchBodyAt(BinaryenExpressionRef expr, BinaryenIndex index, BinaryenExpressionRef catchExpr);
// Appends a catch expression to a `try` expression, returning its insertion
// index.
BinaryenIndex BinaryenTryAppendCatchBody(
    BinaryenExpressionRef expr, BinaryenExpressionRef catchExpr
);
// Inserts a catch expression at the specified index of a `try` expression,
// moving existing catch bodies including the one previously at that index one
// index up.
void BinaryenTryInsertCatchBodyAt(BinaryenExpressionRef expr, BinaryenIndex index, BinaryenExpressionRef catchExpr);
// Removes the catch expression at the specified index of a `try` expression,
// moving all subsequent catch bodies one index down. Returns the catch
// expression.
BinaryenExpressionRef
BinaryenTryRemoveCatchBodyAt(BinaryenExpressionRef expr, BinaryenIndex index);
// Gets whether a `try` expression has a catch_all clause.
_Bool BinaryenTryHasCatchAll(BinaryenExpressionRef expr);
// Gets the target label of a `delegate`.
__const char *
BinaryenTryGetDelegateTarget(BinaryenExpressionRef expr);
// Sets the target label of a `delegate`.
void BinaryenTrySetDelegateTarget(BinaryenExpressionRef expr, __const char *delegateTarget);
// Gets whether a `try` expression is a try-delegate.
_Bool BinaryenTryIsDelegate(BinaryenExpressionRef expr);

// Throw

// Gets the name of the tag being thrown by a `throw` expression.
__const char *BinaryenThrowGetTag(BinaryenExpressionRef expr);
// Sets the name of the tag being thrown by a `throw` expression.
void BinaryenThrowSetTag(BinaryenExpressionRef expr, __const char *tagName);
// Gets the number of operands of a `throw` expression.
BinaryenIndex
BinaryenThrowGetNumOperands(BinaryenExpressionRef expr);
// Gets the operand at the specified index of a `throw` expression.
BinaryenExpressionRef
BinaryenThrowGetOperandAt(BinaryenExpressionRef expr, BinaryenIndex index);
// Sets the operand at the specified index of a `throw` expression.
void BinaryenThrowSetOperandAt(BinaryenExpressionRef expr, BinaryenIndex index, BinaryenExpressionRef operandExpr);
// Appends an operand expression to a `throw` expression, returning its
// insertion index.
BinaryenIndex BinaryenThrowAppendOperand(
    BinaryenExpressionRef expr, BinaryenExpressionRef operandExpr
);
// Inserts an operand expression at the specified index of a `throw` expression,
// moving existing operands including the one previously at that index one index
// up.
void BinaryenThrowInsertOperandAt(BinaryenExpressionRef expr, BinaryenIndex index, BinaryenExpressionRef operandExpr);
// Removes the operand expression at the specified index of a `throw`
// expression, moving all subsequent operands one index down. Returns the
// operand expression.
BinaryenExpressionRef
BinaryenThrowRemoveOperandAt(BinaryenExpressionRef expr, BinaryenIndex index);

// Rethrow

// Gets the target catch's corresponding try label of a `rethrow` expression.
__const char *BinaryenRethrowGetTarget(BinaryenExpressionRef expr);
// Sets the target catch's corresponding try label of a `rethrow` expression.
void BinaryenRethrowSetTarget(BinaryenExpressionRef expr, __const char *target);

// TupleMake

// Gets the number of operands of a `tuple.make` expression.
BinaryenIndex
BinaryenTupleMakeGetNumOperands(BinaryenExpressionRef expr);
// Gets the operand at the specified index of a `tuple.make` expression.
BinaryenExpressionRef
BinaryenTupleMakeGetOperandAt(BinaryenExpressionRef expr, BinaryenIndex index);
// Sets the operand at the specified index of a `tuple.make` expression.
void BinaryenTupleMakeSetOperandAt(BinaryenExpressionRef expr, BinaryenIndex index, BinaryenExpressionRef operandExpr);
// Appends an operand expression to a `tuple.make` expression, returning its
// insertion index.
BinaryenIndex BinaryenTupleMakeAppendOperand(
    BinaryenExpressionRef expr, BinaryenExpressionRef operandExpr
);
// Inserts an operand expression at the specified index of a `tuple.make`
// expression, moving existing operands including the one previously at that
// index one index up.
void BinaryenTupleMakeInsertOperandAt(BinaryenExpressionRef expr, BinaryenIndex index, BinaryenExpressionRef operandExpr);
// Removes the operand expression at the specified index of a `tuple.make`
// expression, moving all subsequent operands one index down. Returns the
// operand expression.
BinaryenExpressionRef BinaryenTupleMakeRemoveOperandAt(
    BinaryenExpressionRef expr, BinaryenIndex index
);

// TupleExtract

// Gets the tuple extracted from of a `tuple.extract` expression.
BinaryenExpressionRef
BinaryenTupleExtractGetTuple(BinaryenExpressionRef expr);
// Sets the tuple extracted from of a `tuple.extract` expression.
void BinaryenTupleExtractSetTuple(BinaryenExpressionRef expr, BinaryenExpressionRef tupleExpr);
// Gets the index extracted at of a `tuple.extract` expression.
BinaryenIndex
BinaryenTupleExtractGetIndex(BinaryenExpressionRef expr);
// Sets the index extracted at of a `tuple.extract` expression.
void BinaryenTupleExtractSetIndex(BinaryenExpressionRef expr, BinaryenIndex index);

// I31New

// Gets the value expression of an `i31.new` expression.
BinaryenExpressionRef
BinaryenI31NewGetValue(BinaryenExpressionRef expr);
// Sets the value expression of an `i31.new` expression.
void BinaryenI31NewSetValue(BinaryenExpressionRef expr, BinaryenExpressionRef valueExpr);

// I31Get

// Gets the i31 expression of an `i31.get` expression.
BinaryenExpressionRef
BinaryenI31GetGetI31(BinaryenExpressionRef expr);
// Sets the i31 expression of an `i31.get` expression.
void BinaryenI31GetSetI31(BinaryenExpressionRef expr, BinaryenExpressionRef i31Expr);
// Gets whether an `i31.get` expression returns a __signed value (`_s`).
_Bool BinaryenI31GetIsSigned(BinaryenExpressionRef expr);
// Sets whether an `i31.get` expression returns a __signed value (`_s`).
void BinaryenI31GetSetSigned(BinaryenExpressionRef expr, _Bool signed_);

// CallRef

BinaryenIndex
BinaryenCallRefGetNumOperands(BinaryenExpressionRef expr);
BinaryenExpressionRef
BinaryenCallRefGetOperandAt(BinaryenExpressionRef expr, BinaryenIndex index);
void BinaryenCallRefSetOperandAt(BinaryenExpressionRef expr, BinaryenIndex index, BinaryenExpressionRef operandExpr);
BinaryenIndex BinaryenCallRefAppendOperand(
    BinaryenExpressionRef expr, BinaryenExpressionRef operandExpr
);
void BinaryenCallRefInsertOperandAt(BinaryenExpressionRef expr, BinaryenIndex index, BinaryenExpressionRef operandExpr);
BinaryenExpressionRef
BinaryenCallRefRemoveOperandAt(BinaryenExpressionRef expr, BinaryenIndex index);
BinaryenExpressionRef
BinaryenCallRefGetTarget(BinaryenExpressionRef expr);
void BinaryenCallRefSetTarget(BinaryenExpressionRef expr, BinaryenExpressionRef targetExpr);
_Bool BinaryenCallRefIsReturn(BinaryenExpressionRef expr);
void BinaryenCallRefSetReturn(BinaryenExpressionRef expr, _Bool isReturn);

// RefTest

BinaryenExpressionRef
BinaryenRefTestGetRef(BinaryenExpressionRef expr);
void BinaryenRefTestSetRef(BinaryenExpressionRef expr, BinaryenExpressionRef refExpr);
BinaryenType
BinaryenRefTestGetCastType(BinaryenExpressionRef expr);
void BinaryenRefTestSetCastType(BinaryenExpressionRef expr, BinaryenType intendedType);

// RefCast

BinaryenExpressionRef
BinaryenRefCastGetRef(BinaryenExpressionRef expr);
void BinaryenRefCastSetRef(BinaryenExpressionRef expr, BinaryenExpressionRef refExpr);

// BrOn

BinaryenOp BinaryenBrOnGetOp(BinaryenExpressionRef expr);
void BinaryenBrOnSetOp(BinaryenExpressionRef expr, BinaryenOp op);
__const char *BinaryenBrOnGetName(BinaryenExpressionRef expr);
void BinaryenBrOnSetName(BinaryenExpressionRef expr, __const char *nameStr);
BinaryenExpressionRef
BinaryenBrOnGetRef(BinaryenExpressionRef expr);
void BinaryenBrOnSetRef(BinaryenExpressionRef expr, BinaryenExpressionRef refExpr);
BinaryenType BinaryenBrOnGetCastType(BinaryenExpressionRef expr);
void BinaryenBrOnSetCastType(BinaryenExpressionRef expr, BinaryenType castType);

// StructNew

BinaryenIndex
BinaryenStructNewGetNumOperands(BinaryenExpressionRef expr);
BinaryenExpressionRef
BinaryenStructNewGetOperandAt(BinaryenExpressionRef expr, BinaryenIndex index);
void BinaryenStructNewSetOperandAt(BinaryenExpressionRef expr, BinaryenIndex index, BinaryenExpressionRef operandExpr);
BinaryenIndex BinaryenStructNewAppendOperand(
    BinaryenExpressionRef expr, BinaryenExpressionRef operandExpr
);
void BinaryenStructNewInsertOperandAt(BinaryenExpressionRef expr, BinaryenIndex index, BinaryenExpressionRef operandExpr);
BinaryenExpressionRef BinaryenStructNewRemoveOperandAt(
    BinaryenExpressionRef expr, BinaryenIndex index
);

// StructGet

BinaryenIndex
BinaryenStructGetGetIndex(BinaryenExpressionRef expr);
void BinaryenStructGetSetIndex(BinaryenExpressionRef expr, BinaryenIndex index);
BinaryenExpressionRef
BinaryenStructGetGetRef(BinaryenExpressionRef expr);
void BinaryenStructGetSetRef(BinaryenExpressionRef expr, BinaryenExpressionRef refExpr);
_Bool BinaryenStructGetIsSigned(BinaryenExpressionRef expr);
void BinaryenStructGetSetSigned(BinaryenExpressionRef expr, _Bool signed_);

// StructSet

BinaryenIndex
BinaryenStructSetGetIndex(BinaryenExpressionRef expr);
void BinaryenStructSetSetIndex(BinaryenExpressionRef expr, BinaryenIndex index);
BinaryenExpressionRef
BinaryenStructSetGetRef(BinaryenExpressionRef expr);
void BinaryenStructSetSetRef(BinaryenExpressionRef expr, BinaryenExpressionRef refExpr);
BinaryenExpressionRef
BinaryenStructSetGetValue(BinaryenExpressionRef expr);
void BinaryenStructSetSetValue(BinaryenExpressionRef expr, BinaryenExpressionRef valueExpr);

// ArrayNew

BinaryenExpressionRef
BinaryenArrayNewGetInit(BinaryenExpressionRef expr);
void BinaryenArrayNewSetInit(BinaryenExpressionRef expr, BinaryenExpressionRef initExpr);
BinaryenExpressionRef
BinaryenArrayNewGetSize(BinaryenExpressionRef expr);
void BinaryenArrayNewSetSize(BinaryenExpressionRef expr, BinaryenExpressionRef sizeExpr);

// ArrayNewFixed

BinaryenIndex
BinaryenArrayNewFixedGetNumValues(BinaryenExpressionRef expr);
BinaryenExpressionRef BinaryenArrayNewFixedGetValueAt(
    BinaryenExpressionRef expr, BinaryenIndex index
);
void BinaryenArrayNewFixedSetValueAt(BinaryenExpressionRef expr, BinaryenIndex index, BinaryenExpressionRef valueExpr);
BinaryenIndex BinaryenArrayNewFixedAppendValue(
    BinaryenExpressionRef expr, BinaryenExpressionRef valueExpr
);
void BinaryenArrayNewFixedInsertValueAt(BinaryenExpressionRef expr, BinaryenIndex index, BinaryenExpressionRef valueExpr);
BinaryenExpressionRef BinaryenArrayNewFixedRemoveValueAt(
    BinaryenExpressionRef expr, BinaryenIndex index
);

// ArrayGet

BinaryenExpressionRef
BinaryenArrayGetGetRef(BinaryenExpressionRef expr);
void BinaryenArrayGetSetRef(BinaryenExpressionRef expr, BinaryenExpressionRef refExpr);
BinaryenExpressionRef
BinaryenArrayGetGetIndex(BinaryenExpressionRef expr);
void BinaryenArrayGetSetIndex(BinaryenExpressionRef expr, BinaryenExpressionRef indexExpr);
_Bool BinaryenArrayGetIsSigned(BinaryenExpressionRef expr);
void BinaryenArrayGetSetSigned(BinaryenExpressionRef expr, _Bool signed_);

// ArraySet

BinaryenExpressionRef
BinaryenArraySetGetRef(BinaryenExpressionRef expr);
void BinaryenArraySetSetRef(BinaryenExpressionRef expr, BinaryenExpressionRef refExpr);
BinaryenExpressionRef
BinaryenArraySetGetIndex(BinaryenExpressionRef expr);
void BinaryenArraySetSetIndex(BinaryenExpressionRef expr, BinaryenExpressionRef indexExpr);
BinaryenExpressionRef
BinaryenArraySetGetValue(BinaryenExpressionRef expr);
void BinaryenArraySetSetValue(BinaryenExpressionRef expr, BinaryenExpressionRef valueExpr);

// ArrayLen

BinaryenExpressionRef
BinaryenArrayLenGetRef(BinaryenExpressionRef expr);
void BinaryenArrayLenSetRef(BinaryenExpressionRef expr, BinaryenExpressionRef refExpr);

// ArrayCopy

BinaryenExpressionRef
BinaryenArrayCopyGetDestRef(BinaryenExpressionRef expr);
void BinaryenArrayCopySetDestRef(BinaryenExpressionRef expr, BinaryenExpressionRef destRefExpr);
BinaryenExpressionRef
BinaryenArrayCopyGetDestIndex(BinaryenExpressionRef expr);
void BinaryenArrayCopySetDestIndex(BinaryenExpressionRef expr, BinaryenExpressionRef destIndexExpr);
BinaryenExpressionRef
BinaryenArrayCopyGetSrcRef(BinaryenExpressionRef expr);
void BinaryenArrayCopySetSrcRef(BinaryenExpressionRef expr, BinaryenExpressionRef srcRefExpr);
BinaryenExpressionRef
BinaryenArrayCopyGetSrcIndex(BinaryenExpressionRef expr);
void BinaryenArrayCopySetSrcIndex(BinaryenExpressionRef expr, BinaryenExpressionRef srcIndexExpr);
BinaryenExpressionRef
BinaryenArrayCopyGetLength(BinaryenExpressionRef expr);
void BinaryenArrayCopySetLength(BinaryenExpressionRef expr, BinaryenExpressionRef lengthExpr);

// StringNew

BinaryenOp BinaryenStringNewGetOp(BinaryenExpressionRef expr);
void BinaryenStringNewSetOp(BinaryenExpressionRef expr, BinaryenOp op);
BinaryenExpressionRef
BinaryenStringNewGetPtr(BinaryenExpressionRef expr);
void BinaryenStringNewSetPtr(BinaryenExpressionRef expr, BinaryenExpressionRef ptrExpr);
BinaryenExpressionRef
BinaryenStringNewGetLength(BinaryenExpressionRef expr);
void BinaryenStringNewSetLength(BinaryenExpressionRef expr, BinaryenExpressionRef lengthExpr);
BinaryenExpressionRef
BinaryenStringNewGetStart(BinaryenExpressionRef expr);
void BinaryenStringNewSetStart(BinaryenExpressionRef expr, BinaryenExpressionRef startExpr);
BinaryenExpressionRef
BinaryenStringNewGetEnd(BinaryenExpressionRef expr);
void BinaryenStringNewSetEnd(BinaryenExpressionRef expr, BinaryenExpressionRef endExpr);
void BinaryenStringNewSetTry(BinaryenExpressionRef expr, _Bool try_);
_Bool BinaryenStringNewIsTry(BinaryenExpressionRef expr);

// StringConst

__const char *
BinaryenStringConstGetString(BinaryenExpressionRef expr);
void BinaryenStringConstSetString(BinaryenExpressionRef expr, __const char *stringStr);

// StringMeasure

BinaryenOp BinaryenStringMeasureGetOp(BinaryenExpressionRef expr);
void BinaryenStringMeasureSetOp(BinaryenExpressionRef expr, BinaryenOp op);
BinaryenExpressionRef
BinaryenStringMeasureGetRef(BinaryenExpressionRef expr);
void BinaryenStringMeasureSetRef(BinaryenExpressionRef expr, BinaryenExpressionRef refExpr);

// StringEncode

BinaryenOp BinaryenStringEncodeGetOp(BinaryenExpressionRef expr);
void BinaryenStringEncodeSetOp(BinaryenExpressionRef expr, BinaryenOp op);
BinaryenExpressionRef
BinaryenStringEncodeGetRef(BinaryenExpressionRef expr);
void BinaryenStringEncodeSetRef(BinaryenExpressionRef expr, BinaryenExpressionRef refExpr);
BinaryenExpressionRef
BinaryenStringEncodeGetPtr(BinaryenExpressionRef expr);
void BinaryenStringEncodeSetPtr(BinaryenExpressionRef expr, BinaryenExpressionRef ptrExpr);
BinaryenExpressionRef
BinaryenStringEncodeGetStart(BinaryenExpressionRef expr);
void BinaryenStringEncodeSetStart(BinaryenExpressionRef expr, BinaryenExpressionRef startExpr);

// StringConcat

BinaryenExpressionRef
BinaryenStringConcatGetLeft(BinaryenExpressionRef expr);
void BinaryenStringConcatSetLeft(BinaryenExpressionRef expr, BinaryenExpressionRef leftExpr);
BinaryenExpressionRef
BinaryenStringConcatGetRight(BinaryenExpressionRef expr);
void BinaryenStringConcatSetRight(BinaryenExpressionRef expr, BinaryenExpressionRef rightExpr);

// StringEq

BinaryenOp BinaryenStringEqGetOp(BinaryenExpressionRef expr);
void BinaryenStringEqSetOp(BinaryenExpressionRef expr, BinaryenOp op);
BinaryenExpressionRef
BinaryenStringEqGetLeft(BinaryenExpressionRef expr);
void BinaryenStringEqSetLeft(BinaryenExpressionRef expr, BinaryenExpressionRef leftExpr);
BinaryenExpressionRef
BinaryenStringEqGetRight(BinaryenExpressionRef expr);
void BinaryenStringEqSetRight(BinaryenExpressionRef expr, BinaryenExpressionRef rightExpr);

// StringAs

BinaryenOp BinaryenStringAsGetOp(BinaryenExpressionRef expr);
void BinaryenStringAsSetOp(BinaryenExpressionRef expr, BinaryenOp op);
BinaryenExpressionRef
BinaryenStringAsGetRef(BinaryenExpressionRef expr);
void BinaryenStringAsSetRef(BinaryenExpressionRef expr, BinaryenExpressionRef refExpr);

// StringWTF8Advance

BinaryenExpressionRef
BinaryenStringWTF8AdvanceGetRef(BinaryenExpressionRef expr);
void BinaryenStringWTF8AdvanceSetRef(BinaryenExpressionRef expr, BinaryenExpressionRef refExpr);
BinaryenExpressionRef
BinaryenStringWTF8AdvanceGetPos(BinaryenExpressionRef expr);
void BinaryenStringWTF8AdvanceSetPos(BinaryenExpressionRef expr, BinaryenExpressionRef posExpr);
BinaryenExpressionRef
BinaryenStringWTF8AdvanceGetBytes(BinaryenExpressionRef expr);
void BinaryenStringWTF8AdvanceSetBytes(BinaryenExpressionRef expr, BinaryenExpressionRef bytesExpr);

// StringWTF16Get

BinaryenExpressionRef
BinaryenStringWTF16GetGetRef(BinaryenExpressionRef expr);
void BinaryenStringWTF16GetSetRef(BinaryenExpressionRef expr, BinaryenExpressionRef refExpr);
BinaryenExpressionRef
BinaryenStringWTF16GetGetPos(BinaryenExpressionRef expr);
void BinaryenStringWTF16GetSetPos(BinaryenExpressionRef expr, BinaryenExpressionRef posExpr);

// StringIterNext

BinaryenExpressionRef
BinaryenStringIterNextGetRef(BinaryenExpressionRef expr);
void BinaryenStringIterNextSetRef(BinaryenExpressionRef expr, BinaryenExpressionRef refExpr);

// StringIterMove

BinaryenOp BinaryenStringIterMoveGetOp(BinaryenExpressionRef expr);
void BinaryenStringIterMoveSetOp(BinaryenExpressionRef expr, BinaryenOp op);
BinaryenExpressionRef
BinaryenStringIterMoveGetRef(BinaryenExpressionRef expr);
void BinaryenStringIterMoveSetRef(BinaryenExpressionRef expr, BinaryenExpressionRef refExpr);
BinaryenExpressionRef
BinaryenStringIterMoveGetNum(BinaryenExpressionRef expr);
void BinaryenStringIterMoveSetNum(BinaryenExpressionRef expr, BinaryenExpressionRef numExpr);

// StringSliceWTF

BinaryenOp BinaryenStringSliceWTFGetOp(BinaryenExpressionRef expr);
void BinaryenStringSliceWTFSetOp(BinaryenExpressionRef expr, BinaryenOp op);
BinaryenExpressionRef
BinaryenStringSliceWTFGetRef(BinaryenExpressionRef expr);
void BinaryenStringSliceWTFSetRef(BinaryenExpressionRef expr, BinaryenExpressionRef refExpr);
BinaryenExpressionRef
BinaryenStringSliceWTFGetStart(BinaryenExpressionRef expr);
void BinaryenStringSliceWTFSetStart(BinaryenExpressionRef expr, BinaryenExpressionRef startExpr);
BinaryenExpressionRef
BinaryenStringSliceWTFGetEnd(BinaryenExpressionRef expr);
void BinaryenStringSliceWTFSetEnd(BinaryenExpressionRef expr, BinaryenExpressionRef endExpr);

// StringSliceIter

BinaryenExpressionRef
BinaryenStringSliceIterGetRef(BinaryenExpressionRef expr);
void BinaryenStringSliceIterSetRef(BinaryenExpressionRef expr, BinaryenExpressionRef refExpr);
BinaryenExpressionRef
BinaryenStringSliceIterGetNum(BinaryenExpressionRef expr);
void BinaryenStringSliceIterSetNum(BinaryenExpressionRef expr, BinaryenExpressionRef numExpr);

// Functions

typedef struct Binaryen##Function *Binaryen##Function##Ref;
;

// Adds a function to the module. This is thread-safe.
// @varTypes: the types of variables. In WebAssembly, vars share
//            an index space with params. In other words, params come from
//            the function type, and vars are provided in this call, and
//            together they are all the locals. The order is first params
//            and then vars, so if you have one param it will be at index
//            0 (and written $0), and if you also have 2 vars they will be
//            at indexes 1 and 2, etc., that is, they share an index space.
BinaryenFunctionRef
BinaryenAddFunction(BinaryenModuleRef module, __const char *name, BinaryenType params, BinaryenType results, BinaryenType *varTypes, BinaryenIndex numVarTypes, BinaryenExpressionRef body);
// Gets a function reference by name. Returns ((void*)0) if the function does not
// exist.
BinaryenFunctionRef BinaryenGetFunction(BinaryenModuleRef module, __const char *name);
// Removes a function by name.
void BinaryenRemoveFunction(BinaryenModuleRef module, __const char *name);

// Gets the number of functions in the module.
BinaryenIndex BinaryenGetNumFunctions(BinaryenModuleRef module);
// Gets the function at the specified index.
BinaryenFunctionRef
BinaryenGetFunctionByIndex(BinaryenModuleRef module, BinaryenIndex index);

// Imports

// These either create a new entity (function/table/memory/etc.) and
// mark it as an import, or, if an entity already exists with internalName then
// the existing entity is turned into an import.

void BinaryenAddFunctionImport(BinaryenModuleRef module, __const char *internalName, __const char *externalModuleName, __const char *externalBaseName, BinaryenType params, BinaryenType results);
void BinaryenAddTableImport(BinaryenModuleRef module, __const char *internalName, __const char *externalModuleName, __const char *externalBaseName);
void BinaryenAddMemoryImport(BinaryenModuleRef module, __const char *internalName, __const char *externalModuleName, __const char *externalBaseName, uint8_t shared);
void BinaryenAddGlobalImport(BinaryenModuleRef module, __const char *internalName, __const char *externalModuleName, __const char *externalBaseName, BinaryenType globalType, _Bool mutable_);
void BinaryenAddTagImport(BinaryenModuleRef module, __const char *internalName, __const char *externalModuleName, __const char *externalBaseName, BinaryenType params, BinaryenType results);

// Memory
typedef struct Binaryen##Memory *Binaryen##Memory##Ref;
;

// Exports

typedef struct Binaryen##Export *Binaryen##Export##Ref;
;

__attribute__((deprecated)) BinaryenExportRef BinaryenAddExport(BinaryenModuleRef module, __const char *internalName, __const char *externalName);
// Adds a function export to the module.
BinaryenExportRef BinaryenAddFunctionExport(
    BinaryenModuleRef module, __const char *internalName, __const char *externalName
);
// Adds a table export to the module.
BinaryenExportRef BinaryenAddTableExport(BinaryenModuleRef module, __const char *internalName, __const char *externalName);
// Adds a memory export to the module.
BinaryenExportRef BinaryenAddMemoryExport(
    BinaryenModuleRef module, __const char *internalName, __const char *externalName
);
// Adds a global export to the module.
BinaryenExportRef BinaryenAddGlobalExport(
    BinaryenModuleRef module, __const char *internalName, __const char *externalName
);
// Adds a tag export to the module.
BinaryenExportRef BinaryenAddTagExport(BinaryenModuleRef module, __const char *internalName, __const char *externalName);
// Gets an export reference by external name. Returns ((void*)0) if the export does
// not exist.
BinaryenExportRef BinaryenGetExport(BinaryenModuleRef module, __const char *externalName);
// Removes an export by external name.
void BinaryenRemoveExport(BinaryenModuleRef module, __const char *externalName);
// Gets the number of exports in the module.
BinaryenIndex BinaryenGetNumExports(BinaryenModuleRef module);
// Gets the export at the specified index.
BinaryenExportRef
BinaryenGetExportByIndex(BinaryenModuleRef module, BinaryenIndex index);

// Globals

typedef struct Binaryen##Global *Binaryen##Global##Ref;
;

// Adds a global to the module.
BinaryenGlobalRef BinaryenAddGlobal(BinaryenModuleRef module, __const char *name, BinaryenType type, _Bool mutable_, BinaryenExpressionRef init);
// Gets a global reference by name. Returns ((void*)0) if the global does not exist.
BinaryenGlobalRef BinaryenGetGlobal(BinaryenModuleRef module, __const char *name);
// Removes a global by name.
void BinaryenRemoveGlobal(BinaryenModuleRef module, __const char *name);
// Gets the number of globals in the module.
BinaryenIndex BinaryenGetNumGlobals(BinaryenModuleRef module);
// Gets the global at the specified index.
BinaryenGlobalRef
BinaryenGetGlobalByIndex(BinaryenModuleRef module, BinaryenIndex index);

// Tags

typedef struct Binaryen##Tag *Binaryen##Tag##Ref;
;

// Adds a tag to the module.
BinaryenTagRef BinaryenAddTag(BinaryenModuleRef module, __const char *name, BinaryenType params, BinaryenType results);
// Gets a tag reference by name. Returns ((void*)0) if the tag does not exist.
BinaryenTagRef BinaryenGetTag(BinaryenModuleRef module, __const char *name);
// Removes a tag by name.
void BinaryenRemoveTag(BinaryenModuleRef module, __const char *name);

// Tables

typedef struct Binaryen##Table *Binaryen##Table##Ref;
;

BinaryenTableRef BinaryenAddTable(BinaryenModuleRef module, __const char *table, BinaryenIndex initial, BinaryenIndex maximum, BinaryenType tableType);
void BinaryenRemoveTable(BinaryenModuleRef module, __const char *table);
BinaryenIndex BinaryenGetNumTables(BinaryenModuleRef module);
BinaryenTableRef BinaryenGetTable(BinaryenModuleRef module, __const char *name);
BinaryenTableRef BinaryenGetTableByIndex(BinaryenModuleRef module, BinaryenIndex index);

// Elem segments

typedef struct Binaryen##ElementSegment *Binaryen##ElementSegment##Ref;
;

BinaryenElementSegmentRef
BinaryenAddActiveElementSegment(BinaryenModuleRef module, __const char *table, __const char *name, __const char **funcNames, BinaryenIndex numFuncNames, BinaryenExpressionRef offset);
BinaryenElementSegmentRef
BinaryenAddPassiveElementSegment(BinaryenModuleRef module, __const char *name, __const char **funcNames, BinaryenIndex numFuncNames);
void BinaryenRemoveElementSegment(BinaryenModuleRef module, __const char *name);
BinaryenIndex
BinaryenGetNumElementSegments(BinaryenModuleRef module);
BinaryenElementSegmentRef
BinaryenGetElementSegment(BinaryenModuleRef module, __const char *name);
BinaryenElementSegmentRef
BinaryenGetElementSegmentByIndex(BinaryenModuleRef module, BinaryenIndex index);

// This will create a memory, overwriting any existing memory
// Each memory has data in segments, a start offset in segmentOffsets, and a
// size in segmentSizes. exportName can be ((void*)0)
void BinaryenSetMemory(BinaryenModuleRef module, BinaryenIndex initial, BinaryenIndex maximum, __const char *exportName, __const char **segments, _Bool *segmentPassive, BinaryenExpressionRef *segmentOffsets, BinaryenIndex *segmentSizes, BinaryenIndex numSegments, _Bool shared, _Bool memory64, __const char *name);

_Bool BinaryenHasMemory(BinaryenModuleRef module);
BinaryenIndex BinaryenMemoryGetInitial(BinaryenModuleRef module, __const char *name);
_Bool BinaryenMemoryHasMax(BinaryenModuleRef module, __const char *name);
BinaryenIndex BinaryenMemoryGetMax(BinaryenModuleRef module, __const char *name);
__const char *BinaryenMemoryImportGetModule(BinaryenModuleRef module, __const char *name);
__const char *BinaryenMemoryImportGetBase(BinaryenModuleRef module, __const char *name);
_Bool BinaryenMemoryIsShared(BinaryenModuleRef module, __const char *name);
_Bool BinaryenMemoryIs64(BinaryenModuleRef module, __const char *name);

// Memory segments. Query utilities.

uint32_t BinaryenGetNumMemorySegments(BinaryenModuleRef module);
uint32_t
BinaryenGetMemorySegmentByteOffset(BinaryenModuleRef module, BinaryenIndex id);
size_t BinaryenGetMemorySegmentByteLength(BinaryenModuleRef module, BinaryenIndex id);
_Bool BinaryenGetMemorySegmentPassive(BinaryenModuleRef module, BinaryenIndex id);
void BinaryenCopyMemorySegmentData(BinaryenModuleRef module, BinaryenIndex id, char *buffer);

// Start function. One per module

void BinaryenSetStart(BinaryenModuleRef module, BinaryenFunctionRef start);

// Features

// These control what features are allowed when validation and in passes.
BinaryenFeatures
BinaryenModuleGetFeatures(BinaryenModuleRef module);
void BinaryenModuleSetFeatures(BinaryenModuleRef module, BinaryenFeatures features);

//
// ========== Module Operations ==========
//

// Parse a module in s-expression text format
BinaryenModuleRef BinaryenModuleParse(__const char *text);

// Print a module to stdout in s-expression text format. Useful for debugging.
void BinaryenModulePrint(BinaryenModuleRef module);

// Print a module to stdout in stack IR text format. Useful for debugging.
void BinaryenModulePrintStackIR(BinaryenModuleRef module, _Bool optimize);

// Print a module to stdout in asm.js syntax.
void BinaryenModulePrintAsmjs(BinaryenModuleRef module);

// Validate a module, showing errors on problems.
//  @return 0 if an error occurred, 1 if validated succesfully
_Bool BinaryenModuleValidate(BinaryenModuleRef module);

// Runs the standard optimization passes on the module. Uses the currently set
// global optimize and shrink level.
void BinaryenModuleOptimize(BinaryenModuleRef module);

// Updates the internal name mapping logic in a module. This must be called
// after renaming module elements.
void BinaryenModuleUpdateMaps(BinaryenModuleRef module);

// Gets the currently set optimize level. Applies to all modules, globally.
// 0, 1, 2 correspond to -O0, -O1, -O2 (default), etc.
int BinaryenGetOptimizeLevel(void);

// Sets the optimization level to use. Applies to all modules, globally.
// 0, 1, 2 correspond to -O0, -O1, -O2 (default), etc.
void BinaryenSetOptimizeLevel(int level);

// Gets the currently set shrink level. Applies to all modules, globally.
// 0, 1, 2 correspond to -O0, -Os (default), -Oz.
int BinaryenGetShrinkLevel(void);

// Sets the shrink level to use. Applies to all modules, globally.
// 0, 1, 2 correspond to -O0, -Os (default), -Oz.
void BinaryenSetShrinkLevel(int level);

// Gets whether generating debug information is currently enabled or not.
// Applies to all modules, globally.
_Bool BinaryenGetDebugInfo(void);

// Enables or disables debug information in emitted binaries.
// Applies to all modules, globally.
void BinaryenSetDebugInfo(_Bool on);

// Gets whether the low 1K of memory can be considered unused when optimizing.
// Applies to all modules, globally.
_Bool BinaryenGetLowMemoryUnused(void);

// Enables or disables whether the low 1K of memory can be considered unused
// when optimizing. Applies to all modules, globally.
void BinaryenSetLowMemoryUnused(_Bool on);

// Gets whether to assume that an imported memory is zero-initialized.
_Bool BinaryenGetZeroFilledMemory(void);

// Enables or disables whether to assume that an imported memory is
// zero-initialized.
void BinaryenSetZeroFilledMemory(_Bool on);

// Gets whether fast math optimizations are enabled, ignoring for example
// corner cases of floating-point math like NaN changes.
// Applies to all modules, globally.
_Bool BinaryenGetFastMath(void);

// Enables or disables fast math optimizations, ignoring for example
// corner cases of floating-point math like NaN changes.
// Applies to all modules, globally.
void BinaryenSetFastMath(_Bool value);

// Gets the value of the specified arbitrary pass argument.
// Applies to all modules, globally.
__const char *BinaryenGetPassArgument(__const char *name);

// Sets the value of the specified arbitrary pass argument. Removes the
// respective argument if `value` is ((void*)0). Applies to all modules, globally.
void BinaryenSetPassArgument(__const char *name, __const char *value);

// Clears all arbitrary pass arguments.
// Applies to all modules, globally.
void BinaryenClearPassArguments();

// Gets the function size at which we always __inline.
// Applies to all modules, globally.
BinaryenIndex BinaryenGetAlwaysInlineMaxSize(void);

// Sets the function size at which we always __inline.
// Applies to all modules, globally.
void BinaryenSetAlwaysInlineMaxSize(BinaryenIndex size);

// Gets the function size which we __inline when functions are lightweight.
// Applies to all modules, globally.
BinaryenIndex BinaryenGetFlexibleInlineMaxSize(void);

// Sets the function size which we __inline when functions are lightweight.
// Applies to all modules, globally.
void BinaryenSetFlexibleInlineMaxSize(BinaryenIndex size);

// Gets the function size which we __inline when there is only one caller.
// Applies to all modules, globally.
BinaryenIndex BinaryenGetOneCallerInlineMaxSize(void);

// Sets the function size which we __inline when there is only one caller.
// Applies to all modules, globally.
void BinaryenSetOneCallerInlineMaxSize(BinaryenIndex size);

// Gets whether functions with loops are allowed to be inlined.
// Applies to all modules, globally.
_Bool BinaryenGetAllowInliningFunctionsWithLoops(void);

// Sets whether functions with loops are allowed to be inlined.
// Applies to all modules, globally.
void BinaryenSetAllowInliningFunctionsWithLoops(_Bool enabled);

// Runs the specified passes on the module. Uses the currently set global
// optimize and shrink level.
void BinaryenModuleRunPasses(BinaryenModuleRef module, __const char **passes, BinaryenIndex numPasses);

// Auto-generate drop() operations where needed. This lets you generate code
// without worrying about where they are needed. (It is more efficient to do it
// yourself, but simpler to use autodrop).
void BinaryenModuleAutoDrop(BinaryenModuleRef module);

// Serialize a module into binary form. Uses the currently set global debugInfo
// option.
// @return how many bytes were written. This will be less than or equal to
//         outputSize
size_t BinaryenModuleWrite(BinaryenModuleRef module, char *output, size_t outputSize);

// Serialize a module in s-expression text format.
// @return how many bytes were written. This will be less than or equal to
//         outputSize
size_t BinaryenModuleWriteText(BinaryenModuleRef module, char *output, size_t outputSize);

// Serialize a module in stack IR text format.
// @return how many bytes were written. This will be less than or equal to
//         outputSize
size_t BinaryenModuleWriteStackIR(BinaryenModuleRef module, char *output, size_t outputSize, _Bool optimize);

typedef struct BinaryenBufferSizes {
  size_t outputBytes;
  size_t sourceMapBytes;
} BinaryenBufferSizes;

// Serialize a module into binary form including its source map. Uses the
// currently set global debugInfo option.
// @returns how many bytes were written. This will be less than or equal to
//          outputSize
BinaryenBufferSizes
BinaryenModuleWriteWithSourceMap(BinaryenModuleRef module, __const char *url, char *output, size_t outputSize, char *sourceMap, size_t sourceMapSize);

// Result structure of BinaryenModuleAllocateAndWrite. Contained buffers have
// been allocated using malloc() and the user is expected to free() them
// manually once not needed anymore.
typedef struct BinaryenModuleAllocateAndWriteResult {
  void *binary;
  size_t binaryBytes;
  char *sourceMap;
} BinaryenModuleAllocateAndWriteResult;

// Serializes a module into binary form, optionally including its source map if
// sourceMapUrl has been specified. Uses the currently set global debugInfo
// option. Differs from BinaryenModuleWrite in that it implicitly allocates
// appropriate buffers using malloc(), and expects the user to free() them
// manually once not needed anymore.
BinaryenModuleAllocateAndWriteResult
BinaryenModuleAllocateAndWrite(BinaryenModuleRef module, __const char *sourceMapUrl);

// Serialize a module in s-expression form. Implicity allocates the returned
// char* with malloc(), and expects the user to free() them manually
// once not needed anymore.
char *BinaryenModuleAllocateAndWriteText(BinaryenModuleRef module);

// Serialize a module in stack IR form. Implicitly allocates the returned
// char* with malloc(), and expects the user to free() them manually
// once not needed anymore.
char *
BinaryenModuleAllocateAndWriteStackIR(BinaryenModuleRef module, _Bool optimize);

// Deserialize a module from binary form.
BinaryenModuleRef BinaryenModuleRead(char *input, size_t inputSize);

// Execute a module in the Binaryen interpreter. This will create an instance of
// the module, run it in the interpreter - which means running the start method
// - and then destroying the instance.
void BinaryenModuleInterpret(BinaryenModuleRef module);

// Adds a debug info file name to the module and returns its index.
BinaryenIndex BinaryenModuleAddDebugInfoFileName(
    BinaryenModuleRef module, __const char *filename
);

// Gets the name of the debug info file at the specified index. Returns `((void*)0)`
// if it does not exist.
__const char *
BinaryenModuleGetDebugInfoFileName(BinaryenModuleRef module, BinaryenIndex index);

//
// ========== Function Operations ==========
//

// Gets the name of the specified `Function`.
__const char *BinaryenFunctionGetName(BinaryenFunctionRef func);
// Gets the type of the parameter at the specified index of the specified
// `Function`.
BinaryenType BinaryenFunctionGetParams(BinaryenFunctionRef func);
// Gets the result type of the specified `Function`.
BinaryenType BinaryenFunctionGetResults(BinaryenFunctionRef func);
// Gets the number of additional locals within the specified `Function`.
BinaryenIndex BinaryenFunctionGetNumVars(BinaryenFunctionRef func);
// Gets the type of the additional local at the specified index within the
// specified `Function`.
BinaryenType BinaryenFunctionGetVar(BinaryenFunctionRef func, BinaryenIndex index);
// Gets the number of locals within the specified function. Includes parameters.
BinaryenIndex
BinaryenFunctionGetNumLocals(BinaryenFunctionRef func);
// Tests if the local at the specified index has a name.
_Bool BinaryenFunctionHasLocalName(BinaryenFunctionRef func, BinaryenIndex index);
// Gets the name of the local at the specified index.
__const char *BinaryenFunctionGetLocalName(BinaryenFunctionRef func, BinaryenIndex index);
// Sets the name of the local at the specified index.
void BinaryenFunctionSetLocalName(BinaryenFunctionRef func, BinaryenIndex index, __const char *name);
// Gets the body of the specified `Function`.
BinaryenExpressionRef
BinaryenFunctionGetBody(BinaryenFunctionRef func);
// Sets the body of the specified `Function`.
void BinaryenFunctionSetBody(BinaryenFunctionRef func, BinaryenExpressionRef body);

// Runs the standard optimization passes on the function. Uses the currently set
// global optimize and shrink level.
void BinaryenFunctionOptimize(BinaryenFunctionRef func, BinaryenModuleRef module);

// Runs the specified passes on the function. Uses the currently set global
// optimize and shrink level.
void BinaryenFunctionRunPasses(BinaryenFunctionRef func, BinaryenModuleRef module, __const char **passes, BinaryenIndex numPasses);

// Sets the debug location of the specified `Expression` within the specified
// `Function`.
void BinaryenFunctionSetDebugLocation(BinaryenFunctionRef func, BinaryenExpressionRef expr, BinaryenIndex fileIndex, BinaryenIndex lineNumber, BinaryenIndex columnNumber);

//
// ========== Table Operations ==========
//

// Gets the name of the specified `Table`.
__const char *BinaryenTableGetName(BinaryenTableRef table);
// Sets the name of the specified `Table`.
void BinaryenTableSetName(BinaryenTableRef table, __const char *name);
// Gets the initial number of pages of the specified `Table`.
BinaryenIndex BinaryenTableGetInitial(BinaryenTableRef table);
// Sets the initial number of pages of the specified `Table`.
void BinaryenTableSetInitial(BinaryenTableRef table, BinaryenIndex initial);
// Tests whether the specified `Table` has a maximum number of pages.
_Bool BinaryenTableHasMax(BinaryenTableRef table);
// Gets the maximum number of pages of the specified `Table`.
BinaryenIndex BinaryenTableGetMax(BinaryenTableRef table);
// Sets the maximum number of pages of the specified `Table`.
void BinaryenTableSetMax(BinaryenTableRef table, BinaryenIndex max);

//
// ========== Elem Segment Operations ==========
//

// Gets the name of the specified `ElementSegment`.
__const char *
BinaryenElementSegmentGetName(BinaryenElementSegmentRef elem);
// Sets the name of the specified `ElementSegment`.
void BinaryenElementSegmentSetName(BinaryenElementSegmentRef elem, __const char *name);
// Gets the table name of the specified `ElementSegment`.
__const char *
BinaryenElementSegmentGetTable(BinaryenElementSegmentRef elem);
// Sets the table name of the specified `ElementSegment`.
void BinaryenElementSegmentSetTable(BinaryenElementSegmentRef elem, __const char *table);
// Gets the segment offset in case of active segments
BinaryenExpressionRef
BinaryenElementSegmentGetOffset(BinaryenElementSegmentRef elem);
// Gets the length of items in the segment
BinaryenIndex
BinaryenElementSegmentGetLength(BinaryenElementSegmentRef elem);
// Gets the item at the specified index
__const char *
BinaryenElementSegmentGetData(BinaryenElementSegmentRef elem, BinaryenIndex dataId);
// Returns 1 if the specified elem segment is passive
_Bool BinaryenElementSegmentIsPassive(BinaryenElementSegmentRef elem);

//
// ========== Global Operations ==========
//

// Gets the name of the specified `Global`.
__const char *BinaryenGlobalGetName(BinaryenGlobalRef global);
// Gets the name of the `GlobalType` associated with the specified `Global`. May
// be `((void*)0)` if the signature is implicit.
BinaryenType BinaryenGlobalGetType(BinaryenGlobalRef global);
// Returns 1 if the specified `Global` is mutable.
_Bool BinaryenGlobalIsMutable(BinaryenGlobalRef global);
// Gets the initialization expression of the specified `Global`.
BinaryenExpressionRef
BinaryenGlobalGetInitExpr(BinaryenGlobalRef global);

//
// ========== Tag Operations ==========
//

// Gets the name of the specified `Tag`.
__const char *BinaryenTagGetName(BinaryenTagRef tag);
// Gets the parameters type of the specified `Tag`.
BinaryenType BinaryenTagGetParams(BinaryenTagRef tag);
// Gets the results type of the specified `Tag`.
BinaryenType BinaryenTagGetResults(BinaryenTagRef tag);

//
// ========== Import Operations ==========
//

// Gets the external module name of the specified import.
__const char *
BinaryenFunctionImportGetModule(BinaryenFunctionRef import);
__const char *BinaryenTableImportGetModule(BinaryenTableRef import);
__const char *
BinaryenGlobalImportGetModule(BinaryenGlobalRef import);
__const char *BinaryenTagImportGetModule(BinaryenTagRef import);
// Gets the external base name of the specified import.
__const char *
BinaryenFunctionImportGetBase(BinaryenFunctionRef import);
__const char *BinaryenTableImportGetBase(BinaryenTableRef import);
__const char *BinaryenGlobalImportGetBase(BinaryenGlobalRef import);
__const char *BinaryenTagImportGetBase(BinaryenTagRef import);

//
// ========== Export Operations ==========
//

// Gets the external kind of the specified export.
BinaryenExternalKind
BinaryenExportGetKind(BinaryenExportRef export_);
// Gets the external name of the specified export.
__const char *BinaryenExportGetName(BinaryenExportRef export_);
// Gets the internal name of the specified export.
__const char *BinaryenExportGetValue(BinaryenExportRef export_);

//
// ========= Custom sections =========
//

void BinaryenAddCustomSection(BinaryenModuleRef module, __const char *name, __const char *contents, BinaryenIndex contentsSize);

//
// ========= Effect analyzer =========
//

typedef uint32_t BinaryenSideEffects;

BinaryenSideEffects BinaryenSideEffectNone(void);
BinaryenSideEffects BinaryenSideEffectBranches(void);
BinaryenSideEffects BinaryenSideEffectCalls(void);
BinaryenSideEffects BinaryenSideEffectReadsLocal(void);
BinaryenSideEffects BinaryenSideEffectWritesLocal(void);
BinaryenSideEffects BinaryenSideEffectReadsGlobal(void);
BinaryenSideEffects BinaryenSideEffectWritesGlobal(void);
BinaryenSideEffects BinaryenSideEffectReadsMemory(void);
BinaryenSideEffects BinaryenSideEffectWritesMemory(void);
BinaryenSideEffects BinaryenSideEffectReadsTable(void);
BinaryenSideEffects BinaryenSideEffectWritesTable(void);
BinaryenSideEffects BinaryenSideEffectImplicitTrap(void);
BinaryenSideEffects BinaryenSideEffectTrapsNeverHappen(void);
BinaryenSideEffects BinaryenSideEffectIsAtomic(void);
BinaryenSideEffects BinaryenSideEffectThrows(void);
BinaryenSideEffects BinaryenSideEffectDanglingPop(void);
BinaryenSideEffects BinaryenSideEffectAny(void);

BinaryenSideEffects BinaryenExpressionGetSideEffects(
    BinaryenExpressionRef expr, BinaryenModuleRef module
);

//
// ========== CFG / Relooper ==========
//
// General usage is (1) create a relooper, (2) create blocks, (3) add
// branches between them, (4) render the output.
//
// For more details, see src/cfg/Relooper.h and
// https://github.com/WebAssembly/binaryen/wiki/Compiling-to-WebAssembly-with-Binaryen#cfg-api

typedef struct Relooper *RelooperRef;
typedef struct RelooperBlock *RelooperBlockRef;

// Create a relooper instance
RelooperRef RelooperCreate(BinaryenModuleRef module);

// Create a basic block that ends with nothing, or with some simple branching
RelooperBlockRef RelooperAddBlock(RelooperRef relooper, BinaryenExpressionRef code);

// Create a branch to another basic block
// The branch can have code on it, that is executed as the branch happens. this
// is useful for phis. otherwise, code can be ((void*)0)
void RelooperAddBranch(RelooperBlockRef from, RelooperBlockRef to, BinaryenExpressionRef condition, BinaryenExpressionRef code);

// Create a basic block that ends a switch on a condition
RelooperBlockRef
RelooperAddBlockWithSwitch(RelooperRef relooper, BinaryenExpressionRef code, BinaryenExpressionRef condition);

// Create a switch-style branch to another basic block. The block's switch table
// will have these indexes going to that target
void RelooperAddBranchForSwitch(RelooperBlockRef from, RelooperBlockRef to, BinaryenIndex *indexes, BinaryenIndex numIndexes, BinaryenExpressionRef code);

// Generate structed wasm control flow from the CFG of blocks and branches that
// were created on this relooper instance. This returns the rendered output, and
// also disposes of the relooper and its blocks and branches, as they are no
// longer needed.
// @param labelHelper To render irreducible control flow, we may need a helper
//        variable to guide us to the right target label. This value should be
//        an index of an i32 local variable that is free for us to use.
BinaryenExpressionRef RelooperRenderAndDispose(
    RelooperRef relooper, RelooperBlockRef entry, BinaryenIndex labelHelper
);

//
// ========= ExpressionRunner ==========
//

typedef struct CExpressionRunner *ExpressionRunnerRef;

typedef uint32_t ExpressionRunnerFlags;

// By default, just evaluate the expression, i.e. all we want to know is whether
// it computes down to a concrete value, where it is not necessary to preserve
// side effects like those of a `local.tee`.
ExpressionRunnerFlags ExpressionRunnerFlagsDefault();

// Be very careful to preserve any side effects. For example, if we are
// intending to replace the expression with a constant afterwards, even if we
// can technically evaluate down to a constant, we still cannot replace the
// expression if it also sets a local, which must be preserved in this scenario
// so subsequent code keeps functioning.
ExpressionRunnerFlags ExpressionRunnerFlagsPreserveSideeffects();

// Traverse through function calls, attempting to compute their concrete value.
// Must not be used in function-parallel scenarios, where the called function
// might be concurrently modified, leading to undefined behavior. Traversing
// another function reuses all of this runner's flags.
ExpressionRunnerFlags ExpressionRunnerFlagsTraverseCalls();

// Creates an ExpressionRunner instance
ExpressionRunnerRef
ExpressionRunnerCreate(BinaryenModuleRef module, ExpressionRunnerFlags flags, BinaryenIndex maxDepth, BinaryenIndex maxLoopIterations);

// Sets a known local value to use. Order matters if expressions have side
// effects. For example, if the expression also sets a local, this side effect
// will also happen (not affected by any flags). Returns `1` if the
// expression actually evaluates to a constant.
_Bool ExpressionRunnerSetLocalValue(ExpressionRunnerRef runner, BinaryenIndex index, BinaryenExpressionRef value);

// Sets a known global value to use. Order matters if expressions have side
// effects. For example, if the expression also sets a local, this side effect
// will also happen (not affected by any flags). Returns `1` if the
// expression actually evaluates to a constant.
_Bool ExpressionRunnerSetGlobalValue(ExpressionRunnerRef runner, __const char *name, BinaryenExpressionRef value);

// Runs the expression and returns the constant value expression it evaluates
// to, if any. Otherwise returns `((void*)0)`. Also disposes the runner.
BinaryenExpressionRef ExpressionRunnerRunAndDispose(
    ExpressionRunnerRef runner, BinaryenExpressionRef expr
);

//
// ========= TypeBuilder =========
//

typedef struct TypeBuilder *TypeBuilderRef;

typedef uint32_t TypeBuilderErrorReason;

// Indicates a cycle in the supertype relation.
TypeBuilderErrorReason TypeBuilderErrorReasonSelfSupertype(void);
// Indicates that the declared supertype of a type is invalid.
TypeBuilderErrorReason
TypeBuilderErrorReasonInvalidSupertype(void);
// Indicates that the declared supertype is an invalid forward reference.
TypeBuilderErrorReason
TypeBuilderErrorReasonForwardSupertypeReference(void);
// Indicates that a child of a type is an invalid forward reference.
TypeBuilderErrorReason
TypeBuilderErrorReasonForwardChildReference(void);

typedef uint32_t BinaryenBasicHeapType;

// Constructs a new type builder that allows for the construction of recursive
// types. Contains a table of `size` mutable heap types.
TypeBuilderRef TypeBuilderCreate(BinaryenIndex size);
// Grows the backing table of the type builder by `count` slots.
void TypeBuilderGrow(TypeBuilderRef builder, BinaryenIndex count);
// Gets the size of the backing table of the type builder.
BinaryenIndex TypeBuilderGetSize(TypeBuilderRef builder);
// Sets the heap type at index `index` to a concrete signature type. Expects
// temporary tuple types if multiple parameter and/or result types include
// temporary types.
void TypeBuilderSetSignatureType(TypeBuilderRef builder, BinaryenIndex index, BinaryenType paramTypes, BinaryenType resultTypes);
// Sets the heap type at index `index` to a concrete struct type.
void TypeBuilderSetStructType(TypeBuilderRef builder, BinaryenIndex index, BinaryenType *fieldTypes, BinaryenPackedType *fieldPackedTypes, _Bool *fieldMutables, int numFields);
// Sets the heap type at index `index` to a concrete array type.
void TypeBuilderSetArrayType(TypeBuilderRef builder, BinaryenIndex index, BinaryenType elementType, BinaryenPackedType elementPackedType, int elementMutable);
// Gets the temporary heap type to use at index `index`. Temporary heap types
// may only be used to construct temporary types using the type builder.
BinaryenHeapType TypeBuilderGetTempHeapType(TypeBuilderRef builder, BinaryenIndex index);
// Gets a temporary tuple type for use with and owned by the type builder.
BinaryenType TypeBuilderGetTempTupleType(TypeBuilderRef builder, BinaryenType *types, BinaryenIndex numTypes);
// Gets a temporary reference type for use with and owned by the type builder.
BinaryenType TypeBuilderGetTempRefType(TypeBuilderRef builder, BinaryenHeapType heapType, int nullable);
// Sets the type at `index` to be a subtype of the given super type.
void TypeBuilderSetSubType(TypeBuilderRef builder, BinaryenIndex index, BinaryenHeapType superType);
// Creates a new recursion group in the range `index` inclusive to `index +
// length` exclusive. Recursion groups must not overlap.
void TypeBuilderCreateRecGroup(TypeBuilderRef builder, BinaryenIndex index, BinaryenIndex length);
// Builds the heap type hierarchy and disposes the builder. Returns `0` and
// populates `errorIndex` and `errorReason` on failure.
_Bool TypeBuilderBuildAndDispose(TypeBuilderRef builder, BinaryenHeapType *heapTypes, BinaryenIndex *errorIndex, TypeBuilderErrorReason *errorReason);

// Sets the textual name of a compound `heapType`. Has no effect if the type
// already has a canonical name.
void BinaryenModuleSetTypeName(BinaryenModuleRef module, BinaryenHeapType heapType, __const char *name);
// Sets the field name of a struct `heapType` at index `index`.
void BinaryenModuleSetFieldName(BinaryenModuleRef module, BinaryenHeapType heapType, BinaryenIndex index, __const char *name);

//
// ========= Utilities =========
//

// Enable or disable coloring for the Wasm printer
void BinaryenSetColorsEnabled(_Bool enabled);

// Query whether color is enable for the Wasm printer
_Bool BinaryenAreColorsEnabled();
