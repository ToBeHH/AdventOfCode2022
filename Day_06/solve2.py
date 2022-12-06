#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from helper import *

FILENAME = 'input.txt'

if __name__ == "__main__":
    # read the lines of the file
    with open(FILENAME) as f:
        stacks = []
        stackdata = []
        for line in f:
            # parse data input
            data = parseInput(line)
            start = findMarker(data, 14)
            print("first marker after %d" % start)
            