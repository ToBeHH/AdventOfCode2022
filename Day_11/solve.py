#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from monkey import *

FILENAME = 'input.txt'

def print_all_items(monkeys):
    for monkey in monkeys:
        monkey.print_items()

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

        # For Part 2:
        # no need to keep excessively high worry levels, since they'll be tested again each monkey
        # divtest value. I can keep only the reminder of the product of all monkeys' divtest values (all primes, of course!)
        worryMod = 1
        for monkey in monkeys:
            worryMod *= monkey.next_monkey_test
        for monkey in monkeys:
            monkey.worryMod = worryMod

        for round in range(10000):
            for monkey in monkeys:
                monkey.perform_operations(monkeys, lowWorry = False, debug=False)
            if round % 100 == 0:
                print(".", end="")
        inspections = [monkey.inspections for monkey in monkeys]
        inspections.sort(reverse=True)

        print("monkey business is ", inspections[0] * inspections[1])