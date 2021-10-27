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
    
    def test_re_class1(self):
        input = """class m {
            int a;
        }
        class m{final int v;}
        class e{static int x;}"""
        expect = "Redeclared Class: m"
        self.assertTrue(TestChecker.test(input,expect,403))
   
    def test_break_hhh(self):
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
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),FloatLit(4.5))"
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
    def test_literal1(self):
        """StringLit and ArrayLit"""
        input = """class Lit{
        void main(){
        string A;
        A:=\"my name\";
        A:="This is a string containing tab \t";}}"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,453))
    def test_literal2(self):
        input = """class Lit{
        void main(){
        string A;
        A:="";
        A:=A+"HongPhuc";
        }}"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,454))
    def test_literal4(self):
        input = """class Lit{
            void main(){
                string A;
                int[2] b = {1.2,A};
                A:="The comment starts with #";
        
                A:={"A"};}}"""
        expect = "Illegal Array Literal: [FloatLit(1.2),Id(A)]"
        self.assertTrue(TestChecker.test(input,expect,455))
    def test_literal5(self):
        input = """class Lit{
        void main(){
        string A;
        string[1] A;
        A:="Open the string";
        A:={"A#cmt"};}}"""
        expect = "Redeclared Variable: A"
        self.assertTrue(TestChecker.test(input,expect,456))
    def test_literal6(self):
        input = """class Lit{
        void main(){
        int[2] A;
        A:={1.2,6};}}"""
        expect = "Illegal Array Literal: [FloatLit(1.2),IntLit(6)]"
        self.assertTrue(TestChecker.test(input,expect,457))
    def test_literal7(self):
        input = """class Lit{
            final int a = 3.5;
        void main(){
        string A;
        A:="This is a string containing tab \t";}}"""
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),IntType,FloatLit(3.5))"
        self.assertTrue(TestChecker.test(input,expect,458))
    def test_literal8(self):
        """wrong type"""
        input = """class Lit{
            final int a = 3.5;
            final static int a=10;
            static float m="1234";
        void main(){
        string A;
        A:="This is a string containing tab \t";}}"""
        expect = "Redeclared Constant: a"
        self.assertTrue(TestChecker.test(input,expect,459))
    def test_literal9(self):
        """wrong type"""
        input = """class Lit{
            final int a = 3.5;
            final int[2] b = {1.2,3};
        void main(){
        string A;
        A:="This is a string containing tab \t";}}"""
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),IntType,FloatLit(3.5))"
        self.assertTrue(TestChecker.test(input,expect,460))
    def test_extends2(self):
        input = """class A{void x(){}}
        class B extends A{void main(){this.x();}}"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,461))
    def test_extends3(self):
        input = """class A{void x(){}}
        class B extends A{void x(){/*cmt*/ }}"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,462))
    def test_extends4(self):
        input = """class A{void x(){}}
        class B extends A{void x(){io.writeInt(4+5*8/3\ 4);}}"""
        expect = "Type Mismatch In Expression: BinaryOp(\,BinaryOp(/,BinaryOp(*,IntLit(5),IntLit(8)),IntLit(3)),IntLit(4))"
        self.assertTrue(TestChecker.test(input,expect,463))
    def test_extends6(self):
        input = """class A{void x(){} A(){}}
        class B extends A{
            int m;
            int x(){return m;}
        B(){this.m:=5%2-9;
        io.writeInt(m);}}"""
        expect = "Undeclared Identifier: m"
        self.assertTrue(TestChecker.test(input,expect,464))
    def test_exp0(self):
        """test the expression"""
        input = """class A{
        void main(){float m;
        m:= 1*3/5        ;
        }}"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,465))
    def test_exp1(self):
        input = input = """class A{
            void main(){float m;
            m:=   4*5/3\\6+1      ;
            if m==0 then io.writeStr("m=0");
            
            }}"""
        expect = "Type Mismatch In Expression: BinaryOp(\,BinaryOp(/,BinaryOp(*,IntLit(4),IntLit(5)),IntLit(3)),IntLit(6))"
        self.assertTrue(TestChecker.test(input,expect,466))
    def test_exp2(self):
        input = """class A{
            void main(){float m;
            m:=   (1*7)-(5*9)+1.6*50.1      ;
            }}"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,467))
    def test_exp3(self):
        input = """class A{
            void main(){float m;
            m:=  x.m(b[2]).a.g()       ;
            }}"""
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input,expect,468))
    def test_complex(self):
        input = """
class xep{
    void rearrange(int[5]sach){
        for i:= 0 to 4 do
            if sach[i]>sach[i+1] then {
                int m = sach[i+1];
                sach[i+1]:=sach[i];
                sach[i]:=m;
            }
    }
void output(int[5] sach) {
    for i:= 0 to 5 do {
            io.writeInt(xep[i]);
        }
 }
int main(){
    arr:={1,2,3,4,5};
    this.output({1,2,3,4,5});
    this.rearrange(arr);
            }
        }"""
        expect = "Type Mismatch In Expression: ArrayCell(Id(xep),Id(i))"
        self.assertTrue(TestChecker.test(input,expect,469))
    def test_final(self):
        input = """class A{
        final static int k,y=5;}"""
        expect = "Illegal Constant Expression: ConstDecl(Id(k),IntType,None)"
        self.assertTrue(TestChecker.test(input,expect,470))
    def test_final2(self):
        input = """class test{
        int a=4, m;
        int func(){
        final int a=5,m;
        m:=5;
        }
        
        }"""
        expect = "Illegal Constant Expression: ConstDecl(Id(m),IntType,None)"
        self.assertTrue(TestChecker.test(input,expect,471))
    def test_final3(self):
        input = """class A{
            int func(){
            int f,k;
            final string f=5,m;
            m:=k;
            }
            }"""
        expect = "Redeclared Constant: f"
        self.assertTrue(TestChecker.test(input,expect,472))
    def test_final4(self):
        input = """class A{
            int m;
            int m(){}
            int k(){final int d;}
            }"""

        expect = "Redeclared Method: m"
        self.assertTrue(TestChecker.test(input,expect,473))
    def test_exp4(self):
        input = """class A{
            void main(){float m;
            m:=   x.m(b[1*3+4-9*1.3]) - this.m      ;
            if m==0 then io.writeStr("m=0");
            }}"""
        expect = "Illegal Member Access: FieldAccess(Self(),Id(m))"
        self.assertTrue(TestChecker.test(input,expect,474))
    def test_exp5(self):
        input = """class A{
            int[100] arr;
            int b(int s){return s;}
            void main(){float m;
            A x;
            m:=    x.arr[1000]-(x.b(100)*30); 
            }}"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(m),BinaryOp(-,ArrayCell(FieldAccess(Id(x),Id(arr)),IntLit(1000)),BinaryOp(*,CallExpr(Id(x),Id(b),[IntLit(100)]),IntLit(30))))"
        self.assertTrue(TestChecker.test(input,expect,475))
    def test_exp8(self):
        input = """class A{
            void main(){float m;
            m:=   new A   ()   ;
            }}"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,476))
    def test_exp7(self):
        """check the string exp"""
        input = """class A{
            void main(){string m;
            m:="VO"^"HONGPHUC";
            m:=m-"PHUC";
            io.writeBool(m=="VOHONG");
            }}"""
        expect = "Type Mismatch In Expression: BinaryOp(==,Id(m),StringLit(\"VOHONG\"))"
        self.assertTrue(TestChecker.test(input,expect,477))
    def test_for_to_do_break3(self):
        input = """class A{
            void main(){
            for i:= true to 100 do {
            #a line cmt
            /*i:=1000*/
            i:=i+1;
            for i:= a||b to 100-56*1 do {
            k[i]:=i;
            }
            }
            }}"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(i),BooleanLit(True))"
        self.assertTrue(TestChecker.test(input,expect,478))
    def test_for_to_do_breaka(self):
        input = """class A{
            void main(){
            for i:= 3 to 100 do {
            #a line cmt
            /*i:=1000*/
            }
            break;
            }
            }"""
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,479))
    def test_for_to_do_breakas(self):
        input = """class A{
            void main(){
            for i:= 3 to 100 do {
            #a line cmt
            /*i:=1000*/
            }
            continue;
            }
            }"""    
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,480))
    def test_for_to_do_breakag(self):
        input = """class A{
            void main(){
            for i:= 3 to 100 do {
            #a line cmt
            /*i:=1000*/
            {
                {
                    if i==3 then
                        break;
                }
            }
            }
            }
            }"""    
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,481))
    def test_for_to_do_break4(self):
        input = """class A{
            int m(){return 5;}
            void main(){
            for i:= a.k[3+this.m()] to 100 do {
                #if i%2==0 then i:=i*2;
                
            io.writeInt(i);
            break;
            }
            }}"""
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,482))
    def test_for_to_do_break5(self):
        input = """class A{
            void main(){
                m:="PHUC";
            for i:= 1 to 100 do {
                m:=m^"123";
            }
            }
            }"""
        expect = "Undeclared Identifier: m"
        self.assertTrue(TestChecker.test(input,expect,483))
    def test_for_to_do_break7(self):
        input = """class A{
        void main(){
        for i:= 1 to 100.6 do{}
        }}"""
        #TODO raise lộn rồi má
        expect = "Type Mismatch In Statement: AssignStmt(Id(i),FloatLit(100.6))"
        self.assertTrue(TestChecker.test(input,expect,484))
    def test_if_else1(self):
        input = """class A{
        void main(){
        boolean x;
        if x then if x then if m==6 then m:=1000;
        }}"""
        expect = "Undeclared Identifier: m"
        self.assertTrue(TestChecker.test(input,expect,485))
    def test_if_else6(self):
        input = """class A{
        void main(){
        boolean x;
        if x then for i:=1 to 3 do io.writeInt(i);
        else io.writeInt(2);
        }}"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,486))
    def test_if_else8(self):
        input = """class A{
        void main(){
        boolean x;
        if x then x:={1,2,3};
        }}"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(x),[IntLit(1),IntLit(2),IntLit(3)])"
        self.assertTrue(TestChecker.test(input,expect,487))
    def test_complex5(self):
        input = """
            class testing {
                int a,b;
                testing(){
                    this.a:=5;
                    this.b:=6;
                }
            void test(testing a; float b) {
                if a.a then {
                    a := new testing();
                    m := a;
                }
                else {
                    this.a := 5;
                    b := this.test(f, "abc");
                }
            }
        } """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,488))
    def test_complex5(self):
        input = """
            class testing {
                int a,b;
                testing(){
                    this.a:=5;
                    this.b:=6;
                }
            void test(testing a; float b) {
                if a.a then {
                    a := new testing();
                    m := a;
                }
                else {
                    this.a := 5;
                    b := this.test(this.a,1.0);
                }
            }
        } """
        expect = "Type Mismatch In Statement: If(FieldAccess(Id(a),Id(a)),Block([],[AssignStmt(Id(a),NewExpr(Id(testing),[])),AssignStmt(Id(m),Id(a))]),Block([],[AssignStmt(FieldAccess(Self(),Id(a)),IntLit(5)),AssignStmt(Id(b),CallExpr(Self(),Id(test),[FieldAccess(Self(),Id(a)),FloatLit(1.0)]))]))"
        self.assertTrue(TestChecker.test(input,expect,489))
    def test_mixed_statement0(self):
        input = """class Shape {
static final int numOfShape = 0;
final int immuAttribute = 0;
float length,width;
static int getNumOfShape() {
return numOfShape;
}
}
class Rectangle extends Shape {
float getArea(){
return this.length*this.width;
}
}"""
        expect = "Undeclared Identifier: numOfShape"
        self.assertTrue(TestChecker.test(input,expect,490))
    def test_mixed_statement4(self):
        input = """class A{
        A(){}
        A(string x,y; int m){}
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,491))
    def test_mixed_statement5(self):
        input = """class Shape {
float length,width;
float getArea() {}
Shape(float length,width){
this.length := length;
this.width := width;
}
}"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,492))
    def test_mixed_statement6(self):
        input = """class Shape {
float length,width;
float getArea() {}
Shape(float length,width){
this.length := length;
this.width := width;
}
}
class Rectangle extends Shape {
float getArea(){
return this.length*this.width;
}
}
class Triangle extends Shape {
float getArea(){
return this.length*this.width / 3;
}
}
class Example2 {
void main(){
Shape s;
s := new Rectangle(3,4);
io.writeFloatLn(s.getArea());
s := new Triangle(3,4);
io.writeFloatLn(s.getArea());
}
}
"""
        expect = "Illegal Member Access: FieldAccess(Self(),Id(length))"
        self.assertTrue(TestChecker.test(input,expect,493))
    def test_mixed_statement7(self):
        input = """class Example1 {
int factorial(int n){
if n == 0 then return 1; else return n * this.factorial(n - 1);
}
void main(){
int x;
x := io.readInt();
io.writeIntLn(this.factorial(x));
}
}"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,494))
    def test_mixed_statement8(self):
        input = """class X{
        int[100] Intarray;
        X(){
        for i := 1 to 100 do {
io.writeIntLn(i);
this.Intarray[i] := i + 1;
}
for x := 5 downto 3 do
io.writeIntLn(x);
}}"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,495))
    def test_mixed_statement9(self):
        input = """class A{
        A(){
        
#start of declaration part
float r,s;
int[5] a,b;
#list of statements
r:=2.0;
s:=r*r*3.14;
a[0]:= s;
}
}"""
        expect = "Type Mismatch In Statement: AssignStmt(ArrayCell(Id(a),IntLit(0)),Id(s))"
        self.assertTrue(TestChecker.test(input,expect,496))
    def test_sample0(self):
        input = """class A{
        int main(){
        string x;
        io.readString(x);
        io.writeString(\"Your name is\");
        io.writeString(x);
        }}"""
        expect = "Undeclared Method: readString"
        self.assertTrue(TestChecker.test(input,expect,497))
    def test_sample1(self):
        """C++ to BKOOL"""
        """find the first repeating element in an array"""
        input = """
        class X{
        int main(){
  int[100] arr, n, i;
  io.writeStr( "Enter number of elements: ");
  n:=io.readInt();
  for i := 0 to  n do
    arr[i]:=io.readInt();
  for i := 0 to  n do
    for j := i+1 to  n do
      if arr[i] == arr[j] then {
        io.writeStr("First repeating integer is ");
        arr[i]:= io.writeInt();
      }
}}"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(n),CallExpr(Id(io),Id(readInt),[]))"
        self.assertTrue(TestChecker.test(input,expect,498))
    def test_sample3(self):
        input = """class A{
        int main(){
        int x,sum;
        sum:=0;
        io.readInt(x);
        for i:=1 to x do sum:=sum+i;
        }}"""
        expect = "Type Mismatch In Statement: Call(Id(io),Id(readInt),[Id(x)])"
        self.assertTrue(TestChecker.test(input,expect,499))
    