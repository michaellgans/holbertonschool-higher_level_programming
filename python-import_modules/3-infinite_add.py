#!/usr/bin/python3

import sys  # allows access to command-line arguments

if __name__ == "__main__":
    # Total number of arguments
    num_args = len(sys.argv)

    # Total value of all arguments
    sum = 0

    for x in range(1, num_args):
        sum += int(sys.argv[x])

    print(sum)
