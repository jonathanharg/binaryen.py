from .lib import lib as _lib
from .internals import BinaryenOp as _BinaryenOp

# Vim Macro
# 8ly$0iTabreturn _lib.EscOdef EscpA:EscjoEscj0

def CtzInt32() -> _BinaryenOp:
    return _lib.BinaryenCtzInt32()

def PopcntInt32() -> _BinaryenOp:
    return _lib.BinaryenPopcntInt32()

def NegFloat32() -> _BinaryenOp:
    return _lib.BinaryenNegFloat32()

def AbsFloat32() -> _BinaryenOp:
    return _lib.BinaryenAbsFloat32()

def CeilFloat32() -> _BinaryenOp:
    return _lib.BinaryenCeilFloat32()

def FloorFloat32() -> _BinaryenOp:
    return _lib.BinaryenFloorFloat32()

def TruncFloat32() -> _BinaryenOp:
    return _lib.BinaryenTruncFloat32()

def NearestFloat32() -> _BinaryenOp:
    return _lib.BinaryenNearestFloat32()

def SqrtFloat32() -> _BinaryenOp:
    return _lib.BinaryenSqrtFloat32()

def EqZInt32() -> _BinaryenOp:
    return _lib.BinaryenEqZInt32()

def ClzInt64() -> _BinaryenOp:
    return _lib.BinaryenClzInt64()

def CtzInt64() -> _BinaryenOp:
    return _lib.BinaryenCtzInt64()

def PopcntInt64() -> _BinaryenOp:
    return _lib.BinaryenPopcntInt64()

def NegFloat64() -> _BinaryenOp:
    return _lib.BinaryenNegFloat64()

def AbsFloat64() -> _BinaryenOp:
    return _lib.BinaryenAbsFloat64()

def CeilFloat64() -> _BinaryenOp:
    return _lib.BinaryenCeilFloat64()

def FloorFloat64() -> _BinaryenOp:
    return _lib.BinaryenFloorFloat64()

def TruncFloat64() -> _BinaryenOp:
    return _lib.BinaryenTruncFloat64()

def NearestFloat64() -> _BinaryenOp:
    return _lib.BinaryenNearestFloat64()

def SqrtFloat64() -> _BinaryenOp:
    return _lib.BinaryenSqrtFloat64()

def EqZInt64() -> _BinaryenOp:
    return _lib.BinaryenEqZInt64()

def ExtendSInt32() -> _BinaryenOp:
    return _lib.BinaryenExtendSInt32()

def ExtendUInt32() -> _BinaryenOp:
    return _lib.BinaryenExtendUInt32()

def WrapInt64() -> _BinaryenOp:
    return _lib.BinaryenWrapInt64()

def TruncSFloat32ToInt32() -> _BinaryenOp:
    return _lib.BinaryenTruncSFloat32ToInt32()

def TruncSFloat32ToInt64() -> _BinaryenOp:
    return _lib.BinaryenTruncSFloat32ToInt64()

def TruncUFloat32ToInt32() -> _BinaryenOp:
    return _lib.BinaryenTruncUFloat32ToInt32()

def TruncUFloat32ToInt64() -> _BinaryenOp:
    return _lib.BinaryenTruncUFloat32ToInt64()

def TruncSFloat64ToInt32() -> _BinaryenOp:
    return _lib.BinaryenTruncSFloat64ToInt32()

def TruncSFloat64ToInt64() -> _BinaryenOp:
    return _lib.BinaryenTruncSFloat64ToInt64()

def TruncUFloat64ToInt32() -> _BinaryenOp:
    return _lib.BinaryenTruncUFloat64ToInt32()

def TruncUFloat64ToInt64() -> _BinaryenOp:
    return _lib.BinaryenTruncUFloat64ToInt64()

def ReinterpretFloat32() -> _BinaryenOp:
    return _lib.BinaryenReinterpretFloat32()

def ReinterpretFloat64() -> _BinaryenOp:
    return _lib.BinaryenReinterpretFloat64()

def ConvertSInt32ToFloat32() -> _BinaryenOp:
    return _lib.BinaryenConvertSInt32ToFloat32()

def ConvertSInt32ToFloat64() -> _BinaryenOp:
    return _lib.BinaryenConvertSInt32ToFloat64()

def ConvertUInt32ToFloat32() -> _BinaryenOp:
    return _lib.BinaryenConvertUInt32ToFloat32()

def ConvertUInt32ToFloat64() -> _BinaryenOp:
    return _lib.BinaryenConvertUInt32ToFloat64()

def ConvertSInt64ToFloat32() -> _BinaryenOp:
    return _lib.BinaryenConvertSInt64ToFloat32()

def ConvertSInt64ToFloat64() -> _BinaryenOp:
    return _lib.BinaryenConvertSInt64ToFloat64()

def ConvertUInt64ToFloat32() -> _BinaryenOp:
    return _lib.BinaryenConvertUInt64ToFloat32()

def ConvertUInt64ToFloat64() -> _BinaryenOp:
    return _lib.BinaryenConvertUInt64ToFloat64()

def PromoteFloat32() -> _BinaryenOp:
    return _lib.BinaryenPromoteFloat32()

def DemoteFloat64() -> _BinaryenOp:
    return _lib.BinaryenDemoteFloat64()

def ReinterpretInt32() -> _BinaryenOp:
    return _lib.BinaryenReinterpretInt32()

def ReinterpretInt64() -> _BinaryenOp:
    return _lib.BinaryenReinterpretInt64()

def ExtendS8Int32() -> _BinaryenOp:
    return _lib.BinaryenExtendS8Int32()

def ExtendS16Int32() -> _BinaryenOp:
    return _lib.BinaryenExtendS16Int32()

def ExtendS8Int64() -> _BinaryenOp:
    return _lib.BinaryenExtendS8Int64()

def ExtendS16Int64() -> _BinaryenOp:
    return _lib.BinaryenExtendS16Int64()

def ExtendS32Int64() -> _BinaryenOp:
    return _lib.BinaryenExtendS32Int64()

def AddInt32() -> _BinaryenOp:
    return _lib.BinaryenAddInt32()

def SubInt32() -> _BinaryenOp:
    return _lib.BinaryenSubInt32()

def MulInt32() -> _BinaryenOp:
    return _lib.BinaryenMulInt32()

def DivSInt32() -> _BinaryenOp:
    return _lib.BinaryenDivSInt32()

