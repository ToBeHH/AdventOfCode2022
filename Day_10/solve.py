#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from parser import *

FILENAME = 'input.txt'

if __name__ == "__main__":
    # read the lines of the file
    with open(FILENAME) as f:
        lines = []
        for line in f:
            lines.append(line.strip())
            
        cycles = run_program(lines)
        print_sprites(cycles)
        sum = sum_values(cycles)
        print("The sum is",sum)