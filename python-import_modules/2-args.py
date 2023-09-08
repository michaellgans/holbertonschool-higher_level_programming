#!/usr/bin/python3

import sys #allows access to args

if __name__ == "__main__":
    if len(sys.argv) == 1:
        x = 0
        print("{} arguments.".format(x)) #no arguments passed
    elif len(sys.argv) == 2:
        x = 1
        print("{} argument:".format(x)) #one argument passed
        print("{}: {}".format(x, sys.argv[1])) #print single argument
    else:
        x = len(sys.argv) - 1
        print("{} arguments:".format(x)) #more than one arguments passed
        for y in range(1, len(sys.argv)):
            print("{}: {}".format(y, sys.argv[y])) #print each argument
