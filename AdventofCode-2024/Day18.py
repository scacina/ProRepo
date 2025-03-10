from z3 import *
import re
import copy
from queue import PriorityQueue
import collections
import winsound
# global variables
G_INPUTFILENAME = "Day18.txt"



offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def solvepart2(matrix):
    res = 0
    rmax = cmax = 70
    l, r = 0, len(matrix) - 1
    mid = -1
    aset = set()
    while True and l <= r:
        midex = mid
        mid = (l + r) // 2
        if midex <= mid:
            stindex = midex + 1
        else:
            aset = set()
            stindex = 0
        for i in range(stindex, mid+1):
            loc = matrix[i].split(',')
            aset.add((int(loc[1]), int(loc[0])))
        res = sys.maxsize
        pq = PriorityQueue()
        pq.put((0,0,0))
        svisited = set([(0, 0)])
        while not pq.empty():
            step, cr, cc = pq.get()   
            if cr == rmax and cc == cmax:
                res = step
                break
            for dr, dc in offsets:
                if (0 <= cr + dr <= rmax and 0 <= cc + dc <= cmax and (cr + dr, cc + dc) not in svisited and (cr + dr, cc + dc) not in aset):
                    svisited.add((cr + dr, cc + dc))
                    pq.put((step+1, cr + dr, cc + dc))
        if res == sys.maxsize:
            res = matrix[mid]
            r = mid - 1
        else:
            l = mid + 1
    print("Part 2 ended. Result:", res)


def solvepart1(matrix):
    res = 0
    rmax = cmax = 70
    aset = set()
    for i in range(1024):
        loc = matrix[i].split(',')
        aset.add((int(loc[1]), int(loc[0])))
    pq = PriorityQueue()
    pq.put((0,0,0))
    svisited = set([(0, 0)])
    while not pq.empty():
        step, cr, cc = pq.get()   
        if cr == rmax and cc == cmax:
            res = step
            break
        for dr, dc in offsets:
            if (0 <= cr + dr <= rmax and 0 <= cc + dc <= cmax and (cr + dr, cc + dc) not in svisited and (cr + dr, cc + dc) not in aset):
                svisited.add((cr + dr, cc + dc))
                pq.put((step+1, cr + dr, cc + dc))
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
