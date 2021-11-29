blocks = {}


class Block:
    def __init__(self, w, h, x, y, name):
        self.height, self.width, self.x, self.y, self.name = h, w, x, y, name
        blocks[self.name] = self
        if self.height > self.width:
            self.vertical = 1
        else:
            self.vertical = 0


class OptimalBlock:
    def __init__(self, length, vertical, x, y, name):
        self.length, self.vertical, self.x, self.y, self.name = length, vertical, x, y, name
        blocks[self.name] = self


def fromBlock():
    return None