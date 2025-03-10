from z3 import *
import re
import copy
from queue import PriorityQueue
import collections
# global variables
G_INPUTFILENAME = "Day17.txt"
from functools import lru_cache
from z3 import *
import winsound

def solvepart2(matrix):
    res = 0
    winsound.Beep(1500, 500)
    program = [2, 4, 1, 5, 7, 5, 0, 3, 4, 0, 1, 6, 5, 5, 3, 0]
    opt = Optimize()
    s = BitVec('s', 64)
    a, b, c = s, 0, 0
    opt.add(s > 0)
    for x in program:
        b = a & 7  # Extract the least significant 3 bits of a
        b = b ^ 5  # XOR with 5 (binary 101)
        c = a >> b # Bit shift right by b
        a = a >> 3 # Right shift by 3 bits
        b = b ^ c  # XOR b with c
        b = b ^ 6  # XOR with 6 (binary 110)
        opt.add((b & 7) == x)  # Constraint: the least significant 3 bits of b should equal x
    opt.add(a == 0)  # Constraint: a must be 0 at the end
    opt.minimize(s)  # Find the solution with the smallest possible s

    if opt.check() == sat:
        model = opt.model()
        #print(model.eval(s))
        res = model.eval(s).as_long()
    else:
        print("No solution found")
    winsound.Beep(1500, 500)
    print("Part 2 ended. Result:", res)

def get_combo_value(operand, registers):
  """Calculates the value of a combo operand."""
  if 0 <= operand <= 3:
    return operand
  elif operand == 4:
    return registers['A']
  elif operand == 5:
    return registers['B']
  elif operand == 6:
    return registers['C']
  else:
    raise ValueError("Invalid combo operand: 7")


def solvepart1(aval):
    """Executes a program and returns the output."""
    registers = {'A': aval, 'B': 0, 'C': 0}
    instruction_pointer = 0
    output = []
    program = [2,4,1,5,7,5,0,3,4,0,1,6,5,5,3,0]

    while instruction_pointer < len(program):
        instruction = program[instruction_pointer]
        opcode = program[instruction_pointer]
        operand = program[instruction_pointer + 1]
        instruction_pointer += 2

        operand_val = get_combo_value(operand, registers)

        if opcode == 0:  # adv
            denominator = 2**operand_val
            registers['A'] = registers['A'] // denominator
        elif opcode == 1:  # bxl
            registers['B'] = registers['B'] ^ operand
        elif opcode == 2:  # bst
            registers['B'] = operand_val % 8
        elif opcode == 3:  # jnz
            if registers['A'] != 0:
                instruction_pointer = operand
                continue  # Skip the instruction pointer increment
        elif opcode == 4:  # bxc
            registers['B'] = registers['B'] ^ registers['C']
        elif opcode == 5:  # out
            output.append(operand_val % 8)
        elif opcode == 6:  # bdv
            denominator = 2**operand_val
            registers['B'] = registers['A'] // denominator
        elif opcode == 7:  # cdv
            denominator = 2**operand_val
            registers['C'] = registers['A'] // denominator
    print(",".join([str(el) for el in output]))
    return int("".join([str(el) for el in output]))

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
    solvepart1(46187030)
    solvepart2(array)


if __name__ == "__main__":
    main()
