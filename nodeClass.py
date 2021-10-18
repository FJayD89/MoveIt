class Node:

    def __init__(self, value, index, parent = 0):
        self.parent, self.value, self.index = parent, value, index
        self.generation = parent.generation+1
        self.children = 0

    def newChild(self, value):
        return 0
