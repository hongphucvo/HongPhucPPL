import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_bkool_int_ast(self):
        input = """class BKoolClass {static void main() {io.writeInt(1);}}"""
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,500))
    def test_bkool_bin_ast(self):
        input = """class BKoolClass {static void main() {io.writeInt(1+3);}}"""
        expect = "4"
        self.assertTrue(TestCodeGen.test(input,expect,501))
    def test_int_ast(self):
    	input = Program([ClassDecl(Id("BKoolClass"),
                            [MethodDecl(Static(),Id("main"),[],VoidType(),
                                Block([],[CallStmt(Id("io"),Id("writeInt"),[IntLiteral(1)])]))])])
    	expect = "1"
    	self.assertTrue(TestCodeGen.test(input,expect,502))
    def test_binary_ast(self):
        input = Program([ClassDecl(Id("BKoolClass"),
                    [MethodDecl(Static(),Id("main"),[],VoidType(),
                        Block([],[CallStmt(Id("io"),Id("writeInt"),[BinaryOp("+",IntLiteral(1),IntLiteral(3))])]))])])
        expect = "4"
        self.assertTrue(TestCodeGen.test(input,expect,503))


    def test_simple_program(self):
        """Simple program: class main {} """
        input = """class main {}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,300))

    def test_class_with_one_decl_program(self):
        """More complex program"""
        input = """class main {
            int a;
        }"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,301))

    def test_class_with_two_decl_program(self):
        """More complex program"""
        input = """class main {
            int a;
            int b;
        }"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,302))
    def test_simple_program1(self):
        """Simple program: 1 method """
        input = """class A{int main(){}}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 303))

    def test_simple_test1(self):
        input = input = """class A{
    int main(){
    int b;
    {int a;}
    return 0;
    }
}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 304))
    def test_simple_test2(self):
        input = """class A{
        int main(){
          float number, root;
          {}
          }
        }"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 305))
    def test_simple_test3(self):
        input = """class A{
    int main(){
    float number = 7.0, root=2.3;
    {}}
}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 306))
    def test_simple_test4(self):
        input = """class A{int main(){
 float number=9.0; int root;}
}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 307))
    def test_simple_test5(self):
        input = """class A{static int main(){
float number=7.3, root;}
}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 308))
    def test_simple_test6(self):
        input = """class A{int main(){
  final float number = root;
  this.root:=5;}
}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 309))

    def test_simple_test8(self):
        input = """class A{int main(){  io.writeFloat(7*9-10);}}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 310))
    def test_class_dcl1(self):
        """only class declaration"""
        input = """class School{ int longitude,latitude;}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 311))
    def test_class_dcl2(self):
        input = """class School{ int longitude,latitude;}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 312))
    def test_class_dcl3(self):
        input = """class School{int id;}
        class Faculty { int id;}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 313))
    def test_class_dcl4(self):
        input = """class School{
        int id;
        void print(){io.writeInt(this.id);}}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 314))
    def test_class_dcl5(self):
        input = """class School{
        int id;
        void print(){io.writeInt(this.id);}
        int go(int a,b;float d){
            io.writeInt(0);
        }
        }"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 315))
    def test_class_dcl6(self):
        input = """class School{
        int id;
        void print(){io.writeInt(5+7-9*88);}}
        class Faculty{int id;
        void Faculty(){
            this.id:=1911881;
        }}
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 316))
    def test_class_dcl7(self):
        input = """class School{
        int id;
        void print(){}}
        class Faculty{int id;}
        class Student extends School{
            int id;
            }"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 317))

    def test_class_dcl8(self):
        input = """class School{
        int id;
        void print(){io.writeInt(this.id);}
        }
        class Faculty{int id; void main(){return 0;}}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 318))
    def test_class_dcl9(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 319))
    def test_class_dcl10(self):
        input = """class School{
        int _id;
        void print(){
        int a;
        io.writeInt(this.id);
        }
        }"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 320))

    def test_wrong_miss_close1(self):
        """Bracket close"""
        input = """class A{int main(){
            int a = (1234+9857-(6574*(8754-87/3\\1)));}
        }"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 321))
    def test_wrong_miss_close(self):
        input = """class X{
        int[2]m;
         void X(){
         m:={1,2};}}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 322))

    def test_wrong_miss_closede(self):
        input = """class X{
            void k(){io.writeInt(1+4-e);}
            X(){}}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 323))

    def test_asdfgh(self):
        input = """class X{
                int main(){
                boolean _=true||false;
                int a=+1-5;
                boolean  e= _;
                }
                }"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 324))
    def test_final6(self):
        input = """class A{}
            class B extends A{int a;}
            class C extends A{int a;}
            class A{int x;}"""
        expect="""Program([ClassDecl(Id(A),[]),ClassDecl(Id(B),Id(A),[AttributeDecl(Instance,VarDecl(Id(a),IntType))]),ClassDecl(Id(C),Id(A),[AttributeDecl(Instance,VarDecl(Id(a),IntType))]),ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(x),IntType))])])"""
        self.assertTrue(TestCodeGen.test(input, expect, 325))




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
        self.assertTrue(TestCodeGen.test(input, expect, 326))
    def test_t03(self):
        input = """class X{
            int k;
            boolean notequal(X source){
                if this.k==source.k then return false;
                else return true;
            }
            }"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 327))
    def test_t04(self):
        input = """class X{
            int k;
            boolean mod2(X source){
                if (this.k%2==0 )&&(source.k%2==0) then return true;
                else return false;
            }
            }"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 328))
    def test_wrong_miss_close3(self):
        input = """class X{
        void print(string str){io.writeString(str);}
        void main(){this.print(\"str\");}}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 329))
    def test_wrong_miss_close4(self):
        input = """class classX{
        void print(string str){io.writeString(str);}
        void main(){this.print("");}}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 330))








    def test_literal1(self):
        """StringLit and ArrayLit"""
        input = """class Lit{
        void main(){
        string A;
        A:=\"my name\";
        A:="This is a string containing tab \t";}}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 331))
    def test_literal2(self):
        input = """class Lit{
        void main(){
        string A;
        A:="";
        A:=A+"HongPhuc";
        }}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 332))
    def test_literal3(self):
        input = """class Lit{
        void main(){
        string A;
        A:="He asked me: \\\"Where is John?\\\"";}}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 333))
    def test_literal4(self):
        input = """class Lit{
            void main(){
                string A;
                int[2] b = {1.2,A};
                A:="The comment starts with #";
        
                A:={"A"};}}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 334))
    def test_literal5(self):
        input = """class Lit{
        void main(){
        string A;
        string[1] A;
        A:="Open the string";
        A:={"A#cmt"};}}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 335))
    def test_literal6(self):
        input = """class Lit{
        void main(){
        int[2] A;
        A:={1.2,6};}}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 336))
    def test_literal7(self):
        input = """class Lit{
            final int a = 3.5;
        void main(){
        string A;
        A:="This is a string containing tab \t";}}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 337))
    def test_literal8(self):
        """wrong type"""
        input = """class Lit{
            final int a = 3.5;
            final static int a=10;
            static float m="1234";
        void main(){
        string A;
        A:="This is a string containing tab \t";}}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 338))
    def test_literal9(self):
        """wrong type"""
        input = """class Lit{
            final int a = 3.5;
            final int[2] b = {1.2,3};
        void main(){
        string A;
        A:="This is a string containing tab \t";}}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 339))

    def test_extends0(self):
        """inheritance"""
        input = """class A{int b;}
        class B extends A{ int d;}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 340))
    def test_extends1(self):
        input = """class A{int b;}
        class B extends A{ int d;}
        class C extends B{int k;}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 341))
    def test_extends2(self):
        input = """class A{void x(){}}
        class B extends A{void main(){this.x();}}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 342))
    def test_extends3(self):
        input = """class A{void x(){}}
        class B extends A{void x(){/*cmt*/ }}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 343))
    def test_extends4(self):
        input = """class A{void x(){}}
        class B extends A{void x(){io.writeInt(4+5*8/3\ 4+a.b.c.d());}}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 344))
    def test_extends5(self):
        input = """class A{void x(){}}
        class B extends A{void x(){io.writeInt(m.b().a.c().d);}}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 345))
    def test_extends6(self):
        input = """class A{void x(){} A(){}}
        class B extends A{
            int m;
            int x(){return m;}
        B(){this.m:=5%2-9;
        io.writeInt(m);}}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 346))

    def test_exp0(self):
        """test the expression"""
        input = """class A{
        void main(){float m;
        m:= 1*3/5        ;
        }}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 347))

    def test_exp1(self):
        input = input = """class A{
            void main(){float m;
            m:=   4*5/3\\6+1      ;
            if m==0 then io.writeStr("m=0");
            
            }}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 348))

    def test_exp2(self):
        input = """class A{
            void main(){float m;
            m:=   (1*7)-(5*9)+1.6*50.1      ;
            }}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 349))
    def test_exp3(self):
        input = """class A{
            void main(){float m;
            m:=  x.m(b[2]).a.g()       ;
            }}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 350))

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
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 351))
    def test_final(self):
        input = """class A{
        final static int k,y=5;}"""

        expect="""Program([ClassDecl(Id(A),[AttributeDecl(Static,ConstDecl(Id(k),IntType,None)),AttributeDecl(Static,ConstDecl(Id(y),IntType,IntLit(5)))])])"""
        self.assertTrue(TestCodeGen.test(input, expect, 352))

    def test_final1(self):
        input = """class MJ{
        final int k=5; 
        int g=3;}
        class HJ{
        final int k=5; 
        int e=3;}"""

        expect="""Program([ClassDecl(Id(MJ),[AttributeDecl(Instance,ConstDecl(Id(k),IntType,IntLit(5))),AttributeDecl(Instance,VarDecl(Id(g),IntType,IntLit(3)))]),ClassDecl(Id(HJ),[AttributeDecl(Instance,ConstDecl(Id(k),IntType,IntLit(5))),AttributeDecl(Instance,VarDecl(Id(e),IntType,IntLit(3)))])])"""
        self.assertTrue(TestCodeGen.test(input, expect, 353))

    def test_final2(self):
        input = """class test{
        int a=4, m;
        int func(){
        final int a=5,m;
        m:=5;
        }
        
        }"""

        expect="""Program([ClassDecl(Id(test),[AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(4))),AttributeDecl(Instance,VarDecl(Id(m),IntType)),MethodDecl(Id(func),Instance,[],IntType,Block([ConstDecl(Id(a),IntType,IntLit(5)),ConstDecl(Id(m),IntType,None)],[AssignStmt(Id(m),IntLit(5))]))])])"""
        self.assertTrue(TestCodeGen.test(input, expect, 354))

    def test_final3(self):
        input = """class A{
            int func(){
            int f,k;
            final string f=5,m;
            m:=k;
            }
            }"""

        expect="""Program([ClassDecl(Id(A),[MethodDecl(Id(func),Instance,[],IntType,Block([VarDecl(Id(f),IntType),VarDecl(Id(k),IntType),ConstDecl(Id(f),StringType,IntLit(5)),ConstDecl(Id(m),StringType,None)],[AssignStmt(Id(m),Id(k))]))])])"""
        self.assertTrue(TestCodeGen.test(input, expect, 355))



    def test_final4(self):
        input = """class A{
            int m;
            int m(){}
            int k(){final int m;}
            }"""

        expect="""Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(m),IntType)),MethodDecl(Id(m),Instance,[],IntType,Block([],[])),MethodDecl(Id(k),Instance,[],IntType,Block([ConstDecl(Id(m),IntType,None)],[]))])])"""
        self.assertTrue(TestCodeGen.test(input, expect, 356))
    def test_final5(self):
        input = """class MJ{
            final int k=5; 
            int g=3;}
            class HJ{
            final int k=5; 
            int e=3;}"""

        expect="""Program([ClassDecl(Id(MJ),[AttributeDecl(Instance,ConstDecl(Id(k),IntType,IntLit(5))),AttributeDecl(Instance,VarDecl(Id(g),IntType,IntLit(3)))]),ClassDecl(Id(HJ),[AttributeDecl(Instance,ConstDecl(Id(k),IntType,IntLit(5))),AttributeDecl(Instance,VarDecl(Id(e),IntType,IntLit(3)))])])"""
        self.assertTrue(TestCodeGen.test(input, expect, 357))


    def test_exp4(self):
        input = """class A{
            void main(){float m;
            m:=   x.m(b[1*3+4-9*1.3]) - this.kd      ;
            if m==0 then io.writeStr("m=0");
            }}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 358))
    def test_exp5(self):
        input = """class A{
            void main(){float m;
            m:=    x.arr[1000]-(x.b(100)*30); 
            }}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 359))
    def test_exp8(self):
        """We need """
        input = """class A{
            void main(){float m;
            m:=   new A   ()   ;
            }}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 360))
    def test_exp7(self):
        """check the string exp"""
        input = """class A{
            void main(){string m;
            m:="VO"^"HONGPHUC";
            m:=m-"PHUC";
            io.writeBool(m=="VOHONG");
            }}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 361))
    def test_exp6(self):
        """str exp"""
        input = """class A{final string m = "HONGPHUC";
            void main(){
            m:="VO"^"HONGPHUC";
            m:=m-"PHUC";
            io.writeBool(m=="VOHONG");
            }}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 362))
    def test_for_to_do_break3(self):
        input = """class A{
            void main(){
            for i:= a==t to 100 do {
            #a line cmt
            /*i:=1000*/
            i:=i+1;
            for i:= a||b to 100-56*1 do {
            k[i]:=i;
            }
            }
            }}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 363))
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
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 364))
    def test_for_to_do_break5(self):
        input = """class A{
            void main(){
                m:="PHUC";
            for i:= 1 to 100 do {
                m:=m^"123";
            }
            }
            }"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 365))



    def test_for_to_do_break6(self):
        input = """class A{
        int m(){}
        void main(){
        A x;
        for i:= 1 downto 100 do {
            x.m();
            continue;
        }
        }}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 366))
    def test_for_to_do_break7(self):
        input = """class A{
        void main(){
        for i:= 1 to 100.6 do{}
        }}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 367))
    def test_if_else1(self):
        input = """class A{
        void main(){
        boolean x;
        if x then if x then if m==6 then m:=1000;
        }}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 368))
    def test_if_else4(self):
        input = """class A{
        void main(){
        boolean x;
        if x then if y then x:=false;
        else x:=true;
        }}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 369))
    def test_if_else5(self):
        input = """class A{
        void main(){
        boolean x;
        if x then if(this.m==7)then x:=true;
        else io.writeInt(100);
        else io.writeInt(1);
        }}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 370))
    def test_if_else6(self):
        input = """class A{
        void main(){
        boolean x;
        if x then for i:=1 to 3 do io.writeInt(i);
        else io.writeInt(2);
        }}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 371))
    def test_if_else7(self):
        input = """class A{
        void main(){
        boolean x;
        if x then x.m(5);
        }}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 372))
    def test_if_else8(self):
        input = """class A{
        void main(){
        boolean x;
        if x then x:={1,2,3};
        }}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 373))
    def test_if_else9(self):
        input = """class A{
        void main(){
        boolean x;
        if x then io.readInt(x);
        }}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 374))
    def test_if_else10(self):
        input = """class A{
        void main(){
        boolean x;
        if x then io.readBool(x);
        else io.writeBool(x);
        }}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 375))

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
                    a := new Block(a,d);
                    m := a.v.x.a[1];
                }
                else {
                    this.a := this.function();
                    b := m.g.h(f, "abc");
                }
            }
        } """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 376))
    def test_complex6(self):
        input = """
        class A extends M{
            int a=5;
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 377))
    def test_complex7(self):
        input = """
        class Bus
    {
        string ID;
        string Code;
        int Case;
        int Start;
        int Finish;

        Bus()
        {
            ID := "";
            Code := "";
            Case := -1;
            Start := 0;
            Finish := 0;
            next := 0;
            prev := 0;
        }
        Bus(string ID , CODE ; int Case , Start , Finish)
        {
            this.ID := ID;
            this.Code := CODE;
            this.Case := Case;
            this.Start := Start;
            this.Finish := Finish;
        }
    }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 378))
    def test_complex8(self):
        input = """
        class xep{
void output(int[5] sach) {
    for i:= 0 to 5 do {
            io.writeInt(xep[i]);
        }
 }
int main(){
    this.output({1,2,3,4,5});
            }
        }"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 379))

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
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 380))
    def test_mixed_statement1(self):
        input = """class A{
        #this is a cmt
        int a=4+5;
        }"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 381))
    def test_mixed_statement2(self):
        input = """ class A{
        # cmt contain illegal escape \p
        int main(){
        io.writeString("legal");
        }
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 382))
    def test_mixed_statement3(self):
        input = """
        class A{int x;
        }
        #cmt"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 383))
    def test_mixed_statement4(self):
        input = """class A{
        A(){}
        A(string x,y; int m){}
        }"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 384))
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
        self.assertTrue(TestCodeGen.test(input, expect, 385))


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
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 386))
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
        self.assertTrue(TestCodeGen.test(input, expect, 387))
    def test_mixed_statement8(self):
        input = """class X{
        int[100] Intarray;
        X(){
        for i := 1 to 100 do {
io.writeIntLn(i);
Intarray[i] := i + 1;
}
for x := 5 downto 3 do
io.writeIntLn(x);
}}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 388))
    def test_mixed_statement9(self):
        input = """class A{
        A(){
        
#start of declaration part
float r,s;
int[5] a,b;
#list of statements
r:=2.0;
s:=r*r*this.myPI;
a[0]:= s;
}
}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 389))

    def test_sample0(self):
        input = """class A{
        int main(){
        string x;
        io.readString(x);
        io.writeString(\"Your name is\");
        io.writeString(x);
        }}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 390))


    def test_sample1(self):
        """C++ to BKOOL"""
        """find the first repeating element in an array"""
        input = """
        class X{
        int main(){
  int[100] arr, n, i;
  io.writeString( "Enter number of elements: ");
  io.readInt(n);
  for i := 0 to  n do
    io.readInt(arr[i]);
  for i := 0 to  n do
    for j := i+1 to  n do
      if arr[i] == arr[j] then {
        io.writeString("First repeating integer is ");
         io.writeInt(arr[i]);
      }
}}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 391))
        """P of triangle"""
    def test_sample2(self):
        input = """class A{
        int main(){
        io.writeInt(io.readInt(x)+io.readInt(x)+io.readInt(x));
        }}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 392))

        """Sum of n"""
    def test_sample3(self):
        input = """class A{
        int main(){
        int x,sum;
        sum:=0;
        io.readInt(x);
        for i:=1 to x do sum:=sum+i;
        }}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 393))

    def test_sample4(self):
        """sum of two ints"""
        input = """class A{
        int main(){
        int x,y;
        io.readInt(x);
        io.readInt(y);
        io.writeInt(x+y);
        }}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 394))
        """cmt in main"""
    def test_sample5(self):
        input = """class A{
        int main(){
        int x,y;
        io.readInt(x);
        io.readInt(y);
        # this is a line cmt
        /* and a terminated cmt*/
        }
        }"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 395))

    def test_sample6(self):
        input = """class A{
        int main(){
        int[3] x;
        int sum; sum:=0;
        for i:=1 to n do sum := sum*10+io.readInt(x[i]);
        }}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 396))

    def test_sample7(self):
        input = """class A{
        int main(){
        int x;
        io.readInt(x);
        io.writeInt(-x);
        }}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 397))

    def test_sample8(self):
        input = """class A{
        int main(){
        int x;
        io.readInt(x);
        io.writeInt(x%3);
        }}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 398))
        """rec class"""
    def test_sample9(self):
        input = """class rec{
        int w,b;
        int main(){
        io.readInt(this.w);
        io.readInt(this.b);
        io.writeInt(w*b);
        }}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 399))
