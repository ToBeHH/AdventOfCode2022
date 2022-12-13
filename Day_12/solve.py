#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import curses

FILENAME = 'input.txt'

stdscr = curses.initscr()
curses.noecho()


def read_file(file):
    grid = []
    for line in file:
        line = line.strip()
        grid.append(line)
    return grid


def find_pos(grid, elevation):
    '''Return all positions in the grid with the given elevation'''
    positions = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == elevation:
                positions.append((x, y))
    return positions


def get_elevation(grid, x, y):
    if x < 0 or y < 0:
        return None
    if x >= len(grid[0]) or y >= len(grid):
        return None
    return grid[y][x]


def find_adjacent_pos(grid, current_pos, elevations):
    positions = []
    x = current_pos[0]
    y = current_pos[1]
    elev = get_elevation(grid, x - 1, y)
    if elev is not None and elev in elevations:
        positions.append((x - 1, y))
    elev = get_elevation(grid, x + 1, y)
    if elev is not None and elev in elevations:
        positions.append((x + 1, y))
    elev = get_elevation(grid, x, y - 1)
    if elev is not None and elev in elevations:
        positions.append((x, y - 1))
    elev = get_elevation(grid, x, y + 1)
    if elev is not None and elev in elevations:
        positions.append((x, y + 1))
    return positions


def traverse(grid, current_pos, steps):
    visited = []
    paths = [[current_pos]]
    solutions = []

    while len(paths):
        path = paths.pop(0)
        current_pos = path[-1]
        current_elevation = get_elevation(grid, current_pos[0], current_pos[1])
        steps_index = steps.index(current_elevation)
        possible_elevations = steps[1: (steps_index + 2)]  # Why start at a? Not in the description

        for i in range(len(grid)):
            stdscr.addstr(i, 0, grid[i], curses.A_DIM | curses.color_pair(1))
        for f in paths:
            for p in f:
                stdscr.addstr(p[1], p[0], "X", curses.color_pair(3))
        for p in path:
            stdscr.addstr(p[1], p[0], "X", curses.color_pair(2))
        stdscr.addstr(len(grid) + 2, 0, "Buchstabe: %s, Länge: %d" % (current_elevation, len(path)),
                      curses.color_pair(1))

        # Find out all possible next positions
        possible_next_pos = find_adjacent_pos(grid, current_pos, possible_elevations)

        for p in possible_next_pos:
            stdscr.addstr(p[1], p[0], "?", curses.color_pair(4))

        stdscr.refresh()
        for a in possible_next_pos:
            if a not in path and a not in visited:
                newpath = list(path)
                newpath.append(a)
                xa, ya = a
                if grid[ya][xa] == 'E':
                    stdscr.addstr(len(grid) + 4, 0, "Done!")
                    stdscr.refresh()
                    solutions.append(newpath)
                else:
                    paths.append(newpath)
                    visited.append(a)

    if len(solutions) == 0:
        stdscr.addstr(len(grid) + 4, 0, "NO PATH FOUND!!!")
        stdscr.refresh()
        return []
    else:
        # return shortes solution
        solutions.sort(key=len)
        return solutions[0]


if __name__ == "__main__":
    # Clear screen
    stdscr.clear()
    curses.cbreak()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    # read the lines of the file
    with open(FILENAME) as f:
        grid = read_file(f)
        path = traverse(grid, find_pos(grid, "S")[0], "SabcdefghijklmnopqrstuvwxyzE")  # [::-1])

        stdscr.getkey()
        curses.endwin()
        # We need to remove start and end point
        print("We took", len(path) - 3, "steps")
