from ._binaryen import lib as __lib
from .internals import BinaryenOp as __Op

# Vim Macro
# 8ly$0iTabreturn __lib.EscOdef EscpA:EscjoEscj0


def CtzInt32() -> __Op:
    return __lib.BinaryenCtzInt32()


def PopcntInt32() -> __Op:
    return __lib.BinaryenPopcntInt32()


def NegFloat32() -> __Op:
    return __lib.BinaryenNegFloat32()


def AbsFloat32() -> __Op:
    return __lib.BinaryenAbsFloat32()


def CeilFloat32() -> __Op:
    return __lib.BinaryenCeilFloat32()


def FloorFloat32() -> __Op:
    return __lib.BinaryenFloorFloat32()


def TruncFloat32() -> __Op:
    return __lib.BinaryenTruncFloat32()


def NearestFloat32() -> __Op:
    return __lib.BinaryenNearestFloat32()


def SqrtFloat32() -> __Op:
    return __lib.BinaryenSqrtFloat32()


def EqZInt32() -> __Op:
    return __lib.BinaryenEqZInt32()


def ClzInt64() -> __Op:
    return __lib.BinaryenClzInt64()


def CtzInt64() -> __Op:
    return __lib.BinaryenCtzInt64()


def PopcntInt64() -> __Op:
    return __lib.BinaryenPopcntInt64()


def NegFloat64() -> __Op:
    return __lib.BinaryenNegFloat64()


def AbsFloat64() -> __Op:
    return __lib.BinaryenAbsFloat64()


def CeilFloat64() -> __Op:
    return __lib.BinaryenCeilFloat64()


def FloorFloat64() -> __Op:
    return __lib.BinaryenFloorFloat64()


def TruncFloat64() -> __Op:
    return __lib.BinaryenTruncFloat64()


def NearestFloat64() -> __Op:
    return __lib.BinaryenNearestFloat64()


def SqrtFloat64() -> __Op:
    return __lib.BinaryenSqrtFloat64()


def EqZInt64() -> __Op:
    return __lib.BinaryenEqZInt64()


def ExtendSInt32() -> __Op:
    return __lib.BinaryenExtendSInt32()


def ExtendUInt32() -> __Op:
    return __lib.BinaryenExtendUInt32()


def WrapInt64() -> __Op:
    return __lib.BinaryenWrapInt64()


def TruncSFloat32ToInt32() -> __Op:
    return __lib.BinaryenTruncSFloat32ToInt32()


def TruncSFloat32ToInt64() -> __Op:
    return __lib.BinaryenTruncSFloat32ToInt64()


def TruncUFloat32ToInt32() -> __Op:
    return __lib.BinaryenTruncUFloat32ToInt32()


def TruncUFloat32ToInt64() -> __Op:
    return __lib.BinaryenTruncUFloat32ToInt64()


def TruncSFloat64ToInt32() -> __Op:
    return __lib.BinaryenTruncSFloat64ToInt32()


def TruncSFloat64ToInt64() -> __Op:
    return __lib.BinaryenTruncSFloat64ToInt64()


def TruncUFloat64ToInt32() -> __Op:
    return __lib.BinaryenTruncUFloat64ToInt32()


def TruncUFloat64ToInt64() -> __Op:
    return __lib.BinaryenTruncUFloat64ToInt64()


def ReinterpretFloat32() -> __Op:
    return __lib.BinaryenReinterpretFloat32()


def ReinterpretFloat64() -> __Op:
    return __lib.BinaryenReinterpretFloat64()


def ConvertSInt32ToFloat32() -> __Op:
    return __lib.BinaryenConvertSInt32ToFloat32()


def ConvertSInt32ToFloat64() -> __Op:
    return __lib.BinaryenConvertSInt32ToFloat64()


def ConvertUInt32ToFloat32() -> __Op:
    return __lib.BinaryenConvertUInt32ToFloat32()


def ConvertUInt32ToFloat64() -> __Op:
    return __lib.BinaryenConvertUInt32ToFloat64()


def ConvertSInt64ToFloat32() -> __Op:
    return __lib.BinaryenConvertSInt64ToFloat32()


def ConvertSInt64ToFloat64() -> __Op:
    return __lib.BinaryenConvertSInt64ToFloat64()


def ConvertUInt64ToFloat32() -> __Op:
    return __lib.BinaryenConvertUInt64ToFloat32()


def ConvertUInt64ToFloat64() -> __Op:
    return __lib.BinaryenConvertUInt64ToFloat64()


def PromoteFloat32() -> __Op:
    return __lib.BinaryenPromoteFloat32()


def DemoteFloat64() -> __Op:
    return __lib.BinaryenDemoteFloat64()


def ReinterpretInt32() -> __Op:
    return __lib.BinaryenReinterpretInt32()


def ReinterpretInt64() -> __Op:
    return __lib.BinaryenReinterpretInt64()


def ExtendS8Int32() -> __Op:
    return __lib.BinaryenExtendS8Int32()


def ExtendS16Int32() -> __Op:
    return __lib.BinaryenExtendS16Int32()


def ExtendS8Int64() -> __Op:
    return __lib.BinaryenExtendS8Int64()


def ExtendS16Int64() -> __Op:
    return __lib.BinaryenExtendS16Int64()


def ExtendS32Int64() -> __Op:
    return __lib.BinaryenExtendS32Int64()


def AddInt32() -> __Op:
    return __lib.BinaryenAddInt32()


def SubInt32() -> __Op:
    return __lib.BinaryenSubInt32()


def MulInt32() -> __Op:
    return __lib.BinaryenMulInt32()


def DivSInt32() -> __Op:
    return __lib.BinaryenDivSInt32()


