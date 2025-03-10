import re
import copy
import heapq
import collections
import winsound
from queue import PriorityQueue
import itertools
import functools

# global variables
G_INPUTFILENAME = "Day20.txt"


direction_changes = {
    '^': (-1, 0),  # Moving up decreases the row (y-axis).
    'v': (1, 0),   # Moving down increases the row (y-axis).
    '>': (0, 1),   # Moving right increases the column (x-axis).
    '<': (0, -1)   # Moving left decreases the column (x-axis).
}

keypad_n = {
    (0,0): '7', (0,1): '8', (0,2): '9',
    (1,0): '4', (1,1): '5', (1,2): '6',
    (2,0): '1', (2,1): '2', (2,2): '3',
                (3,1): '0', (3,2): 'A'
#   (3,0): ' ', (3,1): '0', (3,2): 'A'
}

keypad_d = {
                (0,1): '^', (0,2): 'A',
#   (0,0): ' ', (0,1): '^', (0,2): 'A',
    (1,0): '<', (1,1): 'v', (1,2): '>'
}

oppdir = {
    '^': 'v',  # Moving up decreases the row (y-axis).
    'v': '^',  # Moving down increases the row (y-axis).
    '>': '<',   # Moving right increases the column (x-axis).
    '<': '>',   # Moving left decreases the column (x-axis).
    'A': '.'    # this is dummy
}

keypad_h = "<>^vA"

def checkifinrange(cmdin, posin):
    r, c = posin
    for ch in cmdin:
        dr, dc = direction_changes[ch]
        r, c = r + dr, c + dc
        if (r,c) not in keypad_d:
            return False
    return True

def checkifrangenumpad(cmdin, posin):
    r, c = posin
    for ch in cmdin:
        dr, dc = direction_changes[ch]
        r, c = r + dr, c + dc
        if (r,c) not in keypad_n:
            return False
    return True

def checkifneeded(cmd, ch):
    if not cmd:
        return True
    
    if cmd[-1] != oppdir[ch]:
        return True

    return False


@functools.lru_cache(maxsize=None)
def getnewstatus(lencmd, pturn, cmdA, cmd1, pos1, cmd2, post2, cmd3, pos3, inch):
    res = None
    pturn *= -1
    targetword = '480A'
    if pturn == 0: # human turn
        #clength += 1
        ch = inch
        if ch == 'A' and checkifinrange(cmdA, pos1):
            res = (lencmd, -1, cmdA, cmd1, pos1, cmd2, post2, cmd3, pos3)
        elif ch != 'A' and checkifinrange(cmdA+ch, pos1):
            res = (lencmd, 0, cmdA + ch, cmd1, pos1, cmd2, post2, cmd3, pos3)
    elif pturn == 1: #robot 1
        r, c = pos1
        gapaim = False
        for ch in cmdA:
            dr, dc = direction_changes[ch]
            r, c = r + dr, c + dc
            if (r,c) not in keypad_d:
                gapaim = True
                break
        if gapaim == False:
            cmdA = ''
            currch = keypad_d[(r,c)]
            if currch == 'A' and checkifinrange(cmd1, post2):
                res = (lencmd, -2, cmdA, cmd1, (r,c), cmd2, post2, cmd3, pos3)
            elif currch != 'A' and checkifinrange(cmd1+currch, post2) and checkifneeded(cmd1, currch):
                res = (lencmd, 0, cmdA, cmd1 + currch, (r,c), cmd2, post2, cmd3, pos3)
    elif pturn == 2: #robot 2
        r, c = post2
        gapaim = False
        for ch in cmd1:
            dr, dc = direction_changes[ch]
            r, c = r + dr, c + dc
            if (r,c) not in keypad_d:
                gapaim = True
                break
        if gapaim == False:
            cmd1 = ''
            currch = keypad_d[(r,c)]
            if currch == 'A' and checkifrangenumpad(cmd2, pos3):
                res = (lencmd, -3, cmdA, cmd1, pos1, cmd2, (r,c), cmd3, pos3)
            elif currch != 'A' and checkifrangenumpad(cmd2+currch, pos3) and checkifneeded(cmd2, currch):
                res = (lencmd, 0, cmdA, cmd1, pos1, cmd2 + currch, (r,c), cmd3, pos3)
    else:
        assert pturn == 3
        r, c = pos3
        gapaim = False
        for ch in cmd2:
            dr, dc = direction_changes[ch]
            r, c = r + dr, c + dc
            if (r,c) not in keypad_n:
                gapaim = True
                break
        if gapaim == False:
            cmd2 = ''
            currch = keypad_n[(r,c)]
            cmd3 += currch
            if targetword.startswith(cmd3):
                if len(targetword) == len(cmd3):
                    print("found")
                    winsound.Beep(1000, 10000)
                    exit()
                else:
                    res = (-len(cmd3), 0, cmdA, cmd1, pos1, cmd2, post2, cmd3, (r,c))
    return res

def solvepart2(matrix):
    res = 0
    print("Part 2 ended. Result:", res)
    return res

def solvepart1(matrix):
    res = 0
    targetword = "0"
    pq = PriorityQueue()
    # clength | player turn | commands till A | robot1command | robot1post | robot2command | robot2pos | robot3command | robot3 position
    pq.put((0, 0, 0, "", "", (0,2), "", (0,2), "", (3,2)))
    clength = 0
    while not pq.empty():
        lencmd, pturn, clength, cmdA, cmd1, pos1, cmd2, post2, cmd3, pos3 = pq.get()
        print(clength)
        if pturn == 0:
            clength += 1
            
            for ch in keypad_h:
                res = None
                if cmdA == "" or (cmdA[-1] != oppdir[ch]):
                    res = getnewstatus(lencmd, pturn, cmdA, cmd1, pos1, cmd2, post2, cmd3, pos3, ch)
                
                if res is not None:
                    res = (res[0], res[1], clength, res[2], res[3], res[4], res[5], res[6], res[7], res[8])
                    pq.put(res)
        else:
            res = getnewstatus(lencmd, pturn, cmdA, cmd1, pos1, cmd2, post2, cmd3, pos3, ch)
            if res is not None:
                res = (res[0], res[1], clength, res[2], res[3], res[4], res[5], res[6], res[7], res[8])
                pq.put(res)
    print("part 1 ended")
    return res

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
