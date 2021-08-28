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
        input = """int a, b,c;
                   float foo(int a; float c, d) {
                      int e ;
                      e = a + 4 ;
                      c = a * d / 2.0 ;
                      return c + 1
}
                   float goo (float a, b) {
                      return foo(1, a, b);
                   }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))