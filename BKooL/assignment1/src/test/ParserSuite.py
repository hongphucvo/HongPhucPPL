
import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: 1 stm """
        input = """class A{int main(){}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
        input = """class A{int main(){
  return 0;}
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))
        input = """class A{int main(){
  float number, root;
  }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))
        input = """class A{
int main(){
final float number = 7.0, root=2.3;}
}"""
        expect = "Error on line 3 col 19: ="
        self.assertTrue(TestParser.test(input, expect, 204))
        input = """class A{int main(){
static float number=9.0; int root;}
}"""
        expect = "Error on line 2 col 0: static"
        self.assertTrue(TestParser.test(input, expect, 205))
        input = """class A{static int main(){
float number=7.3, root;}
}"""
        expect = "Error on line 2 col 12: ="
        self.assertTrue(TestParser.test(input, expect, 206))
        input = """class A{int main(){
  float number = root;}
}"""
        expect = "Error on line 2 col 15: ="
        self.assertTrue(TestParser.test(input, expect, 207))
        input = """class A{int main(){
  io.writeFloat(root);}
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))
        input = """class A{int main(){
  io.writeFloat(7*9-10);}
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 209))
        input = """class A{int main(){
        #This is a line cmt
}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))

    def test_class_dcl(self):
        """only class declaration"""
        input = """class School{ int longitude,latitude;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 211))
        input = """class School{ int longitude,latitude;"""
        expect = "Error on line 1 col 37: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 212))
        input = """class School{int id;}
        class Faculty { int id;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))
        input = """class School{
        int id;
        void print(){io.writeInt(this.id);}"""
        expect = "Error on line 3 col 43: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 214))
        input = """class School{
        int 0id;
        void print(){io.writeInt(this.id);}"""
        expect = "Error on line 2 col 12: 0"
        self.assertTrue(TestParser.test(input, expect, 215))
        input = """class School{
        int id;
        void print(){io.writeInt(this.id);}
        class Faculty{int id;}
        """
        expect = "Error on line 4 col 8: class"
        self.assertTrue(TestParser.test(input, expect, 216))
        input = """class School{
        int id;
        void print(){}}
        class Faculty{int id;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 217))
        input = """class School{
        int id;
        void print(){io.writeInt(this.id);}
        }
        class Faculty{int id; void main(){return 0;}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))
        input = """class School{
        int id;
        void print(){
        int a=100;
        io.writeInt(a);}
        }"""
        expect = "Error on line 4 col 13: ="
        self.assertTrue(TestParser.test(input, expect, 219))
        input = """class School{
        int _id;
        void print(){
        io.writeInt(this.id);
        int a;}
        }"""
        expect = "Error on line 5 col 8: int"
        self.assertTrue(TestParser.test(input, expect, 220))

    def test_wrong_miss_close(self):
        """Bracket close"""
        input = """class A{int main(){}"""
        expect = "Error on line 1 col 20: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 221))
        input = """class exp{
        final int k=(1+3*(4-7));}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 222))
        input = """class exp{
        int a;
        void print(){"""
        expect = "Error on line 3 col 21: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 223))
        input = """class A{int main(){ m.print(;}}"""
        expect = "Error on line 1 col 28: ;"
        self.assertTrue(TestParser.test(input, expect, 224))
        input = """class X{
        int[2]m;
         void X(){
         m:={1,2;}}"""
        expect = "Error on line 4 col 16: ;"
        self.assertTrue(TestParser.test(input, expect, 225))
        input = """class X{
        void print(int a; float b{}}"""
        expect = "Error on line 2 col 33: {"
        self.assertTrue(TestParser.test(input, expect, 226))
        input = """class X{
        void X(){}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 227))
        input = """class X{
        int a;
        void X(){ this.a=((5*8)-123;}"""
        expect = "Error on line 3 col 24: ="
        self.assertTrue(TestParser.test(input, expect, 228))
        input = """class X{
        void print(string str){io.writeString(str);}
        void main(){this.print(\"str\");}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 229))
        input = """classX{
        void print(string str){io.writeString(str);}
        void main(){this.print("";}}"""
        expect = "Error on line 1 col 0: classX"
        self.assertTrue(TestParser.test(input, expect, 230))


    def test_literal(self):
        """StringLit and ArrayLit"""
        input = """class Lit{
        void main(){
        string A;
        A:=\"my name\";}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231))
        input = """class Lit{
        void main(){
        string A;
        A:="This is a string containing tab \t";}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 232))
        input = """class Lit{
        void main(){
        string A;
        A:="He asked me: \\\"Where is John?\\\"";}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 233))
        input = """class Lit{
        void main(){
        string A;
        A:=\"The comment starts with \\\\\";}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 234))
        input = """class Lit{
        void main(){
        string A;
        A:="Open the string;}}"""
        expect = "\"Open the string;}}"
        self.assertTrue(TestParser.test(input, expect, 235))
        input = """class Lit{
        void main(){
        string[1] A;
        A:={"A\n"};}}"""
        expect = "\"A\n"
        self.assertTrue(TestParser.test(input, expect, 236))
        input = """class Lit{
        void main(){
        string[1] A;
        A:={\"\t\b\f\"};}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 237))
        input = """class Lit{
        void main(){
        string[1] A;
        A:={"\\\\"};}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 238))
        input = """class Lit{
        void main(){
        string[1] A;
        A:={\"\\"\\"\"};}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 239))
        input = """class Lit{
        void main(){
        int[2] A;
        A:={1.2,6};}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 240))
    def test_extends(self):
        """inheritance"""
        input = """class A{int b;}
        class B extends A{ int d;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 241))
        input = """class A{int b;}
        class B extends A{ int d;"""
        expect = "Error on line 2 col 33: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 242))
        input = """class A{int x;}
        class B{int y;}
        class C extends A,B{ int d;}"""
        expect = "Error on line 3 col 25: ,"
        self.assertTrue(TestParser.test(input, expect, 243))
        input = """class A{int b;}
        class B extends A{ int d;}
        class C extends B{int k;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 244))
        input = """class A{void x(){}}
        class B extends A{void main(){this.x();}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 245))
        input = """class A{void x(){}}
        class B extends A{void x(){/*cmt*/}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 246))
        input = """class A{void x(){}}
        class B extends A{void x(){#cmt
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 247))
        input = """class A{void x(){}}
        class B extends A{void x(){io.writeInt(4+5);}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 248))
        input = """class A{void x(){}}
        class B extends A{void print(){io.writeInt(4+5);}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 249))
        input = """class A{void x(){}}
        class B extends A{void main(){int a:=7;}}"""
        expect = "Error on line 2 col 43: :="
        self.assertTrue(TestParser.test(input, expect, 250))
    def test_exp(self):
        """test the expression"""
        input = """class A{
        void main(){float m;
        m:= 1*3/5        ;
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 251))
        input = """class A{
        void main(){float m;
        m:=  (1*3)/5       ;
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 252))
        input = """class A{
        void main(){float m;
        m:=    (1--5*9)+9     ;
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 253))
        input = """class A{
        void main(){float m;
        m:=   4*5/3\ 6+1      ;
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 254))
        input = """class A{
        int var;
        void main(){float m;
        m:=    var*9-7     ;
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 255))
        input = """class A{
        void main(){float m;
        m:=   (1*7)-(5*9)+1.6*50.1      ;
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 256))
        input = """class A{
        void main(){float m;
        m:=  x.m(b[2])       ;
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 257))
        input = """class A{
        void main(){float m;
        m:=   x.m(b[1*3+4-9*1.3]) - this.kd      ;
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 258))
        input = """class A{
        void main(){float m;
        m:=    x.arr[1000]-(x.b(100)*30;     ;
        }}"""
        expect = "Error on line 3 col 39: ;"
        self.assertTrue(TestParser.test(input, expect, 259))
        input = """class A{
        void main(){float m;
        m:=   new A      ;
        }}"""
        expect = "Error on line 3 col 25: ;"
        self.assertTrue(TestParser.test(input, expect, 260))

    def test_for_to_do_break(self):
        """test the loop components"""
        input = """class A{
        void main(){
        for i:= 1 to 100 do {
        
        }
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 261))
        input = """class A{
        int[100]k;
        void main(){
        for i:= 1 to 100 do {
        k[i]:=i;
        }
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 262))
        input = """class A{
        void main(){
        for i:= 1 to 100 do {
        #a line cmt
        /*i:=1000*/
        i:=i+1;
        }
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 263))
        input = """class A{
        void main(){
        for i:= 1 to 100 do {
            if i%2==0 then i:=i*2;
        }
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 264))
        input = """class A{
        void main(){
        for i:= 1 to 100 do {
        i:=1000;
        io.writeInt(i);
        break;
        }
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 265))
        input = """class A{
        void main(){
        for i:= 1 to 100 do {
        io.writeInt(i);
            break;
        }
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 266))
        input = """class A{
        void main(){
        for i:= 1 to 100 do {
            i:=i"123";
        }
        }}"""
        expect = """Error on line 4 col 16: \"123\""""
        self.assertTrue(TestParser.test(input, expect, 267))
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
        input = """class A{
        void main(){
        for i:= 1 to 100 do 
            io.writeInt(i*2);
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 269))
        input = """class A{
        void main(){
        for i:= 1 to 100.6 do;
        }}"""
        expect = "Error on line 3 col 29: ;"
        self.assertTrue(TestParser.test(input, expect, 270))

    def test_if_else(self):
        input = """class A{
        void main(){
        boolean x;
        if x then x:=True;
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 271))
        input = """class A{
        void main(){
        boolean x;
        if x then io.writeInt(100);
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 272))
        input = """class A{
        void main(){
        boolean x;
        if x then if x then if m==6 then m:=1000;
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 273))
        input = """class A{
        void main(){
        boolean x;
        if x then if y x:=False;
        else x:=True;
        }}"""
        expect = "Error on line 4 col 23: x"
        self.assertTrue(TestParser.test(input, expect, 274))
        input = """class A{
        void main(){
        boolean x;
        if x then if(this.m==7)then x:=True;
        else io.writeInt(100);
        else io.writeInt(1);
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 275))
        input = """class A{
        void main(){
        bool x;
        if x then for i:=1 to 2 do io.writeInt(i);
        else io.writeInt(2);
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 276))
        input = """class A{
        void main(){
        boolean x;
        if x then x.m(5);
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 277))
        input = """class A{
        void main(){
        bool x;
        if x then x:={1,2,3};
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 278))
        input = """class A{
        void main(){
        bool x;
        if x then io.readInt(x);
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 279))
        input = """class A{
        void main(){
        bool x;
        if x then io.readBool(x);
        else io.writeBool(x);
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 280))



    def test_mixed_statement(self):
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 281))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 282))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 283))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 284))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 285))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 286))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 287))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 288))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 289))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 290))
















    def test_sample(self):
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
        input = """class A{
        int main(){
        io.writeInt(io.readInt(x)+io.readInt(x)+io.readInt(x));
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 292))

        """Sum of n"""
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
        input = """class A{
        int main(){
        int[3] x;
        int sum; sum:=0;
        for i:=1 to n do sum := sum*10+io.readInt(x[i]);
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 296))
        """flip sign"""
        input = """class A{
        int main(){
        int x;
        io.readInt(x);
        io.writeInt(-x);
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 297))
        """mod 3"""
        input = """class A{
        int main(){
        int x;
        io.readInt(x);
        io.writeInt(x%3);
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 298))
        """rec class"""
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
        input = """class A{
        int main(){
        string x;
        io.readString(x);
        io.writeString(\"Your name is\");
        io.writeString(x);
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 300))







