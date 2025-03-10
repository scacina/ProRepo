import collections
import typing
import copy
import sys
import string

# global variables
G_INPUTFILENAME = "Day01.txt"


def solvepart2(inlines: typing.List[str]):
    lls = []
    dcntr = collections.Counter()
    res = 0
    for line in inlines:
        x, y = map(int, line.split())
        lls.append(x)
        dcntr[y] += 1
    for num in lls:
        res += num * dcntr[num]
    print("part 2 ended", res)

def solvepart1(inlines: typing.List[str]):
    lls = []
    rls = []
    res = 0
    for line in inlines:
        x, y = map(int, line.split())
        lls.append(x)
        rls.append(y)
    lls.sort()
    rls.sort()
    res = sum([abs(x-y) for x, y in zip(lls, rls)])
    print("part 1 ended", res)


# main...
def main():
    array = []
    with open(G_INPUTFILENAME) as f:
        for line in f:  # read rest of lines
            line = line.strip()
            line = line.strip("\n")
            line = line.strip("\r")
            line = line.strip()
            if line:
                array.append(line)
    solvepart1(array)
    solvepart2(array)


if __name__ == "__main__":
    main()