def DivUInt32() -> _BinaryenOp:
    return _lib.BinaryenDivUInt32()

def RemSInt32() -> _BinaryenOp:
    return _lib.BinaryenRemSInt32()

def RemUInt32() -> _BinaryenOp:
    return _lib.BinaryenRemUInt32()

def AndInt32() -> _BinaryenOp:
    return _lib.BinaryenAndInt32()

def OrInt32() -> _BinaryenOp:
    return _lib.BinaryenOrInt32()

def XorInt32() -> _BinaryenOp:
    return _lib.BinaryenXorInt32()

def ShlInt32() -> _BinaryenOp:
    return _lib.BinaryenShlInt32()

def ShrUInt32() -> _BinaryenOp:
    return _lib.BinaryenShrUInt32()

def ShrSInt32() -> _BinaryenOp:
    return _lib.BinaryenShrSInt32()

def RotLInt32() -> _BinaryenOp:
    return _lib.BinaryenRotLInt32()

def RotRInt32() -> _BinaryenOp:
    return _lib.BinaryenRotRInt32()

def EqInt32() -> _BinaryenOp:
    return _lib.BinaryenEqInt32()

def NeInt32() -> _BinaryenOp:
    return _lib.BinaryenNeInt32()

def LtSInt32() -> _BinaryenOp:
    return _lib.BinaryenLtSInt32()

def LtUInt32() -> _BinaryenOp:
    return _lib.BinaryenLtUInt32()

def LeSInt32() -> _BinaryenOp:
    return _lib.BinaryenLeSInt32()

def LeUInt32() -> _BinaryenOp:
    return _lib.BinaryenLeUInt32()

def GtSInt32() -> _BinaryenOp:
    return _lib.BinaryenGtSInt32()

def GtUInt32() -> _BinaryenOp:
    return _lib.BinaryenGtUInt32()

def GeSInt32() -> _BinaryenOp:
    return _lib.BinaryenGeSInt32()

def GeUInt32() -> _BinaryenOp:
    return _lib.BinaryenGeUInt32()

def AddInt64() -> _BinaryenOp:
    return _lib.BinaryenAddInt64()

def SubInt64() -> _BinaryenOp:
    return _lib.BinaryenSubInt64()

def MulInt64() -> _BinaryenOp:
    return _lib.BinaryenMulInt64()

def DivSInt64() -> _BinaryenOp:
    return _lib.BinaryenDivSInt64()

def DivUInt64() -> _BinaryenOp:
    return _lib.BinaryenDivUInt64()

def RemSInt64() -> _BinaryenOp:
    return _lib.BinaryenRemSInt64()

def RemUInt64() -> _BinaryenOp:
    return _lib.BinaryenRemUInt64()

def AndInt64() -> _BinaryenOp:
    return _lib.BinaryenAndInt64()

def OrInt64() -> _BinaryenOp:
    return _lib.BinaryenOrInt64()

def XorInt64() -> _BinaryenOp:
    return _lib.BinaryenXorInt64()

def ShlInt64() -> _BinaryenOp:
    return _lib.BinaryenShlInt64()

def ShrUInt64() -> _BinaryenOp:
    return _lib.BinaryenShrUInt64()

def ShrSInt64() -> _BinaryenOp:
    return _lib.BinaryenShrSInt64()

def RotLInt64() -> _BinaryenOp:
    return _lib.BinaryenRotLInt64()

def RotRInt64() -> _BinaryenOp:
    return _lib.BinaryenRotRInt64()

def EqInt64() -> _BinaryenOp:
    return _lib.BinaryenEqInt64()

def NeInt64() -> _BinaryenOp:
    return _lib.BinaryenNeInt64()

def LtSInt64() -> _BinaryenOp:
    return _lib.BinaryenLtSInt64()

def LtUInt64() -> _BinaryenOp:
    return _lib.BinaryenLtUInt64()

def LeSInt64() -> _BinaryenOp:
    return _lib.BinaryenLeSInt64()

def LeUInt64() -> _BinaryenOp:
    return _lib.BinaryenLeUInt64()

def GtSInt64() -> _BinaryenOp:
    return _lib.BinaryenGtSInt64()

def GtUInt64() -> _BinaryenOp:
    return _lib.BinaryenGtUInt64()

def GeSInt64() -> _BinaryenOp:
    return _lib.BinaryenGeSInt64()

def GeUInt64() -> _BinaryenOp:
    return _lib.BinaryenGeUInt64()

def AddFloat32() -> _BinaryenOp:
    return _lib.BinaryenAddFloat32()

def SubFloat32() -> _BinaryenOp:
    return _lib.BinaryenSubFloat32()

def MulFloat32() -> _BinaryenOp:
    return _lib.BinaryenMulFloat32()

def DivFloat32() -> _BinaryenOp:
    return _lib.BinaryenDivFloat32()

def CopySignFloat32() -> _BinaryenOp:
    return _lib.BinaryenCopySignFloat32()

def MinFloat32() -> _BinaryenOp:
    return _lib.BinaryenMinFloat32()

def MaxFloat32() -> _BinaryenOp:
    return _lib.BinaryenMaxFloat32()

def EqFloat32() -> _BinaryenOp:
    return _lib.BinaryenEqFloat32()

def NeFloat32() -> _BinaryenOp:
    return _lib.BinaryenNeFloat32()

def LtFloat32() -> _BinaryenOp:
    return _lib.BinaryenLtFloat32()

def LeFloat32() -> _BinaryenOp:
    return _lib.BinaryenLeFloat32()

def GtFloat32() -> _BinaryenOp:
    return _lib.BinaryenGtFloat32()

def GeFloat32() -> _BinaryenOp:
    return _lib.BinaryenGeFloat32()

def AddFloat64() -> _BinaryenOp:
    return _lib.BinaryenAddFloat64()

def SubFloat64() -> _BinaryenOp:
    return _lib.BinaryenSubFloat64()

def MulFloat64() -> _BinaryenOp:
    return _lib.BinaryenMulFloat64()

def DivFloat64() -> _BinaryenOp:
    return _lib.BinaryenDivFloat64()

def CopySignFloat64() -> _BinaryenOp:
    return _lib.BinaryenCopySignFloat64()

def MinFloat64() -> _BinaryenOp:
    return _lib.BinaryenMinFloat64()

