import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_lowercase_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("count","count,<EOF>",101))
        self.assertTrue(TestLexer.test("_count","_count,<EOF>",102))
        self.assertTrue(TestLexer.test("0_count","Error Token 0",103))
        self.assertTrue(TestLexer.test("$count","Error Token $",104))
        self.assertTrue(TestLexer.test("_count total","_count,total,<EOF>",105))
        self.assertTrue(TestLexer.test("_count 123total","_count,Error Token 1",106))
        self.assertTrue(TestLexer.test("$count total","Error Token $",107))
        self.assertTrue(TestLexer.test("_count x1","_count,x1,<EOF>",108))
        self.assertTrue(TestLexer.test("_count_id","_count_id,<EOF>",109))
        self.assertTrue(TestLexer.test("count_id1","count_id1,<EOF>",110))
    def test_lower_upper_id(self):
        """test mix identifiers"""
        self.assertTrue(TestLexer.test("cOuNt","cOuNt,<EOF>",111))
        self.assertTrue(TestLexer.test("_COUNT","_COUNT,<EOF>",112))
        self.assertTrue(TestLexer.test("0_Count","Error Token 0",113))
        self.assertTrue(TestLexer.test("$Count","Error Token $",114))
        self.assertTrue(TestLexer.test("_count TOTAL","_count,TOTAL,<EOF>",115))
        self.assertTrue(TestLexer.test("_CoUnt 123total","_CoUnt,Error Token 1",116))
        self.assertTrue(TestLexer.test("$count123 total","Error Token $",117))
        self.assertTrue(TestLexer.test("_count X1","_count,X1,<EOF>",118))
        self.assertTrue(TestLexer.test("_countID","_countID,<EOF>",119))
        self.assertTrue(TestLexer.test("_count_ID1","_count_ID1,<EOF>",120))
    def test_mixed_id(self):
        '''self.assertTrue(TestLexer.test("aAsVN3","aAsVN,3,<EOF>",103))'''
    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.test(" 12345 ","12345,<EOF>",121))
        self.assertTrue(TestLexer.test(" +6 ","+6,<EOF>",122))
        self.assertTrue(TestLexer.test("-7  ","-7,<EOF>",123))
        self.assertTrue(TestLexer.test(" 6 78 "," 6,78,<EOF>",124))
        self.assertTrue(TestLexer.test(" 150 000 "," 150 000,<EOF>",125))
        self.assertTrue(TestLexer.test(" -7.6 -5 ","-7,Error Token .",126))
        self.assertTrue(TestLexer.test(" 5 0.03 ","5,0,Error Token .",127))
        self.assertTrue(TestLexer.test(" 5a37 ","5,Error Token a",128))
        self.assertTrue(TestLexer.test("a123","Error Token a",129))
        self.assertTrue(TestLexer.test(" 5+100 ","5,+100,<EOF>",130))
    def test_float(self):
        """test integers"""
        self.assertTrue(TestLexer.test(" 7.5 0.6 ","7.5,0.6,<EOF>",131))
        self.assertTrue(TestLexer.test(" 6.8+9.2 ","6.8,+9.2,<EOF>",132))
        self.assertTrue(TestLexer.test(" -1.3+1e3 ","-1.3,+1e3,<EOF>",133))
        self.assertTrue(TestLexer.test(" .6 ","Error Token .,<EOF>",134))
        self.assertTrue(TestLexer.test(" 7E15 ","7E15,<EOF>",135))
        self.assertTrue(TestLexer.test(" 1.0e ","1.0,Error Token e,<EOF>",136))
        #self.assertTrue(TestLexer.test(" 143 "," ,<EOF>",137))
        self.assertTrue(TestLexer.test("  "," ,<EOF>",138))
        self.assertTrue(TestLexer.test("  "," ,<EOF>",139))
        self.assertTrue(TestLexer.test("  "," ,<EOF>",140))
    def test_string_escape(self):
        """test strings with escape"""
        self.assertTrue(TestLexer.test("\"This is a string containing tab \t\" "   ,"\"This is a string containing tab \t\",<EOF>" ,141))
        self.assertTrue(TestLexer.test("\"He asked me: \"Where is John?\"\" "      ,"\"He asked me: \"Where is John?\"\",<EOF>"    ,142))
        self.assertTrue(TestLexer.test("\"My name is Hong Phuc Vo!\""               ,"\"My name is Hong Phuc Vo!\",<EOF>"           ,143))
        self.assertTrue(TestLexer.test("\"This string contain new line \n \""      ,"\"This string contain new line \n \",<EOF>",144))
        self.assertTrue(TestLexer.test("\"This is the new line char \\n \" ","\"This is the new line syntax \\n \",<EOF>",145))
        self.assertTrue(TestLexer.test("\"This is backspace char \b\"","\"This is backspace char \b\",<EOF>",146))
        self.assertTrue(TestLexer.test("\"The comment starts with \\\\\"  ","\"The comment starts with \\\\\",<EOF>",147))
        self.assertTrue(TestLexer.test("\"first line\nsecond line\"","\"first line\nsecond line\",<EOF>",148))
        self.assertTrue(TestLexer.test("\"head \t tail\"","\"head \t tail\",<EOF>",149))
        self.assertTrue(TestLexer.test("\"New line is saved as \\n.\"","\"New line is saved as \\n.\",<EOF>",150))
    def test_inline_cmt(self):
        """test lines with inline cmts"""
        self.assertTrue(TestLexer.test("\\\\This is a line cmt  ","\\\\This is a line cmt,<EOF>",151))
        self.assertTrue(TestLexer.test("\"This string contains \\\\.\"","\"This string contains \\\\.\",<EOF>",152))
        self.assertTrue(TestLexer.test("\\\\An inline cmt with escape \t","\\\\An inline cmt with escape \t,<EOF>",153))
        self.assertTrue(TestLexer.test("\\\\An inline cmt ends with at \n \\\\This is the second cmt","\\\\An inline cmt ends with at \n \\\\This is the second cmt,<EOF>",154))
        self.assertTrue(TestLexer.test("\\\\An inline cmt \n \\* before a block cmt*\\  ","\\\\An inline cmt \n \\* before a block cmt*\\,<EOF>",155))
    def test_block_cmt(self):
        """test the block cmts"""
        self.assertTrue(TestLexer.test("\\*This is a block cmt*\\ ","\\*This is a block cmt*\\,<EOF>",156))
        self.assertTrue(TestLexer.test(" \\* inside this block cmt is a smtblk{int a;}*\\","\\* inside this block cmt is a smtblk{int a;}*\\,<EOF>",157))
        self.assertTrue(TestLexer.test("\\* unclosed block cmt","Unclosed comment",158))
        self.assertTrue(TestLexer.test("\\* escape in block cmt \t*\\","\\* escape i block cmt \t*\\,<EOF>",159))
        self.assertTrue(TestLexer.test("\\*block cmt1*\\ \\*block cmt2*\\","\\*block cmt1*\\ \\*block cmt2*\\,<EOF>",160))
    def test_nested_cmt(self):
        """test the nested cmts"""
        self.assertTrue(TestLexer.test("\\\\A line cmt \\\\contains a line cmt\\n","\\\\A line cmt \\\\contains a line cmt\\n,<EOF>",161))
        self.assertTrue(TestLexer.test("\\* a block cmt \\*cover a block cmt*\\ *\\","\\* a block cmt \\*cover a block cmt*\\,Error Token *",162))
        self.assertTrue(TestLexer.test("\\* A block cmt \\\\ includes a line cmt*\\ ","\\* A block cmt \\\\ includes a line cmt*\\,<EOF>",163))
        self.assertTrue(TestLexer.test("\\* This block cmt is followed by*\\ \\\\An inline cmt","\\* This block cmt is followed by*\\ \\\\An inline cmt,<EOF>",164))
        self.assertTrue(TestLexer.test("\\*Big block cmt \\\\with small inline cmt\n *\\","\\*Big block cmt \\\\with small inline cmt\n *\\,<EOF>",165))
    def test_illegal_str(self):
        """illegal char, unclose, escape"""
        self.assertTrue(TestLexer.test(" \"Open the string","Unclosed string,<EOF>",166))
        self.assertTrue(TestLexer.test(" \"string with strange character \p \"","\"string with strange character,Illegal Escape,<EOF>",167))
        self.assertTrue(TestLexer.test(" "," ,<EOF>",168))
        self.assertTrue(TestLexer.test(" "," ,<EOF>",169))
        self.assertTrue(TestLexer.test(" "," ,<EOF>",170))
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
        self.assertTrue(TestLexer.test("-8+9 10","-8,+9,10,<EOF>",182))
        self.assertTrue(TestLexer.test("_var:=1.9","_var,:=,1.9,<EOF>",183))
        self.assertTrue(TestLexer.test("class Shape","class,Shape,<EOF>",184))
        self.assertTrue(TestLexer.test("for i:=1 to 10 do","for,i,:=,1,to,10,do,<EOF>",185))
        self.assertTrue(TestLexer.test("static x;","static,x,;,<EOF>",186))
        self.assertTrue(TestLexer.test("this.name:=1998","this,.,name,:=,1998,<EOF>",187))
        self.assertTrue(TestLexer.test("x.head==7","x,.,head,==,7,<EOF>",188))
        self.assertTrue(TestLexer.test("123class","123,class,<EOF>",189))
        self.assertTrue(TestLexer.test("12.5_count","12.5,_count,<EOF>",190))
        self.assertTrue(TestLexer.test("$no idea","Error token $",191))
        self.assertTrue(TestLexer.test("string str:=\"content\"","string,str,:=,\"content\",<EOF>",192))
        self.assertTrue(TestLexer.test(""," ,<EOF>",193))
        self.assertTrue(TestLexer.test(" "," ,<EOF>",194))
        self.assertTrue(TestLexer.test(" "," ,<EOF>",195))
        self.assertTrue(TestLexer.test(" "," ,<EOF>",196))
        self.assertTrue(TestLexer.test(" "," ,<EOF>",197))
        self.assertTrue(TestLexer.test(" "," ,<EOF>",198))
        self.assertTrue(TestLexer.test(" "," ,<EOF>",199))
        self.assertTrue(TestLexer.test(" "," ,<EOF>",200))