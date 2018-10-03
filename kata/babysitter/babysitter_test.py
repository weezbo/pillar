import unittest
from babysitter import *
class BabysitterTests(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello_world(), 'hello world')