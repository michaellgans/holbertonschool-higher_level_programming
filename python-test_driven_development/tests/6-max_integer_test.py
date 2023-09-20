""" Unitest for max_integer """

import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """ Class for testing max integer """
    def test_max_integer(self):
        """ All integers are positive """
        test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(max_integer(test_list), 9)

