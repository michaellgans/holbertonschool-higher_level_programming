#!/usr/bin/python3

def number_keys(a_dic):
    return (0 if not isinstance(a_dic, dict)
        else len(a_dic) + sum(number_keys(val) for val in a_dic.values()))
    res = number_keys(a_dic)
    return res
