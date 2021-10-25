import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_program1(self):
        input = """class ABC {}"""
        expect = "Program([ClassDecl(Id(ABC),[])])"
        self.assertTrue(TestAST.test(input,expect,201))
    def test_program2(self):
        input = """class ABC extends Object{ }"""
        expect = "Program([ClassDecl(Id(ABC),Id(Object),[])])"
        self.assertTrue(TestAST.test(input,expect,202))
    def test_program3(self):
        input = """
        class ABC extends Character {
            void a;
            int b=5,c;
            int getPowerCombat() {
                return atk + def;
            }
            #static ABC a= new ABC(); 
        }
        """
        expect = "Program([ClassDecl(Id(ABC),Id(Character),[AttributeDecl(Instance,VarDecl(Id(a),VoidType)),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(5))),AttributeDecl(Instance,VarDecl(Id(c),IntType)),MethodDecl(Id(getPowerCombat),Instance,[],IntType,Block([],[Return(BinaryOp(+,Id(atk),Id(def)))]))])])"
        self.assertTrue(TestAST.test(input,expect,203))
    def test_program4(self):
        input = """
        class Hero extends Character {
            Person a = new Person(1,2), b = new Person();
        }
        """
        expect = "Program([ClassDecl(Id(Hero),Id(Character),[AttributeDecl(Instance,VarDecl(Id(a),ClassType(Id(Person)),NewExpr(Id(Person),[IntLit(1),IntLit(2)]))),AttributeDecl(Instance,VarDecl(Id(b),ClassType(Id(Person)),NewExpr(Id(Person),[])))])])"
        self.assertTrue(TestAST.test(input,expect,204))
    def test_program5(self):
        input = """class ABC {
            static int x,y = 0;
            final int My1stCons = 6,My2ndCons = 2;
        }"""
        expect = "Program([ClassDecl(Id(ABC),[AttributeDecl(Static,VarDecl(Id(x),IntType)),AttributeDecl(Static,VarDecl(Id(y),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(My1stCons),IntType,IntLit(6))),AttributeDecl(Instance,ConstDecl(Id(My2ndCons),IntType,IntLit(2)))])])"
        self.assertTrue(TestAST.test(input,expect,205))
    def test_program6(self):
        input = """class Shape {
        static final int numOfShape = 0;
        final int immuAttribute = 0;
        float length,width;
        static int getNumOfShape() {
        return numOfShape;
        }
        }"""
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id(numOfShape),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(immuAttribute),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(length),FloatType)),AttributeDecl(Instance,VarDecl(Id(width),FloatType)),MethodDecl(Id(getNumOfShape),Static,[],IntType,Block([],[Return(Id(numOfShape))]))])])"
        self.assertTrue(TestAST.test(input,expect,206))
    def test_program7(self):
        input = """class Shape {
        int a, b,c;
        float foo(int a){
            return a;
        }
        float foo(int a; float c, d) {
            float v = c + d;
            return v + b.foo(a);
        }
        }"""
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Instance,VarDecl(Id(b),IntType)),AttributeDecl(Instance,VarDecl(Id(c),IntType)),MethodDecl(Id(foo),Instance,[param(Id(a),IntType)],FloatType,Block([],[Return(Id(a))])),MethodDecl(Id(foo),Instance,[param(Id(a),IntType),param(Id(c),FloatType),param(Id(d),FloatType)],FloatType,Block([VarDecl(Id(v),FloatType,BinaryOp(+,Id(c),Id(d)))],[Return(BinaryOp(+,Id(v),CallExpr(Id(b),Id(foo),[Id(a)])))]))])])"
        self.assertTrue(TestAST.test(input,expect,207))
    def test_program8(self):
        input = """class Shape {
        int c;
        foo(){}
        }"""
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Instance,VarDecl(Id(c),IntType)),MethodDecl(Id(<init>),Instance,[],Block([],[]))])])"
        self.assertTrue(TestAST.test(input,expect,208))
    def test_program9(self):
        input = """class Shape {
        int a, b,c;
        float foo(int a; float c, d) {}
        int c,d;
        float goo (float a, b) {}
        }"""
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Instance,VarDecl(Id(b),IntType)),AttributeDecl(Instance,VarDecl(Id(c),IntType)),MethodDecl(Id(foo),Instance,[param(Id(a),IntType),param(Id(c),FloatType),param(Id(d),FloatType)],FloatType,Block([],[])),AttributeDecl(Instance,VarDecl(Id(c),IntType)),AttributeDecl(Instance,VarDecl(Id(d),IntType)),MethodDecl(Id(goo),Instance,[param(Id(a),FloatType),param(Id(b),FloatType)],FloatType,Block([],[]))])])"
        self.assertTrue(TestAST.test(input,expect,209))
    def test_program10(self):
        input = """class Shape {
        void main() {
            int[5] a;
            Object o = 1;
        }
        }"""
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(main),Instance,[],VoidType,Block([VarDecl(Id(a),ArrayType(5,IntType)),VarDecl(Id(o),ClassType(Id(Object)),IntLit(1))],[]))])])"
        self.assertTrue(TestAST.test(input,expect,210))
    def test_program11(self):
        input = """
        class Hero extends Character {
            int a;
            int b=5,c;
            int getPowerCombat() {
                return atk + def;
            }
        }
        """
        expect = "Program([ClassDecl(Id(Hero),Id(Character),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(5))),AttributeDecl(Instance,VarDecl(Id(c),IntType)),MethodDecl(Id(getPowerCombat),Instance,[],IntType,Block([],[Return(BinaryOp(+,Id(atk),Id(def)))]))])])"
        self.assertTrue(TestAST.test(input,expect,211))
    def test_program12(self):
        input = """
        class Hero extends Character {
            void a;
            void check(){
                a := 0 == 1;
            }
        }
        """
        expect = "Program([ClassDecl(Id(Hero),Id(Character),[AttributeDecl(Instance,VarDecl(Id(a),VoidType)),MethodDecl(Id(check),Instance,[],VoidType,Block([],[AssignStmt(Id(a),BinaryOp(==,IntLit(0),IntLit(1)))]))])])"
        self.assertTrue(TestAST.test(input,expect,212))
    def test_program13(self):
        input = """
        class ABC extends Character {
            #start of declaration part
            int a(){
                this.aPI := 3.14;
                value := x.foo(5);
                l[3] := value * 2;
            }
        }
        """
        expect = "Program([ClassDecl(Id(ABC),Id(Character),[MethodDecl(Id(a),Instance,[],IntType,Block([],[AssignStmt(FieldAccess(Self(),Id(aPI)),FloatLit(3.14)),AssignStmt(Id(value),CallExpr(Id(x),Id(foo),[IntLit(5)])),AssignStmt(ArrayCell(Id(l),IntLit(3)),BinaryOp(*,Id(value),IntLit(2)))]))])])"
        self.assertTrue(TestAST.test(input,expect,213))
    def test_program14(self):
        input = """
        class ABC extends Character {
            void main(){
                #start of declaration part
                for x := 5 downto 2 do
                    io.writeIntLn(x);
            }
        }
        """
        expect = "Program([ClassDecl(Id(ABC),Id(Character),[MethodDecl(Id(main),Instance,[],VoidType,Block([],[For(Id(x),IntLit(5),IntLit(2),False,Call(Id(io),Id(writeIntLn),[Id(x)])])]))])])"
        self.assertTrue(TestAST.test(input,expect,214))
    def test_program15(self):
        input = """
        class Example extends _E1{
		Example(int a; float b ){
			int a = 3 == 5 <= 6;
		}
	    }
	    """
        expect = "Program([ClassDecl(Id(Example),Id(_E1),[MethodDecl(Id(<init>),Instance,[param(Id(a),IntType),param(Id(b),FloatType)],Block([VarDecl(Id(a),IntType,BinaryOp(<=,BinaryOp(==,IntLit(3),IntLit(5)),IntLit(6)))],[]))])])"
        self.assertTrue(TestAST.test(input,expect,215))
    def test_program16(self):
        input = """
        class ABC extends Character {
            static int a;
            void b=5,c;
            int getPowerCombat() {
                return atk + def;
            }
            #static ABC a= new ABC(); 
        }
        """
        expect = "Program([ClassDecl(Id(ABC),Id(Character),[AttributeDecl(Static,VarDecl(Id(a),IntType)),AttributeDecl(Instance,VarDecl(Id(b),VoidType,IntLit(5))),AttributeDecl(Instance,VarDecl(Id(c),VoidType)),MethodDecl(Id(getPowerCombat),Instance,[],IntType,Block([],[Return(BinaryOp(+,Id(atk),Id(def)))]))])])"
        self.assertTrue(TestAST.test(input,expect,216))
    def test_program17(self):
        input = """
        class ABC extends Character {
            final void a = 2 + 3, b = 5;
            int b=5,c= b+2;
            int getPowerCombat() {
                return atk + def;
            }
            #static ABC a= new ABC(); 
        }
        """
        expect = "Program([ClassDecl(Id(ABC),Id(Character),[AttributeDecl(Instance,ConstDecl(Id(a),VoidType,BinaryOp(+,IntLit(2),IntLit(3)))),AttributeDecl(Instance,ConstDecl(Id(b),VoidType,IntLit(5))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(5))),AttributeDecl(Instance,VarDecl(Id(c),IntType,BinaryOp(+,Id(b),IntLit(2)))),MethodDecl(Id(getPowerCombat),Instance,[],IntType,Block([],[Return(BinaryOp(+,Id(atk),Id(def)))]))])])"
        self.assertTrue(TestAST.test(input,expect,217))
    def test_program18(self):
        input = """
        class ABC extends Character {
            static final int a = 0;
            int b,c= b+2;
            int getPowerCombat() {
                return atk + def;
            }
            #static ABC a= new ABC(); 
        }
        """
        expect = "Program([ClassDecl(Id(ABC),Id(Character),[AttributeDecl(Static,ConstDecl(Id(a),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(b),IntType)),AttributeDecl(Instance,VarDecl(Id(c),IntType,BinaryOp(+,Id(b),IntLit(2)))),MethodDecl(Id(getPowerCombat),Instance,[],IntType,Block([],[Return(BinaryOp(+,Id(atk),Id(def)))]))])])"
        self.assertTrue(TestAST.test(input,expect,218))
    def test_program19(self):
        input = """
        class ABC extends Character {
            static Shape[10] a;
        }
        """
        expect = "Program([ClassDecl(Id(ABC),Id(Character),[AttributeDecl(Static,VarDecl(Id(a),ArrayType(10,ClassType(Id(Shape)))))])])"
        self.assertTrue(TestAST.test(input,expect,219))
    def test_program20(self):
        input = """
        class ABC extends Character {
            #start of declaration part
            float r,s;
            int[5] a,b;
            #list of statements
        }
        """
        expect = "Program([ClassDecl(Id(ABC),Id(Character),[AttributeDecl(Instance,VarDecl(Id(r),FloatType)),AttributeDecl(Instance,VarDecl(Id(s),FloatType)),AttributeDecl(Instance,VarDecl(Id(a),ArrayType(5,IntType))),AttributeDecl(Instance,VarDecl(Id(b),ArrayType(5,IntType)))])])"
        self.assertTrue(TestAST.test(input,expect,220))
    def test_program21(self):
        input = """
        class ABC extends Character {
            void main(){
                #start of declaration part
                for x := 5 downto 2 do
                    io.writeIntLn(x);
            }
        }
        """
        expect = "Program([ClassDecl(Id(ABC),Id(Character),[MethodDecl(Id(main),Instance,[],VoidType,Block([],[For(Id(x),IntLit(5),IntLit(2),False,Call(Id(io),Id(writeIntLn),[Id(x)])])]))])])"
        self.assertTrue(TestAST.test(input,expect,221))
    def test_program22(self):
        input = """
        class Car {
            string type;
            string model;
            string color;
            int speed;
        
            Car(string type; string model, color) {
                this.type := type;
                this.model := model;
                this.color := color;
            }
            
            int increaseSpeed(int increment) {
                this.speed := this.speed + increment;
                return this.speed;
            }
        }
	    """
        expect = "Program([ClassDecl(Id(Car),[AttributeDecl(Instance,VarDecl(Id(type),StringType)),AttributeDecl(Instance,VarDecl(Id(model),StringType)),AttributeDecl(Instance,VarDecl(Id(color),StringType)),AttributeDecl(Instance,VarDecl(Id(speed),IntType)),MethodDecl(Id(<init>),Instance,[param(Id(type),StringType),param(Id(model),StringType),param(Id(color),StringType)],Block([],[AssignStmt(FieldAccess(Self(),Id(type)),Id(type)),AssignStmt(FieldAccess(Self(),Id(model)),Id(model)),AssignStmt(FieldAccess(Self(),Id(color)),Id(color))])),MethodDecl(Id(increaseSpeed),Instance,[param(Id(increment),IntType)],IntType,Block([],[AssignStmt(FieldAccess(Self(),Id(speed)),BinaryOp(+,FieldAccess(Self(),Id(speed)),Id(increment))),Return(FieldAccess(Self(),Id(speed)))]))])])"
        self.assertTrue(TestAST.test(input,expect,222))
    def test_program23(self):
        input = """
        class ABC extends Character {
            int a, b,c;
            float foo(int a; float c, d) {
            int e ;
            return (a<=c).name + 1;
            }
            float goo (float a, b) {
            return x.foo(1, a, b);
            }
            void main(){
                if ((a > 0) || (b >0)) then
                    io.writeLn("My name is " + this.name);
                else break;
            }
        }
        """
        expect = "Program([ClassDecl(Id(ABC),Id(Character),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Instance,VarDecl(Id(b),IntType)),AttributeDecl(Instance,VarDecl(Id(c),IntType)),MethodDecl(Id(foo),Instance,[param(Id(a),IntType),param(Id(c),FloatType),param(Id(d),FloatType)],FloatType,Block([VarDecl(Id(e),IntType)],[Return(BinaryOp(+,FieldAccess(BinaryOp(<=,Id(a),Id(c)),Id(name)),IntLit(1)))])),MethodDecl(Id(goo),Instance,[param(Id(a),FloatType),param(Id(b),FloatType)],FloatType,Block([],[Return(CallExpr(Id(x),Id(foo),[IntLit(1),Id(a),Id(b)]))])),MethodDecl(Id(main),Instance,[],VoidType,Block([],[If(BinaryOp(||,BinaryOp(>,Id(a),IntLit(0)),BinaryOp(>,Id(b),IntLit(0))),Call(Id(io),Id(writeLn),[BinaryOp(+,StringLit(\"My name is \"),FieldAccess(Self(),Id(name)))]),Break)]))])])"
        self.assertTrue(TestAST.test(input,expect,223))
    def test_program24(self):
        """More complex program"""
        input = """
        class ABC extends abc {
            static int a=5+2,b=6;
            int b,c= b+2;
            A(){}
            static void getPowerCombat(int a, b; int b) {
                return atk + def;
            }
            #static ABC a= new ABC(); 
        }
        """
        expect = "Program([ClassDecl(Id(ABC),Id(abc),[AttributeDecl(Static,VarDecl(Id(a),IntType,BinaryOp(+,IntLit(5),IntLit(2)))),AttributeDecl(Static,VarDecl(Id(b),IntType,IntLit(6))),AttributeDecl(Instance,VarDecl(Id(b),IntType)),AttributeDecl(Instance,VarDecl(Id(c),IntType,BinaryOp(+,Id(b),IntLit(2)))),MethodDecl(Id(<init>),Instance,[],Block([],[])),MethodDecl(Id(getPowerCombat),Static,[param(Id(a),IntType),param(Id(b),IntType),param(Id(b),IntType)],VoidType,Block([],[Return(BinaryOp(+,Id(atk),Id(def)))]))])])"
        self.assertTrue(TestAST.test(input,expect,224))
    def test_program25(self):
        input = """
        class ABC extends Character {
            int a, b,c;
            float foo(int a; float c, d) {
            int e ;
            e := a + 4 ;
            c := a * d / 2.0 ;
            return c + 1;
            }
            float goo (float a, b) {
            return a.foo(1, a, b);
            }
        }
        """
        expect = "Program([ClassDecl(Id(ABC),Id(Character),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Instance,VarDecl(Id(b),IntType)),AttributeDecl(Instance,VarDecl(Id(c),IntType)),MethodDecl(Id(foo),Instance,[param(Id(a),IntType),param(Id(c),FloatType),param(Id(d),FloatType)],FloatType,Block([VarDecl(Id(e),IntType)],[AssignStmt(Id(e),BinaryOp(+,Id(a),IntLit(4))),AssignStmt(Id(c),BinaryOp(/,BinaryOp(*,Id(a),Id(d)),FloatLit(2.0))),Return(BinaryOp(+,Id(c),IntLit(1)))])),MethodDecl(Id(goo),Instance,[param(Id(a),FloatType),param(Id(b),FloatType)],FloatType,Block([],[Return(CallExpr(Id(a),Id(foo),[IntLit(1),Id(a),Id(b)]))]))])])"
        self.assertTrue(TestAST.test(input,expect,225))
    def test_program26(self):
        input = """
        class ABC extends Character {
            int a, b,c;
            float foo(int a; float c, d) {
            int e ;
            e := (a<=b)[2];
            c := a * d / 2.0 ;
            return c + 1;
            }
            float goo (float a, b) {
            return this.foo(1, a, b);
            }
        }
        """
        expect = "Program([ClassDecl(Id(ABC),Id(Character),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Instance,VarDecl(Id(b),IntType)),AttributeDecl(Instance,VarDecl(Id(c),IntType)),MethodDecl(Id(foo),Instance,[param(Id(a),IntType),param(Id(c),FloatType),param(Id(d),FloatType)],FloatType,Block([VarDecl(Id(e),IntType)],[AssignStmt(Id(e),ArrayCell(BinaryOp(<=,Id(a),Id(b)),IntLit(2))),AssignStmt(Id(c),BinaryOp(/,BinaryOp(*,Id(a),Id(d)),FloatLit(2.0))),Return(BinaryOp(+,Id(c),IntLit(1)))])),MethodDecl(Id(goo),Instance,[param(Id(a),FloatType),param(Id(b),FloatType)],FloatType,Block([],[Return(CallExpr(Self(),Id(foo),[IntLit(1),Id(a),Id(b)]))]))])])"
        self.assertTrue(TestAST.test(input,expect,226))
    def test_program27(self):
        input = """
        class Shape {
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
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Instance,VarDecl(Id(length),FloatType)),AttributeDecl(Instance,VarDecl(Id(width),FloatType)),MethodDecl(Id(getArea),Instance,[],FloatType,Block([],[])),MethodDecl(Id(<init>),Instance,[param(Id(length),FloatType),param(Id(width),FloatType)],Block([],[AssignStmt(FieldAccess(Self(),Id(length)),Id(length)),AssignStmt(FieldAccess(Self(),Id(width)),Id(width))]))]),ClassDecl(Id(Rectangle),Id(Shape),[MethodDecl(Id(getArea),Instance,[],FloatType,Block([],[Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))]),ClassDecl(Id(Triangle),Id(Shape),[MethodDecl(Id(getArea),Instance,[],FloatType,Block([],[Return(BinaryOp(/,BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))),IntLit(2)))]))]),ClassDecl(Id(Example2),[MethodDecl(Id(main),Instance,[],VoidType,Block([VarDecl(Id(s),ClassType(Id(Shape)))],[AssignStmt(Id(s),NewExpr(Id(Rectangle),[IntLit(3),IntLit(4)])),Call(Id(io),Id(writeFloatLn),[CallExpr(Id(s),Id(getArea),[])]),AssignStmt(Id(s),NewExpr(Id(Triangle),[IntLit(3),IntLit(4)])),Call(Id(io),Id(writeFloatLn),[CallExpr(Id(s),Id(getArea),[])])]))])])"
        self.assertTrue(TestAST.test(input,expect,227))
    def test_program28(self):
        input = """
        class Example1 {
        int factorial(int n){
        if n == 0 then return 1; else return n * this.factorial(n - 1);
        }
        Example1(){}
        void main(){
        int x;
        x := io.readInt();
        io.writeIntLn(this.factorial(x));
        }
        }
        """
        expect = "Program([ClassDecl(Id(Example1),[MethodDecl(Id(factorial),Instance,[param(Id(n),IntType)],IntType,Block([],[If(BinaryOp(==,Id(n),IntLit(0)),Return(IntLit(1)),Return(BinaryOp(*,Id(n),CallExpr(Self(),Id(factorial),[BinaryOp(-,Id(n),IntLit(1))]))))])),MethodDecl(Id(<init>),Instance,[],Block([],[])),MethodDecl(Id(main),Instance,[],VoidType,Block([VarDecl(Id(x),IntType)],[AssignStmt(Id(x),CallExpr(Id(io),Id(readInt),[])),Call(Id(io),Id(writeIntLn),[CallExpr(Self(),Id(factorial),[Id(x)])])]))])])"
        self.assertTrue(TestAST.test(input,expect,228))
    def test_program29(self):
        input = """
        class Example extends _E1{
		Example(int a; float b ){
			a := new B(1, 2, "a");
            b := this;
		}
	    }
	    """
        expect = "Program([ClassDecl(Id(Example),Id(_E1),[MethodDecl(Id(<init>),Instance,[param(Id(a),IntType),param(Id(b),FloatType)],Block([],[AssignStmt(Id(a),NewExpr(Id(B),[IntLit(1),IntLit(2),StringLit(\"a\")])),AssignStmt(Id(b),Self())]))])])"
        self.assertTrue(TestAST.test(input,expect,229))
    def test_program30(self):
        input = """
        class Example extends _E1{
		Example(int a; float b ){
			int a = 3 == 5 <= 6;
		}
	    }
	    """
        expect = "Program([ClassDecl(Id(Example),Id(_E1),[MethodDecl(Id(<init>),Instance,[param(Id(a),IntType),param(Id(b),FloatType)],Block([VarDecl(Id(a),IntType,BinaryOp(<=,BinaryOp(==,IntLit(3),IntLit(5)),IntLit(6)))],[]))])])"
        self.assertTrue(TestAST.test(input,expect,230))
    def test_program31(self):
        input = """
        class Example{
		void assign(){
            a[3+x.foo(2)] := a[b[2]] +3;
        }
	    }
	    """
        expect = "Program([ClassDecl(Id(Example),[MethodDecl(Id(assign),Instance,[],VoidType,Block([],[AssignStmt(ArrayCell(Id(a),BinaryOp(+,IntLit(3),CallExpr(Id(x),Id(foo),[IntLit(2)]))),BinaryOp(+,ArrayCell(Id(a),ArrayCell(Id(b),IntLit(2))),IntLit(3)))]))])])"
        self.assertTrue(TestAST.test(input,expect,231))
    def test_program32(self):
        input = """
        class Example{
		void assign(){
            x.b[2] := x.m()[3];
        }
	    }
	    """
        expect = "Program([ClassDecl(Id(Example),[MethodDecl(Id(assign),Instance,[],VoidType,Block([],[AssignStmt(ArrayCell(FieldAccess(Id(x),Id(b)),IntLit(2)),ArrayCell(CallExpr(Id(x),Id(m),[]),IntLit(3)))]))])])"
        self.assertTrue(TestAST.test(input,expect,232))
    def test_program33(self):
        input = """
        class Example{
		void assign(){
            (a>=b).c := "Hello World";
        }
	    }
	    """
        expect = "Program([ClassDecl(Id(Example),[MethodDecl(Id(assign),Instance,[],VoidType,Block([],[AssignStmt(FieldAccess(BinaryOp(>=,Id(a),Id(b)),Id(c)),StringLit(\"Hello World\"))]))])])"
        self.assertTrue(TestAST.test(input,expect,233))
    def test_program34(self):
        input = """
        class School{
		void main(){
        }
	    }
	    """
        expect = "Program([ClassDecl(Id(School),[MethodDecl(Id(main),Instance,[],VoidType,Block([],[]))])])"
        self.assertTrue(TestAST.test(input,expect,234))
    def test_program35(self):
        input = """
        class School{
		void main(){
            string s = 1;
            final int a = 0;
        }
	    }
	    """
        expect = "Program([ClassDecl(Id(School),[MethodDecl(Id(main),Instance,[],VoidType,Block([VarDecl(Id(s),StringType,IntLit(1)),ConstDecl(Id(a),IntType,IntLit(0))],[]))])])"
        self.assertTrue(TestAST.test(input,expect,235))
    def test_program36(self):
        input = """
        class Geeks
        {
            string geekname;
            void printname()
            {
            io.writeLn("Hello" ^ "World");
            }
        }
	    """
        expect = """Program([ClassDecl(Id(Geeks),[AttributeDecl(Instance,VarDecl(Id(geekname),StringType)),MethodDecl(Id(printname),Instance,[],VoidType,Block([],[Call(Id(io),Id(writeLn),[BinaryOp(^,StringLit("Hello"),StringLit("World"))])]))])])"""
        self.assertTrue(TestAST.test(input,expect,236))
    def test_program37(self):
        input = """
        class A extends B {
        int main() {
            Geeks obj1;
            obj1.geekname := "Abhi";
            obj1.printname();
            return 0;
        }}
	    """
        expect = "Program([ClassDecl(Id(A),Id(B),[MethodDecl(Id(main),Instance,[],IntType,Block([VarDecl(Id(obj1),ClassType(Id(Geeks)))],[AssignStmt(FieldAccess(Id(obj1),Id(geekname)),StringLit(\"Abhi\")),Call(Id(obj1),Id(printname),[]),Return(IntLit(0))]))])])"
        self.assertTrue(TestAST.test(input,expect,237))
    def test_program38(self):
        input = """
        class School extends Organization{
        final id a;
		School(){}
        School searchSchool(int id){
        if this.id == id then
        return this;
        }
	    }
	    """
        expect = "Program([ClassDecl(Id(School),Id(Organization),[AttributeDecl(Instance,ConstDecl(Id(a),ClassType(Id(id)),None)),MethodDecl(Id(<init>),Instance,[],Block([],[])),MethodDecl(Id(searchSchool),Instance,[param(Id(id),IntType)],ClassType(Id(School)),Block([],[If(BinaryOp(==,FieldAccess(Self(),Id(id)),Id(id)),Return(Self()))]))])])"
        self.assertTrue(TestAST.test(input,expect,238))
    def test_program39(self):
        input = """
        class School{
		float a=0,m=1,x=2,l=3;
	    }
        class Student extends School{}
	    """
        expect = "Program([ClassDecl(Id(School),[AttributeDecl(Instance,VarDecl(Id(a),FloatType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(m),FloatType,IntLit(1))),AttributeDecl(Instance,VarDecl(Id(x),FloatType,IntLit(2))),AttributeDecl(Instance,VarDecl(Id(l),FloatType,IntLit(3)))]),ClassDecl(Id(Student),Id(School),[])])"
        self.assertTrue(TestAST.test(input,expect,239))
    def test_program40(self):
        input = """
        class Dum_Truck {
            Vehicle vehicle = new Dump_Truck(); 
            Dum_Truck(){
                this.vehicle.start_engine(); 
                this.vehicle.drive();        
                this.vehicle.raise_bed(); 
            }
        }
	    """
        expect = "Program([ClassDecl(Id(Dum_Truck),[AttributeDecl(Instance,VarDecl(Id(vehicle),ClassType(Id(Vehicle)),NewExpr(Id(Dump_Truck),[]))),MethodDecl(Id(<init>),Instance,[],Block([],[Call(FieldAccess(Self(),Id(vehicle)),Id(start_engine),[]),Call(FieldAccess(Self(),Id(vehicle)),Id(drive),[]),Call(FieldAccess(Self(),Id(vehicle)),Id(raise_bed),[])]))])])"
        self.assertTrue(TestAST.test(input,expect,240))
    def test_program41(self):
        input = """
        class School{
		void main(){
            final int a = 0;
            for a := 0 to 10 do
            io.print("Hello");
        }
	    }
	    """
        expect = "Program([ClassDecl(Id(School),[MethodDecl(Id(main),Instance,[],VoidType,Block([ConstDecl(Id(a),IntType,IntLit(0))],[For(Id(a),IntLit(0),IntLit(10),True,Call(Id(io),Id(print),[StringLit(\"Hello\")])])]))])])"
        self.assertTrue(TestAST.test(input,expect,241))
    def test_program42(self):
        input = """
        class School{
		bool flag = true, bflag, cflag = new Object();
        bflag(){

        }
	    }
	    """
        expect = "Program([ClassDecl(Id(School),[AttributeDecl(Instance,VarDecl(Id(flag),ClassType(Id(bool)),BooleanLit(True))),AttributeDecl(Instance,VarDecl(Id(bflag),ClassType(Id(bool)))),AttributeDecl(Instance,VarDecl(Id(cflag),ClassType(Id(bool)),NewExpr(Id(Object),[]))),MethodDecl(Id(<init>),Instance,[],Block([],[]))])])"
        self.assertTrue(TestAST.test(input,expect,242))
    def test_program43(self):
        input = """
        class name{
		void main(){
            string s = 1;
            final int m, a = 5+4*a-m;
        }
	    }
	    """
        expect = "Program([ClassDecl(Id(name),[MethodDecl(Id(main),Instance,[],VoidType,Block([VarDecl(Id(s),StringType,IntLit(1)),ConstDecl(Id(m),IntType,None),ConstDecl(Id(a),IntType,BinaryOp(-,BinaryOp(+,IntLit(5),BinaryOp(*,IntLit(4),Id(a))),Id(m)))],[]))])])"
        self.assertTrue(TestAST.test(input,expect,243))
    def test_program44(self):
        input = """
        class classroom{
        void roomnumber = {1,2,3,4};
		Classroom(float a; bool c){}
	    }
	    """
        expect = "Program([ClassDecl(Id(classroom),[AttributeDecl(Instance,VarDecl(Id(roomnumber),VoidType,[IntLit(1),IntLit(2),IntLit(3),IntLit(4)])),MethodDecl(Id(<init>),Instance,[param(Id(a),FloatType),param(Id(c),ClassType(Id(bool)))],Block([],[]))])])"
        self.assertTrue(TestAST.test(input,expect,244))
    def test_program45(self):
        input = """
        class classroom{
        void roomnumber = new Classroom();
		Classroom(float a){
            return a;
        }
	    }
	    """
        expect = "Program([ClassDecl(Id(classroom),[AttributeDecl(Instance,VarDecl(Id(roomnumber),VoidType,NewExpr(Id(Classroom),[]))),MethodDecl(Id(<init>),Instance,[param(Id(a),FloatType)],Block([],[Return(Id(a))]))])])"
        self.assertTrue(TestAST.test(input,expect,245))
    def test_program46(self):
        input = """
        class Rectangle {
            int width, height;
            int area (){
                if (a == b) then {
                    io.print();
                } else {

                }
            }
        } 
	    """
        expect = "Program([ClassDecl(Id(Rectangle),[AttributeDecl(Instance,VarDecl(Id(width),IntType)),AttributeDecl(Instance,VarDecl(Id(height),IntType)),MethodDecl(Id(area),Instance,[],IntType,Block([],[If(BinaryOp(==,Id(a),Id(b)),Block([],[Call(Id(io),Id(print),[])]),Block([],[]))]))])])"
        self.assertTrue(TestAST.test(input,expect,246))
    def test_program47(self):
        input = """
        class Rectangle {
            int width, height;
            void set_values (int a; bool c){
                return b;
            }
            int area (void main){

            }
        }
	    """
        expect = "Program([ClassDecl(Id(Rectangle),[AttributeDecl(Instance,VarDecl(Id(width),IntType)),AttributeDecl(Instance,VarDecl(Id(height),IntType)),MethodDecl(Id(set_values),Instance,[param(Id(a),IntType),param(Id(c),ClassType(Id(bool)))],VoidType,Block([],[Return(Id(b))])),MethodDecl(Id(area),Instance,[param(Id(main),VoidType)],IntType,Block([],[]))])])"
        self.assertTrue(TestAST.test(input,expect,247))
    def test_program48(self):
        input = """
        class Rectangle {
            int width, height;
            void set_values (int a; bool c){
                return b;
            }
            void main(){
                rect.set_values (3,4);
                myarea := rect.area(); 
            }
        }
	    """
        expect = "Program([ClassDecl(Id(Rectangle),[AttributeDecl(Instance,VarDecl(Id(width),IntType)),AttributeDecl(Instance,VarDecl(Id(height),IntType)),MethodDecl(Id(set_values),Instance,[param(Id(a),IntType),param(Id(c),ClassType(Id(bool)))],VoidType,Block([],[Return(Id(b))])),MethodDecl(Id(main),Instance,[],VoidType,Block([],[Call(Id(rect),Id(set_values),[IntLit(3),IntLit(4)]),AssignStmt(Id(myarea),CallExpr(Id(rect),Id(area),[]))]))])])"
        self.assertTrue(TestAST.test(input,expect,248))
    def test_program49(self):
        input = """
        class Student{
		void main(){
            Student s1; 
            Student s2; 
            s1.insert(201, "Sonoo");    
            s2.insert(202, "Nakul");    
            s1.display();    
            s2.display();  
            return 0;  
        }
	    }
	    """
        expect = "Program([ClassDecl(Id(Student),[MethodDecl(Id(main),Instance,[],VoidType,Block([VarDecl(Id(s1),ClassType(Id(Student))),VarDecl(Id(s2),ClassType(Id(Student)))],[Call(Id(s1),Id(insert),[IntLit(201),StringLit(\"Sonoo\")]),Call(Id(s2),Id(insert),[IntLit(202),StringLit(\"Nakul\")]),Call(Id(s1),Id(display),[]),Call(Id(s2),Id(display),[]),Return(IntLit(0))]))])])"
        self.assertTrue(TestAST.test(input,expect,249))
    def test_program50(self):
        input = """
        class Employee {    
            int id;
            string name; 
            float salary;  
            void insert(int i; string n; float s)    
                {    
                    id := i;    
                    this.name := n;    
                    this.salary := s;  
                }    
            void display()    
                {    
                    this.print(this.salary);
                }    
        }
	    """
        expect = "Program([ClassDecl(Id(Employee),[AttributeDecl(Instance,VarDecl(Id(id),IntType)),AttributeDecl(Instance,VarDecl(Id(name),StringType)),AttributeDecl(Instance,VarDecl(Id(salary),FloatType)),MethodDecl(Id(insert),Instance,[param(Id(i),IntType),param(Id(n),StringType),param(Id(s),FloatType)],VoidType,Block([],[AssignStmt(Id(id),Id(i)),AssignStmt(FieldAccess(Self(),Id(name)),Id(n)),AssignStmt(FieldAccess(Self(),Id(salary)),Id(s))])),MethodDecl(Id(display),Instance,[],VoidType,Block([],[Call(Self(),Id(print),[FieldAccess(Self(),Id(salary))])]))])])"
        self.assertTrue(TestAST.test(input,expect,250))
    def test_program51(self):
        input = """
        class Rectangle {
            int width, height;
            void set_values (int a; boolean c){
                return b;
            }
            void main(){
                arr[4] r = {1,2,3}; 
            }
        }
	    """
        expect = "Program([ClassDecl(Id(Rectangle),[AttributeDecl(Instance,VarDecl(Id(width),IntType)),AttributeDecl(Instance,VarDecl(Id(height),IntType)),MethodDecl(Id(set_values),Instance,[param(Id(a),IntType),param(Id(c),BoolType)],VoidType,Block([],[Return(Id(b))])),MethodDecl(Id(main),Instance,[],VoidType,Block([VarDecl(Id(r),ArrayType(4,ClassType(Id(arr))),[IntLit(1),IntLit(2),IntLit(3)])],[]))])])"
        self.assertTrue(TestAST.test(input,expect,251))
    def test_program52(self):
        input = """
        class Test {
            string toString(int a, _123){}
        }
	    """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(toString),Instance,[param(Id(a),IntType),param(Id(_123),IntType)],StringType,Block([],[]))])])"
        self.assertTrue(TestAST.test(input,expect,252))
    def test_program53(self):
        input = """
        class Test {
            void main(){
                if a == b then
                io.write("a equals to b");
                else break;
            }
        }
	    """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(main),Instance,[],VoidType,Block([],[If(BinaryOp(==,Id(a),Id(b)),Call(Id(io),Id(write),[StringLit(\"a equals to b\")]),Break)]))])])"
        self.assertTrue(TestAST.test(input,expect,253))
    def test_program54(self):
        input = """
        class Test {
            void main(){
                if a != b then {
                    b := (a-b)[2*3+5];
                }
            }
        }
	    """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(main),Instance,[],VoidType,Block([],[If(BinaryOp(!=,Id(a),Id(b)),Block([],[AssignStmt(Id(b),ArrayCell(BinaryOp(-,Id(a),Id(b)),BinaryOp(+,BinaryOp(*,IntLit(2),IntLit(3)),IntLit(5))))]))]))])])"
        self.assertTrue(TestAST.test(input,expect,254))
    def test_program55(self):
        input = """
        class Test {
            void main(){
                if a != b then {
                    b := (a-b)[2*3+5];
                } else {
                    break;
                }
            }
        }
	    """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(main),Instance,[],VoidType,Block([],[If(BinaryOp(!=,Id(a),Id(b)),Block([],[AssignStmt(Id(b),ArrayCell(BinaryOp(-,Id(a),Id(b)),BinaryOp(+,BinaryOp(*,IntLit(2),IntLit(3)),IntLit(5))))]),Block([],[Break]))]))])])"
        self.assertTrue(TestAST.test(input,expect,255))
    def test_program56(self):
        input = """
        class Test {
            string toString(int a, b){}
        }
        class Test1 extends Test{}
	    """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(toString),Instance,[param(Id(a),IntType),param(Id(b),IntType)],StringType,Block([],[]))]),ClassDecl(Id(Test1),Id(Test),[])])"
        self.assertTrue(TestAST.test(input,expect,256))
    def test_program57(self):
        input = """
        class Test {
            string toString(int a, b){}
        }
        class Test1 extends Test{
            void initData(double len; double brth; double hgt) {
            length := len;
            breadth := brth;
            height := hgt;
            }

            float calculateArea() {
                return length * breadth;
            }

            float calculateVolume() {
                return length * breadth * height;
            }
        }
	    """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(toString),Instance,[param(Id(a),IntType),param(Id(b),IntType)],StringType,Block([],[]))]),ClassDecl(Id(Test1),Id(Test),[MethodDecl(Id(initData),Instance,[param(Id(len),ClassType(Id(double))),param(Id(brth),ClassType(Id(double))),param(Id(hgt),ClassType(Id(double)))],VoidType,Block([],[AssignStmt(Id(length),Id(len)),AssignStmt(Id(breadth),Id(brth)),AssignStmt(Id(height),Id(hgt))])),MethodDecl(Id(calculateArea),Instance,[],FloatType,Block([],[Return(BinaryOp(*,Id(length),Id(breadth)))])),MethodDecl(Id(calculateVolume),Instance,[],FloatType,Block([],[Return(BinaryOp(*,BinaryOp(*,Id(length),Id(breadth)),Id(height)))]))])])"
        self.assertTrue(TestAST.test(input,expect,257))
    def test_program58(self):
        input = """
        class Test {
            int main() {
            # create object of Room class
            Room room1;
            # pass the values of private variables as arguments
            room1.initData(42.5, 30.8, 19.2);
            io.writeStr("Area of Room =  " + room1.calculateArea());
            return 0;
        }
        }
	    """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(main),Instance,[],IntType,Block([VarDecl(Id(room1),ClassType(Id(Room)))],[Call(Id(room1),Id(initData),[FloatLit(42.5),FloatLit(30.8),FloatLit(19.2)]),Call(Id(io),Id(writeStr),[BinaryOp(+,StringLit(\"Area of Room =  \"),CallExpr(Id(room1),Id(calculateArea),[]))]),Return(IntLit(0))]))])])"
        self.assertTrue(TestAST.test(input,expect,258))
    def test_program59(self):
        input = """
        class Test {
            int main() {
            #create object of Room class
            Room room1;
            #pass the values of private variables as arguments
            room1.initData(42.5, 30.8, 19.2);
            io.writeStr("Area of Room =  " + room1.calculateArea());
            return 0;
        }
        }
	    """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(main),Instance,[],IntType,Block([VarDecl(Id(room1),ClassType(Id(Room)))],[Call(Id(room1),Id(initData),[FloatLit(42.5),FloatLit(30.8),FloatLit(19.2)]),Call(Id(io),Id(writeStr),[BinaryOp(+,StringLit(\"Area of Room =  \"),CallExpr(Id(room1),Id(calculateArea),[]))]),Return(IntLit(0))]))])])"
        self.assertTrue(TestAST.test(input,expect,259))
    def test_program60(self):
        input = """
        class Test {
            string toString(int a; float b,c,d; bool e){
                return new Object(a[2]);
            }
        }
	    """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(toString),Instance,[param(Id(a),IntType),param(Id(b),FloatType),param(Id(c),FloatType),param(Id(d),FloatType),param(Id(e),ClassType(Id(bool)))],StringType,Block([],[Return(NewExpr(Id(Object),[ArrayCell(Id(a),IntLit(2))]))]))])])"
        self.assertTrue(TestAST.test(input,expect,260))
    def test_program61(self):
        input = """
        class Test {
            void main(){}
            void main(){
                int i = 0, s = 0;
                for i := 1 to 10 do
                {float c = 1.e3;}
                s := s + i;
            }
        }
	    """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(main),Instance,[],VoidType,Block([],[])),MethodDecl(Id(main),Instance,[],VoidType,Block([VarDecl(Id(i),IntType,IntLit(0)),VarDecl(Id(s),IntType,IntLit(0))],[For(Id(i),IntLit(1),IntLit(10),True,Block([VarDecl(Id(c),FloatType,FloatLit(1000.0))],[])]),AssignStmt(Id(s),BinaryOp(+,Id(s),Id(i)))]))])])"
        self.assertTrue(TestAST.test(input,expect,261))
    def test_program62(self):
        input = """
        class Test {
            void main(){}
            void main(){
                int i = 0, s = 0;
                float c = 1.e3;
                for i := 1 to 10 do
                s := s + i;
            }
        }
	    """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(main),Instance,[],VoidType,Block([],[])),MethodDecl(Id(main),Instance,[],VoidType,Block([VarDecl(Id(i),IntType,IntLit(0)),VarDecl(Id(s),IntType,IntLit(0)),VarDecl(Id(c),FloatType,FloatLit(1000.0))],[For(Id(i),IntLit(1),IntLit(10),True,AssignStmt(Id(s),BinaryOp(+,Id(s),Id(i)))])]))])])"
        self.assertTrue(TestAST.test(input,expect,262))
    def test_program63(self):
        input = """
        class Test {
            void main(){}
            void main(){
                int i = 0, s = 0;
                float c = 1.e3;
                for i := 1 to 10 do
                s := s + i;
                if s != 10 then 
                    {bool flag = true;}
                else continue;
            }
        }
	    """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(main),Instance,[],VoidType,Block([],[])),MethodDecl(Id(main),Instance,[],VoidType,Block([VarDecl(Id(i),IntType,IntLit(0)),VarDecl(Id(s),IntType,IntLit(0)),VarDecl(Id(c),FloatType,FloatLit(1000.0))],[For(Id(i),IntLit(1),IntLit(10),True,AssignStmt(Id(s),BinaryOp(+,Id(s),Id(i)))]),If(BinaryOp(!=,Id(s),IntLit(10)),Block([VarDecl(Id(flag),ClassType(Id(bool)),BooleanLit(True))],[]),Continue)]))])])"
        self.assertTrue(TestAST.test(input,expect,263))
    def test_program64(self):
        input = """
        class Test {
            Test(int a,b; int[5] c) {
                if a.min < c[2] then {
                    a := new Block(a.z, b+d);
                    a := a.v.x.a[1];
                }
                else {
                    this.A := this;
                    this.B := Test.block.function(f, "abc");
                }
            }
        }
	    """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(<init>),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),ArrayType(5,IntType))],Block([],[If(BinaryOp(<,FieldAccess(Id(a),Id(min)),ArrayCell(Id(c),IntLit(2))),Block([],[AssignStmt(Id(a),NewExpr(Id(Block),[FieldAccess(Id(a),Id(z)),BinaryOp(+,Id(b),Id(d))])),AssignStmt(Id(a),ArrayCell(FieldAccess(FieldAccess(FieldAccess(Id(a),Id(v)),Id(x)),Id(a)),IntLit(1)))]),Block([],[AssignStmt(FieldAccess(Self(),Id(A)),Self()),AssignStmt(FieldAccess(Self(),Id(B)),CallExpr(FieldAccess(Id(Test),Id(block)),Id(function),[Id(f),StringLit(\"abc\")]))]))]))])])"
        self.assertTrue(TestAST.test(input,expect,264))
    def test_program65(self):
        input = """
        class Animal {
            # abstract methods
            void move(){}
            void eat(){}

            # concrete method
            void label() {
                System.out.println("Animal's data:");
            }
        }
	    """
        expect = "Program([ClassDecl(Id(Animal),[MethodDecl(Id(move),Instance,[],VoidType,Block([],[])),MethodDecl(Id(eat),Instance,[],VoidType,Block([],[])),MethodDecl(Id(label),Instance,[],VoidType,Block([],[Call(FieldAccess(Id(System),Id(out)),Id(println),[StringLit(\"Animal's data:\")])]))])])"
        self.assertTrue(TestAST.test(input,expect,265))
    def test_program66(self):
        input = """
        class Animal {
            void move(){}
            float a = x.move();

            void label() {
                System.out.println("Animal's data:");
            }
        }
	    """
        expect = "Program([ClassDecl(Id(Animal),[MethodDecl(Id(move),Instance,[],VoidType,Block([],[])),AttributeDecl(Instance,VarDecl(Id(a),FloatType,CallExpr(Id(x),Id(move),[]))),MethodDecl(Id(label),Instance,[],VoidType,Block([],[Call(FieldAccess(Id(System),Id(out)),Id(println),[StringLit(\"Animal's data:\")])]))])])"
        self.assertTrue(TestAST.test(input,expect,266))
    def test_program67(self):
        input = """
        class TestBird {
            static void main(int args) {
                Animal myBird = new Bird();
                myBird.label();
                myBird.move();
                myBird.eat();
            }
        }
        class TestFish {
            static void main(int args) {
                Animal myFish = new Fish();
                myFish.label();
                myFish.move();
                myFish.eat();
            }
        }
	    """
        expect = "Program([ClassDecl(Id(TestBird),[MethodDecl(Id(main),Static,[param(Id(args),IntType)],VoidType,Block([VarDecl(Id(myBird),ClassType(Id(Animal)),NewExpr(Id(Bird),[]))],[Call(Id(myBird),Id(label),[]),Call(Id(myBird),Id(move),[]),Call(Id(myBird),Id(eat),[])]))]),ClassDecl(Id(TestFish),[MethodDecl(Id(main),Static,[param(Id(args),IntType)],VoidType,Block([VarDecl(Id(myFish),ClassType(Id(Animal)),NewExpr(Id(Fish),[]))],[Call(Id(myFish),Id(label),[]),Call(Id(myFish),Id(move),[]),Call(Id(myFish),Id(eat),[])]))])])"
        self.assertTrue(TestAST.test(input,expect,267))
    def test_program68(self):
        input = """
        class Eagle extends Animal{
            void eat() {
                System.out.println("Eats reptiles and amphibians.");
            }
            void sound() {
                System.out.println("Has a high-pitched whistling sound.");
            }
            void fly() {
                System.out.println("Flies up to 10,000 feet.");
            }
        }
	    """
        expect = "Program([ClassDecl(Id(Eagle),Id(Animal),[MethodDecl(Id(eat),Instance,[],VoidType,Block([],[Call(FieldAccess(Id(System),Id(out)),Id(println),[StringLit(\"Eats reptiles and amphibians.\")])])),MethodDecl(Id(sound),Instance,[],VoidType,Block([],[Call(FieldAccess(Id(System),Id(out)),Id(println),[StringLit(\"Has a high-pitched whistling sound.\")])])),MethodDecl(Id(fly),Instance,[],VoidType,Block([],[Call(FieldAccess(Id(System),Id(out)),Id(println),[StringLit(\"Flies up to 10,000 feet.\")])]))])])"
        self.assertTrue(TestAST.test(input,expect,268))
    def test_program69(self):
        input = """
        class Test {
            Object find(int x; float m,n){
                final int[5] a = {1,2,3,4,5};
                return this;
            }
        }
	    """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(find),Instance,[param(Id(x),IntType),param(Id(m),FloatType),param(Id(n),FloatType)],ClassType(Id(Object)),Block([ConstDecl(Id(a),ArrayType(5,IntType),[IntLit(1),IntLit(2),IntLit(3),IntLit(4),IntLit(5)])],[Return(Self())]))])])"
        self.assertTrue(TestAST.test(input,expect,269))
    def test_program70(self):
        input = """
        class List{
            node[10] begin;
            node[100] end;
        }
	    """
        expect = "Program([ClassDecl(Id(List),[AttributeDecl(Instance,VarDecl(Id(begin),ArrayType(10,ClassType(Id(node))))),AttributeDecl(Instance,VarDecl(Id(end),ArrayType(100,ClassType(Id(node)))))])])"
        self.assertTrue(TestAST.test(input,expect,270))
    def test_program71(self):
        input = """
        class Dum_Truck {
            Vehicle vehicle = new Dump_Truck(); 
            Dum_Truck(){
            vehicle.start_engine(); 
            vehicle.drive();        
            vehicle.raise_bed(); 
            }
        }
	    """
        expect = "Program([ClassDecl(Id(Dum_Truck),[AttributeDecl(Instance,VarDecl(Id(vehicle),ClassType(Id(Vehicle)),NewExpr(Id(Dump_Truck),[]))),MethodDecl(Id(<init>),Instance,[],Block([],[Call(Id(vehicle),Id(start_engine),[]),Call(Id(vehicle),Id(drive),[]),Call(Id(vehicle),Id(raise_bed),[])]))])])"
        self.assertTrue(TestAST.test(input,expect,271))
    def test_program72(self):
        input = """
        class List{
            node begin;
            node end;
            List List(){
                if (begin != nil) then
                return this;
            }
        }
	    """
        expect = "Program([ClassDecl(Id(List),[AttributeDecl(Instance,VarDecl(Id(begin),ClassType(Id(node)))),AttributeDecl(Instance,VarDecl(Id(end),ClassType(Id(node)))),MethodDecl(Id(List),Instance,[],ClassType(Id(List)),Block([],[If(BinaryOp(!=,Id(begin),NullLiteral()),Return(Self()))]))])])"
        self.assertTrue(TestAST.test(input,expect,272))
    def test_program73(self):
        input = """
        class Bird{
            void fly(int height) {
                System.out.println("The bird is flying " + height + " feet high.");
            }
            void fly(String name; int height) {
                System.out.println("The " + name + " is flying " + height + " feet high.");
            }
        }
	    """
        expect = "Program([ClassDecl(Id(Bird),[MethodDecl(Id(fly),Instance,[param(Id(height),IntType)],VoidType,Block([],[Call(FieldAccess(Id(System),Id(out)),Id(println),[BinaryOp(+,BinaryOp(+,StringLit(\"The bird is flying \"),Id(height)),StringLit(\" feet high.\"))])])),MethodDecl(Id(fly),Instance,[param(Id(name),ClassType(Id(String))),param(Id(height),IntType)],VoidType,Block([],[Call(FieldAccess(Id(System),Id(out)),Id(println),[BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,StringLit(\"The \"),Id(name)),StringLit(\" is flying \")),Id(height)),StringLit(\" feet high.\"))])]))])])"
        self.assertTrue(TestAST.test(input,expect,273))
    def test_program74(self):
        input = """
        class Fraction{
            Fraction(){
                this.n := n;
                this.d := d;
                a := n/0 +2 - a >= b;
            }
        }
	    """
        expect = "Program([ClassDecl(Id(Fraction),[MethodDecl(Id(<init>),Instance,[],Block([],[AssignStmt(FieldAccess(Self(),Id(n)),Id(n)),AssignStmt(FieldAccess(Self(),Id(d)),Id(d)),AssignStmt(Id(a),BinaryOp(>=,BinaryOp(-,BinaryOp(+,BinaryOp(/,Id(n),IntLit(0)),IntLit(2)),Id(a)),Id(b)))]))])])"
        self.assertTrue(TestAST.test(input,expect,274))
    def test_program75(self):
        input = """
        class Fraction{
            Fraction(){
                this.n := n;
                this.d := d;
                a := n/0 +2 - a >= b;
                c := (a > b) ==  (a / b == 1);
            }
        }
	    """
        expect = "Program([ClassDecl(Id(Fraction),[MethodDecl(Id(<init>),Instance,[],Block([],[AssignStmt(FieldAccess(Self(),Id(n)),Id(n)),AssignStmt(FieldAccess(Self(),Id(d)),Id(d)),AssignStmt(Id(a),BinaryOp(>=,BinaryOp(-,BinaryOp(+,BinaryOp(/,Id(n),IntLit(0)),IntLit(2)),Id(a)),Id(b))),AssignStmt(Id(c),BinaryOp(==,BinaryOp(>,Id(a),Id(b)),BinaryOp(==,BinaryOp(/,Id(a),Id(b)),IntLit(1))))]))])])"
        self.assertTrue(TestAST.test(input,expect,275))
    def test_program76(self):
        input = """
        class Sample{
            float b,c,d = 1;
            string search(string b,c){
                int a,b,c,d,e = 2;		
                a := b+c;
                t := x+y/z*y%d;
                a.foo(a.foo(x,y),z);
                if 1 then 
                    a := 1;
                else
                    b := a;
            }
        }
	    """
        expect = "Program([ClassDecl(Id(Sample),[AttributeDecl(Instance,VarDecl(Id(b),FloatType)),AttributeDecl(Instance,VarDecl(Id(c),FloatType)),AttributeDecl(Instance,VarDecl(Id(d),FloatType,IntLit(1))),MethodDecl(Id(search),Instance,[param(Id(b),StringType),param(Id(c),StringType)],StringType,Block([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),IntType),VarDecl(Id(d),IntType),VarDecl(Id(e),IntType,IntLit(2))],[AssignStmt(Id(a),BinaryOp(+,Id(b),Id(c))),AssignStmt(Id(t),BinaryOp(+,Id(x),BinaryOp(%,BinaryOp(*,BinaryOp(/,Id(y),Id(z)),Id(y)),Id(d)))),Call(Id(a),Id(foo),[CallExpr(Id(a),Id(foo),[Id(x),Id(y)]),Id(z)]),If(IntLit(1),AssignStmt(Id(a),IntLit(1)),AssignStmt(Id(b),Id(a)))]))])])"
        self.assertTrue(TestAST.test(input,expect,276))
    def test_program77(self):
        input = """
        class Dog {
            int _attendance = 0;
            constructor(name birthday) {
                this.name := name;
                this.birthday := birthday;
            }
        }
	    """
        expect = """Program([ClassDecl(Id(Dog),[AttributeDecl(Instance,VarDecl(Id(_attendance),IntType,IntLit(0))),MethodDecl(Id(<init>),Instance,[param(Id(birthday),ClassType(Id(name)))],Block([],[AssignStmt(FieldAccess(Self(),Id(name)),Id(name)),AssignStmt(FieldAccess(Self(),Id(birthday)),Id(birthday))]))])])"""
        self.assertTrue(TestAST.test(input,expect,277))
    def test_program78(self):
        input = """
        class Dog {
            constructor(string name, birthday) {
                this.name[1] := name;
                this.birthday[a<=c] := birthday;
            }
        }
	    """
        expect = "Program([ClassDecl(Id(Dog),[MethodDecl(Id(<init>),Instance,[param(Id(name),StringType),param(Id(birthday),StringType)],Block([],[AssignStmt(ArrayCell(FieldAccess(Self(),Id(name)),IntLit(1)),Id(name)),AssignStmt(ArrayCell(FieldAccess(Self(),Id(birthday)),BinaryOp(<=,Id(a),Id(c))),Id(birthday))]))])])"
        self.assertTrue(TestAST.test(input,expect,278))
    def test_program79(self):
        input = """
        class Dog {
            calcAge() {
                #calculate age using today's date and birthday
                return Date.now() - this.birthday;
            }
            
            bark() {
                return console.log("Woof!");
            }

            updateAttendance() {
                #add a day to the dog's attendance days at the petsitters
                return this._attendance;
            }
        }
	    """
        expect = """Program([ClassDecl(Id(Dog),[MethodDecl(Id(<init>),Instance,[],Block([],[Return(BinaryOp(-,CallExpr(Id(Date),Id(now),[]),FieldAccess(Self(),Id(birthday))))])),MethodDecl(Id(<init>),Instance,[],Block([],[Return(CallExpr(Id(console),Id(log),[StringLit("Woof!")]))])),MethodDecl(Id(<init>),Instance,[],Block([],[Return(FieldAccess(Self(),Id(_attendance)))]))])])"""
        self.assertTrue(TestAST.test(input,expect,279))
    def test_program80(self):
        input = """
        class Dog {
            calcAge() {
                #calculate age using today's date and birthday
                return Date.now() - this.birthday;
            }
        }
	    """
        expect = "Program([ClassDecl(Id(Dog),[MethodDecl(Id(<init>),Instance,[],Block([],[Return(BinaryOp(-,CallExpr(Id(Date),Id(now),[]),FieldAccess(Self(),Id(birthday))))]))])])"
        self.assertTrue(TestAST.test(input,expect,280))
    def test_program81(self):
        input = """
        class TestBird {
            static void main(String _args) {
                Bird myBird = new Bird();

                myBird.fly();
                myBird.fly(10000);
                myBird.fly("eagle", 10000);
            }
        }
	    """
        expect = """Program([ClassDecl(Id(TestBird),[MethodDecl(Id(main),Static,[param(Id(_args),ClassType(Id(String)))],VoidType,Block([VarDecl(Id(myBird),ClassType(Id(Bird)),NewExpr(Id(Bird),[]))],[Call(Id(myBird),Id(fly),[]),Call(Id(myBird),Id(fly),[IntLit(10000)]),Call(Id(myBird),Id(fly),[StringLit("eagle"),IntLit(10000)])]))])])"""
        self.assertTrue(TestAST.test(input,expect,281))
    def test_program82(self):
        input = """
        class Test{
            static void main(String _args) {
                if a then 
                    if a then
                        if a then
                            if a then b:=a;
            }
        }
	    """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(main),Static,[param(Id(_args),ClassType(Id(String)))],VoidType,Block([],[If(Id(a),If(Id(a),If(Id(a),If(Id(a),AssignStmt(Id(b),Id(a))))))]))])])"
        self.assertTrue(TestAST.test(input,expect,282))
    def test_program83(self):
        input = """
        class Test{
            static void main(String _args) {
                this.ID := a[5]*x.foo(1,2,3);
            }
        }
	    """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(main),Static,[param(Id(_args),ClassType(Id(String)))],VoidType,Block([],[AssignStmt(FieldAccess(Self(),Id(ID)),BinaryOp(*,ArrayCell(Id(a),IntLit(5)),CallExpr(Id(x),Id(foo),[IntLit(1),IntLit(2),IntLit(3)])))]))])])"
        self.assertTrue(TestAST.test(input,expect,283))
    def test_program84(self):
        input = """
        class Test extends Test1{
            static void main(String _args) {
                a := a[5]*x.foo(1,2,3);
            }
        }
	    """
        expect = "Program([ClassDecl(Id(Test),Id(Test1),[MethodDecl(Id(main),Static,[param(Id(_args),ClassType(Id(String)))],VoidType,Block([],[AssignStmt(Id(a),BinaryOp(*,ArrayCell(Id(a),IntLit(5)),CallExpr(Id(x),Id(foo),[IntLit(1),IntLit(2),IntLit(3)])))]))])])"
        self.assertTrue(TestAST.test(input,expect,284))
    def test_program85(self):
        input = """
        class Dog{
            def __init__(self name, age){
                self.name := name;
                self.age := age;
            }
        }
	    """
        expect = "Program([ClassDecl(Id(Dog),[MethodDecl(Id(__init__),Instance,[param(Id(name),ClassType(Id(self))),param(Id(age),ClassType(Id(self)))],ClassType(Id(def)),Block([],[AssignStmt(FieldAccess(Id(self),Id(name)),Id(name)),AssignStmt(FieldAccess(Id(self),Id(age)),Id(age))]))])])"
        self.assertTrue(TestAST.test(input,expect,285))
    def test_program86(self):
        input = """
        class PPL {
            float express(float a,b) {
                return a*b\c+4==5;
                return "mdgnskaf";
            }
            boolean express(boolean a,b) {
                return !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!(c == f) && a || !b;
            }
            string express(string a) {
                return a ^ b ^(c ^ d ^ ("abc" ^ _24dha));
            }
            PPL New(int a; float b) {
                if a == 0 then
                    return new New(a,b,c,d,1./2);
                else {
                    if a<1 then
                        return this;
                    else
                        return nil;
                }
            }
        }
	    """
        expect = """Program([ClassDecl(Id(PPL),[MethodDecl(Id(express),Instance,[param(Id(a),FloatType),param(Id(b),FloatType)],FloatType,Block([],[Return(BinaryOp(==,BinaryOp(+,BinaryOp(\,BinaryOp(*,Id(a),Id(b)),Id(c)),IntLit(4)),IntLit(5))),Return(StringLit("mdgnskaf"))])),MethodDecl(Id(express),Instance,[param(Id(a),BoolType),param(Id(b),BoolType)],BoolType,Block([],[Return(BinaryOp(||,BinaryOp(&&,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,BinaryOp(==,Id(c),Id(f))))))))))))))))))))))))))))))))),Id(a)),UnaryOp(!,Id(b))))])),MethodDecl(Id(express),Instance,[param(Id(a),StringType)],StringType,Block([],[Return(BinaryOp(^,BinaryOp(^,Id(a),Id(b)),BinaryOp(^,BinaryOp(^,Id(c),Id(d)),BinaryOp(^,StringLit("abc"),Id(_24dha)))))])),MethodDecl(Id(New),Instance,[param(Id(a),IntType),param(Id(b),FloatType)],ClassType(Id(PPL)),Block([],[If(BinaryOp(==,Id(a),IntLit(0)),Return(NewExpr(Id(New),[Id(a),Id(b),Id(c),Id(d),BinaryOp(/,FloatLit(1.0),IntLit(2))])),Block([],[If(BinaryOp(<,Id(a),IntLit(1)),Return(Self()),Return(NullLiteral()))]))]))])])"""
        self.assertTrue(TestAST.test(input,expect,286))
    def test_program87(self):
        input = """
        class Number {
            void[10000000000] a = new Object(1,2,3,4,5);
        }
	    """
        expect = "Program([ClassDecl(Id(Number),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(10000000000,VoidType),NewExpr(Id(Object),[IntLit(1),IntLit(2),IntLit(3),IntLit(4),IntLit(5)])))])])"
        self.assertTrue(TestAST.test(input,expect,287))
    def test_program88(self):
        input = """
        class Number {
            void[10000000000] a = new Object(1,2,3,4,5);
            void main(){
                a[b[2]*c[3]] := this.value;
                this.value.foo().fooo1().foo2 := a >= b;
            }
        }
	    """
        expect = """Program([ClassDecl(Id(Number),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(10000000000,VoidType),NewExpr(Id(Object),[IntLit(1),IntLit(2),IntLit(3),IntLit(4),IntLit(5)]))),MethodDecl(Id(main),Instance,[],VoidType,Block([],[AssignStmt(ArrayCell(Id(a),BinaryOp(*,ArrayCell(Id(b),IntLit(2)),ArrayCell(Id(c),IntLit(3)))),FieldAccess(Self(),Id(value))),AssignStmt(FieldAccess(CallExpr(CallExpr(FieldAccess(Self(),Id(value)),Id(foo),[]),Id(fooo1),[]),Id(foo2)),BinaryOp(>=,Id(a),Id(b)))]))])])"""
        self.assertTrue(TestAST.test(input,expect,288))
    def test_program89(self):
        input = """
        class Number {
            void[10000000000] a = new Object(1,2,3,4,5);
            void main(){
                a[2*3] := this.value;
                this.value.foo().fooo1().foo2 := a >= b;
            }
            void display(void[5] a,b,c){
                if (a[1] == b[1]) then {
                    io.writeStr(a ^ b ^ c);
                }
            }
        }
	    """
        expect = "Program([ClassDecl(Id(Number),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(10000000000,VoidType),NewExpr(Id(Object),[IntLit(1),IntLit(2),IntLit(3),IntLit(4),IntLit(5)]))),MethodDecl(Id(main),Instance,[],VoidType,Block([],[AssignStmt(ArrayCell(Id(a),BinaryOp(*,IntLit(2),IntLit(3))),FieldAccess(Self(),Id(value))),AssignStmt(FieldAccess(CallExpr(CallExpr(FieldAccess(Self(),Id(value)),Id(foo),[]),Id(fooo1),[]),Id(foo2)),BinaryOp(>=,Id(a),Id(b)))])),MethodDecl(Id(display),Instance,[param(Id(a),ArrayType(5,VoidType)),param(Id(b),ArrayType(5,VoidType)),param(Id(c),ArrayType(5,VoidType))],VoidType,Block([],[If(BinaryOp(==,ArrayCell(Id(a),IntLit(1)),ArrayCell(Id(b),IntLit(1))),Block([],[Call(Id(io),Id(writeStr),[BinaryOp(^,BinaryOp(^,Id(a),Id(b)),Id(c))])]))]))])])"
        self.assertTrue(TestAST.test(input,expect,289))
    def test_program90(self):
        input = """
        class Number {
            void[10000000000] a = new Object(1,2,3,4,5);
            void main(){
                a[b[2]*c[3]] := this.value;
                this.value.foo().fooo1().foo2 := a >= b;
            }
            void display(void[5] a,b,c){
                if (a[1] >= b[1] == c[1]) then{
                    io.writeStr(a ^ b ^ c);
                }
                else return a.x[5];
                for a := 5 to 100 do
                continue;
            }
        }
	    """
        expect = """Program([ClassDecl(Id(Number),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(10000000000,VoidType),NewExpr(Id(Object),[IntLit(1),IntLit(2),IntLit(3),IntLit(4),IntLit(5)]))),MethodDecl(Id(main),Instance,[],VoidType,Block([],[AssignStmt(ArrayCell(Id(a),BinaryOp(*,ArrayCell(Id(b),IntLit(2)),ArrayCell(Id(c),IntLit(3)))),FieldAccess(Self(),Id(value))),AssignStmt(FieldAccess(CallExpr(CallExpr(FieldAccess(Self(),Id(value)),Id(foo),[]),Id(fooo1),[]),Id(foo2)),BinaryOp(>=,Id(a),Id(b)))])),MethodDecl(Id(display),Instance,[param(Id(a),ArrayType(5,VoidType)),param(Id(b),ArrayType(5,VoidType)),param(Id(c),ArrayType(5,VoidType))],VoidType,Block([],[If(BinaryOp(>=,ArrayCell(Id(a),IntLit(1)),BinaryOp(==,ArrayCell(Id(b),IntLit(1)),ArrayCell(Id(c),IntLit(1)))),Block([],[Call(Id(io),Id(writeStr),[BinaryOp(^,BinaryOp(^,Id(a),Id(b)),Id(c))])]),Return(ArrayCell(FieldAccess(Id(a),Id(x)),IntLit(5)))),For(Id(a),IntLit(5),IntLit(100),True,Continue])]))])])"""
        self.assertTrue(TestAST.test(input,expect,290))
    def test_program91(self):
        input = """
        class Audi extends ParentCar {
            int speed=0;
            int gear=1;
            void changeGear( int value){
                gear:=value;
            }
            void speedUp( int increment)
            {
                this.speed:=this.speed+increment;
            }
            void applyBrakes(int decrement)
            {
                speed:=speed-decrement;
            }
            void printStates(){
                io.writeStr("speed:"^ speed ^ "gear:" ^ gear);
            }
            static void main() {
                Audi A6= new Audi();
                A6.speedUp(50);
                A6.printStates();
                A6.changeGear(4);
                A6.SpeedUp(100);
                A6.printStates();
            }
        }
	    """
        expect = """Program([ClassDecl(Id(Audi),Id(ParentCar),[AttributeDecl(Instance,VarDecl(Id(speed),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(gear),IntType,IntLit(1))),MethodDecl(Id(changeGear),Instance,[param(Id(value),IntType)],VoidType,Block([],[AssignStmt(Id(gear),Id(value))])),MethodDecl(Id(speedUp),Instance,[param(Id(increment),IntType)],VoidType,Block([],[AssignStmt(FieldAccess(Self(),Id(speed)),BinaryOp(+,FieldAccess(Self(),Id(speed)),Id(increment)))])),MethodDecl(Id(applyBrakes),Instance,[param(Id(decrement),IntType)],VoidType,Block([],[AssignStmt(Id(speed),BinaryOp(-,Id(speed),Id(decrement)))])),MethodDecl(Id(printStates),Instance,[],VoidType,Block([],[Call(Id(io),Id(writeStr),[BinaryOp(^,BinaryOp(^,BinaryOp(^,StringLit("speed:"),Id(speed)),StringLit("gear:")),Id(gear))])])),MethodDecl(Id(main),Static,[],VoidType,Block([VarDecl(Id(A6),ClassType(Id(Audi)),NewExpr(Id(Audi),[]))],[Call(Id(A6),Id(speedUp),[IntLit(50)]),Call(Id(A6),Id(printStates),[]),Call(Id(A6),Id(changeGear),[IntLit(4)]),Call(Id(A6),Id(SpeedUp),[IntLit(100)]),Call(Id(A6),Id(printStates),[])]))])])"""
        self.assertTrue(TestAST.test(input,expect,291))
    def test_program92(self):
        input = """
        class Car{
            def __init__(){
                self.model := model;
                self.passengers := passengers;
                self.color := color;
                self.speed := speed;
            }
            def accelerate(self m){
                self.speed := self.speed + 2;
                m.print(self.speed);
            }
            void main(){
                bmw := a.Car("BMW", 4, "red", 5);
                ferrari := a.Car("Ferrari", 2, "black", 10);
                ford := a.Car("Ford", 6, "blue", 6);
            }
        }
	    """
        expect = """Program([ClassDecl(Id(Car),[MethodDecl(Id(__init__),Instance,[],ClassType(Id(def)),Block([],[AssignStmt(FieldAccess(Id(self),Id(model)),Id(model)),AssignStmt(FieldAccess(Id(self),Id(passengers)),Id(passengers)),AssignStmt(FieldAccess(Id(self),Id(color)),Id(color)),AssignStmt(FieldAccess(Id(self),Id(speed)),Id(speed))])),MethodDecl(Id(accelerate),Instance,[param(Id(m),ClassType(Id(self)))],ClassType(Id(def)),Block([],[AssignStmt(FieldAccess(Id(self),Id(speed)),BinaryOp(+,FieldAccess(Id(self),Id(speed)),IntLit(2))),Call(Id(m),Id(print),[FieldAccess(Id(self),Id(speed))])])),MethodDecl(Id(main),Instance,[],VoidType,Block([],[AssignStmt(Id(bmw),CallExpr(Id(a),Id(Car),[StringLit("BMW"),IntLit(4),StringLit("red"),IntLit(5)])),AssignStmt(Id(ferrari),CallExpr(Id(a),Id(Car),[StringLit("Ferrari"),IntLit(2),StringLit("black"),IntLit(10)])),AssignStmt(Id(ford),CallExpr(Id(a),Id(Car),[StringLit("Ford"),IntLit(6),StringLit("blue"),IntLit(6)]))]))])])"""
        self.assertTrue(TestAST.test(input,expect,292))
    def test_program93(self):
        input = """
        class Number {
            void[10000000000] a = new Object(1,2,3,4,5);
            void main(){
                a[b[2]*c[3]] := this.value;
                this.value.foo().fooo1().foo2 := a >= b;
            }
            void display(void[5] a,b,c){
                if (a[1] >= b[1] == c[1]) then{
                    io.writeStr(a ^ b ^ c);
                }
                else return a.x[5];
                for a := 5 to 100 do
                continue;
            }
        }
	    """
        expect = """Program([ClassDecl(Id(Number),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(10000000000,VoidType),NewExpr(Id(Object),[IntLit(1),IntLit(2),IntLit(3),IntLit(4),IntLit(5)]))),MethodDecl(Id(main),Instance,[],VoidType,Block([],[AssignStmt(ArrayCell(Id(a),BinaryOp(*,ArrayCell(Id(b),IntLit(2)),ArrayCell(Id(c),IntLit(3)))),FieldAccess(Self(),Id(value))),AssignStmt(FieldAccess(CallExpr(CallExpr(FieldAccess(Self(),Id(value)),Id(foo),[]),Id(fooo1),[]),Id(foo2)),BinaryOp(>=,Id(a),Id(b)))])),MethodDecl(Id(display),Instance,[param(Id(a),ArrayType(5,VoidType)),param(Id(b),ArrayType(5,VoidType)),param(Id(c),ArrayType(5,VoidType))],VoidType,Block([],[If(BinaryOp(>=,ArrayCell(Id(a),IntLit(1)),BinaryOp(==,ArrayCell(Id(b),IntLit(1)),ArrayCell(Id(c),IntLit(1)))),Block([],[Call(Id(io),Id(writeStr),[BinaryOp(^,BinaryOp(^,Id(a),Id(b)),Id(c))])]),Return(ArrayCell(FieldAccess(Id(a),Id(x)),IntLit(5)))),For(Id(a),IntLit(5),IntLit(100),True,Continue])]))])])"""
        self.assertTrue(TestAST.test(input,expect,293))
    def test_program94(self):
        input = """
        class IceCream {
            int total_cost(void self){
                #vanilla ice cream is sold at a discount of half off!
                if self.flavor == "vanilla" then 
                    total_cost := self.numScoops * 5*self.costPerScoop;
                else
                    total_cost := self.numScoops * self.costPerScoop;
                return total_cost;
            }
        }
	    """
        expect = """Program([ClassDecl(Id(IceCream),[MethodDecl(Id(total_cost),Instance,[param(Id(self),VoidType)],IntType,Block([],[If(BinaryOp(==,FieldAccess(Id(self),Id(flavor)),StringLit("vanilla")),AssignStmt(Id(total_cost),BinaryOp(*,BinaryOp(*,FieldAccess(Id(self),Id(numScoops)),IntLit(5)),FieldAccess(Id(self),Id(costPerScoop)))),AssignStmt(Id(total_cost),BinaryOp(*,FieldAccess(Id(self),Id(numScoops)),FieldAccess(Id(self),Id(costPerScoop))))),Return(Id(total_cost))]))])])"""
        self.assertTrue(TestAST.test(input,expect,294))
    def test_program95(self):
        input = """
        class Person{

        }
        class Parent{

        }
        class Children{

        }
	    """
        expect = "Program([ClassDecl(Id(Person),[]),ClassDecl(Id(Parent),[]),ClassDecl(Id(Children),[])])"
        self.assertTrue(TestAST.test(input,expect,295))
    def test_program96(self):
        input = """
        class Number {
            static int x,y,z = 5;
            void main(){
                for i:=x downto -1 do {
                    float s = "Mean";
                    if i == 0 then break;
                }
            }
        }
	    """
        expect = """Program([ClassDecl(Id(Number),[AttributeDecl(Static,VarDecl(Id(x),IntType)),AttributeDecl(Static,VarDecl(Id(y),IntType)),AttributeDecl(Static,VarDecl(Id(z),IntType,IntLit(5))),MethodDecl(Id(main),Instance,[],VoidType,Block([],[For(Id(i),Id(x),UnaryOp(-,IntLit(1)),False,Block([VarDecl(Id(s),FloatType,StringLit("Mean"))],[If(BinaryOp(==,Id(i),IntLit(0)),Break)])])]))])])"""
        self.assertTrue(TestAST.test(input,expect,296))
    def test_program97(self):
        input = """
        class A{
            /* The BKOOL program consists of 
        many class declaration. */
        }
	    """
        expect = "Program([ClassDecl(Id(A),[])])"
        self.assertTrue(TestAST.test(input,expect,297))
    def test_program98(self):
        input = """
            class BowlerClass{
            void bowlingMethod()
            {
            System.out.println(" bowler ");
            }}
            class FastPacer{
            void bowlingMethod()
            {
            System.out.println(" fast bowler ");
            }
            static void main(String[5] args)
            {
            FastPacer obj= new FastPacer();
            obj.bowlingMethod();
            }
            }
        """
        expect = """Program([ClassDecl(Id(BowlerClass),[MethodDecl(Id(bowlingMethod),Instance,[],VoidType,Block([],[Call(FieldAccess(Id(System),Id(out)),Id(println),[StringLit(" bowler ")])]))]),ClassDecl(Id(FastPacer),[MethodDecl(Id(bowlingMethod),Instance,[],VoidType,Block([],[Call(FieldAccess(Id(System),Id(out)),Id(println),[StringLit(" fast bowler ")])])),MethodDecl(Id(main),Static,[param(Id(args),ArrayType(5,ClassType(Id(String))))],VoidType,Block([VarDecl(Id(obj),ClassType(Id(FastPacer)),NewExpr(Id(FastPacer),[]))],[Call(Id(obj),Id(bowlingMethod),[])]))])])"""
        self.assertTrue(TestAST.test(input,expect,298))
    def test_program99(self):
        input = """class A {
            int main(int input) {
                int x = -1, y;
                for i := 0 to list.size() do {
                    for j := 0 to this.len(list.get(i)) do {
                        if list.get(i)[j] == -2 then continue;
                        if list.get(i)[j] == input then {
                            x := i;
                            y := j;
                            break;
                        }
                    }
                }
            }
        }"""
        expect = "Program([ClassDecl(Id(A),[MethodDecl(Id(main),Instance,[param(Id(input),IntType)],IntType,Block([VarDecl(Id(x),IntType,UnaryOp(-,IntLit(1))),VarDecl(Id(y),IntType)],[For(Id(i),IntLit(0),CallExpr(Id(list),Id(size),[]),True,Block([],[For(Id(j),IntLit(0),CallExpr(Self(),Id(len),[CallExpr(Id(list),Id(get),[Id(i)])]),True,Block([],[If(BinaryOp(==,ArrayCell(CallExpr(Id(list),Id(get),[Id(i)]),Id(j)),UnaryOp(-,IntLit(2))),Continue),If(BinaryOp(==,ArrayCell(CallExpr(Id(list),Id(get),[Id(i)]),Id(j)),Id(input)),Block([],[AssignStmt(Id(x),Id(i)),AssignStmt(Id(y),Id(j)),Break]))])])])])]))])])"
        self.assertTrue(TestAST.test(input,expect,299))
    def test_program100(self):
        input = input = """class A {
            final static string a = "Abc", b = "z a@ 1";
        }"""
        expect = """Program([ClassDecl(Id(A),[AttributeDecl(Static,ConstDecl(Id(a),StringType,StringLit("Abc"))),AttributeDecl(Static,ConstDecl(Id(b),StringType,StringLit("z a@ 1")))])])"""
        self.assertTrue(TestAST.test(input,expect,300))
    