def DivUInt32() -> __Op:
    return __lib.BinaryenDivUInt32()


def RemSInt32() -> __Op:
    return __lib.BinaryenRemSInt32()


def RemUInt32() -> __Op:
    return __lib.BinaryenRemUInt32()


def AndInt32() -> __Op:
    return __lib.BinaryenAndInt32()


def OrInt32() -> __Op:
    return __lib.BinaryenOrInt32()


def XorInt32() -> __Op:
    return __lib.BinaryenXorInt32()


def ShlInt32() -> __Op:
    return __lib.BinaryenShlInt32()


def ShrUInt32() -> __Op:
    return __lib.BinaryenShrUInt32()


def ShrSInt32() -> __Op:
    return __lib.BinaryenShrSInt32()


def RotLInt32() -> __Op:
    return __lib.BinaryenRotLInt32()


def RotRInt32() -> __Op:
    return __lib.BinaryenRotRInt32()


def EqInt32() -> __Op:
    return __lib.BinaryenEqInt32()


def NeInt32() -> __Op:
    return __lib.BinaryenNeInt32()


def LtSInt32() -> __Op:
    return __lib.BinaryenLtSInt32()


def LtUInt32() -> __Op:
    return __lib.BinaryenLtUInt32()


def LeSInt32() -> __Op:
    return __lib.BinaryenLeSInt32()


def LeUInt32() -> __Op:
    return __lib.BinaryenLeUInt32()


def GtSInt32() -> __Op:
    return __lib.BinaryenGtSInt32()


def GtUInt32() -> __Op:
    return __lib.BinaryenGtUInt32()


def GeSInt32() -> __Op:
    return __lib.BinaryenGeSInt32()


def GeUInt32() -> __Op:
    return __lib.BinaryenGeUInt32()


def AddInt64() -> __Op:
    return __lib.BinaryenAddInt64()


def SubInt64() -> __Op:
    return __lib.BinaryenSubInt64()


def MulInt64() -> __Op:
    return __lib.BinaryenMulInt64()


def DivSInt64() -> __Op:
    return __lib.BinaryenDivSInt64()


def DivUInt64() -> __Op:
    return __lib.BinaryenDivUInt64()


def RemSInt64() -> __Op:
    return __lib.BinaryenRemSInt64()


def RemUInt64() -> __Op:
    return __lib.BinaryenRemUInt64()


def AndInt64() -> __Op:
    return __lib.BinaryenAndInt64()


def OrInt64() -> __Op:
    return __lib.BinaryenOrInt64()


def XorInt64() -> __Op:
    return __lib.BinaryenXorInt64()


def ShlInt64() -> __Op:
    return __lib.BinaryenShlInt64()


def ShrUInt64() -> __Op:
    return __lib.BinaryenShrUInt64()


def ShrSInt64() -> __Op:
    return __lib.BinaryenShrSInt64()


def RotLInt64() -> __Op:
    return __lib.BinaryenRotLInt64()


def RotRInt64() -> __Op:
    return __lib.BinaryenRotRInt64()


def EqInt64() -> __Op:
    return __lib.BinaryenEqInt64()


def NeInt64() -> __Op:
    return __lib.BinaryenNeInt64()


def LtSInt64() -> __Op:
    return __lib.BinaryenLtSInt64()


def LtUInt64() -> __Op:
    return __lib.BinaryenLtUInt64()


def LeSInt64() -> __Op:
    return __lib.BinaryenLeSInt64()


def LeUInt64() -> __Op:
    return __lib.BinaryenLeUInt64()


def GtSInt64() -> __Op:
    return __lib.BinaryenGtSInt64()


def GtUInt64() -> __Op:
    return __lib.BinaryenGtUInt64()


def GeSInt64() -> __Op:
    return __lib.BinaryenGeSInt64()


def GeUInt64() -> __Op:
    return __lib.BinaryenGeUInt64()


def AddFloat32() -> __Op:
    return __lib.BinaryenAddFloat32()


def SubFloat32() -> __Op:
    return __lib.BinaryenSubFloat32()


def MulFloat32() -> __Op:
    return __lib.BinaryenMulFloat32()


def DivFloat32() -> __Op:
    return __lib.BinaryenDivFloat32()


def CopySignFloat32() -> __Op:
    return __lib.BinaryenCopySignFloat32()


def MinFloat32() -> __Op:
    return __lib.BinaryenMinFloat32()


def MaxFloat32() -> __Op:
    return __lib.BinaryenMaxFloat32()


def EqFloat32() -> __Op:
    return __lib.BinaryenEqFloat32()


def NeFloat32() -> __Op:
    return __lib.BinaryenNeFloat32()


def LtFloat32() -> __Op:
    return __lib.BinaryenLtFloat32()


def LeFloat32() -> __Op:
    return __lib.BinaryenLeFloat32()


def GtFloat32() -> __Op:
    return __lib.BinaryenGtFloat32()


def GeFloat32() -> __Op:
    return __lib.BinaryenGeFloat32()


def AddFloat64() -> __Op:
    return __lib.BinaryenAddFloat64()


def SubFloat64() -> __Op:
    return __lib.BinaryenSubFloat64()


def MulFloat64() -> __Op:
    return __lib.BinaryenMulFloat64()


def DivFloat64() -> __Op:
    return __lib.BinaryenDivFloat64()


def CopySignFloat64() -> __Op:
    return __lib.BinaryenCopySignFloat64()


def MinFloat64() -> __Op:
    return __lib.BinaryenMinFloat64()


def MaxFloat64() -> __Op:
    return __lib.BinaryenMaxFloat64()


def EqFloat64() -> __Op:
    return __lib.BinaryenEqFloat64()


def NeFloat64() -> __Op:
    return __lib.BinaryenNeFloat64()


