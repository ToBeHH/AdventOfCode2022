#!/usr/bin/env python3
# -*- coding: utf-8 -*-

file = open('input.txt', 'r')
lines = file.readlines()

sum_of_priorities = 0
rucksack = ['','','']
rucksack_index = 0

# read the lines of the file
for line in lines:
    # remove new-line character
    line = line.strip()
    # put them into one rucksack
    rucksack[rucksack_index] = line
    rucksack_index = rucksack_index + 1
    # are all rucksacks filled?
    if rucksack_index == 3:
        rucksack_index = 0
    
        # now find common characters in each string
        common = set(rucksack[0]).intersection(rucksack[1]).intersection(rucksack[2])
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