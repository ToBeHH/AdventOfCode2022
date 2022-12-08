#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from helper import *

FILENAME = 'input.txt'

if __name__ == "__main__":
    # read the lines of the file
    with open(FILENAME) as f:
        forest = []
        for line in f:
            forest.append(parseInput(line))
            
        best_sconic_score = highest_scenic_score(forest)
        print("There best sconic score is", best_sconic_score)