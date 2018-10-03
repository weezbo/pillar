import unittest
from babysitter import *
class BabysitterTests(unittest.TestCase):
    def test_enforce_minimum_time(self):
        self.assertEqual(babysitter_pay_calc(12, 4), "Start or end time is out of bounds")
        #whoops, we can start after midnight
        self.assertEqual(babysitter_pay_calc(3, 4), "Acceptable times")
        #also should allow starting at 17 but not starting at 4
        self.assertEqual(babysitter_pay_calc(17, 4), "Acceptable times")
        self.assertEqual(babysitter_pay_calc(4, 4), "Start or end time is out of bounds")
