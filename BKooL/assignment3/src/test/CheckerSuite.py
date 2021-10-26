import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
  
    def test_un_parent(self):
        input = Program([ClassDecl(Id("a"),[],Id("b"))])
        expect = "Undeclared Class: b"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_re_class(self):
        input = """class m {
            int a;
        }
        class m{int x;}
        """
        expect = "Redeclared Class: m"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_re_att(self):
        input = """class m {
            int a;
            int a;
        }
        """
        expect = "Redeclared Attribute: a"
        self.assertTrue(TestChecker.test(input,expect,402))
#TODO: test re att const
    
    def test_re_class1(self):
        input = """class m {
            int a;
        }
        class m{final int v;}
        class e{static int x;}"""
        expect = "Redeclared Class: m"
        self.assertTrue(TestChecker.test(input,expect,403))
   
    def test_break(self):
        input = "class A{int x(){break;}}"
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,404))
 
    def test_break(self):
        input = "class A{int x(){for i:=5 to 10 do {} break;}}"
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,405))
        
    def test_con(self):
        input = "class A{int x(){for i:=5 downto 10 do {} continue;}}"
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,406))
       
    def test_re_param(self):
        input = "class A{int x(int k,k){}}"
        expect = "Redeclared Parameter: k"
        self.assertTrue(TestChecker.test(input,expect,407))
    
    def test_re_method(self):
        input = "class A{int x(int k){return 5;} int x(){return 5;}}"
        expect = "Redeclared Method: x"
        self.assertTrue(TestChecker.test(input,expect,408))
    
    def test_wrong_attri(self):
        input = "class A{int x=5.0;}"
        expect = "Type Mismatch In Statement: VarDecl(Id(x),IntType,FloatLit(5.0))"
        self.assertTrue(TestChecker.test(input,expect,409))
    
    def test_wrong_attri1(self):
        input = "class A{string x=1;}"
        expect = "Type Mismatch In Statement: VarDecl(Id(x),StringType,IntLit(1))"
        self.assertTrue(TestChecker.test(input,expect,410))
    
    def test_wrong_var(self):
        input = """class A{int x(){ int a=\"5\";return 5;}}"""
        expect = "Type Mismatch In Statement: VarDecl(Id(a),IntType,StringLit(\"5\"))"
        self.assertTrue(TestChecker.test(input,expect,411))
    
    def test_wrong_return(self):
        input = """class A{int x(){ int a=5;return 5.2;}}"""
        expect = "Type Mismatch In Statement: Return(FloatLit(5.2))"
        self.assertTrue(TestChecker.test(input,expect,412))
    def test_wrong_assign_fi(self):
        input = """class A{int x(){ int a=5;a:=2.1;}}"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),FloatLit(2.1))"
        self.assertTrue(TestChecker.test(input,expect,413))
    
    def test_wrong_exp_sf(self):
        input = """class A{int x(){ int a=5;a:=2.1+"";}}"""
        expect = "Type Mismatch In Expression: BinaryOp(+,FloatLit(2.1),StringLit(\"\"))"
        self.assertTrue(TestChecker.test(input,expect,414))
     
    def test_undecl(self):
        input = "class A{int x(){ int m; m:=k;}}"
        expect = "Undeclared Identifier: k"
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_wrong_for(self):
        input = "class A{int x(){ int m;for a:=4.5 to 10 do {int x;}}}"
        expect = "Type Mismatch In Statement: a:=FloatLit(4.5)"
        self.assertTrue(TestChecker.test(input,expect,416))
    
    def test_wrong_array(self):
        input = "class A{int x(){ int[1] m={4.0};}}"
        expect = "Type Mismatch In Statement: VarDecl(Id(m),ArrayType(1,IntType),[FloatLit(4.0)])"
        self.assertTrue(TestChecker.test(input,expect,417))
    
    
    def test_wrong_arrayindex(self):
        input = "class A{int x(){ int[1] m={4.0};}}"
        expect = "Type Mismatch In Statement: VarDecl(Id(m),ArrayType(1,IntType),[FloatLit(4.0)])"
        self.assertTrue(TestChecker.test(input,expect,417))
    
    def test_wrong_field_acc(self):
        input = """class A{
            int k;
            int x(int e)
            {  A temp;
                temp.m:=5;
            }
            }"""
        expect = "Illegal Member Access: FieldAccess(Id(temp),Id(m))"
        self.assertTrue(TestChecker.test(input,expect,418))
    
    def test_right_field_par(self):
        input = """
        class X{int m;}
        class A extends X{
            int k;
            int x(int e)
            {  A temp;
                temp.m:=5;
            }
            }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,419))
    
    def test_wrong_cell(self):
        input = """
        class A {
            int[1] k;
            int x()
            {  this.k[2]:=2.5;
            }
            }"""
        expect = "Type Mismatch In Statement: AssignStmt(ArrayCell(FieldAccess(Self(),Id(k)),IntLit(2)),FloatLit(2.5))"
        self.assertTrue(TestChecker.test(input,expect,420))
    
    def test_wrong_call_void(self):
        input = """
        class A {
            int[1] k;
            int y(){int a=5;}
            int x()
            {  this.y();
            }

            }"""
        expect = "Type Mismatch In Statement: Call(Self(),Id(y),[])"
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_right_call_(self):
        input = """
        class A {
            int[1] k;
            void y(int b){int a=5;}
            int x()
            {  this.y(10);
            }

            }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,422))
    def test_wrong_call_para(self):
        input = """
        class A {
            int[1] k;
            void y(int b){int a=5;}
            int x()
            {  this.y(10.5);
            }

            }"""
        expect = "Type Mismatch In Statement: Call(Self(),Id(y),[FloatLit(10.5)])"
        self.assertTrue(TestChecker.test(input,expect,423))
    def test_var_as_class(self):
        input = """
        class A {
            int A;}"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,424))
    def test_ill_const(self):
        input = Program([ClassDecl(Id("Ex"),[AttributeDecl(Static(),VarDecl(Id("a"),IntType())),AttributeDecl(Instance(),ConstDecl(Id("x"),IntType(),FieldAccess(Id("Ex"),Id("a"))))])])
        expect = "Illegal Constant Expression: FieldAccess(Id(Ex),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,425))




#testwith class io






































