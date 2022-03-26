import time

from betterSearch import *
from blockClass import *
from textToBoard import textToBoard


# define win conditions here

# board = Board(6, 6, [x, o, q, p], x, 4, 2)
# board = textToBoard('boards/board.txt', 'x', 4, 2)
board = textToBoard('boards/' + input('Enter the filename: '), input('Enter the win_name: '))

board_size = board[0]
board_blocks = board[1]
board_win_name = list(board_blocks.keys())[0]
board_txt = board[2]
exit_direction = int(input('Enter the exit_direction (-1/1): '))
win_block = board_blocks[board_win_name]
board_win_pos = [0, 0]  # default
board_win_pos[1-win_block.vertical] = win_block.pos[1-win_block.vertical]
board_win_pos[win_block.vertical] = int((board_size[win_block.vertical]-win_block.length)*(1+exit_direction)/2)

gameEnded = False
maxDepth = 2  # don't change these!!!
depth = 0
moveList = []

OGpos = {}

startTime = time.time()
print(startTime)
print('Starting position:')
print(board_txt)

for block in allBlocks.values():
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
    global depth, gameEnded, moveList
    depth += 1
    if not gameEnded:
        if not depth == maxDepth:
            # generate possible moves
            for move in moves(board_blocks, last_cmd):
                # do move
                makeMove(board_blocks, move)
                moveList.append(move)
                recurse(move)
                # revert move
                makeMove(board_blocks, [move[0], 1 - move[1]])
                moveList = moveList[:-1]

        depth -= 1
        if winCheck(board_win_name, board_win_pos):
            gameEnded = True
            board.writeOut()
            print('Game won in ' + str(depth) + ' steps!')
            # print(str(checksMade) + ' checks were made')
            print(moveList)
            return 0
        distToExit = pathClear(board_blocks, board_win_name, board_size)
        if not distToExit == 0:
            gameEnded = True
            for i in range(distToExit):
                moveList.append([board_win_name, board.winDirection])
            print('Game won in ' + str(depth) + ' steps!')
            print(moveList)
            return 0


# while not gameEnded:
#     recurse('')
#     print(str(time.time()) + ' Not ' + str(maxDepth - 1))
#     maxDepth += 1

# runTime = time.time()-startTime
# print(runTime)
#
# print(freeMoveSpace(board, blocks['b'], 1))

clear = pathClear(board_blocks, 'x', board_size, 1)
moves = moves(board_blocks, board_size)
print('clear:', clear)
print('moves:', moves)
print('bwp:', board_win_pos)
