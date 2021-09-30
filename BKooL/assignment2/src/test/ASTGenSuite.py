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
        expect = '''Program([ClassDecl(Id(A),[MethodDecl(Id(main(<init>)),Static,[],IntType,Block([],[]))])])'''
        self.assertTrue(TestAST.test(input, expect, 303))
    
    
    
    def test_simple_test1(self):
        input = """class A{
        int main(){
        int b;
        {int a;}
        return 0;}
}"""
        expect = '''Program([ClassDecl(Id(A),[MethodDecl(Id(main(<init>)),Static,[],IntType,Block([VarDecl(Id("b"),IntType())],[Block([VarDecl(Id("a"),IntType())],[]),Return(IntLit(0))]))])])'''
        self.assertTrue(TestAST.test(input, expect, 304))
    def test_simple_test2(self):
        input = """class A{int main(){
  float number, root;
  {}
  }
}"""
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 305))
    def test_simple_test3(self):
        input = """class A{
    int main(){
    float number = 7.0, root=2.3;
    {}}
}"""
        expect = ""
        self.assertTrue(TestAST.test(input, expect, 306))
    def test_simple_test4(self):
        input = """class A{int main(){
 float number=9.0; int root;}
}"""
        expect = ""
        self.assertTrue(TestAST.test(input, expect, 307))
    def test_simple_test5(self):
        input = """class A{static int main(){
float number=7.3, root;}
}"""
        expect = ""
        self.assertTrue(TestAST.test(input, expect, 308))
    def test_simple_test6(self):
        input = """class A{int main(){
  final float number = root;
  this.root:=5;}
}"""
        expect = ""
        self.assertTrue(TestAST.test(input, expect, 309))
    '''def test_simple_test7(self):
        input = """class A{int main(){
  io.writeFloat(root);}
}"""
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 310))
    
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
        self.assertTrue(TestAST.test(input, expect, 310))'''
    def test_class_dcl1(self):
        """only class declaration"""
        input = """class School{ int longitude,latitude;}"""
        expect = """Program([ClassDecl(Id(School),[AttributeDecl(Instance,VarDecl(Id(longitude),IntType)),AttributeDecl(Instance,VarDecl(Id(latitude),IntType))])])"""
        self.assertTrue(TestAST.test(input, expect, 311))
    def test_class_dcl2(self):
        input = """class School{ int longitude,latitude;}"""
        expect = """Program([ClassDecl(Id(School),[AttributeDecl(Instance,VarDecl(Id(longitude),IntType)),AttributeDecl(Instance,VarDecl(Id(latitude),IntType))])])"""
        self.assertTrue(TestAST.test(input, expect, 312))
    def test_class_dcl3(self):
        input = """class School{int id;}
        class Faculty { int id;}"""
        expect = """Program([ClassDecl(Id(School),[AttributeDecl(Instance,VarDecl(Id(id),IntType))]),ClassDecl(Id(Faculty),[AttributeDecl(Instance,VarDecl(Id(id),IntType))])])"""
        self.assertTrue(TestAST.test(input, expect, 313))
    def test_class_dcl4(self):
        input = """class School{
        int id;
        void print(){io.writeInt(this.id);}}"""
        expect = """Program([ClassDecl(Id(School),[AttributeDecl(Instance,VarDecl(Id(id),IntType)),MethodDecl(Id(print),Instance,[],VoidType,Block([],[Call(Id(io),Id(writeInt),[FieldAccess(Self(),Id(id))])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 314))
    def test_class_dcl5(self):
        input = """class School{
        int id;
        void print(){io.writeInt(this.id);}}"""
        expect = """Program([ClassDecl(Id(School),[AttributeDecl(Instance,VarDecl(Id(id),IntType)),MethodDecl(Id(print),Instance,[],VoidType,Block([],[Call(Id(io),Id(writeInt),[FieldAccess(Self(),Id(id))])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 315))
    def test_class_dcl6(self):
        input = """class School{
        int id;
        void print(){io.writeInt(this.id);}}
        class Faculty{int id;}
        """
        expect = """Program([ClassDecl(Id(School),[AttributeDecl(Instance,VarDecl(Id(id),IntType)),MethodDecl(Id(print),Instance,[],VoidType,Block([],[Call(Id(io),Id(writeInt),[FieldAccess(Self(),Id(id))])]))]),ClassDecl(Id(Faculty),[AttributeDecl(Instance,VarDecl(Id(id),IntType))])])"""
        self.assertTrue(TestAST.test(input, expect, 316))
    def test_class_dcl7(self):
        input = """class School{
        int id;
        void print(){}}
        class Faculty{int id;}"""
        expect = """Program([ClassDecl(Id(School),[AttributeDecl(Instance,VarDecl(Id(id),IntType)),MethodDecl(Id(print),Instance,[],VoidType,Block([],[]))]),ClassDecl(Id(Faculty),[AttributeDecl(Instance,VarDecl(Id(id),IntType))])])"""
        self.assertTrue(TestAST.test(input, expect, 317))
    def test_class_dcl8(self):
        input = """class School{
        int id;
        void print(){io.writeInt(this.id);}
        }
        class Faculty{int id; void main(){return 0;}}"""
        expect = """Program([ClassDecl(Id(School),[AttributeDecl(Instance,VarDecl(Id(id),IntType)),MethodDecl(Id(print),Instance,[],VoidType,Block([],[Call(Id(io),Id(writeInt),[FieldAccess(Self(),Id(id))])]))]),ClassDecl(Id(Faculty),[AttributeDecl(Instance,VarDecl(Id(id),IntType)),MethodDecl(Id(main(<init>)),Static,[],VoidType,Block([],[Return(IntLit(0))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 318))
    def test_class_dcl9(self):
        input = """class School{
        static int id;
        void print(){
        int a=100;
        io.writeInt(a);}
        }"""
        expect = "Error on line 4 col 8: static"
        self.assertTrue(TestAST.test(input, expect, 319))
    def test_class_dcl10(self):
        input = """class School{
        int _id;
        void print(){
        int a;
        io.writeInt(this.id);
        }
        }"""
        expect = "Error on line 5 col 8: int"
        self.assertTrue(TestAST.test(input, expect, 320))