def MaxFloat64() -> _BinaryenOp:
    return _lib.BinaryenMaxFloat64()

def EqFloat64() -> _BinaryenOp:
    return _lib.BinaryenEqFloat64()

def NeFloat64() -> _BinaryenOp:
    return _lib.BinaryenNeFloat64()

def LtFloat64() -> _BinaryenOp:
    return _lib.BinaryenLtFloat64()

def LeFloat64() -> _BinaryenOp:
    return _lib.BinaryenLeFloat64()

def GtFloat64() -> _BinaryenOp:
    return _lib.BinaryenGtFloat64()

def GeFloat64() -> _BinaryenOp:
    return _lib.BinaryenGeFloat64()

def AtomicRMWAdd() -> _BinaryenOp:
    return _lib.BinaryenAtomicRMWAdd()

def AtomicRMWSub() -> _BinaryenOp:
    return _lib.BinaryenAtomicRMWSub()

def AtomicRMWAnd() -> _BinaryenOp:
    return _lib.BinaryenAtomicRMWAnd()

def AtomicRMWOr() -> _BinaryenOp:
    return _lib.BinaryenAtomicRMWOr()

def AtomicRMWXor() -> _BinaryenOp:
    return _lib.BinaryenAtomicRMWXor()

def AtomicRMWXchg() -> _BinaryenOp:
    return _lib.BinaryenAtomicRMWXchg()

def TruncSatSFloat32ToInt32() -> _BinaryenOp:
    return _lib.BinaryenTruncSatSFloat32ToInt32()

def TruncSatSFloat32ToInt64() -> _BinaryenOp:
    return _lib.BinaryenTruncSatSFloat32ToInt64()

def TruncSatUFloat32ToInt32() -> _BinaryenOp:
    return _lib.BinaryenTruncSatUFloat32ToInt32()

def TruncSatUFloat32ToInt64() -> _BinaryenOp:
    return _lib.BinaryenTruncSatUFloat32ToInt64()

def TruncSatSFloat64ToInt32() -> _BinaryenOp:
    return _lib.BinaryenTruncSatSFloat64ToInt32()

def TruncSatSFloat64ToInt64() -> _BinaryenOp:
    return _lib.BinaryenTruncSatSFloat64ToInt64()

def TruncSatUFloat64ToInt32() -> _BinaryenOp:
    return _lib.BinaryenTruncSatUFloat64ToInt32()

def TruncSatUFloat64ToInt64() -> _BinaryenOp:
    return _lib.BinaryenTruncSatUFloat64ToInt64()

def SplatVecI8x16() -> _BinaryenOp:
    return _lib.BinaryenSplatVecI8x16()

def ExtractLaneSVecI8x16() -> _BinaryenOp:
    return _lib.BinaryenExtractLaneSVecI8x16()

def ExtractLaneUVecI8x16() -> _BinaryenOp:
    return _lib.BinaryenExtractLaneUVecI8x16()

def ReplaceLaneVecI8x16() -> _BinaryenOp:
    return _lib.BinaryenReplaceLaneVecI8x16()

def SplatVecI16x8() -> _BinaryenOp:
    return _lib.BinaryenSplatVecI16x8()

def ExtractLaneSVecI16x8() -> _BinaryenOp:
    return _lib.BinaryenExtractLaneSVecI16x8()

def ExtractLaneUVecI16x8() -> _BinaryenOp:
    return _lib.BinaryenExtractLaneUVecI16x8()

def ReplaceLaneVecI16x8() -> _BinaryenOp:
    return _lib.BinaryenReplaceLaneVecI16x8()

def SplatVecI32x4() -> _BinaryenOp:
    return _lib.BinaryenSplatVecI32x4()

def ExtractLaneVecI32x4() -> _BinaryenOp:
    return _lib.BinaryenExtractLaneVecI32x4()

def ReplaceLaneVecI32x4() -> _BinaryenOp:
    return _lib.BinaryenReplaceLaneVecI32x4()

def SplatVecI64x2() -> _BinaryenOp:
    return _lib.BinaryenSplatVecI64x2()

def ExtractLaneVecI64x2() -> _BinaryenOp:
    return _lib.BinaryenExtractLaneVecI64x2()

def ReplaceLaneVecI64x2() -> _BinaryenOp:
    return _lib.BinaryenReplaceLaneVecI64x2()

def SplatVecF32x4() -> _BinaryenOp:
    return _lib.BinaryenSplatVecF32x4()

def ExtractLaneVecF32x4() -> _BinaryenOp:
    return _lib.BinaryenExtractLaneVecF32x4()

def ReplaceLaneVecF32x4() -> _BinaryenOp:
    return _lib.BinaryenReplaceLaneVecF32x4()

def SplatVecF64x2() -> _BinaryenOp:
    return _lib.BinaryenSplatVecF64x2()

def ExtractLaneVecF64x2() -> _BinaryenOp:
    return _lib.BinaryenExtractLaneVecF64x2()

def ReplaceLaneVecF64x2() -> _BinaryenOp:
    return _lib.BinaryenReplaceLaneVecF64x2()

def EqVecI8x16() -> _BinaryenOp:
    return _lib.BinaryenEqVecI8x16()

def NeVecI8x16() -> _BinaryenOp:
    return _lib.BinaryenNeVecI8x16()

def LtSVecI8x16() -> _BinaryenOp:
    return _lib.BinaryenLtSVecI8x16()

def LtUVecI8x16() -> _BinaryenOp:
    return _lib.BinaryenLtUVecI8x16()

def GtSVecI8x16() -> _BinaryenOp:
    return _lib.BinaryenGtSVecI8x16()

def GtUVecI8x16() -> _BinaryenOp:
    return _lib.BinaryenGtUVecI8x16()

def LeSVecI8x16() -> _BinaryenOp:
    return _lib.BinaryenLeSVecI8x16()

def LeUVecI8x16() -> _BinaryenOp:
    return _lib.BinaryenLeUVecI8x16()

def GeSVecI8x16() -> _BinaryenOp:
    return _lib.BinaryenGeSVecI8x16()

def GeUVecI8x16() -> _BinaryenOp:
    return _lib.BinaryenGeUVecI8x16()

def EqVecI16x8() -> _BinaryenOp:
    return _lib.BinaryenEqVecI16x8()

def NeVecI16x8() -> _BinaryenOp:
    return _lib.BinaryenNeVecI16x8()

