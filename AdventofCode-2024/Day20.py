from z3 import *
import re
import copy
import heapq
import collections
import winsound
from collections import deque
from queue import PriorityQueue
# global variables
G_INPUTFILENAME = "Day20.txt"

def manhattan_distance_points(x, y, distance):
    points = []
    for dx in range(-distance, distance + 1):
        for dy in range(-distance + abs(dx), distance - abs(dx) + 1):
            points.append((x + dx, y + dy))
    return points

def bfs_all_the_path(grid, start, dest):
    rows = len(grid)
    cols = len(grid[0])
    sx, sy = start
    dx, dy = dest
    # Initialize the distance and predecessor matrices
    distances = [[-1 for _ in range(cols)] for _ in range(rows)]
    
    # BFS queue initialization
    queue = deque()
    queue.append((sx, sy, [(sx,sy)]))
    distances[sx][sy] = 0
    
    # Directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Perform BFS to find shortest distances
    while queue:
        x, y, path = queue.popleft()
        if x == dx and y == dy:
            break
        for dx_move, dy_move in directions:
            nx, ny = x + dx_move, y + dy_move
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] in ['.', 'S', 'E']:
                if distances[nx][ny] == -1:
                    distances[nx][ny] = distances[x][y] + 1
                    path = path + [(nx, ny)]
                    queue.append((nx, ny, path))  
    
    # Check if destination is reachable
    if distances[dx][dy] == -1:
        #print("No path found from the start to the destination.")
        return [], []
    else:
        return distances, path
    

def solvepart2(matrix, mdistance):
    res = 0
    sr = sc = er = ec = 0
    grid = []
    for r, line in enumerate(matrix):
        grid.append([ch for ch in line])
        if 'S' in line:
            sr, sc = r, line.find('S')
        if 'E' in line:
            er, ec = r, line.find('E')
        res += line.count('.')
    dcntr = collections.Counter()
    rows = len(grid)
    cols = len(grid[0])
    distgrid, path = bfs_all_the_path(grid, (sr,sc), (er,ec))
    svisited = set()
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '#' or distgrid[r][c] == -1:
                continue
            for (nr, nc) in manhattan_distance_points(r, c, mdistance):
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == '#':
                        continue
                    if distgrid[nr][nc] == -1 or distgrid[r][c] == -1:
                        continue
                    if distgrid[r][c] - distgrid[nr][nc] - abs(nr-r) -  abs(nc-c) >= 100 and (nr, nc) in path and (r, c) in  path and ((r,c,nr,nc) not in svisited):
                        dcntr[distgrid[r][c] - distgrid[nr][nc] - abs(nr-r) -  abs(nc-c)] += 1
                        svisited.add((r,c,nr,nc))
    res = 0
    for key in dcntr.keys():
        res += dcntr.get(key)
    print("Part 2 ended. Result:", res)
    return res


def solvepart1(matrix):
    res = 0
    res = solvepart2(matrix, 2)
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
    solvepart2(array, 20)


if __name__ == "__main__":
    main()
