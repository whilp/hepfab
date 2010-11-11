from .support import BaseTest

from hepfab.util import *

class TestDigits(BaseTest):
    
    def test_ten(self):
        self.assertEqual(digits(10), 2)
    
    def test_zero(self):
        self.assertEqual(digits(0), 1)
    
    def test_negative(self):
        self.assertEqual(digits(-11), 2)

class TestGenrange(BaseTest):
    
    def test_simple(self):
        gen = list(genrange("g10", 24))
        self.assertEqual(len(gen), 24)
        self.assertEqual(gen[0], "g10n01")
        self.assertEqual(gen[-1], "g10n24")

    def test_startstop(self):
        gen = list(genrange("g10", 10, 24))
        self.assertEqual(len(gen), 15)
        self.assertEqual(gen[0], "g10n10")
        self.assertEqual(gen[-1], "g10n24")

    def test_starstopstep(self):
        gen = list(genrange("g10", 10, 24, 2))
        self.assertEqual(len(gen), 8)
        self.assertEqual(gen[0], "g10n10")
        self.assertEqual(gen[1], "g10n12")
        self.assertEqual(gen[-1], "g10n24")