def LtFloat64() -> __Op:
    return __lib.BinaryenLtFloat64()


def LeFloat64() -> __Op:
    return __lib.BinaryenLeFloat64()


def GtFloat64() -> __Op:
    return __lib.BinaryenGtFloat64()


def GeFloat64() -> __Op:
    return __lib.BinaryenGeFloat64()


def AtomicRMWAdd() -> __Op:
    return __lib.BinaryenAtomicRMWAdd()


def AtomicRMWSub() -> __Op:
    return __lib.BinaryenAtomicRMWSub()


def AtomicRMWAnd() -> __Op:
    return __lib.BinaryenAtomicRMWAnd()


def AtomicRMWOr() -> __Op:
    return __lib.BinaryenAtomicRMWOr()


def AtomicRMWXor() -> __Op:
    return __lib.BinaryenAtomicRMWXor()


def AtomicRMWXchg() -> __Op:
    return __lib.BinaryenAtomicRMWXchg()


def TruncSatSFloat32ToInt32() -> __Op:
    return __lib.BinaryenTruncSatSFloat32ToInt32()


def TruncSatSFloat32ToInt64() -> __Op:
    return __lib.BinaryenTruncSatSFloat32ToInt64()


def TruncSatUFloat32ToInt32() -> __Op:
    return __lib.BinaryenTruncSatUFloat32ToInt32()


def TruncSatUFloat32ToInt64() -> __Op:
    return __lib.BinaryenTruncSatUFloat32ToInt64()


def TruncSatSFloat64ToInt32() -> __Op:
    return __lib.BinaryenTruncSatSFloat64ToInt32()


def TruncSatSFloat64ToInt64() -> __Op:
    return __lib.BinaryenTruncSatSFloat64ToInt64()


def TruncSatUFloat64ToInt32() -> __Op:
    return __lib.BinaryenTruncSatUFloat64ToInt32()


def TruncSatUFloat64ToInt64() -> __Op:
    return __lib.BinaryenTruncSatUFloat64ToInt64()


def SplatVecI8x16() -> __Op:
    return __lib.BinaryenSplatVecI8x16()


def ExtractLaneSVecI8x16() -> __Op:
    return __lib.BinaryenExtractLaneSVecI8x16()


def ExtractLaneUVecI8x16() -> __Op:
    return __lib.BinaryenExtractLaneUVecI8x16()


def ReplaceLaneVecI8x16() -> __Op:
    return __lib.BinaryenReplaceLaneVecI8x16()


def SplatVecI16x8() -> __Op:
    return __lib.BinaryenSplatVecI16x8()


def ExtractLaneSVecI16x8() -> __Op:
    return __lib.BinaryenExtractLaneSVecI16x8()


def ExtractLaneUVecI16x8() -> __Op:
    return __lib.BinaryenExtractLaneUVecI16x8()


def ReplaceLaneVecI16x8() -> __Op:
    return __lib.BinaryenReplaceLaneVecI16x8()


def SplatVecI32x4() -> __Op:
    return __lib.BinaryenSplatVecI32x4()


def ExtractLaneVecI32x4() -> __Op:
    return __lib.BinaryenExtractLaneVecI32x4()


def ReplaceLaneVecI32x4() -> __Op:
    return __lib.BinaryenReplaceLaneVecI32x4()


def SplatVecI64x2() -> __Op:
    return __lib.BinaryenSplatVecI64x2()


def ExtractLaneVecI64x2() -> __Op:
    return __lib.BinaryenExtractLaneVecI64x2()


def ReplaceLaneVecI64x2() -> __Op:
    return __lib.BinaryenReplaceLaneVecI64x2()


def SplatVecF32x4() -> __Op:
    return __lib.BinaryenSplatVecF32x4()


def ExtractLaneVecF32x4() -> __Op:
    return __lib.BinaryenExtractLaneVecF32x4()


def ReplaceLaneVecF32x4() -> __Op:
    return __lib.BinaryenReplaceLaneVecF32x4()


def SplatVecF64x2() -> __Op:
    return __lib.BinaryenSplatVecF64x2()


def ExtractLaneVecF64x2() -> __Op:
    return __lib.BinaryenExtractLaneVecF64x2()


def ReplaceLaneVecF64x2() -> __Op:
    return __lib.BinaryenReplaceLaneVecF64x2()


def EqVecI8x16() -> __Op:
    return __lib.BinaryenEqVecI8x16()


def NeVecI8x16() -> __Op:
    return __lib.BinaryenNeVecI8x16()


def LtSVecI8x16() -> __Op:
    return __lib.BinaryenLtSVecI8x16()


def LtUVecI8x16() -> __Op:
    return __lib.BinaryenLtUVecI8x16()


def GtSVecI8x16() -> __Op:
    return __lib.BinaryenGtSVecI8x16()


def GtUVecI8x16() -> __Op:
    return __lib.BinaryenGtUVecI8x16()


def LeSVecI8x16() -> __Op:
    return __lib.BinaryenLeSVecI8x16()


def LeUVecI8x16() -> __Op:
    return __lib.BinaryenLeUVecI8x16()


def GeSVecI8x16() -> __Op:
    return __lib.BinaryenGeSVecI8x16()


def GeUVecI8x16() -> __Op:
    return __lib.BinaryenGeUVecI8x16()


def EqVecI16x8() -> __Op:
    return __lib.BinaryenEqVecI16x8()


def NeVecI16x8() -> __Op:
    return __lib.BinaryenNeVecI16x8()


def LtSVecI16x8() -> __Op:
    return __lib.BinaryenLtSVecI16x8()


def LtUVecI16x8() -> __Op:
    return __lib.BinaryenLtUVecI16x8()


