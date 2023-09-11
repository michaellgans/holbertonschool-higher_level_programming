#!/usr/bin/python3

def multiple_returns(sentence):
    
    if not sentence:
        return
    length = len(sentence)
    first = sentence[0]

    return length, first
