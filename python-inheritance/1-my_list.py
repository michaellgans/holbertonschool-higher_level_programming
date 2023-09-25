#!/usr/bin/python3
""" Creates a list called MyList """


class MyList(list):
    """ Inherits from list """
    def print_sorted(self):
        """prints a sorted list a to z"""
        copy_list = self.copy()
        copy_list.sort()
        print(copy_list)