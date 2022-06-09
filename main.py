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
board_win_pos = int((board_size[win_block.vertical]-win_block.length)*(1+exit_direction)/2)

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


def recurse(last_move):
    global depth, gameEnded, moveList, board_blocks
    depth += 1
    if not gameEnded:

        if winCheck(board_blocks, board_win_name, board_win_pos, exit_direction):
            gameEnded = True
            boardWriteOut(board_blocks)
            win_block = board_blocks[board_win_name]
            if not win_block.pos[win_block.vertical] == board_win_pos:
                moveList.append([board_win_name, board_win_pos - win_block.pos[win_block.vertical]])

            print('Game won in ' + str(depth) + ' steps!')
            # print(str(checksMade) + ' checks were made')
            print(moveList)
            return 0

        if not depth == maxDepth:
            # generate possible moves
            for move in moves(board_blocks, board_size, last_move):
                # do move - actually changes board_blocks apparently
                makeMove(move, board_blocks)
                moveList.append(move)
                if recurse(move):
                    return True
                # revert move
                makeMove([move[0], -move[1]], board_blocks)
                moveList = moveList[:-1]

        depth -= 1

    pass


while not gameEnded:
    recurse([1, 0])
    print(str(time.time() - startTime) + ' Not ' + str(maxDepth))
    maxDepth += 1

# clear = pathClear(board_blocks, 'h', board_size, -1)
# print('clear:', clear)

# moves = moves(board_blocks, board_size, ['null', 0])
# print('moves:', moves)
# print('bwp:', board_win_pos)