def LtSVecI16x8() -> _BinaryenOp:
    return _lib.BinaryenLtSVecI16x8()

def LtUVecI16x8() -> _BinaryenOp:
    return _lib.BinaryenLtUVecI16x8()

def GtSVecI16x8() -> _BinaryenOp:
    return _lib.BinaryenGtSVecI16x8()

def GtUVecI16x8() -> _BinaryenOp:
    return _lib.BinaryenGtUVecI16x8()

def LeSVecI16x8() -> _BinaryenOp:
    return _lib.BinaryenLeSVecI16x8()

def LeUVecI16x8() -> _BinaryenOp:
    return _lib.BinaryenLeUVecI16x8()

def GeSVecI16x8() -> _BinaryenOp:
    return _lib.BinaryenGeSVecI16x8()

def GeUVecI16x8() -> _BinaryenOp:
    return _lib.BinaryenGeUVecI16x8()

def EqVecI32x4() -> _BinaryenOp:
    return _lib.BinaryenEqVecI32x4()

def NeVecI32x4() -> _BinaryenOp:
    return _lib.BinaryenNeVecI32x4()

def LtSVecI32x4() -> _BinaryenOp:
    return _lib.BinaryenLtSVecI32x4()

def LtUVecI32x4() -> _BinaryenOp:
    return _lib.BinaryenLtUVecI32x4()

def GtSVecI32x4() -> _BinaryenOp:
    return _lib.BinaryenGtSVecI32x4()

def GtUVecI32x4() -> _BinaryenOp:
    return _lib.BinaryenGtUVecI32x4()

def LeSVecI32x4() -> _BinaryenOp:
    return _lib.BinaryenLeSVecI32x4()

def LeUVecI32x4() -> _BinaryenOp:
    return _lib.BinaryenLeUVecI32x4()

def GeSVecI32x4() -> _BinaryenOp:
    return _lib.BinaryenGeSVecI32x4()

def GeUVecI32x4() -> _BinaryenOp:
    return _lib.BinaryenGeUVecI32x4()

def EqVecI64x2() -> _BinaryenOp:
    return _lib.BinaryenEqVecI64x2()

def NeVecI64x2() -> _BinaryenOp:
    return _lib.BinaryenNeVecI64x2()

def LtSVecI64x2() -> _BinaryenOp:
    return _lib.BinaryenLtSVecI64x2()

def GtSVecI64x2() -> _BinaryenOp:
    return _lib.BinaryenGtSVecI64x2()

def LeSVecI64x2() -> _BinaryenOp:
    return _lib.BinaryenLeSVecI64x2()

def GeSVecI64x2() -> _BinaryenOp:
    return _lib.BinaryenGeSVecI64x2()

def EqVecF32x4() -> _BinaryenOp:
    return _lib.BinaryenEqVecF32x4()

def NeVecF32x4() -> _BinaryenOp:
    return _lib.BinaryenNeVecF32x4()

def LtVecF32x4() -> _BinaryenOp:
    return _lib.BinaryenLtVecF32x4()

def GtVecF32x4() -> _BinaryenOp:
    return _lib.BinaryenGtVecF32x4()

def LeVecF32x4() -> _BinaryenOp:
    return _lib.BinaryenLeVecF32x4()

def GeVecF32x4() -> _BinaryenOp:
    return _lib.BinaryenGeVecF32x4()

def EqVecF64x2() -> _BinaryenOp:
    return _lib.BinaryenEqVecF64x2()

def NeVecF64x2() -> _BinaryenOp:
    return _lib.BinaryenNeVecF64x2()

def LtVecF64x2() -> _BinaryenOp:
    return _lib.BinaryenLtVecF64x2()

def GtVecF64x2() -> _BinaryenOp:
    return _lib.BinaryenGtVecF64x2()

def LeVecF64x2() -> _BinaryenOp:
    return _lib.BinaryenLeVecF64x2()

def GeVecF64x2() -> _BinaryenOp:
    return _lib.BinaryenGeVecF64x2()

def NotVec128() -> _BinaryenOp:
    return _lib.BinaryenNotVec128()

def AndVec128() -> _BinaryenOp:
    return _lib.BinaryenAndVec128()

def OrVec128() -> _BinaryenOp:
    return _lib.BinaryenOrVec128()

def XorVec128() -> _BinaryenOp:
    return _lib.BinaryenXorVec128()

def AndNotVec128() -> _BinaryenOp:
    return _lib.BinaryenAndNotVec128()

def BitselectVec128() -> _BinaryenOp:
    return _lib.BinaryenBitselectVec128()

def RelaxedFmaVecF32x4() -> _BinaryenOp:
    return _lib.BinaryenRelaxedFmaVecF32x4()

def RelaxedFmsVecF32x4() -> _BinaryenOp:
    return _lib.BinaryenRelaxedFmsVecF32x4()

def RelaxedFmaVecF64x2() -> _BinaryenOp:
    return _lib.BinaryenRelaxedFmaVecF64x2()

def RelaxedFmsVecF64x2() -> _BinaryenOp:
    return _lib.BinaryenRelaxedFmsVecF64x2()

def LaneselectI8x16() -> _BinaryenOp:
    return _lib.BinaryenLaneselectI8x16()

def LaneselectI16x8() -> _BinaryenOp:
    return _lib.BinaryenLaneselectI16x8()

def LaneselectI32x4() -> _BinaryenOp:
    return _lib.BinaryenLaneselectI32x4()

def LaneselectI64x2() -> _BinaryenOp:
    return _lib.BinaryenLaneselectI64x2()

def DotI8x16I7x16AddSToVecI32x4() -> _BinaryenOp:
    return _lib.BinaryenDotI8x16I7x16AddSToVecI32x4()

def AnyTrueVec128() -> _BinaryenOp:
    return _lib.BinaryenAnyTrueVec128()

def PopcntVecI8x16() -> _BinaryenOp:
    return _lib.BinaryenPopcntVecI8x16()

def AbsVecI8x16() -> _BinaryenOp:
    return _lib.BinaryenAbsVecI8x16()

def NegVecI8x16() -> _BinaryenOp:
    return _lib.BinaryenNegVecI8x16()

def AllTrueVecI8x16() -> _BinaryenOp:
    return _lib.BinaryenAllTrueVecI8x16()

def BitmaskVecI8x16() -> _BinaryenOp:
    return _lib.BinaryenBitmaskVecI8x16()

