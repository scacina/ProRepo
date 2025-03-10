import collections
import functools
import heapq
# Global variable
import sys
from itertools import combinations
G_INPUTFILENAME = "Day24.txt"


def solvepart2(matrix):
    wires = {}
    operations = []
    res = ""

    def process(op, op1, op2):
        if op == "AND":
            return op1 & op2
        elif op == "OR":
            return op1 | op2
        elif op == "XOR":
            return op1 ^ op2

    highest_z = "z00"
    data = open("Day24.txt").read().split("\n")
    for line in data:
        if ":" in line:
            wire, value = line.split(": ")
            wires[wire] = int(value)
        elif "->" in line:
            op1, op, op2, _, res = line.split(" ")
            operations.append((op1, op, op2, res))
            if res[0] == "z" and int(res[1:]) > int(highest_z[1:]):
                highest_z = res

    wrong = set()
    for op1, op, op2, res in operations:
        if res[0] == "z" and op != "XOR" and res != highest_z:
            wrong.add(res)
        if (
            op == "XOR"
            and res[0] not in ["x", "y", "z"]
            and op1[0] not in ["x", "y", "z"]
            and op2[0] not in ["x", "y", "z"]
        ):
            wrong.add(res)
        if op == "AND" and "x00" not in [op1, op2]:
            for subop1, subop, subop2, subres in operations:
                if (res == subop1 or res == subop2) and subop != "OR":
                    wrong.add(res)
        if op == "XOR":
            for subop1, subop, subop2, subres in operations:
                if (res == subop1 or res == subop2) and subop == "OR":
                    wrong.add(res)

    while len(operations):
        op1, op, op2, res = operations.pop(0)
        if op1 in wires and op2 in wires:
            wires[res] = process(op, wires[op1], wires[op2])
        else:
            operations.append((op1, op, op2, res))

    bits = [str(wires[wire]) for wire in sorted(wires, reverse=True) if wire[0] == "z"]
    res = ",".join(sorted(wrong))
    print("part 2 ended", res)


def solvehelper(key, dval, deq):
    if key in dval:
        return dval[key]
    eq = deq[key]
    eq = eq.split(" ")
    key1, op, key2 = eq[0], eq[1], eq[2]
    dval[key1]  = solvehelper(key1, dval, deq)
    dval[key2]  = solvehelper(key2, dval, deq)
    if op == 'XOR':
        dval[key] = dval[key1] ^ dval[key2]
    elif op == 'AND':
        dval[key] = dval[key1] & dval[key2]
    elif op == 'OR':
        dval[key] = dval[key1] | dval[key2]
    else:
        assert False

    return dval[key]


def solvepart1(matrix):
    res = resx = resy = ""
    dval = {}
    deq = {}
    for line in matrix:
        if len(line) == 6:
            line = line.split(': ')
            dval[line[0]] = int(line[1])
        else:
            line = line.split(" -> ")
            deq[line[1]] = line[0]
    
    for i in range(101):
        formatted_string = f"z{i:02}"  # Format the number with leading zeros
        if formatted_string in dval:
            res = str(dval[formatted_string]) + res
        elif formatted_string in deq:
            res = str(solvehelper(formatted_string, dval, deq)) + res
        else:
            break
    for i in range(len(res) - 1):
        formatted_string = f"x{i:02}"
        resx = str(dval[formatted_string]) + resx
        formatted_string = f"y{i:02}"
        resy = str(dval[formatted_string]) + resy
    print(int(res,2))    
    return print(res)

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
