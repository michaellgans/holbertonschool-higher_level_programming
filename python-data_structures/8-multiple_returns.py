#!/usr/bin/python3

def multiple_returns(sentence):
    
    if sentence == "":
        first = None
    else:
        first = sentence[0]
    length = len(sentence)

    return length, first
