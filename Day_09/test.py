import unittest

from helper import *

class TestRope(unittest.TestCase):
    def test_move_tail(self):
        rope = Rope(4, 1, 3, 0, debug=True)
        rope.print()
        rope.move_head("U 1")
        self.assertEqual(rope.rope[1], {"x": 4, "y": 1})

    def test_sample(self):
        rope = Rope(debug=True)
        rope.move_head("R 4")
        rope.move_head("U 4")
        rope.move_head("L 3")
        rope.move_head("D 1")
        rope.move_head("R 4")
        rope.move_head("D 1")
        rope.move_head("L 5")
        rope.move_head("R 2")
        self.assertEqual(rope.get_number_of_visited_positions(), 13)
    
    def test_negative_space(self):
        rope = Rope(-10,-10,-10,-10,debug=True)
        rope.move_head("R 4")
        rope.move_head("U 4")
        rope.move_head("L 3")
        rope.move_head("D 1")
        rope.move_head("R 4")
        rope.move_head("D 1")
        rope.move_head("L 5")
        rope.move_head("R 2")
        self.assertEqual(rope.get_number_of_visited_positions(), 13)

    def test_sample2(self):
        rope = Rope(rope_length = 10, debug=True)
        rope.move_head("R 5")
        rope.move_head("U 8")
        rope.move_head("L 8")
        rope.move_head("D 3")
        rope.move_head("R 17")
        rope.move_head("D 10")
        rope.move_head("L 25")
        rope.move_head("U 20")
        self.assertEqual(rope.get_number_of_visited_positions(), 36)
    

if __name__ == '__main__':
    unittest.main()