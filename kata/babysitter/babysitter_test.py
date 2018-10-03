import unittest
from babysitter import *
class BabysitterTests(unittest.TestCase):
    def test_enforce_minimum_time(self):
        self.assertEqual(babysitter_pay_calc(12, 4), "Start time is out of bounds")
        #whoops, we can start after midnight
        self.assertEqual(babysitter_pay_calc(3, 4), "Acceptable times")
        #also should allow starting at 17 but not starting at 4
        self.assertEqual(babysitter_pay_calc(17, 4), "Acceptable times")
        self.assertEqual(babysitter_pay_calc(4, 4), "Start time is out of bounds")
    def test_enforce_maximum_end_time(self):
        self.assertEqual(babysitter_pay_calc(17, 5), "End time is out of bounds")
    def test_enforce_clock_times(self):
        self.assertEqual(babysitter_pay_calc(25, 4), "Start time is out of bounds")
        self.assertEqual(babysitter_pay_calc(-1, 4), "Start time is out of bounds")
        self.assertEqual(babysitter_pay_calc(17, 25), "End time is out of bounds")
        self.assertEqual(babysitter_pay_calc(17, -1), "End time is out of bounds")
