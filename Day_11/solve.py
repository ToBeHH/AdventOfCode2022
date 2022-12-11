#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from monkey import *

FILENAME = 'input.txt'

if __name__ == "__main__":
    # read the lines of the file
    with open(FILENAME) as f:
        monkey_lines = []
        monkeys = []
        for line in f:
            line = line.strip()
            if line == "":
                monkeys.append(Monkey(monkey_lines))
                monkey_lines = []
            else:
                monkey_lines.append(line.strip())
        monkeys.append(Monkey(monkey_lines))

        for round in range(20):
            for monkey in monkeys:
                monkey.perform_operations(monkeys, False)
        inspections = [monkey.inspections for monkey in monkeys]
        inspections.sort(reverse=True)

        print("monkey business is ", inspections[0] * inspections[1])