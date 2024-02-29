from enum import Flag

from ._binaryen import lib


class Feature(Flag):
    MVP = lib.BinaryenFeatureMVP()
    Atomics = lib.BinaryenFeatureAtomics()
    BulkMemory = lib.BinaryenFeatureBulkMemory()
    MutableGlobals = lib.BinaryenFeatureMutableGlobals()
    NontrappingFPToInt = lib.BinaryenFeatureNontrappingFPToInt()
    SignExt = lib.BinaryenFeatureSignExt()
    SIMD128 = lib.BinaryenFeatureSIMD128()
    ExceptionHandling = lib.BinaryenFeatureExceptionHandling()
    TailCall = lib.BinaryenFeatureTailCall()
    ReferenceTypes = lib.BinaryenFeatureReferenceTypes()
    Multivalue = lib.BinaryenFeatureMultivalue()
    GC = lib.BinaryenFeatureGC()
    Memory64 = lib.BinaryenFeatureMemory64()
    RelaxedSIMD = lib.BinaryenFeatureRelaxedSIMD()
    ExtendedConst = lib.BinaryenFeatureExtendedConst()
    Strings = lib.BinaryenFeatureStrings()
    MultiMemory = lib.BinaryenFeatureMultiMemory()
    All = lib.BinaryenFeatureAll()
