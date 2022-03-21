from blockClass import *
# import time
checksMade = 0





def moveCheck(board_size, blocks, move, last_move):
    block = allBlocks[move[0]]
    loHiDifference = move[1]*(block.length + 1)
    xNew = block.x + (1 - block.vertical) * (loHiDifference - 1)
    yNew = block.y + block.vertical * (loHiDifference - 1)
    # if it isn't the inverse of what you just did
    if not last_move == [block.name, 0]:
        # check if touching high wall

        relevantSize = board_size[block.vertical]
        relevantHigh = block.length + [block.x, block.y][block.vertical]
        if not relevantSize == relevantHigh:
            # check if space empty
            xNew += (1-block.vertical) * (block.length + 1)
            yNew += block.vertical * (block.length + 1)
            if board.board[xNew][yNew] == '.':
                return 1
    return 0


def moves(blocks, board_size, last_cmd):
    moves = []
    for block in blocks:
        multiplier = moveCheck(board, [block.name, 0], last_cmd)
        if not multiplier == 0:
            # append to list
            moves.append([block.name, 0, multiplier])

        multiplier = moveCheck(board, [block.name, 1], last_cmd)
        if not multiplier == 0:
            # append to list
            moves.append([block.name, 1, multiplier])
    return moves


def update(board, cmd):
    block = allBlocks[cmd[0]]

    newDifference = cmd[1] * (block.length + 1) - 1
    newX = block.x + (1 - block.vertical) * newDifference
    newY = block.y + block.vertical * newDifference

    oldDifference = (1 - cmd[1]) * (block.length - 1)
    oldX = block.x + (1 - block.vertical) * oldDifference
    oldY = block.y + block.vertical * oldDifference

    board.board[newX][newY] = block.name
    board.board[oldX][oldY] = '.'

    # board.writeOut()

    blockDifference = cmd[1] * 2 - 1
    block.x += (1 - block.vertical) * blockDifference
    block.y += block.vertical * blockDifference


def multiUpdate(board, cmd_list):
    for cmd in cmd_list:
        update(board, cmd)


def freeMoveSpace(board, win_block, direction):
    space = 0
    relevantSize = direction * ((1 - win_block.vertical) * board.width + win_block.vertical * board.height)
    relevantPos = (1 - win_block.vertical) * win_block.x + win_block.vertical * win_block.y
    for i in range(relevantPos + direction * win_block.length, relevantSize, 2 * direction - 1):
        cell = board.board[(1 - win_block.vertical) * i + win_block.vertical * win_block.x]\
                       [win_block.vertical * i + (1 - win_block.vertical) * win_block.y]
        if not (cell == '.' or cell == win_block.name):
            break
        space += 1
    return space


def pathClear(board):
    block = allBlocks[board.winBlock]
    relevantPos = [block.x, block.y][block.vertical]
    relevantWinPos = (1-block.vertical)*board.winX + block.vertical*board.winY
    distToExit = relevantWinPos - relevantPos
    moveSpace = freeMoveSpace(board, block, board.winDirection)
    if moveSpace == distToExit:
        return moveSpace
    return 0
