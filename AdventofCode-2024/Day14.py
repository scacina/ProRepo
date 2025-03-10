from z3 import *
import re
import sympy
import copy

# global variables
G_INPUTFILENAME = "Day14.txt"

def are_points_connected(points):
    # Set of all points for quick lookup
    points = [(x,y) for (x,y,dx,dy) in points]
    point_set = set(points)
    return len(points) == len(point_set)



def solvepart2(matrix):
    res = 0
    rls = []
    resq1 = resq2 = resq3 = resq4 = 0
    gridw = 101
    gridl = 103
    grid = []
    gridb = []
    for i in range(gridl):
        grid.append(["." for _ in range(gridw)])
        gridb.append(["." for _ in range(gridw)])

    for line in matrix:
        line = line.split(" ")
        # Extract x, y from the first part of the line
        x, y = map(int, line[0].split("=")[1].split(","))
        # Extract dx, dy from the second part of the line
        dx, dy = map(int, line[1].split("=")[1].split(","))
        rls.append((x,y,dx,dy))
    nls = rls.copy()   
    while True:
        res += 1
        rls= nls
        nls = []
        grid = copy.deepcopy(gridb)
        while rls:
            x,y,dx,dy = rls.pop()
            x,y = move_object(x,y,dx,dy, grid)
            grid[y][x] = "*" 
            nls.append((x,y,dx,dy))

        if are_points_connected(nls):
            print(i, ("-------------------------------------------------"))
            for line in grid:
                print("".join(line))
            break

    print("Part 2 ended. Result:", res)

def move_object(initial_x, initial_y, x_speed, y_speed, grid):
    """
    Moves an object within a grid with given speed and teleports it to the other side
    when it exceeds the boundaries.

    Args:
        initial_x (int): Initial x-coordinate of the object.
        initial_y (int): Initial y-coordinate of the object.
        x_speed (int): Speed of the object along the x-axis.
        y_speed (int): Speed of the object along the y-axis.
        grid (list of list): 2D grid matrix.

    Returns:
        tuple: New (x, y) coordinates of the object.
    """
    rows = len(grid)      # Number of rows in the grid
    cols = len(grid[0])   # Number of columns in the grid
    
    # Calculate new position
    new_x = initial_x + x_speed
    new_y = initial_y + y_speed

    # Handle teleportation on x-axis
    if new_x < 0:
        new_x = (new_x % cols + cols) % cols
    elif new_x >= cols:
        new_x = new_x % cols

    # Handle teleportation on y-axis
    if new_y < 0:
        new_y = (new_y % rows + rows) % rows
    elif new_y >= rows:
        new_y = new_y % rows

    return new_x, new_y


def solvepart1(matrix):
    res = 0
    resq1 = resq2 = resq3 = resq4 = 0
    gridw = 101
    gridl = 103
    grid = []
    for i in range(gridl):
        grid.append(["." for _ in range(gridw)])

    for line in matrix:
        line = line.split(" ")
        # Extract x, y from the first part of the line
        x, y = map(int, line[0].split("=")[1].split(","))
        # Extract dx, dy from the second part of the line
        dx, dy = map(int, line[1].split("=")[1].split(","))
        for i in range(100):
            x,y = move_object(x,y,dx,dy, grid)
        if 0 <= x <  (gridw // 2):
            if 0 <= y < (gridl // 2):
                resq1 += 1
            elif ((gridl // 2) + 1 )<= y:
                resq2 += 1
        elif ((gridw // 2) + 1) <= x:
            if 0 <= y < (gridl // 2):
                resq3 += 1
            elif ((gridl // 2) + 1 )<= y:
                resq4 += 1        

    res = resq1 * resq2 * resq3 * resq4
    print(resq1, resq2, resq3, resq4)
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
