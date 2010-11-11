from .support import BaseTest

from hepfab import util

class TestDigits(BaseTest):
    
    def test_foo(self):
        self.assertEqual(util.digits(10), 2)