def GtSVecI16x8() -> __Op:
    return __lib.BinaryenGtSVecI16x8()


def GtUVecI16x8() -> __Op:
    return __lib.BinaryenGtUVecI16x8()


def LeSVecI16x8() -> __Op:
    return __lib.BinaryenLeSVecI16x8()


def LeUVecI16x8() -> __Op:
    return __lib.BinaryenLeUVecI16x8()


def GeSVecI16x8() -> __Op:
    return __lib.BinaryenGeSVecI16x8()


def GeUVecI16x8() -> __Op:
    return __lib.BinaryenGeUVecI16x8()


def EqVecI32x4() -> __Op:
    return __lib.BinaryenEqVecI32x4()


def NeVecI32x4() -> __Op:
    return __lib.BinaryenNeVecI32x4()


def LtSVecI32x4() -> __Op:
    return __lib.BinaryenLtSVecI32x4()


def LtUVecI32x4() -> __Op:
    return __lib.BinaryenLtUVecI32x4()


def GtSVecI32x4() -> __Op:
    return __lib.BinaryenGtSVecI32x4()


def GtUVecI32x4() -> __Op:
    return __lib.BinaryenGtUVecI32x4()


def LeSVecI32x4() -> __Op:
    return __lib.BinaryenLeSVecI32x4()


def LeUVecI32x4() -> __Op:
    return __lib.BinaryenLeUVecI32x4()


def GeSVecI32x4() -> __Op:
    return __lib.BinaryenGeSVecI32x4()


def GeUVecI32x4() -> __Op:
    return __lib.BinaryenGeUVecI32x4()


def EqVecI64x2() -> __Op:
    return __lib.BinaryenEqVecI64x2()


def NeVecI64x2() -> __Op:
    return __lib.BinaryenNeVecI64x2()


def LtSVecI64x2() -> __Op:
    return __lib.BinaryenLtSVecI64x2()


def GtSVecI64x2() -> __Op:
    return __lib.BinaryenGtSVecI64x2()


def LeSVecI64x2() -> __Op:
    return __lib.BinaryenLeSVecI64x2()


def GeSVecI64x2() -> __Op:
    return __lib.BinaryenGeSVecI64x2()


def EqVecF32x4() -> __Op:
    return __lib.BinaryenEqVecF32x4()


def NeVecF32x4() -> __Op:
    return __lib.BinaryenNeVecF32x4()


def LtVecF32x4() -> __Op:
    return __lib.BinaryenLtVecF32x4()


def GtVecF32x4() -> __Op:
    return __lib.BinaryenGtVecF32x4()


def LeVecF32x4() -> __Op:
    return __lib.BinaryenLeVecF32x4()


def GeVecF32x4() -> __Op:
    return __lib.BinaryenGeVecF32x4()


def EqVecF64x2() -> __Op:
    return __lib.BinaryenEqVecF64x2()


def NeVecF64x2() -> __Op:
    return __lib.BinaryenNeVecF64x2()


def LtVecF64x2() -> __Op:
    return __lib.BinaryenLtVecF64x2()


def GtVecF64x2() -> __Op:
    return __lib.BinaryenGtVecF64x2()


def LeVecF64x2() -> __Op:
    return __lib.BinaryenLeVecF64x2()


def GeVecF64x2() -> __Op:
    return __lib.BinaryenGeVecF64x2()


def NotVec128() -> __Op:
    return __lib.BinaryenNotVec128()


def AndVec128() -> __Op:
    return __lib.BinaryenAndVec128()


def OrVec128() -> __Op:
    return __lib.BinaryenOrVec128()


def XorVec128() -> __Op:
    return __lib.BinaryenXorVec128()


def AndNotVec128() -> __Op:
    return __lib.BinaryenAndNotVec128()


def BitselectVec128() -> __Op:
    return __lib.BinaryenBitselectVec128()


def RelaxedFmaVecF32x4() -> __Op:
    return __lib.BinaryenRelaxedFmaVecF32x4()


def RelaxedFmsVecF32x4() -> __Op:
    return __lib.BinaryenRelaxedFmsVecF32x4()


def RelaxedFmaVecF64x2() -> __Op:
    return __lib.BinaryenRelaxedFmaVecF64x2()


def RelaxedFmsVecF64x2() -> __Op:
    return __lib.BinaryenRelaxedFmsVecF64x2()


def LaneselectI8x16() -> __Op:
    return __lib.BinaryenLaneselectI8x16()


def LaneselectI16x8() -> __Op:
    return __lib.BinaryenLaneselectI16x8()


def LaneselectI32x4() -> __Op:
    return __lib.BinaryenLaneselectI32x4()


def LaneselectI64x2() -> __Op:
    return __lib.BinaryenLaneselectI64x2()


def DotI8x16I7x16AddSToVecI32x4() -> __Op:
    return __lib.BinaryenDotI8x16I7x16AddSToVecI32x4()


def AnyTrueVec128() -> __Op:
    return __lib.BinaryenAnyTrueVec128()


def PopcntVecI8x16() -> __Op:
    return __lib.BinaryenPopcntVecI8x16()


def AbsVecI8x16() -> __Op:
    return __lib.BinaryenAbsVecI8x16()


def NegVecI8x16() -> __Op:
    return __lib.BinaryenNegVecI8x16()


def AllTrueVecI8x16() -> __Op:
    return __lib.BinaryenAllTrueVecI8x16()


def BitmaskVecI8x16() -> __Op:
    return __lib.BinaryenBitmaskVecI8x16()


def ShlVecI8x16() -> __Op:
    return __lib.BinaryenShlVecI8x16()


def ShrSVecI8x16() -> __Op:
    return __lib.BinaryenShrSVecI8x16()


