import collections
import typing
import copy
import sys
import string
from z3 import *

# global variables
G_INPUTFILENAME = "Day07.txt"


def can_form_target(numbers, target):
    n = len(numbers)
    # Create a Z3 Solver
    solver = Solver()

    # Create symbolic variables for operations (0 = +, 1 = *)
    ops = [Int(f'op_{i}') for i in range(n - 1)]
    for op in ops:
        solver.add(Or(op == 0, op == 1))  # Only + (0) or * (1) allowed

    # Create symbolic variables for intermediate results
    values = [Real(f'val_{i}') for i in range(n)]
    for i, num in enumerate(numbers):
        solver.add(values[i] == num)  # Fix input numbers

    # Apply operations to form expressions
    expr = values[0]
    for i in range(1, n):
        expr = If(ops[i - 1] == 0, expr + values[i], expr * values[i])

    # Add the target constraint
    solver.add(expr == target)

    # Check if the solution exists
    if solver.check() == sat:
        model = solver.model()
        return True
    else:
        return False


def can_form_target_with_concat(numbers, target):
    n = len(numbers)
    # Create a Z3 Solver
    solver = Solver()

    # Create symbolic variables for operations (0 = +, 1 = *, 2 = ||)
    ops = [Int(f'op_{i}') for i in range(n - 1)]
    for op in ops:
        solver.add(Or(op == 0, op == 1, op == 2))  # Allow +, *, or ||

    # Create symbolic variables for intermediate results
    values = [Real(f'val_{i}') for i in range(n)]
    for i, num in enumerate(numbers):
        solver.add(values[i] == num)  # Fix input numbers

    # Apply operations to form expressions
    expr = values[0]
    for i in range(1, n):
        # Calculate digit multiplier for `||` operation
        current_value = values[i]
        shift_amount = If(current_value < 10, 1,
                          If(current_value < 100, 2,
                             3))
        shifted_result = expr * (10 ** shift_amount) + current_value

        expr = If(
            ops[i - 1] == 0, expr + values[i],  # Addition
            If(
                ops[i - 1] == 1, expr * values[i],  # Multiplication
                shifted_result
            )
        )

    # Add the target constraint
    solver.add(expr == target)

    # Check if the solution exists
    if solver.check() == sat:
        model = solver.model()
        return True
    else:
        return False

def solvepart2(inlines: typing.List[str]):
    res = 0

    for line in inlines:
        line = line.split(": ")
        #print(line)
        target = int(line[0])
        inls = list(map(int, line[1].split()))
        if can_form_target_with_concat(inls, target):
            res += target
    return res

def solvepart1(inlines: typing.List[str]):
    res = 0
    resls = []
    newset = []
    for line in inlines:
        linebackup = line
        line = line.split(": ")
        #print(line)
        target = int(line[0])
        inls = list(map(int, line[1].split()))
        resls += inls
        if can_form_target(inls, target):
            res += target
        else:
            newset.append(linebackup)
    print("part 1 ended", res)
    res += solvepart2(newset)
    print("part 2 ended", res)


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
    #solvepart2(array)


if __name__ == "__main__":
    main()
