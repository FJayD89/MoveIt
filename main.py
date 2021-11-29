import time

from mainFunctions import *
from textToBoard import textToBoard


# define win conditions here
winName = ''
# board = Board(6, 6, [x, o, q, p], x, 4, 2)
# board = textToBoard('boards/board.txt', 'x', 4, 2)
board = textToBoard('boards/' + input('Enter the filename:'), 'x', 4, 2)
gameEnded = False
maxDepth = 2  # don't change these!!!
depth = 0
moveList = []

OGpos = {}

startTime = time.time()
print(startTime)
print('Starting position:')
board.writeOut()

for block in blocks.values():
    OGpos[block.name] = [block.x, block.y]


# while not cmd == 'end' and not gameEnded:
#     cmd = input(':')
#     if cmd[-1] in Board.cmds.keys():
#         if cmd[:-1] in blocks.keys():
#             board.moveBlock(blocks[cmd[:-1]], cmd[-1])
#             moveCount += 1
#             if board.winCheck():
#                 gameEnded = True
#             continue
#     if cmd == 'moves':
#         print(board.moves())
#     if not cmd == ('end' or 'moves'):
#         print("Invalid command!")
#         board.writeOut()
#
# print('You won in ' + str(moveCount) + ' moves! Good job!')

# def recurseNode(moveList):
#     for move

# def moves(moveList):
#     for block


# print(str(board.winX) + ', ' + str(board.winY) + ', ' + board.winBlock)


def recurse(last_cmd, game_board=0, game_depth=0, move_list=0, game_ended=0):
    global depth, gameEnded, moveList, maxDepth
    depth += 1
    if not gameEnded:
        if not depth == maxDepth:
            # generate possible moves
            for move in moves(board, last_cmd):
                # do move
                update(board, move)
                moveList.append(move)
                recurse(move)
                # revert move
                update(board, [move[0], 1 - move[1]])
                moveList = moveList[:-1]

        depth -= 1
        if winCheck(board):
            gameEnded = True
            board.writeOut()
            print('Game won in ' + str(depth) + ' steps!')
            print(str(checksMade) + ' checks were made')
            print(moveList)
            return 0
        distToExit = pathClear(board)
        if not distToExit == 0:
            gameEnded = True
            for i in range(distToExit):
                moveList.append([winName, board.winDirection])
            print('Game won in ' + str(depth) + ' steps!')
            print(moveList)
            return 0


while not gameEnded:
    recurse('')
    print(str(time.time()) + ' Not ' + str(maxDepth - 1))
    maxDepth += 1

# runTime = time.time()-startTime
# print(runTime)

# print(freeMoveSpace(board, blocks['b'], 1))