def ShrUVecI8x16() -> __Op:
    return __lib.BinaryenShrUVecI8x16()


def AddVecI8x16() -> __Op:
    return __lib.BinaryenAddVecI8x16()


def AddSatSVecI8x16() -> __Op:
    return __lib.BinaryenAddSatSVecI8x16()


def AddSatUVecI8x16() -> __Op:
    return __lib.BinaryenAddSatUVecI8x16()


def SubVecI8x16() -> __Op:
    return __lib.BinaryenSubVecI8x16()


def SubSatSVecI8x16() -> __Op:
    return __lib.BinaryenSubSatSVecI8x16()


def SubSatUVecI8x16() -> __Op:
    return __lib.BinaryenSubSatUVecI8x16()


def MinSVecI8x16() -> __Op:
    return __lib.BinaryenMinSVecI8x16()


def MinUVecI8x16() -> __Op:
    return __lib.BinaryenMinUVecI8x16()


def MaxSVecI8x16() -> __Op:
    return __lib.BinaryenMaxSVecI8x16()


def MaxUVecI8x16() -> __Op:
    return __lib.BinaryenMaxUVecI8x16()


def AvgrUVecI8x16() -> __Op:
    return __lib.BinaryenAvgrUVecI8x16()


def AbsVecI16x8() -> __Op:
    return __lib.BinaryenAbsVecI16x8()


def NegVecI16x8() -> __Op:
    return __lib.BinaryenNegVecI16x8()


def AllTrueVecI16x8() -> __Op:
    return __lib.BinaryenAllTrueVecI16x8()


def BitmaskVecI16x8() -> __Op:
    return __lib.BinaryenBitmaskVecI16x8()


def ShlVecI16x8() -> __Op:
    return __lib.BinaryenShlVecI16x8()


def ShrSVecI16x8() -> __Op:
    return __lib.BinaryenShrSVecI16x8()


def ShrUVecI16x8() -> __Op:
    return __lib.BinaryenShrUVecI16x8()


def AddVecI16x8() -> __Op:
    return __lib.BinaryenAddVecI16x8()


def AddSatSVecI16x8() -> __Op:
    return __lib.BinaryenAddSatSVecI16x8()


def AddSatUVecI16x8() -> __Op:
    return __lib.BinaryenAddSatUVecI16x8()


def SubVecI16x8() -> __Op:
    return __lib.BinaryenSubVecI16x8()


def SubSatSVecI16x8() -> __Op:
    return __lib.BinaryenSubSatSVecI16x8()


def SubSatUVecI16x8() -> __Op:
    return __lib.BinaryenSubSatUVecI16x8()


def MulVecI16x8() -> __Op:
    return __lib.BinaryenMulVecI16x8()


def MinSVecI16x8() -> __Op:
    return __lib.BinaryenMinSVecI16x8()


def MinUVecI16x8() -> __Op:
    return __lib.BinaryenMinUVecI16x8()


def MaxSVecI16x8() -> __Op:
    return __lib.BinaryenMaxSVecI16x8()


def MaxUVecI16x8() -> __Op:
    return __lib.BinaryenMaxUVecI16x8()


def AvgrUVecI16x8() -> __Op:
    return __lib.BinaryenAvgrUVecI16x8()


def Q15MulrSatSVecI16x8() -> __Op:
    return __lib.BinaryenQ15MulrSatSVecI16x8()


def ExtMulLowSVecI16x8() -> __Op:
    return __lib.BinaryenExtMulLowSVecI16x8()


def ExtMulHighSVecI16x8() -> __Op:
    return __lib.BinaryenExtMulHighSVecI16x8()


def ExtMulLowUVecI16x8() -> __Op:
    return __lib.BinaryenExtMulLowUVecI16x8()


def ExtMulHighUVecI16x8() -> __Op:
    return __lib.BinaryenExtMulHighUVecI16x8()


def AbsVecI32x4() -> __Op:
    return __lib.BinaryenAbsVecI32x4()


def NegVecI32x4() -> __Op:
    return __lib.BinaryenNegVecI32x4()


def AllTrueVecI32x4() -> __Op:
    return __lib.BinaryenAllTrueVecI32x4()


def BitmaskVecI32x4() -> __Op:
    return __lib.BinaryenBitmaskVecI32x4()


def ShlVecI32x4() -> __Op:
    return __lib.BinaryenShlVecI32x4()


def ShrSVecI32x4() -> __Op:
    return __lib.BinaryenShrSVecI32x4()


def ShrUVecI32x4() -> __Op:
    return __lib.BinaryenShrUVecI32x4()


def AddVecI32x4() -> __Op:
    return __lib.BinaryenAddVecI32x4()


def SubVecI32x4() -> __Op:
    return __lib.BinaryenSubVecI32x4()


def MulVecI32x4() -> __Op:
    return __lib.BinaryenMulVecI32x4()


def MinSVecI32x4() -> __Op:
    return __lib.BinaryenMinSVecI32x4()


def MinUVecI32x4() -> __Op:
    return __lib.BinaryenMinUVecI32x4()


def MaxSVecI32x4() -> __Op:
    return __lib.BinaryenMaxSVecI32x4()


def MaxUVecI32x4() -> __Op:
    return __lib.BinaryenMaxUVecI32x4()


def DotSVecI16x8ToVecI32x4() -> __Op:
    return __lib.BinaryenDotSVecI16x8ToVecI32x4()


def ExtMulLowSVecI32x4() -> __Op:
    return __lib.BinaryenExtMulLowSVecI32x4()


def ExtMulHighSVecI32x4() -> __Op:
    return __lib.BinaryenExtMulHighSVecI32x4()


