from .support import BaseTest

from hepfab import util

class TestDigits(BaseTest):
    
    def test_ten(self):
        self.assertEqual(util.digits(10), 2)
    
    def test_zero(self):
        self.assertEqual(util.digits(0), 1)
    
    def test_negative(self):
        self.assertEqual(util.digits(-11), 2)
