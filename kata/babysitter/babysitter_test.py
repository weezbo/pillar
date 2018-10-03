import unittest
from babysitter import *
class BabysitterTests(unittest.TestCase):
    def test_calculate_standard_total(self):
        self.assertEqual(calculate_total_for_period(4, 12), 48)
        self.assertEqual(calculate_total_for_period(3, 12), 36)
    def test_calculate_post_bedtime_total(self):
        self.assertEqual(calculate_total_for_period(2, 8), 16)
        self.assertEqual(calculate_total_for_period(0, 8), 0)
        self.assertEqual(calculate_total_for_period(1, 8), 8)
    def test_calculate_post_midnight_total(self):
        self.assertEqual(calculate_total_for_period(3, 16), 48)
        self.assertEqual(calculate_total_for_period(2, 16), 32)
    def test_calculate_hours_for_after_midnight(self):
        self.assertEqual(calculate_hours_for_period(0, 4), 4)
        self.assertEqual(calculate_hours_for_period(2, 4), 2)
    def test_calculate_hours_before_midnight(self):
        self.assertEqual(calculate_hours_for_period(17, 23), 6)
        self.assertEqual(calculate_hours_for_period(18, 23), 5)
    def test_calculate_hours_for_full_shift(self):
        self.assertEqual(calculate_hours_for_period(18, 3), 9)
        self.assertEqual(calculate_hours_for_period(23, 2), 3)
    def test_calculate_pre_midnight_total_no_bedtime(self):
        self.assertEqual(babysitter_pay_calc(20, 0), 48)

