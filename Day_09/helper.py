# -*- coding: utf-8 -*-

def sign(value):
    if value > 0:
        return 1
    if value < 0:
        return -1
    return 0

class Rope(object):
    "Class representing the rope"
    def __init__(self, hx = 0, hy = 0, tx = 0, ty = 0, debug = False):
        self.head = {"x": hx, "y": hy}
        self.tail = {"x": tx, "y": ty}
        self.tail_visited = set() # using a set to remove duplicates
        self.max = {"x": 6, "y": 6}
        self.debug = debug

    def move_head(self, line):
        # read line
        assert(len(line) >= 2)
        [direction, distanceStr] = line.split(" ")
        distance = int(distanceStr)
        if self.debug:
            print("==",line, "==")
        for step in range(distance):
            # move head
            if direction == "R":
                self.head = {"x": self.head["x"] + 1, "y": self.head["y"]}
            if direction == "L":
                self.head = {"x": self.head["x"] - 1, "y": self.head["y"]}
            if direction == "U":
                self.head = {"x": self.head["x"], "y": self.head["y"] + 1}
            if direction == "D":
                self.head = {"x": self.head["x"], "y": self.head["y"] - 1}
            self.move_tail()
            if self.debug:
                self.print()
        if self.debug:
            self.adapt_max()      
            print()

    def move_tail(self):
        dist_x = abs(self.head["x"] - self.tail["x"])
        dist_y = abs(self.head["y"] - self.tail["y"])

        if dist_x >=2 or dist_y >= 2:
            walk_x = sign(self.head["x"] - self.tail["x"])
            walk_y = sign(self.head["y"] - self.tail["y"])
            if self.debug:
                print(walk_x, walk_y)
            self.tail = {"x": self.tail["x"] + walk_x, "y": self.tail["y"] + walk_y}
        # remember position
        self.tail_visited.add((self.tail["x"], self.tail["y"]))

    def get_number_of_visited_positions(self):
        if self.debug:
            for y in range(self.max["y"], -1, -1):
                for x in range(self.max["x"]):
                    if (x,y) in self.tail_visited:
                        print("#", end="")
                    else:
                        print(".", end="")
                print()
            print(self.tail_visited)
        return len(self.tail_visited)

    def adapt_max(self):
        if (self.head["x"] + 2) > self.max["x"]:
            self.max["x"] = self.head["x"] + 1
        if (self.head["y"] + 2) > self.max["y"]:
            self.max["y"] = self.head["y"] + 1

    def print(self):
        for y in range(self.max["y"], -1, -1):
            for x in range(self.max["x"]):
                if self.head["x"] == x and self.head["y"] == y:
                    print("H", end = "")
                else:
                    if self.tail["x"] == x and self.tail["y"] == y:
                        print("T", end = "")
                    else:
                        if x == 0 and y == 0:
                            print("s", end = "")
                        else:
                            print(".", end = "")
            print(".")
        print()
                