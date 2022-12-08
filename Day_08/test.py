import unittest

from helper import *

class TestReader(unittest.TestCase):

    def test_read_lime(self):
        self.assertEqual(parseInput("123"), [1, 2, 3])

class TesVisibility(unittest.TestCase):
    forest = [[3, 0, 3, 7, 3], 
                [2, 5, 5, 1, 2],
                [6, 5, 3, 3, 2],
                [3, 3, 5, 4, 9],
                [3, 5 ,3 ,9, 0]]
                
    def test_happy_path(self):
        self.assertTrue(is_tree_visible(self.forest, 0, 0))
        self.assertTrue(is_tree_visible(self.forest, 1, 1))
        self.assertTrue(is_tree_visible(self.forest, 2, 1))
        self.assertFalse(is_tree_visible(self.forest, 3, 1))
        self.assertTrue(is_tree_visible(self.forest, 1, 2))
        self.assertFalse(is_tree_visible(self.forest, 2, 2))
        self.assertTrue(is_tree_visible(self.forest, 3, 2))
        self.assertFalse(is_tree_visible(self.forest, 1, 3))
        self.assertTrue(is_tree_visible(self.forest, 2, 3))
        self.assertFalse(is_tree_visible(self.forest, 3, 3))

    def test_count(self):
        self.assertEqual(count_visible_trees(self.forest), 21)

    def test_scenic_score(self):
        self.assertEqual(scenic_score(self.forest, 2, 1), 4)
        self.assertEqual(scenic_score(self.forest, 2, 3), 8)

    def test_max(self):
        self.assertEqual(highest_scenic_score(self.forest), 8)

if __name__ == '__main__':
    unittest.main()