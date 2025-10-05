import unittest
from datetime import datetime
from clock import greeting

def fixed_time(h, m=0):
    # Returns a callable that mimics datetime.now()
    return lambda: datetime(2025, 1, 1, h, m, 0)

class TestClock(unittest.TestCase):
    def test_morning(self):
        self.assertEqual(greeting(fixed_time(9)), "good morning")

    def test_afternoon(self):
        self.assertEqual(greeting(fixed_time(15)), "good afternoon")

    def test_evening(self):
        self.assertEqual(greeting(fixed_time(19)), "good evening")

    def test_night(self):
        self.assertEqual(greeting(fixed_time(2)), "hello night owl")

if __name__ == "__main__":
    unittest.main(verbosity=2)
