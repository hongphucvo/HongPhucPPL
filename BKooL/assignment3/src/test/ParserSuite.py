import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        input = """class A{int x(){break;}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))