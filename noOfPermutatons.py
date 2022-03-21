from textToBoard import textToBoard

myBoard = textToBoard("boards/board.txt", 'a', 3, 1)
cars = []
carsPlaced = 0
# def noOfPermutations(board):
# 	blocksUsed = 0
# 	while blocksUsed < len(myBoard.blocks):
# 		myBoard.blocks[blocksUsed].x =


def placeCar(board, car):
	global carsPlaced, cars

	rightmost = car.vertical*(car.length - 1) + 1
	if not rightmost == board.width:
		for
		placeCar(board, cars[carsPlaced], 0)

	for

	if not board.blockCheck(car):
		return


def permutaions(board):
	global cars, carsPlaced
	cars = board.allBlocks
	board.allBlocks = []
	foundPositions = 0
	carsPlaced = 0
	placeCar(board, cars[0])


	return foundPositions