def ShlVecI8x16() -> _BinaryenOp:
    return _lib.BinaryenShlVecI8x16()

def ShrSVecI8x16() -> _BinaryenOp:
    return _lib.BinaryenShrSVecI8x16()

def ShrUVecI8x16() -> _BinaryenOp:
    return _lib.BinaryenShrUVecI8x16()

def AddVecI8x16() -> _BinaryenOp:
    return _lib.BinaryenAddVecI8x16()

def AddSatSVecI8x16() -> _BinaryenOp:
    return _lib.BinaryenAddSatSVecI8x16()

def AddSatUVecI8x16() -> _BinaryenOp:
    return _lib.BinaryenAddSatUVecI8x16()

def SubVecI8x16() -> _BinaryenOp:
    return _lib.BinaryenSubVecI8x16()

def SubSatSVecI8x16() -> _BinaryenOp:
    return _lib.BinaryenSubSatSVecI8x16()

def SubSatUVecI8x16() -> _BinaryenOp:
    return _lib.BinaryenSubSatUVecI8x16()

def MinSVecI8x16() -> _BinaryenOp:
    return _lib.BinaryenMinSVecI8x16()

def MinUVecI8x16() -> _BinaryenOp:
    return _lib.BinaryenMinUVecI8x16()

def MaxSVecI8x16() -> _BinaryenOp:
    return _lib.BinaryenMaxSVecI8x16()

def MaxUVecI8x16() -> _BinaryenOp:
    return _lib.BinaryenMaxUVecI8x16()

def AvgrUVecI8x16() -> _BinaryenOp:
    return _lib.BinaryenAvgrUVecI8x16()

def AbsVecI16x8() -> _BinaryenOp:
    return _lib.BinaryenAbsVecI16x8()

def NegVecI16x8() -> _BinaryenOp:
    return _lib.BinaryenNegVecI16x8()

def AllTrueVecI16x8() -> _BinaryenOp:
    return _lib.BinaryenAllTrueVecI16x8()

def BitmaskVecI16x8() -> _BinaryenOp:
    return _lib.BinaryenBitmaskVecI16x8()

def ShlVecI16x8() -> _BinaryenOp:
    return _lib.BinaryenShlVecI16x8()

def ShrSVecI16x8() -> _BinaryenOp:
    return _lib.BinaryenShrSVecI16x8()

def ShrUVecI16x8() -> _BinaryenOp:
    return _lib.BinaryenShrUVecI16x8()

def AddVecI16x8() -> _BinaryenOp:
    return _lib.BinaryenAddVecI16x8()

def AddSatSVecI16x8() -> _BinaryenOp:
    return _lib.BinaryenAddSatSVecI16x8()

def AddSatUVecI16x8() -> _BinaryenOp:
    return _lib.BinaryenAddSatUVecI16x8()

def SubVecI16x8() -> _BinaryenOp:
    return _lib.BinaryenSubVecI16x8()

def SubSatSVecI16x8() -> _BinaryenOp:
    return _lib.BinaryenSubSatSVecI16x8()

def SubSatUVecI16x8() -> _BinaryenOp:
    return _lib.BinaryenSubSatUVecI16x8()

def MulVecI16x8() -> _BinaryenOp:
    return _lib.BinaryenMulVecI16x8()

def MinSVecI16x8() -> _BinaryenOp:
    return _lib.BinaryenMinSVecI16x8()

def MinUVecI16x8() -> _BinaryenOp:
    return _lib.BinaryenMinUVecI16x8()

def MaxSVecI16x8() -> _BinaryenOp:
    return _lib.BinaryenMaxSVecI16x8()

def MaxUVecI16x8() -> _BinaryenOp:
    return _lib.BinaryenMaxUVecI16x8()

def AvgrUVecI16x8() -> _BinaryenOp:
    return _lib.BinaryenAvgrUVecI16x8()

def Q15MulrSatSVecI16x8() -> _BinaryenOp:
    return _lib.BinaryenQ15MulrSatSVecI16x8()

def ExtMulLowSVecI16x8() -> _BinaryenOp:
    return _lib.BinaryenExtMulLowSVecI16x8()

def ExtMulHighSVecI16x8() -> _BinaryenOp:
    return _lib.BinaryenExtMulHighSVecI16x8()

def ExtMulLowUVecI16x8() -> _BinaryenOp:
    return _lib.BinaryenExtMulLowUVecI16x8()

def ExtMulHighUVecI16x8() -> _BinaryenOp:
    return _lib.BinaryenExtMulHighUVecI16x8()

def AbsVecI32x4() -> _BinaryenOp:
    return _lib.BinaryenAbsVecI32x4()

def NegVecI32x4() -> _BinaryenOp:
    return _lib.BinaryenNegVecI32x4()

def AllTrueVecI32x4() -> _BinaryenOp:
    return _lib.BinaryenAllTrueVecI32x4()

def BitmaskVecI32x4() -> _BinaryenOp:
    return _lib.BinaryenBitmaskVecI32x4()

def ShlVecI32x4() -> _BinaryenOp:
    return _lib.BinaryenShlVecI32x4()

def ShrSVecI32x4() -> _BinaryenOp:
    return _lib.BinaryenShrSVecI32x4()

def ShrUVecI32x4() -> _BinaryenOp:
    return _lib.BinaryenShrUVecI32x4()

def AddVecI32x4() -> _BinaryenOp:
    return _lib.BinaryenAddVecI32x4()

def SubVecI32x4() -> _BinaryenOp:
    return _lib.BinaryenSubVecI32x4()

def MulVecI32x4() -> _BinaryenOp:
    return _lib.BinaryenMulVecI32x4()

def MinSVecI32x4() -> _BinaryenOp:
    return _lib.BinaryenMinSVecI32x4()

def MinUVecI32x4() -> _BinaryenOp:
    return _lib.BinaryenMinUVecI32x4()

def MaxSVecI32x4() -> _BinaryenOp:
    return _lib.BinaryenMaxSVecI32x4()

def MaxUVecI32x4() -> _BinaryenOp:
    return _lib.BinaryenMaxUVecI32x4()

def DotSVecI16x8ToVecI32x4() -> _BinaryenOp:
    return _lib.BinaryenDotSVecI16x8ToVecI32x4()

def ExtMulLowSVecI32x4() -> _BinaryenOp:
    return _lib.BinaryenExtMulLowSVecI32x4()

