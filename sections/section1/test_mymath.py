import unittest
import mymath

class TestMyMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(mymath.add(2, 3), 5)
        self.assertEqual(mymath.add(-1, 1), 0)

if __name__ == "__main__":
    unittest.main(verbosity=2)
