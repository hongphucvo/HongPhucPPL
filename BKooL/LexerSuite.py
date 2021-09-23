import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    def test_lowercase_identifier1(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("count","count,<EOF>",101))
    def test_lowercase_identifier2(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("_count","_count,<EOF>",102))
    def test_lowercase_identifier3(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("0_count","0,_count,<EOF>",103))
    def test_lowercase_identifier4(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("$count","Error Token $",104))
    def test_lowercase_identifier5(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("_count total","_count,total,<EOF>",105))
    def test_lowercase_identifier6(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("_count 123total||x","_count,123,total,||,x,<EOF>",106))
    def test_lowercase_identifier7(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("$count total&&5","Error Token $",107))
    def test_lowercase_identifier8(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("_count x1&7","_count,x1,Error Token &",108))
    def test_lowercase_identifier9(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("_count_id","_count_id,<EOF>",109))
    def test_lowercase_identifier10(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("count_id1","count_id1,<EOF>",110))


    def test_lower_upper_id1(self):
        """test mix identifiers"""
        self.assertTrue(TestLexer.test("cOuNt","cOuNt,<EOF>",111))
    def test_lower_upper_id2(self):
        """test mix identifiers"""
        self.assertTrue(TestLexer.test("_COUNT","_COUNT,<EOF>",112))
    def test_lower_upper_id3(self):
        """test mix identifiers"""
        self.assertTrue(TestLexer.test("0_Count","0,_Count,<EOF>",113))
    def test_lower_upper_id4(self):
        """test mix identifiers"""
        self.assertTrue(TestLexer.test("$Count","Error Token $",114))
    def test_lower_upper_id5(self):
        """test mix identifiers"""
        self.assertTrue(TestLexer.test("_count TOTAL","_count,TOTAL,<EOF>",115))
    def test_lower_upper_id6(self):
        """test mix identifiers"""
        self.assertTrue(TestLexer.test("_CoUnt 123total","_CoUnt,123,total,<EOF>",116))
    def test_lower_upper_id7(self):
        """test mix identifiers"""
        self.assertTrue(TestLexer.test("$count123 total","Error Token $",117))
    def test_lower_upper_id8(self):
        """test mix identifiers"""
        self.assertTrue(TestLexer.test("_count X1","_count,X1,<EOF>",118))
    def test_lower_upper_id9(self):
        """test mix identifiers"""
        self.assertTrue(TestLexer.test("_countID","_countID,<EOF>",119))
    def test_lower_upper_id10(self):
        """test mix identifiers"""
        self.assertTrue(TestLexer.test("_count_ID1","_count_ID1,<EOF>",120))


    def test_integer1(self):
        """test integers"""
        self.assertTrue(TestLexer.test(" 12345 ","12345,<EOF>",121))
    def test_integer2(self):
        """test integers"""
        self.assertTrue(TestLexer.test(" 6 ","6,<EOF>",122))
    def test_integer3(self):
        """test integers"""
        self.assertTrue(TestLexer.test("7.3  ","7.3,<EOF>",123))
    def test_integer4(self):
        """test integers"""
        self.assertTrue(TestLexer.test(" 6 78 ","6,78,<EOF>",124))
    def test_integer5(self):
        """test integers"""
        self.assertTrue(TestLexer.test(" 150 000 ","150,000,<EOF>",125))
    def test_integer6(self):
        """test integers"""
        self.assertTrue(TestLexer.test(" -7.6 -5 ","-,7.6,-,5,<EOF>",126))
    def test_integer7(self):
        """test integers"""
        self.assertTrue(TestLexer.test(" 5 0.03 ","5,0.03,<EOF>",127))
    def test_integer8(self):
        """test integers"""
        self.assertTrue(TestLexer.test(" 5a37 ","5,a37,<EOF>",128))
    def test_integer9(self):
        """test integers"""
        self.assertTrue(TestLexer.test("a123","a123,<EOF>",129))
    def test_integer10(self):
        """test integers"""
        self.assertTrue(TestLexer.test(" 5+100 ","5,+,100,<EOF>",130))


    def test_float1(self):
        """test floats"""
        self.assertTrue(TestLexer.test(" 7.5 0.6 ","7.5,0.6,<EOF>",131))
    def test_float2(self):
        """test floats"""
        self.assertTrue(TestLexer.test(" 6.8+9.2 ","6.8,+,9.2,<EOF>",132))
    def test_float3(self):
        """test floats"""
        self.assertTrue(TestLexer.test(" -1.3+1e3 ","-,1.3,+,1e3,<EOF>",133))
    def test_float4(self):
        """test floats"""
        self.assertTrue(TestLexer.test(" .6 ",".,6,<EOF>",134))
    def test_float5(self):
        """test floats"""
        self.assertTrue(TestLexer.test(" 7E15 ","7E15,<EOF>",135))
    def test_float6(self):
        """test floats"""
        self.assertTrue(TestLexer.test(" 1.0e ","1.0,e,<EOF>",136))
    def test_float7(self):
        """test floats"""
        self.assertTrue(TestLexer.test("4.1e3 ","4.1e3,<EOF>",137))
    def test_float8(self):
        """test floats"""
        self.assertTrue(TestLexer.test("  3.5e-8","3.5e-8,<EOF>",138))
    def test_float9(self):
        """test floats"""
        self.assertTrue(TestLexer.test(" 5e-8+6 ","5e-8,+,6,<EOF>",139))
    def test_float10(self):
        """test floats"""
        self.assertTrue(TestLexer.test(" 5.1+1e5 ","5.1,+,1e5,<EOF>",140))

    def test_string_escape1(self):
        """test strings with escape"""
        self.assertTrue(TestLexer.test(""" "This is a string containing tab \t" """ ,""""This is a string containing tab \t",<EOF>""" ,141))
    def test_string_escape2(self):
        """test strings with escape"""
        self.assertTrue(TestLexer.test(""" "He asked me: \\"Where is John?\\"" """,""""He asked me: \\"Where is John?\\"",<EOF>"""    ,142))
    def test_string_escape3(self):
        """test strings with escape"""
        self.assertTrue(TestLexer.test(""" "My name is Hong Phuc Vo!" """,""""My name is Hong Phuc Vo!",<EOF>"""           ,143))
    def test_string_escape4(self):
        """test strings with escape"""
        self.assertTrue(TestLexer.test(""" "This string contains new line\n" ""","""Unclosed String: \"This string contains new line""",144))
    def test_string_escape5(self):
        """test strings with escape"""
        self.assertTrue(TestLexer.test(""" "This is the new line char \\n " """,""""This is the new line char \\n ",<EOF>""",145))
    def test_string_escape6(self):
        """test strings with escape"""
        self.assertTrue(TestLexer.test(""" "This is backspace \b " """,""""This is backspace \b ",<EOF>""",146))
    def test_string_escape7(self):
        """test strings with escape"""
        self.assertTrue(TestLexer.test(""" "The  \\\\ " """,""""The  \\\\ ",<EOF>""",147))
    def test_string_escape8(self):
        """test strings with escape"""
        self.assertTrue(TestLexer.test(""" "He asked me: \\"Where is John?\\" " """,""""He asked me: \\"Where is John?\\" ",<EOF>""",148))
    def test_string_escape9(self):
        """test strings with escape"""
        self.assertTrue(TestLexer.test(""" "head \t tail " """,""""head \t tail ",<EOF>""",149))
    def test_string_escape10(self):
        """test strings with escape"""
        self.assertTrue(TestLexer.test(""" "New line is saved as \\n. " """,""""New line is saved as \\n. ",<EOF>""",150))


    def test_inline_cmt1(self):
        """test lines with inline cmts"""
        self.assertTrue(TestLexer.test("#This is a line cmt  ","<EOF>",151))
    def test_inline_cmt2(self):
        """test lines with inline cmts"""
        self.assertTrue(TestLexer.test("""\"This string contains #.\"""",""""This string contains #.",<EOF>""",152))
    def test_inline_cmt3(self):
        """test lines with inline cmts"""
        self.assertTrue(TestLexer.test("""#An inline cmt with escape \t""","<EOF>",153))
    def test_inline_cmt4(self):
        """test lines with inline cmts"""
        self.assertTrue(TestLexer.test("""#An inline cmt ends with at \n #This is the second cmt""","<EOF>",154))


    def test_block_cmt1(self):
        """test the block cmts"""
        self.assertTrue(TestLexer.test("""#An inline cmt \n/* before a block cmt*/ ""","<EOF>",155))
    def test_block_cmt2(self):
        """test the block cmts"""
        self.assertTrue(TestLexer.test("""/*This is a block cmt*/ ""","""<EOF>""",156))
    def test_block_cmt3(self):
        """test the block cmts"""
        self.assertTrue(TestLexer.test(" /* inside this block cmt is a smtblk{int a;}*/","<EOF>",157))
    def test_block_cmt4(self):
        """test the block cmts"""
        self.assertTrue(TestLexer.test("/* unclosed block cmt","/,*,unclosed,block,cmt,<EOF>",158))
    def test_block_cmt5(self):
        """test the block cmts"""
        self.assertTrue(TestLexer.test("/* escape in block cmt \t*/","<EOF>",159))
    def test_block_cmt6(self):
        """test the block cmts"""
        self.assertTrue(TestLexer.test("/*block cmt1*/ /*block cmt2*/","<EOF>",160))

    def test_nested_cmt1(self):
        """test the nested cmts"""
        self.assertTrue(TestLexer.test("#A line cmt #contains a line cmt/n","<EOF>",161))
    def test_nested_cmt2(self):
        """test the nested cmts"""
        self.assertTrue(TestLexer.test("/* a block cmt /*cover a block cmt*/ */","*,/,<EOF>",162))
    def test_nested_cmt3(self):
        """test the nested cmts"""
        self.assertTrue(TestLexer.test("/* A block cmt # includes a line cmt*/ ","<EOF>",163))
    def test_nested_cmt4(self):
        """test the nested cmts"""
        self.assertTrue(TestLexer.test("/* This block cmt is followed by*/ #An inline cmt","<EOF>",164))
    def test_nested_cmt5(self):
        """test the nested cmts"""
        self.assertTrue(TestLexer.test("/*Big block cmt #with small inline cmt\n */","<EOF>",165))


    def test_illegal_str1(self):
        """illegal char, unclose, escape"""
        self.assertTrue(TestLexer.test(""" \"Open the string""","""Unclosed String: \"Open the string""",166))
    def test_illegal_str2(self):
        """illegal char, unclose, escape"""
        self.assertTrue(TestLexer.test(""""a\b b"  """,""""a\b b",<EOF>""",167))
    def test_illegal_str3(self):
        """illegal char, unclose, escape"""
        self.assertTrue(TestLexer.test(""" \"Open the string \h \"""","""Illegal Escape In String: \"Open the string \h""",168))
    def test_illegal_str4(self):
        """illegal char, unclose, escape"""
        self.assertTrue(TestLexer.test(""" \"Open the string \n\"""","""Unclosed String: \"Open the string """,169))

    def test_keyword1(self):
        """keyword list"""
        self.assertTrue(TestLexer.test(" class nil this","class,nil,this,<EOF>",170))
    def test_keyword2(self):
        """keyword list"""
        self.assertTrue(TestLexer.test(" if then else","if,then,else,<EOF>",171))
    def test_keyword3(self):
        """keyword list"""
        self.assertTrue(TestLexer.test(" for to do","for,to,do,<EOF>",172))
    def test_keyword4(self):
        """keyword list"""
        self.assertTrue(TestLexer.test(" for downto do","for,downto,do,<EOF>",173))
    def test_keyword5(self):
        """keyword list"""
        self.assertTrue(TestLexer.test(" break continue","break,continue,<EOF>",174))
    def test_keyword6(self):
        """keyword list"""
        self.assertTrue(TestLexer.test(" void return","void,return,<EOF>",175))
    def test_keyword7(self):
        """keyword list"""
        self.assertTrue(TestLexer.test(" class extends new","class,extends,new,<EOF>",176))
    def test_keyword8(self):
        """keyword list"""
        self.assertTrue(TestLexer.test(" int void float","int,void,float,<EOF>",177))
    def test_keyword9(self):
        """keyword list"""
        self.assertTrue(TestLexer.test(" boolean string","boolean,string,<EOF>",178))
    def test_keyword10(self):
        """keyword list"""
        self.assertTrue(TestLexer.test(" true false","true,false,<EOF>",179))
    def test_keyword11(self):
        """keyword list"""
        self.assertTrue(TestLexer.test(" static final","static,final,<EOF>",180))

    def test_full1(self):
        """all of the token"""
        self.assertTrue(TestLexer.test("int aAbB","int,aAbB,<EOF>",181))
    def test_full2(self):
        """all of the token"""
        self.assertTrue(TestLexer.test("-8+9 10","-,8,+,9,10,<EOF>",182))
    def test_full3(self):
        """all of the token"""
        self.assertTrue(TestLexer.test("_var:=1.9","_var,:=,1.9,<EOF>",183))
    def test_full4(self):
        """all of the token"""
        self.assertTrue(TestLexer.test("class Shape","class,Shape,<EOF>",184))
    def test_full5(self):
        """all of the token"""
        self.assertTrue(TestLexer.test("for i:=1 to 10 do","for,i,:=,1,to,10,do,<EOF>",185))
    def test_full6(self):
        """all of the token"""
        self.assertTrue(TestLexer.test("static x;","static,x,;,<EOF>",186))
    def test_full7(self):
        """all of the token"""
        self.assertTrue(TestLexer.test("this.name:=1998","this,.,name,:=,1998,<EOF>",187))
    def test_full8(self):
        """all of the token"""
        self.assertTrue(TestLexer.test("x.head==7","x,.,head,==,7,<EOF>",188))
    def test_full9(self):
        """all of the token"""
        self.assertTrue(TestLexer.test("123class","123,class,<EOF>",189))
    def test_full10(self):
        """all of the token"""
        self.assertTrue(TestLexer.test("12.5_count","12.5,_count,<EOF>",190))
    def test_full11(self):
        """all of the token"""
        self.assertTrue(TestLexer.test("$no idea","Error Token $",191))
    def test_full12(self):
        """all of the token"""
        self.assertTrue(TestLexer.test("""string str:=\"content\"""","""string,str,:=,\"content\",<EOF>""",192))


    def test_prog1(self):
        """a full program"""
        input = """class School{
        int id;
        void print(){
        int a=100;
        io.writeInt(a);}
        }"""
        expect = "class,School,{,int,id,;,void,print,(,),{,int,a,=,100,;,io,.,writeInt,(,a,),;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 193))
    def test_prog2(self):
        """a full program"""
        input = """class A{int main(){}"""
        expect = "class,A,{,int,main,(,),{,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 194))
    def test_prog3(self):
        """a full program"""
        input = """class X{
        int[2]m;
         void X(){
         m:={1,2};}}"""
        expect = "class,X,{,int,[,2,],m,;,void,X,(,),{,m,:=,{,1,,,2,},;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 195))
    def test_prog4(self):
        """a full program"""
        input = """class X{
        void print(int a; float b{}}"""
        expect = "class,X,{,void,print,(,int,a,;,float,b,{,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 196))
    def test_prog5(self):
        """a full program"""
        input = """class X{
        int a;
        void X(){ this.a=((5*8)-123;}"""
        expect = "class,X,{,int,a,;,void,X,(,),{,this,.,a,=,(,(,5,*,8,),-,123,;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 197))
    def test_prog6(self):
        """a full program"""
        input = """classX{
        void print(string str){io.writeString(str);}
        void main(){this.print("");}}"""
        expect = """classX,{,void,print,(,string,str,),{,io,.,writeString,(,str,),;,},void,main,(,),{,this,.,print,(,"",),;,},},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 198))
    def test_prog7(self):
        """a full program"""
        input = """class A{int b;}
        class B extends A{ int d;}"""
        expect = """class,A,{,int,b,;,},class,B,extends,A,{,int,d,;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 199))
    def test_prog8(self):
        """a full program"""
        input = """class A{void x(){}}
        class B extends A{void x(){/*cmt*/}}"""
        expect = "class,A,{,void,x,(,),{,},},class,B,extends,A,{,void,x,(,),{,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 200))

