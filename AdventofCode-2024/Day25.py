import collections
import functools
import heapq
import itertools
# Global variable
import sys
from itertools import combinations
G_INPUTFILENAME = "Day25.txt"


def solvepart2(matrix):
    return 0


def solvepart1(matrix):
    res = 0
    lsl = []
    lsp = []
    width = 6
    for r in range(0, len(matrix), 7):
        cset = set()
        if matrix[r].count('.') == 0 and matrix[r+width].count('#') == 0:
            for cr in range(r, r+width+1):
                for cc, ch in enumerate(matrix[cr]):
                    if ch == '#':
                        cset.add((cr-r, cc))
            lsl.append(cset)
        elif matrix[r].count('#') == 0 and matrix[r+width].count('.') == 0:
            for cr in range(r, r+width+1):
                for cc, ch in enumerate(matrix[cr]):
                    if ch == '#':
                        cset.add((cr-r, cc))
            lsp.append(cset)
        else:
            assert False
    res = sum(1 for lck, pin in itertools.product(lsl, lsp) if lck.isdisjoint(pin))
    return print("part 1 ended", res)

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
