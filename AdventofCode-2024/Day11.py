from collections import deque
import typing
import copy
import sys
import string
from z3 import *

# global variables
G_INPUTFILENAME = "Day11.txt"


def incrementcnt(ininput, newls):
    (ccntr, numstr) = ininput
    for i in range(len(newls)):
        if newls[i][1] == numstr:
            newls[i] = (newls[i][0] + ccntr, numstr)
            return
    newls.append((ccntr, numstr))
    return

def solvepart2(inlines: typing.List[str]):
    res = 0
    instr = inlines[0].split()
    for numstr in instr:
        newls = [(1, numstr)]
        for i in range(75):
            cls = newls
            newls = []
            cnt = 0
            for (ccntr, numstr) in cls:
                if int(numstr) == 0:
                    incrementcnt((ccntr, '1'), newls)
                elif len(numstr) % 2 == 0:
                    incrementcnt((ccntr, str(int(numstr[0:len(numstr)//2]))), newls)
                    incrementcnt((ccntr, str(int(numstr[len(numstr)//2:]))), newls)
                else:
                    incrementcnt((ccntr, str(int(numstr)*2024)), newls)
        res += sum([x for x,y in newls])
    print("part 2 ended", res)



def solvepart1(inlines):
    res = 0
    instr = inlines[0].split()
    for i in range(25):
        newls = []
        for numstr in instr:
            if int(numstr) == 0:
                newls.append("1")
            elif len(numstr) % 2 == 0:
                newls.append(str(int(numstr[0:len(numstr)//2])))
                newls.append(str(int(numstr[len(numstr)//2:])))
            else:
                newls.append(str(int(numstr)*2024))
        instr = newls
    #print(len(newls), newls)
    res = len(newls)
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
