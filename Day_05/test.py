import unittest

from solve1 import *

class TestReader(unittest.TestCase):

    def test_read_emptylime(self):
        self.assertEqual(parseInput(""), { "type": "separator"}, "Should be a separator")

    def test_read_graphics(self):
        self.assertEqual(parseInput(" 1   2   3 "), { "type": "stack", "line": " 1   2   3 "}, "Should be graphics line")
        self.assertEqual(parseInput("[Z] [M] [P]"), { "type": "stack", "line": "[Z] [M] [P]"}, "Should be graphics line")
        self.assertEqual(parseInput("    [D]  "), { "type": "stack", "line": "    [D]  "}, "Should be graphics line with spaces")

    def test_move(self):
        self.assertEqual(parseInput("move 1 from 2 to 3"), { "type": "move", "from": 2, "to": 3, "howmany": 1})
        self.assertEqual(parseInput("move 3 from 1 to 2"), { "type": "move", "from": 1, "to": 2, "howmany": 3})

class TestBuildInitialStack(unittest.TestCase):
    def test_happy_path(self):
        # Data taken from the initial sample
        self.assertEqual(buildInitialStack(["    [D]    ","[N] [C]    ","[Z] [M] [P]", " 1   2   3 "]), [['Z', 'N'],['M', 'C', 'D'], ['P']])

class TestMove(unittest.TestCase):
    def test_happy_path(self):
        self.assertEqual(move([['Z', 'N'],['M', 'C', 'D'], ['P']], 2, 1, 1), [['Z', 'N', 'D'],['M', 'C'], ['P']])
        self.assertEqual(move([['Z', 'N', 'D'],['M', 'C'], ['P']], 1, 3, 3), [[],['M', 'C'], ['P', 'D', 'N', 'Z']])
    
class TestBuildResult(unittest.TestCase):
    def test_happy_path(self):
        self.assertEqual(topOfStacks([['Z', 'N'],['M', 'C', 'D'], ['P']]), "NDP")

if __name__ == '__main__':
    unittest.main()