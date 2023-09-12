#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max_key = max(a_dictionary.keys())
    if max_key is None:
        return None
    return max_key
