#!/usr/bin/env python3
# -*- coding: utf-8 -*-

file = open('input.txt', 'r')
lines = file.readlines()

overlaps = 0

# read the lines of the file
for line in lines:
    # remove new-line character
    line = line.strip()
    # parse the data
    [elve1, elve2] = line.split(",")
    [elve1minS,elve1maxS] = elve1.strip().split("-")
    [elve2minS,elve2maxS] = elve2.strip().split("-")
    elve1min = int(elve1minS.strip())
    elve1max = int(elve1maxS.strip())
    elve2min = int(elve2minS.strip())
    elve2max = int(elve2maxS.strip())

    # now do the comparison
    if (elve1min <= elve2min and elve1max >= elve2max) \
        or (elve1min >= elve2min and elve1max <= elve2max) \
        or (elve1min < elve2min and elve1max < elve2max and elve1max >= elve2min) \
        or (elve2min < elve1min and elve2max < elve1max and elve2max >= elve1min):
        overlaps = overlaps + 1

print("There are %d overlapping assignments" % overlaps)