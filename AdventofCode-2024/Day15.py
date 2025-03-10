from z3 import *
import re
import copy

# global variables
G_INPUTFILENAME = "Day15.txt"


def canmove(cr,cc,dr,dc,grid):
    if grid[cr][cc] == '#':
        return False
    elif grid[cr][cc] == '.':
        return True
    elif grid[cr][cc] == '[':
        return canmove(cr+dr,cc+dc,dr,dc,grid) and canmove(cr+dr,cc+dc+1,dr,dc,grid)
    else:
        assert grid[cr][cc] == ']'
        return canmove(cr+dr,cc+dc,dr,dc,grid) and canmove(cr+dr,cc+dc-1,dr,dc,grid)

def movevertical(cr,cc,dr,dc,grid):
    if grid[cr][cc] == '#':
        assert False
    elif grid[cr][cc] == '.':
        return
    elif grid[cr][cc] == '[':
        movevertical(cr+dr,cc+dc,dr,dc,grid) 
        movevertical(cr+dr,cc+dc+1,dr,dc,grid)
        grid[cr+dr][cc+dc], grid[cr][cc] = grid[cr][cc], grid[cr+dr][cc+dc]
        grid[cr+dr][cc+dc+1], grid[cr][cc+1] = grid[cr][cc+1], grid[cr+dr][cc+dc+1]
    else:
        assert grid[cr][cc] == ']'
        movevertical(cr+dr,cc+dc,dr,dc,grid) 
        movevertical(cr+dr,cc+dc-1,dr,dc,grid)
        grid[cr+dr][cc+dc], grid[cr][cc] = grid[cr][cc], grid[cr+dr][cc+dc]
        grid[cr+dr][cc+dc-1], grid[cr][cc-1] = grid[cr][cc-1], grid[cr+dr][cc+dc-1]  



def moveingridp2(cr,cc,dr,dc,grid):
    if (canmove(cr+dr,cc+dc,dr,dc,grid)):
        movevertical(cr+dr,cc+dc,dr,dc,grid)
        grid[cr+dr][cc+dc], grid[cr][cc] = grid[cr][cc], grid[cr+dr][cc+dc]
        cr, cc = cr + dr, cc + dc
    return cr, cc




def solvepart2(matrix):
    res = 0
    grid = []
    instr = ""
    cr = cc = 0
    for i in range(len(matrix)):
        if "." in matrix[i] or '#' in matrix[i]:
            newr = []
            for ch in matrix[i]:
                if ch == '#':
                    newr += ['#', "#"]
                elif ch == '.':
                    newr += ['.', "."]
                elif ch == 'O':
                    newr += ['[', "]"]
                else:
                    assert ch == "@"
                    newr += ['@', "."]
            grid.append(newr)
            if '@' in matrix[i]:
                cr, cc = i, newr.index('@')
        else:
            instr = instr + matrix[i]
    
    increments = {'v': (1, 0),'>': (0, 1),'^': (-1, 0),'<': (0, -1)}
    for ch in instr:
        if ch == '>' or ch == '<':
            cr,cc = moveingrid(cr, cc, increments[ch][0], increments[ch][1], grid)
        else:
            cr,cc = moveingridp2(cr, cc, increments[ch][0], increments[ch][1], grid)
        # for line in grid:
        #     print("".join(line))

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '[':
                res += (100*r + c)
    print("Part 2 ended. Result:", res)


def moveingrid(cr,cc,dr,dc,grid):
    nr, nc = cr + dr, cc + dc
    while grid[nr][nc] not in ['#', '.']:
        nr, nc = nr + dr, nc + dc
    if grid[nr][nc] == '#':
        return cr, cc
    dr, dc = -dr, -dc
    while (nr,nc) != (cr, cc):
        grid[nr+dr][nc+dc], grid[nr][nc] = grid[nr][nc], grid[nr+dr][nc+dc]
        nr,nc = nr+dr, nc+dc
    return cr-dr, cc-dc


def solvepart1(matrix):
    res = 0
    grid = []
    instr = ""
    cr = cc = 0
    for i in range(len(matrix)):
        if "." in matrix[i] or '#' in matrix[i]:
            grid.append(list(matrix[i]))
            if '@' in matrix[i]:
                cr, cc = i, matrix[i].find('@')
        else:
            instr = instr + matrix[i]
    increments = {'v': (1, 0),'>': (0, 1),'^': (-1, 0),'<': (0, -1)}
    for ch in instr:
        cr,cc = moveingrid(cr, cc, increments[ch][0], increments[ch][1], grid)
        # for line in grid:
        #     print("".join(line))

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 'O':
                res += (100*r) + c
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
