import collections
import typing
import copy
import sys
import string

# global variables
G_INPUTFILENAME = "Day05.txt"

def solvepart2(inlines: typing.List[str], innums):
    res = -solvepart1(inlines, innums)
    for line in innums:
        line = line.split(",")
        for i in range(len(line)-1, 0, -1):
            if line[i-1] + '|' + line[i] not in inlines:
                line[i-1], line[i] =  line[i], line[i-1]
                line = ",".join(line)
                innums.append(line)
                break
        else:
            res += int(line[len(line) // 2])
    print("res is:", res)
    print("part 2 ended")

def solvepart1(inlines: typing.List[str], innums):
    lls = []
    rls = []
    res = 0
    for line in innums:
        line = line.split(",")
        for i in range(len(line)-1, 0, -1):
            if line[i-1] + '|' + line[i] not in inlines:
                break
        else:
            res += int(line[len(line) // 2])
    print("part 1 ended", res)
    return res

# main...
def main():
    res = array = []
    arrayin = []
    with open(G_INPUTFILENAME) as f:
        for line in f:  # read rest of lines
            line = line.strip()
            line = line.strip("\n")
            line = line.strip("\r")
            line = line.strip()
            if line:
                res.append(line)
            else:
                res = arrayin
    solvepart1(array, arrayin)
    solvepart2(array, arrayin)


if __name__ == "__main__":
    main()
