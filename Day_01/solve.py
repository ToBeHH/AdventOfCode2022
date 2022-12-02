#!/usr/bin/env python3
# -*- coding: utf-8 -*-

file = open('input.txt', 'r')
lines = file.readlines()

# Use an array to store the calories for each elv
# This only works if there is a "small" number of elves, because of memory issues
calories = []
current = 0

# read the lines of the file
for line in lines:
    if line.strip() == "":
        calories.append(current)
        current = 0
    else:
        current = current + int(line)
    
# sort the array to get the top 3
calories.sort(reverse=True)

print("The elf carrying the top 3 caliories have %d calories" % (calories[0] + calories[1] + calories[2]))
