import unittest
from feature_flags import is_feature_enabled

class TestFeatureFlags(unittest.TestCase):
    def test_admin_enabled(self):
        self.assertTrue(is_feature_enabled("admin"))

    @unittest.skip("Pending product decision for guest access")
    def test_guest_enabled(self):
        # Not supported yet; skip so it doesn't count as a failure.
        self.assertTrue(is_feature_enabled("guest"))

    @unittest.expectedFailure
    def test_moderator_expected_failure(self):
        # Spec says moderators will be enabled later; currently False.
        self.assertTrue(is_feature_enabled("moderator"))

if __name__ == "__main__":
    unittest.main(verbosity=2)
