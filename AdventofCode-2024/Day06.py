import collections
import typing
import copy
import sys
import string

# global variables
G_INPUTFILENAME = "Day06.txt"

def solvepart2helper(inlines: typing.List[str], cx, cy, cd):
    ddir = { '^':(-1,0,'>'),  '>':(0,1,'v'),  'v':(1,0,'<'),  '<':(0,-1,'^')}
    maxrow = len(inlines)
    maxcol = len(inlines[0])
    svisited = set()
    while (cx,cy,cd) not in svisited:
        dx,dy,nd = ddir[cd]
        svisited.add((cx,cy,cd))
        if 0 <= cx + dx < maxrow and 0 <= cy + dy < maxcol:
            if  inlines[cx + dx][cy + dy] != '#':
                cx, cy = cx + dx, cy +dy
            else:
                cd = nd
        else:
            return False
    return True



def solvepart2(inlines: typing.List[str]):
    svisited = set()
    sres = set()
    ddir = { '^':(-1,0,'>'),  '>':(0,1,'v'),  'v':(1,0,'<'),  '<':(0,-1,'^')}
    maxrow = len(inlines)
    maxcol = len(inlines[0])
    cx = cy = 0
    res = 0
    for i in range(maxrow):
        inlines[i] = list(inlines[i])

    for i in range(maxrow):
        for j in range(maxcol):
            if inlines[i][j] in ddir:
                cx = i
                cy = j
                cd = inlines[i][j]
    xstart, ystart, dstart = cx, cy, cd
    while True:
        dx,dy,nd = ddir[cd]
        if 0 <= cx + dx < maxrow and 0 <= cy + dy < maxcol:
            if  inlines[cx + dx][cy + dy] != '#':             
                if (cx,cy) != (xstart, ystart):
                    inlines[cx + dx][cy + dy] = '#'
                    if solvepart2helper(inlines, xstart, ystart, dstart):
                        sres.add((cx + dx, cy + dy))
                    inlines[cx + dx][cy + dy] = '.'
                cx, cy = cx + dx, cy +dy
            else:
                cd = nd
        else:
            break
    print("part 2 ended", len(sres))

def solvepart1(inlines: typing.List[str]):
    svisited = set()
    ddir = { '^':(-1,0,'>'),  '>':(0,1,'v'),  'v':(1,0,'<'),  '<':(0,-1,'^')}
    maxrow = len(inlines)
    maxcol = len(inlines[0])
    cx = cy = 0
    for i in range(maxrow):
        for j in range(maxcol):
            if inlines[i][j] in ddir:
                cx = i
                cy = j
                cd = inlines[i][j]
    print(cx,cy,cd)
    svisited.add((cx, cy))
    while True:
        dx,dy,nd = ddir[cd]
        if 0 <= cx + dx < maxrow and 0 <= cy + dy < maxcol:
            if  inlines[cx + dx][cy + dy] != '#':
                cx, cy = cx + dx, cy +dy
                svisited.add((cx, cy))
            else:
                cd = nd
        else:
            break
    print("part 1 ended", len(svisited))


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
