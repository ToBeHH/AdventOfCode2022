#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import the methods, which have not been changed
from solve1 import *

FILENAME = 'input.txt'

if __name__ == "__main__":
    # read the lines of the file
    with open(FILENAME) as f:
        stacks = []
        stackdata = []
        for line in f:
            # parse data input
            data = parseInput(line)
            if data["type"] == "stack":
                stackdata.append(data["line"])
            if data["type"] == "separator":
                stacks = buildInitialStack(stackdata)
            if data["type"] == "move":
                # different calculation algorithm
                crates = []
                for i in range(data["howmany"]):
                    # pop last element
                    crates.append(stacks[data["from"]-1].pop(-1))
                crates.reverse()
                for crate in crates:
                    stacks[data["to"]-1].append(crate)

        print("The top elements of the stack are %s" % topOfStacks(stacks))