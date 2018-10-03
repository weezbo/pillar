import unittest
from babysitter import *
class BabysitterTests(unittest.TestCase):
    def test_enforce_minimum_time(self):
        self.assertEqual(babysitter_pay_calc(12, 4, 14), "Start or end time is out of bounds")
