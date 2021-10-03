
import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):


    def test_simple_test1(self):
        input = """class A{int main(){
        int b;
        {int a;}
  return 0;}
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))
    def test_simple_test2(self):
        input = """class A{int main(){
  float number, root;
  {}
  }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))
    def test_simple_test3(self):
        input = """class A{
int main(){
{}
final float number = 7.0, root=2.3;}
}"""
        expect = "Error on line 4 col 0: final"
        self.assertTrue(TestParser.test(input, expect, 204))
    def test_simple_test4(self):
        input = """class A{int main(){
static float number=9.0; int root;}
}"""
        expect = "Error on line 2 col 0: static"
        self.assertTrue(TestParser.test(input, expect, 205))
    def test_simple_test5(self):
        input = """class A{static int main(){
float number=7.3; root;}
}"""
        expect = "Error on line 2 col 22: ;"
        self.assertTrue(TestParser.test(input, expect, 206))
    def test_simple_test6(self):
        input = """class A{int main(){
  final float number = root;
  this.root:=5;
final x;}
}"""
        expect = "Error on line 4 col 0: final"
        self.assertTrue(TestParser.test(input, expect, 207))
    def test_simple_test7(self):
        input = """class A{int main(){
  io.writeFloat(root);}
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))
    def test_simple_test8(self):
        input = """class A{int main(){
  io.writeFloat(7*9-10);}
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 209))
    def test_simple_test9(self):
        input = """class A{int main(){
        #This is a line cmt
}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))

    def test_class_dcl1(self):
        """only class declaration"""
        input = """class School{ int longitude,latitude;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 211))
    def test_class_dcl2(self):
        input = """class School{ int longitude,latitude;"""
        expect = "Error on line 1 col 37: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 212))
    def test_class_dcl3(self):
        input = """class School{int id;}
        class Faculty { int id;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))
    def test_class_dcl4(self):
        input = """class School{
        int id;
        void print(){io.writeInt(this.id);}"""
        expect = "Error on line 3 col 43: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 214))
    def test_class_dcl5(self):
        input = """class School{
        int 0id;
        void print(){io.writeInt(this.id);}"""
        expect = "Error on line 2 col 12: 0"
        self.assertTrue(TestParser.test(input, expect, 215))
    def test_class_dcl6(self):
        input = """class School{
        int id;
        void print(){io.writeInt(this.id);}
        class Faculty{int id;}
        """
        expect = "Error on line 4 col 8: class"
        self.assertTrue(TestParser.test(input, expect, 216))
    def test_class_dcl7(self):
        input = """class School{
        int id;
        void print(){}}
        class Faculty{int id;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 217))
    def test_class_dcl8(self):
        input = """class School{
        int id;
        void print(){io.writeInt(this.id);}
        }
        class Faculty{int id; void main(){return 0;}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))
    def test_class_dcl9(self):
        input = """class School{
        int id;
        void print(){
        static int a=100;
        io.writeInt(a);}
        }"""
        expect = "Error on line 4 col 8: static"
        self.assertTrue(TestParser.test(input, expect, 219))
    def test_class_dcl10(self):
        input = """class School{
        int _id;
        void print(){
        io.writeInt(this.id);
        int a;}
        }"""
        expect = "Error on line 5 col 8: int"
        self.assertTrue(TestParser.test(input, expect, 220))

    def test_wrong_miss_close1(self):
        """Bracket close"""
        input = """class A{int main(){}"""
        expect = "Error on line 1 col 20: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 221))
    def test_wrong_miss_close2(self):
        input = """class exp{
        final int k=(1+3*(4-7));}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 222))
    def test_wrong_miss_close3(self):
        input = """class exp{
        int a;
        void print(){"""
        expect = "Error on line 3 col 21: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 223))
    def test_wrong_miss_close4(self):
        input = """class A{int main(){ m.print(;}}"""
        expect = "Error on line 1 col 28: ;"
        self.assertTrue(TestParser.test(input, expect, 224))
    def test_wrong_miss_close5(self):
        input = """class X{
        int[2]m;
         void X(){
         m:={1,2;}}"""
        expect = "Error on line 4 col 16: ;"
        self.assertTrue(TestParser.test(input, expect, 225))
    def test_wrong_miss_close6(self):
        input = """class X{
        void print(int a; float b{}}"""
        expect = "Error on line 2 col 33: {"
        self.assertTrue(TestParser.test(input, expect, 226))
    def test_wrong_miss_close7(self):
        input = """class X{
        void X(){}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 227))
    def test_wrong_miss_close8(self):
        input = """class X{
        int a;
        void X(){ this.a=((5*8)-123;}"""
        expect = "Error on line 3 col 24: ="
        self.assertTrue(TestParser.test(input, expect, 228))
    def test_wrong_miss_close9(self):
        input = """class X{
        void print(string str){io.writeString(str);}
        void main(){this.print(\"str\");}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 229))
    def test_wrong_miss_close10(self):
        input = """classX{
        void print(string str){io.writeString(str);}
        void main(){this.print("";}}"""
        expect = "Error on line 1 col 0: classX"
        self.assertTrue(TestParser.test(input, expect, 230))


    def test_literal1(self):
        """StringLit and ArrayLit"""
        input = """class Lit{
        void main(){
        string A;
        A:=\"my name\";}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231))
    def test_literal2(self):
        input = """class Lit{
        void main(){
        string A;
        A:="This is a string containing tab \t";}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 232))
    def test_literal3(self):
        input = """class Lit{
        void main(){
        string A;
        A:="He asked me: \\\"Where is John?\\\"";}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 233))
    def test_literal4(self):
        input = """class Lit{
        void main(){
        string A;
        A:=\"The comment starts with \\\\\";}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 234))
    def test_literal5(self):
        input = """class Lit{
        void main(){
        string A;
        A:="Open the string;}}"""
        expect = "\"Open the string;}}"
        self.assertTrue(TestParser.test(input, expect, 235))
    def test_literal6(self):
        input = """class Lit{
        void main(){
        string[1] A;
        A:={"A\n"};}}"""
        expect = "\"A"
        self.assertTrue(TestParser.test(input, expect, 236))
    def test_literal7(self):
        input = """class Lit{
        void main(){
        string[1] A;
        A:={\"\t\b\f\"};}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 237))
    def test_literal8(self):
        input = """class Lit{
        void main(){
        string[1] A;
        A:={"\\\\"};}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 238))
    def test_literal9(self):
        input = """class Lit{
        void main(){
        string[1] A;
        A:={\"\\"\\"\"};}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 239))
    def test_literal10(self):
        input = """class Lit{
        void main(){
        int[2] A;
        A:={1.2,6};}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 240))
    def test_extends1(self):
        """inheritance"""
        input = """class A{int b;}
        class B extends A{ int d;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 241))
    def test_extends2(self):
        input = """class A{int b;}
        class B extends A{ int d;"""
        expect = "Error on line 2 col 33: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 242))
    def test_extends3(self):
        input = """class A{int x;}
        class B{int y;}
        class C extends A,B{ int d;}"""
        expect = "Error on line 3 col 25: ,"
        self.assertTrue(TestParser.test(input, expect, 243))
    def test_extends4(self):
        input = """class A{int b;}
        class B extends A{ int d;}
        class C extends B{int k;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 244))
    def test_extends5(self):
        input = """class A{void x(){}}
        class B extends A{void main(){this.x();}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 245))
    def test_extends6(self):
        input = """class A{void x(){}}
        class B extends A{void x(){/*cmt*/}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 246))
    def test_extends7(self):
        input = """class A{void x(){}}
        class B extends A{void x(){#cmt
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 247))
    def test_extends8(self):
        input = """class A{void x(){}}
        class B extends A{void x(){io.writeInt(4+5);}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 248))
    def test_extends9(self):
        input = """class A{void x(){}}
        class B extends A{void print(){io.writeInt(4+5);}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 249))
    def test_extends10(self):
        input = """class A{void x(){}}
        class B extends A{void main(){int a:=7;}}"""
        expect = "Error on line 2 col 43: :="
        self.assertTrue(TestParser.test(input, expect, 250))


    def test_exp10(self):
        """test the expression"""
        input = """class A{
        void main(){float m;
        m:= 1*3/5        ;
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 251))
    def test_exp1(self):
        input = """class A{
        void main(){float m;
        m:=  (1*3)/5       ;
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 252))
    def test_exp2(self):
        input = """class A{
        void main(){float m;
        m:=    (1--5*9)+9     ;
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 253))
    def test_exp3(self):
        input = """class A{
        void main(){float m;
        m:=   4*5/3\\6+1      ;
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 254))
    def test_exp4(self):
        input = """class A{
        int var;
        void main(){float m;
        m:=    var*9-7     ;
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 255))
    def test_exp5(self):
        input = """class A{
        void main(){float m;
        m:=   (1*7)-(5*9)+1.6*50.1      ;
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 256))
    def test_exp6(self):
        input = """class A{
        void main(){float m;
        m:=  x.m(b[2])       ;
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 257))
    def test_exp7(self):
        input = """class A{
        void main(){float m;
        m:=   x.m(b[1*3+4-9*1.3]) - this.kd      ;
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 258))
    def test_exp8(self):
        input = """class A{
        void main(){float m;
        m:=    x.arr[1000]-(x.b(100)*30;     ;
        }}"""
        expect = "Error on line 3 col 39: ;"
        self.assertTrue(TestParser.test(input, expect, 259))
    def test_exp9(self):
        """We need """
        input = """class A{
        void main(){float m;
        m:=   new A      ;
        }}"""
        expect = "Error on line 3 col 25: ;"
        self.assertTrue(TestParser.test(input, expect, 260))

    def test_for_to_do_break1(self):
        """test the loop components"""
        input = """class A{
        void main(){
        for i:= 1 to 100 +j*5/4do {
        
        }
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 261))
    def test_for_to_do_break2(self):
        input = """class A{
        int[100]k;
        void main(){
        for i:= a||b to 100-56*1 do {
        k[i]:=i;
        }
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 262))
    def test_for_to_do_break3(self):
        input = """class A{
        void main(){
        for i:= a==t to 100 do {
        #a line cmt
        /*i:=1000*/
        i:=i+1;
        }
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 263))
    def test_for_to_do_break4(self):
        input = """class A{
        void main(){
        for i:= a.k[3] to 100 do {
            if i%2==0 then i:=i*2;
        }
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 264))
    def test_for_to_do_break5(self):
        input = """class A{
        void main(){
        for i:= 1 to a.[3] do {
        i:=1000;
        io.writeInt(i);
        break;
        }
        }}"""
        expect = "Error on line 3 col 23: ["
        self.assertTrue(TestParser.test(input, expect, 265))
    def test_for_to_do_break6(self):
        input = """class A{
        void main(){
        for i:= 1 to 100 do {
        io.writeInt(i);
            break;
        }
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 266))
    def test_for_to_do_break7(self):
        input = """class A{
        void main(){
        for i:= 1 to 100 do {
            i:=i"123";
        }
        }}"""
        expect = """Error on line 4 col 16: \"123\""""
        self.assertTrue(TestParser.test(input, expect, 267))
    def test_for_to_do_break8(self):
        input = """class A{
        int m(){}
        void main(){
        A x;
        for i:= 1 downto 100 do {
            x.m();
            continue;
        }
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 268))
    def test_for_to_do_break9(self):
        input = """class A{
        void main(){
        for i:= 1 to 100 do 
            io.writeInt(i*2);
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 269))
    def test_for_to_do_break10(self):
        input = """class A{
        void main(){
        for i:= 1 to 100.6 do;
        }}"""
        expect = "Error on line 3 col 29: ;"
        self.assertTrue(TestParser.test(input, expect, 270))

    def test_if_else1(self):
        input = """class A{
        void main(){
        boolean x;
        if x then x:=true;
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 271))
    def test_if_else2(self):
        input = """class A{
        void main(){
        boolean x;
        if x then io.writeInt(100);
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 272))
    def test_if_else3(self):
        input = """class A{
        void main(){
        boolean x;
        if x then if x then if m==6 then m:=1000;
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 273))
    def test_if_else4(self):
        input = """class A{
        void main(){
        boolean x;
        if x then if y x:=False;
        else x:=true;
        }}"""
        expect = "Error on line 4 col 23: x"
        self.assertTrue(TestParser.test(input, expect, 274))
    def test_if_else5(self):
        input = """class A{
        void main(){
        boolean x;
        if x then if(this.m==7)then x:=true;
        else io.writeInt(100);
        else io.writeInt(1);
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 275))
    def test_if_else6(self):
        input = """class A{
        void main(){
        bool x;
        if x then for i:=1 to 2 do io.writeInt(i);
        else io.writeInt(2);
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 276))
    def test_if_else7(self):
        input = """class A{
        void main(){
        boolean x;
        if x then x.m(5);
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 277))
    def test_if_else8(self):
        input = """class A{
        void main(){
        bool x;
        if x then x:={1,2,3};
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 278))
    def test_if_else9(self):
        input = """class A{
        void main(){
        bool x;
        if x then io.readInt(x);
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 279))
    def test_if_else10(self):
        input = """class A{
        void main(){
        bool x;
        if x then io.readBool(x);
        else io.writeBool(x);
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 280))



    def test_mixed_statement1(self):
        input = """class A{
        #this is a cmt
        int a=4+5;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 281))
    def test_mixed_statement2(self):
        input = """ class A{
        # cmt contain illegal escape \p
        int main(){
        io.writeString("legal");
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 282))
    def test_mixed_statement3(self):
        input = """
        class A{int x;
        }
        #cmt"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 283))
        #''''"""constructor"""
    def test_mixed_statement4(self):
        input = """class A{
        A(){}
        A(string x,y; int m){}
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 284))
    def test_mixed_statement5(self):
        input = """class Shape {
float length,width;
float getArea() {}
Shape(float length,width){
this.length := length;
this.width := width;
}
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 285))
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
return this.length*this.width / 2;
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 286))
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 287))
    def test_mixed_statement8(self):
        input = """class X{
        int[100] Intarray;
        X(){
        for i := 1 to 100 do {
io.writeIntLn(i);
Intarray[i] := i + 1;
}
for x := 5 downto 2 do
io.writeIntLn(x);
}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 288))
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 289))
    def test_mixed_statement10(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 290))
















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
      if arr[i] == arr[j]{
        io.writeString("First repeating integer is ");
         io.writeInt(arr[i]);
      }
}}"""
        expect = "Error on line 11 col 25: {"
        self.assertTrue(TestParser.test(input, expect, 291))
        """P of triangle"""
    def test_sample2(self):
        input = """class A{
        int main(){
        io.writeInt(io.readInt(x)+io.readInt(x)+io.readInt(x));
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 292))

        """Sum of n"""
    def test_sample3(self):
        input = """class A{
        int main(){
        int x,sum;
        sum:=0;
        io.readInt(x);
        for i:=1 to x do sum:=sum+i;
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 293))
        """sum of two ints"""
    def test_sample4(self):
        input = """class A{
        int main(){
        int x,y;
        io.readInt(x);
        io.readInt(y);
        io.writeInt(x+y);
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 294))
        """cmt in main"""
    def test_sample5(self):
        input = """class A{
        int main(){
        int x,y;
        io.readInt(x);
        io.readInt(y);
        # this is a line cmt
        /* and an unterminated cmt
        }}"""
        expect = "Error on line 7 col 8: /"
        self.assertTrue(TestParser.test(input, expect, 295))
        """array to int"""
    def test_sample6(self):
        input = """class A{
        int main(){
        int[3] x;
        int sum; sum:=0;
        for i:=1 to n do sum := sum*10+io.readInt(x[i]);
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 296))
        """flip sign"""
    def test_sample7(self):
        input = """class A{
        int main(){
        int x;
        io.readInt(x);
        io.writeInt(-x);
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 297))
        """mod 3"""
    def test_sample8(self):
        input = """class A{
        int main(){
        int x;
        io.readInt(x);
        io.writeInt(x%3);
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 298))
        """rec class"""
    def test_sample9(self):
        input = """class rec{
        int w,b;
        int main(){
        io.readInt(this.w);
        io.readInt(this.b);
        io.writeInt(w*b);
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 299))
        """write your name"""
    def test_sample10(self):
        input = """class A{
        int main(){
        string x;
        io.readString(x);
        io.writeString(\"Your name is\");
        io.writeString(x);
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 300))







