import unittest
from ohlc.util1 import is_it_ascending
#from testdata1 import *
class test_compare(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp() 
        #testdata = testdata1.data1
        #print(testdata)

    #@unittest.TestCase('is down')
    def test_compare_isdown(self):
        #self.fail('it always fails')
        pass

    #@unittest.TestCase ('is up')
    def test_compare_isup(self):
        pass

if __name__ == '__main__':
    unittest.main()
    
