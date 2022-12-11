# -*- coding: utf-8 -*-

import unittest

from monkey import *


class TestMonkey(unittest.TestCase):
    def test_init(self):
        lines = ["Monkey 0:",
                 "   Starting items: 79, 98",
                 "   Operation: new = old * 19",
                 "   Test: divisible by 23",
                 "     If true: throw to monkey 2",
                 "     If false: throw to monkey 3"]
        monkey = Monkey(lines)
        self.assertEqual(monkey.items, [79, 98])
        self.assertEqual(monkey.operation, "new = old * 19")
        self.assertEqual(monkey.perform_operation(2), 38)
        self.assertEqual(monkey.next_monkey_test, 23)
        self.assertEqual(monkey.next_monkey_true, 2)
        self.assertEqual(monkey.next_monkey_false, 3)


if __name__ == '__main__':
    unittest.main()
