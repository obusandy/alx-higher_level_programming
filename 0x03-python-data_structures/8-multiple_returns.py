#!/usr/bin/python3
def multiple_returns(line):

    if line == "":
        return (0, None)
    return (len(line), line[0])
