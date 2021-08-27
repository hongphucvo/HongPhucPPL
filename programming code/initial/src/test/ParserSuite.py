import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """declare"""
        input = """float goo (float a, b) {
   return 1 - foo(1, a, b);
}
c=5;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))
    
    def test_wrong_miss_close(self):
        """Variable and Function"""
        input = """float goo (float a, b) {
   return foo(1, a, b) + 1;
} """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))