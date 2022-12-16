#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from itertools import zip_longest

FILENAME = 'input.txt'


def compare(left, right):
    if left is None:
        return -1
    if right is None:
        return 1

    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1
        elif left > right:
            return 1
        else:
            return 0
    elif isinstance(left, list) and isinstance(right, list):
        for l2, r2 in zip_longest(left, right):
            if (result := compare(l2, r2)) != 0:
                return result
        return 0
    else:
        l2 = [left] if isinstance(left, int) else left
        r2 = [right] if isinstance(right, int) else right
        return compare(l2, r2)


def compare_arrays(array1, array2):
    left_side_smaller = True
    for compare_index in range(len(array1)):
        if array1[compare_index] > array2[compare_index]:
            left_side_smaller = False
    print(array1, array2, left_side_smaller)


if __name__ == "__main__":
    # read the lines of the file
    with open(FILENAME) as f:
        array1 = []
        array2 = []
        line_index = 0
        sum = 0
        pair_index = 1
        for line in f:
            if line_index == 0:
                array1 = eval(line.strip())
            if line_index == 1:
                loc = {}
                array2 = eval(line.strip())
                if compare(array1, array2) == -1:
                    sum += pair_index
            if line_index == 2:
                line_index = -1
                pair_index += 1
            line_index += 1
        print(sum)
