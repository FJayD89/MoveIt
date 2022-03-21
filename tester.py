from numpy.linalg import LinAlgError
import numpy as np
from blockClass import OptimalBlock, fromBlock
from boardClass import Board
import time
# import this
from betterSearch import *
# from textToBoard import textToBoard

ml1 = [
	['c', 2]
]

ml2 = [
	['c', 3],
	['c', -1],
]

mBlocksSetup = {
	'o': OptimalBlock(3, 1, 3, 0, 'o'),
	'p': OptimalBlock(3, 1, 0, 3, 'p'),
	'x': OptimalBlock(2, 0, 0, 2, 'x'),
	'q': OptimalBlock(3, 0, 1, 3, 'q')
}

# a = 1
# b = 0
# c = [a, b]

coefficients = np.array([
	[1,1,0,0,0],
	[1,0,1,0,0],
	[1,0,0,1,0],
	[1,0,0,0,1],
	[0,1,1,0,0],
	[0,1,0,1,0],
	[0,1,0,0,1],
	[0,0,1,1,0],
	[0,0,1,0,1],
	[0,0,0,1,1]
])

startTime = time.time()

# print(moves(mBlocksSetup, [6, 6]))

# print(block.pos[1-block.vertical])

# board = textToBoard('boards/1.txt', 'x', 0, 0)
# print(board.moves())

arr = [1,2,3]

for i in range(10):
	for cycle in range(pow(10, 6)):
		a = np.sum(np.array(arr))

	print(time.time() - startTime)
	startTime = time.time()
