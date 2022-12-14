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
        # Rock and I need to loose, so I need to choose Scissors - I loose, scissor is 3
        score = score + 3 + 0
    if line.strip() == "A Y":
        # Rock and I need to draw, so I need to choose rock - Draw, rock is 1 
        score = score + 1 + 3
    if line.strip() == "A Z":
        # Rock and I need to win, so I need to choose Paper - I win, paper is 2
        score = score + 2 + 6
    if line.strip() == "B X":
        # Paper and I need to loose, so I need to choose Rock - I loose, rock is 1
        score = score + 1  + 0
    if line.strip() == "B Y":
        # Paper and I need to draw, so I need to choose Paper - Draw, paper is 2
        score = score + 2 + 3
    if line.strip() == "B Z":
        # Paper and I need to win, so I need to choose Scissors - I win, scissor is 3
        score = score + 3 + 6
    if line.strip() == "C X":
        # Scissors and I need to loose, so I need to choose Paper - I loos, paper is 2
        score = score + 2 + 0
    if line.strip() == "C Y":
        # Scissors and I need to draw, so I need to choose Scissors - Draw - scissor is 3
        score = score + 3 + 3
    if line.strip() == "C Z":
        # Scissors and I need to win, so I need to choose Rock - I win, rock is 1
        score = score + 1 + 6

print("The total score is %d" % score)
