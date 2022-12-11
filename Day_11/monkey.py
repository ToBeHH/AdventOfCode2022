# -*- coding: utf-8 -*-

class Monkey(object):
    def __init__(self, lines):
        self.name = lines[0].split(":")[0]
        itemsStr = lines[1].split(":")[1].split(",")
        self.items = [int(x) for x in itemsStr]
        self.operation = lines[2].split(":")[1].strip()
        self.testStr = lines[3].split(":")[1].strip()
        self.next_monkey_test = int(lines[3].split(" ")[-1])
        self.next_monkey_true = int(lines[4].split(" ")[-1])
        self.next_monkey_false = int(lines[5].split(" ")[-1])
        self.inspections = 0
        self.worryMod = 0

    def perform_operation(self, value):
        loc = {}
        exec(self.operation.replace("old", str(value)), globals(), loc)
        return loc['new']

    def catch_item(self, item):
        self.items.append(item)

    def print_items(self):
        print("%s: %s" % (self.name, ", ".join([str(item) for item in self.items])))

    def perform_operations(self, monkeys, lowWorry = True, debug = False):
        if debug:
            print("%s:" % self.name)
        while len(self.items) > 0:
            item = self.items.pop(0)
            if debug:
                print("  Monkey inspects an item with a worry level of %d." % item)
            worry_level = self.perform_operation(item)
            if debug:
                print("    Worry level after operation: %d" % worry_level)
            if lowWorry:
                worry_level = int(worry_level / 3)
            if self.worryMod:
                worry_level %= self.worryMod
            if debug:
                print("    Monkey gets bored with item. Worry level is divided by 3 to %d.", worry_level)
            test = worry_level % self.next_monkey_test == 0
            not_str = ""
            if not test:
                not_str = " not"
            if debug:
                print("    Current worry level is%s divisible by %d." % (not_str, self.next_monkey_test))
            next_monkey = self.next_monkey_false
            if test:
                next_monkey = self.next_monkey_true
            if debug:
                print("    Item with worry level %d is thrown to monkey %d." % (worry_level, next_monkey))
            monkeys[next_monkey].catch_item(worry_level)
            self.inspections = self.inspections + 1
