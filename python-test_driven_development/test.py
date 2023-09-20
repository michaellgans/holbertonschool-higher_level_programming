#!/usr/bin/python3
""" Unitest for my_func """

import unittest
my_func = __import__("File_Name").my_func


class Test_My_Class(unittest.TestCase):
    """ Class for testing my_func """ <----
    def test_normal_behavior(self):
        """ Documentation """
        my_test = my_data
        self.assertEqual(my_func(my_test), my_answer)

    def test_wrong_type(self):
        """ Documentation """
        my_test = my_data
        self.assertEqual(my_func(my_test), my_answer)

    def test_one_arg_missing(self):
        """ Documentation """
        my_test = my_data
        self.assertEqual(my_func(my_test), my_answer)

    def test_all_args_missing(self):
        """ Documentation """
        my_test = my_data
        self.assertEqual(my_func(my_test), my_answer)

    def test_data_out_of_range(self):
        """ Documentation """
        my_test = my_data
        self.assertEqual(my_func(my_test), my_answer)

    def test_None_passed(self):
        """ Documentation """
        my_test = my_data
        self.assertEqual(my_func(my_test), my_answer)

    def test_optional(self):
        """ Documentation """
        my_test = my_data
        self.assertEqual(my_func(my_test), my_answer)
