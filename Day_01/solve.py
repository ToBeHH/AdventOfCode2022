#!/usr/bin/env python3
# -*- coding: utf-8 -*-

file = open('input.txt', 'r')
lines = file.readlines()

max = 0
current = 0

for line in lines:
    if line.strip() == "":
        if current >= max:
            max = current
        current = 0
    else:
        current = current + int(line)
    
print("The elf carrying most caliories has %d calories" % max)
