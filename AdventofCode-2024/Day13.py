import typing
import re
import sys
import string
from z3 import *
from typing import List, Tuple
from collections import defaultdict, deque

# global variables
G_INPUTFILENAME = "Day13.txt"

# Function to find minimum cost
def find_minimum_cost(x_target_val, y_target_val, adx, ady, bdx, bdy):
    # Define variables
    x_target = Int('x_target')  # Target x coordinate
    y_target = Int('y_target')  # Target y coordinate
    option_a_count = Int('option_a_count')  # Number of times to use option A
    option_b_count = Int('option_b_count')  # Number of times to use option B
    # Define solver
    s = Optimize()
    # Constraints
    s.add(option_a_count >= 0)
    s.add(option_b_count >= 0)
    # Reach the target coordinates
    s.add(option_a_count * adx + option_b_count * bdx == x_target)
    s.add(option_a_count * ady + option_b_count * bdy == y_target)
    # Cost function to minimize
    cost = option_a_count * 3 + option_b_count * 1
    s.minimize(cost)
    s.add(x_target == x_target_val)
    s.add(y_target == y_target_val)

    if s.check() == sat:
        m = s.model()
        return True, m.eval(cost).as_long()
    else:
        return False, 0

def solvepart2(matrix):
    res = 0
    # Solve for x = 8400, y = 5400
    for i in range(0, len(matrix), 3):
        adx, ady = re.findall(r'\d+', matrix[i])
        bdx, bdy = re.findall(r'\d+', matrix[i+1])
        tdx, tdy = map(int, re.findall(r'\d+', matrix[i+2]))
        found, val = find_minimum_cost(tdx+10000000000000, tdy+10000000000000, adx, ady, bdx, bdy)
        if found:
            res += int(val)
    print("Part 2 ended. Result:", res)


def solvepart1(matrix):
    res = 0
    # Solve for x = 8400, y = 5400
    for i in range(0, len(matrix), 3):
        adx, ady = re.findall(r'\d+', matrix[i])
        bdx, bdy = re.findall(r'\d+', matrix[i+1])
        tdx, tdy = map(int, re.findall(r'\d+', matrix[i+2]))
        found, val = find_minimum_cost(tdx, tdy, adx, ady, bdx, bdy)
        if found:
            res += int(val)
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
