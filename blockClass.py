allBlocks = {}


class Block:
	def __init__(self, w, h, x, y, name):
		self.height, self.width, self.x, self.y, self.name = h, w, x, y, name
		allBlocks[self.name] = self
		if self.height > self.width:
			self.vertical = 1
		else:
			self.vertical = 0


class OptimalBlock:
	def __init__(self, length, vertical, x, y, name):
		self.length, self.vertical, self.x, self.y, self.name = length, vertical, x, y, name
		allBlocks[self.name] = self
		self.pos = [self.x, self.y]

	def __repr__(self):
		return '[ ' + str(self.length) + \
				', ' + str(self.vertical) + \
				', ' + str(self.x) + \
				', ' + str(self.y) + \
				', ' + str(self.name) + ' ]'

	def attributes(self):
		return [
			# self.length,
			# self.vertical,
			self.x,
			self.y,
			# self.name
		]

	def __eq__(self, other):
		return self.attributes() == other.attributes()


def fromBlock(optimal_block):
	return OptimalBlock(
		optimal_block.length,
		optimal_block.vertical,
		optimal_block.x,
		optimal_block.y,
		optimal_block.name
	)
