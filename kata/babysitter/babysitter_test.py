import unittest
from babysitter import *
pre_bed = 12
post_bed = 8
post_mid = 16
class BabysitterTests(unittest.TestCase):
    def test_enforce_minimum_time(self):
        self.assertEqual(babysitter_pay_calc(12, 4), "Start time is out of bounds")
        #whoops, we can start after midnight
        self.assertGreater(babysitter_pay_calc(3, 4), 0)
        #also should allow starting at 17 but not starting at 4
        self.assertGreater(babysitter_pay_calc(17, 4), 0)
        self.assertEqual(babysitter_pay_calc(4, 4), "Start time is out of bounds")
    def test_enforce_maximum_end_time(self):
        self.assertEqual(babysitter_pay_calc(17, 5), "End time is out of bounds")
    def test_enforce_clock_times(self):
        self.assertEqual(babysitter_pay_calc(25, 4), "Start time is out of bounds")
        self.assertEqual(babysitter_pay_calc(-1, 4), "Start time is out of bounds")
        self.assertEqual(babysitter_pay_calc(17, 25), "End time is out of bounds")
        self.assertEqual(babysitter_pay_calc(17, -1), "End time is out of bounds")
    def test_enforce_time_direction(self):
        self.assertEqual(babysitter_pay_calc(19, 18), "End time must be later than start time")
        #need to check after midnight, too
        self.assertEqual(babysitter_pay_calc(3, 2), "End time must be later than start time")
    def test_bed_time_is_real(self):
        self.assertEqual(babysitter_pay_calc(3, 4, 25), "Bed time is out of bounds")
        self.assertEqual(babysitter_pay_calc(3, 4, -1), "Bed time is out of bounds")
    def test_pre_midnight_rate_no_bedtime(self):
        self.assertEqual(babysitter_pay_calc(17, 20, False), 3 * pre_bed)
    def test_post_midnight_rate(self):
        self.assertEqual(babysitter_pay_calc(2, 4, 3), 2 * post_mid)
    def test_cross_midnight_rate_no_bedtime(self):
        self.assertEqual(babysitter_pay_calc(23, 2, False), (1 * pre_bed) + (2 * post_mid))
    def test_pre_midnight_rate_with_bedtime(self):
        self.assertEqual(babysitter_pay_calc(17, 23, 19), (2 * pre_bed) + (4 * post_bed))
    def test_cross_midnight_rate_with_bedtime(self):
        self.assertEqual(babysitter_pay_calc(17, 4, 19), (2 * pre_bed) + (5 * post_bed) + (4 * post_mid))
    def test_ends_at_midnight_with_bedtime(self):
        self.assertEqual(babysitter_pay_calc(17, 0, 19), (2 * pre_bed) + (5 * post_bed))
        self.assertEqual(babysitter_pay_calc(17, 24, 19), (2 * pre_bed) + (5 * post_bed))
    def test_cross_midnight_midnight_bedtime(self):
        self.assertEqual(babysitter_pay_calc(23, 2, 0), (1 * pre_bed) + (2 * post_mid))
        self.assertEqual(babysitter_pay_calc(23, 4, 24), (1 * pre_bed) + (4 * post_mid))
    def test_equal_start_and_end_time(self):
        self.assertEqual(babysitter_pay_calc(18,18,19), "End time must be later than start time")
    def test_early_bedtime(self):
        self.assertEqual(babysitter_pay_calc(17, 4, 14), (7 * post_bed) + (4 * post_mid ))