import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,204))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,205))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,206))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,207))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,208))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,209))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,210))

    def test_more_complex_program(self):
        """More complex program"""
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,211))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,212))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,213))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,214))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,215))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,216))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,217))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,218))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,219))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,220))
    
    def test_wrong_miss_close(self):
        """Miss ) int main( {}"""
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,221))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,222))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,223))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,224))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,225))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,226))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,227))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,228))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,229))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,230))


    def test_   (self):
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,231))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,232))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,233))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,234))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,235))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,236))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,237))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,238))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,239))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,240))

    def test_a   (self):
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,241))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,242))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,243))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,244))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,245))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,246))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,247))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,248))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,249))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,250))

    def test_b   (self):
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,251))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,252))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,253))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,254))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,255))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,256))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,257))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,258))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,259))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,260))

    def test_c   (self):
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,261))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,262))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,263))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,264))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,265))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,266))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,267))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,268))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,269))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,270))

    def test_d   (self):
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,271))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,272))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,273))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,274))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,275))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,276))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,277))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,278))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,279))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,280))

    def test_e   (self):
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,281))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,282))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,283))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,284))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,285))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,286))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,287))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,288))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,289))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,290))

    def test_f   (self):
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,291))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,292))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,293))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,294))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,295))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,296))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,297))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,298))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,299))
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,300))
