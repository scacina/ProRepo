from z3 import *
import re
import copy
from queue import PriorityQueue
import collections
# global variables
G_INPUTFILENAME = "Day16.txt"


# Define directions and corresponding moves
DIRECTIONS = ['^', '>', 'v', '<']
MOVE_DELTA = {
    '^': (-1, 0),  # Move up
    '>': (0, 1),   # Move right
    'v': (1, 0),   # Move down
    '<': (0, -1)   # Move left
}

def parse_direction_cost(current, target):
    """Calculate the cost to turn from current direction to target direction."""
    current_index = DIRECTIONS.index(current)
    target_index = DIRECTIONS.index(target)
    turns = (target_index - current_index) % 4
    return min(turns, 4 - turns) * 1000  # Cost of turning

def shortest_path(maze, start, end):
    """
    Find the shortest path in a maze with minimized cost.

    Args:
    - maze: 2D list representing the maze
    - start: Tuple (x, y, direction) where the player starts
    - end: Tuple (x, y) where the player must reach
    
    Returns:
    - Minimum cost to reach the end point or -1 if no path exists
    """
    rows, cols = len(maze), len(maze[0])
    start_x, start_y, start_dir = start
    end_x, end_y = end
    prevcost = sys.maxsize
    # Priority queue for A* search (cost, x, y, direction)
    pq = PriorityQueue()
    pq.put((0, start_x, start_y, start_dir, set()))  # (cost, x, y, direction)
    
    # Visited states to prevent revisiting (x, y, direction)
    visited = collections.defaultdict(lambda: float('inf'))
    # If we exhaust the queue without finding the end
    for i in range(len(maze)):
        maze[i] = list(maze[i])

    while not pq.empty():
        cost, x, y, direction, cset = pq.get()
        cset.add((x,y))
        if cost > prevcost:
            continue

        # Check if we reached the end
        if (x, y) == (end_x, end_y):
            prevcost = cost
            for (r, c) in cset:
                maze[r][c] = 'O'
            continue

        # Try all four directions
        for next_dir in DIRECTIONS:
            turn_cost = parse_direction_cost(direction, next_dir)
            dx, dy = MOVE_DELTA[next_dir]
            nx, ny = x + dx, y + dy

            # Check if the move is within bounds and not a block
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] != '#':
                next_cost = cost + turn_cost + 1  # Turn cost + move cost
                state = (nx, ny, next_dir)

                # Only explore this state if it's cheaper than previously visited
                if next_cost <= visited[state]:
                    visited[state] = next_cost
                    pq.put((next_cost, nx, ny, next_dir, cset.copy()))
    return prevcost



def solvepart2(matrix):
    res = 0
    for line in matrix:
        for el in line:
            if el == 'O':
                res += 1
    print("Part 2 ended. Result:", res)


def solvepart1(matrix):
    res = 0
    x = y = 0
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == 'S':
                start = (r,c, ">")
            elif matrix[r][c] == 'E':
                end = (r,c)
    res = shortest_path(matrix, start, end)
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
