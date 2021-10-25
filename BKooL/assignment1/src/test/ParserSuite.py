
import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):


    def test_simple_test1(self):
        input = """class Test {
            void main(){}
            void main(){
                int i = 0, s = 0;
                for i := 1 to 10 do
                float c = 1.e3;
                s := s + i;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))