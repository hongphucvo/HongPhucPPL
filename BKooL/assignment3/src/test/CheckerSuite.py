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
    













































