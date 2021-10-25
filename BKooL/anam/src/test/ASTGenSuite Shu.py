from main.bkool.utils.AST import ArrayCell, ArrayLiteral, ArrayType, Assign, AttributeDecl, BinaryOp, Block, BoolType, BooleanLiteral, Break, CallExpr, CallStmt, ClassDecl, ClassType, ConstDecl, Continue, FieldAccess, FloatLiteral, FloatType, For, Id, If, Instance, IntLiteral, IntType, MethodDecl, NewExpr, NullLiteral, Return, SelfLiteral, Static, StringLiteral, StringType, UnaryOp, VarDecl, VoidType
import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    #=======================================#
    #               300 - 309               #
    #=======================================#
    def test_class_decl_01(self):
        input = """class A {}"""
        expect = str(Program([ClassDecl(Id("A"),[])]))
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_class_decl_02(self):
        input = """class A extends B {}"""
        expect = str(Program([ClassDecl(Id("A"),[],Id("B"))]))
        self.assertTrue(TestAST.test(input, expect, 301))
    
    def test_class_decl_03(self):
        input = """class A {}
        class B extends A {}"""
        expect = str(Program([ClassDecl(Id("A"),[]),ClassDecl(Id("B"),[],Id("A"))]))
        self.assertTrue(TestAST.test(input, expect, 302))
    
    def test_class_decl_04(self):
        input = """class A {}
        class B extends A {}
        class C {}"""
        expect = str(Program([ClassDecl(Id("A"),[]),ClassDecl(Id("B"),[],Id("A")),ClassDecl(Id("C"),[])]))
        self.assertTrue(TestAST.test(input, expect, 303))
    
    def test_attr_decl_01(self):
        input = """class A {
            static int a;
            final int b = 4;
        }"""
        expect = str(Program([ClassDecl(Id("A"),[
            AttributeDecl(Static(),VarDecl(Id("a"),IntType())),
            AttributeDecl(Instance(),ConstDecl(Id("b"),IntType(),IntLiteral(4)))])]))
        self.assertTrue(TestAST.test(input, expect, 304))

    def test_attr_decl_02(self):
        input = """class A {
            static final float a = 2.100e12;
        }"""
        expect = str(Program([ClassDecl(Id("A"), [
            AttributeDecl(Static(),ConstDecl(Id("a"),FloatType(),FloatLiteral(2.100e12)))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 305))

    def test_attr_decl_03(self):
        input = """class A {
            final static string a = "Abc", b = "z a@ 1";
        }"""
        expect = str(Program([ClassDecl(Id("A"),[
            AttributeDecl(Static(),ConstDecl(Id("a"),StringType(),StringLiteral('''"Abc"'''))),
            AttributeDecl(Static(),ConstDecl(Id("b"),StringType(),StringLiteral('''"z a@ 1"''')))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 306))

    def test_attr_decl_04(self):
        input = """class A {
            int a, b, c;
            static float z = 2.1, d;
        }"""
        expect = str(Program([ClassDecl(Id("A"), [
            AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),
            AttributeDecl(Instance(),VarDecl(Id("b"),IntType())),
            AttributeDecl(Instance(),VarDecl(Id("c"),IntType())),
            AttributeDecl(Static(),VarDecl(Id("z"),FloatType(),FloatLiteral(2.1))),
            AttributeDecl(Static(),VarDecl(Id("d"),FloatType()))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 307))

    def test_attr_decl_05(self):
        input = """class A {
            int a = 2;
            final float c = 2.222;
            static final string str = "abc";
        }"""
        expect = str(Program([ClassDecl(Id("A"), [
            AttributeDecl(Instance(),VarDecl(Id("a"),IntType(),IntLiteral(2))),
            AttributeDecl(Instance(),ConstDecl(Id("c"),FloatType(),FloatLiteral(2.222))),
            AttributeDecl(Static(),ConstDecl(Id("str"),StringType(),StringLiteral('''"abc"''')))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 308))
    
    def test_attr_decl_06(self):
        input = """class A {
            int a;
            final float x = 5.0;
        }
        class C extends A{
            static int z = 5, x;
            final static int a = 2;
            static string s = "Hi!!!";
        }
        """
        expect = str(Program([
            ClassDecl(Id("A"), [
                AttributeDecl(Instance(), VarDecl(Id("a"),IntType())),
                AttributeDecl(Instance(), ConstDecl(Id("x"),FloatType(),FloatLiteral(5.0)))
            ]),
            ClassDecl(Id("C"),[
                AttributeDecl(Static(),VarDecl(Id("z"),IntType(),IntLiteral(5))),
                AttributeDecl(Static(),VarDecl(Id("x"),IntType())),
                AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(2))),
                AttributeDecl(Static(),VarDecl(Id("s"),StringType(),StringLiteral('''"Hi!!!"''')))
            ],Id("A"))]))
        self.assertTrue(TestAST.test(input, expect, 309))
    
    #=======================================#
    #               310 - 319               #
    #=======================================#
    def test_attr_decl_07(self):
        input = """class A {
            static B a;
            int[2] c;
        }"""
        expect = str(Program([ClassDecl(Id("A"), [
            AttributeDecl(Static(),VarDecl(Id("a"),ClassType(Id("B")))),
            AttributeDecl(Instance(),VarDecl(Id("c"),ArrayType(2,IntType())))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 310))

    def test_attr_decl_08(self):
        input = """class A {
            final static int[5] a = {1,2,3,4,5};
        }"""
        expect = str(Program([ClassDecl(Id("A"), [
            AttributeDecl(Static(),ConstDecl(Id("a"),ArrayType(5,IntType()),ArrayLiteral([
                IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5)])))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 311))

    def test_attr_decl_09(self):
        input = """class A {
            B a;
            final boolean[2] b = {true, false};
            static B[10] z;
        }"""
        expect = str(Program([ClassDecl(Id("A"), [
            AttributeDecl(Instance(),VarDecl(Id("a"),ClassType(Id("B")))),
            AttributeDecl(Instance(),ConstDecl(Id("b"),ArrayType(2,BoolType()),ArrayLiteral([
                BooleanLiteral(True),BooleanLiteral(False)
            ]))),
            AttributeDecl(Static(),VarDecl(Id("z"),ArrayType(10,ClassType(Id("B")))))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 312))

    def test_method_decl_01(self):
        input = """class A {
            int main() {}
        }"""
        expect = str(Program([ClassDecl(Id("A"), [MethodDecl(Instance(), Id("main"), [], IntType(), Block([], []))])]))
        self.assertTrue(TestAST.test(input, expect, 313))

    def test_method_decl_02(self):
        input = """class A {
            A() {}
        }"""
        expect = str(Program([ClassDecl(Id("A"), [MethodDecl(Instance(), Id("<init>"), [], None, Block([], []))])]))
        self.assertTrue(TestAST.test(input, expect, 314))

    def test_method_decl_03(self):
        input = """class A {
            static float foo() {}
            string foo() {}
            foo() {}
        }"""
        expect = str(Program([ClassDecl(Id("A"), [
            MethodDecl(Static(), Id("foo"), [], FloatType(), Block([], [])),
            MethodDecl(Instance(), Id("foo"), [], StringType(), Block([], [])),
            MethodDecl(Instance(), Id("<init>"), [], None, Block([], []))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 315))

    def test_method_decl_04(self):
        input = """class A {
            int[5] getArray(int a,v; float c) {}
        }"""
        expect = str(Program([ClassDecl(Id("A"), [
            MethodDecl(Instance(),Id("getArray"),[
                VarDecl(Id("a"),IntType()),
                VarDecl(Id("v"),IntType()),
                VarDecl(Id("c"),FloatType())
            ], ArrayType(5, IntType()), Block([], []))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 316))

    def test_method_decl_05(self):
        input = """class A {
            static A B (A a) {}
            A(int a,b) {}
            A() {}
        }"""
        expect = str(Program([ClassDecl(Id("A"), [
            MethodDecl(Static(), Id("B"), [VarDecl(Id("a"), ClassType(Id("A")))], ClassType(Id("A")), Block([], [])),
            MethodDecl(Instance(),Id("<init>"),[
                VarDecl(Id("a"),IntType()),
                VarDecl(Id("b"), IntType())], None, Block([], [])),
            MethodDecl(Instance(), Id("<init>"), [], None, Block([], []))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 317))

    def test_method_decl_06(self):
        input = """class A {
            A() {
            }
            A(int a; float b; string c; boolean d) {}
        }"""
        expect = str(Program([ClassDecl(Id("A"), [
            MethodDecl(Instance(),Id("<init>"),[],None,Block([],[])),
            MethodDecl(Instance(),Id("<init>"),[
                VarDecl(Id("a"),IntType()),
                VarDecl(Id("b"),FloatType()),
                VarDecl(Id("c"),StringType()),
                VarDecl(Id("d"),BoolType())
            ],None,Block([],[]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 318))

    def test_method_decl_07(self):
        input = """class B extends A {
            B(A a,b; B c; A[2] z) {}
        }"""
        expect = str(Program([ClassDecl(Id("B"),[
            MethodDecl(Instance(),Id("<init>"),[
                VarDecl(Id("a"),ClassType(Id("A"))),
                VarDecl(Id("b"),ClassType(Id("A"))),
                VarDecl(Id("c"),ClassType(Id("B"))),
                VarDecl(Id("z"),ArrayType(2,ClassType(Id("A"))))
            ],None,Block([],[]))
        ],Id("A"))]))
        self.assertTrue(TestAST.test(input, expect, 319))
    
    #=======================================#
    #               320 - 329               #
    #=======================================#
    def test_method_decl_08(self):
        input = """class A {
            static A getA() {}
        }
        class B extends A {
            static A getA(int a) {}
        }"""
        expect = str(Program([ClassDecl(Id("A"), [MethodDecl(Static(),Id("getA"),[],ClassType(Id("A")),Block([],[]))]),
                              ClassDecl(Id("B"), [MethodDecl(Static(),Id("getA"),[VarDecl(Id("a"),IntType())],ClassType(Id("A")),Block([], []))],Id("A"))]))
        self.assertTrue(TestAST.test(input, expect, 320))

    def test_method_decl_09(self):
        input = """
        class A {
            A() {}
            static int getNum(int[5] a; A[5] a) {}
        }
        class Story extends test {
            void main(){}
        }"""
        expect = str(Program([
            ClassDecl(Id("A"), [
                MethodDecl(Instance(),Id("<init>"),[],None,Block([],[])),
                MethodDecl(Static(),Id("getNum"),[
                    VarDecl(Id("a"),ArrayType(5,IntType())),
                    VarDecl(Id("a"),ArrayType(5,ClassType(Id("A"))))
                ],IntType(),Block([],[]))
            ]),
            ClassDecl(Id("Story"),[
                MethodDecl(Instance(),Id("main"),[],VoidType(),Block([],[]))
            ],Id("test"))]))
        self.assertTrue(TestAST.test(input, expect, 321))

    def test_mix_decl_01(self):
        input = """class A {
            final int x = 2;
            int main() {}
        }"""
        expect = str(Program([ClassDecl(Id("A"), [
            AttributeDecl(Instance(),ConstDecl(Id("x"),IntType(),IntLiteral(2))),
            MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 323))

    def test_mix_decl_02(self):
        input = """class A {
            final int x = 2;
            int main() {}
            static float y;
        }"""
        expect = str(Program([ClassDecl(Id("A"), [
            AttributeDecl(Instance(),ConstDecl(Id("x"),IntType(),IntLiteral(2))),
            MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[])),
            AttributeDecl(Static(),VarDecl(Id("y"),FloatType()))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 322))

    def test_mix_decl_03(self):
        input = """class A {
            int main() {}
            static float x;
            static void main() {}
        }"""
        expect = str(Program([ClassDecl(Id("A"), [
            MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[])),
            AttributeDecl(Static(),VarDecl(Id("x"),FloatType())),
            MethodDecl(Static(),Id("main"),[],VoidType(),Block([],[]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 324))

    def test_mix_decl_04(self):
        input = """class A {
            int a;
            A() {}
            float c;
            A(int f) {}
        }"""
        expect = str(Program([ClassDecl(Id("A"), [
            AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),
            MethodDecl(Instance(),Id("<init>"),[],None,Block([],[])),
            AttributeDecl(Instance(),VarDecl(Id("c"),FloatType())),
            MethodDecl(Instance(), Id("<init>"), [VarDecl(
                Id("f"), IntType())], None, Block([], []))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 325))

    def test_mix_decl_05(self):
        input = """class A {
            A() {}
            static final int z = 4;
            static int A() {}
        }"""
        expect = str(Program([ClassDecl(Id("A"), [
            MethodDecl(Instance(),Id("<init>"),[],None,Block([],[])),
            AttributeDecl(Static(),ConstDecl(Id("z"),IntType(),IntLiteral(4))),
            MethodDecl(Static(),Id("A"),[],IntType(),Block([],[]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 326))

    def test_mix_decl_06(self):
        input = """class A {
            int a, b;
            final static float c = 2.0e-123;
            int main() {}
            static void checkFloat(float f) {}
        }"""
        expect = str(Program([ClassDecl(Id("A"), [
            AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),
            AttributeDecl(Instance(),VarDecl(Id("b"),IntType())),
            AttributeDecl(Static(),ConstDecl(Id("c"),FloatType(),FloatLiteral(2.0e-123))),
            MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[])),
            MethodDecl(Static(),Id("checkFloat"),[VarDecl(Id("f"),FloatType())],VoidType(),Block([],[]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 327))

    def test_mix_decl_07(self):
        input = """class A {
            int a;
            final static string[2] c = {"abc","def"};
            int main() {}
            int b;
            static void checkFloat(float f,d; int z) {}
            static final float c = 1.001;
        }"""
        expect = str(Program([ClassDecl(Id("A"), [
            AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),
            AttributeDecl(Static(),ConstDecl(Id("c"),ArrayType(2,StringType()),ArrayLiteral([
                StringLiteral('''"abc"'''),
                StringLiteral('''"def"''')
            ]))),
            MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[])),
            AttributeDecl(Instance(),VarDecl(Id("b"),IntType())),
            MethodDecl(Static(),Id("checkFloat"),[
                VarDecl(Id("f"),FloatType()),
                VarDecl(Id("d"),FloatType()),
                VarDecl(Id("z"),IntType())
            ],VoidType(),Block([],[])),
            AttributeDecl(Static(),ConstDecl(Id("c"),FloatType(),FloatLiteral(1.001)))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 328))

    def test_mix_decl_08(self):
        input = """class e {
            e() {}
            void main() {}
        }
        class childe extends e {
            static int count;
            childe() {}
            int main() {}
        }"""
        expect = str(Program([
            ClassDecl(Id("e"), [
                MethodDecl(Instance(),Id("<init>"),[],None,Block([],[])),
                MethodDecl(Instance(),Id("main"),[],VoidType(),Block([],[]))
            ]),
            ClassDecl(Id("childe"),[
                AttributeDecl(Static(),VarDecl(Id("count"),IntType())),
                MethodDecl(Instance(),Id("<init>"),[],None,Block([],[])),
                MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[]))
            ],Id("e"))]))
        self.assertTrue(TestAST.test(input, expect, 329))
    
    #=======================================#
    #               330 - 339               #
    #=======================================#
    def test_exp0_1(self):
        input = """class A {
            # test exp
            boolean a0 = 9 < 10;
            boolean a1 = 9 <= 10;
            boolean a2 = 9 > 10;
            boolean a3 = 9 >= 10;
            # test exp1
            boolean a4 = 9 == 10;
            boolean a5 = 9 != 10;
        }"""
        expect = str(Program([ClassDecl(Id("A"), [
            AttributeDecl(Instance(),VarDecl(Id("a0"),BoolType(),BinaryOp("<",IntLiteral(9),IntLiteral(10)))),
            AttributeDecl(Instance(),VarDecl(Id("a1"),BoolType(),BinaryOp("<=",IntLiteral(9),IntLiteral(10)))),
            AttributeDecl(Instance(),VarDecl(Id("a2"),BoolType(),BinaryOp(">",IntLiteral(9),IntLiteral(10)))),
            AttributeDecl(Instance(),VarDecl(Id("a3"),BoolType(),BinaryOp(">=",IntLiteral(9),IntLiteral(10)))),
            AttributeDecl(Instance(),VarDecl(Id("a4"),BoolType(),BinaryOp("==",IntLiteral(9),IntLiteral(10)))),
            AttributeDecl(Instance(),VarDecl(Id("a5"),BoolType(),BinaryOp("!=",IntLiteral(9),IntLiteral(10)))),
        ])]))
        self.assertTrue(TestAST.test(input, expect, 330))

    def test_exp2_3(self):
        input = """class A {
            # test exp2
            boolean a0 = true && false;
            boolean a1 = true || false;
            # test exp3
            int a2 = 9 + 10;
            int a3 = 9 - 10;
        }"""
        expect = str(Program([ClassDecl(Id("A"), [
            AttributeDecl(Instance(),VarDecl(Id("a0"),BoolType(),BinaryOp("&&",BooleanLiteral(True),BooleanLiteral(False)))),
            AttributeDecl(Instance(),VarDecl(Id("a1"),BoolType(),BinaryOp("||",BooleanLiteral(True),BooleanLiteral(False)))),
            AttributeDecl(Instance(),VarDecl(Id("a2"),IntType(),BinaryOp("+",IntLiteral(9),IntLiteral(10)))),
            AttributeDecl(Instance(),VarDecl(Id("a3"),IntType(),BinaryOp("-",IntLiteral(9),IntLiteral(10))))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 331))

    def test_exp4_5(self):
        input = """class A {
            # test exp4
            int   a0 = 9 * 10;
            float a1 = 9.001 / 10;
            int   a2 = 9 \\ 10;
            int   a3 = 9 % 10;
            # test exp5
            string s = "abc " ^ "zzz";
        }"""
        expect = str(Program([ClassDecl(Id("A"), [
            AttributeDecl(Instance(),VarDecl(Id("a0"),IntType(),BinaryOp("*",IntLiteral(9),IntLiteral(10)))),
            AttributeDecl(Instance(),VarDecl(Id("a1"),FloatType(),BinaryOp("/",FloatLiteral(9.001),IntLiteral(10)))),
            AttributeDecl(Instance(),VarDecl(Id("a2"),IntType(),BinaryOp("\\",IntLiteral(9),IntLiteral(10)))),
            AttributeDecl(Instance(),VarDecl(Id("a3"),IntType(),BinaryOp("%",IntLiteral(9),IntLiteral(10)))),
            AttributeDecl(Instance(),VarDecl(Id("s"),StringType(),BinaryOp("^",StringLiteral('''"abc "'''),StringLiteral('''"zzz"'''))))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 332))

    def test_exp6_7(self):
        input = """class A {
            # test exp6
            boolean a0 = !a, a1 = !!!a;
            # test exp7
            int a2 = -9, a3 = +(1 - 2);
        }"""
        expect = str(Program([ClassDecl(Id("A"), [
            AttributeDecl(Instance(),VarDecl(Id("a0"),BoolType(),UnaryOp("!",Id("a")))),
            AttributeDecl(Instance(),VarDecl(Id("a1"),BoolType(),UnaryOp("!",UnaryOp("!",UnaryOp("!",Id("a")))))),
            AttributeDecl(Instance(),VarDecl(Id("a2"),IntType(),UnaryOp("-",IntLiteral(9)))),
            AttributeDecl(Instance(),VarDecl(Id("a3"),IntType(),UnaryOp("+",BinaryOp("-",IntLiteral(1),IntLiteral(2)))))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 333))

    def test_exp8_10(self):
        input = """class A {
            # test exp8
            int a = b[2];
            float c = b[a + 5];
            # test exp10
            B obj = new B();
            B _obj = new B(1,a);
        }"""
        expect = str(Program([ClassDecl(Id("A"), [
            AttributeDecl(Instance(),VarDecl(Id("a"),IntType(),ArrayCell(Id("b"),IntLiteral(2)))),
            AttributeDecl(Instance(),VarDecl(Id("c"),FloatType(),ArrayCell(Id("b"),BinaryOp("+",Id("a"),IntLiteral(5))))),
            AttributeDecl(Instance(),VarDecl(Id("obj"),ClassType(Id("B")),NewExpr(Id("B"),[]))),
            AttributeDecl(Instance(),VarDecl(Id("_obj"),ClassType(Id("B")),NewExpr(Id("B"),[IntLiteral(1),Id("a")])))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 334))

    def test_exp9(self):
        input = """class A {
            int a0 = b.get();
            int a1 = b.data;
            int a2 = a.b.data;
            int a3 = a.b.get(a0);
        }"""
        expect = str(Program([ClassDecl(Id("A"), [
            AttributeDecl(Instance(),VarDecl(Id("a0"),IntType(),CallExpr(Id("b"),Id("get"),[]))),
            AttributeDecl(Instance(),VarDecl(Id("a1"),IntType(),FieldAccess(Id("b"),Id("data")))),
            AttributeDecl(Instance(),VarDecl(Id("a2"),IntType(),FieldAccess(FieldAccess(Id("a"),Id("b")),Id("data")))),
            AttributeDecl(Instance(),VarDecl(Id("a3"),IntType(),CallExpr(FieldAccess(Id("a"),Id("b")),Id("get"),[Id("a0")])))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 335))

    def test_mix_exp_01(self):
        input = """class A {
            int a = z + c/d;
            int z = bfs.check() + (a - e)[2];
        }"""
        expect = str(Program([ClassDecl(Id("A"), [
            AttributeDecl(Instance(),VarDecl(Id("a"),IntType(),BinaryOp("+",Id("z"),BinaryOp("/",Id("c"),Id("d"))))),
            AttributeDecl(Instance(),VarDecl(Id("z"),IntType(),BinaryOp("+",CallExpr(Id("bfs"),Id("check"),[]),ArrayCell(BinaryOp("-",Id("a"),Id("e")),IntLiteral(2)))))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 336))

    def test_mix_exp_02(self):
        input = """class A {
            boolean z = !(!a && b || f) && !((a == z[3]) >= e);
        }"""
        expect = str(Program([ClassDecl(Id("A"), [
            AttributeDecl(Instance(),VarDecl(Id("z"),BoolType(),
                BinaryOp("&&",
                    UnaryOp("!",
                        BinaryOp("||",
                            BinaryOp("&&",
                                UnaryOp("!",Id("a")),
                                Id("b")),
                            Id("f"))),
                    UnaryOp("!",
                    BinaryOp(">=",
                        BinaryOp("==",
                            Id("a"),
                            ArrayCell(Id("z"),IntLiteral(3))),
                        Id("e"))))
            ))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 337))

    def test_mix_exp_03(self):
        input = """class A {
            int f = a.get()[a.dot - a] + (a * 2 - f).get()[b.a.d(b.get() - 1)];
        }"""
        expect = str(Program([ClassDecl(Id("A"), [
            AttributeDecl(Instance(),VarDecl(Id("f"),IntType(),
            BinaryOp("+",
                ArrayCell(
                    CallExpr(Id("a"),Id("get"),[]),
                    BinaryOp("-",FieldAccess(Id("a"),Id("dot")),Id("a"))),
                ArrayCell(
                    CallExpr(
                        BinaryOp("-",BinaryOp("*",Id("a"),IntLiteral(2)),Id("f")),
                        Id("get"), []),
                    CallExpr(
                        FieldAccess(Id("b"),Id("a")),
                        Id("d"),
                        [BinaryOp("-",CallExpr(Id("b"),Id("get"),[]),IntLiteral(1))]))
            )))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 338))

    def test_mix_exp_04(self):
        input = """class A {
            boolean b = (-(a * d) > (a.get() \\ f % m)) && !(f != a.c) || a;
        }"""
        expect = str(Program([ClassDecl(Id("A"), [
            AttributeDecl(Instance(),VarDecl(Id("b"),BoolType(),
            BinaryOp("||",
                BinaryOp("&&",
                    BinaryOp(">",
                        UnaryOp("-",
                            BinaryOp("*",
                                Id("a"),
                                Id("d"))),
                        BinaryOp("%",
                            BinaryOp("\\",
                                CallExpr(Id("a"),Id("get"),[]),
                                Id("f")),
                            Id("m"))),
                    UnaryOp("!",
                        BinaryOp("!=",
                            Id("f"),
                            FieldAccess(Id("a"),Id("c"))))),
                Id("a"))
            ))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 339))
    
    #=======================================#
    #               340 - 349               #
    #=======================================#
    def test_vardecl_block_01(self):
        input = """class A {
            int main() {
                int a = 2,b;
                final A f = new A();
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"),[
            MethodDecl(Instance(),Id("main"),[],IntType(),Block([
                VarDecl(Id("a"),IntType(),IntLiteral(2)),
                VarDecl(Id("b"),IntType()),
                ConstDecl(Id("f"),ClassType(Id("A")),NewExpr(Id("A"),[]))
            ],[]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 340))

    def test_vardecl_block_02(self):
        input = """class A {
            int main() {
                float[2] a = {1.01, 2.0E+123};
                A[5] f;
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"),[
            MethodDecl(Instance(),Id("main"),[],IntType(),Block([
                VarDecl(Id("a"),ArrayType(2,FloatType()),ArrayLiteral([FloatLiteral(1.01),FloatLiteral(2.0E+123)])),
                VarDecl(Id("f"), ArrayType(5,ClassType(Id("A")))),
            ],[]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 341))
    
    def test_return_01(self):
        input = """class A {
            int main() {
                int a;
                return a;
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"), [
            MethodDecl(Instance(),Id("main"),[],IntType(),Block(
                [VarDecl(Id("a"),IntType())],
                [Return(Id("a"))]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 342))
    
    def test_return_02(self):
        input = """class A {
            int main() {
                return new Obj(a, n).f();
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"), [
            MethodDecl(Instance(),Id("main"),[],IntType(),Block(
                [],
                [Return(CallExpr(NewExpr(Id("Obj"),[Id("a"),Id("n")]),Id("f"),[]))]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 343))
    
    def test_return_03(self):
        input = """class A {
            int main() {
                return a^(a ^ B);
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"), [
            MethodDecl(Instance(),Id("main"),[],IntType(),Block(
                [],
                [Return(BinaryOp("^",Id("a"),BinaryOp("^",Id("a"),Id("B"))))]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 344))

    def test_assign_01(self):
        input = """class A {
            int main() {
                int a;
                a := 2;
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"), [
            MethodDecl(Instance(),Id("main"),[],IntType(),Block(
                [VarDecl(Id("a"),IntType())],
                [Assign(Id("a"),IntLiteral(2))]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 345))

    def test_assign_02(self):
        input = """class A {
            int main() {
                a[2] := a[1];
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"), [
            MethodDecl(Instance(),Id("main"),[],IntType(),Block(
                [],
                [Assign(ArrayCell(Id("a"),IntLiteral(2)),ArrayCell(Id("a"),IntLiteral(1)))]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 346))

    def test_assign_03(self):
        input = """class A {
            int main() {
                a.f := {1, 2, 3};
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"), [
            MethodDecl(Instance(),Id("main"),[],IntType(),Block(
                [],
                [Assign(FieldAccess(Id("a"),Id("f")),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]))]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 347))

    def test_assign_04(self):
        input = """class A {
            int main() {
                (a + f).m := "abv";
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"), [
            MethodDecl(Instance(),Id("main"),[],IntType(),Block(
                [],
                [Assign(FieldAccess(BinaryOp("+",Id("a"),Id("f")),Id("m")),StringLiteral('''"abv"'''))]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 348))
    
    def test_assign_05(self):
        input = """class A {
            int main() {
                A a;
                a := nil;
                value := this.M;
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"), [
            MethodDecl(Instance(),Id("main"),[],IntType(),Block(
                [VarDecl(Id("a"),ClassType(Id("A")))],
                [Assign(Id("a"),NullLiteral()), Assign(Id("value"),FieldAccess(SelfLiteral(),Id("M")))]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 349))
    
    #=======================================#
    #               350 - 359               #
    #=======================================#
    def test_meth_invo_01(self):
        input = """class A {
            int main() {
                this.function();
                a.function();
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"),[
            MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[
                CallStmt(SelfLiteral(),Id("function"),[]),
                CallStmt(Id("a"),Id("function"),[])
            ]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 350))

    def test_meth_invo_02(self):
        input = """class A {
            int main() {
                this.checkData(a, this.v);
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"),[
            MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[
                CallStmt(SelfLiteral(),Id("checkData"),[Id("a"),FieldAccess(SelfLiteral(),Id("v"))]),
            ]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 351))
    
    def test_meth_invo_03(self):
        input = """class A {
            int main() {
                (this.f + e).check();
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"),[
            MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[
                CallStmt(BinaryOp("+",FieldAccess(SelfLiteral(),Id("f")),Id("e")),Id("check"),[]),
            ]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 352))
    
    def test_meth_invo_04(self):
        input = """class A {
            int main() {
                (data != nil).callFunction(a, nil, c, this);
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"),[
            MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[
                CallStmt(BinaryOp("!=",Id("data"),NullLiteral()),Id("callFunction"),[Id("a"),NullLiteral(),Id("c"),SelfLiteral()]),
            ]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 353))
    
    def test_if_01(self):
        input = """class A {
            int main() {
                if a == b then a:=1;
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"),[
            MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[
                If(BinaryOp("==",Id("a"),Id("b")),Assign(Id("a"),IntLiteral(1)))
            ]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 354))

    def test_if_02(self):
        input = """class A {
            int main() {
                if a == b then a:=1;
                else a := 2;
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"),[
            MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[
                If(BinaryOp("==",Id("a"),Id("b")),Assign(Id("a"),IntLiteral(1)),Assign(Id("a"),IntLiteral(2)))
            ]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 355))

    def test_if_03(self):
        input = """class A {
            int main() {
                if a==3 then
                    if b == 3 then
                        return 3;
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"),[
            MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[
                If(BinaryOp("==",Id("a"),IntLiteral(3)),If(BinaryOp("==",Id("b"),IntLiteral(3)),Return(IntLiteral(3))))
            ]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 356))

    def test_if_04(self):
        input = """class A {
            int main() {
                if a==3 then
                    if b == 3 then
                        return 3;
                    else return 2;
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"),[
            MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[
                If(BinaryOp("==",Id("a"),IntLiteral(3)),If(BinaryOp("==",Id("b"),IntLiteral(3)),Return(IntLiteral(3)),Return(IntLiteral(2))))
            ]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 357))

    def test_if_05(self):
        input = """class A {
            int main() {
                if a==3 then
                    if b == 3 then
                        return 3;
                    else return 2;
                else return 1;
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"),[
            MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[
                If(BinaryOp("==",Id("a"),IntLiteral(3)),If(BinaryOp("==",Id("b"),IntLiteral(3)),Return(IntLiteral(3)),Return(IntLiteral(2))),Return(IntLiteral(1)))
            ]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 358))
    
    def test_if_06(self):
        input = """class A {
            int main() {
                if a then return b;
                if c then if d then if f then return g;
                else return h;
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"),[
            MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[
                If(Id("a"),Return(Id("b"))),
                If(Id("c"),If(Id("d"),If(Id("f"),Return(Id("g")),Return(Id("h")))))
            ]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 359))
    
    #=======================================#
    #               360 - 369               #
    #=======================================#
    def test_if_07(self):
        input = """class A {
            int main() {
                if c then if d then if f then return g;
                else return h;
                else return k;
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"),[
            MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[
                If(Id("c"),If(Id("d"),If(Id("f"),Return(Id("g")),Return(Id("h"))),Return(Id("k"))))
            ]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 360))

    def test_if_08(self):
        input = """class A {
            int main() {
                if c then if d then if f then return g;
                else return h;
                else return k;
                else return j;
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"),[
            MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[
                If(Id("c"),If(Id("d"),If(Id("f"),Return(Id("g")),Return(Id("h"))),Return(Id("k"))),Return(Id("j")))
            ]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 361))

    def test_if_09(self):
        input = """class A {
            int main() {
                if a then {
                    if b then return b;
                }
                else a := 2;
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"),[
            MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[
                If(Id("a"),Block([],[If(Id("b"),Return(Id("b")))]),Assign(Id("a"),IntLiteral(2)))
            ]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 362))

    def test_for_01(self):
        input = """class A {
            int main() {
                for i := 1 to 2 do a:=1;
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"),[
            MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[
                For(Id("i"),IntLiteral(1),IntLiteral(2),True,Assign(Id("a"),IntLiteral(1)))
            ]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 363))

    def test_for_02(self):
        input = """class A {
            int main() {
                for i := 1 downto 2 do a:=1;
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"),[
            MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[
                For(Id("i"),IntLiteral(1),IntLiteral(2),False,Assign(Id("a"),IntLiteral(1)))
            ]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 364))

    def test_for_03(self):
        input = """class A {
            int main() {
                for i := a.get(value) to 1-f.a+22 do
                    if i > a then return this;
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"),[
            MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[
                For(Id("i"),
                    CallExpr(Id("a"),Id("get"),[Id("value")]),
                    BinaryOp("+",BinaryOp("-",IntLiteral(1),FieldAccess(Id("f"),Id("a"))),IntLiteral(22)),
                    True,
                    If(BinaryOp(">",Id("i"),Id("a")),Return(SelfLiteral())))
            ]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 365))

    def test_for_04(self):
        input = """class A {
            int main() {
                for i := a.get(value) downto 1-f.a+22 do
                    if i > a then return this;
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"),[
            MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[
                For(Id("i"),
                    CallExpr(Id("a"),Id("get"),[Id("value")]),
                    BinaryOp("+",BinaryOp("-",IntLiteral(1),FieldAccess(Id("f"),Id("a"))),IntLiteral(22)),
                    False,
                    If(BinaryOp(">",Id("i"),Id("a")),Return(SelfLiteral())))
            ]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 366))

    def test_for_05(self):
        input = """class A {
            int main() {
                for i := 0 to 10 do
                    for j := 10 downto 0 do
                        a[i] := b[j];
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"),[
            MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[
                For(Id("i"),IntLiteral(0),IntLiteral(10),True,
                    For(Id("j"),IntLiteral(10),IntLiteral(0),False,
                        Assign(
                            ArrayCell(Id("a"),Id("i")),
                            ArrayCell(Id("b"),Id("j")))))
            ]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 367))

    def test_for_06(self):
        input = """class A {
            int main() {
                for i := 10 downto 0 do
                    for j := 0 to 10 do
                        a[i] := b[j];
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"),[
            MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[
                For(Id("i"),IntLiteral(10),IntLiteral(0),False,
                    For(Id("j"),IntLiteral(0),IntLiteral(10),True,
                        Assign(
                            ArrayCell(Id("a"),Id("i")),
                            ArrayCell(Id("b"),Id("j")))))
            ]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 368))

    def test_for_07(self):
        input = """class A {
            int main() {
                for i := a to b do
                    a := a + i;
                for i := a downto b do
                    a := a - i;
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"),[
            MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[
                For(Id("i"),Id("a"),Id("b"),True,Assign(Id("a"),BinaryOp("+",Id("a"),Id("i")))),
                For(Id("i"),Id("a"),Id("b"),False,Assign(Id("a"),BinaryOp("-",Id("a"),Id("i"))))
            ]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 369))
    
    #=======================================#
    #               370 - 379               #
    #=======================================#
    def test_for_08(self):
        input = """class A {
            int main() {
                for i := a downto b do
                    a := a + i;
                for i := a to b do
                    a := a - i;
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"),[
            MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[
                For(Id("i"),Id("a"),Id("b"),False,Assign(Id("a"),BinaryOp("+",Id("a"),Id("i")))),
                For(Id("i"),Id("a"),Id("b"),True,Assign(Id("a"),BinaryOp("-",Id("a"),Id("i"))))
            ]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 370))

    def test_for_09(self):
        input = """class A {
            int main() {
                for i := 0 to 10 do {
                    if i == f then
                        return i;
                    else f := !f;
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"),[
            MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[
                For(Id("i"),IntLiteral(0),IntLiteral(10),True,
                    Block([], [If(BinaryOp("==", Id("i"), Id("f")),Return(Id("i")), Assign(Id("f"),UnaryOp("!", Id("f"))))]))
            ]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 371))
    
    def test_block_01(self):
        input = """class A {
            int main() {
                final int a = 2;
                float b;
                b := a/2;
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"), [
            MethodDecl(Instance(),Id("main"),[],IntType(),Block([
                ConstDecl(Id("a"),IntType(),IntLiteral(2)),
                VarDecl(Id("b"),FloatType())
            ],[
                Assign(Id("b"),BinaryOp("/",Id("a"),IntLiteral(2)))
            ]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 372))
    
    def test_block_02(self):
        input = """class A {
            int main() {
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"), [
            MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 373))
    
    def test_block_03(self):
        input = """class A {
            int main() {
                {return a;}
                {return b;}
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"), [
            MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[
                Block([],[Return(Id("a"))]),
                Block([],[Return(Id("b"))])
            ]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 374))

    def test_block_04(self):
        input = """class A {
            int main() {
                if a.check() then {
                    a := f;
                    return a / 2;
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"), [
            MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[
                If(CallExpr(Id("a"),Id("check"),[]),Block([],[Assign(Id("a"),Id("f")),Return(BinaryOp("/",Id("a"),IntLiteral(2)))]))
            ]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 375))

    def test_block_05(self):
        input = """class A {
            int main() {
                if a.check() then {
                    a := f;
                    return a / 2;
                }
                else {
                    return a;
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"), [
            MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[
                If(CallExpr(Id("a"),Id("check"),[]),
                    Block([],[Assign(Id("a"),Id("f")),Return(BinaryOp("/",Id("a"),IntLiteral(2)))]),
                    Block([],[Return(Id("a"))]))
            ]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 376))

    def test_block_06(self):
        input = """class A {
            int main() {
                if a != b then {
                    if a then {
                        b := this.test(a,b);
                        return b + a;
                    }
                    else return !a;
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"), [
            MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[
                If(BinaryOp("!=",Id("a"),Id("b")),Block([],[
                    If(Id("a"),Block([],[
                        Assign(Id("b"),CallExpr(SelfLiteral(),Id("test"),[Id("a"),Id("b")])),
                        Return(BinaryOp("+",Id("b"),Id("a")))
                    ]),Return(UnaryOp("!",Id("a"))))
                ]))
            ]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 377))

    def test_block_07(self):
        input = """class A {
            int main() {
                for i := 1 to 10 do {
                    string f;
                    f.get();
                    str := str ^ f;
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"), [
            MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[
                For(Id("i"),IntLiteral(1),IntLiteral(10),True,
                    Block([VarDecl(Id("f"),StringType())],[
                        CallStmt(Id("f"),Id("get"),[]),
                        Assign(Id("str"),BinaryOp("^",Id("str"),Id("f")))
                    ]))
            ]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 378))
    
    def test_block_08(self):
        input = """class A {
            int main() {
                for i := 10 downto n do {
                    string f;
                    f.get();
                    str := str ^ f;
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"), [
            MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[
                For(Id("i"),IntLiteral(10),Id("n"),False,
                    Block([VarDecl(Id("f"),StringType())],[
                        CallStmt(Id("f"),Id("get"),[]),
                        Assign(Id("str"),BinaryOp("^",Id("str"),Id("f")))
                    ]))
            ]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 379))
    
    #=======================================#
    #               380 - 389               #
    #=======================================#
    def test_block_09(self):
        input = """class A {
            int main() {
                int c,l;
                int min,max;
                min := this.get();
                max := this.get();
                for i := min to max do {
                    if i > 0 then {
                        if i % 2 == 0 then c := c + i;
                        else l := l + i;
                    }
                    else {
                        i := 0;
                        c := 0;
                        l := 0;
                    }
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"), [
            MethodDecl(Instance(),Id("main"),[],IntType(),Block([
                VarDecl(Id("c"),IntType()),VarDecl(Id("l"),IntType()),VarDecl(Id("min"),IntType()),VarDecl(Id("max"),IntType())
            ],[
                Assign(Id("min"),CallExpr(SelfLiteral(),Id("get"),[])),
                Assign(Id("max"),CallExpr(SelfLiteral(),Id("get"),[])),
                For(Id("i"),Id("min"),Id("max"),True,Block([],[
                    If(
                        BinaryOp(">",Id("i"),IntLiteral(0)), 
                        Block([],[
                            If(BinaryOp("==",BinaryOp("%",Id("i"),IntLiteral(2)),IntLiteral(0)),
                                Assign(Id("c"),BinaryOp("+",Id("c"),Id("i"))),
                                Assign(Id("l"),BinaryOp("+",Id("l"),Id("i"))))
                            ]),
                        Block([],[
                        Assign(Id("i"),IntLiteral(0)),
                        Assign(Id("c"),IntLiteral(0)),
                        Assign(Id("l"),IntLiteral(0))
                    ]))
                ]))
            ]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 380))

    def test_break_01(self):
        input = """class A {
            int main() {
                for i := 1 to 2 do {
                    if i > n then break;
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"),[
            MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[
                For(Id("i"),IntLiteral(1),IntLiteral(2),True,Block([],[
                    If(BinaryOp(">",Id("i"),Id("n")),Break())
                ]))
            ]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 381))

    def test_break_02(self):
        input = """class A {
            int main() {
                for i := 1 to 2 do {
                    if i > n then break;
                    else {
                        n := i;
                        if n > f then break;
                    }
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"),[
            MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[
                For(Id("i"),IntLiteral(1),IntLiteral(2),True,Block([],[
                    If(BinaryOp(">",Id("i"),Id("n")),Break(),Block([],[
                        Assign(Id("n"),Id("i")),
                        If(BinaryOp(">",Id("n"),Id("f")),Break())
                    ]))
                ]))
            ]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 382))

    def test_continue_01(self):
        input = """class A {
            int main() {
                for i := 1 to 2 do {
                    if i > n then continue;
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"),[
            MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[
                For(Id("i"),IntLiteral(1),IntLiteral(2),True,Block([],[
                    If(BinaryOp(">",Id("i"),Id("n")),Continue())
                ]))
            ]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 383))

    def test_continue_02(self):
        input = """class A {
            int main() {
                for i := 1 to 2 do {
                    if i > n then continue;
                    else {
                        n := i;
                        if n > f then continue;
                    }
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"),[
            MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[
                For(Id("i"),IntLiteral(1),IntLiteral(2),True,Block([],[
                    If(BinaryOp(">",Id("i"),Id("n")),Continue(),Block([],[
                        Assign(Id("n"),Id("i")),
                        If(BinaryOp(">",Id("n"),Id("f")),Continue())
                    ]))
                ]))
            ]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 384))

    def test_mix_break_continue_01(self):
        input = """class A {
            int main() {
                for i := 1 to 2 do {
                    if i > n then continue;
                    else {
                        n := i;
                        if n > f then break;
                    }
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"),[
            MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[
                For(Id("i"),IntLiteral(1),IntLiteral(2),True,Block([],[
                    If(BinaryOp(">",Id("i"),Id("n")),Continue(),Block([],[
                        Assign(Id("n"),Id("i")),
                        If(BinaryOp(">",Id("n"),Id("f")),Break())
                    ]))
                ]))
            ]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 385))

    def test_mix_break_continue_02(self):
        input = """class A {
            int main(int input) {
                int x = -1, y;
                for i := 0 to arr.size() do {
                    for j := 0 to this.len(arr.get(i)) do {
                        if arr.get(i)[j] == -2 then continue;
                        if arr.get(i)[j] == input then {
                            x := i;
                            y := j;
                            break;
                        }
                    }
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"),[
            MethodDecl(Instance(),Id("main"),[VarDecl(Id("input"),IntType())],IntType(),Block([
                VarDecl(Id("x"),IntType(),UnaryOp("-",IntLiteral(1))),
                VarDecl(Id("y"),IntType())
            ],[
                For(Id("i"),IntLiteral(0),CallExpr(Id("arr"),Id("size"),[]),True,Block([],[
                    For(Id("j"),IntLiteral(0),CallExpr(SelfLiteral(),Id("len"),[CallExpr(Id("arr"),Id("get"),[Id("i")])]),True,Block([],[
                        If(BinaryOp("==",ArrayCell(CallExpr(Id("arr"),Id("get"),[Id("i")]),Id("j")),UnaryOp("-",IntLiteral(2))),Continue()),
                        If(BinaryOp("==",ArrayCell(CallExpr(Id("arr"),Id("get"),[Id("i")]),Id("j")),Id("input")),Block([],[
                            Assign(Id("x"),Id("i")),
                            Assign(Id("y"),Id("j")),
                            Break()
                        ]))
                    ]))
                ]))
            ]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 386))

    def test_mix_break_continue_03(self):
        input = """class A {
            int main(int input) {
                int x = -1, y;
                for i := 0 to arr.size() do {
                    for j := 0 to this.len(arr.get(i)) do {
                        if arr.get(i)[j] == -2 then continue;
                        if arr.get(i)[j] == input then {
                            x := i;
                            y := j;
                            break;
                        }
                    }
                    if x != -1 then break;
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"),[
            MethodDecl(Instance(),Id("main"),[VarDecl(Id("input"),IntType())],IntType(),Block([
                VarDecl(Id("x"),IntType(),UnaryOp("-",IntLiteral(1))),
                VarDecl(Id("y"),IntType())
            ],[
                For(Id("i"),IntLiteral(0),CallExpr(Id("arr"),Id("size"),[]),True,Block([],[
                    For(Id("j"),IntLiteral(0),CallExpr(SelfLiteral(),Id("len"),[CallExpr(Id("arr"),Id("get"),[Id("i")])]),True,Block([],[
                        If(BinaryOp("==",ArrayCell(CallExpr(Id("arr"),Id("get"),[Id("i")]),Id("j")),UnaryOp("-",IntLiteral(2))),Continue()),
                        If(BinaryOp("==",ArrayCell(CallExpr(Id("arr"),Id("get"),[Id("i")]),Id("j")),Id("input")),Block([],[
                            Assign(Id("x"),Id("i")),
                            Assign(Id("y"),Id("j")),
                            Break()
                        ]))
                    ])),
                    If(BinaryOp("!=",Id("x"),UnaryOp("-",IntLiteral(1))),Break())
                ]))
            ]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 387))

    def test_mix_break_continue_04(self):
        input = """class A {
            int main(int input) {
                int x = -1, y;
                for i := 0 to arr.size() do {
                    if arr.get(i) == nil then continue;
                    for j := 0 to this.len(arr.get(i)) do {
                        if arr.get(i)[j] == -2 then continue;
                        if arr.get(i)[j] == input then {
                            x := i;
                            y := j;
                            break;
                        }
                    }
                    if x != -1 then break;
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"),[
            MethodDecl(Instance(),Id("main"),[VarDecl(Id("input"),IntType())],IntType(),Block([
                VarDecl(Id("x"),IntType(),UnaryOp("-",IntLiteral(1))),
                VarDecl(Id("y"),IntType())
            ],[
                For(Id("i"),IntLiteral(0),CallExpr(Id("arr"),Id("size"),[]),True,Block([],[
                    If(BinaryOp("==",CallExpr(Id("arr"),Id("get"),[Id("i")]),NullLiteral()),Continue()),
                    For(Id("j"),IntLiteral(0),CallExpr(SelfLiteral(),Id("len"),[CallExpr(Id("arr"),Id("get"),[Id("i")])]),True,Block([],[
                        If(BinaryOp("==",ArrayCell(CallExpr(Id("arr"),Id("get"),[Id("i")]),Id("j")),UnaryOp("-",IntLiteral(2))),Continue()),
                        If(BinaryOp("==",ArrayCell(CallExpr(Id("arr"),Id("get"),[Id("i")]),Id("j")),Id("input")),Block([],[
                            Assign(Id("x"),Id("i")),
                            Assign(Id("y"),Id("j")),
                            Break()
                        ]))
                    ])),
                    If(BinaryOp("!=",Id("x"),UnaryOp("-",IntLiteral(1))),Break())
                ]))
            ]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 388))

    def test_mix_01(self):
        input = """class A {
            int main(int input) {
                int x = -1, y;
                for i := 0 to arr.size() do {
                    if arr.get(i) == nil then continue;
                    for j := 0 to this.len(arr.get(i)) do {
                        if arr.get(i)[j] == -2 then continue;
                        if arr.get(i)[j] == input then {
                            x := i;
                            y := j;
                            break;
                        }
                    }
                    if x != -1 then break;
                }
                if x != -1 then return arr.get(x)[y];
                else return -1;
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"),[
            MethodDecl(Instance(),Id("main"),[VarDecl(Id("input"),IntType())],IntType(),Block([
                VarDecl(Id("x"),IntType(),UnaryOp("-",IntLiteral(1))),
                VarDecl(Id("y"),IntType())
            ],[
                For(Id("i"),IntLiteral(0),CallExpr(Id("arr"),Id("size"),[]),True,Block([],[
                    If(BinaryOp("==",CallExpr(Id("arr"),Id("get"),[Id("i")]),NullLiteral()),Continue()),
                    For(Id("j"),IntLiteral(0),CallExpr(SelfLiteral(),Id("len"),[CallExpr(Id("arr"),Id("get"),[Id("i")])]),True,Block([],[
                        If(BinaryOp("==",ArrayCell(CallExpr(Id("arr"),Id("get"),[Id("i")]),Id("j")),UnaryOp("-",IntLiteral(2))),Continue()),
                        If(BinaryOp("==",ArrayCell(CallExpr(Id("arr"),Id("get"),[Id("i")]),Id("j")),Id("input")),Block([],[
                            Assign(Id("x"),Id("i")),
                            Assign(Id("y"),Id("j")),
                            Break()
                        ]))
                    ])),
                    If(BinaryOp("!=",Id("x"),UnaryOp("-",IntLiteral(1))),Break())
                ])),
                If(
                    BinaryOp("!=",Id("x"),UnaryOp("-",IntLiteral(1))),
                    Return(ArrayCell(CallExpr(Id("arr"),Id("get"),[Id("x")]),Id("y"))),
                    Return(UnaryOp("-",IntLiteral(1))))
            ]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 389))
    
    #=======================================#
    #               390 - 399               #
    #=======================================#
    def test_mix_02(self):
        input = """class A {
            void main() {
                int[5] arr;
                for i := 0 to 5 do {
                    int v;
                    v := os.get("int");
                    if v <= 0 then {
                        os.print("Error!!");
                        break;
                    }
                    arr[i] := v;
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"), [
            MethodDecl(Instance(),Id("main"),[],VoidType(),Block([
                VarDecl(Id("arr"),ArrayType(5,IntType()))
            ],[
                For(Id("i"),IntLiteral(0),IntLiteral(5),True,Block([VarDecl(Id("v"),IntType())],[
                    Assign(Id("v"),CallExpr(Id("os"),Id("get"),[StringLiteral('''"int"''')])),
                    If(BinaryOp("<=",Id("v"),IntLiteral(0)),Block([],[
                        CallStmt(Id("os"),Id("print"),[StringLiteral('''"Error!!"''')]),
                        Break()
                    ])),
                    Assign(ArrayCell(Id("arr"),Id("i")),Id("v"))
                ]))
            ]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 390))

    def test_mix_03(self):
        input = """class A {
            int sum(int[5] arr) {
                int s = 0;
                for i := 0 to 5 do
                    s := s + arr[i];
                return s;
            }
            void main() {
                int[5] arr;
                for i := 0 to 5 do {
                    int v;
                    v := os.get("int");
                    if v <= 0 then {
                        os.print("Error!!");
                        break;
                    }
                    arr[i] := v;
                }
                os.print(this.sum(arr));
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"), [
            MethodDecl(Instance(),Id("sum"),[VarDecl(Id("arr"),ArrayType(5,IntType()))],IntType(),Block([
                VarDecl(Id("s"),IntType(),IntLiteral(0))
                ],[
                For(Id("i"),IntLiteral(0),IntLiteral(5),True,Assign(Id("s"),BinaryOp("+",Id("s"),ArrayCell(Id("arr"),Id("i"))))),
                Return(Id("s"))
            ])),
            MethodDecl(Instance(),Id("main"),[],VoidType(),Block([VarDecl(Id("arr"),ArrayType(5,IntType()))],[
                For(Id("i"),IntLiteral(0),IntLiteral(5),True,Block([VarDecl(Id("v"),IntType())],[
                    Assign(Id("v"),CallExpr(Id("os"),Id("get"),[StringLiteral('''"int"''')])),
                    If(BinaryOp("<=",Id("v"),IntLiteral(0)),Block([],[
                        CallStmt(Id("os"),Id("print"),[StringLiteral('''"Error!!"''')]),
                        Break()
                    ])),
                    Assign(ArrayCell(Id("arr"),Id("i")),Id("v"))
                ])),
                CallStmt(Id("os"),Id("print"),[CallExpr(SelfLiteral(),Id("sum"),[Id("arr")])])
            ]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 391))

    def test_mix_04(self):
        input = """class A {
            static A instance;
            A() {
                if instance == nil then
                    instance := this;
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"), [
            AttributeDecl(Static(),VarDecl(Id("instance"),ClassType(Id("A")))),
            MethodDecl(Instance(),Id("<init>"),[],None,Block([],[If(BinaryOp("==",Id("instance"),NullLiteral()),Assign(Id("instance"),SelfLiteral()))]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 392))

    def test_mix_05(self):
        input = """class A {
            static A instance;
            A() {
                if instance == nil then
                    instance := this;
            }
            Text txt;
            static void Display(string str) {
                txt.text := str;
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"), [
            AttributeDecl(Static(),VarDecl(Id("instance"),ClassType(Id("A")))),
            MethodDecl(Instance(),Id("<init>"),[],None,Block([],[If(BinaryOp("==",Id("instance"),NullLiteral()),Assign(Id("instance"),SelfLiteral()))])),
            AttributeDecl(Instance(),VarDecl(Id("txt"),ClassType(Id("Text")))),
            MethodDecl(Static(),Id("Display"),[VarDecl(Id("str"),StringType())],VoidType(),Block([],[Assign(FieldAccess(Id("txt"),Id("text")),Id("str"))]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 393))

    def test_mix_06(self):
        input = """
        class makeSchool {
            void main() {
                for i:=true downto z-1 do {
                    string new_class;
                    io.fflush(stdin);
                    io.getline(new_class);
                    if new_class != "-1" then
                        School.updateClass(new_class);
                    else break;
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("makeSchool"),[
            MethodDecl(Instance(),Id("main"),[],VoidType(),Block([],[
                For(Id("i"),BooleanLiteral(True),BinaryOp("-",Id("z"),IntLiteral(1)),False,Block([
                    VarDecl(Id("new_class"),StringType())],
                [
                    CallStmt(Id("io"),Id("fflush"),[Id("stdin")]),
                    CallStmt(Id("io"),Id("getline"),[Id("new_class")]),
                    If(BinaryOp("!=",Id("new_class"),StringLiteral('''"-1"''')),
                        CallStmt(Id("School"),Id("updateClass"),[Id("new_class")]),Break())
                ]))
            ]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 394))

    def test_mix_07(self):
        input = """class mainFuncion {
            void insert (int index; node root, n) {
                if index == 0 then {
                    n.setNext(root.getNext());
                    root.setNext(n);
                }
                else
                    array.insert();
            }
        }"""
        expect = str(Program([ClassDecl(Id("mainFuncion"), [
            MethodDecl(Instance(),Id("insert"),[
                VarDecl(Id("index"),IntType()),
                VarDecl(Id("root"),ClassType(Id("node"))),
                VarDecl(Id("n"),ClassType(Id("node")))
                ],VoidType(),Block([],[
                    If(BinaryOp("==",Id("index"),IntLiteral(0)),
                        Block([],[
                            CallStmt(Id("n"),Id("setNext"),[CallExpr(Id("root"),Id("getNext"),[])]),
                            CallStmt(Id("root"),Id("setNext"),[Id("n")])]),
                        CallStmt(Id("array"),Id("insert"),[]))
                ]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 395))

    def test_mix_08(self):
        input = """
        class mainFuncion {
            void insert (int index; node root, n) {
                if index == 0 then {
                    n.setNext(root.getNext());
                    root.setNext(n);
                }
                else
                    array.insert(index - 1, root.getNext(), n);
            }
        }"""
        expect = str(Program([ClassDecl(Id("mainFuncion"), [
            MethodDecl(Instance(),Id("insert"),[
                VarDecl(Id("index"),IntType()),
                VarDecl(Id("root"),ClassType(Id("node"))),
                VarDecl(Id("n"),ClassType(Id("node")))
                ],VoidType(),Block([],[
                    If(BinaryOp("==",Id("index"),IntLiteral(0)),
                        Block([],[
                            CallStmt(Id("n"),Id("setNext"),[CallExpr(Id("root"),Id("getNext"),[])]),
                            CallStmt(Id("root"),Id("setNext"),[Id("n")])]),
                        CallStmt(Id("array"),Id("insert"),[
                            BinaryOp("-",Id("index"),IntLiteral(1)),
                            CallExpr(Id("root"),Id("getNext"),[]),
                            Id("n")
                        ]))
                ]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 396))

    def test_mix_09(self):
        input = """
        class A {}
        class B extends A {}
        class mainStream {
            void main() {
                A[5] a;
                for i:=0 to 5 do {
                    int v;
                    v := os.random() % 2;
                    if v then a[i] := new A();
                    else a[i] := new B();
                }
            }
        }"""
        expect = str(Program([
            ClassDecl(Id("A"), []),
            ClassDecl(Id("B"),[],Id("A")),
            ClassDecl(Id("mainStream"),[
                MethodDecl(Instance(),Id("main"),[],VoidType(),Block([
                    VarDecl(Id("a"),ArrayType(5,ClassType(Id("A"))))
                ],[
                    For(Id("i"),IntLiteral(0),IntLiteral(5),True,Block([VarDecl(Id("v"),IntType())],[
                        Assign(Id("v"),BinaryOp("%",CallExpr(Id("os"),Id("random"),[]),IntLiteral(2))),
                        If(Id("v"),Assign(ArrayCell(Id("a"),Id("i")),NewExpr(Id("A"),[])),Assign(ArrayCell(Id("a"),Id("i")),NewExpr(Id("B"),[])))
                    ]))
                ]))
            ])]))
        self.assertTrue(TestAST.test(input, expect, 397))

    def test_mix_10(self):
        input = """
        class A {
            void check() {}
        }
        class B extends A {
            void check() {}
        }
        class mainStream {
            void main() {
                A[5] a;
                for i:=0 to 5 do {
                    int v;
                    v := os.random() % 2;
                    if v then a[i] := new A();
                    else a[i] := new B();
                }
                for i:=4 downto -1 do (a[i]).check();
            }
        }"""
        expect = str(Program([
            ClassDecl(Id("A"), [
                MethodDecl(Instance(),Id("check"),[],VoidType(),Block([],[]))
            ]),
            ClassDecl(Id("B"),[
                MethodDecl(Instance(),Id("check"),[],VoidType(),Block([],[]))
            ],Id("A")),
            ClassDecl(Id("mainStream"),[
                MethodDecl(Instance(),Id("main"),[],VoidType(),Block([
                    VarDecl(Id("a"),ArrayType(5,ClassType(Id("A"))))
                ],[
                    For(Id("i"),IntLiteral(0),IntLiteral(5),True,Block([VarDecl(Id("v"),IntType())],[
                        Assign(Id("v"),BinaryOp("%",CallExpr(Id("os"),Id("random"),[]),IntLiteral(2))),
                        If(Id("v"),Assign(ArrayCell(Id("a"),Id("i")),NewExpr(Id("A"),[])),Assign(ArrayCell(Id("a"),Id("i")),NewExpr(Id("B"),[])))
                    ])),
                    For(Id("i"),IntLiteral(4),UnaryOp("-",IntLiteral(1)),False,CallStmt(ArrayCell(Id("a"),Id("i")),Id("check"),[]))
                ]))
            ])]))
        self.assertTrue(TestAST.test(input, expect, 398))

    def test_mix_11(self):
        input = """
        class A {
            static int random() {
                return os.random() * os.random() \\ 2;
            }
            int check() {
                return this.random();
            }
        }
        class B extends A {
            int check() {
                return A.random() * A.random() \\ 2;
            }
        }
        class mainStream {
            void main() {
                A[5] a;
                int max = 0;
                for i:=0 to 5 do {
                    int v;
                    v := os.random() % 2;
                    if v then a[i] := new A();
                    else a[i] := new B();
                }
                for i:=4 downto -1 do {
                    int v = (a[i]).check();
                    if v > max then max := v;
                }
            }
        }"""
        expect = str(Program([
            ClassDecl(Id("A"), [
                MethodDecl(Static(),Id("random"),[],IntType(),Block([],[
                    Return(BinaryOp("\\",BinaryOp("*",CallExpr(Id("os"),Id("random"),[]),CallExpr(Id("os"),Id("random"),[])),IntLiteral(2)))
                ])),
                MethodDecl(Instance(),Id("check"),[],IntType(),Block([],[
                    Return(CallExpr(SelfLiteral(),Id("random"),[]))
                ]))
            ]),
            ClassDecl(Id("B"),[
                MethodDecl(Instance(),Id("check"),[],IntType(),Block([],[
                    Return(BinaryOp("\\",BinaryOp("*",CallExpr(Id("A"),Id("random"),[]),CallExpr(Id("A"),Id("random"),[])),IntLiteral(2)))
                ]))
            ],Id("A")),
            ClassDecl(Id("mainStream"),[
                MethodDecl(Instance(),Id("main"),[],VoidType(),Block([
                    VarDecl(Id("a"),ArrayType(5,ClassType(Id("A")))),
                    VarDecl(Id("max"),IntType(),IntLiteral(0))
                ],[
                    For(Id("i"),IntLiteral(0),IntLiteral(5),True,Block([VarDecl(Id("v"),IntType())],[
                        Assign(Id("v"),BinaryOp("%",CallExpr(Id("os"),Id("random"),[]),IntLiteral(2))),
                        If(Id("v"),Assign(ArrayCell(Id("a"),Id("i")),NewExpr(Id("A"),[])),Assign(ArrayCell(Id("a"),Id("i")),NewExpr(Id("B"),[])))
                    ])),
                    For(Id("i"),IntLiteral(4),UnaryOp("-",IntLiteral(1)),False,Block([
                        VarDecl(Id("v"),IntType(),CallExpr(ArrayCell(Id("a"),Id("i")),Id("check"),[]))
                    ],[
                        If(BinaryOp(">",Id("v"),Id("max")),Assign(Id("max"),Id("v")))
                    ]))
                ]))
            ])]))
        self.assertTrue(TestAST.test(input, expect, 399))
   
