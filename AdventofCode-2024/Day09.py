import collections
import typing
import copy
import sys
import string
from z3 import *

# global variables
G_INPUTFILENAME = "Day09.txt"


def solvepart2(inlines: typing.List[str]):
    res = 0
   
    # Ensure input is a list of strings
    inlines = [ch for ch in inlines[0]]
    resls = []
    emptyls = []
    lend = cindex = 0
    for i in range(0, len(inlines) - 1, 2):
        numl = int(inlines[i])
        enuml = int(inlines[i + 1])
        if numl:
            resls.append((cindex, lend, lend + numl))
            lend += numl
        if enuml:
            emptyls.append((lend, lend + enuml)) # Second range
            lend += enuml
        cindex += 1
    numl = int(inlines[-1])
    resls.append((cindex, lend, lend + numl))

    for i in range(len(resls) - 1, -1, -1):
        (indx, rst, ren) = resls[i]
        j = 0
        while j < len(emptyls) and emptyls[j][0] < rst:
            (est, een) = emptyls[j]
            lemtpy = een - est
            lnumber = ren - rst
            if lemtpy >= lnumber:
                lemtpy -= lnumber
                if lemtpy:
                    emptyls[j] = (est + lnumber, een)
                else:
                    emptyls = emptyls[0:j] + emptyls[j+1:]
                resls[i] = (indx, est, est + lnumber)
                break
            j += 1

    for (indx, st, en) in resls:
        for i in range(st, en):
            res += (indx*i)

    #print(resls)
    #print("Result list:", resls)
    #print("emptyls list:", emptyls)
    print("part 2 ended", res)



def solvepart1(inlines):
    res = 0
    print("Input size:", len(inlines))
    
    # Ensure input is a list of strings
    inlines = [ch for ch in inlines[0]]
    resls = collections.deque()
    emptyls = []
    lend = cindex = 0
    for i in range(0, len(inlines) - 1, 2):
        numl = int(inlines[i])
        enuml = int(inlines[i + 1])
        if numl:
            resls.append((cindex, lend, lend + numl))
            lend += numl
        if enuml:
            emptyls.append((lend, lend + enuml)) # Second range
            lend += enuml
        cindex += 1
    numl = int(inlines[-1])
    resls.append((cindex, lend, lend + numl))    
    emptyls.reverse()
    while emptyls and emptyls[-1][0] < resls[-1][1]:
        (est, een) = emptyls[-1]
        (indx, rst, ren) = resls[-1]
        if (een - est) > (ren -rst):
            emptyls[-1] = (est + ren - rst, een)
            resls.pop()
            resls.appendleft((indx, est, est + ren - rst))
        elif (een - est) < (ren - rst):
            emptyls.pop()
            resls.pop()
            resls.appendleft((indx, est, een))
            resls.append((indx, rst, rst + (ren-rst) - (een-est)))           
        else:
            emptyls = emptyls[:-1]
            resls.pop()
            resls.appendleft((indx, est, een))

    for (indx, st, en) in resls:
        for i in range(st, en):
            res += (indx*i)

    #print(resls)
    #print("Result list:", resls)
    #print("emptyls list:", emptyls)
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
