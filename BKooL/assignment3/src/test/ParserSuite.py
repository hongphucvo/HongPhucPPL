import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        input = """class A{int x(){ int m;for a:=4.5 to 10 do {int x;}}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))