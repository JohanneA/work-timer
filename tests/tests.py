import unittest
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from src.timer import *

class TestTimer(unittest.TestCase):

    def setUp(self):
        pass

    def test_small_numbers(self):
        self.assertEquals()

if __name__ == '__main__':
    unittest.main()
