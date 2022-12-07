#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from helper import *

FILENAME = 'input.txt'

if __name__ == "__main__":
    # read the lines of the file
    with open(FILENAME) as f:
        filetree = readLines(f)
        filetree.calculate_sizes()
        free_space = 70000000 - filetree.file_sizes
        print("Free space is ", free_space)
        dirs = filetree.add_directory_bigger_than(30000000 - free_space)
        dirs.sort()
        print("The size of the best directory to delete is ", dirs[0])