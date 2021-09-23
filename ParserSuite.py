import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    #======================================= 0-9 ==========================================
    # class declaration
    def test_class_1(self):
        input = """class abc {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 200))
    def test_class_2(self):
        input = """class abc extends D {} """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
    def test_class_3(self):
        input = """class abc extends D,E{}  """
        expect = "Error on line 1 col 19: ,"
        self.assertTrue(TestParser.test(input, expect, 202))
    def test_class_4(self):
        input = """ class abc extends D (int a,b) {} """
        expect = "Error on line 1 col 21: ("
        self.assertTrue(TestParser.test(input, expect, 203))
    def test_class_5(self):
        input = """/*def class*/class A {}\nclass B extends A{};"""
        expect = "Error on line 2 col 19: ;"
        self.assertTrue(TestParser.test(input, expect, 204))
    # attribute and method declaration
    def test_attr_met_1(self):
        input = """class A {
            final static int a;
            static final float b;
            static boolean c;
            final string str;
            int[4] arr;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))
    def test_attr_met_2(self):
        input = """
        class school {
            int a,b,c,d;
            static static int c;
        }"""
        expect = "Error on line 4 col 19: static"
        self.assertTrue(TestParser.test(input, expect, 206))
    def test_attr_met_3(self):
        input = """
        class school {
            static int a = 1 + 2,b;
            final float c;d = 1.0256;
        }"""
        expect = "Error on line 4 col 28: ="
        self.assertTrue(TestParser.test(input, expect, 207))
    def test_attr_met_4(self):
        input = """
        class school {
            int[3] a = {1, 1 + 2, z + b/2, c};
            child a = 1.023e123;
        }"""
        expect = "Error on line 3 col 29: +"
        self.assertTrue(TestParser.test(input, expect, 208))
    def test_attr_met_5(self):
        input = """
        class school {
            class room {}
        }"""
        expect = "Error on line 3 col 12: class"
        self.assertTrue(TestParser.test(input, expect, 209))
    # #======================================= 10-19 ==========================================
    def test_attr_met_6(self):
        input = """
        class school {
            static final b;
        }"""
        expect = "Error on line 3 col 26: ;"
        self.assertTrue(TestParser.test(input, expect, 210))
    def test_attr_met_7(self):
        input = """
        class school {
            static final int a,float b;
        }"""
        expect = "Error on line 3 col 31: float"
        self.assertTrue(TestParser.test(input, expect, 211))
    def test_attr_met_8(self):
        input = """
        class school {
            static checker(int a, b, float c) {}
        }"""
        expect = "Error on line 3 col 26: ("
        self.assertTrue(TestParser.test(input, expect, 212))
    def test_attr_met_9(self):
        input = """
        class school {
            static void checker(int a, b, float c) {
            }
        }"""
        expect = "Error on line 3 col 42: float"
        self.assertTrue(TestParser.test(input, expect, 213))
    def test_attr_met_10(self):
        input = """
        class school {
            static void checker(int a, b; float c) {
            }
            school(int[5] arr) {
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))
    def test_attr_met_11(self):
        input = """
        class school {
            final int a;
            static void checker(int a, b; float c) {
            }
            static a = 2, b = 6;
            school(int[5] arr) {
            }
        }"""
        expect = "Error on line 6 col 21: ="
        self.assertTrue(TestParser.test(input, expect, 215))
    def test_attr_met_12(self):
        input = """
        class school {
            static void checker(int a, b; float c) {
            }
            static float a = 2, b = 6;
            school(int[5] arr) {
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))
    def test_attr_met_13(self):
        input = """
        class school {
            static boolean ID;
            school(int a,b) {}
            void makeSchool() {}
        }
        class University extends school {
            University(a,b) {}
        }"""
        expect = "Error on line 8 col 24: ,"
        self.assertTrue(TestParser.test(input, expect, 217))
    def test_attr_met_14(self):
        input = """
        class student {
            final static school sch;
            final static string ID;
            student(school sch, string ID) {}
            static void getData(string ID) {}
        }"""
        expect = "Error on line 5 col 32: string"
        self.assertTrue(TestParser.test(input, expect, 218))
    def test_attr_met_15(self):
        input = """
        class teacher extends student {
            string[3] getData(boolean a; school D) {}
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 219))
    #======================================= 20-29 ==========================================\
    # test stmt and exp
    def test_assign_stmt(self):
        input = """
        class testData {
            testData(int a; float b) {
                a.b := z + a;
                a.a.b := z + b;
                a.b[1] := 2 + 1 - 1.0023e-12;
                arr := {1,2,3,4};
                a := 1 + 2 - abc;
                a := new Doctor(1,2,3,z,t);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 220))
    def test_if_stmt_1(self):
        input = """
        class testData {
            testData(int a,b; float b) {
                if (a == b) then a := 1;
                if a > b then a : = 2; else a := 2;
            }
        }"""
        expect = "Error on line 5 col 32: :"
        self.assertTrue(TestParser.test(input, expect, 221))
    def test_if_stmt_2(self):
        input = """
        class testData {
            testData(int a,b; float b) {
                if a.v < z[2] then {
                    a := new Block(a.z, b+d);
                    a := a.v.x.a[1];
                }
                else {
                    this.A := this.function();
                    this.B := Data.block.function(f, "abc");
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 222))
    def test_if_stmt_3(self):
        input = """
        class testData {
            testData(int a,b; float b) {
                if a.v < z[2] then {
                    if (a == 1) then {
                        if (a == 1) then {
                            if (a > 1) then {
                                a := 5;
                                b := 6;
                            }
                            else {
                                if a > b then a := 2; else a := 2;
                            }
                        }
                    }
                    else {
                        if a > b then a := 2; else a := 2;
                    }
                }
                else {
                    if (a == 1) then {
                        if (a == 1) then {
                            if (a > 1) then {
                                a := 5;
                                b := 6;
                            }
                            else {
                                if a > b then a := 2; else a := 2;
                            }
                        }
                        else {
                            if (a == 1) then {
                        if (a == 1) then {
                            if (a > 1) then {
                                a := 5;
                                b := 6;
                            }
                            else {
                                if a > b then a := 2; else a := 2;
                            }
                        }
                    }
                    else {
                        if a > b then a := 2; else a := 2;
                    }
                        }
                    }
                    else {
                        if a > b then a := 2; else a := 2;
                    }
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))
    def test_for_stmt_1(self):
        input = """
        class testFor {
            testFor() {
                for i:=1 to 10 do a:=a+1;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 224))
    def test_for_stmt_2(self):
        input = """
        class testFor {
            testFor() {
                for i:=1 to 10 do a:=a+1;
            }
            testClass callFor() {
                for a.b[2]:=5 downto 25 do a:=a+1;
            }
        }"""
        expect = "Error on line 7 col 21: ."
        self.assertTrue(TestParser.test(input, expect, 225))
    def test_for_stmt_3(self):
        input = """
        class testFor {
            testFor() {
                for i:=1 to 10 do a:=a+1;
            }
            testClass callFor() {
                for a:=5 downto 25 do {
                    a := a + 1;
                };
            }
        }"""
        expect = "Error on line 9 col 17: ;"
        self.assertTrue(TestParser.test(input, expect, 226))
    def test_for_stmt_4(self):
        input = """
        class testFor {
            testFor() {
                for i:=1 to 10 do a:=a+1;
            }
            testClass callFor() {
                for a:=5 downto 25 do {
                    a := a + 1;
                    for a:= 245 to 21 do {
                        a.Pi[5] := 1 + 2;
                    }
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 227))
    def test_for_stmt_5(self):
        input = """
        class testFor {
            testFor() {
                for i:=1 to 10 do a:=a+1;
            }
            testClass callFor() {
                for a:=5 downto 25 do {
                    a := a + 1;
                    for a:= 245 to 21 do {
                        a.Pi[5] := 1 + 2;
                        if a.v < z[2] then {
                            if (a == 1) then {
                                if (a == 1) then {
                                    if (a > 1) then {
                                        a := 5;
                                        b := 6;
                                    }
                                    else {
                                        if a > b then a := 2; else a := 2;
                                    }
                                }
                            }
                            else {
                                if a > b then a := 2; else a := 2;
                            }
                        }
                    }
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 228))
    def test_for_stmt_6(self):
        input = """
        class testFor {
            testFor() {
                for i:=1 to 10 do a:=a+1;
            }
            testClass callFor() {
                for a:=5 downto 25 do {
                    a := a + 1;
                    for a:= 245 to 21 do {
                        a.Pi[5] := 1 + 2;
                        if a.v < z[2] then {
                            if (a == 1) then {
                                for i:=1 downto 10 do {
                                    if a < 2 then a:=1;
                                    else {
                                        a :=2;
                                    }
                                }
                            }
                            for i:=1 to 10 do a:=a+1;
                        }
                    }
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 229))
    # #======================================= 30-39 ==========================================
    def test_for_stmt_7(self):
        input = """
        class testFor {
            testFor() {
                for i:=1 to 10 do a:=a+1;
            }
            testClass callFor() {
                for a:=5 downto 25 do
                    for a:=5 downto 25 do
                        for a:=5 downto 25 do
                            for a:=5 downto 25 do
                                for a:=5 downto 25 do
                                    for a:=5 downto 25 do
                                        a:= 2;
                for a:=5 downto 25 do
                    for a:=5 downto 25 do
                        for a:=5 downto 25 do
                            for a:=5 downto 25 do
                                for a:=5 downto 25 do
                                    for a:=5 downto 25 do
                                        a:= 2;
                for a:=5 downto 25 do
                    for a:=5 downto 25 do
                        for a:=5 downto 25 do
                            for a:=5 downto 25 do
                                for a:=5 downto 25 do
                                    for a:=5 downto 25 do
                                        /*a:= 2;*/
            }
        }"""
        expect = "Error on line 28 col 12: }"
        self.assertTrue(TestParser.test(input, expect, 230))
    def test_for_stmt_8(self):
        input = """
        class testFor {
            testFor() {
                for i:=1 to 10 do a:=a+1;
            }
            testClass callFor() {
                for a:=5 downto 25 do
                    for a:=5 downto 25 do
                        for a:=5 downto 25 do
                            for a:=5 downto 25 do
                                for a:=5 downto 25 do
                                    for a:=5 downto 25 do
                                        a:= 2;
                for a:=5 downto 25 do
                    for a:=5 downto 25 do
                        for a:=5 downto 25 do
                            for a:=5 downto 25 do
                                for a:=5 downto 25 do
                                    for a:=5 downto 25 do
                                        a:= 2;
                for a:=5 downto 25 do
                    for a:=5 downto 25 do
                        for a:=5 downto 25 do
                            for a:=5 downto 25 do
                                for a:=5 downto 25 do
                                    for a:=5 downto 25 do
                                        a:= 2;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231))
    def test_break_con_1(self):
        input = """
        class testData extends PPL {
            void loopTest(int a,v; float c,d; boolean a,s; string str1,str2; Room r1,r2) {
                for i := (a + c -d == f) downto a+(a >=d)/32 do {
                    if a > f-1 then break;
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 232))
    def test_break_con_2(self):
        input = """
        class testData extends PPL {
            void loopTest(int a,v; float c,d; boolean a,s; string str1,str2; Room r1,r2) {
                for i := (a + c -d == f) downto a+(a >=d)/32 do {
                    if a > f-1 then break; else continue;
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 233))
    def test_break_con_3(self):
        input = """
        class testData extends PPL {
            void loopTest(int a,v; float c,d; boolean a,s; string str1,str2; Room r1,r2) {
                for i := (a + c -d == f) downto a+(a >=d)/32 do {
                    for _PPP:= in[1]+123-1.002e+1 to (1+boo[22])._zzt("abc",1,ea01)%12\\22 do {
                        if a == 2 then {
                            a := 1 == 2;
                            continue;
                        }
                        else {
                            if a<= 1+in[2].block then break;
                            else {
                                a := a - 2\\2;
                            }
                        }
                    }
                }
            }
        }"""
        expect = "Error on line 11 col 42: ."
        self.assertTrue(TestParser.test(input, expect, 234))
    def test_break_con_4(self):
        input = """
        class testData extends PPL {
            void loopTest(int a,v; float c,d; boolean a,s; string str1,str2; Room r1,r2) {
                for i := (a + c -d == f) downto a+(a >=d)/32 do {
                    for _PPP:= in[1]+123-1.002e+1 to (1+boo[22])._zzt("abc",1,ea01)%12\\22 do {
                        if a == 2 then {
                            a := 1 == 2;
                            continue;
                        }
                        else {
                            if a<= 1+(in[2]).block then break;
                            else {
                                a := a - 2\\2;
                            }
                        }
                    }
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 235))
    def test_break_con_5(self):
        input = """
        class testData extends PPL {
            void loopTest(int a,v; float c,d; boolean a,s; string str1,str2; Room r1,r2) {
                for i := (a + c -d == f) downto a+(a >=d)/32 do {
                    if a > f-1 then break;
                    for i := (a + c -d == f) downto a+(a >=d)/32 do {
                        for i := (a + c -d == f) downto a+(a >=d)/32 do {
                            for i := (a + c -d == f) downto a+(a >=d)/32 do {
                                for i := (a + c -d == f) downto a+(a >=d)/32 do {
                                    if a > f-1 then break;
                                }
                            }
                        ]
                    }
                }
            }
        }"""
        expect = "Error on line 13 col 24: ]"
        self.assertTrue(TestParser.test(input, expect, 236))
    def test_break_con_6(self):
        input = """
        class testData extends PPL {
            void loopTest(int a,v; float c,d; boolean a,s; string str1,str2; Room r1,r2) {
                for i := (a + c -d == f) downto a+(a >=d)/32 do {
                    if a > f-1 then break;
                    for i := (a + c -d == f) downto a+(a >=d)/32 do {
                        for i := (a + c -d == f) downto a+(a >=d)/32 do {
                            for i := (a + c -d == f) downto a+(a >=d)/32 do {
                                for i := (a + c -d == f) downto a+(a >=d)/32 do {
                                    if a > f-1 then break;
                                }
                                if a > f-1 then break;
                            }
                            if a > f-1 then break;
                        }
                        if a > f-1 then break
                    }
                    if a > f-1 then break;
                }
            }
        }"""
        expect = "Error on line 17 col 20: }"
        self.assertTrue(TestParser.test(input, expect, 237))
    def test_break_con_7(self):
        input = """
        class testData extends PPL {
            void loopTest(int a,v; float c,d; boolean a,s; string str1,str2; Room r1,r2) {
                for i := (a + c -d == f) downto a+(a >=d)/32 do {
                    if a > f-1 then break;
                    for i := (a + c -d == f) downto a+(a >=d)/32 do {
                        for i := (a + c -d == f) downto a+(a >=d)/32 do {
                            for i := (a + c -d == f) downto a+(a >=d)/32 do {
                                for i := (a + c -d == f) downto a+(a >=d)/32 do {
                                    if a > f-1 then break;
                                }
                                if a > f-1 then break;
                            }
                            if a > f-1 then break;
                        }
                        if a > f-1 then break;
                    }
                    if a > f-1 then break;
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 238))
    def test_return_1(self):
        input = """
        class School {
            Student cloneStudent(Student stu){
                Student clone = new Student();
                if clone != nil then
                return clone;
                else return nil;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 239))
    # #======================================= 40-49 ==========================================
    def test_return_2(self):
        input = """class Res {
            int Add(int a, b) {
                return a + b;
            }
            float Add(float a,b) {
                return a + b \\ c % 2 / 1 * a;
            }
            boolean Add(boolean a,b) {
                return a || !b && !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!(c == f);
            }
            string Add (string a, "abcd") {
                return a ^ b ^(c ^ d ^ ("abc" ^ fffffffffffffff));
            }
            doctor makeNew(int a; float b) {
                if a== 0 then
                return new doctor(a,b,c,d,1./2);
                else {
                    if a<1 then
                        return this.doctor;
                    else
                        return nil;
                }
            }
        }"""
        expect = '''Error on line 11 col 34: "abcd"'''
        self.assertTrue(TestParser.test(input, expect, 240))
    def test_return_3(self):
        input = """class Res {
            int Add(int a, b) {
                return a + b;
            }
            float Add(float a,b) {
                return a + b \\ c % 2 / 1 * a;
            }
            boolean Add(boolean a,b) {
                return a || !b && !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!(c == f);
            }
            string Add (string a) {
                return a ^ b ^(c ^ d ^ ("abc" ^ fffffffffffffff));
            }
            doctor makeNew(int a; float b) {
                if a== 0 then
                return new doctor(a,b,c,d,1./2);
                else {
                    if a<1 then
                        return this.doctor;
                    else
                        return nil
                }
            }
        }"""
        expect = "Error on line 22 col 16: }"
        self.assertTrue(TestParser.test(input, expect, 241))
    def test_return_4(self):
        input = """class Res {
            int[6] add (int[3] a,b) {
                int[6] res = copy.Array(a,b,res);
                if res.size() != 0 then
                    return res;
                else
                    return {0,0,0,0,0,0};
            }
        }"""
        expect = "Error on line 7 col 27: {"
        self.assertTrue(TestParser.test(input, expect, 242))
    def test_stmt_1(self):
        input = """
        class C1 {
            static int a;
            C1(int a) {
                this.a := a;
                if this.CheckA() == true then this.PrintA();
                else this.getA();
            }
            boolean CheckA() {
                if this.a <= 0 then return false;
                else return true;
            }
            void PrintA() {
                io.print("Data of list" ^ str.makeStr(a));
            }
            void getA() {
                for i:=0 to -1 do {
                    int a = io.getInt();
                    if (a > 0) then {
                        this.a = a;
                        break;
                    }
                }
                this.PrintA();
            }
        }"""
        expect = "Error on line 20 col 31: ="
        self.assertTrue(TestParser.test(input, expect, 243))
    def test_stmt_2(self):
        input = """
        class C1 {
            static int a;
            C1(int a) {
                this.a := a;
                if this.CheckA() == true then this.PrintA();
                else this.getA();
            }
            boolean CheckA() {
                if this.a <= 0 then return false;
                else return true;
            }
            void PrintA() {
                io.print("Data of list" ^ str.makeStr(a));
            }
            void getA() {
                for i:=0 to -1 do {
                    int a = io.getInt();
                    if (a > 0) then {
                        this.a := a;
                        break;
                    }
                }
                this.PrintA();
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 244))
    def test_stmt_3(self):
        input = """
        class C2 {
            static C1 c;
            final static int[5] arr;
            C2(C1 c) {
                this.c := c;
                C1.PrintA();
            }
            void getArray() {
                for i:=4 downto 0 do {
                    int val = io.getInt();
                    arr[i] := val;
                }
            }
            int[5] getArr() {
                return arr;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 245))
    def test_stmt_4(self):
        input = """
        class C3 extends C2 {
            final string name;
            C3(string n, C1 c) {
                this.name := n;
                this.C2(c);
            }
            string getName() {
                return "Name of C3: " ^ name;
            }
            boolean checkName(string n1) {
                return n1 == name;
            }
        }"""
        expect = "Error on line 4 col 28: c"
        self.assertTrue(TestParser.test(input, expect, 246))
    def test_stmt_5(self):
        input = """
        class checkExp {
            void check1(boolean a,b,c) {
                a1:= a > b > c;
            }
        }"""
        expect = "Error on line 4 col 27: >"
        self.assertTrue(TestParser.test(input, expect, 247))
    def test_stmt_6(self):
        input = """
        class checkExp {
            void check1(boolean a,b,c) {
                a1:= a > (b > c);
                a2:= a==b!=c;
            }
        }"""
        expect = "Error on line 5 col 25: !="
        self.assertTrue(TestParser.test(input, expect, 248))
    def test_stmt_7(self):
        input = """
        class checkExp {
            void check1(boolean a,b,c) {
                a1:= a > (b > c);
                a2:= ((a==b)!=c)==123;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 249))
    # #======================================= 50-59 ==========================================
    def test_stmt_8(self):
        input = """
        class C3 extends C2 {
            string name;
            C3(string n; C1 c) {
                this.name := n;
                this.C2(c);
            }
            string getName() {
                return "Name of C3: " ^ name;
            }
            boolean checkName(string n1) {
                return n1 == name;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 250))
    def test_stmt_9(self):
        input = """
        class mainClass {
            void main() {
                C1 c1 = new C1();
                C2 c2 = new C2(c1);
                C3 c3;
                c3 := new C3("abc
                ",c1);
            }
        }"""
        expect = """"abc"""
        self.assertTrue(TestParser.test(input, expect, 251))
    def test_stmt_10(self):
        input = """
        class mainClass {
            void main() {
                C1 c1 = new C1();
                C2 c2 = new C2(c1);
                C3 c3;
                c3 := new C3("abc",c1);
                c3.checkName("abcd");
                io.Print(c3.getName());
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 252))
    # test random
    def test_only_EOF(self):
        input = """/*no have class
        *****************
        ******************/
        # only have cmt"""
        expect = "Error on line 4 col 23: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 253))
    def test_random_1(self):
        input = """
        # class parent
        class Exp {
            float eval() {}
        }
        # class intlit and floatlit
        class IntLit extends Exp {
            int value;
            Intlit(int a) {
                this.value := a;
            }
            float eval() {
                return this.value;
            }
        }
        # class floatlit and floatlit
        class FloatLit extends Exp {
            float value;
            Intlit(float a) {
                this.value := a;
            }
            float eval() {
                return this.value;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 254))
    def test_random_2(self):
        input = """
        class UnExp extends Exp {
            string op;
            float value;
            UnExp(string op; float value) {
                this.op := op;
                this.value := value;
            }
            float eval() {
                if op == "+" then return value;
                else return value * (-1);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 255))
    def test_random_3(self):
        input = """
        class BinExp extends Exp {
            string op;
            float left,right;
            BinExp(string op; float l,r) {
                this.op := op;
                this.l := l;
                this.r := r;
            }
            float eval() {
                if op == "+" then return left + right;
                else if op == "-" then return lef - right;
                else if op == "*" then return lef * right;
                else if op == "/" then return lef / right;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 256))
    def test_random_4(self):
        input = """class follow_mouse {
    void FixedUpdate () {
        #Get the Screen positions of the object
        Vector2 positionOnScreen = Camera.main.WorldToViewportPoint (transform.position);
        #Get the Screen position of the mouse
        Vector2 mouseOnScreen = (Vector2)Camera.main.ScreenToViewportPoint(Input.mousePosition);
        #Get the angle between the points
        float angle = system.AngleBetweenTwoPoints(positionOnScreen, mouseOnScreen);
        transform.rotation =  Quaternion.Euler(new Vector3(0,0,angle - 180));
    }
 
    float AngleBetweenTwoPoints(Vector3 a, b) {
         return Math.Atan2(a.y - b.y, a.x - b.x) * Math.Rad2Deg;
    }
}"""
        expect = "Error on line 6 col 41: Camera"
        self.assertTrue(TestParser.test(input, expect, 257))
    def test_random_5(self):
        input = """
class smoke_run extends MonoBehaviour{
    float speed = 5f;
    Rigidbody2D rb;
    float counter = 0;
    Vector3 scaleChange;

    void Start()
    {
        rb.velocity := transform.right * speed;
        scaleChange := new Vector3(0.01, 0.01, 0.01);
    }

    void FixedUpdate()
    {
        transform.localScale := transform.localScale + scaleChange;
        if (counter == 100) then {
            system.Destroy(this);
        }
    }
}"""
        expect = "Error on line 3 col 19: f"
        self.assertTrue(TestParser.test(input, expect, 258))
    def test_random_6(self):
        input = """
class skill_check {
    void FixedUpdate()
    {
        if (Input.GetKeyDown("s")) then {
            Destroy(this);
        }
    }
}"""
        expect = "Error on line 6 col 19: ("
        self.assertTrue(TestParser.test(input, expect, 259))
    #======================================= 60-69 ==========================================
    def test_random_7(self):
        input = """
class virus_move {
    GameObject myEffect;
    float speed_virus = -0.15;
    void FixedUpdate()
    {
        transform.position := transform.position + new Vector3(speed_virus, 0, 0);
    }
    void OnTriggerEnter2D(Collider2D col) {
        
        if (col.gameObject.tag == "bullet_water") || (col.gameObject.tag == "bullet_water_skill") then {
            system.Destroy(this);
            system.Instantiate(myEffect, transform.position, transform.rotation);
        }
        if (col.gameObject.tag == "bullet_mask") || (col.gameObject.tag == "bullet_water") then system.Destroy(col.gameObject);
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 260))
    def test_random_8(self):
        input = """
class drop_victim {
    static float count_time = 0;

    static void Update()
    {
        if (count_time < 5) then transform.position := transform.position + new Vector3(0.5, 0.2, 0);
        else transform.position := transform.position + new Vector3(0.5, -0.1, 0);
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 261))
    def test_random_9(self):
        input = """
class control_victim {
    GameObject victim_die;
    GameObject eff;
    float speed_human = -0.15;

    void FixedUpdate()
    {
        transform.position := transform.position + new Vector3(speed_human, 0, 0);
    }
    void OnTriggerEnter2D(Collider2D col) {  
        if (col.gameObject.tag == "bullet_mask") || (col.gameObject.tag == "bullet_water_skill") then {
            system.Destroy(this);
            system.Instantiate(eff, transform.position, transform.rotation);
            system.Instantiate(victim_die, transform.position, transform.rotation);
        }
        if (col.gameObject.tag == "bullet_water") || (col.gameObject.tag == "bullet_mask") then system.Destroy(col.gameObject);
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 262))
    def test_random_10(self):
        input = """
class move {
    Transform smoke_point;
    GameObject smoke_pre;
    float falling = -0.04;
    float jumping = 0.8;
    AudioSource jumpAudio;
    float myHP = 10;
    bool isJump = false;
    float counting = 0;
    float countJump = 0;
    bool checkRun = false;
    Text txt;

    # FIRE
    Transform fire_point;
    GameObject bullet_water;
    GameObject bullet_mask;
    AudioSource shoot_Audio;
    float num_bullet = 1.;
    float count_trigger = 0;
    # special skill
    float count_skill = 100.e-123;
    bool can_skill = false;
    bool have_button = false;
    GameObject water_skill;
    GameObject button_skill;
    AudioSource skill_Audio;

    GameObject Heart;
    float count_kira = -1.0e12;
    void Update() {
        if (Input.GetKeyDown("f")) then {
            this.changeState();
        }
        if (!checkRun) then {
            # UPDATE PLAYER'S HP
            txt.text := myHP.ToString();
            if (transform.position.y > 6) || (transform.position.y < -6) then this.GameOver();
            # CONTROLL JUMP AND DROP OF PLAYER
            if Input.GetButtonDown("Jump") && !isJump then {
                jumpAudio.Play(0);
                countJump := 4;
                isJump := true;
                counting := 3;
                this.outSmoke();
                this.jumpUp(jumping / 2);
            }
            else if countJump != 0 then {
                if countJump > 3 then    this.jumpUp(jumping);
                else                 this.jumpUp(jumping / 3);
            }
            else {
                this.dropDown();
                if counting == 0 then isJump := false;
            }
        }
    }
    void changeState() {
        checkRun := !checkRun;
    }
    # FUNCTION FOR SKILL AND FIRE BULLET
    void create_button_skill() {
        system.Instantiate(button_skill, new Vector3(-6.5,-4,0), transform.rotation);
    }
    void create_skill() {
        can_skill := false;
        have_button := false;
        system.Instantiate(water_skill, new Vector3(-10,0,0), transform.rotation);  
        skill_Audio.Play(0);   
    }
    void shootWater() {
        for i := 0  to num_bullet do {
            system.Instantiate(bullet_water, fire_point.position, fire_point.rotation);  
            shoot_Audio.Play(0);       
        }
    }
    void shootMask() {
        for i := 0 to num_bullet do {
            system.Instantiate(bullet_mask, fire_point.position, fire_point.rotation);  
            shoot_Audio.Play(0);       
        }
    }
    # FUNCTION CONTROLL UFO AND EFFECT WHEN JUMPING
    void outSmoke() {
        system.Instantiate(smoke_pre, smoke_point.position, smoke_point.rotation);
    }
    void jumpUp(float upSize) {
        system.transform.position := transform.position + new Vector3(0, upSize, 0);
    }
    void dropDown() {
        system.transform.position := transform.position + new Vector3(0, falling, 0);
    }
    void GameOver() {
        SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex - 1);
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 263))
    def test_random_11(self):
        input = """
class PlayerMoment extends MonoBehaviour{
    CharacterController ctrller;
    Transform groundCheck;
    float groundDistance = 0.4;
    LayerMask groundMask;

    float speed = 12;
    float gravity = -9.81* 10;
    float jumpHeight = 7;
    Vector3 velocity;
    bool isGrounded;
    # Update is called once per frame
    void Update()
    {
        isGrounded := Physics.CheckSphere(groundCheck.position, groundDistance, groundMask);

        if (isGrounded && velocity.y < 0) then {
            velocity.y := -2;
        }
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 264))
    def test_random_12(self):
        input = """
class PlayerMoment extends MonoBehaviour{
    CharacterController ctrller;
    Transform groundCheck;
    float groundDistance = 0.4;
    LayerMask groundMask;

    float speed = 12;
    float gravity = -9.81 * 10;
    float jumpHeight = 7;
    Vector3 velocity;
    bool isGrounded;
    # Update is called once per frame
    void Update()
    {
        Vector3 move;
        float x,z;
        isGrounded := Physics.CheckSphere(groundCheck.position, groundDistance, groundMask);

        if (isGrounded) && (velocity.y < 0) then {
            velocity.y := -2;
        }

        x := Input.GetAxis("Horizontal");
        z := Input.GetAxis("Vertical");

        move := transform.right * x + transform.forward * z;
        ctrller.Move(move  * speed * Time.deltaTime);

        if Input.GetButtonDown("Jump") && isGrounded then {
            velocity.y := Mathf.Sqrt(jumpHeight * -2 * gravity);
        }

        velocity.y := velocity.y + gravity * Time.deltaTime;
        ctrller.Move(velocity * Time.deltaTime);
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 265))
    def test_random_13(self):
        input = """
class Faculty {
        string name;
        Faculty(string n = "") : name(n) {}
        string getNameFaculty() { return name;  }
        void setNameFaculty(string n) { name := n;  }
}"""
        expect = "Error on line 4 col 25: ="
        self.assertTrue(TestParser.test(input, expect, 266))
    def test_random_14(self):
        input = """
# LECTURER

class Lecturer {
        string name;
        Faculty lecFaculty;
        Lecturer(string n)  { name:=n; }
        Lecturer(string n; Faculty f) { name := n; lecFaculty := f; }
        string getNameLecturer() { return name; }
        void setNameLecturer(string n) { name := n; }
        string getNameFacultyOfLecturer() { return lecFaculty.getNameFaculty(); }
        void setNameFacultyOfLecturer(string n) { lecFaculty.setNameFaculty(n); }
};

# CLASSROOM

class Classroom {
        string nameRoom;
        Classroom(string n) { nameRoom:=n;}
        string getNameClassroom() { return nameRoom; }
        void setNameClassroom(string n) { nameRoom := n; }
}"""
        expect = "Error on line 13 col 1: ;"
        self.assertTrue(TestParser.test(input, expect, 267))
    def test_random_15(self):
        input = """
class Subject {
        string name;
        Lecturer[5] subLecturer;
        int sLec;
        Classroom subRoom;
        Subject(string n) { name:=n; sLec:=0;}
        string getNameSubject() { return name; }
        void setNameSubject(string n) { name := n; }
};"""
        expect = "Error on line 4 col 16: ["
        self.assertTrue(TestParser.test(input, expect, 268))
    def test_random_16(self):
        input = """
class Subject {
        string name;
        Lecturer subLecturer;
        int sLec;
        Classroom subRoom;
        Subject(string n) { name:=n; sLec:=0;}
        string getNameSubject() { return name; }
        void setNameSubject(string n) { name := n; }
        void inputData() {
            string n;
            int num;
            io.print("---------------\\n");
            io.print("Input name of Subject: ");
            io.fflush(stdin);
            io.getline(n);
            name := n;

            io.Print("How many Lecturer? ");
            io.getInt(num);
            sLec := num;

            for i:= 0 to -1 do {
                io.print("The number must less than or equal 5!\\n");
                io.print("How many Lecturer? ");
                io.getInt(num);
                if (num > 0) then i := -2;
            }

            io.print("---------------\\n");
            for j := 0 to num do {
                io.print("Input name of Lecturer " ^ str.toString(j + 1) ^ ":\\n");
                io.fflush(stdin);
                io.getline(n);
                subLecturer.setNameLecturer(n);
                io.print("Input Lecturer's Faculty " ^ str.toString(j + 1) ^ ":\\n");
                io.fflush(stdin);
                io.getline(n);
                subLecturer.setNameFacultyOfLecturer(n);
            }
            io.print("----------\\n");
            io.print("Input name of Room: ");
            io.fflush(stdin);
            io.getline(n);
            subRoom.setNameClassroom(n);
        }
        bool checkRoom(string name) {
            string className = subRoom.getNameClassroom();
            if (className == name) then    return 1;
            return false;
        }
        void checkLect() {
            io.print("List Lecturers of " ^ name ^ ":\\n");
            for i := 0 to sLec do
                io.print(subLecturer.getNameLecturer() ^ endl);
        }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 269))
    # #======================================= 70-79 ==========================================
    def test_random_17(self):
        input = """
# STUDENT

class Student {
        string name;
        int id;
        Faculty facul;
        Subject subs;
        int nSub;
        Student(string n; int i; int nS) { name:=n; id:=i; nSub:=nS; }
        void setNameStudent(string n) { name := n;  }
        void setID(int n) { id := n;  }
        void setNameFacultyStudent(string n) { facul := n; }
        string getNameStudent() { return name;  }
        int getID() { return id;  }
        string getNameFacultyStudent() { return facul.getNameFaculty();  }
        void inputSub(int n) {
            if (n > 10) then io.print("Number of Subject must less than or equal 10");
            nSub := n;
            for i := 0 to nSub do {
                io.print("Input subject " ^str.toString(i + 1)^ ":\\n");
                subs.inputData();
            }
        }
        bool findSubject(string name) {
            for i := 0 do
                if (subs.getNameSubject() == name)then return 1;
            return 0;
        }
        void checkLec() {
            for i := 0 to nSub do {
                io.print("\\n----------\\n");
                subs.checkLect();
            }
        }
        bool checkFacuSub(string facu; string sub) {
            if (facul.getNameFaculty() != facu) then   return 0;
            return this.findSubject(sub);
        }
}"""
        expect = "Error on line 26 col 23: do"
        self.assertTrue(TestParser.test(input, expect, 270))
    def test_random_18(self):
        input = """
# STUDENT

class Student {
        string name;
        int id;
        Faculty facul;
        Subject subs;
        int nSub;
        Student(string n; int i; int nS) { name:=n; id:=i; nSub:=nS; }
        void setNameStudent(string n) { name := n;  }
        void setID(int n) { id := n;  }
        void setNameFacultyStudent(string n) { facul := n; }
        string getNameStudent() { return name;  }
        int getID() { return id;  }
        string getNameFacultyStudent() { return facul.getNameFaculty();  }
        void inputSub(int n) {
            if (n > 10) then io.print("Number of Subject must less than or equal 10");
            nSub := n;
            for i := 0 to nSub do {
                io.print("Input subject " ^str.toString(i + 1)^ ":\\n");
                subs.inputData();
            }
        }
        bool findSubject(string name) {
            for i := 0 to nSub do
                if (subs.getNameSubject() == name)then return 1;
            return 0;
        }
        void checkLec() {
            for i := 0 to nSub do {
                io.print("\\n----------\\n");
                subs.checkLect();
            }
        }
        bool checkFacuSub(string facu; string sub) {
            if (facul.getNameFaculty() != facu) then   return 0;
            return this.findSubject(sub);
        }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 271))
    def test_random_19(self):
        input =  """
class mainClass {
int main() {
    Faculty facul;
    Lecturer lect;
    Student stud;
    Classroom classR;
    Subject subj;
    int sFacu, sLect, sStud, sRoom, sSubj;
    int n;

    #=========================FACULTY=========================//
    io.print("=============================================================\\n");
    io.print("How many Faculties? ");
    io.getInt(n);
    sFacu := n;
    for i := 0 to n do {
        string name;
        io.print("-----------------------------\\nInput details for Faculty " ^ str.toString(i + 1) ^ ":\\n");
        io.print("Input name of Faculty: ");
        io.fflush(stdin);
        io.getline(name);
        facul.setNameFaculty(name);
    }
    #=======================LECTURER=======================//
    io.print("=============================================================\\n");
    io.print("How many Lecturer? ");
    io.getInt(n);
    sLect := n;
    for i := 0 to i<n do {
        string name;
        io.print("------------------------------\\n");
        io.print("Input details for Lecturer " ^ str.toString(i + 1) ^ ":\\n");
        io.print("Input name of Lecturer: ");
        io.fflush(stdin);
        io.getline(name);
        this.lectsetNameLecturer(name);
        io.print("Input Lecturer's Faculty: ");
        io.fflush(stdin);
        io.getline(name);
        lect.setNameFacultyOfLecturer(name);
    }
    #=========================STUDENT=========================//
    io.print("\\n=============================================================\\n");
    io.print("How many Student? ");
    io.getInt(n);
    sStud := n;
    for i := 0 to n do {
        string name;
        int id;
        io.print("----------------------------------------\\n");
        io.print("Input details for Student " ^ str.toString(i + 1) ^ ":\\n");
        io.print("Input name of Student: ");
        io.fflush(stdin);
        io.getline(name);
        stud.setNameStudent(name);
        io.print("Input ID of Student: ");
        io.getInt(id);
        stud.setID(id);
        io.print("Input Faculty of Student: ");
        io.fflush(stdin);
        io.getline(name);
        stud.setNameFacultyStudent(name);
        io.print("Input number of Subject: ");
        io.getInt(id);
        io.print("--------------------\\n");
        stud.inputSub(id);
    }

    #=========================CLASSROOM===========================//
    io.print("\\n=============================================================\\n");
    io.print("How many Classroom? ");
    io.getInt(n);
    sRoom := n;
    for i:=0 to n do {
        string name;
        io.print("---------------------------------\\n");
        io.print("Input details for Classroom " ^ str.toString(i + 1) ^ ":\\n");
        io.print("Input name of Classroom: ");
        io.fflush(stdin);
        io.getline(name);
        classR.setNameClassroom(name);
    }

    #=========================SUBJECT============================//
    io.print("\\n=============================================================\\n");
    io.print("How many Subject? ");
    io.getInt(n);
    sSubj := n;
    subj.inputData();
    io.print("\\n=============================================================\\n");
    return 0;

}

}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 272))
    def test_random_20(self):
        input = """
class mainClass {
int main() {
    Faculty facul;
    Lecturer lect;
    Student stud;
    Classroom classR;
    Subject subj;
    int sFacu, sLect, sStud, sRoom, sSubj;
    int n;

    #=========================FACULTY=========================//
    io.print("=============================================================\\n");
    io.print("How many Faculties? ");
    io.getInt(n);
    sFacu := n;
    for i := 0 to n do {
        string name;
        io.print("-----------------------------\\nInput details for Faculty " ^ str.toString(i + 1) ^ ":\\n");
        io.print("Input name of Faculty: ");
        io.fflush(stdin);
        io.getline(name);
        facul.setNameFaculty(name);
    }
    #=======================LECTURER=======================//
    io.print("=============================================================\\n");
    io.print("How many Lecturer? ");
    io.getInt(n);
    sLect := n;
    for i := 0 to i<n do {
        string name;
        io.print("------------------------------\\n");
        io.print("Input details for Lecturer " ^ str.toString(i + 1) ^ ":\\n");
        io.print("Input name of Lecturer: ");
        io.fflush(stdin);
        io.getline(name);
        this.lectsetNameLecturer(name);
        io.print("Input Lecturer's Faculty: ");
        io.fflush(stdin);
        io.getline(name);
        lect.setNameFacultyOfLecturer(name);
    }
    #=========================STUDENT=========================//
    io.print("\\n=============================================================\\n");
    io.print("How many Student? ");
    io.getInt(n);
    sStud := n;
    for i := 0 to n do {
        string name;
        int id;
        io.print("----------------------------------------\\n");
        io.print("Input details for Student " ^ str.toString(i + 1) ^ ":\\n");
        io.print("Input name of Student: ");
        io.fflush(stdin);
        io.getline(name);
        stud.setNameStudent(name);
        io.print("Input ID of Student: ");
        io.getInt(id);
        stud.setID(id);
        io.print("Input Faculty of Student: ");
        io.fflush(stdin);
        io.getline(name);
        stud.setNameFacultyStudent(name);
        io.print("Input number of Subject: ");
        io.getInt(id);
        io.print("--------------------\\n");
        stud.inputSub(id);
    }

    #=========================CLASSROOM===========================//
    io.print("\\n=============================================================\\n");
    io.print("How many Classroom? ");
    io.getInt(n);
    sRoom := n;
    for i:=0 to n do {
        string name;
        io.print("---------------------------------\\n");
        io.print("Input details for Classroom " ^ str.toString(i + 1) ^ ":\\n");
        io.print("Input name of Classroom: ");
        io.fflush(stdin);
        io.getline(name);
        classR.setNameClassroom(name);
    }

    #=========================SUBJECT============================//
    io.print("\\n=============================================================\\n");
    io.print("How many Subject? ");
    io.getInt(n);
    sSubj := n;
    subj.inputData();
    io.print("\\n=============================================================\\n");
    
    #======================QUIZ 2====================//
    n:=1;
    if n!=0 then {
        io.print("Please choose:");
        io.getInt(n);
        io.print("==========\\n");
        if n== 1 then {
            string name;
            bool hasKnown = 0;
            io.print("Enter classroom name? ");
            io.fflush(stdin);
            io.getline(name);
            for i := 0 to sSubj do {
                if (subj.checkRoom(name)) then {
                    if (hasKnown == 0) then {
                        hasKnown := 1;
                        io.print("----------\\nList subjects hosted in this classroom:\\n");
                    }
                    io.print(subj.getNameSubject() ^ endl);
                }
            }
            if (hasKnown == 0) then
                io.print("Don't have any subject hosted in this classroom!\\n");
            break;  
        }

        else if n== 2 then{
            string name;
            bool hasKnown = 0;
            io.print("Enter subject name? ");
            io.fflush(stdin);
            io.getline(name);
            for i := 0 to sSubj do {
                if (stud.findSubject(name)) then{
                    if (hasKnown == 0) then{
                        hasKnown := 1;
                        io.print("-----------\\nList students studying this subject:\\n");
                    }
                    io.print(stud.getNameStudent() ^ endl);
                }
            }
            if (hasKnown == 0) then
                io.print("Don't have any student studying this subject!\\n");
            break;
        }

        else if n== 3 then {
            string name;
            bool hasKnown = 0;
            io.print("Enter student name? ");
            io.fflush(stdin);
            io.getline(name);
            for i := 0 to sStud do
                if (stud.getNameStudent() == name)then {
                    hasKnown := 1;
                    stud.checkLec();
                }
            if (hasKnown == 0)then
                io.print("Don't have this student in database!\\n");
            break;
        }

        else if n== 4 then {
            string facu, sub;
            bool hasKnown = 0;
            io.print("Enter faculty name? ");
            io.fflush(stdin);
            io.getline(facu);
            io.print("Enter subject name? ");
            io.fflush(stdin);
            io.getline(sub);
            for i := 0 to sStud do {
                if (stud.checkFacuSub(facu, sub))then {
                    if (hasKnown == 0)then {
                        hasKnown := 1;
                        io.print("----------\\nList students belonging to this faculty and study this subject:\\n");
                    }
                    io.print(   stud.getNameStudent() ^ endl);
                }
            }
            if (hasKnown == 0)then
                io.print("Don't have any student belonging to this faculty and study this subject!\\n");
            break;
        }
        else {
            io.print("WRONG CODE NUMBER!");
            break;
        }
        io.print("\\n=========\\nContinue ? Press 0 to EXIT or anykey to continue: ");
        io.getInt(n);
    }
    return 0;

}

}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 273))
    def test_random_21(self):
        input = """
class display {
    static display dis_instance;
    Text txt;
    void Start()
    {
        if (dis_instance == null) then {
            dis_instance := this;
        }
    }
    static void Display(string str) {
        txt.text := str;
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 274))
    def test_random_22(self):
        input = """
class skill{
    string name = "";
    skill(){
        if (this.name == "") then
            this.name := "Skill";
    }
    string getName() {
        return this.name;
    }
    void displayData() {}
}
class FireBall extends skill{
    FireBall(){
        this.name := "FireBall";
    }
    void displayData() {
        display.dis_instance.Display(this.name);
    }
}
class RockShield extends skill{
    RockShield(){
        this.name := "RockShield";
    }
    void displayData() {
        display.dis_instance.Display(this.name);
    }
}
class WaterHealing extends skill{
    WaterHealing(){ this.name := "WaterHealing";}
    void displayData() {
        display.dis_instance.Display(this.name);
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 275))
    def test_random_23(self):
        input = """
class ButtonRun {
    skill my_skill;
    Text txt;
    void InitButton(skill input_skill) {
        this.my_skill := input_skill;
        txt.text := my_skill.getName();
    }
    void clickButton() {
        my_skill.displayData();
    }
}
class factory_skil{
    static skill get_skill(all_skill i) {
        if i == all_skill.FireBall then
                return new FireBall();
        else if i == all_skill.WaterHealing then
                return new WaterHealing();
        else if i == all_skill.RockShield then
                return new RockShield();
        else
                return new skill();
    }
}
class manager_skill {
    ButtonRun list_button;
    manager_skill(all_skill i) {
        list_button.InitButton(factory_skill.get_skill(i));
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 276))
    def test_random_24(self):
        input = """
class Bank {
    string bankName;

    void doSomething()
    {
        #
    }
} class Agribank extends Bank{
    Agribank()
    {
        bankName := "Agribank";
    }
    void doSomething()
    {
        io.print("Agribank");
    }
}  \t\t\t class OCB extends Bank{
    OCB()
    {
        bankName := "OCB";
    }
    void doSomething()
    {
        io.print("OCB");
    }
} class Vietcombank extends Bank{
    Vietcombank()
    {
        bankName := "Vietcombank";
    }
    void doSomething()
    {
        io.print("Vietcombank");
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 277))
    def test_random_25(self):
        input = """
class Grade {
        string nameOfCourse;
        int mark;
        Grade() {
            nameOfCourse := "";
            mark := 0;
        }
        Grade(string nameOfCourse; int mark) {
            this.nameOfCourse := nameOfCourse;
            this.mark := mark;
        }
        void setName(string name) { this.nameOfCourse := name; }
        void setMark(int mark)  { this.mark := mark;}
        int getMark()      { return mark; }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 278))
    def test_random_26(self):
        input = """
class Student {
        int studentID;
        string name;
        Grade grades;
        int numOfGrade;
        int sumMark;
        Student(int ID; string name) {
            this.studentID := ID;
            this.name := name;
            numOfGrade := 0;
            sumMark := 0;
        }
        void insertGrade(string nameOfCourse; int mark) {
            grades.setName(nameOfCourse);
            grades.setMark(mark);
            numOfGrade := numOfGrade+1;
            sumMark := sumMark+ mark;
        }
        float getAverage()  {
            return (float)sumMark / numOfGrade;
        }
};"""
        expect = "Error on line 21 col 20: float"
        self.assertTrue(TestParser.test(input, expect, 279))
    # #======================================= 80-89 ==========================================
    def test_random_27(self):
        input = """
class mainClass {
int main() {
    int n;
    Student students;
    int ID;
    string name;
    int numOfMark;
    string nameMark;
    int mark;
    io.print("Enter number of Students? ");
    io.getInt(n);
        # GET INFORMATION
        io.print("Input details for Student " ^ (i + 1) ^ ":\\n");
        io.print("Student ID? ");
        io.getInt(ID);
        for i := true to 1.234E-12 do {
            io.fflush(stdin);
            io.print("Name? ");
            io.getline(name);
            if (name.size() < 40) then    break;
            io.print("Name of Student must have less than 40 characters!\\n");
            name.clear();
        }
        students.push(new Student(ID, name));
        # GET MARK
        for i := true to 1.234E-12 do {
            io.print("How many Grades? ");
            io.getInt(numOfMark);
            if (numOfMark < 10) then   break;
            io.print("Number of Mark must less than or equal 10!\\n");
        }
        if (j != 0) then io.print("-----\\n");
        for i := true to 1.234E-12 do {
            io.print("Name of Grade " ^ (j + 1) ^ ": ");
            io.fflush(stdin);
            io.getline(nameMark);
            if (nameMark.size() < 40)  then  break;
            io.print("Name of Mark must have less than 40 characters!\\n");
        }
            
        io.print("Mark of Grade " ^ (j + 1) << ": ");
        io.getInt(mark);
        students.insertGrade(nameMark, mark);
    n := 1;
    # GET AVERAGE
    for i := true to 1.234E-12 do {
        io.print("Which student average grade? ");
        io.getInt(n);
        if (n > 0) && (n <= students.size()) then
            io.print("Average grade for student " ^ n ^ ": " ^ students.getAverage());
        else
            io.print("Don't have student " ^ n ^ endl);

        for i := true to 1.234E-12 do  {
            io.print("\\nIf your want to continues, press 1, else, press 0: ");
            io.getInt(n);
            if (n == 1) || (n == 0) then    break;
            io.print("\\"Input 0 or 1!\\"\\n");
        }
        
        if (n == 1) then   io.print("-----\\n");
    }
    return 0;
}
}"""
        expect = "Error on line 42 col 45: <"
        self.assertTrue(TestParser.test(input, expect, 280))
    def test_random_28(self):
        input = """
class mainClass {
int main() {
    int n;
    Student students;
    int ID;
    string name;
    int numOfMark;
    string nameMark;
    int mark;
    io.print("Enter number of Students? ");
    io.getInt(n);
        # GET INFORMATION
        io.print("Input details for Student " ^ (i + 1) ^ ":\\n");
        io.print("Student ID? ");
        io.getInt(ID);
        for i := true to 1.234E-12 do {
            io.fflush(stdin);
            io.print("Name? ");
            io.getline(name);
            if (name.size() < 40) then    break;
            io.print("Name of Student must have less than 40 characters!\\n");
            name.clear();
        }
        students.push(new Student(ID, name));
        # GET MARK
        for i := true to 1.234E-12 do {
            io.print("How many Grades? ");
            io.getInt(numOfMark);
            if (numOfMark < 10) then   break;
            io.print("Number of Mark must less than or equal 10!\\n");
        }
        if (j != 0) then io.print("-----\\n");
        for i := true to 1.234E-12 do {
            io.print("Name of Grade " ^ (j + 1) ^ ": ");
            io.fflush(stdin);
            io.getline(nameMark);
            if (nameMark.size() < 40)  then  break;
            io.print("Name of Mark must have less than 40 characters!\\n");
        }
            
        io.print("Mark of Grade " ^ (j + 1) ^ ": ");
        io.getInt(mark);
        students.insertGrade(nameMark, mark);
    n := 1;
    # GET AVERAGE
    for i := true to 1.234E-12 do {
        io.print("Which student average grade? ");
        io.getInt(n);
        if (n > 0) && (n <= students.size()) then
            io.print("Average grade for student " ^ n ^ ": " ^ students.getAverage());
        else
            io.print("Don't have student " ^ n ^ endl);

        for i := true to 1.234E-12 do  {
            io.print("\\nIf your want to continues, press 1, else, press 0: ");
            io.getInt(n);
            if (n == 1) || (n == 0) then    break;
            io.print("\\"Input 0 or 1!\\"\\n");
        }
        
        if (n == 1) then   io.print("-----\\n");
    }
    return 0;
}
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 281))
    def test_random_29(self):
        input = """
class io {
    static void getInt(int a) {
        int data = (system.checkIntLitForm(system.getIO())).toInt();
        a := data;
    }
    static void getFloat(float a) {
        float data = (system.checkFloatLitForm(system.getIO())).toFloat();
        a := data;
    }
    static void getBoolean(boolean a) {
        boolean data = (system.checkBooleanLitForm(system.getIO())).toBoolean();
        a := data;
    }
    static void getline(string a) {
        string test = system.getIO();
        a := "";
        for i:=(true && false==true) downto 1. + 2e-123 do{
            a := a^test;
            test := system.getIO();
            if test == "\\n" then break;
            else continue;
        }
    }
    static void fflush(typeIO s) {
        if s == stdin then system.clear_console();
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 282))
    def test_random_30(self):
        input = """
class heap {
int minWaitingTime(int n; int arrvalTime[]; int[5] completeTime) {
    int curTime = 0;
    int totalWaitTime = 0;
    int min = -1;
    int serCos = -1;
    int serTime = -1;

    return totalWaitTime;   
}
}"""
        expect = "Error on line 3 col 40: ["
        self.assertTrue(TestParser.test(input, expect, 283))
    def test_random_31(self):
        input = """
class heap {
int minWaitingTime(int n; int[] arrvalTime; int[5] completeTime) {
    int curTime = 0;
    int totalWaitTime = 0;
    int min = -1;
    int serCos = -1;
    int serTime = -1;

    return totalWaitTime;   
}
}"""
        expect = "Error on line 3 col 30: ]"
        self.assertTrue(TestParser.test(input, expect, 284))
    def test_random_32(self):
        input = """
class heap {
int minWaitingTime(int n; int[5] arrvalTime, completeTime) {
    int curTime = 0;
    int totalWaitTime = 0;
    int min = -1;
    int serCos = -1;
    int serTime = -1;
    for i:=((-1!=true||false)==(2\\2/15)) downto xyz do {
        for i := 0 to n do {
            if ((curTime >= arrvalTime[i]) && ((serCos == -1) || (serTime > completeTime[i]))) then {
                    serCos := i;
                    serTime := completeTime[i];
            }
            if (min == -1) || (min > arrvalTime[i]) then   min := arrvalTime[i];
        }
        if (serCos != -1) then {
            totalWaitTime := totalWaitTime + curTime - arrvalTime[serCos] + serTime;
            curTime := curTime + serTime;
            n:= n-1;
            algorithm.swap(arrvalTime[serCos], arrvalTime[n]);
            algorithm.swap(completeTime[serCos], completeTime[n]);
            serCos := -1;
        }
        else    curTime := min;
        if n < 0 then break;
    }
    return totalWaitTime;   
}

int main() {
    {
        int n = 3;
        int[5] arrvalTime = {0, 1, 2, 3, 4};
        int[5] completeTime = {3, 9, 6, 10, 8};

        io.print(this.minWaitingTime(n, arrvalTime, completeTime));
    }
    io.print(endl);
    {
        int n = 4;
        int[5] arrvalTime = {0, 4, 2, 5, 7};
        int[5] completeTime = {4, 2, 3, 4, 10};

        io.print(this.minWaitingTime(n, arrvalTime, completeTime));
    }
}
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 285))
    def test_random_33(self):
        input = """
class student {
    static int num_student;
    string name;
    string ID;
    Class c;
    student(string name, id; Class c) {
        this.name := name;
        this.ID := id;
        num_student := num_student + 1;
        this.c := c;
    }
    int getNumStudent() {
        return num_student;
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 286))
    def test_random_34(self):
        input = """
class special_student extends student {
    string[100] list_skill_special;
    int num_skill;
    special_student(string name, id; Class c) {
        this.student(name, id, c);
        num_skill := 0;
    }
    void updateSkill(string skill) {
        this.list_skill_special[num_skill] := skill; 
        num_skill := num_skill + 1;
    }
    int getNumSkill() {
        return num_skill;
    }
    string[100] getSkill() {
        return list_skill_special;
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 287))
    def test_random_35(self):
        input = """
class  Class {
    string name;
    Class(string name) {
        this.name := name;
    }
    student getStudent(string name, id; Class c; boolean option) {
        if option == true then
            return new special_student(name,id,c);
        else
            return new student(name,id,c);
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 288))
    def test_random_36(self):
        input = """
class School {
    static string[50] class_name;
    static int num_class;
    static int getNumClass() {
        return num_class;
    }
    static string getNameClass(int i) {
        if i < num_class then
        return class_name[i];
    }
    static updateClass(string name) {
        class_name[num_class] := name;
        num_class := num_class + 1;
    }
}"""
        expect = "Error on line 12 col 22: ("
        self.assertTrue(TestParser.test(input, expect, 289))
    # #======================================= 90-99 ==========================================
    def test_random_37(self):
        input = """
class makeSchool {
    void main() {
        for i:=true downto z-1 do {
            string class;
            io.fflush(stdin);
            io.getline(class);
            if class != "-1" then
                School.updateClass(class);
            else break;
        }
    }
}"""
        expect = "Error on line 5 col 19: class"
        self.assertTrue(TestParser.test(input, expect, 290))
    def test_random_38(self):
        input = """
class makeSchool {
    void main() {
        for i:=true downto z-1 do {
            string new_class;
            io.fflush(stdin);
            io.getline(new_class);
            if new_class != "-1" then
                School.updateClass(new_class);
            else break;
        }
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 291))
    def test_random_39(self):
        input = """
class getStudent {
    int main() {
        int n;
        io.getInt(n);
        for i:= 0 to n do {
            string id;
            string new_stu;
            boolean option;
            io.getlint(id);
            io.fflush(stdin);
            io.getlint(new_stu);
            io.fflush(stdin);
            io.getBoolean(option);
            student new_student = (School.getNameClass(range.random() % School.num_class)).getStudent(name,id,option);
            Class.updateStudent(new_student);
        }
    }
}"""
        expect = "Error on line 15 col 20: new_student"
        self.assertTrue(TestParser.test(input, expect, 292))
    def test_random_40(self):
        input = """
class node {
    int data;
    node next;
    node(int data; node next) {
        this.data := data;
        this.next := next;
    }
    int getData() {
        return data;
    }
    node getNext() {
        return next;
    }
    void setData(int data) {
        this.data := data;
    }
    void setNext(node next) {
        this.next := next;
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 293))
    def test_random_41(self):
        input = """
class linked_list {
    static node start;
    linked_list(node s) {
        this.start := s;
    }
    static node getNode(int index; node n) {
        if index == 0 then
            return n;
        else
            return this.getNode(index - 1, n.getNext());
    }
    static void putNode(node n) {
        if n.getNext() == nil then {
            int data;
            io.getInt(data);
            n.setNext(new node(data, nil));
        }
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 294))
    def test_random_42(self):
        input = """
class mainFuncion {
    void insert (int index; node root, n) {
        if index == 0 then
            n.setNext(root.getNext());
            root.setNext(n);
        else
            insert(index - 1, root.getNext(), n);
    }
}"""
        expect = "Error on line 7 col 8: else"
        self.assertTrue(TestParser.test(input, expect, 295))
    def test_random_43(self):
        input = """
class mainFuncion {
    void insert (int index; node root, n) {
        if index == 0 then {
            n.setNext(root.getNext());
            root.setNext(n);
        }
        else
            array.insert(index - 1, root.getNext(), n);
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 296))
    # test array literal
    def test_arraylit_1(self):
        input = """
class tesster {
    int[5] getCaculatorInt(int a,b) {
        int[5] arr = {a + b, a - b, a * b, a % b, a \\ b};
    }
}"""
        expect = "Error on line 4 col 22: a"
        self.assertTrue(TestParser.test(input, expect, 297))
    def test_arraylit_2(self):
        input = """
class tesster {
    int[5] getCaculatorInt(int a,b) {
        int[5] arr;
        arr := {a + b, a - b, a * b, a % b, a \\ b};
    }
}"""
        expect = "Error on line 5 col 16: a"
        self.assertTrue(TestParser.test(input, expect, 298))
    def test_arraylit_3(self):
        input = """
class tesster {
    int[5] getCaculatorInt(int a,b) {
        int[5] arr;
        int a1 = a + b;
        int a2 = a- b;
        int a3 = a*b;
        int a4 = a%b;
        int a5 = a\\b;
        arr := {a1,a2,a3,a4,a5};
    }
}"""
        expect = "Error on line 10 col 16: a1"
        self.assertTrue(TestParser.test(input, expect, 299))