def ExtMulLowUVecI32x4() -> __Op:
    return __lib.BinaryenExtMulLowUVecI32x4()


def ExtMulHighUVecI32x4() -> __Op:
    return __lib.BinaryenExtMulHighUVecI32x4()


def AbsVecI64x2() -> __Op:
    return __lib.BinaryenAbsVecI64x2()


def NegVecI64x2() -> __Op:
    return __lib.BinaryenNegVecI64x2()


def AllTrueVecI64x2() -> __Op:
    return __lib.BinaryenAllTrueVecI64x2()


def BitmaskVecI64x2() -> __Op:
    return __lib.BinaryenBitmaskVecI64x2()


def ShlVecI64x2() -> __Op:
    return __lib.BinaryenShlVecI64x2()


def ShrSVecI64x2() -> __Op:
    return __lib.BinaryenShrSVecI64x2()


def ShrUVecI64x2() -> __Op:
    return __lib.BinaryenShrUVecI64x2()


def AddVecI64x2() -> __Op:
    return __lib.BinaryenAddVecI64x2()


def SubVecI64x2() -> __Op:
    return __lib.BinaryenSubVecI64x2()


def MulVecI64x2() -> __Op:
    return __lib.BinaryenMulVecI64x2()


def ExtMulLowSVecI64x2() -> __Op:
    return __lib.BinaryenExtMulLowSVecI64x2()


def ExtMulHighSVecI64x2() -> __Op:
    return __lib.BinaryenExtMulHighSVecI64x2()


def ExtMulLowUVecI64x2() -> __Op:
    return __lib.BinaryenExtMulLowUVecI64x2()


def ExtMulHighUVecI64x2() -> __Op:
    return __lib.BinaryenExtMulHighUVecI64x2()


def AbsVecF32x4() -> __Op:
    return __lib.BinaryenAbsVecF32x4()


def NegVecF32x4() -> __Op:
    return __lib.BinaryenNegVecF32x4()


def SqrtVecF32x4() -> __Op:
    return __lib.BinaryenSqrtVecF32x4()


def AddVecF32x4() -> __Op:
    return __lib.BinaryenAddVecF32x4()


def SubVecF32x4() -> __Op:
    return __lib.BinaryenSubVecF32x4()


def MulVecF32x4() -> __Op:
    return __lib.BinaryenMulVecF32x4()


def DivVecF32x4() -> __Op:
    return __lib.BinaryenDivVecF32x4()


def MinVecF32x4() -> __Op:
    return __lib.BinaryenMinVecF32x4()


def MaxVecF32x4() -> __Op:
    return __lib.BinaryenMaxVecF32x4()


def PMinVecF32x4() -> __Op:
    return __lib.BinaryenPMinVecF32x4()


def PMaxVecF32x4() -> __Op:
    return __lib.BinaryenPMaxVecF32x4()


def CeilVecF32x4() -> __Op:
    return __lib.BinaryenCeilVecF32x4()


def FloorVecF32x4() -> __Op:
    return __lib.BinaryenFloorVecF32x4()


def TruncVecF32x4() -> __Op:
    return __lib.BinaryenTruncVecF32x4()


def NearestVecF32x4() -> __Op:
    return __lib.BinaryenNearestVecF32x4()


def AbsVecF64x2() -> __Op:
    return __lib.BinaryenAbsVecF64x2()


def NegVecF64x2() -> __Op:
    return __lib.BinaryenNegVecF64x2()


def SqrtVecF64x2() -> __Op:
    return __lib.BinaryenSqrtVecF64x2()


def AddVecF64x2() -> __Op:
    return __lib.BinaryenAddVecF64x2()


def SubVecF64x2() -> __Op:
    return __lib.BinaryenSubVecF64x2()


def MulVecF64x2() -> __Op:
    return __lib.BinaryenMulVecF64x2()


def DivVecF64x2() -> __Op:
    return __lib.BinaryenDivVecF64x2()


def MinVecF64x2() -> __Op:
    return __lib.BinaryenMinVecF64x2()


def MaxVecF64x2() -> __Op:
    return __lib.BinaryenMaxVecF64x2()


def PMinVecF64x2() -> __Op:
    return __lib.BinaryenPMinVecF64x2()


def PMaxVecF64x2() -> __Op:
    return __lib.BinaryenPMaxVecF64x2()


def CeilVecF64x2() -> __Op:
    return __lib.BinaryenCeilVecF64x2()


def FloorVecF64x2() -> __Op:
    return __lib.BinaryenFloorVecF64x2()


def TruncVecF64x2() -> __Op:
    return __lib.BinaryenTruncVecF64x2()


def NearestVecF64x2() -> __Op:
    return __lib.BinaryenNearestVecF64x2()


def ExtAddPairwiseSVecI8x16ToI16x8() -> __Op:
    return __lib.BinaryenExtAddPairwiseSVecI8x16ToI16x8()


def ExtAddPairwiseUVecI8x16ToI16x8() -> __Op:
    return __lib.BinaryenExtAddPairwiseUVecI8x16ToI16x8()


def ExtAddPairwiseSVecI16x8ToI32x4() -> __Op:
    return __lib.BinaryenExtAddPairwiseSVecI16x8ToI32x4()


def ExtAddPairwiseUVecI16x8ToI32x4() -> __Op:
    return __lib.BinaryenExtAddPairwiseUVecI16x8ToI32x4()


def TruncSatSVecF32x4ToVecI32x4() -> __Op:
    return __lib.BinaryenTruncSatSVecF32x4ToVecI32x4()


def TruncSatUVecF32x4ToVecI32x4() -> __Op:
    return __lib.BinaryenTruncSatUVecF32x4ToVecI32x4()


