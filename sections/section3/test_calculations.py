import unittest
from code.my_calculations import Calculations

class TestCalculations(unittest.TestCase):
    def test_sum(self):
        c = Calculations(8, 2)
        self.assertEqual(c.get_sum(), 10, "Sum is incorrect.")

    def test_difference(self):
        c = Calculations(8, 2)
        self.assertEqual(c.get_difference(), 6)

    def test_product(self):
        c = Calculations(8, 2)
        self.assertEqual(c.get_product(), 16)

    def test_quotient(self):
        c = Calculations(8, 2)
        self.assertEqual(c.get_quotient(), 4)

if __name__ == "__main__":
    unittest.main(verbosity=2)
