#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import cmp_to_key
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
        packets = []
        line_index = 0
        sum = 0
        pair_index = 1
        for line in f:
            if line_index == 0:
                packets.append(eval(line.strip()))
            if line_index == 1:
                loc = {}
                packets.append(eval(line.strip()))
            if line_index == 2:
                line_index = -1
                pair_index += 1
            line_index += 1

        div1, div2 = [[2]], [[6]]
        sorted_packets = sorted([*packets, div1, div2], key=cmp_to_key(compare))
        print((sorted_packets.index(div1) + 1) * (sorted_packets.index(div2) + 1))