def ExtMulHighSVecI32x4() -> _BinaryenOp:
    return _lib.BinaryenExtMulHighSVecI32x4()

def ExtMulLowUVecI32x4() -> _BinaryenOp:
    return _lib.BinaryenExtMulLowUVecI32x4()

def ExtMulHighUVecI32x4() -> _BinaryenOp:
    return _lib.BinaryenExtMulHighUVecI32x4()

def AbsVecI64x2() -> _BinaryenOp:
    return _lib.BinaryenAbsVecI64x2()

def NegVecI64x2() -> _BinaryenOp:
    return _lib.BinaryenNegVecI64x2()

def AllTrueVecI64x2() -> _BinaryenOp:
    return _lib.BinaryenAllTrueVecI64x2()

def BitmaskVecI64x2() -> _BinaryenOp:
    return _lib.BinaryenBitmaskVecI64x2()

def ShlVecI64x2() -> _BinaryenOp:
    return _lib.BinaryenShlVecI64x2()

def ShrSVecI64x2() -> _BinaryenOp:
    return _lib.BinaryenShrSVecI64x2()

def ShrUVecI64x2() -> _BinaryenOp:
    return _lib.BinaryenShrUVecI64x2()

def AddVecI64x2() -> _BinaryenOp:
    return _lib.BinaryenAddVecI64x2()

def SubVecI64x2() -> _BinaryenOp:
    return _lib.BinaryenSubVecI64x2()

def MulVecI64x2() -> _BinaryenOp:
    return _lib.BinaryenMulVecI64x2()

def ExtMulLowSVecI64x2() -> _BinaryenOp:
    return _lib.BinaryenExtMulLowSVecI64x2()

def ExtMulHighSVecI64x2() -> _BinaryenOp:
    return _lib.BinaryenExtMulHighSVecI64x2()

def ExtMulLowUVecI64x2() -> _BinaryenOp:
    return _lib.BinaryenExtMulLowUVecI64x2()

def ExtMulHighUVecI64x2() -> _BinaryenOp:
    return _lib.BinaryenExtMulHighUVecI64x2()

def AbsVecF32x4() -> _BinaryenOp:
    return _lib.BinaryenAbsVecF32x4()

def NegVecF32x4() -> _BinaryenOp:
    return _lib.BinaryenNegVecF32x4()

def SqrtVecF32x4() -> _BinaryenOp:
    return _lib.BinaryenSqrtVecF32x4()

def AddVecF32x4() -> _BinaryenOp:
    return _lib.BinaryenAddVecF32x4()

def SubVecF32x4() -> _BinaryenOp:
    return _lib.BinaryenSubVecF32x4()

def MulVecF32x4() -> _BinaryenOp:
    return _lib.BinaryenMulVecF32x4()

def DivVecF32x4() -> _BinaryenOp:
    return _lib.BinaryenDivVecF32x4()

def MinVecF32x4() -> _BinaryenOp:
    return _lib.BinaryenMinVecF32x4()

def MaxVecF32x4() -> _BinaryenOp:
    return _lib.BinaryenMaxVecF32x4()

def PMinVecF32x4() -> _BinaryenOp:
    return _lib.BinaryenPMinVecF32x4()

def PMaxVecF32x4() -> _BinaryenOp:
    return _lib.BinaryenPMaxVecF32x4()

def CeilVecF32x4() -> _BinaryenOp:
    return _lib.BinaryenCeilVecF32x4()

def FloorVecF32x4() -> _BinaryenOp:
    return _lib.BinaryenFloorVecF32x4()

def TruncVecF32x4() -> _BinaryenOp:
    return _lib.BinaryenTruncVecF32x4()

def NearestVecF32x4() -> _BinaryenOp:
    return _lib.BinaryenNearestVecF32x4()

def AbsVecF64x2() -> _BinaryenOp:
    return _lib.BinaryenAbsVecF64x2()

def NegVecF64x2() -> _BinaryenOp:
    return _lib.BinaryenNegVecF64x2()

def SqrtVecF64x2() -> _BinaryenOp:
    return _lib.BinaryenSqrtVecF64x2()

def AddVecF64x2() -> _BinaryenOp:
    return _lib.BinaryenAddVecF64x2()

def SubVecF64x2() -> _BinaryenOp:
    return _lib.BinaryenSubVecF64x2()

def MulVecF64x2() -> _BinaryenOp:
    return _lib.BinaryenMulVecF64x2()

def DivVecF64x2() -> _BinaryenOp:
    return _lib.BinaryenDivVecF64x2()

def MinVecF64x2() -> _BinaryenOp:
    return _lib.BinaryenMinVecF64x2()

def MaxVecF64x2() -> _BinaryenOp:
    return _lib.BinaryenMaxVecF64x2()

def PMinVecF64x2() -> _BinaryenOp:
    return _lib.BinaryenPMinVecF64x2()

def PMaxVecF64x2() -> _BinaryenOp:
    return _lib.BinaryenPMaxVecF64x2()

def CeilVecF64x2() -> _BinaryenOp:
    return _lib.BinaryenCeilVecF64x2()

def FloorVecF64x2() -> _BinaryenOp:
    return _lib.BinaryenFloorVecF64x2()

def TruncVecF64x2() -> _BinaryenOp:
    return _lib.BinaryenTruncVecF64x2()

def NearestVecF64x2() -> _BinaryenOp:
    return _lib.BinaryenNearestVecF64x2()

def ExtAddPairwiseSVecI8x16ToI16x8() -> _BinaryenOp:
    return _lib.BinaryenExtAddPairwiseSVecI8x16ToI16x8()

def ExtAddPairwiseUVecI8x16ToI16x8() -> _BinaryenOp:
    return _lib.BinaryenExtAddPairwiseUVecI8x16ToI16x8()

def ExtAddPairwiseSVecI16x8ToI32x4() -> _BinaryenOp:
    return _lib.BinaryenExtAddPairwiseSVecI16x8ToI32x4()

def ExtAddPairwiseUVecI16x8ToI32x4() -> _BinaryenOp:
    return _lib.BinaryenExtAddPairwiseUVecI16x8ToI32x4()

def TruncSatSVecF32x4ToVecI32x4() -> _BinaryenOp:
    return _lib.BinaryenTruncSatSVecF32x4ToVecI32x4()

