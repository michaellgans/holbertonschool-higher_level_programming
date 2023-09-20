""" Unitest for max_integer """

import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """ Class for testing max integer """
    def test_max_end(self):
        """ Max number at the end """
        test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(max_integer(test_list), 9)

    def test_max_beginning(self):
        """ Max number at the beginning """
        test_list = [9, 4, 1]
        self.assertEqual(max_integer(test_list), 9)

    def test_max_middle(self):
        """ Max number in the middle """
        test_list = [4, 9, 1]
        self.assertEqual(max_integer(test_list), 9)

    def test_one_negative(self):
        """ One negative number in list """
        test_list = [-1, 3, 9]
        self.assertEqual(max_integer(test_list), 9)

    def test_all_negative(self):
        """ All negative numbers """
        test_list = [-1, -2, -3]
        self.assertEqual(max_integer(test_list), -1)

    def test_short_lsit(self):
        """ Just one number in list """
        test_list = [1]
        self.assertEqual(max_integer(test_list), 1)

    def test_empty_list(self):
        """ Empty list """
        test_list = []
        self.assertEqual(max_integer(test_list), None)
