# -*- coding: utf-8 -*-

def parseInput(line: str):
    '''parse the input format for one line

    separated into separate function for easier testablity
    
    Parameters
    ----------
    line : str
        The line read from the input file

    Returns
    -------
    data
        an array with the heights as integers
    '''
    l = line.strip()
    parsed = []
    for char in l:
        parsed.append(int(char))
    return parsed

def is_tree_visible(forest, x, y):
    if x == 0 or y == 0:
        return True
    if x == len(forest[0]) or y == len(forest):
        return True
    height = forest[y][x]
    # look left
    visible_left = True
    for x_pos in range(x):
        if forest[y][x_pos] >= height:
            visible_left = False
            break
    
    visibile_right = True
    for x_pos in range(x+1, len(forest[0])):
        if forest[y][x_pos] >= height:
            visibile_right = False
            break
    
    visible_top = True
    for y_pos in range(y):
        if forest[y_pos][x] >= height:
            visible_top = False
            break
    
    visible_bottom = True
    for y_pos in range(y+1, len(forest)):
        if forest[y_pos][x] >= height:
            visible_bottom = False
            break

    return visible_left or visibile_right or visible_top or visible_bottom

def scenic_score(forest, x, y):
    # the outside scenic score is always 0, because one viewing distance is 0 and 
    # in the end the data is multiplied
    if x == 0 or y == 0:
        return 0
    if x == len(forest[0]) or y == len(forest):
        return 0
    height = forest[y][x]
    # look left
    visible_left = 0
    for x_pos in range(x-1, -1, -1):
        visible_left = visible_left + 1
        if forest[y][x_pos] >= height:
            break
    
    visibile_right = 0
    for x_pos in range(x+1, len(forest[0])):
        visibile_right = visibile_right + 1
        if forest[y][x_pos] >= height:
            break
    
    visible_top = 0
    for y_pos in range(y-1, -1, -1):
        visible_top = visible_top + 1
        if forest[y_pos][x] >= height:
            break
    
    visible_bottom = 0
    for y_pos in range(y+1, len(forest)):
        visible_bottom = visible_bottom + 1
        if forest[y_pos][x] >= height:
            break
        
    return visible_left * visibile_right * visible_top * visible_bottom

def count_visible_trees(forest):
    count = 0
    for x in range(len(forest[0])):
        for y in range(len(forest)):
            if is_tree_visible(forest, x, y):
                count = count + 1
    return count

def highest_scenic_score(forest):
    maximum = 0
    for x in range(len(forest[0])):
        for y in range(len(forest)):
            maximum = max(maximum, scenic_score(forest, x, y))
    return maximum