def ConvertSVecI32x4ToVecF32x4() -> __Op:
    return __lib.BinaryenConvertSVecI32x4ToVecF32x4()


def ConvertUVecI32x4ToVecF32x4() -> __Op:
    return __lib.BinaryenConvertUVecI32x4ToVecF32x4()


def Load8SplatVec128() -> __Op:
    return __lib.BinaryenLoad8SplatVec128()


def Load16SplatVec128() -> __Op:
    return __lib.BinaryenLoad16SplatVec128()


def Load32SplatVec128() -> __Op:
    return __lib.BinaryenLoad32SplatVec128()


def Load64SplatVec128() -> __Op:
    return __lib.BinaryenLoad64SplatVec128()


def Load8x8SVec128() -> __Op:
    return __lib.BinaryenLoad8x8SVec128()


def Load8x8UVec128() -> __Op:
    return __lib.BinaryenLoad8x8UVec128()


def Load16x4SVec128() -> __Op:
    return __lib.BinaryenLoad16x4SVec128()


def Load16x4UVec128() -> __Op:
    return __lib.BinaryenLoad16x4UVec128()


def Load32x2SVec128() -> __Op:
    return __lib.BinaryenLoad32x2SVec128()


def Load32x2UVec128() -> __Op:
    return __lib.BinaryenLoad32x2UVec128()


def Load32ZeroVec128() -> __Op:
    return __lib.BinaryenLoad32ZeroVec128()


def Load64ZeroVec128() -> __Op:
    return __lib.BinaryenLoad64ZeroVec128()


def Load8LaneVec128() -> __Op:
    return __lib.BinaryenLoad8LaneVec128()


def Load16LaneVec128() -> __Op:
    return __lib.BinaryenLoad16LaneVec128()


def Load32LaneVec128() -> __Op:
    return __lib.BinaryenLoad32LaneVec128()


def Load64LaneVec128() -> __Op:
    return __lib.BinaryenLoad64LaneVec128()


def Store8LaneVec128() -> __Op:
    return __lib.BinaryenStore8LaneVec128()


def Store16LaneVec128() -> __Op:
    return __lib.BinaryenStore16LaneVec128()


def Store32LaneVec128() -> __Op:
    return __lib.BinaryenStore32LaneVec128()


def Store64LaneVec128() -> __Op:
    return __lib.BinaryenStore64LaneVec128()


def NarrowSVecI16x8ToVecI8x16() -> __Op:
    return __lib.BinaryenNarrowSVecI16x8ToVecI8x16()


def NarrowUVecI16x8ToVecI8x16() -> __Op:
    return __lib.BinaryenNarrowUVecI16x8ToVecI8x16()


def NarrowSVecI32x4ToVecI16x8() -> __Op:
    return __lib.BinaryenNarrowSVecI32x4ToVecI16x8()


def NarrowUVecI32x4ToVecI16x8() -> __Op:
    return __lib.BinaryenNarrowUVecI32x4ToVecI16x8()


def ExtendLowSVecI8x16ToVecI16x8() -> __Op:
    return __lib.BinaryenExtendLowSVecI8x16ToVecI16x8()


def ExtendHighSVecI8x16ToVecI16x8() -> __Op:
    return __lib.BinaryenExtendHighSVecI8x16ToVecI16x8()


def ExtendLowUVecI8x16ToVecI16x8() -> __Op:
    return __lib.BinaryenExtendLowUVecI8x16ToVecI16x8()


def ExtendHighUVecI8x16ToVecI16x8() -> __Op:
    return __lib.BinaryenExtendHighUVecI8x16ToVecI16x8()


def ExtendLowSVecI16x8ToVecI32x4() -> __Op:
    return __lib.BinaryenExtendLowSVecI16x8ToVecI32x4()


def ExtendHighSVecI16x8ToVecI32x4() -> __Op:
    return __lib.BinaryenExtendHighSVecI16x8ToVecI32x4()


def ExtendLowUVecI16x8ToVecI32x4() -> __Op:
    return __lib.BinaryenExtendLowUVecI16x8ToVecI32x4()


def ExtendHighUVecI16x8ToVecI32x4() -> __Op:
    return __lib.BinaryenExtendHighUVecI16x8ToVecI32x4()


def ExtendLowSVecI32x4ToVecI64x2() -> __Op:
    return __lib.BinaryenExtendLowSVecI32x4ToVecI64x2()


def ExtendHighSVecI32x4ToVecI64x2() -> __Op:
    return __lib.BinaryenExtendHighSVecI32x4ToVecI64x2()


def ExtendLowUVecI32x4ToVecI64x2() -> __Op:
    return __lib.BinaryenExtendLowUVecI32x4ToVecI64x2()


def ExtendHighUVecI32x4ToVecI64x2() -> __Op:
    return __lib.BinaryenExtendHighUVecI32x4ToVecI64x2()


def ConvertLowSVecI32x4ToVecF64x2() -> __Op:
    return __lib.BinaryenConvertLowSVecI32x4ToVecF64x2()


def ConvertLowUVecI32x4ToVecF64x2() -> __Op:
    return __lib.BinaryenConvertLowUVecI32x4ToVecF64x2()


def TruncSatZeroSVecF64x2ToVecI32x4() -> __Op:
    return __lib.BinaryenTruncSatZeroSVecF64x2ToVecI32x4()


def TruncSatZeroUVecF64x2ToVecI32x4() -> __Op:
    return __lib.BinaryenTruncSatZeroUVecF64x2ToVecI32x4()


def DemoteZeroVecF64x2ToVecF32x4() -> __Op:
    return __lib.BinaryenDemoteZeroVecF64x2ToVecF32x4()


def PromoteLowVecF32x4ToVecF64x2() -> __Op:
    return __lib.BinaryenPromoteLowVecF32x4ToVecF64x2()


