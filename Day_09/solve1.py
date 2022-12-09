#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from helper import *

FILENAME = 'input.txt'

if __name__ == "__main__":
    # read the lines of the file
    with open(FILENAME) as f:
        rope = Rope()
        for line in f:
            rope.move_head(line)
            
        visited = rope.get_number_of_visited_positions()
        print("The rope visited", visited, "positions")