def TruncSatUVecF32x4ToVecI32x4() -> _BinaryenOp:
    return _lib.BinaryenTruncSatUVecF32x4ToVecI32x4()

def ConvertSVecI32x4ToVecF32x4() -> _BinaryenOp:
    return _lib.BinaryenConvertSVecI32x4ToVecF32x4()

def ConvertUVecI32x4ToVecF32x4() -> _BinaryenOp:
    return _lib.BinaryenConvertUVecI32x4ToVecF32x4()

def Load8SplatVec128() -> _BinaryenOp:
    return _lib.BinaryenLoad8SplatVec128()

def Load16SplatVec128() -> _BinaryenOp:
    return _lib.BinaryenLoad16SplatVec128()

def Load32SplatVec128() -> _BinaryenOp:
    return _lib.BinaryenLoad32SplatVec128()

def Load64SplatVec128() -> _BinaryenOp:
    return _lib.BinaryenLoad64SplatVec128()

def Load8x8SVec128() -> _BinaryenOp:
    return _lib.BinaryenLoad8x8SVec128()

def Load8x8UVec128() -> _BinaryenOp:
    return _lib.BinaryenLoad8x8UVec128()

def Load16x4SVec128() -> _BinaryenOp:
    return _lib.BinaryenLoad16x4SVec128()

def Load16x4UVec128() -> _BinaryenOp:
    return _lib.BinaryenLoad16x4UVec128()

def Load32x2SVec128() -> _BinaryenOp:
    return _lib.BinaryenLoad32x2SVec128()

def Load32x2UVec128() -> _BinaryenOp:
    return _lib.BinaryenLoad32x2UVec128()

def Load32ZeroVec128() -> _BinaryenOp:
    return _lib.BinaryenLoad32ZeroVec128()

def Load64ZeroVec128() -> _BinaryenOp:
    return _lib.BinaryenLoad64ZeroVec128()

def Load8LaneVec128() -> _BinaryenOp:
    return _lib.BinaryenLoad8LaneVec128()

def Load16LaneVec128() -> _BinaryenOp:
    return _lib.BinaryenLoad16LaneVec128()

def Load32LaneVec128() -> _BinaryenOp:
    return _lib.BinaryenLoad32LaneVec128()

def Load64LaneVec128() -> _BinaryenOp:
    return _lib.BinaryenLoad64LaneVec128()

def Store8LaneVec128() -> _BinaryenOp:
    return _lib.BinaryenStore8LaneVec128()

def Store16LaneVec128() -> _BinaryenOp:
    return _lib.BinaryenStore16LaneVec128()

def Store32LaneVec128() -> _BinaryenOp:
    return _lib.BinaryenStore32LaneVec128()

def Store64LaneVec128() -> _BinaryenOp:
    return _lib.BinaryenStore64LaneVec128()

def NarrowSVecI16x8ToVecI8x16() -> _BinaryenOp:
    return _lib.BinaryenNarrowSVecI16x8ToVecI8x16()

def NarrowUVecI16x8ToVecI8x16() -> _BinaryenOp:
    return _lib.BinaryenNarrowUVecI16x8ToVecI8x16()

def NarrowSVecI32x4ToVecI16x8() -> _BinaryenOp:
    return _lib.BinaryenNarrowSVecI32x4ToVecI16x8()

def NarrowUVecI32x4ToVecI16x8() -> _BinaryenOp:
    return _lib.BinaryenNarrowUVecI32x4ToVecI16x8()

def ExtendLowSVecI8x16ToVecI16x8() -> _BinaryenOp:
    return _lib.BinaryenExtendLowSVecI8x16ToVecI16x8()

def ExtendHighSVecI8x16ToVecI16x8() -> _BinaryenOp:
    return _lib.BinaryenExtendHighSVecI8x16ToVecI16x8()

def ExtendLowUVecI8x16ToVecI16x8() -> _BinaryenOp:
    return _lib.BinaryenExtendLowUVecI8x16ToVecI16x8()

def ExtendHighUVecI8x16ToVecI16x8() -> _BinaryenOp:
    return _lib.BinaryenExtendHighUVecI8x16ToVecI16x8()

def ExtendLowSVecI16x8ToVecI32x4() -> _BinaryenOp:
    return _lib.BinaryenExtendLowSVecI16x8ToVecI32x4()

def ExtendHighSVecI16x8ToVecI32x4() -> _BinaryenOp:
    return _lib.BinaryenExtendHighSVecI16x8ToVecI32x4()

def ExtendLowUVecI16x8ToVecI32x4() -> _BinaryenOp:
    return _lib.BinaryenExtendLowUVecI16x8ToVecI32x4()

def ExtendHighUVecI16x8ToVecI32x4() -> _BinaryenOp:
    return _lib.BinaryenExtendHighUVecI16x8ToVecI32x4()

def ExtendLowSVecI32x4ToVecI64x2() -> _BinaryenOp:
    return _lib.BinaryenExtendLowSVecI32x4ToVecI64x2()

def ExtendHighSVecI32x4ToVecI64x2() -> _BinaryenOp:
    return _lib.BinaryenExtendHighSVecI32x4ToVecI64x2()

def ExtendLowUVecI32x4ToVecI64x2() -> _BinaryenOp:
    return _lib.BinaryenExtendLowUVecI32x4ToVecI64x2()

def ExtendHighUVecI32x4ToVecI64x2() -> _BinaryenOp:
    return _lib.BinaryenExtendHighUVecI32x4ToVecI64x2()

def ConvertLowSVecI32x4ToVecF64x2() -> _BinaryenOp:
    return _lib.BinaryenConvertLowSVecI32x4ToVecF64x2()

def ConvertLowUVecI32x4ToVecF64x2() -> _BinaryenOp:
    return _lib.BinaryenConvertLowUVecI32x4ToVecF64x2()

def TruncSatZeroSVecF64x2ToVecI32x4() -> _BinaryenOp:
    return _lib.BinaryenTruncSatZeroSVecF64x2ToVecI32x4()

def TruncSatZeroUVecF64x2ToVecI32x4() -> _BinaryenOp:
    return _lib.BinaryenTruncSatZeroUVecF64x2ToVecI32x4()

def DemoteZeroVecF64x2ToVecF32x4() -> _BinaryenOp:
    return _lib.BinaryenDemoteZeroVecF64x2ToVecF32x4()

