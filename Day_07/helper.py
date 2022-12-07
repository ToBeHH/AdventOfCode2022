# -*- coding: utf-8 -*-

class Node(object):
    "Generic directory node"
    def __init__(self, name='/', children=None):
        self.name = name
        self.children = []
        self.files = []
        self.file_sizes = 0
        if children is not None:
            for child in children:
                self.add_child(child)
    def __repr__(self):
        return self.printTree(0)
    def printTree(self, level = 0):
        levelstr = ""
        for i in range(level):
            levelstr = levelstr + "  "
        name = levelstr + self.name + " [" + str(self.file_sizes) + "]\n"
        for child in self.children:
            name = name + child.printTree(level + 1)
        return name
    def add_child(self, node):
        assert isinstance(node, Node)
        self.children.append(node)
    def go_to(self, names):
        if len(names) == 0:
            return self
        for child in self.children:
            if child.name == names[0]:
                return child.go_to(names[1:])
        self.children.append(Node(names[0]))
        return self.children[-1].go_to(names[1:])
    def add_file(self, filename, filesize):
        self.files.append({"name": filename, "size": filesize})
    def calculate_sizes(self):
        sum = 0
        for file in self.files:
            sum = sum + file["size"]
        for child in self.children:
            sum = sum + child.calculate_sizes()            
        self.file_sizes = sum
        return sum
    def sum(self, threshold, currentsum = 0):
        sum = currentsum
        for child in self.children:
            if child.file_sizes <= threshold:
                sum = sum + child.file_sizes
            sum = child.sum(threshold, sum)
        return sum
    def add_directory_bigger_than(self, threshold):
        data = []
        if self.file_sizes >= threshold:
            data.append(self.file_sizes)
        for child in self.children:
            childdata = child.add_directory_bigger_than(threshold)
            data = data + childdata
        return data

def readLines(file):
    '''Read the file line by line and build a directory structure
    '''
    filetree = Node('/')
    currentDir = []
    for line in file:
        line = line.strip()
        if line[0:4] == '$ cd':
            dir = line[5:]
            if dir == "/":
                currentDir = []
            else:
                if dir == "..":
                    currentDir.pop()
                else:
                    currentDir.append(dir)
        if line[0:2] == "ls":
            # can be ignored, dirs are created with dir
            pass
        if line[0:3] == "dir":
            # append directory to current filetree
            filetree.go_to(currentDir).add_child(Node(line[4:]))
        if line[0] >= "0" and line[0] <= "9":
            [filesizeS, filename] = line.split(' ')
            filetree.go_to(currentDir).add_file(filename, int(filesizeS))
    return filetree
