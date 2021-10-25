import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: class main {} """
        input = """class main {int a;}"""
        expect = """Program([ClassDecl(Id(main),[AttributeDecl(Instance,VarDecl(Id(a),IntType))])])"""
        self.assertTrue(TestAST.test(input,expect,300))

    def test_class_with_one_decl_program(self):
        """More complex program"""
        input = """class A{int x(){break;}}"""
        expect = """Program([ClassDecl(Id(A),[MethodDecl(Id(x),Instance,[],IntType,Block([],[Break]))])])"""
        self.assertTrue(TestAST.test(input,expect,301))
