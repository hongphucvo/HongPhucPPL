import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_1(self):
        input = r"""class b_45 extends b_98 {
b_25(boolean[10] b_55, b_29; b_91[6] b_34) {
void[3] b_90, b_30 = b_66;
if b_74[b_23] != b_5.b_21 then
break;
else
return (0.68 && 20) / b_52;
}
}
"""
        expect = str(Program([ClassDecl(Id("b_45"), [MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_55"), ArrayType(10, BoolType()), None), VarDecl(Id("b_29"), ArrayType(10, BoolType()), None), VarDecl(Id("b_34"), ArrayType(6, ClassType(Id("b_91"))), None)], None, Block([VarDecl(Id("b_90"), ArrayType(3, VoidType()), None), VarDecl(Id("b_30"), ArrayType(3, VoidType()), Id("b_66"))], [If(BinaryOp("!=", ArrayCell(Id("b_74"), Id("b_23")), FieldAccess(Id("b_5"), Id("b_21"))), Break(), Return(BinaryOp("/", BinaryOp("&&", FloatLiteral(0.68), IntLiteral(20)), Id("b_52"))))]))], Id("b_98"))]))
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_2(self):
        input = r"""class b_94 {
static boolean[8] b_18 = {0.23}, b_35;
}
"""
        expect = str(Program([ClassDecl(Id("b_94"), [AttributeDecl(Static(), VarDecl(Id("b_18"), ArrayType(8, BoolType()), ArrayLiteral([FloatLiteral(0.23)]))), AttributeDecl(Static(), VarDecl(Id("b_35"), ArrayType(8, BoolType()), None))], None)]))
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_3(self):
        input = r"""class b_7 extends b_30 {
b_63(boolean[7] b_29, b_17; boolean b_65) {
}
}
"""
        expect = str(Program([ClassDecl(Id("b_7"), [MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_29"), ArrayType(7, BoolType()), None), VarDecl(Id("b_17"), ArrayType(7, BoolType()), None), VarDecl(Id("b_65"), BoolType(), None)], None, Block([], []))], Id("b_30"))]))
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_4(self):
        input = r"""class b_66 extends b_31 {
b_28[10] b_72, b_88;
}
"""
        expect = str(Program([ClassDecl(Id("b_66"), [AttributeDecl(Instance(), VarDecl(Id("b_72"), ArrayType(10, ClassType(Id("b_28"))), None)), AttributeDecl(Instance(), VarDecl(Id("b_88"), ArrayType(10, ClassType(Id("b_28"))), None))], Id("b_31"))]))
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_5(self):
        input = r"""class b_32 extends b_43 {
b_69(boolean[1] b_4, b_85; float b_51) {
boolean[10] b_63 = b_58.b_62.b_17((b_55[{true}] ^ 0.27), b_96[(b_1 * b_10)]);
return this;
}
}
"""
        expect = str(Program([ClassDecl(Id("b_32"), [MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_4"), ArrayType(1, BoolType()), None), VarDecl(Id("b_85"), ArrayType(1, BoolType()), None), VarDecl(Id("b_51"), FloatType(), None)], None, Block([VarDecl(Id("b_63"), ArrayType(10, BoolType()), CallExpr(FieldAccess(Id("b_58"), Id("b_62")), Id("b_17"), [BinaryOp("^", ArrayCell(Id("b_55"), ArrayLiteral([BooleanLiteral(True)])), FloatLiteral(0.27)), ArrayCell(Id("b_96"), BinaryOp("*", Id("b_1"), Id("b_10")))]))], [Return(SelfLiteral())]))], Id("b_43"))]))
        self.assertTrue(TestAST.test(input, expect, 304))

    def test_6(self):
        input = r"""class b_23 {
b_26(int b_15, b_78; float b_3) {
break;
}
}
"""
        expect = str(Program([ClassDecl(Id("b_23"), [MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_15"), IntType(), None), VarDecl(Id("b_78"), IntType(), None), VarDecl(Id("b_3"), FloatType(), None)], None, Block([], [Break()]))], None)]))
        self.assertTrue(TestAST.test(input, expect, 305))

    def test_7(self):
        input = r"""class b_9 extends b_6 {
b_59(b_53[1] b_39, b_94; boolean b_36) {
string b_19;
continue;
}
}
"""
        expect = str(Program([ClassDecl(Id("b_9"), [MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_39"), ArrayType(1, ClassType(Id("b_53"))), None), VarDecl(Id("b_94"), ArrayType(1, ClassType(Id("b_53"))), None), VarDecl(Id("b_36"), BoolType(), None)], None, Block([VarDecl(Id("b_19"), StringType(), None)], [Continue()]))], Id("b_6"))]))
        self.assertTrue(TestAST.test(input, expect, 306))

    def test_8(self):
        input = r"""class b_69 extends b_31 {
b_76 b_100(string b_86, b_13; b_43 b_4) {
b_96.b_7(b_15.b_26, {0.81, false, "string literal", this, nil});
}
}
"""
        expect = str(Program([ClassDecl(Id("b_69"), [MethodDecl(Instance(), Id("b_100"), [VarDecl(Id("b_86"), StringType(), None), VarDecl(Id("b_13"), StringType(), None), VarDecl(Id("b_4"), ClassType(Id("b_43")), None)], ClassType(Id("b_76")), Block([], [CallStmt(Id("b_96"), Id("b_7"), [FieldAccess(Id("b_15"), Id("b_26")), ArrayLiteral([FloatLiteral(0.81), BooleanLiteral(False), StringLiteral('"string literal"'), SelfLiteral(), NullLiteral()])])]))], Id("b_31"))]))
        self.assertTrue(TestAST.test(input, expect, 307))

    def test_9(self):
        input = r"""class b_18 {
float b_82(b_27[7] b_57, b_12; int b_77) {
boolean[9] b_60;
b_9 := b_83;
}
}
"""
        expect = str(Program([ClassDecl(Id("b_18"), [MethodDecl(Instance(), Id("b_82"), [VarDecl(Id("b_57"), ArrayType(7, ClassType(Id("b_27"))), None), VarDecl(Id("b_12"), ArrayType(7, ClassType(Id("b_27"))), None), VarDecl(Id("b_77"), IntType(), None)], FloatType(), Block([VarDecl(Id("b_60"), ArrayType(9, BoolType()), None)], [Assign(Id("b_9"), Id("b_83"))]))], None)]))
        self.assertTrue(TestAST.test(input, expect, 308))

    def test_10(self):
        input = r"""class b_11 extends b_50 {
float b_40(string[5] b_81, b_36; string b_9) {
boolean[7] b_72, b_7;
}
}
"""
        expect = str(Program([ClassDecl(Id("b_11"), [MethodDecl(Instance(), Id("b_40"), [VarDecl(Id("b_81"), ArrayType(5, StringType()), None), VarDecl(Id("b_36"), ArrayType(5, StringType()), None), VarDecl(Id("b_9"), StringType(), None)], FloatType(), Block([VarDecl(Id("b_72"), ArrayType(7, BoolType()), None), VarDecl(Id("b_7"), ArrayType(7, BoolType()), None)], []))], Id("b_50"))]))
        self.assertTrue(TestAST.test(input, expect, 309))

    def test_11(self):
        input = r"""class b_16 extends b_26 {
string b_30(string[8] b_28, b_37; int b_82) {
boolean[2] b_54;
continue;
}
}
"""
        expect = str(Program([ClassDecl(Id("b_16"), [MethodDecl(Instance(), Id("b_30"), [VarDecl(Id("b_28"), ArrayType(8, StringType()), None), VarDecl(Id("b_37"), ArrayType(8, StringType()), None), VarDecl(Id("b_82"), IntType(), None)], StringType(), Block([VarDecl(Id("b_54"), ArrayType(2, BoolType()), None)], [Continue()]))], Id("b_26"))]))
        self.assertTrue(TestAST.test(input, expect, 310))

    def test_12(self):
        input = r"""class b_45 extends b_49 {
float b_83(void[3] b_54, b_88; b_93 b_56) {
return (b_36 - b_76);
}
}
"""
        expect = str(Program([ClassDecl(Id("b_45"), [MethodDecl(Instance(), Id("b_83"), [VarDecl(Id("b_54"), ArrayType(3, VoidType()), None), VarDecl(Id("b_88"), ArrayType(3, VoidType()), None), VarDecl(Id("b_56"), ClassType(Id("b_93")), None)], FloatType(), Block([], [Return(BinaryOp("-", Id("b_36"), Id("b_76")))]))], Id("b_49"))]))
        self.assertTrue(TestAST.test(input, expect, 311))

    def test_13(self):
        input = r"""class b_98 {
b_44(int[7] b_81, b_88; boolean[1] b_39) {
}
}
"""
        expect = str(Program([ClassDecl(Id("b_98"), [MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_81"), ArrayType(7, IntType()), None), VarDecl(Id("b_88"), ArrayType(7, IntType()), None), VarDecl(Id("b_39"), ArrayType(1, BoolType()), None)], None, Block([], []))], None)]))
        self.assertTrue(TestAST.test(input, expect, 312))

    def test_14(self):
        input = r"""class b_19 {
b_66(string b_45, b_96; float b_60) {
float[8] b_89 = "string literal" && this && 4, b_10;
{
}
}
}
"""
        expect = str(Program([ClassDecl(Id("b_19"), [MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_45"), StringType(), None), VarDecl(Id("b_96"), StringType(), None), VarDecl(Id("b_60"), FloatType(), None)], None, Block([VarDecl(Id("b_89"), ArrayType(8, FloatType()), BinaryOp("&&", BinaryOp("&&", StringLiteral('"string literal"'), SelfLiteral()), IntLiteral(4))), VarDecl(Id("b_10"), ArrayType(8, FloatType()), None)], [Block([], [])]))], None)]))
        self.assertTrue(TestAST.test(input, expect, 313))

    def test_15(self):
        input = r"""class b_92 extends b_68 {
b_99 b_10(b_76 b_0, b_42; string[4] b_14) {
{
return b_96[b_94];
}
}
}
"""
        expect = str(Program([ClassDecl(Id("b_92"), [MethodDecl(Instance(), Id("b_10"), [VarDecl(Id("b_0"), ClassType(Id("b_76")), None), VarDecl(Id("b_42"), ClassType(Id("b_76")), None), VarDecl(Id("b_14"), ArrayType(4, StringType()), None)], ClassType(Id("b_99")), Block([], [Block([], [Return(ArrayCell(Id("b_96"), Id("b_94")))])]))], Id("b_68"))]))
        self.assertTrue(TestAST.test(input, expect, 314))

    def test_16(self):
        input = r"""class b_88 {
b_99(b_48 b_79, b_89; boolean b_75) {
void b_42, b_61 = (b_56.b_78((b_52 / "string literal"), b_3) || b_87);
b_28.b_89((11 - "string literal"), b_33);
}
}
"""
        expect = str(Program([ClassDecl(Id("b_88"), [MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_79"), ClassType(Id("b_48")), None), VarDecl(Id("b_89"), ClassType(Id("b_48")), None), VarDecl(Id("b_75"), BoolType(), None)], None, Block([VarDecl(Id("b_42"), VoidType(), None), VarDecl(Id("b_61"), VoidType(), BinaryOp("||", CallExpr(Id("b_56"), Id("b_78"), [BinaryOp("/", Id("b_52"), StringLiteral('"string literal"')), Id("b_3")]), Id("b_87")))], [CallStmt(Id("b_28"), Id("b_89"), [BinaryOp("-", IntLiteral(11), StringLiteral('"string literal"')), Id("b_33")])]))], None)]))
        self.assertTrue(TestAST.test(input, expect, 315))

    def test_17(self):
        input = r"""class b_76 extends b_99 {
b_80 b_86(string b_14, b_89; boolean[5] b_86) {
b_26.b_79(b_26[b_39], b_63);
}
}
"""
        expect = str(Program([ClassDecl(Id("b_76"), [MethodDecl(Instance(), Id("b_86"), [VarDecl(Id("b_14"), StringType(), None), VarDecl(Id("b_89"), StringType(), None), VarDecl(Id("b_86"), ArrayType(5, BoolType()), None)], ClassType(Id("b_80")), Block([], [CallStmt(Id("b_26"), Id("b_79"), [ArrayCell(Id("b_26"), Id("b_39")), Id("b_63")])]))], Id("b_99"))]))
        self.assertTrue(TestAST.test(input, expect, 316))

    def test_18(self):
        input = r"""class b_39 {
void b_17(string b_46, b_21; void[10] b_30) {
continue;
}
}
"""
        expect = str(Program([ClassDecl(Id("b_39"), [MethodDecl(Instance(), Id("b_17"), [VarDecl(Id("b_46"), StringType(), None), VarDecl(Id("b_21"), StringType(), None), VarDecl(Id("b_30"), ArrayType(10, VoidType()), None)], VoidType(), Block([], [Continue()]))], None)]))
        self.assertTrue(TestAST.test(input, expect, 317))

    def test_19(self):
        input = r"""class b_32 extends b_10 {
b_97[9] b_96 = (b_36[b_60] + b_88), b_76 = b_25.b_50.b_65 || b_57.b_10.b_85 - b_47;
}
"""
        expect = str(Program([ClassDecl(Id("b_32"), [AttributeDecl(Instance(), VarDecl(Id("b_96"), ArrayType(9, ClassType(Id("b_97"))), BinaryOp("+", ArrayCell(Id("b_36"), Id("b_60")), Id("b_88")))), AttributeDecl(Instance(), VarDecl(Id("b_76"), ArrayType(9, ClassType(Id("b_97"))), BinaryOp("||", FieldAccess(FieldAccess(Id("b_25"), Id("b_50")), Id("b_65")), BinaryOp("-", FieldAccess(FieldAccess(Id("b_57"), Id("b_10")), Id("b_85")), Id("b_47")))))], Id("b_10"))]))
        self.assertTrue(TestAST.test(input, expect, 318))

    def test_20(self):
        input = r"""class b_84 {
final b_80 b_0, b_12;
}
"""
        expect = str(Program([ClassDecl(Id("b_84"), [AttributeDecl(Instance(), ConstDecl(Id("b_0"), ClassType(Id("b_80")), None)), AttributeDecl(Instance(), ConstDecl(Id("b_12"), ClassType(Id("b_80")), None))], None)]))
        self.assertTrue(TestAST.test(input, expect, 319))

    def test_21(self):
        input = r"""class b_37 {
static float[1] b_77 = b_50, b_81 = b_15;
}
"""
        expect = str(Program([ClassDecl(Id("b_37"), [AttributeDecl(Static(), VarDecl(Id("b_77"), ArrayType(1, FloatType()), Id("b_50"))), AttributeDecl(Static(), VarDecl(Id("b_81"), ArrayType(1, FloatType()), Id("b_15")))], None)]))
        self.assertTrue(TestAST.test(input, expect, 320))

    def test_22(self):
        input = r"""class b_5 extends b_41 {
static string[9] b_75 = "string literal";
}
"""
        expect = str(Program([ClassDecl(Id("b_5"), [AttributeDecl(Static(), VarDecl(Id("b_75"), ArrayType(9, StringType()), StringLiteral('"string literal"')))], Id("b_41"))]))
        self.assertTrue(TestAST.test(input, expect, 321))

    def test_23(self):
        input = r"""class b_11 extends b_29 {
string[8] b_9 = (b_48.b_67 || {true, nil});
}
"""
        expect = str(Program([ClassDecl(Id("b_11"), [AttributeDecl(Instance(), VarDecl(Id("b_9"), ArrayType(8, StringType()), BinaryOp("||", FieldAccess(Id("b_48"), Id("b_67")), ArrayLiteral([BooleanLiteral(True), NullLiteral()]))))], Id("b_29"))]))
        self.assertTrue(TestAST.test(input, expect, 322))

    def test_24(self):
        input = r"""class b_8 {
static void[7] b_0 = (b_31 - b_77[{nil, 14, this, 0.35} * this]), b_38;
}
"""
        expect = str(Program([ClassDecl(Id("b_8"), [AttributeDecl(Static(), VarDecl(Id("b_0"), ArrayType(7, VoidType()), BinaryOp("-", Id("b_31"), ArrayCell(Id("b_77"), BinaryOp("*", ArrayLiteral([NullLiteral(), IntLiteral(14), SelfLiteral(), FloatLiteral(0.35)]), SelfLiteral()))))), AttributeDecl(Static(), VarDecl(Id("b_38"), ArrayType(7, VoidType()), None))], None)]))
        self.assertTrue(TestAST.test(input, expect, 323))

    def test_25(self):
        input = r"""class b_4 {
int b_1(void[7] b_63, b_8; float[4] b_1) {
int b_98 = (b_89[b_76] - b_86 * true), b_28;
break;
}
}
"""
        expect = str(Program([ClassDecl(Id("b_4"), [MethodDecl(Instance(), Id("b_1"), [VarDecl(Id("b_63"), ArrayType(7, VoidType()), None), VarDecl(Id("b_8"), ArrayType(7, VoidType()), None), VarDecl(Id("b_1"), ArrayType(4, FloatType()), None)], IntType(), Block([VarDecl(Id("b_98"), IntType(), BinaryOp("-", ArrayCell(Id("b_89"), Id("b_76")), BinaryOp("*", Id("b_86"), BooleanLiteral(True)))), VarDecl(Id("b_28"), IntType(), None)], [Break()]))], None)]))
        self.assertTrue(TestAST.test(input, expect, 324))

    def test_26(self):
        input = r"""class b_74 {
string b_50(boolean b_55, b_0; b_38 b_64) {
}
}
"""
        expect = str(Program([ClassDecl(Id("b_74"), [MethodDecl(Instance(), Id("b_50"), [VarDecl(Id("b_55"), BoolType(), None), VarDecl(Id("b_0"), BoolType(), None), VarDecl(Id("b_64"), ClassType(Id("b_38")), None)], StringType(), Block([], []))], None)]))
        self.assertTrue(TestAST.test(input, expect, 325))

    def test_27(self):
        input = r"""class b_47 extends b_33 {
b_59(int b_53, b_17; void b_56) {
b_83 b_15 = b_32;
}
}
"""
        expect = str(Program([ClassDecl(Id("b_47"), [MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_53"), IntType(), None), VarDecl(Id("b_17"), IntType(), None), VarDecl(Id("b_56"), VoidType(), None)], None, Block([VarDecl(Id("b_15"), ClassType(Id("b_83")), Id("b_32"))], []))], Id("b_33"))]))
        self.assertTrue(TestAST.test(input, expect, 326))

    def test_28(self):
        input = r"""class b_55 extends b_46 {
int b_40(void[3] b_4, b_100; boolean[10] b_30) {
void b_34 = b_55 || this, b_85;
}
}
"""
        expect = str(Program([ClassDecl(Id("b_55"), [MethodDecl(Instance(), Id("b_40"), [VarDecl(Id("b_4"), ArrayType(3, VoidType()), None), VarDecl(Id("b_100"), ArrayType(3, VoidType()), None), VarDecl(Id("b_30"), ArrayType(10, BoolType()), None)], IntType(), Block([VarDecl(Id("b_34"), VoidType(), BinaryOp("||", Id("b_55"), SelfLiteral())), VarDecl(Id("b_85"), VoidType(), None)], []))], Id("b_46"))]))
        self.assertTrue(TestAST.test(input, expect, 327))

    def test_29(self):
        input = r"""class b_19 {
float b_48(int[10] b_63, b_68; float b_14) {
}
}
"""
        expect = str(Program([ClassDecl(Id("b_19"), [MethodDecl(Instance(), Id("b_48"), [VarDecl(Id("b_63"), ArrayType(10, IntType()), None), VarDecl(Id("b_68"), ArrayType(10, IntType()), None), VarDecl(Id("b_14"), FloatType(), None)], FloatType(), Block([], []))], None)]))
        self.assertTrue(TestAST.test(input, expect, 328))

    def test_30(self):
        input = r"""class b_21 {
final void b_57, b_60 = b_18;
}
"""
        expect = str(Program([ClassDecl(Id("b_21"), [AttributeDecl(Instance(), ConstDecl(Id("b_57"), VoidType(), None)), AttributeDecl(Instance(), ConstDecl(Id("b_60"), VoidType(), Id("b_18")))], None)]))
        self.assertTrue(TestAST.test(input, expect, 329))

    def test_31(self):
        input = r"""class b_77 {
string b_90(string[6] b_1, b_45; b_13[9] b_23) {
this.b_25 := this;
}
}
"""
        expect = str(Program([ClassDecl(Id("b_77"), [MethodDecl(Instance(), Id("b_90"), [VarDecl(Id("b_1"), ArrayType(6, StringType()), None), VarDecl(Id("b_45"), ArrayType(6, StringType()), None), VarDecl(Id("b_23"), ArrayType(9, ClassType(Id("b_13"))), None)], StringType(), Block([], [Assign(FieldAccess(SelfLiteral(), Id("b_25")), SelfLiteral())]))], None)]))
        self.assertTrue(TestAST.test(input, expect, 330))

    def test_32(self):
        input = r"""class b_81 {
static void[9] b_1;
}
"""
        expect = str(Program([ClassDecl(Id("b_81"), [AttributeDecl(Static(), VarDecl(Id("b_1"), ArrayType(9, VoidType()), None))], None)]))
        self.assertTrue(TestAST.test(input, expect, 331))

    def test_33(self):
        input = r"""class b_38 extends b_9 {
b_60(boolean[2] b_1, b_81; int[3] b_9) {
}
}
"""
        expect = str(Program([ClassDecl(Id("b_38"), [MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_1"), ArrayType(2, BoolType()), None), VarDecl(Id("b_81"), ArrayType(2, BoolType()), None), VarDecl(Id("b_9"), ArrayType(3, IntType()), None)], None, Block([], []))], Id("b_9"))]))
        self.assertTrue(TestAST.test(input, expect, 332))

    def test_34(self):
        input = r"""class b_97 {
int b_69(string b_54, b_46; int[1] b_12) {
int b_98 = b_80, b_0 = b_62;
if {this, true, 15} >= (b_55 / b_75.b_72((b_71[b_87 - b_30] && nil), b_94)) - this - b_59[b_95 && "string literal"] then
return 0.15;
}
}
"""
        expect = str(Program([ClassDecl(Id("b_97"), [MethodDecl(Instance(), Id("b_69"), [VarDecl(Id("b_54"), StringType(), None), VarDecl(Id("b_46"), StringType(), None), VarDecl(Id("b_12"), ArrayType(1, IntType()), None)], IntType(), Block([VarDecl(Id("b_98"), IntType(), Id("b_80")), VarDecl(Id("b_0"), IntType(), Id("b_62"))], [If(BinaryOp(">=", ArrayLiteral([SelfLiteral(), BooleanLiteral(True), IntLiteral(15)]), BinaryOp("-", BinaryOp("-", BinaryOp("/", Id("b_55"), CallExpr(Id("b_75"), Id("b_72"), [BinaryOp("&&", ArrayCell(Id("b_71"), BinaryOp("-", Id("b_87"), Id("b_30"))), NullLiteral()), Id("b_94")])), SelfLiteral()), ArrayCell(Id("b_59"), BinaryOp("&&", Id("b_95"), StringLiteral('"string literal"'))))), Return(FloatLiteral(0.15)), None)]))], None)]))
        self.assertTrue(TestAST.test(input, expect, 333))

    def test_35(self):
        input = r"""class b_74 {
b_21(void[8] b_87, b_41; string b_76) {
{
boolean[5] b_32 = (b_3[(b_22 && b_90[(b_58[b_70] / b_1[{"string literal", 5}])])] * {4} + {0.84, "string literal", "string literal", true} * b_47), b_2;
}
}
}
"""
        expect = str(Program([ClassDecl(Id("b_74"), [MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_87"), ArrayType(8, VoidType()), None), VarDecl(Id("b_41"), ArrayType(8, VoidType()), None), VarDecl(Id("b_76"), StringType(), None)], None, Block([], [Block([VarDecl(Id("b_32"), ArrayType(5, BoolType()), BinaryOp("+", BinaryOp("*", ArrayCell(Id("b_3"), BinaryOp("&&", Id("b_22"), ArrayCell(Id("b_90"), BinaryOp("/", ArrayCell(Id("b_58"), Id("b_70")), ArrayCell(Id("b_1"), ArrayLiteral([StringLiteral('"string literal"'), IntLiteral(5)])))))), ArrayLiteral([IntLiteral(4)])), BinaryOp("*", ArrayLiteral([FloatLiteral(0.84), StringLiteral('"string literal"'), StringLiteral('"string literal"'), BooleanLiteral(True)]), Id("b_47")))), VarDecl(Id("b_2"), ArrayType(5, BoolType()), None)], [])]))], None)]))
        self.assertTrue(TestAST.test(input, expect, 334))

    def test_36(self):
        input = r"""class b_86 extends b_83 {
final float b_28, b_14;
}
"""
        expect = str(Program([ClassDecl(Id("b_86"), [AttributeDecl(Instance(), ConstDecl(Id("b_28"), FloatType(), None)), AttributeDecl(Instance(), ConstDecl(Id("b_14"), FloatType(), None))], Id("b_83"))]))
        self.assertTrue(TestAST.test(input, expect, 335))

    def test_37(self):
        input = r"""class b_27 {
boolean b_47(b_90[5] b_66, b_12; void[3] b_53) {
}
}
"""
        expect = str(Program([ClassDecl(Id("b_27"), [MethodDecl(Instance(), Id("b_47"), [VarDecl(Id("b_66"), ArrayType(5, ClassType(Id("b_90"))), None), VarDecl(Id("b_12"), ArrayType(5, ClassType(Id("b_90"))), None), VarDecl(Id("b_53"), ArrayType(3, VoidType()), None)], BoolType(), Block([], []))], None)]))
        self.assertTrue(TestAST.test(input, expect, 336))

    def test_38(self):
        input = r"""class b_36 {
b_79(float[8] b_16, b_93; string[8] b_6) {
{
string[9] b_25 = b_79 - b_20.b_33.b_45(b_18, b_21);
}
}
}
"""
        expect = str(Program([ClassDecl(Id("b_36"), [MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_16"), ArrayType(8, FloatType()), None), VarDecl(Id("b_93"), ArrayType(8, FloatType()), None), VarDecl(Id("b_6"), ArrayType(8, StringType()), None)], None, Block([], [Block([VarDecl(Id("b_25"), ArrayType(9, StringType()), BinaryOp("-", Id("b_79"), CallExpr(FieldAccess(Id("b_20"), Id("b_33")), Id("b_45"), [Id("b_18"), Id("b_21")])))], [])]))], None)]))
        self.assertTrue(TestAST.test(input, expect, 337))

    def test_39(self):
        input = r"""class b_82 extends b_94 {
b_99(float[4] b_36, b_83; int b_27) {
boolean[7] b_16, b_87;
for b_100 := b_18 downto ({"string literal", this, nil, "string literal"} && b_97[(b_84.b_18.b_1 + b_25[b_89[b_25 && b_39[(b_36 / b_69.b_31.b_50({0.22, 5, 0.96, "string literal"} && b_15, b_0.b_25.b_25))]]])]) do
b_36.b_34 := b_39 + b_43[({0.47, 0.47, nil, false} && {true, true})] || b_58;
}
}
"""
        expect = str(Program([ClassDecl(Id("b_82"), [MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_36"), ArrayType(4, FloatType()), None), VarDecl(Id("b_83"), ArrayType(4, FloatType()), None), VarDecl(Id("b_27"), IntType(), None)], None, Block([VarDecl(Id("b_16"), ArrayType(7, BoolType()), None), VarDecl(Id("b_87"), ArrayType(7, BoolType()), None)], [For(Id("b_100"), Id("b_18"), BinaryOp("&&", ArrayLiteral([StringLiteral('"string literal"'), SelfLiteral(), NullLiteral(), StringLiteral('"string literal"')]), ArrayCell(Id("b_97"), BinaryOp("+", FieldAccess(FieldAccess(Id("b_84"), Id("b_18")), Id("b_1")), ArrayCell(Id("b_25"), ArrayCell(Id("b_89"), BinaryOp("&&", Id("b_25"), ArrayCell(Id("b_39"), BinaryOp("/", Id("b_36"), CallExpr(FieldAccess(Id("b_69"), Id("b_31")), Id("b_50"), [BinaryOp("&&", ArrayLiteral([FloatLiteral(0.22), IntLiteral(5), FloatLiteral(0.96), StringLiteral('"string literal"')]), Id("b_15")), FieldAccess(FieldAccess(Id("b_0"), Id("b_25")), Id("b_25"))]))))))))), False, Assign(FieldAccess(Id("b_36"), Id("b_34")), BinaryOp("||", BinaryOp("+", Id("b_39"), ArrayCell(Id("b_43"), BinaryOp("&&", ArrayLiteral([FloatLiteral(0.47), FloatLiteral(0.47), NullLiteral(), BooleanLiteral(False)]), ArrayLiteral([BooleanLiteral(True), BooleanLiteral(True)])))), Id("b_58"))))]))], Id("b_94"))]))
        self.assertTrue(TestAST.test(input, expect, 338))

    def test_40(self):
        input = r"""class b_87 {
int b_28(void b_14, b_3; b_36 b_31) {
return "string literal" * {this, 14, 14};
}
}
"""
        expect = str(Program([ClassDecl(Id("b_87"), [MethodDecl(Instance(), Id("b_28"), [VarDecl(Id("b_14"), VoidType(), None), VarDecl(Id("b_3"), VoidType(), None), VarDecl(Id("b_31"), ClassType(Id("b_36")), None)], IntType(), Block([], [Return(BinaryOp("*", StringLiteral('"string literal"'), ArrayLiteral([SelfLiteral(), IntLiteral(14), IntLiteral(14)])))]))], None)]))
        self.assertTrue(TestAST.test(input, expect, 339))

    def test_41(self):
        input = r"""class b_32 extends b_20 {
final static void b_57;
}
"""
        expect = str(Program([ClassDecl(Id("b_32"), [AttributeDecl(Static(), ConstDecl(Id("b_57"), VoidType(), None))], Id("b_20"))]))
        self.assertTrue(TestAST.test(input, expect, 340))

    def test_42(self):
        input = r"""class b_67 {
static float b_8;
}
"""
        expect = str(Program([ClassDecl(Id("b_67"), [AttributeDecl(Static(), VarDecl(Id("b_8"), FloatType(), None))], None)]))
        self.assertTrue(TestAST.test(input, expect, 341))

    def test_43(self):
        input = r"""class b_74 {
static float[1] b_36;
}
"""
        expect = str(Program([ClassDecl(Id("b_74"), [AttributeDecl(Static(), VarDecl(Id("b_36"), ArrayType(1, FloatType()), None))], None)]))
        self.assertTrue(TestAST.test(input, expect, 342))

    def test_44(self):
        input = r"""class b_43 extends b_46 {
float b_53(void[9] b_70, b_8; float[4] b_97) {
}
}
"""
        expect = str(Program([ClassDecl(Id("b_43"), [MethodDecl(Instance(), Id("b_53"), [VarDecl(Id("b_70"), ArrayType(9, VoidType()), None), VarDecl(Id("b_8"), ArrayType(9, VoidType()), None), VarDecl(Id("b_97"), ArrayType(4, FloatType()), None)], FloatType(), Block([], []))], Id("b_46"))]))
        self.assertTrue(TestAST.test(input, expect, 343))

    def test_45(self):
        input = r"""class b_90 {
boolean[5] b_40 = (b_96 + b_38[2 / b_77.b_54]) / (0.82 / {nil, this, 10}), b_52 = (b_28 / b_55);
b_42(boolean[7] b_75, b_89; b_3[7] b_52) {
continue;
}
}
"""
        expect = str(Program([ClassDecl(Id("b_90"), [AttributeDecl(Instance(), VarDecl(Id("b_40"), ArrayType(5, BoolType()), BinaryOp("/", BinaryOp("+", Id("b_96"), ArrayCell(Id("b_38"), BinaryOp("/", IntLiteral(2), FieldAccess(Id("b_77"), Id("b_54"))))), BinaryOp("/", FloatLiteral(0.82), ArrayLiteral([NullLiteral(), SelfLiteral(), IntLiteral(10)]))))), AttributeDecl(Instance(), VarDecl(Id("b_52"), ArrayType(5, BoolType()), BinaryOp("/", Id("b_28"), Id("b_55")))), MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_75"), ArrayType(7, BoolType()), None), VarDecl(Id("b_89"), ArrayType(7, BoolType()), None), VarDecl(Id("b_52"), ArrayType(7, ClassType(Id("b_3"))), None)], None, Block([], [Continue()]))], None)]))
        self.assertTrue(TestAST.test(input, expect, 344))

    def test_46(self):
        input = r"""class b_80 {
void b_96(void[5] b_67, b_89; b_61 b_11) {
b_28.b_6(b_10.b_86((b_13 + b_49), b_39), b_72);
}
final string[2] b_79, b_56 = b_69;
}
"""
        expect = str(Program([ClassDecl(Id("b_80"), [MethodDecl(Instance(), Id("b_96"), [VarDecl(Id("b_67"), ArrayType(5, VoidType()), None), VarDecl(Id("b_89"), ArrayType(5, VoidType()), None), VarDecl(Id("b_11"), ClassType(Id("b_61")), None)], VoidType(), Block([], [CallStmt(Id("b_28"), Id("b_6"), [CallExpr(Id("b_10"), Id("b_86"), [BinaryOp("+", Id("b_13"), Id("b_49")), Id("b_39")]), Id("b_72")])])), AttributeDecl(Instance(), ConstDecl(Id("b_79"), ArrayType(2, StringType()), None)), AttributeDecl(Instance(), ConstDecl(Id("b_56"), ArrayType(2, StringType()), Id("b_69")))], None)]))
        self.assertTrue(TestAST.test(input, expect, 345))

    def test_47(self):
        input = r"""class b_22 {
int b_14(void[10] b_71, b_14; int[3] b_2) {
boolean[8] b_67, b_12 = ((b_93 && {this, this, false, 0.22, 2}) + b_49 && 8);
}
b_24 b_72(float b_11, b_40; int[5] b_47) {
}
}
"""
        expect = str(Program([ClassDecl(Id("b_22"), [MethodDecl(Instance(), Id("b_14"), [VarDecl(Id("b_71"), ArrayType(10, VoidType()), None), VarDecl(Id("b_14"), ArrayType(10, VoidType()), None), VarDecl(Id("b_2"), ArrayType(3, IntType()), None)], IntType(), Block([VarDecl(Id("b_67"), ArrayType(8, BoolType()), None), VarDecl(Id("b_12"), ArrayType(8, BoolType()), BinaryOp("&&", BinaryOp("+", BinaryOp("&&", Id("b_93"), ArrayLiteral([SelfLiteral(), SelfLiteral(), BooleanLiteral(False), FloatLiteral(0.22), IntLiteral(2)])), Id("b_49")), IntLiteral(8)))], [])), MethodDecl(Instance(), Id("b_72"), [VarDecl(Id("b_11"), FloatType(), None), VarDecl(Id("b_40"), FloatType(), None), VarDecl(Id("b_47"), ArrayType(5, IntType()), None)], ClassType(Id("b_24")), Block([], []))], None)]))
        self.assertTrue(TestAST.test(input, expect, 346))

    def test_48(self):
        input = r"""class b_40 {
final static string[3] b_8;
b_83(b_41[7] b_28, b_75; b_91[7] b_97) {
if b_12 + b_57 + b_47 >= b_78.b_10.b_19 + b_22 then
return b_71[b_60];
else
continue;
}
}
"""
        expect = str(Program([ClassDecl(Id("b_40"), [AttributeDecl(Static(), ConstDecl(Id("b_8"), ArrayType(3, StringType()), None)), MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_28"), ArrayType(7, ClassType(Id("b_41"))), None), VarDecl(Id("b_75"), ArrayType(7, ClassType(Id("b_41"))), None), VarDecl(Id("b_97"), ArrayType(7, ClassType(Id("b_91"))), None)], None, Block([], [If(BinaryOp(">=", BinaryOp("+", BinaryOp("+", Id("b_12"), Id("b_57")), Id("b_47")), BinaryOp("+", FieldAccess(FieldAccess(Id("b_78"), Id("b_10")), Id("b_19")), Id("b_22"))), Return(ArrayCell(Id("b_71"), Id("b_60"))), Continue())]))], None)]))
        self.assertTrue(TestAST.test(input, expect, 347))

    def test_49(self):
        input = r"""class b_78 extends b_51 {
b_91(boolean[3] b_29, b_16; string[5] b_71) {
void b_42;
break;
}
b_9(float b_31, b_67; string b_5) {
b_0.b_29({this, false, 0.08, 0.33, 0.55}, b_25);
}
}
"""
        expect = str(Program([ClassDecl(Id("b_78"), [MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_29"), ArrayType(3, BoolType()), None), VarDecl(Id("b_16"), ArrayType(3, BoolType()), None), VarDecl(Id("b_71"), ArrayType(5, StringType()), None)], None, Block([VarDecl(Id("b_42"), VoidType(), None)], [Break()])), MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_31"), FloatType(), None), VarDecl(Id("b_67"), FloatType(), None), VarDecl(Id("b_5"), StringType(), None)], None, Block([], [CallStmt(Id("b_0"), Id("b_29"), [ArrayLiteral([SelfLiteral(), BooleanLiteral(False), FloatLiteral(0.08), FloatLiteral(0.33), FloatLiteral(0.55)]), Id("b_25")])]))], Id("b_51"))]))
        self.assertTrue(TestAST.test(input, expect, 348))

    def test_50(self):
        input = r"""class b_0 {
b_70(int[4] b_98, b_3; void[8] b_60) {
b_22 b_99 = ((b_90 * b_27[(b_97 + b_83.b_10((b_58 || false), {nil, 0.95, 0, "string literal", "string literal"}))]) * b_79), b_57 = {0.97, true, false, nil};
}
b_69 b_25(string[2] b_64, b_75; int[10] b_47) {
string[1] b_64;
}
}
"""
        expect = str(Program([ClassDecl(Id("b_0"), [MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_98"), ArrayType(4, IntType()), None), VarDecl(Id("b_3"), ArrayType(4, IntType()), None), VarDecl(Id("b_60"), ArrayType(8, VoidType()), None)], None, Block([VarDecl(Id("b_99"), ClassType(Id("b_22")), BinaryOp("*", BinaryOp("*", Id("b_90"), ArrayCell(Id("b_27"), BinaryOp("+", Id("b_97"), CallExpr(Id("b_83"), Id("b_10"), [BinaryOp("||", Id("b_58"), BooleanLiteral(False)), ArrayLiteral([NullLiteral(), FloatLiteral(0.95), IntLiteral(0), StringLiteral('"string literal"'), StringLiteral('"string literal"')])])))), Id("b_79"))), VarDecl(Id("b_57"), ClassType(Id("b_22")), ArrayLiteral([FloatLiteral(0.97), BooleanLiteral(True), BooleanLiteral(False), NullLiteral()]))], [])), MethodDecl(Instance(), Id("b_25"), [VarDecl(Id("b_64"), ArrayType(2, StringType()), None), VarDecl(Id("b_75"), ArrayType(2, StringType()), None), VarDecl(Id("b_47"), ArrayType(10, IntType()), None)], ClassType(Id("b_69")), Block([VarDecl(Id("b_64"), ArrayType(1, StringType()), None)], []))], None)]))
        self.assertTrue(TestAST.test(input, expect, 349))

    def test_51(self):
        input = r"""class b_37 extends b_13 {
b_85(boolean[4] b_10, b_85; boolean b_92) {
continue;
}
int b_96 = b_17.b_29.b_45(({this, true, "string literal"} ^ b_63[b_30[(b_20 || b_31)]]), b_61), b_100;
}
"""
        expect = str(Program([ClassDecl(Id("b_37"), [MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_10"), ArrayType(4, BoolType()), None), VarDecl(Id("b_85"), ArrayType(4, BoolType()), None), VarDecl(Id("b_92"), BoolType(), None)], None, Block([], [Continue()])), AttributeDecl(Instance(), VarDecl(Id("b_96"), IntType(), CallExpr(FieldAccess(Id("b_17"), Id("b_29")), Id("b_45"), [BinaryOp("^", ArrayLiteral([SelfLiteral(), BooleanLiteral(True), StringLiteral('"string literal"')]), ArrayCell(Id("b_63"), ArrayCell(Id("b_30"), BinaryOp("||", Id("b_20"), Id("b_31"))))), Id("b_61")]))), AttributeDecl(Instance(), VarDecl(Id("b_100"), IntType(), None))], Id("b_13"))]))
        self.assertTrue(TestAST.test(input, expect, 350))

    def test_52(self):
        input = r"""class b_16 extends b_54 {
b_70(string b_80, b_86; b_95[4] b_17) {
int[6] b_41 = b_99 * "string literal", b_49;
}
final boolean b_25 = b_97.b_48.b_37(b_1, 2), b_40;
}
"""
        expect = str(Program([ClassDecl(Id("b_16"), [MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_80"), StringType(), None), VarDecl(Id("b_86"), StringType(), None), VarDecl(Id("b_17"), ArrayType(4, ClassType(Id("b_95"))), None)], None, Block([VarDecl(Id("b_41"), ArrayType(6, IntType()), BinaryOp("*", Id("b_99"), StringLiteral('"string literal"'))), VarDecl(Id("b_49"), ArrayType(6, IntType()), None)], [])), AttributeDecl(Instance(), ConstDecl(Id("b_25"), BoolType(), CallExpr(FieldAccess(Id("b_97"), Id("b_48")), Id("b_37"), [Id("b_1"), IntLiteral(2)]))), AttributeDecl(Instance(), ConstDecl(Id("b_40"), BoolType(), None))], Id("b_54"))]))
        self.assertTrue(TestAST.test(input, expect, 351))

    def test_53(self):
        input = r"""class b_0 {
string b_52(void b_60, b_86; boolean b_21) {
if b_30[{"string literal"} || b_36] != (b_20 * "string literal") then
b_65.b_97(b_27, 11);
}
float b_28(void[3] b_92, b_87; boolean b_71) {
void[6] b_70 = b_16[b_86[b_58.b_9.b_85(b_93 / b_76, b_90)]];
b_96.b_46(false, b_58.b_27(19 * b_29[(b_37 / b_62)], {true}));
}
}
"""
        expect = str(Program([ClassDecl(Id("b_0"), [MethodDecl(Instance(), Id("b_52"), [VarDecl(Id("b_60"), VoidType(), None), VarDecl(Id("b_86"), VoidType(), None), VarDecl(Id("b_21"), BoolType(), None)], StringType(), Block([], [If(BinaryOp("!=", ArrayCell(Id("b_30"), BinaryOp("||", ArrayLiteral([StringLiteral('"string literal"')]), Id("b_36"))), BinaryOp("*", Id("b_20"), StringLiteral('"string literal"'))), CallStmt(Id("b_65"), Id("b_97"), [Id("b_27"), IntLiteral(11)]), None)])), MethodDecl(Instance(), Id("b_28"), [VarDecl(Id("b_92"), ArrayType(3, VoidType()), None), VarDecl(Id("b_87"), ArrayType(3, VoidType()), None), VarDecl(Id("b_71"), BoolType(), None)], FloatType(), Block([VarDecl(Id("b_70"), ArrayType(6, VoidType()), ArrayCell(Id("b_16"), ArrayCell(Id("b_86"), CallExpr(FieldAccess(Id("b_58"), Id("b_9")), Id("b_85"), [BinaryOp("/", Id("b_93"), Id("b_76")), Id("b_90")]))))], [CallStmt(Id("b_96"), Id("b_46"), [BooleanLiteral(False), CallExpr(Id("b_58"), Id("b_27"), [BinaryOp("*", IntLiteral(19), ArrayCell(Id("b_29"), BinaryOp("/", Id("b_37"), Id("b_62")))), ArrayLiteral([BooleanLiteral(True)])])])]))], None)]))
        self.assertTrue(TestAST.test(input, expect, 352))

    def test_54(self):
        input = r"""class b_52 extends b_0 {
b_62(string b_20, b_15; int[8] b_57) {
}
int[2] b_30 = 0.98, b_2 = b_28;
}
"""
        expect = str(Program([ClassDecl(Id("b_52"), [MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_20"), StringType(), None), VarDecl(Id("b_15"), StringType(), None), VarDecl(Id("b_57"), ArrayType(8, IntType()), None)], None, Block([], [])), AttributeDecl(Instance(), VarDecl(Id("b_30"), ArrayType(2, IntType()), FloatLiteral(0.98))), AttributeDecl(Instance(), VarDecl(Id("b_2"), ArrayType(2, IntType()), Id("b_28")))], Id("b_0"))]))
        self.assertTrue(TestAST.test(input, expect, 353))

    def test_55(self):
        input = r"""class b_91 extends b_91 {
b_14(b_44 b_78, b_35; boolean[9] b_37) {
b_21[3] b_92;
for b_24 := b_77[(b_0 + b_12)] downto b_80[b_48 / b_34] do
b_89.b_18((b_83 - b_87.b_78.b_8), b_0);
}
b_87(string b_66, b_3; float b_71) {
b_15[5] := this + b_87;
}
}
"""
        expect = str(Program([ClassDecl(Id("b_91"), [MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_78"), ClassType(Id("b_44")), None), VarDecl(Id("b_35"), ClassType(Id("b_44")), None), VarDecl(Id("b_37"), ArrayType(9, BoolType()), None)], None, Block([VarDecl(Id("b_92"), ArrayType(3, ClassType(Id("b_21"))), None)], [For(Id("b_24"), ArrayCell(Id("b_77"), BinaryOp("+", Id("b_0"), Id("b_12"))), ArrayCell(Id("b_80"), BinaryOp("/", Id("b_48"), Id("b_34"))), False, CallStmt(Id("b_89"), Id("b_18"), [BinaryOp("-", Id("b_83"), FieldAccess(FieldAccess(Id("b_87"), Id("b_78")), Id("b_8"))), Id("b_0")]))])), MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_66"), StringType(), None), VarDecl(Id("b_3"), StringType(), None), VarDecl(Id("b_71"), FloatType(), None)], None, Block([], [Assign(ArrayCell(Id("b_15"), IntLiteral(5)), BinaryOp("+", SelfLiteral(), Id("b_87")))]))], Id("b_91"))]))
        self.assertTrue(TestAST.test(input, expect, 354))

    def test_56(self):
        input = r"""class b_82 extends b_81 {
b_21(float b_10, b_17; boolean[10] b_30) {
}
b_98 b_72(b_44 b_97, b_79; string b_7) {
}
}
"""
        expect = str(Program([ClassDecl(Id("b_82"), [MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_10"), FloatType(), None), VarDecl(Id("b_17"), FloatType(), None), VarDecl(Id("b_30"), ArrayType(10, BoolType()), None)], None, Block([], [])), MethodDecl(Instance(), Id("b_72"), [VarDecl(Id("b_97"), ClassType(Id("b_44")), None), VarDecl(Id("b_79"), ClassType(Id("b_44")), None), VarDecl(Id("b_7"), StringType(), None)], ClassType(Id("b_98")), Block([], []))], Id("b_81"))]))
        self.assertTrue(TestAST.test(input, expect, 355))

    def test_57(self):
        input = r"""class b_9 extends b_33 {
b_21(string b_97, b_76; int[8] b_89) {
{
if 2 == b_99 - (b_96.b_14.b_81 || 0.17) then
b_29.b_32(b_41.b_87(b_39 || b_49.b_7, b_46[("string literal" * b_17)]), b_16);
else
b_37.b_5(0.57, b_60);
}
}
b_94(void[3] b_88, b_59; boolean[8] b_24) {
continue;
}
}
"""
        expect = str(Program([ClassDecl(Id("b_9"), [MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_97"), StringType(), None), VarDecl(Id("b_76"), StringType(), None), VarDecl(Id("b_89"), ArrayType(8, IntType()), None)], None, Block([], [Block([], [If(BinaryOp("==", IntLiteral(2), BinaryOp("-", Id("b_99"), BinaryOp("||", FieldAccess(FieldAccess(Id("b_96"), Id("b_14")), Id("b_81")), FloatLiteral(0.17)))), CallStmt(Id("b_29"), Id("b_32"), [CallExpr(Id("b_41"), Id("b_87"), [BinaryOp("||", Id("b_39"), FieldAccess(Id("b_49"), Id("b_7"))), ArrayCell(Id("b_46"), BinaryOp("*", StringLiteral('"string literal"'), Id("b_17")))]), Id("b_16")]), CallStmt(Id("b_37"), Id("b_5"), [FloatLiteral(0.57), Id("b_60")]))])])), MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_88"), ArrayType(3, VoidType()), None), VarDecl(Id("b_59"), ArrayType(3, VoidType()), None), VarDecl(Id("b_24"), ArrayType(8, BoolType()), None)], None, Block([], [Continue()]))], Id("b_33"))]))
        self.assertTrue(TestAST.test(input, expect, 356))

    def test_58(self):
        input = r"""class b_31 extends b_83 {
b_57(void b_72, b_20; boolean[7] b_5) {
if b_26 >= (b_71 || b_48.b_2.b_0((true ^ nil), b_26.b_79.b_92)) then
break;
}
b_33(int b_64, b_83; float b_68) {
{
float[6] b_80 = b_52 - {this, this, this, false};
{
continue;
}
}
}
}
"""
        expect = str(Program([ClassDecl(Id("b_31"), [MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_72"), VoidType(), None), VarDecl(Id("b_20"), VoidType(), None), VarDecl(Id("b_5"), ArrayType(7, BoolType()), None)], None, Block([], [If(BinaryOp(">=", Id("b_26"), BinaryOp("||", Id("b_71"), CallExpr(FieldAccess(Id("b_48"), Id("b_2")), Id("b_0"), [BinaryOp("^", BooleanLiteral(True), NullLiteral()), FieldAccess(FieldAccess(Id("b_26"), Id("b_79")), Id("b_92"))]))), Break(), None)])), MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_64"), IntType(), None), VarDecl(Id("b_83"), IntType(), None), VarDecl(Id("b_68"), FloatType(), None)], None, Block([], [Block([VarDecl(Id("b_80"), ArrayType(6, FloatType()), BinaryOp("-", Id("b_52"), ArrayLiteral([SelfLiteral(), SelfLiteral(), SelfLiteral(), BooleanLiteral(False)])))], [Block([], [Continue()])])]))], Id("b_83"))]))
        self.assertTrue(TestAST.test(input, expect, 357))

    def test_59(self):
        input = r"""class b_64 {
string b_15(string b_58, b_85; b_6[1] b_38) {
b_73[4] := ((b_66 || b_69[b_100.b_64.b_9]) || (b_35 || b_32));
}
b_53(b_28[6] b_20, b_40; void b_2) {
void b_50;
if b_83 / b_2 < b_83 then
b_6.b_8(b_98, b_34[b_41]);
else
return {this};
}
}
"""
        expect = str(Program([ClassDecl(Id("b_64"), [MethodDecl(Instance(), Id("b_15"), [VarDecl(Id("b_58"), StringType(), None), VarDecl(Id("b_85"), StringType(), None), VarDecl(Id("b_38"), ArrayType(1, ClassType(Id("b_6"))), None)], StringType(), Block([], [Assign(ArrayCell(Id("b_73"), IntLiteral(4)), BinaryOp("||", BinaryOp("||", Id("b_66"), ArrayCell(Id("b_69"), FieldAccess(FieldAccess(Id("b_100"), Id("b_64")), Id("b_9")))), BinaryOp("||", Id("b_35"), Id("b_32"))))])), MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_20"), ArrayType(6, ClassType(Id("b_28"))), None), VarDecl(Id("b_40"), ArrayType(6, ClassType(Id("b_28"))), None), VarDecl(Id("b_2"), VoidType(), None)], None, Block([VarDecl(Id("b_50"), VoidType(), None)], [If(BinaryOp("<", BinaryOp("/", Id("b_83"), Id("b_2")), Id("b_83")), CallStmt(Id("b_6"), Id("b_8"), [Id("b_98"), ArrayCell(Id("b_34"), Id("b_41"))]), Return(ArrayLiteral([SelfLiteral()])))]))], None)]))
        self.assertTrue(TestAST.test(input, expect, 358))

    def test_60(self):
        input = r"""class b_72 {
b_21 b_57(float[9] b_51, b_27; float[8] b_18) {
void[2] b_79, b_25;
}
b_94(void[9] b_100, b_41; void b_67) {
int b_34 = ((b_66 / b_5) / this), b_17 = nil - b_48 - b_5 * b_71;
return b_73.b_76((b_31 ^ b_75), b_47.b_78.b_0(b_80.b_86(0.67, {this}) && b_54, b_100[nil]));
}
}
"""
        expect = str(Program([ClassDecl(Id("b_72"), [MethodDecl(Instance(), Id("b_57"), [VarDecl(Id("b_51"), ArrayType(9, FloatType()), None), VarDecl(Id("b_27"), ArrayType(9, FloatType()), None), VarDecl(Id("b_18"), ArrayType(8, FloatType()), None)], ClassType(Id("b_21")), Block([VarDecl(Id("b_79"), ArrayType(2, VoidType()), None), VarDecl(Id("b_25"), ArrayType(2, VoidType()), None)], [])), MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_100"), ArrayType(9, VoidType()), None), VarDecl(Id("b_41"), ArrayType(9, VoidType()), None), VarDecl(Id("b_67"), VoidType(), None)], None, Block([VarDecl(Id("b_34"), IntType(), BinaryOp("/", BinaryOp("/", Id("b_66"), Id("b_5")), SelfLiteral())), VarDecl(Id("b_17"), IntType(), BinaryOp("-", BinaryOp("-", NullLiteral(), Id("b_48")), BinaryOp("*", Id("b_5"), Id("b_71"))))], [Return(CallExpr(Id("b_73"), Id("b_76"), [BinaryOp("^", Id("b_31"), Id("b_75")), CallExpr(FieldAccess(Id("b_47"), Id("b_78")), Id("b_0"), [BinaryOp("&&", CallExpr(Id("b_80"), Id("b_86"), [FloatLiteral(0.67), ArrayLiteral([SelfLiteral()])]), Id("b_54")), ArrayCell(Id("b_100"), NullLiteral())])]))]))], None)]))
        self.assertTrue(TestAST.test(input, expect, 359))

    def test_61(self):
        input = r"""class b_61 extends b_87 {
b_73(void[9] b_40, b_10; b_64 b_39) {
float b_85 = b_96, b_40;
if {this, nil, nil} >= b_76[{this, true, false} && b_81.b_70.b_6] / b_69.b_27((b_11 - 5), b_1) / b_68[(b_96 || b_66.b_62((b_64[b_37[b_5[b_100 + b_49] - b_90]] - b_41), "string literal"))] * b_18 then
for b_18 := {0.46, nil, this, nil} downto b_8[b_53.b_55.b_82 ^ b_39] do
b_11.b_49 := b_88;
else
for b_19 := b_74 || b_4.b_100 to b_41[(b_96[("string literal" || b_17[b_22 && "string literal"])] + b_69)] - (b_54 - b_96[(b_20.b_68.b_31 || b_36)]) do
b_5.b_55({12}, b_29);
}
void b_27(string b_30, b_64; float[1] b_41) {
}
}
"""
        expect = str(Program([ClassDecl(Id("b_61"), [MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_40"), ArrayType(9, VoidType()), None), VarDecl(Id("b_10"), ArrayType(9, VoidType()), None), VarDecl(Id("b_39"), ClassType(Id("b_64")), None)], None, Block([VarDecl(Id("b_85"), FloatType(), Id("b_96")), VarDecl(Id("b_40"), FloatType(), None)], [If(BinaryOp(">=", ArrayLiteral([SelfLiteral(), NullLiteral(), NullLiteral()]), BinaryOp("*", BinaryOp("/", BinaryOp("/", ArrayCell(Id("b_76"), BinaryOp("&&", ArrayLiteral([SelfLiteral(), BooleanLiteral(True), BooleanLiteral(False)]), FieldAccess(FieldAccess(Id("b_81"), Id("b_70")), Id("b_6")))), CallExpr(Id("b_69"), Id("b_27"), [BinaryOp("-", Id("b_11"), IntLiteral(5)), Id("b_1")])), ArrayCell(Id("b_68"), BinaryOp("||", Id("b_96"), CallExpr(Id("b_66"), Id("b_62"), [BinaryOp("-", ArrayCell(Id("b_64"), ArrayCell(Id("b_37"), BinaryOp("-", ArrayCell(Id("b_5"), BinaryOp("+", Id("b_100"), Id("b_49"))), Id("b_90")))), Id("b_41")), StringLiteral('"string literal"')])))), Id("b_18"))), For(Id("b_18"), ArrayLiteral([FloatLiteral(0.46), NullLiteral(), SelfLiteral(), NullLiteral()]), ArrayCell(Id("b_8"), BinaryOp("^", FieldAccess(FieldAccess(Id("b_53"), Id("b_55")), Id("b_82")), Id("b_39"))), False, Assign(FieldAccess(Id("b_11"), Id("b_49")), Id("b_88"))), For(Id("b_19"), BinaryOp("||", Id("b_74"), FieldAccess(Id("b_4"), Id("b_100"))), BinaryOp("-", ArrayCell(Id("b_41"), BinaryOp("+", ArrayCell(Id("b_96"), BinaryOp("||", StringLiteral('"string literal"'), ArrayCell(Id("b_17"), BinaryOp("&&", Id("b_22"), StringLiteral('"string literal"'))))), Id("b_69"))), BinaryOp("-", Id("b_54"), ArrayCell(Id("b_96"), BinaryOp("||", FieldAccess(FieldAccess(Id("b_20"), Id("b_68")), Id("b_31")), Id("b_36"))))), True, CallStmt(Id("b_5"), Id("b_55"), [ArrayLiteral([IntLiteral(12)]), Id("b_29")])))])), MethodDecl(Instance(), Id("b_27"), [VarDecl(Id("b_30"), StringType(), None), VarDecl(Id("b_64"), StringType(), None), VarDecl(Id("b_41"), ArrayType(1, FloatType()), None)], VoidType(), Block([], []))], Id("b_87"))]))
        self.assertTrue(TestAST.test(input, expect, 360))

    def test_62(self):
        input = r"""class b_61 {
b_18(int[2] b_55, b_77; boolean[1] b_65) {
}
b_30(float b_46, b_38; float b_18) {
boolean b_3, b_95 = {5};
b_82.b_61 := b_56;
}
}
"""
        expect = str(Program([ClassDecl(Id("b_61"), [MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_55"), ArrayType(2, IntType()), None), VarDecl(Id("b_77"), ArrayType(2, IntType()), None), VarDecl(Id("b_65"), ArrayType(1, BoolType()), None)], None, Block([], [])), MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_46"), FloatType(), None), VarDecl(Id("b_38"), FloatType(), None), VarDecl(Id("b_18"), FloatType(), None)], None, Block([VarDecl(Id("b_3"), BoolType(), None), VarDecl(Id("b_95"), BoolType(), ArrayLiteral([IntLiteral(5)]))], [Assign(FieldAccess(Id("b_82"), Id("b_61")), Id("b_56"))]))], None)]))
        self.assertTrue(TestAST.test(input, expect, 361))

    def test_63(self):
        input = r"""class b_52 {
b_15(float b_44, b_19; string[5] b_70) {
{
}
}
b_4(float[7] b_59, b_3; float b_76) {
b_60[1] b_33 = {nil, true, nil}, b_98 = (b_23 || b_88 + (this * 0.69));
}
}
"""
        expect = str(Program([ClassDecl(Id("b_52"), [MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_44"), FloatType(), None), VarDecl(Id("b_19"), FloatType(), None), VarDecl(Id("b_70"), ArrayType(5, StringType()), None)], None, Block([], [Block([], [])])), MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_59"), ArrayType(7, FloatType()), None), VarDecl(Id("b_3"), ArrayType(7, FloatType()), None), VarDecl(Id("b_76"), FloatType(), None)], None, Block([VarDecl(Id("b_33"), ArrayType(1, ClassType(Id("b_60"))), ArrayLiteral([NullLiteral(), BooleanLiteral(True), NullLiteral()])), VarDecl(Id("b_98"), ArrayType(1, ClassType(Id("b_60"))), BinaryOp("||", Id("b_23"), BinaryOp("+", Id("b_88"), BinaryOp("*", SelfLiteral(), FloatLiteral(0.69)))))], []))], None)]))
        self.assertTrue(TestAST.test(input, expect, 362))

    def test_64(self):
        input = r"""class b_89 extends b_67 {
b_26(float[2] b_94, b_36; boolean[7] b_34) {
b_5.b_80((b_39[({false, this} ^ false)] || {4}), b_45);
}
static void[5] b_46 = b_34 + b_21[b_85 / {17, nil, false, 2, this}] / b_71 && b_91[(0.86 + b_78[b_47 / 0.07])], b_89;
}
"""
        expect = str(Program([ClassDecl(Id("b_89"), [MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_94"), ArrayType(2, FloatType()), None), VarDecl(Id("b_36"), ArrayType(2, FloatType()), None), VarDecl(Id("b_34"), ArrayType(7, BoolType()), None)], None, Block([], [CallStmt(Id("b_5"), Id("b_80"), [BinaryOp("||", ArrayCell(Id("b_39"), BinaryOp("^", ArrayLiteral([BooleanLiteral(False), SelfLiteral()]), BooleanLiteral(False))), ArrayLiteral([IntLiteral(4)])), Id("b_45")])])), AttributeDecl(Static(), VarDecl(Id("b_46"), ArrayType(5, VoidType()), BinaryOp("&&", BinaryOp("+", Id("b_34"), BinaryOp("/", ArrayCell(Id("b_21"), BinaryOp("/", Id("b_85"), ArrayLiteral([IntLiteral(17), NullLiteral(), BooleanLiteral(False), IntLiteral(2), SelfLiteral()]))), Id("b_71"))), ArrayCell(Id("b_91"), BinaryOp("+", FloatLiteral(0.86), ArrayCell(Id("b_78"), BinaryOp("/", Id("b_47"), FloatLiteral(0.07)))))))), AttributeDecl(Static(), VarDecl(Id("b_89"), ArrayType(5, VoidType()), None))], Id("b_67"))]))
        self.assertTrue(TestAST.test(input, expect, 363))

    def test_65(self):
        input = r"""class b_60 extends b_23 {
final static boolean[4] b_15 = b_68[b_93 - b_83.b_79.b_66(({true} && b_51), b_66[{true, 18} - b_73])];
b_97(string[7] b_88, b_9; void[3] b_28) {
float b_91 = "string literal", b_79 = b_68;
}
}
"""
        expect = str(Program([ClassDecl(Id("b_60"), [AttributeDecl(Static(), ConstDecl(Id("b_15"), ArrayType(4, BoolType()), ArrayCell(Id("b_68"), BinaryOp("-", Id("b_93"), CallExpr(FieldAccess(Id("b_83"), Id("b_79")), Id("b_66"), [BinaryOp("&&", ArrayLiteral([BooleanLiteral(True)]), Id("b_51")), ArrayCell(Id("b_66"), BinaryOp("-", ArrayLiteral([BooleanLiteral(True), IntLiteral(18)]), Id("b_73")))]))))), MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_88"), ArrayType(7, StringType()), None), VarDecl(Id("b_9"), ArrayType(7, StringType()), None), VarDecl(Id("b_28"), ArrayType(3, VoidType()), None)], None, Block([VarDecl(Id("b_91"), FloatType(), StringLiteral('"string literal"')), VarDecl(Id("b_79"), FloatType(), Id("b_68"))], []))], Id("b_23"))]))
        self.assertTrue(TestAST.test(input, expect, 364))

    def test_66(self):
        input = r"""class b_59 {
static float[5] b_0 = (b_18.b_59({true, this} || {0.33, "string literal", false}, {"string literal", 0.15, true, true}) - b_68 ^ this), b_90;
final int[6] b_72;
}
"""
        expect = str(Program([ClassDecl(Id("b_59"), [AttributeDecl(Static(), VarDecl(Id("b_0"), ArrayType(5, FloatType()), BinaryOp("-", CallExpr(Id("b_18"), Id("b_59"), [BinaryOp("||", ArrayLiteral([BooleanLiteral(True), SelfLiteral()]), ArrayLiteral([FloatLiteral(0.33), StringLiteral('"string literal"'), BooleanLiteral(False)])), ArrayLiteral([StringLiteral('"string literal"'), FloatLiteral(0.15), BooleanLiteral(True), BooleanLiteral(True)])]), BinaryOp("^", Id("b_68"), SelfLiteral())))), AttributeDecl(Static(), VarDecl(Id("b_90"), ArrayType(5, FloatType()), None)), AttributeDecl(Instance(), ConstDecl(Id("b_72"), ArrayType(6, IntType()), None))], None)]))
        self.assertTrue(TestAST.test(input, expect, 365))

    def test_67(self):
        input = r"""class b_97 extends b_80 {
b_88(string[9] b_64, b_65; b_31[8] b_99) {
boolean b_78, b_89;
b_74.b_96((b_86 / b_94), b_92);
}
string b_71(float b_41, b_84; float[4] b_62) {
}
}
"""
        expect = str(Program([ClassDecl(Id("b_97"), [MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_64"), ArrayType(9, StringType()), None), VarDecl(Id("b_65"), ArrayType(9, StringType()), None), VarDecl(Id("b_99"), ArrayType(8, ClassType(Id("b_31"))), None)], None, Block([VarDecl(Id("b_78"), BoolType(), None), VarDecl(Id("b_89"), BoolType(), None)], [CallStmt(Id("b_74"), Id("b_96"), [BinaryOp("/", Id("b_86"), Id("b_94")), Id("b_92")])])), MethodDecl(Instance(), Id("b_71"), [VarDecl(Id("b_41"), FloatType(), None), VarDecl(Id("b_84"), FloatType(), None), VarDecl(Id("b_62"), ArrayType(4, FloatType()), None)], StringType(), Block([], []))], Id("b_80"))]))
        self.assertTrue(TestAST.test(input, expect, 366))

    def test_68(self):
        input = r"""class b_77 extends b_40 {
boolean[6] b_42, b_19;
b_22(boolean b_52, b_14; float[6] b_34) {
string b_6;
b_11.b_92(b_28, b_12);
}
}
"""
        expect = str(Program([ClassDecl(Id("b_77"), [AttributeDecl(Instance(), VarDecl(Id("b_42"), ArrayType(6, BoolType()), None)), AttributeDecl(Instance(), VarDecl(Id("b_19"), ArrayType(6, BoolType()), None)), MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_52"), BoolType(), None), VarDecl(Id("b_14"), BoolType(), None), VarDecl(Id("b_34"), ArrayType(6, FloatType()), None)], None, Block([VarDecl(Id("b_6"), StringType(), None)], [CallStmt(Id("b_11"), Id("b_92"), [Id("b_28"), Id("b_12")])]))], Id("b_40"))]))
        self.assertTrue(TestAST.test(input, expect, 367))

    def test_69(self):
        input = r"""class b_13 extends b_44 {
b_4(void b_63, b_9; boolean[7] b_26) {
b_16[0] := {13, 17, nil};
}
static string b_22, b_88;
}
"""
        expect = str(Program([ClassDecl(Id("b_13"), [MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_63"), VoidType(), None), VarDecl(Id("b_9"), VoidType(), None), VarDecl(Id("b_26"), ArrayType(7, BoolType()), None)], None, Block([], [Assign(ArrayCell(Id("b_16"), IntLiteral(0)), ArrayLiteral([IntLiteral(13), IntLiteral(17), NullLiteral()]))])), AttributeDecl(Static(), VarDecl(Id("b_22"), StringType(), None)), AttributeDecl(Static(), VarDecl(Id("b_88"), StringType(), None))], Id("b_44"))]))
        self.assertTrue(TestAST.test(input, expect, 368))

    def test_70(self):
        input = r"""class b_45 extends b_65 {
b_18(string[9] b_64, b_91; boolean b_53) {
if b_72 ^ b_64 == (b_74 - b_74.b_37.b_50((b_20 || b_98), {false, 0.73}) * b_26.b_42) then
{
}
}
final static b_79 b_41, b_56;
}
"""
        expect = str(Program([ClassDecl(Id("b_45"), [MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_64"), ArrayType(9, StringType()), None), VarDecl(Id("b_91"), ArrayType(9, StringType()), None), VarDecl(Id("b_53"), BoolType(), None)], None, Block([], [If(BinaryOp("==", BinaryOp("^", Id("b_72"), Id("b_64")), BinaryOp("-", Id("b_74"), BinaryOp("*", CallExpr(FieldAccess(Id("b_74"), Id("b_37")), Id("b_50"), [BinaryOp("||", Id("b_20"), Id("b_98")), ArrayLiteral([BooleanLiteral(False), FloatLiteral(0.73)])]), FieldAccess(Id("b_26"), Id("b_42"))))), Block([], []), None)])), AttributeDecl(Static(), ConstDecl(Id("b_41"), ClassType(Id("b_79")), None)), AttributeDecl(Static(), ConstDecl(Id("b_56"), ClassType(Id("b_79")), None))], Id("b_65"))]))
        self.assertTrue(TestAST.test(input, expect, 369))

    def test_71(self):
        input = r"""class b_0 {
b_37 b_65(string b_60, b_54; void b_21) {
}
boolean b_62(float b_31, b_83; b_13[7] b_38) {
b_65.b_82(b_39, b_3.b_43.b_11(b_58 && b_44, b_30));
}
}
"""
        expect = str(Program([ClassDecl(Id("b_0"), [MethodDecl(Instance(), Id("b_65"), [VarDecl(Id("b_60"), StringType(), None), VarDecl(Id("b_54"), StringType(), None), VarDecl(Id("b_21"), VoidType(), None)], ClassType(Id("b_37")), Block([], [])), MethodDecl(Instance(), Id("b_62"), [VarDecl(Id("b_31"), FloatType(), None), VarDecl(Id("b_83"), FloatType(), None), VarDecl(Id("b_38"), ArrayType(7, ClassType(Id("b_13"))), None)], BoolType(), Block([], [CallStmt(Id("b_65"), Id("b_82"), [Id("b_39"), CallExpr(FieldAccess(Id("b_3"), Id("b_43")), Id("b_11"), [BinaryOp("&&", Id("b_58"), Id("b_44")), Id("b_30")])])]))], None)]))
        self.assertTrue(TestAST.test(input, expect, 370))

    def test_72(self):
        input = r"""class b_47 {
float b_94(float[5] b_8, b_52; void[6] b_19) {
float[9] b_77 = b_95.b_27({this}, b_86) - b_82 - b_38.b_34(b_30[b_58[b_17 * b_76] || b_79], b_76);
b_23.b_23(false, b_100);
}
b_16(int b_60, b_94; int b_35) {
float[1] b_8, b_86 = b_54 || b_39 && (b_81 ^ b_100[{nil, nil, 0.07} / b_11]);
}
}
"""
        expect = str(Program([ClassDecl(Id("b_47"), [MethodDecl(Instance(), Id("b_94"), [VarDecl(Id("b_8"), ArrayType(5, FloatType()), None), VarDecl(Id("b_52"), ArrayType(5, FloatType()), None), VarDecl(Id("b_19"), ArrayType(6, VoidType()), None)], FloatType(), Block([VarDecl(Id("b_77"), ArrayType(9, FloatType()), BinaryOp("-", BinaryOp("-", CallExpr(Id("b_95"), Id("b_27"), [ArrayLiteral([SelfLiteral()]), Id("b_86")]), Id("b_82")), CallExpr(Id("b_38"), Id("b_34"), [ArrayCell(Id("b_30"), BinaryOp("||", ArrayCell(Id("b_58"), BinaryOp("*", Id("b_17"), Id("b_76"))), Id("b_79"))), Id("b_76")])))], [CallStmt(Id("b_23"), Id("b_23"), [BooleanLiteral(False), Id("b_100")])])), MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_60"), IntType(), None), VarDecl(Id("b_94"), IntType(), None), VarDecl(Id("b_35"), IntType(), None)], None, Block([VarDecl(Id("b_8"), ArrayType(1, FloatType()), None), VarDecl(Id("b_86"), ArrayType(1, FloatType()), BinaryOp("&&", BinaryOp("||", Id("b_54"), Id("b_39")), BinaryOp("^", Id("b_81"), ArrayCell(Id("b_100"), BinaryOp("/", ArrayLiteral([NullLiteral(), NullLiteral(), FloatLiteral(0.07)]), Id("b_11"))))))], []))], None)]))
        self.assertTrue(TestAST.test(input, expect, 371))

    def test_73(self):
        input = r"""class b_95 {
int b_22 = "string literal" ^ b_97[b_50.b_48.b_55(b_95, b_81.b_6) + {true}];
final static boolean[8] b_18 = b_18, b_9 = b_61;
}
"""
        expect = str(Program([ClassDecl(Id("b_95"), [AttributeDecl(Instance(), VarDecl(Id("b_22"), IntType(), BinaryOp("^", StringLiteral('"string literal"'), ArrayCell(Id("b_97"), BinaryOp("+", CallExpr(FieldAccess(Id("b_50"), Id("b_48")), Id("b_55"), [Id("b_95"), FieldAccess(Id("b_81"), Id("b_6"))]), ArrayLiteral([BooleanLiteral(True)])))))), AttributeDecl(Static(), ConstDecl(Id("b_18"), ArrayType(8, BoolType()), Id("b_18"))), AttributeDecl(Static(), ConstDecl(Id("b_9"), ArrayType(8, BoolType()), Id("b_61")))], None)]))
        self.assertTrue(TestAST.test(input, expect, 372))

    def test_74(self):
        input = r"""class b_80 {
b_84(float[9] b_100, b_24; int[6] b_48) {
string[9] b_17 = b_99;
}
static int[10] b_41 = b_87, b_61 = 0.44;
}
"""
        expect = str(Program([ClassDecl(Id("b_80"), [MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_100"), ArrayType(9, FloatType()), None), VarDecl(Id("b_24"), ArrayType(9, FloatType()), None), VarDecl(Id("b_48"), ArrayType(6, IntType()), None)], None, Block([VarDecl(Id("b_17"), ArrayType(9, StringType()), Id("b_99"))], [])), AttributeDecl(Static(), VarDecl(Id("b_41"), ArrayType(10, IntType()), Id("b_87"))), AttributeDecl(Static(), VarDecl(Id("b_61"), ArrayType(10, IntType()), FloatLiteral(0.44)))], None)]))
        self.assertTrue(TestAST.test(input, expect, 373))

    def test_75(self):
        input = r"""class b_82 extends b_94 {
final b_42 b_20 = b_89 || b_70, b_22 = {nil, 0.08, 12, true, 0.96};
b_59(b_40 b_97, b_56; int b_3) {
void b_9 = b_58 - b_75, b_21;
}
}
class b_47 extends b_93 {
b_50(int[6] b_99, b_37; b_82 b_49) {
}
b_46 b_74(int[1] b_49, b_2; int b_35) {
b_83[10] b_70 = b_82, b_65;
break;
}
}
"""
        expect = str(Program([ClassDecl(Id("b_82"), [AttributeDecl(Instance(), ConstDecl(Id("b_20"), ClassType(Id("b_42")), BinaryOp("||", Id("b_89"), Id("b_70")))), AttributeDecl(Instance(), ConstDecl(Id("b_22"), ClassType(Id("b_42")), ArrayLiteral([NullLiteral(), FloatLiteral(0.08), IntLiteral(12), BooleanLiteral(True), FloatLiteral(0.96)]))), MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_97"), ClassType(Id("b_40")), None), VarDecl(Id("b_56"), ClassType(Id("b_40")), None), VarDecl(Id("b_3"), IntType(), None)], None, Block([VarDecl(Id("b_9"), VoidType(), BinaryOp("-", Id("b_58"), Id("b_75"))), VarDecl(Id("b_21"), VoidType(), None)], []))], Id("b_94")), ClassDecl(Id("b_47"), [MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_99"), ArrayType(6, IntType()), None), VarDecl(Id("b_37"), ArrayType(6, IntType()), None), VarDecl(Id("b_49"), ClassType(Id("b_82")), None)], None, Block([], [])), MethodDecl(Instance(), Id("b_74"), [VarDecl(Id("b_49"), ArrayType(1, IntType()), None), VarDecl(Id("b_2"), ArrayType(1, IntType()), None), VarDecl(Id("b_35"), IntType(), None)], ClassType(Id("b_46")), Block([VarDecl(Id("b_70"), ArrayType(10, ClassType(Id("b_83"))), Id("b_82")), VarDecl(Id("b_65"), ArrayType(10, ClassType(Id("b_83"))), None)], [Break()]))], Id("b_93"))]))
        self.assertTrue(TestAST.test(input, expect, 374))

    def test_76(self):
        input = r"""class b_58 extends b_15 {
b_88(float b_89, b_79; void b_79) {
}
static float[1] b_76;
}
class b_59 {
b_11(float[8] b_10, b_47; boolean[5] b_48) {
return ({true} || b_7) / b_57 && b_46;
}
void b_8(boolean[6] b_31, b_55; float b_6) {
}
}
"""
        expect = str(Program([ClassDecl(Id("b_58"), [MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_89"), FloatType(), None), VarDecl(Id("b_79"), FloatType(), None), VarDecl(Id("b_79"), VoidType(), None)], None, Block([], [])), AttributeDecl(Static(), VarDecl(Id("b_76"), ArrayType(1, FloatType()), None))], Id("b_15")), ClassDecl(Id("b_59"), [MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_10"), ArrayType(8, FloatType()), None), VarDecl(Id("b_47"), ArrayType(8, FloatType()), None), VarDecl(Id("b_48"), ArrayType(5, BoolType()), None)], None, Block([], [Return(BinaryOp("&&", BinaryOp("/", BinaryOp("||", ArrayLiteral([BooleanLiteral(True)]), Id("b_7")), Id("b_57")), Id("b_46")))])), MethodDecl(Instance(), Id("b_8"), [VarDecl(Id("b_31"), ArrayType(6, BoolType()), None), VarDecl(Id("b_55"), ArrayType(6, BoolType()), None), VarDecl(Id("b_6"), FloatType(), None)], VoidType(), Block([], []))], None)]))
        self.assertTrue(TestAST.test(input, expect, 375))

    def test_77(self):
        input = r"""class b_20 {
string b_89(boolean b_37, b_46; b_67 b_85) {
int b_97 = (0.67 || false && (b_22[b_84 ^ b_58[(b_51 + b_39.b_30)]] ^ b_4.b_50.b_39({this}, b_60))), b_41;
}
int b_1(void b_18, b_4; int[2] b_41) {
break;
}
}
class b_23 {
string b_98(float b_72, b_70; b_72[1] b_20) {
}
float b_35(b_99[1] b_13, b_77; float[5] b_59) {
return (b_74[(b_72 ^ b_77)] * b_51.b_47.b_48(b_53 && 6, {"string literal", "string literal"}));
}
}
"""
        expect = str(Program([ClassDecl(Id("b_20"), [MethodDecl(Instance(), Id("b_89"), [VarDecl(Id("b_37"), BoolType(), None), VarDecl(Id("b_46"), BoolType(), None), VarDecl(Id("b_85"), ClassType(Id("b_67")), None)], StringType(), Block([VarDecl(Id("b_97"), IntType(), BinaryOp("&&", BinaryOp("||", FloatLiteral(0.67), BooleanLiteral(False)), BinaryOp("^", ArrayCell(Id("b_22"), BinaryOp("^", Id("b_84"), ArrayCell(Id("b_58"), BinaryOp("+", Id("b_51"), FieldAccess(Id("b_39"), Id("b_30")))))), CallExpr(FieldAccess(Id("b_4"), Id("b_50")), Id("b_39"), [ArrayLiteral([SelfLiteral()]), Id("b_60")])))), VarDecl(Id("b_41"), IntType(), None)], [])), MethodDecl(Instance(), Id("b_1"), [VarDecl(Id("b_18"), VoidType(), None), VarDecl(Id("b_4"), VoidType(), None), VarDecl(Id("b_41"), ArrayType(2, IntType()), None)], IntType(), Block([], [Break()]))], None), ClassDecl(Id("b_23"), [MethodDecl(Instance(), Id("b_98"), [VarDecl(Id("b_72"), FloatType(), None), VarDecl(Id("b_70"), FloatType(), None), VarDecl(Id("b_20"), ArrayType(1, ClassType(Id("b_72"))), None)], StringType(), Block([], [])), MethodDecl(Instance(), Id("b_35"), [VarDecl(Id("b_13"), ArrayType(1, ClassType(Id("b_99"))), None), VarDecl(Id("b_77"), ArrayType(1, ClassType(Id("b_99"))), None), VarDecl(Id("b_59"), ArrayType(5, FloatType()), None)], FloatType(), Block([], [Return(BinaryOp("*", ArrayCell(Id("b_74"), BinaryOp("^", Id("b_72"), Id("b_77"))), CallExpr(FieldAccess(Id("b_51"), Id("b_47")), Id("b_48"), [BinaryOp("&&", Id("b_53"), IntLiteral(6)), ArrayLiteral([StringLiteral('"string literal"'), StringLiteral('"string literal"')])])))]))], None)]))
        self.assertTrue(TestAST.test(input, expect, 376))

    def test_78(self):
        input = r"""class b_61 {
void b_26(string[9] b_62, b_11; float[5] b_21) {
boolean b_100 = "string literal" ^ b_40, b_82;
}
float b_92 = nil, b_86;
}
class b_94 {
void b_95(boolean b_28, b_56; boolean b_87) {
void b_18 = ({"string literal", nil, this, nil, true} ^ b_60), b_5 = b_28 + {"string literal", 8, nil};
}
b_5(boolean[6] b_96, b_80; void[10] b_37) {
boolean b_88 = b_19;
{
void b_73, b_19;
}
}
}
"""
        expect = str(Program([ClassDecl(Id("b_61"), [MethodDecl(Instance(), Id("b_26"), [VarDecl(Id("b_62"), ArrayType(9, StringType()), None), VarDecl(Id("b_11"), ArrayType(9, StringType()), None), VarDecl(Id("b_21"), ArrayType(5, FloatType()), None)], VoidType(), Block([VarDecl(Id("b_100"), BoolType(), BinaryOp("^", StringLiteral('"string literal"'), Id("b_40"))), VarDecl(Id("b_82"), BoolType(), None)], [])), AttributeDecl(Instance(), VarDecl(Id("b_92"), FloatType(), NullLiteral())), AttributeDecl(Instance(), VarDecl(Id("b_86"), FloatType(), None))], None), ClassDecl(Id("b_94"), [MethodDecl(Instance(), Id("b_95"), [VarDecl(Id("b_28"), BoolType(), None), VarDecl(Id("b_56"), BoolType(), None), VarDecl(Id("b_87"), BoolType(), None)], VoidType(), Block([VarDecl(Id("b_18"), VoidType(), BinaryOp("^", ArrayLiteral([StringLiteral('"string literal"'), NullLiteral(), SelfLiteral(), NullLiteral(), BooleanLiteral(True)]), Id("b_60"))), VarDecl(Id("b_5"), VoidType(), BinaryOp("+", Id("b_28"), ArrayLiteral([StringLiteral('"string literal"'), IntLiteral(8), NullLiteral()])))], [])), MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_96"), ArrayType(6, BoolType()), None), VarDecl(Id("b_80"), ArrayType(6, BoolType()), None), VarDecl(Id("b_37"), ArrayType(10, VoidType()), None)], None, Block([VarDecl(Id("b_88"), BoolType(), Id("b_19"))], [Block([VarDecl(Id("b_73"), VoidType(), None), VarDecl(Id("b_19"), VoidType(), None)], [])]))], None)]))
        self.assertTrue(TestAST.test(input, expect, 377))

    def test_79(self):
        input = r"""class b_6 {
b_14(boolean b_95, b_29; boolean b_52) {
}
static float[5] b_86 = b_3, b_53 = b_73;
}
class b_1 {
void b_18 = b_98;
b_43(string b_86, b_92; boolean[10] b_82) {
b_19.b_38((b_90[b_16 + "string literal"] && b_5.b_53((b_44.b_29.b_80((b_10.b_95.b_94(b_13 || {"string literal", 2, 0.6, "string literal", 0.69}, b_49) ^ nil), {this, 14, "string literal", "string literal"}) ^ b_88.b_10), b_66)), b_96[b_51 ^ true]);
}
}
"""
        expect = str(Program([ClassDecl(Id("b_6"), [MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_95"), BoolType(), None), VarDecl(Id("b_29"), BoolType(), None), VarDecl(Id("b_52"), BoolType(), None)], None, Block([], [])), AttributeDecl(Static(), VarDecl(Id("b_86"), ArrayType(5, FloatType()), Id("b_3"))), AttributeDecl(Static(), VarDecl(Id("b_53"), ArrayType(5, FloatType()), Id("b_73")))], None), ClassDecl(Id("b_1"), [AttributeDecl(Instance(), VarDecl(Id("b_18"), VoidType(), Id("b_98"))), MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_86"), StringType(), None), VarDecl(Id("b_92"), StringType(), None), VarDecl(Id("b_82"), ArrayType(10, BoolType()), None)], None, Block([], [CallStmt(Id("b_19"), Id("b_38"), [BinaryOp("&&", ArrayCell(Id("b_90"), BinaryOp("+", Id("b_16"), StringLiteral('"string literal"'))), CallExpr(Id("b_5"), Id("b_53"), [BinaryOp("^", CallExpr(FieldAccess(Id("b_44"), Id("b_29")), Id("b_80"), [BinaryOp("^", CallExpr(FieldAccess(Id("b_10"), Id("b_95")), Id("b_94"), [BinaryOp("||", Id("b_13"), ArrayLiteral([StringLiteral('"string literal"'), IntLiteral(2), FloatLiteral(0.6), StringLiteral('"string literal"'), FloatLiteral(0.69)])), Id("b_49")]), NullLiteral()), ArrayLiteral([SelfLiteral(), IntLiteral(14), StringLiteral('"string literal"'), StringLiteral('"string literal"')])]), FieldAccess(Id("b_88"), Id("b_10"))), Id("b_66")])), ArrayCell(Id("b_96"), BinaryOp("^", Id("b_51"), BooleanLiteral(True)))])]))], None)]))
        self.assertTrue(TestAST.test(input, expect, 378))

    def test_80(self):
        input = r"""class b_22 {
b_46(boolean[2] b_94, b_24; boolean b_89) {
}
b_55 b_87(float b_45, b_81; int b_37) {
return b_58 ^ {true} + b_26.b_69(b_37[(b_28 * b_54)] - "string literal", b_52[(b_38 + b_26)]);
}
}
class b_92 {
static b_28[7] b_33 = {false, "string literal", "string literal", 1}, b_90 = {0.1, 6};
final static int b_59;
}
"""
        expect = str(Program([ClassDecl(Id("b_22"), [MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_94"), ArrayType(2, BoolType()), None), VarDecl(Id("b_24"), ArrayType(2, BoolType()), None), VarDecl(Id("b_89"), BoolType(), None)], None, Block([], [])), MethodDecl(Instance(), Id("b_87"), [VarDecl(Id("b_45"), FloatType(), None), VarDecl(Id("b_81"), FloatType(), None), VarDecl(Id("b_37"), IntType(), None)], ClassType(Id("b_55")), Block([], [Return(BinaryOp("+", BinaryOp("^", Id("b_58"), ArrayLiteral([BooleanLiteral(True)])), CallExpr(Id("b_26"), Id("b_69"), [BinaryOp("-", ArrayCell(Id("b_37"), BinaryOp("*", Id("b_28"), Id("b_54"))), StringLiteral('"string literal"')), ArrayCell(Id("b_52"), BinaryOp("+", Id("b_38"), Id("b_26")))])))]))], None), ClassDecl(Id("b_92"), [AttributeDecl(Static(), VarDecl(Id("b_33"), ArrayType(7, ClassType(Id("b_28"))), ArrayLiteral([BooleanLiteral(False), StringLiteral('"string literal"'), StringLiteral('"string literal"'), IntLiteral(1)]))), AttributeDecl(Static(), VarDecl(Id("b_90"), ArrayType(7, ClassType(Id("b_28"))), ArrayLiteral([FloatLiteral(0.1), IntLiteral(6)]))), AttributeDecl(Static(), ConstDecl(Id("b_59"), IntType(), None))], None)]))
        self.assertTrue(TestAST.test(input, expect, 379))

    def test_81(self):
        input = r"""class b_65 extends b_27 {
b_55(string[1] b_96, b_6; b_39 b_25) {
for b_85 := b_21 && b_68 downto b_88 do
b_41.b_74 := (b_23 / b_81);
}
static float b_65, b_33;
}
class b_5 {
float b_93(void[5] b_73, b_1; b_34 b_73) {
boolean b_34 = (b_76.b_77(b_18.b_18.b_68 - b_91.b_88((b_100 && {0.63, nil, nil, "string literal", 0.07}), false), b_57) + b_74) ^ (b_22 && b_82), b_52 = (18 * b_86[b_63]);
}
b_98(string[5] b_67, b_14; b_5 b_67) {
void[7] b_86 = b_35.b_81.b_93;
b_89[0] := b_47;
}
}
"""
        expect = str(Program([ClassDecl(Id("b_65"), [MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_96"), ArrayType(1, StringType()), None), VarDecl(Id("b_6"), ArrayType(1, StringType()), None), VarDecl(Id("b_25"), ClassType(Id("b_39")), None)], None, Block([], [For(Id("b_85"), BinaryOp("&&", Id("b_21"), Id("b_68")), Id("b_88"), False, Assign(FieldAccess(Id("b_41"), Id("b_74")), BinaryOp("/", Id("b_23"), Id("b_81"))))])), AttributeDecl(Static(), VarDecl(Id("b_65"), FloatType(), None)), AttributeDecl(Static(), VarDecl(Id("b_33"), FloatType(), None))], Id("b_27")), ClassDecl(Id("b_5"), [MethodDecl(Instance(), Id("b_93"), [VarDecl(Id("b_73"), ArrayType(5, VoidType()), None), VarDecl(Id("b_1"), ArrayType(5, VoidType()), None), VarDecl(Id("b_73"), ClassType(Id("b_34")), None)], FloatType(), Block([VarDecl(Id("b_34"), BoolType(), BinaryOp("^", BinaryOp("+", CallExpr(Id("b_76"), Id("b_77"), [BinaryOp("-", FieldAccess(FieldAccess(Id("b_18"), Id("b_18")), Id("b_68")), CallExpr(Id("b_91"), Id("b_88"), [BinaryOp("&&", Id("b_100"), ArrayLiteral([FloatLiteral(0.63), NullLiteral(), NullLiteral(), StringLiteral('"string literal"'), FloatLiteral(0.07)])), BooleanLiteral(False)])), Id("b_57")]), Id("b_74")), BinaryOp("&&", Id("b_22"), Id("b_82")))), VarDecl(Id("b_52"), BoolType(), BinaryOp("*", IntLiteral(18), ArrayCell(Id("b_86"), Id("b_63"))))], [])), MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_67"), ArrayType(5, StringType()), None), VarDecl(Id("b_14"), ArrayType(5, StringType()), None), VarDecl(Id("b_67"), ClassType(Id("b_5")), None)], None, Block([VarDecl(Id("b_86"), ArrayType(7, VoidType()), FieldAccess(FieldAccess(Id("b_35"), Id("b_81")), Id("b_93")))], [Assign(ArrayCell(Id("b_89"), IntLiteral(0)), Id("b_47"))]))], None)]))
        self.assertTrue(TestAST.test(input, expect, 380))

    def test_82(self):
        input = r"""class b_95 {
static float b_62, b_2;
b_32(void[7] b_29, b_89; float b_12) {
float b_13;
break;
}
}
class b_92 {
string b_67(int b_11, b_62; float b_52) {
for b_18 := (b_75 * b_91) downto 0.43 ^ b_87[b_55 - {nil}] do
b_11.b_18(b_76.b_13({0, this, 0.69, "string literal", this} || b_88, b_89[b_33 + b_67]), nil);
}
static b_93[6] b_14, b_97 = b_3;
}
"""
        expect = str(Program([ClassDecl(Id("b_95"), [AttributeDecl(Static(), VarDecl(Id("b_62"), FloatType(), None)), AttributeDecl(Static(), VarDecl(Id("b_2"), FloatType(), None)), MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_29"), ArrayType(7, VoidType()), None), VarDecl(Id("b_89"), ArrayType(7, VoidType()), None), VarDecl(Id("b_12"), FloatType(), None)], None, Block([VarDecl(Id("b_13"), FloatType(), None)], [Break()]))], None), ClassDecl(Id("b_92"), [MethodDecl(Instance(), Id("b_67"), [VarDecl(Id("b_11"), IntType(), None), VarDecl(Id("b_62"), IntType(), None), VarDecl(Id("b_52"), FloatType(), None)], StringType(), Block([], [For(Id("b_18"), BinaryOp("*", Id("b_75"), Id("b_91")), BinaryOp("^", FloatLiteral(0.43), ArrayCell(Id("b_87"), BinaryOp("-", Id("b_55"), ArrayLiteral([NullLiteral()])))), False, CallStmt(Id("b_11"), Id("b_18"), [CallExpr(Id("b_76"), Id("b_13"), [BinaryOp("||", ArrayLiteral([IntLiteral(0), SelfLiteral(), FloatLiteral(0.69), StringLiteral('"string literal"'), SelfLiteral()]), Id("b_88")), ArrayCell(Id("b_89"), BinaryOp("+", Id("b_33"), Id("b_67")))]), NullLiteral()]))])), AttributeDecl(Static(), VarDecl(Id("b_14"), ArrayType(6, ClassType(Id("b_93"))), None)), AttributeDecl(Static(), VarDecl(Id("b_97"), ArrayType(6, ClassType(Id("b_93"))), Id("b_3")))], None)]))
        self.assertTrue(TestAST.test(input, expect, 381))

    def test_83(self):
        input = r"""class b_84 {
b_30(b_75[2] b_60, b_16; int b_23) {
float[6] b_59, b_21;
}
final b_55 b_0 = (({4, this, nil, this} / b_61) + (b_87 || b_91));
}
class b_85 extends b_83 {
void[9] b_91, b_96 = b_38;
b_73 b_71(string[6] b_94, b_16; string[1] b_69) {
b_37 b_95 = b_52 || b_42;
}
}
"""
        expect = str(Program([ClassDecl(Id("b_84"), [MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_60"), ArrayType(2, ClassType(Id("b_75"))), None), VarDecl(Id("b_16"), ArrayType(2, ClassType(Id("b_75"))), None), VarDecl(Id("b_23"), IntType(), None)], None, Block([VarDecl(Id("b_59"), ArrayType(6, FloatType()), None), VarDecl(Id("b_21"), ArrayType(6, FloatType()), None)], [])), AttributeDecl(Instance(), ConstDecl(Id("b_0"), ClassType(Id("b_55")), BinaryOp("+", BinaryOp("/", ArrayLiteral([IntLiteral(4), SelfLiteral(), NullLiteral(), SelfLiteral()]), Id("b_61")), BinaryOp("||", Id("b_87"), Id("b_91")))))], None), ClassDecl(Id("b_85"), [AttributeDecl(Instance(), VarDecl(Id("b_91"), ArrayType(9, VoidType()), None)), AttributeDecl(Instance(), VarDecl(Id("b_96"), ArrayType(9, VoidType()), Id("b_38"))), MethodDecl(Instance(), Id("b_71"), [VarDecl(Id("b_94"), ArrayType(6, StringType()), None), VarDecl(Id("b_16"), ArrayType(6, StringType()), None), VarDecl(Id("b_69"), ArrayType(1, StringType()), None)], ClassType(Id("b_73")), Block([VarDecl(Id("b_95"), ClassType(Id("b_37")), BinaryOp("||", Id("b_52"), Id("b_42")))], []))], Id("b_83"))]))
        self.assertTrue(TestAST.test(input, expect, 382))

    def test_84(self):
        input = r"""class b_57 {
b_93(int[4] b_42, b_46; b_38[5] b_72) {
b_23[4] := ({nil, "string literal"} && b_30);
}
b_51 b_63(b_55 b_38, b_49; b_54[8] b_11) {
b_3 := b_53[b_0 - b_97];
}
}
class b_95 {
final static boolean b_80 = b_1;
final static void[10] b_49;
}
"""
        expect = str(Program([ClassDecl(Id("b_57"), [MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_42"), ArrayType(4, IntType()), None), VarDecl(Id("b_46"), ArrayType(4, IntType()), None), VarDecl(Id("b_72"), ArrayType(5, ClassType(Id("b_38"))), None)], None, Block([], [Assign(ArrayCell(Id("b_23"), IntLiteral(4)), BinaryOp("&&", ArrayLiteral([NullLiteral(), StringLiteral('"string literal"')]), Id("b_30")))])), MethodDecl(Instance(), Id("b_63"), [VarDecl(Id("b_38"), ClassType(Id("b_55")), None), VarDecl(Id("b_49"), ClassType(Id("b_55")), None), VarDecl(Id("b_11"), ArrayType(8, ClassType(Id("b_54"))), None)], ClassType(Id("b_51")), Block([], [Assign(Id("b_3"), ArrayCell(Id("b_53"), BinaryOp("-", Id("b_0"), Id("b_97"))))]))], None), ClassDecl(Id("b_95"), [AttributeDecl(Static(), ConstDecl(Id("b_80"), BoolType(), Id("b_1"))), AttributeDecl(Static(), ConstDecl(Id("b_49"), ArrayType(10, VoidType()), None))], None)]))
        self.assertTrue(TestAST.test(input, expect, 383))

    def test_85(self):
        input = r"""class b_68 extends b_99 {
b_26(void b_68, b_65; void[6] b_7) {
continue;
}
string b_16(float[5] b_81, b_21; b_25[10] b_70) {
string b_75;
{
string[9] b_54;
}
}
}
class b_67 extends b_56 {
float b_76(boolean[6] b_10, b_39; b_56 b_14) {
}
final void b_53;
}
"""
        expect = str(Program([ClassDecl(Id("b_68"), [MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_68"), VoidType(), None), VarDecl(Id("b_65"), VoidType(), None), VarDecl(Id("b_7"), ArrayType(6, VoidType()), None)], None, Block([], [Continue()])), MethodDecl(Instance(), Id("b_16"), [VarDecl(Id("b_81"), ArrayType(5, FloatType()), None), VarDecl(Id("b_21"), ArrayType(5, FloatType()), None), VarDecl(Id("b_70"), ArrayType(10, ClassType(Id("b_25"))), None)], StringType(), Block([VarDecl(Id("b_75"), StringType(), None)], [Block([VarDecl(Id("b_54"), ArrayType(9, StringType()), None)], [])]))], Id("b_99")), ClassDecl(Id("b_67"), [MethodDecl(Instance(), Id("b_76"), [VarDecl(Id("b_10"), ArrayType(6, BoolType()), None), VarDecl(Id("b_39"), ArrayType(6, BoolType()), None), VarDecl(Id("b_14"), ClassType(Id("b_56")), None)], FloatType(), Block([], [])), AttributeDecl(Instance(), ConstDecl(Id("b_53"), VoidType(), None))], Id("b_56"))]))
        self.assertTrue(TestAST.test(input, expect, 384))

    def test_86(self):
        input = r"""class b_89 extends b_96 {
final static void[8] b_37 = b_25[(b_10 - {nil})], b_37;
float b_12(int[9] b_61, b_88; boolean[9] b_25) {
int b_3, b_92 = b_17.b_69.b_10(b_59.b_71.b_0, b_24);
b_42.b_45((b_58 && b_60), b_13);
}
}
class b_55 {
static void[3] b_46, b_43 = b_39[(b_44.b_81.b_85 ^ b_33.b_85.b_84(b_72 / b_16[b_5 && this], b_74[b_62 ^ b_14]))];
b_12(b_39[8] b_57, b_60; string b_55) {
b_94[9] b_87 = ("string literal" / 9), b_72 = b_28;
return b_68;
}
}
"""
        expect = str(Program([ClassDecl(Id("b_89"), [AttributeDecl(Static(), ConstDecl(Id("b_37"), ArrayType(8, VoidType()), ArrayCell(Id("b_25"), BinaryOp("-", Id("b_10"), ArrayLiteral([NullLiteral()]))))), AttributeDecl(Static(), ConstDecl(Id("b_37"), ArrayType(8, VoidType()), None)), MethodDecl(Instance(), Id("b_12"), [VarDecl(Id("b_61"), ArrayType(9, IntType()), None), VarDecl(Id("b_88"), ArrayType(9, IntType()), None), VarDecl(Id("b_25"), ArrayType(9, BoolType()), None)], FloatType(), Block([VarDecl(Id("b_3"), IntType(), None), VarDecl(Id("b_92"), IntType(), CallExpr(FieldAccess(Id("b_17"), Id("b_69")), Id("b_10"), [FieldAccess(FieldAccess(Id("b_59"), Id("b_71")), Id("b_0")), Id("b_24")]))], [CallStmt(Id("b_42"), Id("b_45"), [BinaryOp("&&", Id("b_58"), Id("b_60")), Id("b_13")])]))], Id("b_96")), ClassDecl(Id("b_55"), [AttributeDecl(Static(), VarDecl(Id("b_46"), ArrayType(3, VoidType()), None)), AttributeDecl(Static(), VarDecl(Id("b_43"), ArrayType(3, VoidType()), ArrayCell(Id("b_39"), BinaryOp("^", FieldAccess(FieldAccess(Id("b_44"), Id("b_81")), Id("b_85")), CallExpr(FieldAccess(Id("b_33"), Id("b_85")), Id("b_84"), [BinaryOp("/", Id("b_72"), ArrayCell(Id("b_16"), BinaryOp("&&", Id("b_5"), SelfLiteral()))), ArrayCell(Id("b_74"), BinaryOp("^", Id("b_62"), Id("b_14")))]))))), MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_57"), ArrayType(8, ClassType(Id("b_39"))), None), VarDecl(Id("b_60"), ArrayType(8, ClassType(Id("b_39"))), None), VarDecl(Id("b_55"), StringType(), None)], None, Block([VarDecl(Id("b_87"), ArrayType(9, ClassType(Id("b_94"))), BinaryOp("/", StringLiteral('"string literal"'), IntLiteral(9))), VarDecl(Id("b_72"), ArrayType(9, ClassType(Id("b_94"))), Id("b_28"))], [Return(Id("b_68"))]))], None)]))
        self.assertTrue(TestAST.test(input, expect, 385))

    def test_87(self):
        input = r"""class b_39 {
b_43(boolean[7] b_18, b_49; b_95 b_61) {
string b_24 = (b_45 || b_44), b_23 = (b_45[b_4[b_26 && b_52]] + true * {0.39, this, "string literal", this});
}
b_95(void[8] b_19, b_98; int b_88) {
b_37[8] b_71 = b_41 + (b_76 ^ b_9), b_76;
}
}
class b_24 {
b_79(string b_44, b_52; int b_33) {
int[1] b_35 = b_28.b_65(b_75 - b_96, b_21);
}
b_76 b_53 = b_39, b_97 = (b_43.b_92.b_21 + b_57[b_18 * b_35] || b_49[b_5 - b_80]);
}
"""
        expect = str(Program([ClassDecl(Id("b_39"), [MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_18"), ArrayType(7, BoolType()), None), VarDecl(Id("b_49"), ArrayType(7, BoolType()), None), VarDecl(Id("b_61"), ClassType(Id("b_95")), None)], None, Block([VarDecl(Id("b_24"), StringType(), BinaryOp("||", Id("b_45"), Id("b_44"))), VarDecl(Id("b_23"), StringType(), BinaryOp("+", ArrayCell(Id("b_45"), ArrayCell(Id("b_4"), BinaryOp("&&", Id("b_26"), Id("b_52")))), BinaryOp("*", BooleanLiteral(True), ArrayLiteral([FloatLiteral(0.39), SelfLiteral(), StringLiteral('"string literal"'), SelfLiteral()]))))], [])), MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_19"), ArrayType(8, VoidType()), None), VarDecl(Id("b_98"), ArrayType(8, VoidType()), None), VarDecl(Id("b_88"), IntType(), None)], None, Block([VarDecl(Id("b_71"), ArrayType(8, ClassType(Id("b_37"))), BinaryOp("+", Id("b_41"), BinaryOp("^", Id("b_76"), Id("b_9")))), VarDecl(Id("b_76"), ArrayType(8, ClassType(Id("b_37"))), None)], []))], None), ClassDecl(Id("b_24"), [MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_44"), StringType(), None), VarDecl(Id("b_52"), StringType(), None), VarDecl(Id("b_33"), IntType(), None)], None, Block([VarDecl(Id("b_35"), ArrayType(1, IntType()), CallExpr(Id("b_28"), Id("b_65"), [BinaryOp("-", Id("b_75"), Id("b_96")), Id("b_21")]))], [])), AttributeDecl(Instance(), VarDecl(Id("b_53"), ClassType(Id("b_76")), Id("b_39"))), AttributeDecl(Instance(), VarDecl(Id("b_97"), ClassType(Id("b_76")), BinaryOp("||", BinaryOp("+", FieldAccess(FieldAccess(Id("b_43"), Id("b_92")), Id("b_21")), ArrayCell(Id("b_57"), BinaryOp("*", Id("b_18"), Id("b_35")))), ArrayCell(Id("b_49"), BinaryOp("-", Id("b_5"), Id("b_80"))))))], None)]))
        self.assertTrue(TestAST.test(input, expect, 386))

    def test_88(self):
        input = r"""class b_84 extends b_83 {
b_66(void[6] b_4, b_31; boolean b_46) {
int b_75 = this - b_44 ^ b_94 + b_55.b_75.b_79((b_80 ^ b_41), this);
for b_58 := b_94.b_93.b_9(({6, this, "string literal"} && b_97), 0.48) downto "string literal" && (b_54 + b_37) do
b_37[3] := b_97.b_22.b_36;
}
b_73(string b_80, b_63; void b_29) {
}
}
class b_99 extends b_13 {
void b_70(b_1[8] b_60, b_2; b_8[10] b_21) {
if this > b_73 && b_95[{false, 0.23, nil, this, "string literal"} ^ b_75] then
if {true, nil, nil, 1, this} * b_25 < {true, "string literal", 8, true} then
this.b_77 := nil - b_33.b_75.b_74({0.45, 1, "string literal"} - b_23, b_50) && b_7["string literal" && b_86];
}
b_95(void b_37, b_75; b_9[7] b_16) {
void[8] b_11 = "string literal" || b_96.b_24(b_28 * b_2, b_58), b_36 = b_46;
b_92.b_20(b_36, {0.76, this, this, 7});
}
}
"""
        expect = str(Program([ClassDecl(Id("b_84"), [MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_4"), ArrayType(6, VoidType()), None), VarDecl(Id("b_31"), ArrayType(6, VoidType()), None), VarDecl(Id("b_46"), BoolType(), None)], None, Block([VarDecl(Id("b_75"), IntType(), BinaryOp("+", BinaryOp("-", SelfLiteral(), BinaryOp("^", Id("b_44"), Id("b_94"))), CallExpr(FieldAccess(Id("b_55"), Id("b_75")), Id("b_79"), [BinaryOp("^", Id("b_80"), Id("b_41")), SelfLiteral()])))], [For(Id("b_58"), CallExpr(FieldAccess(Id("b_94"), Id("b_93")), Id("b_9"), [BinaryOp("&&", ArrayLiteral([IntLiteral(6), SelfLiteral(), StringLiteral('"string literal"')]), Id("b_97")), FloatLiteral(0.48)]), BinaryOp("&&", StringLiteral('"string literal"'), BinaryOp("+", Id("b_54"), Id("b_37"))), False, Assign(ArrayCell(Id("b_37"), IntLiteral(3)), FieldAccess(FieldAccess(Id("b_97"), Id("b_22")), Id("b_36"))))])), MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_80"), StringType(), None), VarDecl(Id("b_63"), StringType(), None), VarDecl(Id("b_29"), VoidType(), None)], None, Block([], []))], Id("b_83")), ClassDecl(Id("b_99"), [MethodDecl(Instance(), Id("b_70"), [VarDecl(Id("b_60"), ArrayType(8, ClassType(Id("b_1"))), None), VarDecl(Id("b_2"), ArrayType(8, ClassType(Id("b_1"))), None), VarDecl(Id("b_21"), ArrayType(10, ClassType(Id("b_8"))), None)], VoidType(), Block([], [If(BinaryOp(">", SelfLiteral(), BinaryOp("&&", Id("b_73"), ArrayCell(Id("b_95"), BinaryOp("^", ArrayLiteral([BooleanLiteral(False), FloatLiteral(0.23), NullLiteral(), SelfLiteral(), StringLiteral('"string literal"')]), Id("b_75"))))), If(BinaryOp("<", BinaryOp("*", ArrayLiteral([BooleanLiteral(True), NullLiteral(), NullLiteral(), IntLiteral(1), SelfLiteral()]), Id("b_25")), ArrayLiteral([BooleanLiteral(True), StringLiteral('"string literal"'), IntLiteral(8), BooleanLiteral(True)])), Assign(FieldAccess(SelfLiteral(), Id("b_77")), BinaryOp("&&", BinaryOp("-", NullLiteral(), CallExpr(FieldAccess(Id("b_33"), Id("b_75")), Id("b_74"), [BinaryOp("-", ArrayLiteral([FloatLiteral(0.45), IntLiteral(1), StringLiteral('"string literal"')]), Id("b_23")), Id("b_50")])), ArrayCell(Id("b_7"), BinaryOp("&&", StringLiteral('"string literal"'), Id("b_86"))))), None), None)])), MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_37"), VoidType(), None), VarDecl(Id("b_75"), VoidType(), None), VarDecl(Id("b_16"), ArrayType(7, ClassType(Id("b_9"))), None)], None, Block([VarDecl(Id("b_11"), ArrayType(8, VoidType()), BinaryOp("||", StringLiteral('"string literal"'), CallExpr(Id("b_96"), Id("b_24"), [BinaryOp("*", Id("b_28"), Id("b_2")), Id("b_58")]))), VarDecl(Id("b_36"), ArrayType(8, VoidType()), Id("b_46"))], [CallStmt(Id("b_92"), Id("b_20"), [Id("b_36"), ArrayLiteral([FloatLiteral(0.76), SelfLiteral(), SelfLiteral(), IntLiteral(7)])])]))], Id("b_13"))]))
        self.assertTrue(TestAST.test(input, expect, 387))

    def test_89(self):
        input = r"""class b_78 extends b_69 {
b_48(boolean[5] b_72, b_85; float b_47) {
b_88.b_20 := b_15;
}
b_68(float b_77, b_4; b_76 b_71) {
return b_60;
}
}
class b_68 extends b_31 {
boolean b_25(b_66 b_80, b_86; b_3 b_93) {
continue;
}
int b_88(b_42 b_76, b_85; float b_98) {
}
}
"""
        expect = str(Program([ClassDecl(Id("b_78"), [MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_72"), ArrayType(5, BoolType()), None), VarDecl(Id("b_85"), ArrayType(5, BoolType()), None), VarDecl(Id("b_47"), FloatType(), None)], None, Block([], [Assign(FieldAccess(Id("b_88"), Id("b_20")), Id("b_15"))])), MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_77"), FloatType(), None), VarDecl(Id("b_4"), FloatType(), None), VarDecl(Id("b_71"), ClassType(Id("b_76")), None)], None, Block([], [Return(Id("b_60"))]))], Id("b_69")), ClassDecl(Id("b_68"), [MethodDecl(Instance(), Id("b_25"), [VarDecl(Id("b_80"), ClassType(Id("b_66")), None), VarDecl(Id("b_86"), ClassType(Id("b_66")), None), VarDecl(Id("b_93"), ClassType(Id("b_3")), None)], BoolType(), Block([], [Continue()])), MethodDecl(Instance(), Id("b_88"), [VarDecl(Id("b_76"), ClassType(Id("b_42")), None), VarDecl(Id("b_85"), ClassType(Id("b_42")), None), VarDecl(Id("b_98"), FloatType(), None)], IntType(), Block([], []))], Id("b_31"))]))
        self.assertTrue(TestAST.test(input, expect, 388))

    def test_90(self):
        input = r"""class b_91 extends b_75 {
b_12(string b_27, b_40; float[6] b_92) {
{
float b_88 = b_50[b_81 * b_26] * 0.62;
}
}
final static void b_4 = (b_1.b_71(b_39, b_27) - b_49);
boolean b_92(b_8[5] b_32, b_46; b_9[2] b_22) {
void[10] b_96, b_41;
{
}
}
}
class b_67 extends b_2 {
b_38(boolean[2] b_78, b_81; string[2] b_48) {
b_11[5] b_65;
for b_73 := b_54 && b_2 to b_8 - {false, 0.79} do
b_35[5] := ("string literal" / b_53);
}
b_67(boolean b_37, b_99; float b_50) {
}
final static int[9] b_60 = true, b_30;
}
"""
        expect = str(Program([ClassDecl(Id("b_91"), [MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_27"), StringType(), None), VarDecl(Id("b_40"), StringType(), None), VarDecl(Id("b_92"), ArrayType(6, FloatType()), None)], None, Block([], [Block([VarDecl(Id("b_88"), FloatType(), BinaryOp("*", ArrayCell(Id("b_50"), BinaryOp("*", Id("b_81"), Id("b_26"))), FloatLiteral(0.62)))], [])])), AttributeDecl(Static(), ConstDecl(Id("b_4"), VoidType(), BinaryOp("-", CallExpr(Id("b_1"), Id("b_71"), [Id("b_39"), Id("b_27")]), Id("b_49")))), MethodDecl(Instance(), Id("b_92"), [VarDecl(Id("b_32"), ArrayType(5, ClassType(Id("b_8"))), None), VarDecl(Id("b_46"), ArrayType(5, ClassType(Id("b_8"))), None), VarDecl(Id("b_22"), ArrayType(2, ClassType(Id("b_9"))), None)], BoolType(), Block([VarDecl(Id("b_96"), ArrayType(10, VoidType()), None), VarDecl(Id("b_41"), ArrayType(10, VoidType()), None)], [Block([], [])]))], Id("b_75")), ClassDecl(Id("b_67"), [MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_78"), ArrayType(2, BoolType()), None), VarDecl(Id("b_81"), ArrayType(2, BoolType()), None), VarDecl(Id("b_48"), ArrayType(2, StringType()), None)], None, Block([VarDecl(Id("b_65"), ArrayType(5, ClassType(Id("b_11"))), None)], [For(Id("b_73"), BinaryOp("&&", Id("b_54"), Id("b_2")), BinaryOp("-", Id("b_8"), ArrayLiteral([BooleanLiteral(False), FloatLiteral(0.79)])), True, Assign(ArrayCell(Id("b_35"), IntLiteral(5)), BinaryOp("/", StringLiteral('"string literal"'), Id("b_53"))))])), MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_37"), BoolType(), None), VarDecl(Id("b_99"), BoolType(), None), VarDecl(Id("b_50"), FloatType(), None)], None, Block([], [])), AttributeDecl(Static(), ConstDecl(Id("b_60"), ArrayType(9, IntType()), BooleanLiteral(True))), AttributeDecl(Static(), ConstDecl(Id("b_30"), ArrayType(9, IntType()), None))], Id("b_2"))]))
        self.assertTrue(TestAST.test(input, expect, 389))

    def test_91(self):
        input = r"""class b_62 {
static int[3] b_51 = b_18;
string b_11(string[4] b_95, b_54; string[2] b_96) {
boolean[5] b_61 = b_14.b_42.b_85((b_33 * this), b_89) ^ b_67 - b_88 + {0.93, this}, b_17 = (b_50 ^ b_95 ^ (false / b_26));
break;
}
static b_68[7] b_65 = b_8, b_68;
}
class b_35 {
b_62(b_34 b_25, b_69; b_96[9] b_4) {
b_91.b_22({this, false, 3, this}, b_11);
}
b_19(void[1] b_68, b_89; b_2[6] b_98) {
continue;
}
b_30 b_43(boolean[10] b_73, b_44; boolean[1] b_29) {
return b_19;
}
}
"""
        expect = str(Program([ClassDecl(Id("b_62"), [AttributeDecl(Static(), VarDecl(Id("b_51"), ArrayType(3, IntType()), Id("b_18"))), MethodDecl(Instance(), Id("b_11"), [VarDecl(Id("b_95"), ArrayType(4, StringType()), None), VarDecl(Id("b_54"), ArrayType(4, StringType()), None), VarDecl(Id("b_96"), ArrayType(2, StringType()), None)], StringType(), Block([VarDecl(Id("b_61"), ArrayType(5, BoolType()), BinaryOp("+", BinaryOp("-", BinaryOp("^", CallExpr(FieldAccess(Id("b_14"), Id("b_42")), Id("b_85"), [BinaryOp("*", Id("b_33"), SelfLiteral()), Id("b_89")]), Id("b_67")), Id("b_88")), ArrayLiteral([FloatLiteral(0.93), SelfLiteral()]))), VarDecl(Id("b_17"), ArrayType(5, BoolType()), BinaryOp("^", BinaryOp("^", Id("b_50"), Id("b_95")), BinaryOp("/", BooleanLiteral(False), Id("b_26"))))], [Break()])), AttributeDecl(Static(), VarDecl(Id("b_65"), ArrayType(7, ClassType(Id("b_68"))), Id("b_8"))), AttributeDecl(Static(), VarDecl(Id("b_68"), ArrayType(7, ClassType(Id("b_68"))), None))], None), ClassDecl(Id("b_35"), [MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_25"), ClassType(Id("b_34")), None), VarDecl(Id("b_69"), ClassType(Id("b_34")), None), VarDecl(Id("b_4"), ArrayType(9, ClassType(Id("b_96"))), None)], None, Block([], [CallStmt(Id("b_91"), Id("b_22"), [ArrayLiteral([SelfLiteral(), BooleanLiteral(False), IntLiteral(3), SelfLiteral()]), Id("b_11")])])), MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_68"), ArrayType(1, VoidType()), None), VarDecl(Id("b_89"), ArrayType(1, VoidType()), None), VarDecl(Id("b_98"), ArrayType(6, ClassType(Id("b_2"))), None)], None, Block([], [Continue()])), MethodDecl(Instance(), Id("b_43"), [VarDecl(Id("b_73"), ArrayType(10, BoolType()), None), VarDecl(Id("b_44"), ArrayType(10, BoolType()), None), VarDecl(Id("b_29"), ArrayType(1, BoolType()), None)], ClassType(Id("b_30")), Block([], [Return(Id("b_19"))]))], None)]))
        self.assertTrue(TestAST.test(input, expect, 390))

    def test_92(self):
        input = r"""class b_78 {
string b_63(void b_31, b_90; void[7] b_10) {
int[4] b_43 = nil;
}
b_42(boolean b_55, b_7; b_92 b_34) {
}
b_3(string[3] b_34, b_33; float[1] b_16) {
boolean b_94 = 0.53 / b_91 || b_20 ^ b_39, b_17 = (b_37[{0.91, "string literal", 0, nil, true} * b_72] || b_43 ^ (nil + b_84[b_20.b_9.b_9 - {"string literal", nil, 15, 0.61}]));
}
}
class b_100 {
final static boolean[5] b_63, b_20 = b_7;
void b_45(int b_4, b_45; string b_69) {
b_12.b_82(b_87, b_34);
}
void b_55(float[2] b_26, b_86; int[4] b_85) {
void[7] b_25 = nil;
}
}
"""
        expect = str(Program([ClassDecl(Id("b_78"), [MethodDecl(Instance(), Id("b_63"), [VarDecl(Id("b_31"), VoidType(), None), VarDecl(Id("b_90"), VoidType(), None), VarDecl(Id("b_10"), ArrayType(7, VoidType()), None)], StringType(), Block([VarDecl(Id("b_43"), ArrayType(4, IntType()), NullLiteral())], [])), MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_55"), BoolType(), None), VarDecl(Id("b_7"), BoolType(), None), VarDecl(Id("b_34"), ClassType(Id("b_92")), None)], None, Block([], [])), MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_34"), ArrayType(3, StringType()), None), VarDecl(Id("b_33"), ArrayType(3, StringType()), None), VarDecl(Id("b_16"), ArrayType(1, FloatType()), None)], None, Block([VarDecl(Id("b_94"), BoolType(), BinaryOp("||", BinaryOp("/", FloatLiteral(0.53), Id("b_91")), BinaryOp("^", Id("b_20"), Id("b_39")))), VarDecl(Id("b_17"), BoolType(), BinaryOp("||", ArrayCell(Id("b_37"), BinaryOp("*", ArrayLiteral([FloatLiteral(0.91), StringLiteral('"string literal"'), IntLiteral(0), NullLiteral(), BooleanLiteral(True)]), Id("b_72"))), BinaryOp("^", Id("b_43"), BinaryOp("+", NullLiteral(), ArrayCell(Id("b_84"), BinaryOp("-", FieldAccess(FieldAccess(Id("b_20"), Id("b_9")), Id("b_9")), ArrayLiteral([StringLiteral('"string literal"'), NullLiteral(), IntLiteral(15), FloatLiteral(0.61)])))))))], []))], None), ClassDecl(Id("b_100"), [AttributeDecl(Static(), ConstDecl(Id("b_63"), ArrayType(5, BoolType()), None)), AttributeDecl(Static(), ConstDecl(Id("b_20"), ArrayType(5, BoolType()), Id("b_7"))), MethodDecl(Instance(), Id("b_45"), [VarDecl(Id("b_4"), IntType(), None), VarDecl(Id("b_45"), IntType(), None), VarDecl(Id("b_69"), StringType(), None)], VoidType(), Block([], [CallStmt(Id("b_12"), Id("b_82"), [Id("b_87"), Id("b_34")])])), MethodDecl(Instance(), Id("b_55"), [VarDecl(Id("b_26"), ArrayType(2, FloatType()), None), VarDecl(Id("b_86"), ArrayType(2, FloatType()), None), VarDecl(Id("b_85"), ArrayType(4, IntType()), None)], VoidType(), Block([VarDecl(Id("b_25"), ArrayType(7, VoidType()), NullLiteral())], []))], None)]))
        self.assertTrue(TestAST.test(input, expect, 391))

    def test_93(self):
        input = r"""class b_35 extends b_71 {
b_94 b_10(boolean b_85, b_50; float[3] b_79) {
float b_18 = b_75[b_38], b_21;
for b_71 := b_38 downto nil ^ b_25 do
{
}
}
final int b_18 = (b_10 * b_4.b_20), b_28;
b_79(boolean[9] b_59, b_0; b_91 b_73) {
boolean[7] b_19, b_42;
}
}
class b_43 {
float b_53(string b_98, b_8; int[5] b_18) {
}
final float[4] b_63, b_79 = false * b_41;
final string b_11;
}
"""
        expect = str(Program([ClassDecl(Id("b_35"), [MethodDecl(Instance(), Id("b_10"), [VarDecl(Id("b_85"), BoolType(), None), VarDecl(Id("b_50"), BoolType(), None), VarDecl(Id("b_79"), ArrayType(3, FloatType()), None)], ClassType(Id("b_94")), Block([VarDecl(Id("b_18"), FloatType(), ArrayCell(Id("b_75"), Id("b_38"))), VarDecl(Id("b_21"), FloatType(), None)], [For(Id("b_71"), Id("b_38"), BinaryOp("^", NullLiteral(), Id("b_25")), False, Block([], []))])), AttributeDecl(Instance(), ConstDecl(Id("b_18"), IntType(), BinaryOp("*", Id("b_10"), FieldAccess(Id("b_4"), Id("b_20"))))), AttributeDecl(Instance(), ConstDecl(Id("b_28"), IntType(), None)), MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_59"), ArrayType(9, BoolType()), None), VarDecl(Id("b_0"), ArrayType(9, BoolType()), None), VarDecl(Id("b_73"), ClassType(Id("b_91")), None)], None, Block([VarDecl(Id("b_19"), ArrayType(7, BoolType()), None), VarDecl(Id("b_42"), ArrayType(7, BoolType()), None)], []))], Id("b_71")), ClassDecl(Id("b_43"), [MethodDecl(Instance(), Id("b_53"), [VarDecl(Id("b_98"), StringType(), None), VarDecl(Id("b_8"), StringType(), None), VarDecl(Id("b_18"), ArrayType(5, IntType()), None)], FloatType(), Block([], [])), AttributeDecl(Instance(), ConstDecl(Id("b_63"), ArrayType(4, FloatType()), None)), AttributeDecl(Instance(), ConstDecl(Id("b_79"), ArrayType(4, FloatType()), BinaryOp("*", BooleanLiteral(False), Id("b_41")))), AttributeDecl(Instance(), ConstDecl(Id("b_11"), StringType(), None))], None)]))
        self.assertTrue(TestAST.test(input, expect, 392))

    def test_94(self):
        input = r"""class b_61 {
static void b_26 = "string literal";
b_74(float[2] b_94, b_57; b_20 b_70) {
int b_65 = this, b_95;
}
b_40(string[7] b_68, b_90; b_69[6] b_69) {
float b_42;
return b_84 * {this, 0} + b_67;
}
}
class b_30 extends b_35 {
b_85 b_35(float[10] b_12, b_17; string[9] b_39) {
}
int b_84(float b_69, b_78; float[9] b_54) {
b_95.b_66({this} || b_11, b_53);
}
string[2] b_3 = b_20, b_55 = b_20;
}
"""
        expect = str(Program([ClassDecl(Id("b_61"), [AttributeDecl(Static(), VarDecl(Id("b_26"), VoidType(), StringLiteral('"string literal"'))), MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_94"), ArrayType(2, FloatType()), None), VarDecl(Id("b_57"), ArrayType(2, FloatType()), None), VarDecl(Id("b_70"), ClassType(Id("b_20")), None)], None, Block([VarDecl(Id("b_65"), IntType(), SelfLiteral()), VarDecl(Id("b_95"), IntType(), None)], [])), MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_68"), ArrayType(7, StringType()), None), VarDecl(Id("b_90"), ArrayType(7, StringType()), None), VarDecl(Id("b_69"), ArrayType(6, ClassType(Id("b_69"))), None)], None, Block([VarDecl(Id("b_42"), FloatType(), None)], [Return(BinaryOp("+", BinaryOp("*", Id("b_84"), ArrayLiteral([SelfLiteral(), IntLiteral(0)])), Id("b_67")))]))], None), ClassDecl(Id("b_30"), [MethodDecl(Instance(), Id("b_35"), [VarDecl(Id("b_12"), ArrayType(10, FloatType()), None), VarDecl(Id("b_17"), ArrayType(10, FloatType()), None), VarDecl(Id("b_39"), ArrayType(9, StringType()), None)], ClassType(Id("b_85")), Block([], [])), MethodDecl(Instance(), Id("b_84"), [VarDecl(Id("b_69"), FloatType(), None), VarDecl(Id("b_78"), FloatType(), None), VarDecl(Id("b_54"), ArrayType(9, FloatType()), None)], IntType(), Block([], [CallStmt(Id("b_95"), Id("b_66"), [BinaryOp("||", ArrayLiteral([SelfLiteral()]), Id("b_11")), Id("b_53")])])), AttributeDecl(Instance(), VarDecl(Id("b_3"), ArrayType(2, StringType()), Id("b_20"))), AttributeDecl(Instance(), VarDecl(Id("b_55"), ArrayType(2, StringType()), Id("b_20")))], Id("b_35"))]))
        self.assertTrue(TestAST.test(input, expect, 393))

    def test_95(self):
        input = r"""class b_81 {
boolean b_31(float[7] b_42, b_35; b_56 b_9) {
string[5] b_26 = b_69.b_65(b_15, b_82), b_59;
}
float[5] b_19 = (b_77 ^ b_67.b_25(b_96, b_1) + b_34 || b_9.b_75);
final float[9] b_4;
}
class b_30 {
final boolean b_45;
b_72(float b_55, b_72; float[2] b_64) {
b_25[3] := ((b_79[b_20 ^ {17, true, nil, this}] + 0.33) ^ nil || b_5[(b_23.b_22 || b_29)]);
}
b_27(void b_72, b_6; boolean b_10) {
float b_37, b_57 = b_44;
for b_63 := ((b_9[b_44.b_96.b_96] ^ b_5) && {nil, 19, 13, 0.44} || b_10.b_92) downto b_100[b_89] + (b_84[b_1[{"string literal", "string literal", nil} + {true, 0.18, 6}]] * b_32) do
{
b_38.b_93({nil, "string literal", 15, 12, nil}, b_5[(true * b_59.b_79.b_48((this + b_13), b_73))]);
}
}
}
"""
        expect = str(Program([ClassDecl(Id("b_81"), [MethodDecl(Instance(), Id("b_31"), [VarDecl(Id("b_42"), ArrayType(7, FloatType()), None), VarDecl(Id("b_35"), ArrayType(7, FloatType()), None), VarDecl(Id("b_9"), ClassType(Id("b_56")), None)], BoolType(), Block([VarDecl(Id("b_26"), ArrayType(5, StringType()), CallExpr(Id("b_69"), Id("b_65"), [Id("b_15"), Id("b_82")])), VarDecl(Id("b_59"), ArrayType(5, StringType()), None)], [])), AttributeDecl(Instance(), VarDecl(Id("b_19"), ArrayType(5, FloatType()), BinaryOp("||", BinaryOp("+", BinaryOp("^", Id("b_77"), CallExpr(Id("b_67"), Id("b_25"), [Id("b_96"), Id("b_1")])), Id("b_34")), FieldAccess(Id("b_9"), Id("b_75"))))), AttributeDecl(Instance(), ConstDecl(Id("b_4"), ArrayType(9, FloatType()), None))], None), ClassDecl(Id("b_30"), [AttributeDecl(Instance(), ConstDecl(Id("b_45"), BoolType(), None)), MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_55"), FloatType(), None), VarDecl(Id("b_72"), FloatType(), None), VarDecl(Id("b_64"), ArrayType(2, FloatType()), None)], None, Block([], [Assign(ArrayCell(Id("b_25"), IntLiteral(3)), BinaryOp("||", BinaryOp("^", BinaryOp("+", ArrayCell(Id("b_79"), BinaryOp("^", Id("b_20"), ArrayLiteral([IntLiteral(17), BooleanLiteral(True), NullLiteral(), SelfLiteral()]))), FloatLiteral(0.33)), NullLiteral()), ArrayCell(Id("b_5"), BinaryOp("||", FieldAccess(Id("b_23"), Id("b_22")), Id("b_29")))))])), MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_72"), VoidType(), None), VarDecl(Id("b_6"), VoidType(), None), VarDecl(Id("b_10"), BoolType(), None)], None, Block([VarDecl(Id("b_37"), FloatType(), None), VarDecl(Id("b_57"), FloatType(), Id("b_44"))], [For(Id("b_63"), BinaryOp("||", BinaryOp("&&", BinaryOp("^", ArrayCell(Id("b_9"), FieldAccess(FieldAccess(Id("b_44"), Id("b_96")), Id("b_96"))), Id("b_5")), ArrayLiteral([NullLiteral(), IntLiteral(19), IntLiteral(13), FloatLiteral(0.44)])), FieldAccess(Id("b_10"), Id("b_92"))), BinaryOp("+", ArrayCell(Id("b_100"), Id("b_89")), BinaryOp("*", ArrayCell(Id("b_84"), ArrayCell(Id("b_1"), BinaryOp("+", ArrayLiteral([StringLiteral('"string literal"'), StringLiteral('"string literal"'), NullLiteral()]), ArrayLiteral([BooleanLiteral(True), FloatLiteral(0.18), IntLiteral(6)])))), Id("b_32"))), False, Block([], [CallStmt(Id("b_38"), Id("b_93"), [ArrayLiteral([NullLiteral(), StringLiteral('"string literal"'), IntLiteral(15), IntLiteral(12), NullLiteral()]), ArrayCell(Id("b_5"), BinaryOp("*", BooleanLiteral(True), CallExpr(FieldAccess(Id("b_59"), Id("b_79")), Id("b_48"), [BinaryOp("+", SelfLiteral(), Id("b_13")), Id("b_73")])))])]))]))], None)]))
        self.assertTrue(TestAST.test(input, expect, 394))

    def test_96(self):
        input = r"""class b_25 {
b_61(b_48 b_23, b_49; b_61[2] b_97) {
void b_74 = b_85 * b_92 && b_1;
b_27.b_26("string literal", {true, "string literal", "string literal", 0.12});
}
void b_34(void b_25, b_11; string b_30) {
float[7] b_85;
{
}
}
float b_43(float[1] b_40, b_13; b_51[3] b_28) {
}
}
class b_91 {
final static int b_52;
int b_74(float[3] b_36, b_1; b_85[1] b_14) {
boolean b_71;
if (b_90 && b_92[b_59] ^ (b_54 * {nil})) > b_86.b_65.b_93 then
b_44 := {0.38, nil, this, this};
else
return (({this, this, 14, 0, nil} && b_25.b_54.b_23({0.35, nil}, {nil, false, false})) && b_98);
}
string b_66(string b_48, b_31; boolean[2] b_9) {
float b_68 = 3;
}
}
"""
        expect = str(Program([ClassDecl(Id("b_25"), [MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_23"), ClassType(Id("b_48")), None), VarDecl(Id("b_49"), ClassType(Id("b_48")), None), VarDecl(Id("b_97"), ArrayType(2, ClassType(Id("b_61"))), None)], None, Block([VarDecl(Id("b_74"), VoidType(), BinaryOp("&&", BinaryOp("*", Id("b_85"), Id("b_92")), Id("b_1")))], [CallStmt(Id("b_27"), Id("b_26"), [StringLiteral('"string literal"'), ArrayLiteral([BooleanLiteral(True), StringLiteral('"string literal"'), StringLiteral('"string literal"'), FloatLiteral(0.12)])])])), MethodDecl(Instance(), Id("b_34"), [VarDecl(Id("b_25"), VoidType(), None), VarDecl(Id("b_11"), VoidType(), None), VarDecl(Id("b_30"), StringType(), None)], VoidType(), Block([VarDecl(Id("b_85"), ArrayType(7, FloatType()), None)], [Block([], [])])), MethodDecl(Instance(), Id("b_43"), [VarDecl(Id("b_40"), ArrayType(1, FloatType()), None), VarDecl(Id("b_13"), ArrayType(1, FloatType()), None), VarDecl(Id("b_28"), ArrayType(3, ClassType(Id("b_51"))), None)], FloatType(), Block([], []))], None), ClassDecl(Id("b_91"), [AttributeDecl(Static(), ConstDecl(Id("b_52"), IntType(), None)), MethodDecl(Instance(), Id("b_74"), [VarDecl(Id("b_36"), ArrayType(3, FloatType()), None), VarDecl(Id("b_1"), ArrayType(3, FloatType()), None), VarDecl(Id("b_14"), ArrayType(1, ClassType(Id("b_85"))), None)], IntType(), Block([VarDecl(Id("b_71"), BoolType(), None)], [If(BinaryOp(">", BinaryOp("&&", Id("b_90"), BinaryOp("^", ArrayCell(Id("b_92"), Id("b_59")), BinaryOp("*", Id("b_54"), ArrayLiteral([NullLiteral()])))), FieldAccess(FieldAccess(Id("b_86"), Id("b_65")), Id("b_93"))), Assign(Id("b_44"), ArrayLiteral([FloatLiteral(0.38), NullLiteral(), SelfLiteral(), SelfLiteral()])), Return(BinaryOp("&&", BinaryOp("&&", ArrayLiteral([SelfLiteral(), SelfLiteral(), IntLiteral(14), IntLiteral(0), NullLiteral()]), CallExpr(FieldAccess(Id("b_25"), Id("b_54")), Id("b_23"), [ArrayLiteral([FloatLiteral(0.35), NullLiteral()]), ArrayLiteral([NullLiteral(), BooleanLiteral(False), BooleanLiteral(False)])])), Id("b_98"))))])), MethodDecl(Instance(), Id("b_66"), [VarDecl(Id("b_48"), StringType(), None), VarDecl(Id("b_31"), StringType(), None), VarDecl(Id("b_9"), ArrayType(2, BoolType()), None)], StringType(), Block([VarDecl(Id("b_68"), FloatType(), IntLiteral(3))], []))], None)]))
        self.assertTrue(TestAST.test(input, expect, 395))

    def test_97(self):
        input = r"""class b_33 extends b_69 {
b_11(void[9] b_5, b_64; boolean b_19) {
}
b_79(float[7] b_38, b_54; float b_86) {
void b_55 = (nil || b_81), b_4 = b_19.b_18.b_38((b_24 || b_70), 2) && b_12[b_45];
}
int b_14(boolean[9] b_31, b_34; float[2] b_41) {
float b_84;
b_64.b_73(b_99, b_73);
}
}
class b_83 {
void b_11, b_86;
float b_92(float b_38, b_95; string[4] b_44) {
b_37 b_22 = ({0.87} || b_90 && b_58);
}
boolean b_10(void[10] b_57, b_89; b_67 b_51) {
boolean b_43 = b_81 + b_88;
}
}
"""
        expect = str(Program([ClassDecl(Id("b_33"), [MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_5"), ArrayType(9, VoidType()), None), VarDecl(Id("b_64"), ArrayType(9, VoidType()), None), VarDecl(Id("b_19"), BoolType(), None)], None, Block([], [])), MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_38"), ArrayType(7, FloatType()), None), VarDecl(Id("b_54"), ArrayType(7, FloatType()), None), VarDecl(Id("b_86"), FloatType(), None)], None, Block([VarDecl(Id("b_55"), VoidType(), BinaryOp("||", NullLiteral(), Id("b_81"))), VarDecl(Id("b_4"), VoidType(), BinaryOp("&&", CallExpr(FieldAccess(Id("b_19"), Id("b_18")), Id("b_38"), [BinaryOp("||", Id("b_24"), Id("b_70")), IntLiteral(2)]), ArrayCell(Id("b_12"), Id("b_45"))))], [])), MethodDecl(Instance(), Id("b_14"), [VarDecl(Id("b_31"), ArrayType(9, BoolType()), None), VarDecl(Id("b_34"), ArrayType(9, BoolType()), None), VarDecl(Id("b_41"), ArrayType(2, FloatType()), None)], IntType(), Block([VarDecl(Id("b_84"), FloatType(), None)], [CallStmt(Id("b_64"), Id("b_73"), [Id("b_99"), Id("b_73")])]))], Id("b_69")), ClassDecl(Id("b_83"), [AttributeDecl(Instance(), VarDecl(Id("b_11"), VoidType(), None)), AttributeDecl(Instance(), VarDecl(Id("b_86"), VoidType(), None)), MethodDecl(Instance(), Id("b_92"), [VarDecl(Id("b_38"), FloatType(), None), VarDecl(Id("b_95"), FloatType(), None), VarDecl(Id("b_44"), ArrayType(4, StringType()), None)], FloatType(), Block([VarDecl(Id("b_22"), ClassType(Id("b_37")), BinaryOp("&&", BinaryOp("||", ArrayLiteral([FloatLiteral(0.87)]), Id("b_90")), Id("b_58")))], [])), MethodDecl(Instance(), Id("b_10"), [VarDecl(Id("b_57"), ArrayType(10, VoidType()), None), VarDecl(Id("b_89"), ArrayType(10, VoidType()), None), VarDecl(Id("b_51"), ClassType(Id("b_67")), None)], BoolType(), Block([VarDecl(Id("b_43"), BoolType(), BinaryOp("+", Id("b_81"), Id("b_88")))], []))], None)]))
        self.assertTrue(TestAST.test(input, expect, 396))

    def test_98(self):
        input = r"""class b_70 {
final static boolean[8] b_67, b_33;
float b_99(b_90 b_45, b_24; void b_56) {
}
static int b_77, b_89;
}
class b_99 {
void b_43(boolean[7] b_52, b_7; b_50[6] b_27) {
}
b_21(string[5] b_66, b_51; int[3] b_22) {
string[7] b_13 = 0.91 + (b_35.b_80 - b_70);
{
}
}
float b_40(string[10] b_94, b_29; void[9] b_33) {
float b_59, b_92;
break;
}
}
"""
        expect = str(Program([ClassDecl(Id("b_70"), [AttributeDecl(Static(), ConstDecl(Id("b_67"), ArrayType(8, BoolType()), None)), AttributeDecl(Static(), ConstDecl(Id("b_33"), ArrayType(8, BoolType()), None)), MethodDecl(Instance(), Id("b_99"), [VarDecl(Id("b_45"), ClassType(Id("b_90")), None), VarDecl(Id("b_24"), ClassType(Id("b_90")), None), VarDecl(Id("b_56"), VoidType(), None)], FloatType(), Block([], [])), AttributeDecl(Static(), VarDecl(Id("b_77"), IntType(), None)), AttributeDecl(Static(), VarDecl(Id("b_89"), IntType(), None))], None), ClassDecl(Id("b_99"), [MethodDecl(Instance(), Id("b_43"), [VarDecl(Id("b_52"), ArrayType(7, BoolType()), None), VarDecl(Id("b_7"), ArrayType(7, BoolType()), None), VarDecl(Id("b_27"), ArrayType(6, ClassType(Id("b_50"))), None)], VoidType(), Block([], [])), MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_66"), ArrayType(5, StringType()), None), VarDecl(Id("b_51"), ArrayType(5, StringType()), None), VarDecl(Id("b_22"), ArrayType(3, IntType()), None)], None, Block([VarDecl(Id("b_13"), ArrayType(7, StringType()), BinaryOp("+", FloatLiteral(0.91), BinaryOp("-", FieldAccess(Id("b_35"), Id("b_80")), Id("b_70"))))], [Block([], [])])), MethodDecl(Instance(), Id("b_40"), [VarDecl(Id("b_94"), ArrayType(10, StringType()), None), VarDecl(Id("b_29"), ArrayType(10, StringType()), None), VarDecl(Id("b_33"), ArrayType(9, VoidType()), None)], FloatType(), Block([VarDecl(Id("b_59"), FloatType(), None), VarDecl(Id("b_92"), FloatType(), None)], [Break()]))], None)]))
        self.assertTrue(TestAST.test(input, expect, 397))

    def test_99(self):
        input = r"""class b_27 extends b_40 {
void[10] b_60;
void b_81(boolean b_70, b_18; string[7] b_99) {
boolean[2] b_14 = b_9.b_31(b_21 / b_97, 0.14);
return b_38.b_91.b_80;
}
b_42(b_94[7] b_41, b_16; void[4] b_67) {
}
}
class b_5 extends b_51 {
b_12(string b_50, b_73; float[10] b_87) {
}
float b_76(boolean b_18, b_56; float[5] b_90) {
if (b_59 && b_65) <= b_41 then
if b_4.b_32.b_80(b_85, b_81) < b_80 * false + b_8 + b_97[b_35] then
if b_88 * 19 >= (b_99 || b_36 - {true, 14}) then
continue;
else
break;
else
if b_74 == b_38 then
return b_29 * b_43.b_21.b_5 || ({0.51, false} + b_83);
}
void b_20(boolean[3] b_77, b_11; float b_65) {
break;
}
}
"""
        expect = str(Program([ClassDecl(Id("b_27"), [AttributeDecl(Instance(), VarDecl(Id("b_60"), ArrayType(10, VoidType()), None)), MethodDecl(Instance(), Id("b_81"), [VarDecl(Id("b_70"), BoolType(), None), VarDecl(Id("b_18"), BoolType(), None), VarDecl(Id("b_99"), ArrayType(7, StringType()), None)], VoidType(), Block([VarDecl(Id("b_14"), ArrayType(2, BoolType()), CallExpr(Id("b_9"), Id("b_31"), [BinaryOp("/", Id("b_21"), Id("b_97")), FloatLiteral(0.14)]))], [Return(FieldAccess(FieldAccess(Id("b_38"), Id("b_91")), Id("b_80")))])), MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_41"), ArrayType(7, ClassType(Id("b_94"))), None), VarDecl(Id("b_16"), ArrayType(7, ClassType(Id("b_94"))), None), VarDecl(Id("b_67"), ArrayType(4, VoidType()), None)], None, Block([], []))], Id("b_40")), ClassDecl(Id("b_5"), [MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_50"), StringType(), None), VarDecl(Id("b_73"), StringType(), None), VarDecl(Id("b_87"), ArrayType(10, FloatType()), None)], None, Block([], [])), MethodDecl(Instance(), Id("b_76"), [VarDecl(Id("b_18"), BoolType(), None), VarDecl(Id("b_56"), BoolType(), None), VarDecl(Id("b_90"), ArrayType(5, FloatType()), None)], FloatType(), Block([], [If(BinaryOp("<=", BinaryOp("&&", Id("b_59"), Id("b_65")), Id("b_41")), If(BinaryOp("<", CallExpr(FieldAccess(Id("b_4"), Id("b_32")), Id("b_80"), [Id("b_85"), Id("b_81")]), BinaryOp("+", BinaryOp("+", BinaryOp("*", Id("b_80"), BooleanLiteral(False)), Id("b_8")), ArrayCell(Id("b_97"), Id("b_35")))), If(BinaryOp(">=", BinaryOp("*", Id("b_88"), IntLiteral(19)), BinaryOp("||", Id("b_99"), BinaryOp("-", Id("b_36"), ArrayLiteral([BooleanLiteral(True), IntLiteral(14)])))), Continue(), Break()), If(BinaryOp("==", Id("b_74"), Id("b_38")), Return(BinaryOp("||", BinaryOp("*", Id("b_29"), FieldAccess(FieldAccess(Id("b_43"), Id("b_21")), Id("b_5"))), BinaryOp("+", ArrayLiteral([FloatLiteral(0.51), BooleanLiteral(False)]), Id("b_83")))), None)), None)])), MethodDecl(Instance(), Id("b_20"), [VarDecl(Id("b_77"), ArrayType(3, BoolType()), None), VarDecl(Id("b_11"), ArrayType(3, BoolType()), None), VarDecl(Id("b_65"), FloatType(), None)], VoidType(), Block([], [Break()]))], Id("b_51"))]))
        self.assertTrue(TestAST.test(input, expect, 398))

    def test_100(self):
        input = r"""class b_13 {
b_3[9] b_55 = b_58, b_60 = (b_76 || b_85);
final static void[1] b_54;
b_32(boolean[10] b_88, b_35; float[6] b_78) {
return b_85;
}
}
class b_2 {
b_61 b_58(float[6] b_93, b_21; b_29 b_87) {
b_99.b_19((b_69 + b_31), b_24);
}
float b_65(int[1] b_69, b_51; string[9] b_69) {
boolean[9] b_20;
}
float b_95(void[9] b_37, b_52; boolean b_22) {
int b_58;
for b_54 := b_51.b_32(b_97 ^ b_55[(b_52 - b_22.b_66.b_95)], b_98) downto b_54 do
if (this + b_93[b_1]) > b_63 then
if b_25 == (b_6 / b_80[b_69 * b_13[b_80 || b_66]]) then
continue;
}
}
"""
        expect = str(Program([ClassDecl(Id("b_13"), [AttributeDecl(Instance(), VarDecl(Id("b_55"), ArrayType(9, ClassType(Id("b_3"))), Id("b_58"))), AttributeDecl(Instance(), VarDecl(Id("b_60"), ArrayType(9, ClassType(Id("b_3"))), BinaryOp("||", Id("b_76"), Id("b_85")))), AttributeDecl(Static(), ConstDecl(Id("b_54"), ArrayType(1, VoidType()), None)), MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("b_88"), ArrayType(10, BoolType()), None), VarDecl(Id("b_35"), ArrayType(10, BoolType()), None), VarDecl(Id("b_78"), ArrayType(6, FloatType()), None)], None, Block([], [Return(Id("b_85"))]))], None), ClassDecl(Id("b_2"), [MethodDecl(Instance(), Id("b_58"), [VarDecl(Id("b_93"), ArrayType(6, FloatType()), None), VarDecl(Id("b_21"), ArrayType(6, FloatType()), None), VarDecl(Id("b_87"), ClassType(Id("b_29")), None)], ClassType(Id("b_61")), Block([], [CallStmt(Id("b_99"), Id("b_19"), [BinaryOp("+", Id("b_69"), Id("b_31")), Id("b_24")])])), MethodDecl(Instance(), Id("b_65"), [VarDecl(Id("b_69"), ArrayType(1, IntType()), None), VarDecl(Id("b_51"), ArrayType(1, IntType()), None), VarDecl(Id("b_69"), ArrayType(9, StringType()), None)], FloatType(), Block([VarDecl(Id("b_20"), ArrayType(9, BoolType()), None)], [])), MethodDecl(Instance(), Id("b_95"), [VarDecl(Id("b_37"), ArrayType(9, VoidType()), None), VarDecl(Id("b_52"), ArrayType(9, VoidType()), None), VarDecl(Id("b_22"), BoolType(), None)], FloatType(), Block([VarDecl(Id("b_58"), IntType(), None)], [For(Id("b_54"), CallExpr(Id("b_51"), Id("b_32"), [BinaryOp("^", Id("b_97"), ArrayCell(Id("b_55"), BinaryOp("-", Id("b_52"), FieldAccess(FieldAccess(Id("b_22"), Id("b_66")), Id("b_95"))))), Id("b_98")]), Id("b_54"), False, If(BinaryOp(">", BinaryOp("+", SelfLiteral(), ArrayCell(Id("b_93"), Id("b_1"))), Id("b_63")), If(BinaryOp("==", Id("b_25"), BinaryOp("/", Id("b_6"), ArrayCell(Id("b_80"), BinaryOp("*", Id("b_69"), ArrayCell(Id("b_13"), BinaryOp("||", Id("b_80"), Id("b_66"))))))), Continue(), None), None))]))], None)]))
        self.assertTrue(TestAST.test(input, expect, 399))
