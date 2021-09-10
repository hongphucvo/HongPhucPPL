
import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: 1 stm """
        input = """class A{int main(){}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
        input = """class A{int main(){
  return 0;}
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))
        input = """class A{int main(){
  float number, root;
  }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))
        input = """class A{
int main(){
final float number = 7.0, root=2.3;}
}"""
        expect = "Error on line 3 col 19: ="
        self.assertTrue(TestParser.test(input, expect, 204))
        input = """class A{int main(){
static float number=9.0; int root;}
}"""
        expect = "Error on line 2 col 0: static"
        self.assertTrue(TestParser.test(input, expect, 205))
        input = """class A{static int main(){
float number=7.3, root;}
}"""
        expect = "Error on line 2 col 12: ="
        self.assertTrue(TestParser.test(input, expect, 206))
        input = """class A{int main(){
  float number = root;}
}"""
        expect = "Error on line 2 col 15: ="
        self.assertTrue(TestParser.test(input, expect, 207))
        input = """class A{int main(){
  io.writeFloat(root);}
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))
        input = """class A{int main(){
  io.writeFloat(7*9-10);}
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 209))
        input = """class A{int main(){
        #This is a line cmt
}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))