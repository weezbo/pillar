import unittest
from babysitter import Babysitter
Babysitter = Babysitter()
PRE_BED = 12
POST_BED = 8
POST_MID = 16
class BabysitterTests(unittest.TestCase):
    def test_enforce_minimum_time(self):
        self.assertEqual(Babysitter.calculate_pay(12, 4), "Start time is out of bounds")
        #whoops, we can start after midnight
        self.assertGreater(Babysitter.calculate_pay(3, 4), 0)
        #also should allow starting at 17 but not starting at 4
        self.assertGreater(Babysitter.calculate_pay(17, 4), 0)
        self.assertEqual(Babysitter.calculate_pay(4, 4), "Start time is out of bounds")
    def test_enforce_maximum_end_time(self):
        self.assertEqual(Babysitter.calculate_pay(17, 5), "End time is out of bounds")
    def test_enforce_clock_times(self):
        self.assertEqual(Babysitter.calculate_pay(25, 4), "Start time is out of bounds")
        self.assertEqual(Babysitter.calculate_pay(-1, 4), "Start time is out of bounds")
        self.assertEqual(Babysitter.calculate_pay(17, 25), "End time is out of bounds")
        self.assertEqual(Babysitter.calculate_pay(17, -1), "End time is out of bounds")
    def test_enforce_time_direction(self):
        self.assertEqual(Babysitter.calculate_pay(19, 18), "End time must be later than start time")
        #need to check after midnight, too
        self.assertEqual(Babysitter.calculate_pay(3, 2), "End time must be later than start time")
    def test_bed_time_is_real(self):
        self.assertEqual(Babysitter.calculate_pay(3, 4, 25), "Bed time is out of bounds")
        self.assertEqual(Babysitter.calculate_pay(3, 4, -1), "Bed time is out of bounds")
    def test_pre_midnight_rate_no_bedtime(self):
        self.assertEqual(Babysitter.calculate_pay(17, 20, False), 3 * PRE_BED)
    def test_post_midnight_rate(self):
        self.assertEqual(Babysitter.calculate_pay(2, 4, 3), 2 * POST_MID)
    def test_cross_midnight_rate_no_bedtime(self):
        self.assertEqual(Babysitter.calculate_pay(23, 2, False), (1 * PRE_BED) + (2 * POST_MID))
    def test_pre_midnight_rate_with_bedtime(self):
        self.assertEqual(Babysitter.calculate_pay(17, 23, 19), (2 * PRE_BED) + (4 * POST_BED))
    def test_cross_midnight_rate_with_bedtime(self):
        self.assertEqual(Babysitter.calculate_pay(17, 4, 19), (2 * PRE_BED) + (5 * POST_BED) + (4 * POST_MID))
    def test_ends_at_midnight_with_bedtime(self):
        self.assertEqual(Babysitter.calculate_pay(17, 0, 19), (2 * PRE_BED) + (5 * POST_BED))
        self.assertEqual(Babysitter.calculate_pay(17, 24, 19), (2 * PRE_BED) + (5 * POST_BED))
    def test_cross_midnight_midnight_bedtime(self):
        self.assertEqual(Babysitter.calculate_pay(23, 2, 0), (1 * PRE_BED) + (2 * POST_MID))
        self.assertEqual(Babysitter.calculate_pay(23, 4, 24), (1 * PRE_BED) + (4 * POST_MID))
    def test_equal_start_and_end_time(self):
        self.assertEqual(Babysitter.calculate_pay(18, 18, 19), "End time must be later than start time")
    def test_early_bedtime(self):
        self.assertEqual(Babysitter.calculate_pay(17, 4, 14), (7 * POST_BED) + (4 * POST_MID))