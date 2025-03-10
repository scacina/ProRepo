from collections import deque
import typing
import copy
import sys
import string
from z3 import *
from dataclasses import dataclass
from typing import List, Tuple
from dataclasses import dataclass
from typing import List, Tuple
from enum import Enum
from collections import defaultdict, deque


# global variables
G_INPUTFILENAME = "Day12.txt"


def merge_lines(line_pieces):
    # Step 1: Group lines by set number
    set_groups = {}
    for line in line_pieces:
        set_number = line[4]
        if set_number not in set_groups:
            set_groups[set_number] = []
        set_groups[set_number].append(line)

    # Step 2: Initialize merged count
    merged_count = 0

    # Step 3: Process each set
    for set_number, lines in set_groups.items():
        # Separate horizontal and vertical lines
        horizontal_lines = [line for line in lines if line[1] == line[3]]
        vertical_lines = [line for line in lines if line[0] == line[2]]

        # Merge horizontal lines
        merged_horizontal = merge_horizontal_lines(horizontal_lines)

        # Merge vertical lines
        merged_vertical = merge_vertical_lines(vertical_lines)

        # Add the counts
        merged_count += len(merged_horizontal) + len(merged_vertical)

    return merged_count

def merge_horizontal_lines(lines):
    # Group by y-coordinate
    y_groups = {}
    for line in lines:
        y = line[1]
        if y not in y_groups:
            y_groups[y] = []
        y_groups[y].append((line[0], line[2]))  # xstart and xend

    # Merge x-intervals for each y group
    merged_lines = []
    for y, intervals in y_groups.items():
        merged = merge_intervals(intervals)
        for m in merged:
            merged_lines.append((m[0], y, m[1], y))
    return merged_lines

def merge_vertical_lines(lines):
    # Group by x-coordinate
    x_groups = {}
    for line in lines:
        x = line[0]
        if x not in x_groups:
            x_groups[x] = []
        x_groups[x].append((line[1], line[3]))  # ystart and yend

    # Merge y-intervals for each x group
    merged_lines = []
    for x, intervals in x_groups.items():
        merged = merge_intervals(intervals)
        for m in merged:
            merged_lines.append((x, m[0], x, m[1]))
    return merged_lines

def merge_intervals(intervals):
    # Sort intervals by start point
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for interval in intervals[1:]:
        if interval[0] <= merged[-1][1]:
            # Overlapping or contiguous
            merged[-1] = (merged[-1][0], max(merged[-1][1], interval[1]))
        else:
            merged.append(interval)
    return merged


def solvepart2(matrix):
    res = 0
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    # Traverse the matrix
    for row in range(rows):
        for col in range(cols):
            if not visited[row][col]:
                res += bfsp2(row, col, visited, matrix)
    print("part 2 ended", res)


def bfsp2(start_row, start_col, visited, matrix):
    prm = 0  # Initialize prm to count mismatched or out-of-bound points
    queue = deque([(start_row, start_col)])
    # Define directions for up, down, left, right        
    directions = [(-1, 0, (0, 0, 0, 1)), (1, 0, (1, 0, 1, 1)), (0, -1, (0, 0, 1, 0)), (0, 1, (0, 1, 1, 1))] 
    cnt = 1
    visited[start_row][start_col] = True
    rows, cols = len(matrix), len(matrix[0])
    linesset = set()
    while queue:
        current_row, current_col = queue.popleft()
        current_value = matrix[current_row][current_col]

        for i,(dr, dc, drc) in enumerate(directions):
            new_row, new_col = current_row + dr, current_col + dc

            # Check if the new position is within bounds
            if 0 <= new_row < rows and 0 <= new_col < cols:
                if matrix[new_row][new_col] != current_value:
                    prm += 1
                    linesset.add((current_row + drc[0], current_col + drc[1], current_row + drc[2], current_col + drc[3], i))
                if not visited[new_row][new_col]:
                    if matrix[new_row][new_col] == current_value:
                        queue.append((new_row, new_col))
                        visited[new_row][new_col] = True
                        cnt += 1
            else:
                prm += 1  # Increment prm if out of bounds
                if dr == 0:
                    linesset.add((current_row + drc[0], current_col + drc[1], current_row + drc[2], current_col + drc[3], 5))
                else:
                    linesset.add((current_row + drc[0], current_col + drc[1], current_row + drc[2], current_col + drc[3], 6))
    lineslist = list(linesset)
    print(lineslist)
    print(prm, cnt, merge_lines(lineslist))
    return merge_lines(list(linesset)) * cnt

# BFS function
def bfs(start_row, start_col, visited, matrix):
    prm = 0  # Initialize prm to count mismatched or out-of-bound points
    queue = deque([(start_row, start_col)])
    # Define directions for up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    cnt = 1
    visited[start_row][start_col] = True
    rows, cols = len(matrix), len(matrix[0])

    while queue:
        current_row, current_col = queue.popleft()
        current_value = matrix[current_row][current_col]

        for dr, dc in directions:
            new_row, new_col = current_row + dr, current_col + dc

            # Check if the new position is within bounds
            if 0 <= new_row < rows and 0 <= new_col < cols:
                if matrix[new_row][new_col] != current_value:
                    prm += 1
                if not visited[new_row][new_col]:
                    if matrix[new_row][new_col] == current_value:
                        queue.append((new_row, new_col))
                        visited[new_row][new_col] = True
                        cnt += 1
            else:
                prm += 1  # Increment prm if out of bounds
    print(prm, cnt)
    return prm, cnt

def solvepart1(matrix):
    res = 0
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    # Traverse the matrix
    for row in range(rows):
        for col in range(cols):
            if not visited[row][col]:
                prm, cnt = bfs(row, col, visited, matrix)
                res += (prm * cnt)
                print("new value:", matrix[row][col], res)
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
    #solvepart1(array)
    solvepart2(array)


if __name__ == "__main__":
    main()
