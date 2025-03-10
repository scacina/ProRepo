from collections import deque
import typing
import copy
import sys
import string
from z3 import *

# global variables
G_INPUTFILENAME = "Day10.txt"


def solvepart2(inlines: typing.List[str]):
    res = 0
    dxy = [(-1,0), (1,0), (0, -1), (0, 1)]

    for i in range(len(inlines)):
        for j in range(len(inlines[0])):
            if inlines[i][j] == '0':
                nq = [(i,j)]
                cindex = 0
                while nq and cindex != 9:
                    cindex += 1
                    cq = nq
                    nq = []
                    while cq:
                        cx, cy = cq.pop()
                        for dx, dy in dxy:
                            if 0 <= cx + dx < len(inlines) and 0 <= cy + dy < len(inlines[0]):
                                if inlines[cx+dx][cy+dy] == str(cindex):
                                    nq.append((cx+dx, cy+dy))
                                    if cindex == 9:
                                        res += 1
    print("part 2 ended", res)



def solvepart1(inlines):
    res = 0
    dxy = [(-1,0), (1,0), (0, -1), (0, 1)]

    for i in range(len(inlines)):
        for j in range(len(inlines[0])):
            if inlines[i][j] == '0':
                nq = []
                cq = []
                cindex = 0
                nq.append((i,j))
                while nq and cindex != 9:
                    cindex += 1
                    cq = nq
                    nq = []
                    while cq:
                        cx, cy = cq.pop()
                        for dx, dy in dxy:
                            if 0 <= cx + dx < len(inlines) and 0 <= cy + dy < len(inlines[0]):
                                if inlines[cx+dx][cy+dy] == str(cindex):
                                    nq.append((cx+dx, cy+dy))
                res += len(set(nq))
    print("Part 1 ended. Result:", res)



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
