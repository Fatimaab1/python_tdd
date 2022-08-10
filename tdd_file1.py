import unittest

from calc import Simplecalc
import unitest
import pytest

class Caltests(unittest.TestCase):
    calc_obj = Simplecalc()

    def test_add(self):
        self.assertEqual(self.calc_obj.add(2, 4), 6)

    def test_subtract(self):
        self.assertEqual(self.calc_obj.subtract(4, 2), 2)

    def test_multiply(self):
        self.assertEqual(self.calc_obj.multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(self.calc_obj.divide(6, 3), 2)

