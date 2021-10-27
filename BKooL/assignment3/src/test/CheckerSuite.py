import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
 #   '''
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
    
    def test_io(self):
        input = "class io{int x;}"
        expect = "Redeclared Class: io"
        self.assertTrue(TestChecker.test(input,expect,426))
    def test_extend_io(self):
        input = "class m extends io{int x;}"
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,427))
    
    def test_io_med(self):
        input = "class m{int x(){io.writeInt(9);}}"
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,428))
    def test_io_param(self):
        input = "class m{int x(){io.writeInt(9.3);}}"
        expect = "Type Mismatch In Statement: Call(Id(io),Id(writeInt),[FloatLit(9.3)])"
        self.assertTrue(TestChecker.test(input,expect,429))
        
    def test_io_param_1(self):
        input = "class m{int x(){int a=io.readInt();}}"
        expect =""
        self.assertTrue(TestChecker.test(input,expect,430))
    def test_io_2(self):
        input = "class m{int x(){io.writeStr(\"123456\");}}"
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,431))
    
    def test_return0(self):
        input = """class A{
    int main(){
    int b;
    {int a;}
    return 0.5;
    }
}"""
        expect = "Type Mismatch In Statement: Return(FloatLit(0.5))"
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_return_1(self):
        input = "class m{int x(){if True then return 1.3;}}"
        expect = "Undeclared Identifier: True"
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_return_2(self):
        input = "class m{int x(){if true then {return 1.3;}}}"
        expect = "Type Mismatch In Statement: Return(FloatLit(1.3))"
        self.assertTrue(TestChecker.test(input,expect,434))
    
    def test_return_3(self):
        input = "class m{int x(){io.writeStr(\"123456\");}}"
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_empty_block(self):
        input = """class A{
        int main(){
          float number, root;
          {}
          }
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,436))
    def test_const_ill(self):
        input = """class A{int main(){
  final float number = root;
  this.root:=5;}
}"""
        expect = "Undeclared Identifier: root"
        self.assertTrue(TestChecker.test(input,expect,437))
    def test_io_expr(self):
        input = """class A{int main(){  io.writeFloat(7*9-10);}}"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,438))
    def test_dup_att(self):
        input = """class School{int id;}
        class Faculty { int id;}"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,439))
    def test_att_method_inner(self):
        input = """class School{        int id;        void print(){io.writeInt(this.id);}}"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,440))
    def test_method_decl(self):
        input = """class School{
        int id;
        void print(){io.writeInt(this.id);}
        int go(int a,b;float d){
            io.writeInt(0);
        }
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,441))
    def test_io_call(self):
        input = """class School{
        int id;
        void print(){io.writeInt(5+7-9/88);}}
        class Faculty{int id;
        void Faculty(){
            this.id:=1911881;
        }}
        """
        expect = "Type Mismatch In Statement: Call(Id(io),Id(writeInt),[BinaryOp(-,BinaryOp(+,IntLit(5),IntLit(7)),BinaryOp(/,IntLit(9),IntLit(88)))])"
        self.assertTrue(TestChecker.test(input,expect,442))
    def test_extend_io_int(self):
        input = """class m extends io{int x(){
            this.writeInt(1.3);
        }}"""
        expect = "Type Mismatch In Statement: Call(Self(),Id(writeInt),[FloatLit(1.3)])"
        self.assertTrue(TestChecker.test(input,expect,443))
    def test_extend_io_int_1(self):
        input = """class m extends io{int x(){
            this.writeInt(0);
        }}"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,444))
  
    def test_class_decl_0(self):
        input = """class School{
        static int id;
        void print(){
        int a=100;
        io.writeInt(a);}
        }
        class Faculty extends School{
            void print(){
                io.writeInt(1);
            }
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,445))
    def test_expr_0(self):
        input = """class A{int main(){
            int a = (1234+9857-(6574*(8754-87/3\\1)));}
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(\,BinaryOp(/,IntLit(87),IntLit(3)),IntLit(1))"
        self.assertTrue(TestChecker.test(input,expect,446))
    def test_expr_1(self):
        input = """class X{
        int[2]m;
         void X(){
         m:={1,2};}}"""
        expect = "Undeclared Identifier: m"
        self.assertTrue(TestChecker.test(input,expect,447))
    def test_expr_2(self):
        input = """class X{
            void k(){io.writeInt(1+4-e);}
            X(){}}"""
        expect = "Undeclared Identifier: e"
        self.assertTrue(TestChecker.test(input,expect,448))
    
    def test_expr_3(self):
        input = """class X{
                int main(){
                boolean _=true||false;
                int a=+1-5;
                boolean  e= _;
                }
                }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,449))
    #'''
    def test_t02(self):
        input = """class X{
            int k;
            boolean lessthan(X source){
                if this.k<source.k then return true;
                else if this.k==source.k then return false;
                else return false;
            }
            }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,450))
    def test_t03(self):
        input = """class X{
            int k;
            boolean notequal(X source){
                if this.k==source.k+1 then return false;
                else return true;
            }
            }"""
    
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,451))
    def test_t04(self):
        input = """class X{
            int k;
            boolean mod2(X source){
                if (this.k%2==0 )&&(source.k%2==0) then return true;
                else return false;
            }
            }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,452))
    '''def test_io_2(self):
        input = "class m{int x(){io.writeStr(\"123456\");}}"
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,431))
    def test_io_2(self):
        input = "class m{int x(){io.writeStr(\"123456\");}}"
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,431))
    def test_io_2(self):
        input = "class m{int x(){io.writeStr(\"123456\");}}"
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,431))
    def test_io_2(self):
        input = "class m{int x(){io.writeStr(\"123456\");}}"
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,431))
    def test_io_2(self):
        input = "class m{int x(){io.writeStr(\"123456\");}}"
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,431))
    def test_io_2(self):
        input = "class m{int x(){io.writeStr(\"123456\");}}"
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,431))
    def test_io_2(self):
        input = "class m{int x(){io.writeStr(\"123456\");}}"
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,431))
    def test_io_2(self):
        input = "class m{int x(){io.writeStr(\"123456\");}}"
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,431))
    def test_io_2(self):
        input = "class m{int x(){io.writeStr(\"123456\");}}"
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,431))
    def test_io_2(self):
        input = "class m{int x(){io.writeStr(\"123456\");}}"
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,431))
    def test_io_2(self):
        input = "class m{int x(){io.writeStr(\"123456\");}}"
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,431))
    def test_io_2(self):
        input = "class m{int x(){io.writeStr(\"123456\");}}"
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,431))
    def test_io_2(self):
        input = "class m{int x(){io.writeStr(\"123456\");}}"
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,431))
    def test_io_2(self):
        input = "class m{int x(){io.writeStr(\"123456\");}}"
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,431))
    def test_io_2(self):
        input = "class m{int x(){io.writeStr(\"123456\");}}"
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,431))
    def test_io_2(self):
        input = "class m{int x(){io.writeStr(\"123456\");}}"
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,431))
    def test_io_2(self):
        input = "class m{int x(){io.writeStr(\"123456\");}}"
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,431))
    def test_io_2(self):
        input = "class m{int x(){io.writeStr(\"123456\");}}"
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,431))
    def test_io_2(self):
        input = "class m{int x(){io.writeStr(\"123456\");}}"
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,431))
    def test_io_2(self):
        input = "class m{int x(){io.writeStr(\"123456\");}}"
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,431))
    def test_io_2(self):
        input = "class m{int x(){io.writeStr(\"123456\");}}"
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,431))
    def test_io_2(self):
        input = "class m{int x(){io.writeStr(\"123456\");}}"
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,431))
    def test_io_2(self):
        input = "class m{int x(){io.writeStr(\"123456\");}}"
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,431))
    def test_io_2(self):
        input = "class m{int x(){io.writeStr(\"123456\");}}"
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,431))
    def test_io_2(self):
        input = "class m{int x(){io.writeStr(\"123456\");}}"
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,431))
    def test_io_2(self):
        input = "class m{int x(){io.writeStr(\"123456\");}}"
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,431))
    def test_io_2(self):
        input = "class m{int x(){io.writeStr(\"123456\");}}"
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,431))
    def test_io_2(self):
        input = "class m{int x(){io.writeStr(\"123456\");}}"
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,431))
    def test_io_2(self):
        input = "class m{int x(){io.writeStr(\"123456\");}}"
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,431))
    def test_io_2(self):
        input = "class m{int x(){io.writeStr(\"123456\");}}"
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,431))
    def test_io_2(self):
        input = "class m{int x(){io.writeStr(\"123456\");}}"
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,431))
    def test_io_2(self):
        input = "class m{int x(){io.writeStr(\"123456\");}}"
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,431))
    def test_io_2(self):
        input = "class m{int x(){io.writeStr(\"123456\");}}"
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,431))
    def test_io_2(self):
        input = "class m{int x(){io.writeStr(\"123456\");}}"
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,431))
    def test_io_2(self):
        input = "class m{int x(){io.writeStr(\"123456\");}}"
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,431))
    def test_io_2(self):
        input = "class m{int x(){io.writeStr(\"123456\");}}"
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,431))
    def test_io_2(self):
        input = "class m{int x(){io.writeStr(\"123456\");}}"
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,431))
    def test_io_2(self):
        input = "class m{int x(){io.writeStr(\"123456\");}}"
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,431))
    def test_io_2(self):
        input = "class m{int x(){io.writeStr(\"123456\");}}"
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,431))
    def test_io_2(self):
        input = "class m{int x(){io.writeStr(\"123456\");}}"
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,431))
    def test_io_2(self):
        input = "class m{int x(){io.writeStr(\"123456\");}}"
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,431))
    def test_io_2(self):
        input = "class m{int x(){io.writeStr(\"123456\");}}"
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,431))
    def test_io_2(self):
        input = "class m{int x(){io.writeStr(\"123456\");}}"
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,431))
    def test_io_2(self):
        input = "class m{int x(){io.writeStr(\"123456\");}}"
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,431))
    def test_io_2(self):
        input = "class m{int x(){io.writeStr(\"123456\");}}"
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,431))
    def test_io_2(self):
        input = "class m{int x(){io.writeStr(\"123456\");}}"
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,431))
    '''






























