import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    def test_lowercase_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("count","count,<EOF>",101))
        self.assertTrue(TestLexer.test("_count","_count,<EOF>",102))
        self.assertTrue(TestLexer.test("0_count","0,_count,<EOF>",103))
        self.assertTrue(TestLexer.test("$count","Error Token $",104))
        self.assertTrue(TestLexer.test("_count total","_count,total,<EOF>",105))
        self.assertTrue(TestLexer.test("_count 123total","_count,123,total,<EOF>",106))
        self.assertTrue(TestLexer.test("$count total","Error Token $",107))
        self.assertTrue(TestLexer.test("_count x1","_count,x1,<EOF>",108))
        self.assertTrue(TestLexer.test("_count_id","_count_id,<EOF>",109))
        self.assertTrue(TestLexer.test("count_id1","count_id1,<EOF>",110))
    def test_lower_upper_id(self):
        """test mix identifiers"""
        self.assertTrue(TestLexer.test("cOuNt","cOuNt,<EOF>",111))
        self.assertTrue(TestLexer.test("_COUNT","_COUNT,<EOF>",112))
        self.assertTrue(TestLexer.test("0_Count","0,_Count,<EOF>",113))
        self.assertTrue(TestLexer.test("$Count","Error Token $",114))
        self.assertTrue(TestLexer.test("_count TOTAL","_count,TOTAL,<EOF>",115))
        self.assertTrue(TestLexer.test("_CoUnt 123total","_CoUnt,123,total,<EOF>",116))
        self.assertTrue(TestLexer.test("$count123 total","Error Token $",117))
        self.assertTrue(TestLexer.test("_count X1","_count,X1,<EOF>",118))
        self.assertTrue(TestLexer.test("_countID","_countID,<EOF>",119))
        self.assertTrue(TestLexer.test("_count_ID1","_count_ID1,<EOF>",120))
    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.test(" 12345 ","12345,<EOF>",121))
        self.assertTrue(TestLexer.test(" 6 ","6,<EOF>",122))
        self.assertTrue(TestLexer.test("7.3  ","7.3,<EOF>",123))
        self.assertTrue(TestLexer.test(" 6 78 ","6,78,<EOF>",124))
        self.assertTrue(TestLexer.test(" 150 000 ","150,000,<EOF>",125))
        self.assertTrue(TestLexer.test(" -7.6 -5 ","-,7.6,-,5,<EOF>",126))
        self.assertTrue(TestLexer.test(" 5 0.03 ","5,0.03,<EOF>",127))
        self.assertTrue(TestLexer.test(" 5a37 ","5,a37,<EOF>",128))
        self.assertTrue(TestLexer.test("a123","a123,<EOF>",129))
        self.assertTrue(TestLexer.test(" 5+100 ","5,+,100,<EOF>",130))
    def test_float(self):
        """test floats"""
        self.assertTrue(TestLexer.test(" 7.5 0.6 ","7.5,0.6,<EOF>",131))
        self.assertTrue(TestLexer.test(" 6.8+9.2 ","6.8,+,9.2,<EOF>",132))
        self.assertTrue(TestLexer.test(" -1.3+1e3 ","-,1.3,+,1e3,<EOF>",133))
        self.assertTrue(TestLexer.test(" .6 ",".,6,<EOF>",134))
        self.assertTrue(TestLexer.test(" 7E15 ","7E15,<EOF>",135))
        self.assertTrue(TestLexer.test(" 1.0e ","1.0,e,<EOF>",136))
        self.assertTrue(TestLexer.test("4.1e3 ","4.1e3,<EOF>",137))
        self.assertTrue(TestLexer.test("  3.5e-8","3.5e-8,<EOF>",138))
        self.assertTrue(TestLexer.test(" 5e-8+6 ","5e-8,+,6,<EOF>",139))
        self.assertTrue(TestLexer.test(" 5.1+1e5 ","5.1,+,1e5,<EOF>",140))

    def test_string_escape(self):
        """test strings with escape"""
        self.assertTrue(TestLexer.test(""" "This is a string containing tab \t" """ ,""""This is a string containing tab \t",<EOF>""" ,141))
        self.assertTrue(TestLexer.test(""" "He asked me: \\"Where is John?\\"" """,""""He asked me: \\"Where is John?\\"",<EOF>"""    ,142))
        self.assertTrue(TestLexer.test(""" "My name is Hong Phuc Vo!" """,""""My name is Hong Phuc Vo!",<EOF>"""           ,143))
        self.assertTrue(TestLexer.test(""" "This string contains new line\n" ""","""Unclosed String: \"This string contains new line\n""",144))
        self.assertTrue(TestLexer.test(""" "This is the new line char \\n " """,""""This is the new line char \\n ",<EOF>""",145))
        self.assertTrue(TestLexer.test(""" "This is backspace \b " """,""""This is backspace \b ",<EOF>""",146))
        self.assertTrue(TestLexer.test(""" "The  \\\\ " """,""""The  \\\\ ",<EOF>""",147))
        self.assertTrue(TestLexer.test(""" "He asked me: \\"Where is John?\\" " """,""""He asked me: \\"Where is John?\\" ",<EOF>""",148))
        self.assertTrue(TestLexer.test(""" "head \t tail " """,""""head \t tail ",<EOF>""",149))
        self.assertTrue(TestLexer.test(""" "New line is saved as \\n. " """,""""New line is saved as \\n. ",<EOF>""",150))
    def test_inline_cmt(self):
        """test lines with inline cmts"""
        self.assertTrue(TestLexer.test("#This is a line cmt  ","<EOF>",151))
        self.assertTrue(TestLexer.test("""\"This string contains #.\"""",""""This string contains #.",<EOF>""",152))
        self.assertTrue(TestLexer.test("""#An inline cmt with escape \t""","<EOF>",153))
        self.assertTrue(TestLexer.test("""#An inline cmt ends with at \n #This is the second cmt""","<EOF>",154))
    def test_block_cmt(self):
        """test the block cmts"""
        self.assertTrue(TestLexer.test("""#An inline cmt \n/* before a block cmt*/ ""","<EOF>",155))
        self.assertTrue(TestLexer.test("""/*This is a block cmt*/ ""","""<EOF>""",156))
        self.assertTrue(TestLexer.test(" /* inside this block cmt is a smtblk{int a;}*/","<EOF>",157))
        self.assertTrue(TestLexer.test("/* unclosed block cmt","/,*,unclosed,block,cmt,<EOF>",158))
        self.assertTrue(TestLexer.test("/* escape in block cmt \t*/","<EOF>",159))
        self.assertTrue(TestLexer.test("/*block cmt1*/ /*block cmt2*/","<EOF>",160))

    def test_nested_cmt(self):
        """test the nested cmts"""
        self.assertTrue(TestLexer.test("#A line cmt #contains a line cmt/n","<EOF>",161))
        self.assertTrue(TestLexer.test("/* a block cmt /*cover a block cmt*/ */","*,/,<EOF>",162))
        self.assertTrue(TestLexer.test("/* A block cmt # includes a line cmt*/ ","<EOF>",163))
        self.assertTrue(TestLexer.test("/* This block cmt is followed by*/ #An inline cmt","<EOF>",164))
        self.assertTrue(TestLexer.test("/*Big block cmt #with small inline cmt\n */","<EOF>",165))


    def test_illegal_str(self):
        """illegal char, unclose, escape"""
        self.assertTrue(TestLexer.test(""" \"Open the string""","""Unclosed String: \"Open the string""",166))
        self.assertTrue(TestLexer.test(""""a\b b"  """,""""a\b b",<EOF>""",167))
        self.assertTrue(TestLexer.test(""" \"Open the string \h \"""","""Illegal Escape In String: \"Open the string \h""",168))
        self.assertTrue(TestLexer.test(""" \"Open the string \n\"""","""Unclosed String: \"Open the string \n""",169))

    def test_keyword(self):
        """keyword list"""
        self.assertTrue(TestLexer.test(" class nil this","class,nil,this,<EOF>",170))
        self.assertTrue(TestLexer.test(" if then else","if,then,else,<EOF>",171))
        self.assertTrue(TestLexer.test(" for to do","for,to,do,<EOF>",172))
        self.assertTrue(TestLexer.test(" for downto do","for,downto,do,<EOF>",173))
        self.assertTrue(TestLexer.test(" break continue","break,continue,<EOF>",174))
        self.assertTrue(TestLexer.test(" void return","void,return,<EOF>",175))
        self.assertTrue(TestLexer.test(" class extends new","class,extends,new,<EOF>",176))
        self.assertTrue(TestLexer.test(" int void float","int,void,float,<EOF>",177))
        self.assertTrue(TestLexer.test(" boolean string","boolean,string,<EOF>",178))
        self.assertTrue(TestLexer.test(" true false","true,false,<EOF>",179))
        self.assertTrue(TestLexer.test(" static final","static,final,<EOF>",180))

    def test_full(self):
        """all of the token"""
        self.assertTrue(TestLexer.test("int aAbB","int,aAbB,<EOF>",181))
        self.assertTrue(TestLexer.test("-8+9 10","-,8,+,9,10,<EOF>",182))
        self.assertTrue(TestLexer.test("_var:=1.9","_var,:=,1.9,<EOF>",183))
        self.assertTrue(TestLexer.test("class Shape","class,Shape,<EOF>",184))
        self.assertTrue(TestLexer.test("for i:=1 to 10 do","for,i,:=,1,to,10,do,<EOF>",185))
        self.assertTrue(TestLexer.test("static x;","static,x,;,<EOF>",186))
        self.assertTrue(TestLexer.test("this.name:=1998","this,.,name,:=,1998,<EOF>",187))
        self.assertTrue(TestLexer.test("x.head==7","x,.,head,==,7,<EOF>",188))
        self.assertTrue(TestLexer.test("123class","123,class,<EOF>",189))
        self.assertTrue(TestLexer.test("12.5_count","12.5,_count,<EOF>",190))
        self.assertTrue(TestLexer.test("$no idea","Error Token $",191))
        self.assertTrue(TestLexer.test("""string str:=\"content\"""","""string,str,:=,\"content\",<EOF>""",192))

    def test_prog(self):
        """a full program"""
        input = """class School{
        int id;
        void print(){
        int a=100;
        io.writeInt(a);}
        }"""
        expect = "class,School,{,int,id,;,void,print,(,),{,int,a,=,100,;,io,.,writeInt,(,a,),;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 193))
        input = """class A{int main(){}"""
        expect = "class,A,{,int,main,(,),{,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 194))
        input = """class X{
        int[2]m;
         void X(){
         m:={1,2};}}"""
        expect = "class,X,{,int,[,2,],m,;,void,X,(,),{,m,:=,{,1,,,2,},;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 195))
        input = """class X{
        void print(int a; float b{}}"""
        expect = "class,X,{,void,print,(,int,a,;,float,b,{,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 196))
        input = """class X{
        int a;
        void X(){ this.a=((5*8)-123;}"""
        expect = "class,X,{,int,a,;,void,X,(,),{,this,.,a,=,(,(,5,*,8,),-,123,;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 197))
        input = """classX{
        void print(string str){io.writeString(str);}
        void main(){this.print("");}}"""
        expect = """classX,{,void,print,(,string,str,),{,io,.,writeString,(,str,),;,},void,main,(,),{,this,.,print,(,"",),;,},},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 198))
        input = """class A{int b;}
        class B extends A{ int d;}"""
        expect = """class,A,{,int,b,;,},class,B,extends,A,{,int,d,;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 199))

        input = """class A{void x(){}}
        class B extends A{void x(){/*cmt*/}}"""
        expect = "class,A,{,void,x,(,),{,},},class,B,extends,A,{,void,x,(,),{,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 200))





