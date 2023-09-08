#!/usr/bin/python3

import sys #allows access to args

if __name__ == "__main__":
    args = sys.argv[1:] #ignores first argument, program name
    y = 1
    if len(args) == 0:
        x = 0
        print("{} arguments.".format(x)) #no arguments passed
    elif len(args) == 1:
        x = 1
        print("{} argument:".format(x)) #one argument passed
        print("{}: {}".format(x, args[0])) #print single argument
    else:
        x = len(args)
        print("{} arguments:".format(x)) #more than one arguments passed
        for x in args:
            print("{}: {}".format(y, x)) #print each argument
            y += 1
