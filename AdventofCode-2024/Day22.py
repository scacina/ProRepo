import collections
import functools
# Global variable
G_INPUTFILENAME = "Day22.txt"

@functools.lru_cache(maxsize=None)
def prunenumber(innum):
    return innum & 0x0FFFFFF

@functools.lru_cache(maxsize=None)
def mixnumber(innum, mixval):
    return innum ^ mixval

def gettuple(prices, index):
    return (
        prices[index - 3] - prices[index - 4],
        prices[index - 2] - prices[index - 3],
        prices[index - 1] - prices[index - 2],
        prices[index] - prices[index - 1]
    )

def solvepart2(matrix):
    # Step 1: Prepare the grid with sequences
    grid = []
    for line in matrix:
        secret = int(line)
        sequence = []
        for _ in range(2000):
            secret = mixnumber(secret, secret << 6)
            secret = prunenumber(secret)
            secret = mixnumber(secret, secret >> 5)
            secret = prunenumber(secret)
            secret = mixnumber(secret, secret << 11)
            secret = prunenumber(secret)
            sequence.append(secret % 10)
        grid.append(sequence)

    # Step 2: Build target sequences and their occurrences
    griddic = collections.Counter()
    for prices in grid:
        setfound = set()
        for j in range(4, len(prices)):
            targetseq = gettuple(prices, j)
            if targetseq not in setfound:
                griddic[targetseq] += prices[j]
                setfound.add(targetseq)

    # Step 3: Find the maximum result
    res = max(griddic.values())
    
    print("Part 2 ended. Result:", res)
    return res

def solvepart1(matrix):
    res = 0
    for line in matrix:
        secret = int(line)
        for i in range(2000):

            secret = mixnumber(secret, secret << 6)
            secret = prunenumber(secret)

            secret = mixnumber(secret, secret >> 5)
            secret = prunenumber(secret)

            secret = mixnumber(secret, secret << 11)
            secret = prunenumber(secret)
        res += secret
    print("part 1 ended", res)
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
