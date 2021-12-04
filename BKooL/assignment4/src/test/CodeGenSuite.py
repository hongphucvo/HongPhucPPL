import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    '''def test_bkool_int_ast(self):
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
   
    def test_bkool_float_ast(self):
        input = """class BKoolClass {static void main() {io.writeFloat(1.0);}}"""
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input,expect,504))
    
    def test_bkool_float_ast1(self):
        input = """class BKoolClass {static void main() {io.writeFloat(1.1);}}"""
        expect = "1.1"
        self.assertTrue(TestCodeGen.test(input,expect,505))


    def test_con(self):
        
        input = """
        class A{int x;}
        class BKoolClass {
            
            static void main(){
                io.writeInt(12);
            }
        }"""
        expect = "12"
        self.assertTrue(TestCodeGen.test(input,expect,506))
        """//for i:=5 downto 10 do {continue;} int x(){
                
                return 5;
            }"""
      
    def test_bkool_str_ast1(self):
        input = """class BKoolClass {static void main() {io.writeStr("1.1");}}"""
        expect = "1.1"
        self.assertTrue(TestCodeGen.test(input,expect,553))

    def test_bkool_str1(self):
        input = """class BKoolClass {static void main() {io.writeStr("1.1+178273hjshaslcnad");}}"""
        expect = "1.1+178273hjshaslcnad"
        self.assertTrue(TestCodeGen.test(input,expect,554))

    def test_bkool_str(self):
        input = """class BKoolClass {static void main() {io.writeStr("siuadh\\n sajds//sdjansk");}}"""
        expect = """siuadh
 sajds//sdjansk"""
        self.assertTrue(TestCodeGen.test(input,expect,555))
    def test_bkool_bool_ast1(self):
        input = """class BKoolClass {static void main() {io.writeBool(true);}}"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,556))

    def test_bkool_bool1(self):
        input = """class BKoolClass {static void main() {io.writeBool(false);}}"""
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,557))
    
'''



    '''
    def test_bkool_bool1(self):
        input = """class BKoolClass {static void main() {int a;}}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,558))
    
    def test_bkool_bool1(self):
        input = """class BKoolClass {static void main() {final int a;}}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,559))
    
'''

