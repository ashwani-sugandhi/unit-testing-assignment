import unittest
from strings import normalize

class TestStrings(unittest.TestCase):
    def setUp(self):
        # Runs before every test method
        self.samples = [
            ("  Hello   World  ", "hello world"),
            ("\nTabs\tand   Spaces  ", "tabs and spaces"),
            ("MiXeD CaSe", "mixed case"),
        ]

    def tearDown(self):
        # Runs after every test method
        # (Here we don’t need cleanup, but we include it for structure.)
        pass

    def test_normalize_many(self):
        # subTest lets each (input, expected) pair report separately
        for raw, expected in self.samples:
            with self.subTest(raw=raw):
                self.assertEqual(normalize(raw), expected)

if __name__ == "__main__":
    unittest.main(verbosity=2)