def RelaxedTruncSVecF32x4ToVecI32x4() -> __Op:
    return __lib.BinaryenRelaxedTruncSVecF32x4ToVecI32x4()


def RelaxedTruncUVecF32x4ToVecI32x4() -> __Op:
    return __lib.BinaryenRelaxedTruncUVecF32x4ToVecI32x4()


def RelaxedTruncZeroSVecF64x2ToVecI32x4() -> __Op:
    return __lib.BinaryenRelaxedTruncZeroSVecF64x2ToVecI32x4()


def RelaxedTruncZeroUVecF64x2ToVecI32x4() -> __Op:
    return __lib.BinaryenRelaxedTruncZeroUVecF64x2ToVecI32x4()


def SwizzleVecI8x16() -> __Op:
    return __lib.BinaryenSwizzleVecI8x16()


def RelaxedSwizzleVecI8x16() -> __Op:
    return __lib.BinaryenRelaxedSwizzleVecI8x16()


def RelaxedMinVecF32x4() -> __Op:
    return __lib.BinaryenRelaxedMinVecF32x4()


def RelaxedMaxVecF32x4() -> __Op:
    return __lib.BinaryenRelaxedMaxVecF32x4()


def RelaxedMinVecF64x2() -> __Op:
    return __lib.BinaryenRelaxedMinVecF64x2()


def RelaxedMaxVecF64x2() -> __Op:
    return __lib.BinaryenRelaxedMaxVecF64x2()


def RelaxedQ15MulrSVecI16x8() -> __Op:
    return __lib.BinaryenRelaxedQ15MulrSVecI16x8()


def DotI8x16I7x16SToVecI16x8() -> __Op:
    return __lib.BinaryenDotI8x16I7x16SToVecI16x8()


def RefAsNonNull() -> __Op:
    return __lib.BinaryenRefAsNonNull()


def RefAsExternInternalize() -> __Op:
    return __lib.BinaryenRefAsExternInternalize()


def RefAsExternExternalize() -> __Op:
    return __lib.BinaryenRefAsExternExternalize()


def BrOnNull() -> __Op:
    return __lib.BinaryenBrOnNull()


def BrOnNonNull() -> __Op:
    return __lib.BinaryenBrOnNonNull()


def BrOnCast() -> __Op:
    return __lib.BinaryenBrOnCast()


def BrOnCastFail() -> __Op:
    return __lib.BinaryenBrOnCastFail()


def StringNewUTF8() -> __Op:
    return __lib.BinaryenStringNewUTF8()


def StringNewWTF8() -> __Op:
    return __lib.BinaryenStringNewWTF8()


def StringNewLossyUTF8() -> __Op:
    return __lib.BinaryenStringNewLossyUTF8()


def StringNewWTF16() -> __Op:
    return __lib.BinaryenStringNewWTF16()


def StringNewUTF8Array() -> __Op:
    return __lib.BinaryenStringNewUTF8Array()


def StringNewWTF8Array() -> __Op:
    return __lib.BinaryenStringNewWTF8Array()


def StringNewLossyUTF8Array() -> __Op:
    return __lib.BinaryenStringNewLossyUTF8Array()


def StringNewWTF16Array() -> __Op:
    return __lib.BinaryenStringNewWTF16Array()


def StringNewFromCodePoint() -> __Op:
    return __lib.BinaryenStringNewFromCodePoint()


def StringMeasureUTF8() -> __Op:
    return __lib.BinaryenStringMeasureUTF8()


def StringMeasureWTF8() -> __Op:
    return __lib.BinaryenStringMeasureWTF8()


def StringMeasureWTF16() -> __Op:
    return __lib.BinaryenStringMeasureWTF16()


def StringMeasureIsUSV() -> __Op:
    return __lib.BinaryenStringMeasureIsUSV()


def StringMeasureWTF16View() -> __Op:
    return __lib.BinaryenStringMeasureWTF16View()


def StringEncodeUTF8() -> __Op:
    return __lib.BinaryenStringEncodeUTF8()


def StringEncodeLossyUTF8() -> __Op:
    return __lib.BinaryenStringEncodeLossyUTF8()


def StringEncodeWTF8() -> __Op:
    return __lib.BinaryenStringEncodeWTF8()


def StringEncodeWTF16() -> __Op:
    return __lib.BinaryenStringEncodeWTF16()


def StringEncodeUTF8Array() -> __Op:
    return __lib.BinaryenStringEncodeUTF8Array()


def StringEncodeLossyUTF8Array() -> __Op:
    return __lib.BinaryenStringEncodeLossyUTF8Array()


def StringEncodeWTF8Array() -> __Op:
    return __lib.BinaryenStringEncodeWTF8Array()


def StringEncodeWTF16Array() -> __Op:
    return __lib.BinaryenStringEncodeWTF16Array()


def StringAsWTF8() -> __Op:
    return __lib.BinaryenStringAsWTF8()


def StringAsWTF16() -> __Op:
    return __lib.BinaryenStringAsWTF16()


def StringAsIter() -> __Op:
    return __lib.BinaryenStringAsIter()


def StringIterMoveAdvance() -> __Op:
    return __lib.BinaryenStringIterMoveAdvance()


def StringIterMoveRewind() -> __Op:
    return __lib.BinaryenStringIterMoveRewind()


def StringSliceWTF8() -> __Op:
    return __lib.BinaryenStringSliceWTF8()


def StringSliceWTF16() -> __Op:
    return __lib.BinaryenStringSliceWTF16()


def StringEqEqual() -> __Op:
    return __lib.BinaryenStringEqEqual()


def StringEqCompare() -> __Op:
    return __lib.BinaryenStringEqCompare()
