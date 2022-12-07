#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from helper import *

FILENAME = 'input.txt'

if __name__ == "__main__":
    # read the lines of the file
    with open(FILENAME) as f:
        filetree = readLines(f)
        filetree.calculate_sizes()
        sum = filetree.sum(100000)
        print("The sum of all bigger files is", sum)