def PromoteLowVecF32x4ToVecF64x2() -> _BinaryenOp:
    return _lib.BinaryenPromoteLowVecF32x4ToVecF64x2()

def RelaxedTruncSVecF32x4ToVecI32x4() -> _BinaryenOp:
    return _lib.BinaryenRelaxedTruncSVecF32x4ToVecI32x4()

def RelaxedTruncUVecF32x4ToVecI32x4() -> _BinaryenOp:
    return _lib.BinaryenRelaxedTruncUVecF32x4ToVecI32x4()

def RelaxedTruncZeroSVecF64x2ToVecI32x4() -> _BinaryenOp:
    return _lib.BinaryenRelaxedTruncZeroSVecF64x2ToVecI32x4()

def RelaxedTruncZeroUVecF64x2ToVecI32x4() -> _BinaryenOp:
    return _lib.BinaryenRelaxedTruncZeroUVecF64x2ToVecI32x4()

def SwizzleVecI8x16() -> _BinaryenOp:
    return _lib.BinaryenSwizzleVecI8x16()

def RelaxedSwizzleVecI8x16() -> _BinaryenOp:
    return _lib.BinaryenRelaxedSwizzleVecI8x16()

def RelaxedMinVecF32x4() -> _BinaryenOp:
    return _lib.BinaryenRelaxedMinVecF32x4()

def RelaxedMaxVecF32x4() -> _BinaryenOp:
    return _lib.BinaryenRelaxedMaxVecF32x4()

def RelaxedMinVecF64x2() -> _BinaryenOp:
    return _lib.BinaryenRelaxedMinVecF64x2()

def RelaxedMaxVecF64x2() -> _BinaryenOp:
    return _lib.BinaryenRelaxedMaxVecF64x2()

def RelaxedQ15MulrSVecI16x8() -> _BinaryenOp:
    return _lib.BinaryenRelaxedQ15MulrSVecI16x8()

def DotI8x16I7x16SToVecI16x8() -> _BinaryenOp:
    return _lib.BinaryenDotI8x16I7x16SToVecI16x8()

def RefAsNonNull() -> _BinaryenOp:
    return _lib.BinaryenRefAsNonNull()

def RefAsExternInternalize() -> _BinaryenOp:
    return _lib.BinaryenRefAsExternInternalize()

def RefAsExternExternalize() -> _BinaryenOp:
    return _lib.BinaryenRefAsExternExternalize()

def BrOnNull() -> _BinaryenOp:
    return _lib.BinaryenBrOnNull()

def BrOnNonNull() -> _BinaryenOp:
    return _lib.BinaryenBrOnNonNull()

def BrOnCast() -> _BinaryenOp:
    return _lib.BinaryenBrOnCast()

def BrOnCastFail() -> _BinaryenOp:
    return _lib.BinaryenBrOnCastFail()

def StringNewUTF8() -> _BinaryenOp:
    return _lib.BinaryenStringNewUTF8()

def StringNewWTF8() -> _BinaryenOp:
    return _lib.BinaryenStringNewWTF8()

def StringNewLossyUTF8() -> _BinaryenOp:
    return _lib.BinaryenStringNewLossyUTF8()

def StringNewWTF16() -> _BinaryenOp:
    return _lib.BinaryenStringNewWTF16()

def StringNewUTF8Array() -> _BinaryenOp:
    return _lib.BinaryenStringNewUTF8Array()

def StringNewWTF8Array() -> _BinaryenOp:
    return _lib.BinaryenStringNewWTF8Array()

def StringNewLossyUTF8Array() -> _BinaryenOp:
    return _lib.BinaryenStringNewLossyUTF8Array()

def StringNewWTF16Array() -> _BinaryenOp:
    return _lib.BinaryenStringNewWTF16Array()

def StringNewFromCodePoint() -> _BinaryenOp:
    return _lib.BinaryenStringNewFromCodePoint()

def StringMeasureUTF8() -> _BinaryenOp:
    return _lib.BinaryenStringMeasureUTF8()

def StringMeasureWTF8() -> _BinaryenOp:
    return _lib.BinaryenStringMeasureWTF8()

def StringMeasureWTF16() -> _BinaryenOp:
    return _lib.BinaryenStringMeasureWTF16()

def StringMeasureIsUSV() -> _BinaryenOp:
    return _lib.BinaryenStringMeasureIsUSV()

def StringMeasureWTF16View() -> _BinaryenOp:
    return _lib.BinaryenStringMeasureWTF16View()

def StringEncodeUTF8() -> _BinaryenOp:
    return _lib.BinaryenStringEncodeUTF8()

def StringEncodeLossyUTF8() -> _BinaryenOp:
    return _lib.BinaryenStringEncodeLossyUTF8()

def StringEncodeWTF8() -> _BinaryenOp:
    return _lib.BinaryenStringEncodeWTF8()

def StringEncodeWTF16() -> _BinaryenOp:
    return _lib.BinaryenStringEncodeWTF16()

def StringEncodeUTF8Array() -> _BinaryenOp:
    return _lib.BinaryenStringEncodeUTF8Array()

def StringEncodeLossyUTF8Array() -> _BinaryenOp:
    return _lib.BinaryenStringEncodeLossyUTF8Array()

def StringEncodeWTF8Array() -> _BinaryenOp:
    return _lib.BinaryenStringEncodeWTF8Array()

def StringEncodeWTF16Array() -> _BinaryenOp:
    return _lib.BinaryenStringEncodeWTF16Array()

def StringAsWTF8() -> _BinaryenOp:
    return _lib.BinaryenStringAsWTF8()

def StringAsWTF16() -> _BinaryenOp:
    return _lib.BinaryenStringAsWTF16()

def StringAsIter() -> _BinaryenOp:
    return _lib.BinaryenStringAsIter()

def StringIterMoveAdvance() -> _BinaryenOp:
    return _lib.BinaryenStringIterMoveAdvance()

def StringIterMoveRewind() -> _BinaryenOp:
    return _lib.BinaryenStringIterMoveRewind()

def StringSliceWTF8() -> _BinaryenOp:
    return _lib.BinaryenStringSliceWTF8()

def StringSliceWTF16() -> _BinaryenOp:
    return _lib.BinaryenStringSliceWTF16()

def StringEqEqual() -> _BinaryenOp:
    return _lib.BinaryenStringEqEqual()

def StringEqCompare() -> _BinaryenOp:
    return _lib.BinaryenStringEqCompare()

