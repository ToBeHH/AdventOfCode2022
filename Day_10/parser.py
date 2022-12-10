# -*- coding: utf-8 -*-

def run_program(lines, max_cycles = 300):
    # init array with max_cycles cycles
    cycle_value = []
    for index in range(max_cycles):
        cycle_value.append(1)
    
    cycle_num = 0
    for line in lines:
        line = line.strip()
        cycle_num = cycle_num + 1
        if line == "noop":
            # do nothing, only advance the cycle
            continue
        line_parts = line.split(" ")

        if line_parts[0] == "addx":
            cycle_num = cycle_num + 1
            value = int(line_parts[1])
            for index in range(cycle_num + 1, max_cycles):
                cycle_value[index] = cycle_value[index] + value

    return cycle_value

def print_cycles(cycle_value):
    length = len(cycle_value)
    position = 0
    while position < length:
        print(position+1,":", end="")
        for index in range(position, position + 10):
            print("\t", cycle_value[index], end="")
        print()
        position = position + 10

def print_sprites(cycle_values):
    length = len(cycle_values)
    position = 0
    line_position = 0
    line = ""
    while position < length:
        sprite_min = cycle_values[position] - 1
        sprite_max = cycle_values[position] + 1
        if sprite_min <= line_position and line_position <= sprite_max:
            line = line + "#"
        else:
            line = line + "."
        if position % 40 == 0:
            print(line)
            line = ""
            line_position = -1
        line_position = line_position + 1
        position = position + 1
    print(line)

def sum_values(cycle_value):
    print(cycle_value[20])
    print(cycle_value[60])
    return 20 * cycle_value[20] + \
        60 * cycle_value[60] + \
        100 * cycle_value[100] + \
        140 * cycle_value[140] + \
        180 * cycle_value[180] + \
        220 * cycle_value[220] 