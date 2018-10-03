import unittest
from babysitter import *
class BabysitterTests(unittest.TestCase):
    def test_calculate_standard_rate(self):
        self.assertEqual(calculate_total_for_period(4, 12), 48)
        self.assertEqual(calculate_total_for_period(3, 12), 36)
    def test_calculate_post_bedtime_rate(self):
        self.assertEqual(calculate_total_for_period(2, 8), 16)
        self.assertEqual(calculate_total_for_period(0, 8), 0)
        self.assertEqual(calculate_total_for_period(1, 8), 8)

