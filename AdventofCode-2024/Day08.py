import collections
import typing
import copy
import sys
import string
from z3 import *

# global variables
G_INPUTFILENAME = "Day08.txt"


def get_antinodes(coords1,coords2, inlines):
    x1,y1 = coords1
    x2,y2 = coords2
    dx,dy = x2-x1,y2-y1
    shapex = len(inlines)
    shapey = len(inlines[0])
    output = set()
    xa,ya = x1,y1
    while xa in range(shapex) and ya in range(shapey):
        output.add((xa,ya))
        xa,ya = xa+dx,ya+dy
    xa,ya = x1,y1
    while xa in range(shapex) and ya in range(shapey):
        output.add((xa,ya))
        xa,ya = xa-dx,ya-dy
    return output

def find_symmetrical_point(x1, y1, x2, y2):
    """
    Given a point (x1, y1) and a reference point (x2, y2),
    find the symmetrical point of (x1, y1) with respect to (x2, y2).
    """
    # Symmetrical point relative to (x2, y2)
    x3 = 2 * x2 - x1
    y3 = 2 * y2 - y1
    # Symmetrical point relative to (x1, y1)
    x4 = 2 * x1 - x2
    y4 = 2 * y1 - y2


    return [(x3, y3), (x4,y4)]


def solvepart3(inlines: typing.List[str]):
    res = set()
    adict = collections.defaultdict(list)

    for r in range(len(inlines)):
        for c in range(len(inlines[0])):
            if inlines[r][c] not in ('#', '.'):
                adict[inlines[r][c]].append((r,c))

    for row in adict.values():
        for i in range(len(row)):
            (cx, cy) = row[i]
            for j in range(i+1, len(row)):
                (nx, ny) = row[j]
                for (ax,ay) in find_symmetrical_point(cx, cy, nx, ny):
                    if 0 <= ax < len(inlines) and 0 <= ay < len(inlines[0]):
                        res.add((ax, ay))
    print("part 3 ended", len(res))


def solvepart2(inlines: typing.List[str]):
    res = set()
    svisited = set()
    adict = collections.defaultdict(list)

    for r in range(len(inlines)):
        inlines[r] = list(inlines[r])
        for c in range(len(inlines[0])):
            if inlines[r][c] not in ('#', '.'):
                adict[inlines[r][c]].append((r,c))

    for row in adict.values():
        for i in range(len(row)):
            (cx, cy) = row[i]
            for j in range(0, len(row)):
                if i == j:
                    continue
                (nx, ny) = row[j]
                res.add((cx,cy))
                res.add((nx,ny))
                resls = get_antinodes((cx, cy), (nx, ny), inlines)
                res.update(resls)
    print("part 2 ended", len(res))



def calculate_points(cx, cy, nx, ny):
    res = []
    dx = abs(cx-nx)
    dy = abs(cy-ny)

    if cy < ny:
        if cx < nx:
            res.append((cx-dx, cy-dy))
            res.append((nx+dx, ny+dy))
        else:
            res.append((cx+dx, cy-dy))
            res.append((nx-dx, ny+dy))
    else:
        if cx < nx:
            res.append((cx-dx, cy+dy))
            res.append((nx+dx, ny-dy))
        else:
            res.append((cx+dx, cy+dy))
            res.append((nx-dx, ny-dy))   
    return res

def solvepart1(inlines: typing.List[str]):
    res = set()
    adict = collections.defaultdict(list)

    for r in range(len(inlines)):
        for c in range(len(inlines[0])):
            if inlines[r][c] not in ('#', '.'):
                adict[inlines[r][c]].append((r,c))

    for row in adict.values():
        for i in range(len(row)):
            (cx, cy) = row[i]
            for j in range(i+1, len(row)):
                (nx, ny) = row[j]
                for (ax, ay) in calculate_points(cx, cy, nx, ny):
                    if 0 <= ax < len(inlines) and 0 <= ay < len(inlines[0]):
                        res.add((ax, ay))
    print("part 1 ended", len(res))



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
    solvepart3(array)


if __name__ == "__main__":
    main()
