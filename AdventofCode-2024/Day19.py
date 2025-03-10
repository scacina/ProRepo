from z3 import *
import re
import copy
from queue import PriorityQueue
import collections
import winsound
from collections import deque
from queue import PriorityQueue
# global variables
G_INPUTFILENAME = "Day19.txt"


def solvepart2(matrix):
    res = 0
    pieces = matrix[0].split(', ')

    for i in range(1, len(matrix)):
        instr = matrix[i]
        dp = [0] * (len(instr) + 1)
        dp[0] = 1
        match = 0
        for indx in range(1, len(instr) + 1):
            for piece in pieces:
                l = len(piece)
                if indx >= l and dp[indx-l] and instr[indx-l:indx] == piece:
                    dp[indx] += dp[indx-l]
        res += dp[len(instr)]
    print("Part 2 ended. Result:", res)



def solvepart1(matrix):
    res = 0
    pieces = matrix[0].split(', ')

    for i in range(1, len(matrix)):
        instr = matrix[i]
        dp = [0] * (len(instr) + 1)
        dp[0] = 1
        match = 0
        for indx in range(1, len(instr) + 1):
            for piece in pieces:
                l = len(piece)
                if indx >= l and dp[indx-l] and instr[indx-l:indx] == piece:
                    dp[indx] = 1
                    break
        res += dp[len(instr)]
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
