#!/usr/bin/env python3
# -*- coding: utf-8 -*-

file = open('input.txt', 'r')
lines = file.readlines()

sum_of_priorities = 0

# read the lines of the file
for line in lines:
    # remove new-line character
    line = line.strip()
    # find center
    half = int(len(line)/2)
    # build two compartments
    first_compartment = line[:half]
    second_compartment = line[half:]
    
    # now find common characters in each string
    common = set(first_compartment).intersection(second_compartment)
    for common_character in common:
        # get the priority for each character
        if common_character.islower():
            # we use the ascii value to determine the priority
            priority = ord(common_character) - ord('a') + 1
        else:
            # we use the ascii value to determine the priority
            priority = ord(common_character) - ord('A') + 27
        # sum them up
        sum_of_priorities = sum_of_priorities + priority

print("The sum of the priorities is %d" % sum_of_priorities)