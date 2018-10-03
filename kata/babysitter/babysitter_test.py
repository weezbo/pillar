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
        self.assertEqual(calculate_hours_for_period('0000', '0400'), 4)
        self.assertEqual(calculate_hours_for_period('0200', '0400'), 2)
        #only wanting whole hours, rounded up
        self.assertEqual(calculate_hours_for_period('0200', '0230'), 1)

