import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_program1(self):
        input = """class ABC {}"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,401))
    def test_program2(self):
        input = """class ABC extends Object{ }"""
        expect = "Undeclared Class: Object"
        self.assertTrue(TestChecker.test(input,expect,402))
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
        expect = "Undeclared Class: Character"
        self.assertTrue(TestChecker.test(input,expect,403))
    def test_program4(self):
        input = """
        class Hero extends Character {
            Person a = new Person(1,4), b = new Person();
        }
        """
        expect = "Undeclared Class: Character"
        self.assertTrue(TestChecker.test(input,expect,404))
    def test_program5(self):
        input = """class ABC {
            static int x,y = 0;
            final int My1stCons = 6,My2ndCons = 2;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,405))
    def test_program6(self):
        input = """class Shape {
        static final int numOfShape = 0;
        final int immuAttribute = 0;
        float length,width;
        static int getNumOfShape() {
        return numOfShape;
        }
        }"""
        expect = "Undeclared Identifier: numOfShape"
        self.assertTrue(TestChecker.test(input,expect,406))
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
        expect = "Redeclared Method: foo"
        self.assertTrue(TestChecker.test(input,expect,407))
    def test_program8(self):
        input = """class Shape {
        int c;
        foo(){}
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,408))
    def test_program9(self):
        input = """class Shape {
        int a, b,c;
        float foo(int a; float c, d) {}
        int c,d;
        float goo (float a, b) {}
        }"""
        expect = "Redeclared Attribute: c"
        self.assertTrue(TestChecker.test(input,expect,409))
    def test_program10(self):
        input = """class Shape {
        void main() {
            int[5] a;
            Object o = 1;
        }
        }"""
        expect = "Type Mismatch In Statement: VarDecl(Id(o),ClassType(Id(Object)),IntLit(1))"
        self.assertTrue(TestChecker.test(input,expect,410))
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
        expect = "Undeclared Class: Character"
        self.assertTrue(TestChecker.test(input,expect,411))
    def test_program12(self):
        input = """
        class Hero extends Character {
            void a;
            void check(){
                a := 0 == 1;
            }
        }
        """
        expect = "Undeclared Class: Character"
        self.assertTrue(TestChecker.test(input,expect,412))
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
        expect = "Undeclared Class: Character"
        self.assertTrue(TestChecker.test(input,expect,413))
    def test_program14(self):
        input = """
        class ABC extends Character {
            void main(){
                #start of declaration part
                if x == 5 && 2 then
                    io.writeIntLn(x);
            }
        }
        """
        expect = "Undeclared Class: Character"
        self.assertTrue(TestChecker.test(input,expect,414))
    def test_program15(self):
        input = """
        class Example extends _E1{
		Example(int a; float b ){
			int a = 3 == 5 <= 6;
		}
	    }
	    """
        expect = "Undeclared Class: _E1"
        self.assertTrue(TestChecker.test(input,expect,415))
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
        expect = "Undeclared Class: Character"
        self.assertTrue(TestChecker.test(input,expect,416))
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
        expect = "Undeclared Class: Character"
        self.assertTrue(TestChecker.test(input,expect,417))
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
        expect = "Undeclared Class: Character"
        self.assertTrue(TestChecker.test(input,expect,418))
    def test_program19(self):
        input = """
        class ABC extends Character {
            static Shape[10] a;
        }
        """
        expect = "Undeclared Class: Character"
        self.assertTrue(TestChecker.test(input,expect,419))
    def test_program20(self):
        input = """
        class ABC extends Character {
            #start of declaration part
            float r,s;
            int[5] a,b;
            #list of statements
        }
        """
        expect = "Undeclared Class: Character"
        self.assertTrue(TestChecker.test(input,expect,420))
    def test_program21(self):
        input = """
        class ABC extends Character {
            void main(){
                #start of declaration part
                m := a*b*c+d-m%10;
            }
        }
        """
        expect = "Undeclared Class: Character"
        self.assertTrue(TestChecker.test(input,expect,421))
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
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,422))
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
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,423))
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
        expect = "Undeclared Class: abc"
        self.assertTrue(TestChecker.test(input,expect,424))
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
        expect = "Undeclared Class: Character"
        self.assertTrue(TestChecker.test(input,expect,425))
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
        expect = "Undeclared Class: Character"
        self.assertTrue(TestChecker.test(input,expect,426))
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
        expect = "Illegal Member Access: FieldAccess(Self(),Id(length))"
        self.assertTrue(TestChecker.test(input,expect,427))
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
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,428))
    def test_program29(self):
        input = """
        class Example extends _E1{
		Example(int a; float b ){
			a := new B(1, 2, "a");
            b := this;
		}
	    }
	    """
        expect = "Undeclared Class: _E1"
        self.assertTrue(TestChecker.test(input,expect,429))
    def test_program30(self):
        input = """
        class Example extends _E1{
		Example(int a; float b ){
			int a = 3 == 5 <= 6;
		}
	    }
	    """
        expect = "Undeclared Class: _E1"
        self.assertTrue(TestChecker.test(input,expect,430))
    def test_program31(self):
        input = """
        class Example{
		void assign(){
            a[3+x.foo(2)] := a[b[2]] +3;
        }
	    }
	    """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,431))
    def test_program32(self):
        input = """
        class Example{
		void assign(){
            x.b[2] := x.m()[3];
        }
	    }
	    """
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input,expect,432))
    def test_program33(self):
        input = """
        class Example{
		void assign(){
            (a>=b).c := "Hello World";
        }
	    }
	    """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,433))
    def test_program34(self):
        input = """
        class School{
		void main(){
        }
	    }
	    """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,434))
    def test_program35(self):
        input = """
        class School{
		void main(){
            string s = 1;
            final int a = 0;
        }
	    }
	    """
        expect = "Type Mismatch In Statement: VarDecl(Id(s),StringType,IntLit(1))"
        self.assertTrue(TestChecker.test(input,expect,435))
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
        expect = "Undeclared Method: writeLn"
        self.assertTrue(TestChecker.test(input,expect,436))
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
        expect = "Undeclared Class: B"
        self.assertTrue(TestChecker.test(input,expect,437))
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
        expect = "Undeclared Class: Organization"
        self.assertTrue(TestChecker.test(input,expect,438))
    def test_program39(self):
        input = """
        class School{
		float a=0,m=1,x=2,l=3;
	    }
        class Student extends School{}
	    """
        expect = "Type Mismatch In Statement: VarDecl(Id(a),FloatType,IntLit(0))"
        self.assertTrue(TestChecker.test(input,expect,439))
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
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,440))
    def test_program41(self):
        input = """
        class A {
        final int i = 5;
        static ABC[5] f() {}
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,441))
    def test_program42(self):
        input = """
        class School{
		bool flag = true, bflag, cflag = new Object();
        bflag(){

        }
	    }
	    """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,442))
    def test_program43(self):
        input = """
        class name{
		void main(){
            string s = 1;
            final int m, a = 5+4*a-m;
        }
	    }
	    """
        expect = "Type Mismatch In Statement: VarDecl(Id(s),StringType,IntLit(1))"
        self.assertTrue(TestChecker.test(input,expect,443))
    def test_program44(self):
        input = """
        class classroom{
        void roomnumber = {1,4,3,4};
		Classroom(float a; bool c){}
	    }
	    """
        expect = "Type Mismatch In Statement: VarDecl(Id(roomnumber),VoidType,[])"
        self.assertTrue(TestChecker.test(input,expect,444))
    def test_program45(self):
        input = """
        class classroom{
        void roomnumber = new Classroom();
		Classroom(float a){
            return a;
        }
	    }
	    """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,445))
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
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,446))
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
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,447))
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
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,448))
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
        expect = "Undeclared Method: insert"
        self.assertTrue(TestChecker.test(input,expect,449))
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
        expect = "Undeclared Identifier: id"
        self.assertTrue(TestChecker.test(input,expect,450))
    def test_program51(self):
        input = """
        class Rectangle {
            int width, height;
            void set_values (int a; boolean c){
                return b;
            }
            void main(){
                arr[4] r = {1,4,3}; 
            }
        }
	    """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,451))
    def test_program52(self):
        input = """
        class Test {
            string toString(int a, _123){}
        }
	    """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,452))
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
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,453))
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
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,454))
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
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,455))
    def test_program56(self):
        input = """
        class Test {
            string toString(int a, b){}
        }
        class Test1 extends Test{}
	    """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,456))
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
        expect = "Undeclared Identifier: length"
        self.assertTrue(TestChecker.test(input,expect,457))
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
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,458))
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
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,459))
    def test_program60(self):
        input = """
        class Test {
            string toString(int a; float b,c,d; bool e){
                return new Object(a[2]);
            }
        }
	    """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,460))
    def test_program61(self):
        input = """
        class Test {
            void main(){}
            void main(){
                int i = 0, s = 0;
                {float c = 1.e3;}
                s := s + i;
            }
        }
	    """
        expect = "Redeclared Method: main"
        self.assertTrue(TestChecker.test(input,expect,461))
    def test_program62(self):
        input = """
        class Test {
            void main(){}
            void main(){
                {int i = 0, s = 0;
                float c = 1.e3;
                s := s + i;}
            }
        }
	    """
        expect = "Redeclared Method: main"
        self.assertTrue(TestChecker.test(input,expect,462))
    def test_program63(self):
        input = """
        class Test {
            void main(){}
            void main(){
                int i = 0, s = 0;
                float c = 1.e3;
                i := a.foo(2,3);
                s := s + i;
                if s != 10 then 
                    {bool flag = true;}
                else continue;
            }
        }
	    """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,463))
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
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,464))
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
        expect = "Undeclared Identifier: System"
        self.assertTrue(TestChecker.test(input,expect,465))
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
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input,expect,466))
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
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,467))
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
        expect = "Undeclared Class: Animal"
        self.assertTrue(TestChecker.test(input,expect,468))
    def test_program69(self):
        input = """
        class Test {
            Object find(int x; float m,n){
                final int[5] a = {1,4,3,4,5};
                return this;
            }
        }
	    """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),ArrayType(5,IntType),[])"
        self.assertTrue(TestChecker.test(input,expect,469))
    def test_program70(self):
        input = """
        class List{
            node[10] begin;
            node[100] end;
        }
	    """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,470))
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
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),ArrayType(5,IntType),[])"
        self.assertTrue(TestChecker.test(input,expect,471))
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
        expect = "Undeclared Identifier: begin"
        self.assertTrue(TestChecker.test(input,expect,472))
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
        expect = "Redeclared Method: fly"
        self.assertTrue(TestChecker.test(input,expect,473))
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
        expect = "Undeclared Identifier: n"
        self.assertTrue(TestChecker.test(input,expect,474))
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
        expect = "Undeclared Identifier: n"
        self.assertTrue(TestChecker.test(input,expect,475))
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
        expect = "Type Mismatch In Statement: VarDecl(Id(d),FloatType,IntLit(1))"
        self.assertTrue(TestChecker.test(input,expect,476))
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
        expect = "Undeclared Identifier: name"
        self.assertTrue(TestChecker.test(input,expect,477))
    def test_program78(self):
        input = """
        class Dog {
            constructor(string name, birthday) {
                this.name[1] := name;
                this.birthday[a<=c] := birthday;
            }
        }
	    """
        expect = "Illegal Member Access: FieldAccess(Self(),Id(name))"
        self.assertTrue(TestChecker.test(input,expect,478))
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
        expect = "Illegal Member Access: FieldAccess(Self(),Id(birthday))"
        self.assertTrue(TestChecker.test(input,expect,479))
    def test_program80(self):
        input = """
        class Dog {
            calcAge() {
                #calculate age using today's date and birthday
                return Date.now() - this.birthday;
            }
        }
	    """
        expect = "Illegal Member Access: FieldAccess(Self(),Id(birthday))"
        self.assertTrue(TestChecker.test(input,expect,480))
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
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,481))
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
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,482))
    def test_program83(self):
        input = """
        class Test{
            static void main(String _args) {
                this.ID := a[5]*x.foo(1,4,3);
            }
        }
	    """
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input,expect,483))
    def test_program84(self):
        input = """
        class Test extends Test1{
            static void main(String _args) {
                a := a[5]*x.foo(1,4,3);
            }
        }
	    """
        expect = "Undeclared Class: Test1"
        self.assertTrue(TestChecker.test(input,expect,484))
    def test_program85(self):
        input = """
        class Dog{
            def __init__(self name, age){
                self.name := name;
                self.age := age;
            }
        }
	    """
        expect = "Undeclared Identifier: self"
        self.assertTrue(TestChecker.test(input,expect,485))
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
        expect = "Redeclared Method: express"
        self.assertTrue(TestChecker.test(input,expect,486))
    def test_program87(self):
        input = """
        class Number {
            void[10000000000] a = new Object(1,4,3,4,5);
        }
	    """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,487))
    def test_program88(self):
        input = """
        class Number {
            void[10000000000] a = new Object(1,4,3,4,5);
            void main(){
                a[b[2]*c[3]] := this.value;
                this.value.foo().fooo1().foo2 := a >= b;
            }
        }
	    """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,488))
    def test_program89(self):
        input = """
        class Number {
            void[10000000000] a = new Object(1,4,3,4,5);
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
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,489))
    def test_program90(self):
        input = """
        class Number {
            void[10000000000] a = new Object(1,4,3,4,5);
            void main(){
                a[b[2]*c[3]] := this.value;
                this.value.foo().fooo1().foo2 := a >= b;
            }
            void display(void[5] a,b,c){
                if (a[1] >= b[1] == c[1]) then{
                    io.writeStr(a ^ b ^ c);
                }
                else return a.x[5];
            }
        }
	    """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,490))
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
        expect = "Undeclared Class: ParentCar"
        self.assertTrue(TestChecker.test(input,expect,491))
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
        expect = "Undeclared Identifier: model"
        self.assertTrue(TestChecker.test(input,expect,492))
    def test_program93(self):
        input = """
        class Number {
            void[10000000000] a = new Object(1,4,3,4,5);
            void main(){
                a[b[2]*c[3]] := this.value;
                this.value.foo().fooo1().foo2 := a >= b;
            }
            void display(void[5] a,b,c){
                if (a[1] >= b[1] == c[1]) then{
                    io.writeStr(a ^ b ^ c);
                }
                else return a.x[5];
            }
        }
	    """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,493))
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
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,494))
    def test_program95(self):
        input = """
        class Person{

        }
        class Parent{

        }
        class Children{

        }
	    """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,495))
    def test_program96(self):
        input = """
        class Number {
            static int x,y,z = 5;
            void main(){
                if x >= y + z then {
                    float s = "Mean";
                    if i == 0 then break;
                }
            }
        }
	    """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,496))
    def test_program97(self):
        input = """
        class A{
            /* The BKOOL program consists of 
        many class declaration. */
        }
	    """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,497))
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
        expect = "Undeclared Identifier: System"
        self.assertTrue(TestChecker.test(input,expect,498))
    def test_program99(self):
        input = """class A {
            int main(int input) {
                int x = -1, y;
                final int c;
                c:=a.b().d()[2];
            }
        }"""
        expect = "Illegal Constant Expression: ConstDecl(Id(c),IntType,None)"
        self.assertTrue(TestChecker.test(input,expect,499))
    def test_program100(self):
        input = input = """class A {
            final static string a = "Abc", b = "z a@ 1";
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,500))
    