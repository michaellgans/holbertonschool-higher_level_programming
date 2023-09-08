#!/usr/bin/python3
import sys #allows access to command line args
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("0 arguments.") #no arguments passed, only program name
    elif len(sys.argv) == 2:
        print("1 argument:") #one argument passed
        print("1: {}".format(sys.argv[1])) #print single argument
    else:
        print("{} arguments:".format(len(sys.argv) - 1)) #more than one arguments passed
        for x in range(1, len(sys.argv)):
            print("{}: {}".format(x, sys.argv[x])) #print each argument
