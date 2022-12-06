import unittest

from helper import *

class TestReader(unittest.TestCase):

    def test_read_lime(self):
        self.assertEqual(parseInput("line\n"), "line")

class TestAreAllDifferent(unittest.TestCase):
    def test_happy_path(self):
        # Data taken from the initial sample
        self.assertTrue(areAllDifferent("abcd"))
        self.assertFalse(areAllDifferent("abca"))
        self.assertFalse(areAllDifferent("abcb"))
        self.assertFalse(areAllDifferent("abcc"))

class TestFindMarker(unittest.TestCase):
    def test_sample1(self):
        self.assertEqual(findMarker("bvwbjplbgvbhsrlpgdmjqwftvncz", 4), 5)
        self.assertEqual(findMarker("nppdvjthqldpwncqszvftbrmjlhg", 4), 6)
        self.assertEqual(findMarker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 4), 10)
        self.assertEqual(findMarker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 4), 11)
    
    def test_sample2(self):
        self.assertEqual(findMarker("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14), 19)
        self.assertEqual(findMarker("bvwbjplbgvbhsrlpgdmjqwftvncz", 14), 23)
        self.assertEqual(findMarker("nppdvjthqldpwncqszvftbrmjlhg", 14), 23)
        self.assertEqual(findMarker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14), 29)
        self.assertEqual(findMarker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 14), 26)

if __name__ == '__main__':
    unittest.main()