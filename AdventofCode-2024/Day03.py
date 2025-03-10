import collections
import typing
import re
import sys
import string

# global variables
G_INPUTFILENAME = "Day03.txt"


def solvepart2(inlines: typing.List[str]):
    res = 0

    # Regex pattern
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    inline = ""
    # Example string to search
    for line in inlines:
        inline += line
    inline = inline.split("do")
    for line in inline:
    # Find all matches
        if not line.startswith("n't()"):
            matches = re.findall(pattern, line)
            for x, y in matches:
                res += (int(x)*int(y))

    # Output matches
    print("part 2 ended", res)

def solvepart1(inlines: typing.List[str]):
    res = 0

    # Regex pattern
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    inline = ""
    # Example string to search
    for line in inlines:
        inline += line
    # Find all matches
    matches = re.findall(pattern, inline)
    for x, y in matches:
        res += (int(x)*int(y))

    # Output matches
    print("part 1 ended", res)


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
