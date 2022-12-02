#!/usr/bin/env python3
# -*- coding: utf-8 -*-

file = open('input.txt', 'r')
lines = file.readlines()

score = 0

# read the lines of the file
for line in lines:
    # since there are only 9 possibile combinations, I write them out
    # need to add strio() to remove trailing new-line
    if line.strip() == "A X":
        # Rock vs. Rock - Draw, rock is 1 
        score = score + 1 + 3
    if line.strip() == "A Y":
        # Rock vs. Paper - I win, paper is 2
        score = score + 2 + 6
    if line.strip() == "A Z":
        # Rock vs. Scissors - I loose, scissor is 3
        score = score + 3 + 0
    if line.strip() == "B X":
        # Paper vs. Rock - I loose, rock is 1
        score = score + 1  + 0
    if line.strip() == "B Y":
        # Paper vs. Paper - Draw, paper is 2
        score = score + 2 + 3
    if line.strip() == "B Z":
        # Paper vs. Scissors - I win, scissor is 3
        score = score + 3 + 6
    if line.strip() == "C X":
        # Scissors vs. Rock - I win, rock is 1
        score = score + 1 + 6
    if line.strip() == "C Y":
        # Scissors vs. Paper - I loos, paper is 2
        score = score + 2 + 0
    if line.strip() == "C Z":
        # Scissors vs. Scissors - Draw - scissor is 3
        score = score + 3 + 3

print("The total score is %d" % score)
