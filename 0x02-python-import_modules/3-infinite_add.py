#!/usr/bin/python3

if __name__ == "__main__":
    """Print the addition of all arguments."""
    import sys

    totalcount = 0

    for i in range(1, len(sys.argv)):
        totalcount += int(sys.argv[i])

    print("{}".format(totalcount))
