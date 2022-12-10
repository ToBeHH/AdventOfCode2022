# -*- coding: utf-8 -*-

import unittest

from parser import *

class TestParser(unittest.TestCase):
    def test_sample(self):
        lines = ["noop", "addx 3", "addx -5"]
        self.assertEqual(run_program(lines, 7), [1,1,1,1,4,4,-1])

if __name__ == '__main__':
    unittest.main()