#TODO: const and var check
    def test_bkool_bool1(self):
        input = """class BKoolClass { static void main() {int a;a:=1;}}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,559))
    
'''
    def test_bkool_bool1(self):
        input = """class BKoolClass {int b; static void main() {int a;a:=1;}}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,559))
    '''









    
    
















'''
    def test_re_param(self):
        input = """class BKoolClass{
            int x(int k,k){}

            static void main(){
                io.writeInt(2001+1234);
            }
        }"""
        expect = "3235"
        self.assertTrue(TestCodeGen.test(input,expect,507))
    
    def test_re_method(self):
        input = """class BKoolClass{
            int x(){return 5;}
            static void main(){
                io.writeInt(this.x);
            }    
        }"""
        expect = "5"
        self.assertTrue(TestCodeGen.test(input,expect,508))
    
    def test_wrong_attri(self):
        input = """class BKoolClass{
            float x=5.0;

            static void main(){
                io.writeFloat(x);
            }
        }"""
        expect = "5.0"
        self.assertTrue(TestCodeGen.test(input,expect,509))
    
    def test_wrong_attri1(self):
        input = """class BKoolClass{
            string x="1";
            static void main(){
                io.writeStr(x);
            }

        }"""
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,510))
    
    def test_wrong_var(self):
        input = """class BKoolClass{
            int x(){ string a=\"5\";return 5;}
            static void main(){
                string x="5.2";
                io.writeInt(x);
            }
        }"""
        expect = "5.2"
        self.assertTrue(TestCodeGen.test(input,expect,511))
    
    def test_wrong_return(self):
        input = """class BKoolClass{
            float x(){ int a=5;return 5.2;}
            static void main(){
                io.writeBool(true);
            }
        }"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,512))
    def test_wrong_assign_fi(self):
        input = """class BKoolClass{
            int x(){ int a=5;a:=2.1;}
            static void main(){int a=5;a:=2;
                io.writeInt(a+7);
            }
        }"""
        expect = "9"
        self.assertTrue(TestCodeGen.test(input,expect,513))
    
    def test_wrong_exp_sf(self):
        input = """class BKoolClass{
            int x(){ int a=5;a:=2.1+"";}
            static void main(){
                io.writeInt(1+2*3-4\5%8-3);
            }    
        }"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,514))
     
    def test_undecl(self):
        input = """class BKoolClass{
            int x(){ int m; m:=k;}
            static void main(){
                io.writeInt(-1*3);
            }
        }"""
        expect = "-3"
        self.assertTrue(TestCodeGen.test(input,expect,515))

    def test_wrong_for(self):
        input = """class BKoolClass{
            int x(){ 
                int m;
                for a:=5 to 10 do 
                {int x;}
                return 10;
            }
            static void main(){
                io.writeInt(1+this.x(););
            }
        }"""
        expect = "11"
        self.assertTrue(TestCodeGen.test(input,expect,516))
    
    def test_wrong_array(self):
        input = """class BKoolClass{
            int x(){ 
                int[1] m={4};
                return 5;
            }
            static void main(){
                int a;
                int b;
                io.writeInt(1);
            }
        }"""
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,517))
    
    
    def test_wrong_arrayindex(self):
        input = """class BKoolClass{
           void x(){
                int[1] m={4};
                
                io.writeInt(2010);
            }
            static void main(){
                io.writeInt(5);
            }
        }"""
        expect = "5"
        self.assertTrue(TestCodeGen.test(input,expect,517))
    
    def test_wrong_field_acc(self):
        input = """class BKoolClass{
            int k;
            int x(int e)
            {  A temp;
                temp.k:=5;
            }
            static void main(){
                io.writeInt(-74+65
                );
            }
            }"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,518))
    
    def test_right_field_par(self):
        input = """
        class X{int m;}
        class BKoolClass extends X{
            int k;
            int x(int e)
            {  A temp;
                temp.m:=5;
            }
            static void main(){
                int x;
                for x:=5 to 10 do io.writeBool(true);
            }
            }"""
        expect = "truntruetruetruetrue"
        self.assertTrue(TestCodeGen.test(input,expect,519))
    
    def test_wrong_cell(self):
        input = """
        class BKoolClass{
            int[1] k;
            static void main(){
                bool x=true;
                io.writeBoolLn(x);
                io.writeInt(2013);
            }
            int x()
            {  this.k[2]:=2.5;
            }
            }"""
        expect = "true2013"
        self.assertTrue(TestCodeGen.test(input,expect,520))
    
    def test_wrong_call_void(self):
        input = """
        class BKoolClass{
            int[1] k;
            int y(){int a=5;}
            int x()
            {  this.y();
            }
            static void main(){
                io.writeIntStr("2014/asfaf\\asfa");
            }
            }"""
        expect = "2014/asfaf\\asfa"
        self.assertTrue(TestCodeGen.test(input,expect,521))

    def test_right_call_(self):
        input = """
        class BKoolClass{
            int[1] k;
            void y(int b){int a=5;}
            int x()
            {  this.y(10);
            }
            static void main(){
                io.writeBoolLn(true||false&&true||false);
            }
            }"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,522))
    def test_wrong_call_para(self):
        input = """
        class BKoolClass{
            int[1] k;
            void y(int b){int a=5;}
            int x()
            {  this.y(10.5);
            }
            static void main(){
                io.writeBool(5==6&&9==8);
            }
            }"""
        expect = "Type Mismatch In Statement: Call(Self(),Id(y),[FloatLit(10.5)])"
        self.assertTrue(TestCodeGen.test(input,expect,523))
    def test_var_as_class(self):
        input = """
        class BKoolClass{
            int A;
            static void main(){
                io.writeBool(7-5!=4*3)
            }
        }"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,524))
    def test_ill_const(self):
        input = """class BKoolClass{
            static void main(){
                io.writeFloat(7/7/7/7)
            }
            }"""
        expect = " "
        self.assertTrue(TestCodeGen.test(input,expect,525))
    
    def test_io(self):
        input = """class BKoolClass extends io{int x;
            static void main(){
                this.writeInt(2000);
            }
        }"""
        expect = "2000"
        self.assertTrue(TestCodeGen.test(input,expect,526))
    def test_extend_io(self):
        input = """class BKoolClass extends io{
            int x=5;
            static void main(){

                io.writeInt(this.x+6);
            }
            }"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,527))
    
    def test_io_med(self):
        input = """class BKoolClass{
            int x(){
                io.writeInt(9);
            }
            static void main(){
                if (true)
                    io.writeInt(2019);
                else io.writeFloat(7.0);
            }
        }"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,528))
    def test_io_param(self):
        input = """class BKoolClass{
            int x(){
                io.writeInt(9);
                return 2;
            }
            static void main(){
                if(false)
                    io.writeInt(2020);
                io.writeInt(2020);
            }
        }"""
        expect = "Type Mismatch In Statement: Call(Id(io),Id(writeInt),[FloatLit(9.3)])"
        self.assertTrue(TestCodeGen.test(input,expect,529))
        
    def test_io_param_1(self):
        input = """class BKoolClass{
            int x(){
                if (true)
                    int a=7();
                io.writeBool(true);
            }
            static void main(){
                io.writeInt("2021"^"27247");
            }
        }"""
        expect =""
        self.assertTrue(TestCodeGen.test(input,expect,530))
    def test_io_2(self):
        input = """class BKoolClass{
            int x(){
                io.writeStr(\"123456\");
            }
            static void main(){
                string a="";
                if a!="1"
                    io.writeInt(2022);
                io.writeStr(a);
            }
        }"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,531))
    
    def test_return0(self):
        input = """class BKoolClass{
            static void main(){
                io.writeFloat(2022.1);
            }
    int main(){
    int b;
    {int a;}
    return 0.5;
    }
}"""
        expect = "Type Mismatch In Statement: Return(FloatLit(0.5))"
        self.assertTrue(TestCodeGen.test(input,expect,532))

    def test_return_1(self):
        input = """class BKoolClass{
            float x(){
                if true then return 1.3;
            }
            static void main(){
                io.writeFloat(2022.2);
            }
        }"""
        expect = "2022.2"
        self.assertTrue(TestCodeGen.test(input,expect,533))

    def test_return_2(self):
        input = """class BKoolClass{
            m(){
                if true then {return 1.3;}
            }

            static void main(){
                io.writeFloat(2022.3+54);
            }

        }"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,534))
    
    def test_return_3(self):
        input = """class BKoolClass{
            int x(){
                io.writeStr(\"123456\");
            }

            static void main(){
                io.writeFloat(2022.4);
                io.writeStr(\"123456\");
            }

        }"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,535))

    def test_empty_block(self):
        input = """class BKoolClass{
        static void main(){
                io.writeBool(2022.5==789);
            }
        int main(){
          float number, root;
          {}
          }
        }"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,536))
    def test_const_ill(self):
        input = """class BKoolClass{int main(){
  final float number = root;
  this.root:=5;}
            static void main(){
                io.writeFloat(2022.6);
            }
}"""
        expect = "Undeclared Identifier: root"
        self.assertTrue(TestCodeGen.test(input,expect,537))
    def test_io_expr(self):
        input = """class BKoolClass{int main(){ 
             io.writeFloat(7*9-10);
            }
            static void main(){
                io.writeBool(2022.7==1234&&5>6);
            }
        }"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,538))
    def test_dup_att(self):
        input = """class BKoolClass{
            int id;
            static void main(){
                io.writeBool(89==9&&"k"="m");
            }
        }
        class Faculty { int id;}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,539))
    def test_att_method_inner(self):
        input = """class BKoolClass{        
            int id;        
            void print(){
                io.writeInt(this.id);
            }
            static void main(){
                io.writeFloat(2022.9);
                this.id=6;
                io.writeInt(this.id);
                
            }
        }"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,540))
    def test_method_decl(self):
        input = """class BKoolClass{
        int id=4;
        static void main(){
                io.writeFloat(2023.1);
                this.print();
            }
        void print(){io.writeInt(this.id);}
        int go(int a,b;float d){
            io.writeInt(0);

        }
        }"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,541))
    def test_io_call(self):
        input = """class BKoolClass{
        int id;
        static void main(){
                this.print();
            }
        void print(){io.writeFloat(5+7-9/88);}}
        class Faculty{int id;
        void Faculty(){
            this.id:=1911881;
        }}
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,542))
    def test_extend_io_int(self):
        input = """class BKoolClass extends io{
            static void main(){
                io.writeFloat(2023.2);
            }
            int x(){
            this.writeInt(1++35+8+6-4-5-2);
            }
        }"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,543))
    def test_extend_io_int_1(self):
        input = """class BKoolClass {int x(){
                io.writeInt(0);
            }
            static void main(){
                io.writeFloat(2023.3);
            }
        }"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,544))
  
    def test_class_decl_0(self):
        input = """class BKoolClass{
        static int id;
        static void main(){
            Faculty x;
            x.print();
                io.writeFloat(2023.4);
            }
        void print(){
        int a=100;
        io.writeInt(a);}
        }
        class Faculty extends BKoolClass{
            void print(){
                io.writeInt(1);
            }
        }"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,545))
    def test_expr_0(self):
        input = """class BKoolClass{
            static void main(){
                io.writeFloat(2023.5);
                io.writeInt(this.main());
            }
            int main(){
                int a = (1234+9857-(6574*(8754-87/3\\1)));
                io.writeFoat(a);
                return 1;
            }
        }"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,546))
    def test_expr_1(self):
        input = """class BKoolClass{
        int[2]m;
        static void main(){
                io.writeFloat(2023.6);
            }
         void BKoolClass(){
         this.m:={1,2};}}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,547))
    def test_expr_2(self):
        input = """class BKoolClass{
            static void main(){
                io.writeFloat(2023.7);
                io.writeStr("SIDKAHS/*-/23982\\");
            }
            void k(){io.writeInt(1+4-e);}
            X(){}}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,548))
    
    def test_expr_3(self):
        input = """class BKoolClass{
            static void main(){
                io.writeInt(this.main());
            }
                int main(){
                boolean _=true||false;
                int a=+1-5;
                boolean  e= _;
                io.writeBool(_);
                return a;
                }
                }"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,549))
    
    def test_t02(self):
        input = """class BKoolClass{
            int k;
            static void main(){
                X m;
                m.k=5;
                io.writeBool(this.lessthan(m));
            }
            boolean lessthan(X source){
                if this.k<source.k then return true;
                else if this.k==source.k then return false;
                else return false;
            }
            }"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,550))
    def test_t03(self):
        input = """class BKoolClass{
            int k;
            static void main(){
                io.writeStr(\"hippo\");
                X m;
                m.k=5;
                io.writeBool(this.notequal(m));
            }
            boolean notequal(X source){
                if this.k==source.k+1 then return false;
                else return true;
            }
            }"""
    
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,551))
    def test_t04(self):
        input = """class BKoolClass{
            int k;
            static void main(){
                io.writeStr(\"hippo1\");
                X m;
                m.k=5;
                io.writeBool(this.mod2(m));
            }
            boolean mod2(X source){
                if (this.k%2==0 )&&(source.k%2==0) then return true;
                else return false;
            }
            }"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,552))










    
    '''