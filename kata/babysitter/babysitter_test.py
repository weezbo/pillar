import unittest
from babysitter import *
class BabysitterTests(unittest.TestCase):
    def test_calculate_standard_rate(self):
        self.assertEqual(calculate_total_for_period(4, 12), 48)
