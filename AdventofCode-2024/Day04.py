import collections
import typing
import re
import sys
import string

# global variables
G_INPUTFILENAME = "Day04.txt"


def solvepart2(inlines: typing.List[str]):
    res = 0
    rows = len(inlines)
    cols = len(inlines[0]) if rows > 0 else 0

    # Directions for 8 neighbors: N, NE, E, SE, S, SW, W, NW
    directions = [
        (-1, -1), (1, 1),  # Top, Top-Right, Right, Bottom-Right
        (1, -1), (-1, 1) # Bottom, Bottom-Left, Left, Top-Left
    ]
    trgt = "MMSS"
    for i in range(rows):
        for j in range(cols):
            if inlines[i][j] == 'A':
                nwrd = ""
                for dx, dy in directions:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < rows and 0 <= ny < cols:
                        nwrd += inlines[nx][ny]
                        if len(nwrd) == 2 and "".join(sorted(nwrd)) != "MS":
                            nwrd = ""
                if "".join(sorted(nwrd)) == trgt:
                    res += 1
    print("part 2 ended", res)

def solvepart1(inlines: typing.List[str]):
    res = 0

    rows = len(inlines)
    cols = len(inlines[0]) if rows > 0 else 0

    # Directions for 8 neighbors: N, NE, E, SE, S, SW, W, NW
    directions = [
        (-1, 0), (-1, 1), (0, 1), (1, 1),  # Top, Top-Right, Right, Bottom-Right
        (1, 0), (1, -1), (0, -1), (-1, -1) # Bottom, Bottom-Left, Left, Top-Left
    ]

    for i in range(rows):
        for j in range(cols):
            if inlines[i][j] == 'X':
                nls = collections.deque()
                for dx, dy in directions:
                    nls.append((i,j,"MAS",dx,dy))
                while nls:
                    x,y,wrd,dx,dy = nls.popleft()
                    if not wrd:
                        res += 1
                    else:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < rows and 0 <= ny < cols and inlines[nx][ny] == wrd[0]:  # Check bounds
                            nls.append((nx, ny, wrd[1:], dx, dy))
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
