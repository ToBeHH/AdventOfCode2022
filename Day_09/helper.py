# -*- coding: utf-8 -*-

def sign(value):
    if value > 0:
        return 1
    if value < 0:
        return -1
    return 0

class Rope(object):
    "Class representing the rope"
    def __init__(self, hx = 0, hy = 0, tx = 0, ty = 0, rope_length = 2, debug = False):
        self.rope = [{"x": hx, "y": hy}]
        for i in range(1,rope_length):
            self.rope.append({"x": hx, "y": hy})
        self.rope[rope_length - 1] = {"x": tx, "y": ty}
        self.tail_visited = set() # using a set to remove duplicates
        self.max = {"x": 6, "y": 6}
        self.min = {"x": 0, "y": 0}
        self.debug = debug
        self.rope_length = rope_length

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
                self.rope[0] = {"x": self.rope[0]["x"] + 1, "y": self.rope[0]["y"]}
            if direction == "L":
                self.rope[0] = {"x": self.rope[0]["x"] - 1, "y": self.rope[0]["y"]}
            if direction == "U":
                self.rope[0] = {"x": self.rope[0]["x"], "y": self.rope[0]["y"] + 1}
            if direction == "D":
                self.rope[0] = {"x": self.rope[0]["x"], "y": self.rope[0]["y"] - 1}
            self.move_tail()
            if self.debug:
                self.print()
        if self.debug:
            self.adapt_max()      
            print()

    def move_tail(self):
        for rope_segment in range(1, self.rope_length):
            dist_x = abs(self.rope[rope_segment-1]["x"] - self.rope[rope_segment]["x"])
            dist_y = abs(self.rope[rope_segment-1]["y"] - self.rope[rope_segment]["y"])

            if dist_x >= 2 or dist_y >= 2:
                walk_x = sign(self.rope[rope_segment-1]["x"] - self.rope[rope_segment]["x"])
                walk_y = sign(self.rope[rope_segment-1]["y"] - self.rope[rope_segment]["y"])
                self.rope[rope_segment] = {"x": self.rope[rope_segment]["x"] + walk_x, "y": self.rope[rope_segment]["y"] + walk_y}
        # remember position
        self.tail_visited.add((self.rope[self.rope_length - 1]["x"], self.rope[self.rope_length - 1]["y"]))

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
        if (self.rope[0]["x"] + 2) > self.max["x"]:
            self.max["x"] = self.rope[0]["x"] + 1
        if (self.rope[0]["y"] + 2) > self.max["y"]:
            self.max["y"] = self.rope[0]["y"] + 1
        if (self.rope[0]["x"] - 2) < self.min["x"]:
            self.min["x"] = self.rope[0]["x"] - 1
        if (self.rope[0]["y"] - 2) < self.min["y"]:
            self.min["y"] = self.rope[0]["y"] - 1

    def print(self):
        for y in range(self.max["y"], self.min["y"] - 1, -1):
            for x in range(self.min["x"], self.max["x"]):
                printed = False
                for rope_segment in range(self.rope_length):
                    if self.rope[rope_segment]["x"] == x and self.rope[rope_segment]["y"] == y and not printed:
                        printed = True
                        if rope_segment == 0:
                            print("H", end = "")
                            break
                        if rope_segment == self.rope_length - 1:
                            print("T", end = "")
                            break
                        print(hex(rope_segment)[2], end="")
                        break
                if not printed:
                    if x == 0 and y == 0:
                        print("s", end = "")
                    else:
                        print(".", end = "")
            print(".")
        print()
                