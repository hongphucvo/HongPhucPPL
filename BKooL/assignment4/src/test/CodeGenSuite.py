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
    def test_bkool_float_ast(self):
        input = """class BKoolClass {static void main() {io.writeFloat(1.0);}}"""
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,504))
    
    def test_bkool_float_ast1(self):
        input = """class BKoolClass {static void main() {io.writeFloat(1.0+3.0);}}"""
        expect = "4"
        self.assertTrue(TestCodeGen.test(input,expect,505))
    
    