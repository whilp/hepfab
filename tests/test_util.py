from .support import BaseTest

from hepfab.util import *

class TestDigits(BaseTest):
    
    def test_ten(self):
        self.assertEqual(digits(10), 2)
    
    def test_zero(self):
        self.assertEqual(digits(0), 1)
    
    def test_negative(self):
        self.assertEqual(digits(-11), 2)
