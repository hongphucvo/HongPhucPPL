import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: class main {} """
        input = """class main {}"""
        expect = str(Program([ClassDecl(Id("main"),[])]))
        self.assertTrue(TestAST.test(input,expect,300))
    
    def test_class_with_one_decl_program(self):
        """More complex program"""
        input = """class main {
            int a;
        }"""
        expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(Instance(),VarDecl(Id("a"),IntType()))])]))
        self.assertTrue(TestAST.test(input,expect,301))
    
    def test_class_with_two_decl_program(self):
        """More complex program"""
        input = """class main {
            int a;
            int b;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),
             AttributeDecl(Instance(),VarDecl(Id("b"),IntType()))])]))
        self.assertTrue(TestAST.test(input,expect,302))
    def test_simple_program(self):
        """Simple program: 1 stm """
        input = """class A{int main(){}}"""
        expect = str(Program([ClassDecl(Id(A),[MethodDecl(Id(main("<init>")),Static,[],IntType,Block([],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 311))
    def test_simple_test1(self):
        input = """class A{int main(){
        int b;
        {int a;}
  return 0;}
}"""
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 312))
    def test_simple_test2(self):
        input = """class A{int main(){
  float number, root;
  {}
  }
}"""
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 313))
    def test_simple_test3(self):
        input = """class A{
int main(){
{}float number = 7.0, root=2.3;}
}"""
        expect = ""
        self.assertTrue(TestAST.test(input, expect, 314))
    def test_simple_test4(self):
        input = """class A{int main(){
 float number=9.0; int root;}
}"""
        expect = ""
        self.assertTrue(TestAST.test(input, expect, 315))
    def test_simple_test5(self):
        input = """class A{static int main(){
float number=7.3, root;}
}"""
        expect = ""
        self.assertTrue(TestAST.test(input, expect, 316))
    def test_simple_test6(self):
        input = """class A{int main(){
  final float number = root;
  this.root:=5;}
}"""
        expect = ""
        self.assertTrue(TestAST.test(input, expect, 317))
    def test_simple_test7(self):
        input = """class A{int main(){
  io.writeFloat(root);}
}"""
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 318))
    def test_simple_test8(self):
        input = """class A{int main(){
  io.writeFloat(7*9-10);}
}"""
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 319))
    def test_simple_test9(self):
        input = """class A{int main(){
        #This is a line cmt
}}"""
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 210))
